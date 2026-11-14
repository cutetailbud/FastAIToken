"""Generate the multilingual READMEs, pricing.json and the wiki pages (wiki/).

Usage (from the repo root):
    python scripts/readme/gen.py .

Edit data.py for prices, extra.py for the exchange rate, i18n.py / extra.py for wording.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import *
from i18n import T, ORDER
from extra import E, RATE, cn_range, disc, pct, ratio

URL = "https://www.fastaitoken.com/"
QQ_GROUP = "1019537221"
QQ_LABEL = {
    "zh": "QQ 交流群", "en": "QQ Group", "ja": "QQ グループ", "ko": "QQ 그룹", "ru": "Группа в QQ",
    "kk": "QQ тобы", "vi": "Nhóm QQ", "th": "กลุ่ม QQ", "id": "Grup QQ", "ms": "Kumpulan QQ",
}
FILES = {c: ("README.md" if c == "zh" else f"README.{c}.md") for c in ORDER}


def pp(s):
    """discounted (list) pair"""
    if s == "-":
        return "—"
    a, b = s.split("/")
    return f"${a} <sub>(${b})</sub>"


def d(s):
    return "—" if s == "-" else f"${s}"


def code(s):
    return f"`{s}`"


def row(cells):
    return "| " + " | ".join(cells) + " |"


def table(head, rows, align=None):
    """align: string of 'l' / 'r' / 'c' per column; default first column left, others right."""
    align = align or ("l" + "r" * (len(head) - 1))
    sep = {"l": ":---", "r": "---:", "c": ":---:"}
    out = [row(head), row([sep[x] for x in align])]
    out += [row(r) for r in rows]
    return "\n".join(out) + "\n"


def cn_rows():
    """(model, cond, in, out, cache read) for every Chinese model row, in table order."""
    rows = [(m, None, i, o, r) for m, _, _, i, o, _, r in DEEPSEEK]
    rows += [(m, c, i, o, r) for m, c, i, o, _, r in GLM]
    rows += [(m, None, i, o, r) for m, i, o, _, _, r in KIMI]
    rows += [(m, None, i, o, r) for m, _, i, o, _, r in DOUBAO]
    return rows


def cn_ratios(m, c, i, o, r):
    """{'input', 'output', 'cache_read'}: list price / official CNY price (cache read omitted if unknown)."""
    oi, oo, orr = OFFICIAL_CNY[(m, c)]
    out = dict(input=float(i) / float(oi), output=float(o) / float(oo))
    if orr is not None and r != "-":
        out["cache_read"] = float(r) / float(orr)
    return {k: round(v, 4) for k, v in out.items()}


def cn_span():
    """(lowest, highest) output-price ratio over all Chinese models."""
    xs = [cn_ratios(*x)["output"] for x in cn_rows()]
    return min(xs), max(xs)


def cn_disc(lc, t, m, c, i, o, r):
    x = cn_ratios(m, c, i, o, r)
    if len(set(x.values())) == 1:
        return ratio(lc, x["output"])
    name = dict(input=t["c_in"], output=t["c_out"], cache_read=t["c_cr"])
    return "<br>".join(f"{name[k]} {ratio(lc, v)}" for k, v in x.items())


def render(lc):
    t = dict(T[lc]); t.update(E[lc])
    D = lambda m: disc(lc, m)
    G = t["g"]
    tg = t["tag"]
    L = []
    a = L.append

    # ---------- header ----------
    langs = " · ".join(
        f"<b>{T[c]['lang']}</b>" if c == lc else f'<a href="./{FILES[c]}">{T[c]["lang"]}</a>' for c in ORDER
    )
    a('<div align="center">\n')
    a(f'<a href="{URL}"><img src="./sponsor-fastai.png" alt="FastAIToken" width="560"></a>\n')
    a(f"<p><b>{t['tagline']}</b></p>\n")
    a(f'<p><a href="{URL}">{t["website"]}</a> &nbsp;|&nbsp; {QQ_LABEL[lc]}: <b>{QQ_GROUP}</b></p>\n')
    a(f"<p><sub>{langs}</sub></p>\n")
    repo = "https://github.com/cutetailbud/FastAIToken"
    badges = [
        (f"{repo}/actions/workflows/ci.yml", f"{repo}/actions/workflows/ci.yml/badge.svg", "CI"),
        (f"{repo}/releases", "https://img.shields.io/github/v/release/cutetailbud/FastAIToken", "Release"),
        ("./LICENSE", "https://img.shields.io/github/license/cutetailbud/FastAIToken", "License"),
        ("./pricing.json", "https://img.shields.io/badge/pricing-JSON-blue", "pricing.json"),
    ]
    a("<p>\n" + "\n".join(f'  <a href="{h}"><img src="{s}" alt="{n}"></a>' for h, s, n in badges) + "\n</p>\n")
    a("</div>\n")
    a("<br>\n")
    a(t["intro"] + "\n")

    # ---------- highlights ----------
    a(f"## {t['adv_title']}\n")
    for s in t["adv"]:
        a(f"- {s}")
    a("")

    # ---------- billing ----------
    a(f"## {t['billing_title']}\n")
    a(f"```\n{t['formula']}\n```\n")
    a(t["units_note"] + "\n")
    a(t["disc_explain"].replace("💡 ", "").format(
        rate=RATE, ex_pct=pct(0.3), ex_zhe=f"{0.3 / RATE * 10:.2f} 折") + "\n")
    a(f"### {t['sum_title']}\n")
    cn_cell = cn_range(lc, *cn_span())
    a(table([t["c_group"], t["c_mult"], t["c_disc"]], [[n, f"{m}x", cn_cell if r is None else disc(lc, m, r)] for n, m, r in [
        (G["oai_welfare"], 0.06, RATE), (G["oai_std"], 0.2, RATE), (G["oai_backup"], 0.25, RATE),
        (G["oai_pro"], 0.3, RATE), (G["oai_ent"], 0.5, RATE), (G["cl_max"], 1.5, RATE), (G["cl_ent"], 1.9, RATE),
        (t["gem"], 0.3, RATE), (t["cn"], 1, None), (t["vid"], 1, RATE)]]))

    gh = [t["c_group"], t["c_mult"], t["c_disc"], t["c_tags"]]
    ga = "lrrl"

    # ---------- OpenAI ----------
    a("## OpenAI\n")
    a(t["oai_desc"] + "\n")
    a(table(gh, [
        [G["oai_welfare"], "0.06x", D(0.06), f"{tg['lowest']} · {tg['limited']}"],
        [G["oai_std"], "0.2x", D(0.2), tg["limited"]],
        [G["oai_backup"], "0.25x", D(0.25), tg["limited"]],
        [G["oai_pro"], "0.3x", D(0.3), tg["limited"]],
        [G["oai_ent"], "0.5x", D(0.5), f"{tg['exclusive']} · SLA"],
    ], ga))
    a(t["rate_note"].format(g=G["oai_pro"], x="0.3x") + "\n")
    a(table([t["c_model"], t["c_ctx"], t["c_in"], t["c_out"], t["c_cw"], t["c_cr"]],
            [[code(m), c, pp(i), pp(o), pp(w), pp(r)] for m, c, i, o, w, r in OAI], "lcrrrr"))
    a(f"> {t['luna_note']}\n")

    # ---------- Claude ----------
    a("## Claude (Anthropic)\n")
    a(t["claude_desc"] + "\n")
    a(table(gh, [
        [G["cl_max"], "1.5x", D(1.5), tg["lowest"]],
        [G["cl_ent"], "1.9x", D(1.9), f"{tg['exclusive']} · SLA"],
    ], ga))
    a(t["rate_note"].format(g=G["cl_max"], x="1.5x") + "\n")
    a(table([t["c_model"], t["c_same"], t["c_in"], t["c_out"], t["c_cw"], t["c_cr"]],
            [[code(m), s if s == "—" else code(s), pp(i), pp(o), pp(w), pp(r)] for m, s, i, o, w, r in CLAUDE],
            "llrrrr"))
    a(f"> {t['claude_1h']}\n")

    # ---------- Gemini ----------
    a("## Gemini (Google)\n")
    a(t["gemini_desc"] + "\n")
    a(table([t["c_model"], t["c_in"], t["c_out"], t["c_cr"]],
            [[code(m), pp(i), pp(o), pp(r)] for m, i, o, r in GEMINI]))

    # ---------- Chinese models ----------
    a(f"## {t['cn_title']}\n")
    a(t["cn_desc"] + "\n")
    a(t["cn_fx"].format(date=OFFICIAL_AS_OF) + "\n")
    a("### DeepSeek\n")
    colon = "：" if lc in ("zh", "ja") else ": "
    a(f"> {t['ds_peak']}{colon}" + ", ".join(code(m) for m, _, pk, *_ in DEEPSEEK if pk) + "\n")
    cnh = [t["c_model"], t["c_in"], t["c_out"], t["c_cw"], t["c_cr"], t["c_disc"]]
    a(table(cnh,
            [[code(m) + (f"<br><sub>{t['same']}: {s}</sub>" if s else ""), d(i), d(o), d(w), d(r),
              cn_disc(lc, t, m, None, i, o, r)] for m, s, _, i, o, w, r in DEEPSEEK]))
    a(f"### {t['glm_title']}\n")
    cond = {"lt": t["in_lt32"], "ge": t["in_ge32"], None: "—"}
    a(table(cnh[:1] + [t["c_cond"]] + cnh[1:],
            [[code(m), cond[c], d(i), d(o), d(w), d(r), cn_disc(lc, t, m, c, i, o, r)]
             for m, c, i, o, w, r in GLM], "lcrrrrr"))
    a(f"### {t['kimi_title']}\n")
    a(table(cnh,
            [[code(m), d(i), d(o), d(w) + f"<br><sub>{t['h1']}: {d(w1)}</sub>", d(r),
              cn_disc(lc, t, m, None, i, o, r)] for m, i, o, w, w1, r in KIMI]))
    a(f"### {t['doubao_title']}\n")
    a(table(cnh,
            [[code(m) + (f"<br><sub>{t['same']}: {s}</sub>" if s else ""), d(i), d(o), d(w), d(r),
              cn_disc(lc, t, m, None, i, o, r)] for m, s, i, o, w, r in DOUBAO]))

    # ---------- Video ----------
    a(f"## {t['video_title']}\n")
    a(t["video_desc"] + "\n")
    a(f"### {t['per_sec']}\n")
    a(table([t["c_model"], t["c_default"], "480p", "720p", "768p", "1080p", "2K", "4K"],
            [[f"{n}<br><sub>{mid}</sub>"] + [d(x) for x in xs] for n, mid, *xs in VIDEO_SEC]))
    a(f"### {t['per_tok']}\n")
    a(t["tok_format"] + "\n")

    def rn(s):
        if s == "-":
            return "—"
        x, y = s.split("/")
        return f"${x} / ${y}"
    a(table([t["c_model"], "480p", "720p", "1080p", "4K"],
            [[f"{n}<br><sub>{mid}</sub>"] + [rn(x) for x in xs] for n, mid, *xs in VIDEO_TOK]))

    # ---------- Quick start ----------
    a(f"## {t['qs_title']}\n")
    for i, s in enumerate(t["qs"], 1):
        a(f"{i}. " + s.format(url=f"[{URL}]({URL})"))
    a("")
    a("```python\nfrom openai import OpenAI\n\nclient = OpenAI(\n"
      f"    api_key=\"sk-xxxxxxxx\",  # {t['code_key']}\n"
      f"    base_url=\"{t['code_base']}\",\n)\n\n"
      "resp = client.chat.completions.create(\n    model=\"gpt-5.5\",\n"
      f"    messages=[{{\"role\": \"user\", \"content\": \"{t['code_hello']}\"}}],\n)\n"
      "print(resp.choices[0].message.content)\n```\n")
    a("[examples/](./examples) · [pricing.json](./pricing.json) · [CHANGELOG](./CHANGELOG.md) · "
      "[CONTRIBUTING](./CONTRIBUTING.md) · [SECURITY](./SECURITY.md) · [SUPPORT](./SUPPORT.md)\n")

    # ---------- Invoices / contact ----------
    a(f"## {t['inv_title']}\n")
    for s in t["inv"]:
        a(f"- {s}")
    a("")
    a(f"## {t['contact_title']}\n")
    a(f"- {t['website']}: [{URL}]({URL})")
    a(f"- {QQ_LABEL[lc]}: **{QQ_GROUP}**\n")
    a("---\n")
    a(f"<sub>{t['disclaimer']}</sub>")
    return "\n".join(L) + "\n"


def _num(s):
    return None if s == "-" else float(s)


def _pair(s):
    """'discounted/list' -> list price (float) or None"""
    return None if s == "-" else float(s.split("/")[1])


def pricing():
    """Machine-readable pricing (list prices, USD). Price paid = list price x group multiplier."""
    groups = [
        dict(id="openai-welfare", provider="openai", multiplier=0.06, tags=["lowest", "limited"]),
        dict(id="openai-standard", provider="openai", multiplier=0.2, tags=["limited"]),
        dict(id="openai-backup", provider="openai", multiplier=0.25, tags=["limited"]),
        dict(id="openai-pro", provider="openai", multiplier=0.3, tags=["limited"]),
        dict(id="openai-pro-enterprise", provider="openai", multiplier=0.5, tags=["exclusive", "sla"]),
        dict(id="claude-max", provider="anthropic", multiplier=1.5, tags=["lowest"]),
        dict(id="claude-max-enterprise", provider="anthropic", multiplier=1.9, tags=["exclusive", "sla"]),
        dict(id="gemini-chat-coding", provider="google", multiplier=0.3, tags=[]),
        dict(id="cn-models", provider="cn", multiplier=1, tags=["dynamic-discount"]),
        dict(id="video", provider="video", multiplier=1, tags=[]),
    ]
    for g in groups:
        g["vs_official_price"] = round(g["multiplier"] / RATE, 4)
        if g["id"] == "cn-models":  # priced in CNY: compared per model with the official CNY price
            g["vs_official_price"] = None
            g["vs_official_price_range"] = list(cn_span())

    def tok(model, provider, inp, out, cw, cr, **kw):
        return dict(model=model, provider=provider, unit="USD/1M tokens",
                    input=inp, output=out, cache_write=cw, cache_read=cr, **kw)

    models = []
    for m, c, i, o, w, r in OAI:
        for name in m.split(" / ") if " / " in m else [m]:
            name = name if name.startswith("gpt-") else "gpt-5.6-" + name
            models.append(tok(name, "openai", _pair(i), _pair(o), _pair(w), _pair(r),
                              context=None if c == "—" else c))
    for m, s, i, o, w, r in CLAUDE:
        models.append(tok(m, "anthropic", _pair(i), _pair(o), _pair(w), _pair(r),
                          same_price=[] if s == "—" else [x.strip() for x in s.split("/")]))
    for m, i, o, r in GEMINI:
        models.append(tok(m, "google", _pair(i), _pair(o), None, _pair(r)))
    def aliases(s):
        return [x.strip() for x in s.split(",")] if s else []

    for m, s, pk, i, o, w, r in DEEPSEEK:
        models.append(tok(m, "deepseek" if m.startswith("deepseek") else "tencent",
                          _num(i), _num(o), _num(w), _num(r), same_price=aliases(s),
                          peak="weekdays 09:00-12:00, 14:00-18:00 GMT+8 x2" if pk else None))
    for m, c, i, o, w, r in GLM:
        models.append(tok(m, "zhipu", _num(i), _num(o), _num(w), _num(r),
                          condition={"lt": "input<32K", "ge": "input>=32K"}.get(c)))
    for m, i, o, w, w1, r in KIMI:
        models.append(tok(m, "moonshot", _num(i), _num(o), _num(w), _num(r), cache_write_1h=_num(w1)))
    for m, s, i, o, w, r in DOUBAO:
        models.append(tok(m, "bytedance", _num(i), _num(o), _num(w), _num(r), same_price=aliases(s)))
    for x in models:
        for key in OFFICIAL_CNY:
            if key[0] == x["model"] and (key[1] is None or x.get("condition") ==
                                         {"lt": "input<32K", "ge": "input>=32K"}[key[1]]):
                oi, oo, orr = OFFICIAL_CNY[key]
                x["official_cny"] = dict(input=float(oi), output=float(oo), cache_read=_num(orr or "-"))
                x["vs_official"] = cn_ratios(key[0], key[1], x["input"], x["output"],
                                             "-" if x["cache_read"] is None else x["cache_read"])
    res = ["default", "480p", "720p", "768p", "1080p", "2k", "4k"]
    for n, mid, *xs in VIDEO_SEC:
        models.append(dict(model=mid.split(",")[0].strip(), name=n, provider="video", unit="USD/second",
                           prices={k: _num(v) for k, v in zip(res, xs, strict=True) if v != "-"}))
    for n, mid, *xs in VIDEO_TOK:
        p = {}
        for k, v in zip(["480p", "720p", "1080p", "4k"], xs, strict=True):
            if v != "-":
                ref, noref = v.split("/")
                p[k] = dict(with_reference=float(ref), without_reference=float(noref))
        models.append(dict(model=mid, name=n, provider="video", unit="USD/1M tokens", prices=p))
    return dict(
        website=URL,
        note="List prices in USD. Price paid = list price x group multiplier. 1 CNY buys 1 USD of credit. "
             "Chinese models are priced in CNY, so there is no exchange-rate gap: official_cny and vs_official "
             "(list price / official CNY price) are given per model. Live prices on the website prevail.",
        assumed_usd_cny=RATE,
        groups=groups,
        models=models,
    )


def build():
    """Return {relative path: file content} for every generated file."""
    import json
    files = {FILES[c]: render(c) for c in ORDER}
    files["pricing.json"] = json.dumps(pricing(), ensure_ascii=False, indent=2) + "\n"
    from wiki import pages
    files.update(pages())
    return files


if __name__ == "__main__":
    pos = [x for x in sys.argv[1:] if not x.startswith("--")]
    out = pos[0] if pos else "."
    check = "--check" in sys.argv
    stale = []
    for name, content in build().items():
        path = os.path.join(out, name)
        if check:
            try:
                with open(path, encoding="utf-8") as f:
                    if f.read().replace("\r\n", "\n") != content:
                        stale.append(name)
            except FileNotFoundError:
                stale.append(name)
            continue
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print("wrote", name)
    if check:
        if stale:
            print("Out of date, run `python scripts/readme/gen.py .`:", ", ".join(stale))
            sys.exit(1)
        print("All generated files are up to date.")
