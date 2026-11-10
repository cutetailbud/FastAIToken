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


if __name__ == "__main__":
    unittest.main()
