"""Checks for the README generator and pricing data. Run: python -m unittest discover -s tests"""
import json
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts", "readme"))

import data  # noqa: E402
import gen  # noqa: E402
from extra import E  # noqa: E402
from i18n import ORDER, T  # noqa: E402


def pairs(rows, start):
    for r in rows:
        for cell in r[start:]:
            if cell != "-":
                yield r[0], cell


class PriceMath(unittest.TestCase):
    """Discounted price shown in the README must equal list price x group multiplier."""

    def check(self, rows, start, mult):
        for model, cell in pairs(rows, start):
            paid, listed = (float(x) for x in cell.split("/"))
            self.assertAlmostEqual(paid, listed * mult, places=6,
                                   msg=f"{model}: {cell} is not list x {mult}")

    def test_openai_pro_line(self):
        self.check(data.OAI, 2, 0.3)

    def test_claude_max(self):
        self.check(data.CLAUDE, 2, 1.5)

    def test_gemini(self):
        self.check(data.GEMINI, 1, 0.3)

    def test_cn_models_compare_with_official_cny_price(self):
        """CN models are priced in CNY: no exchange rate, every row has an official CNY price to compare with."""
        for m, c, *_ in gen.cn_rows():
            self.assertIn((m, c), data.OFFICIAL_CNY, f"{m} ({c}) has no official CNY price")
        self.assertEqual(len(gen.cn_rows()), len(data.OFFICIAL_CNY))
        lo, hi = gen.cn_span()
        self.assertTrue(0 < lo <= hi <= 1, (lo, hi))


class Translations(unittest.TestCase):
    def test_every_language_has_every_key(self):
        base_t, base_e = set(T["zh"]), set(E["zh"])
        for lc in ORDER:
            with self.subTest(lang=lc):
                self.assertEqual(set(T[lc]), base_t)
                self.assertEqual(set(E[lc]), base_e)
                self.assertEqual(set(T[lc]["g"]), set(T["zh"]["g"]))
                self.assertEqual(len(T[lc]["adv"]), len(T["zh"]["adv"]))

    def test_qq_label_for_every_language(self):
        self.assertEqual(set(gen.QQ_LABEL), set(ORDER))


class GeneratedFiles(unittest.TestCase):
    def test_committed_files_are_up_to_date(self):
        for name, content in gen.build().items():
            with self.subTest(file=name):
                with open(os.path.join(ROOT, name), encoding="utf-8") as f:
                    self.assertEqual(f.read().replace("\r\n", "\n"), content,
                                     f"{name} is stale; run python scripts/readme/gen.py .")

    def test_readmes_link_every_language(self):
        for lc in ORDER:
            text = gen.render(lc)
            for other in ORDER:
                if other != lc:
                    self.assertIn(f"./{gen.FILES[other]}", text)

    def test_pricing_json_is_valid(self):
        p = json.loads(gen.build()["pricing.json"])
        self.assertEqual(p["website"], gen.URL)
        self.assertTrue(p["models"])
        for m in p["models"]:
            self.assertIn("model", m)
            self.assertIn("unit", m)


class Wiki(unittest.TestCase):
    def setUp(self):
        import wiki
        self.wiki = wiki
        self.pages = wiki.pages()
        self.names = {os.path.basename(p)[:-3] for p in self.pages}

    def test_every_page_is_rendered_and_in_sidebar(self):
        sidebar = self.pages["wiki/_Sidebar.md"]
        for name, _, _ in self.wiki.PAGES:
            with self.subTest(page=name):
                self.assertIn(f"wiki/{name}.md", self.pages)
                self.assertIn(f"]({name})", sidebar)

    def test_internal_links_resolve(self):
        import re
        for path, text in self.pages.items():
            for target in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", text):
                if "://" in target or target.startswith("mailto:"):
                    continue
                with self.subTest(page=path, link=target):
                    self.assertIn(target, self.names)

    def test_no_hard_coded_keys(self):
        for path, text in self.pages.items():
            with self.subTest(page=path):
                self.assertNotRegex(text, r"sk-[A-Za-z0-9]{8,}")

    def test_every_model_is_listed(self):
        text = self.pages["wiki/Models-and-Pricing.md"]
        for rows in (data.OAI, data.CLAUDE, data.GEMINI, data.DEEPSEEK, data.GLM):
            for r in rows:
                self.assertIn(f"`{r[0]}`", text)
        for r in data.VIDEO_SEC + data.VIDEO_TOK:
            self.assertIn(r[1], text)


if __name__ == "__main__":
    unittest.main()
