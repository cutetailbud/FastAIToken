"""Generate the multilingual READMEs.

Usage (from the repo root):
    python scripts/readme/gen.py .

Edit data.py for prices, extra.py for the exchange rate, i18n.py / extra.py for wording.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import *
from i18n import T, ORDER
from extra import E, RATE, disc, pct

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
    a(table([t["c_group"], t["c_mult"], t["c_disc"]], [[n, f"{m}x", D(m)] for n, m in [
        (G["oai_welfare"], 0.06), (G["oai_std"], 0.2), (G["oai_backup"], 0.25), (G["oai_pro"], 0.3),
        (G["oai_ent"], 0.5), (G["cl_max"], 1.5), (G["cl_ent"], 1.9), (t["gem"], 0.3), (t["cn"], 1), (t["vid"], 1)]]))

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
    a("### DeepSeek\n")
    a(f"> {t['ds_peak']}\n")
    a(table([t["c_model"], t["c_in"], t["c_out"], t["c_cr"]],
            [[code(m) + (f"<br><sub>{t['same']}: {s}</sub>" if s else ""), d(i), d(o), d(r)]
             for m, s, i, o, r in DEEPSEEK]))
    a(f"### {t['glm_title']}\n")
    cond = {"lt": t["in_lt32"], "ge": t["in_ge32"], None: "—"}
    a(table([t["c_model"], t["c_cond"], t["c_in"], t["c_out"], t["c_cr"]],
            [[code(m), cond[c], d(i), d(o), d(r)] for m, c, i, o, r in GLM], "lcrrr"))
    a(f"### {t['kimi_title']}\n")
    a(table([t["c_model"], t["c_in"], t["c_out"], t["c_cw"], t["c_cr"]], [
        [code("kimi-k3"), "$19.00", "$95.00", "—", "$1.90"],
        [code("kimi-k3.1-pro"), "$13.00", "$68.00", f"$13.00<br><sub>{t['h1']}: $26.00</sub>", "$1.30"],
    ]))
    a(f"### {t['doubao_title']}\n")
    a(table([t["c_model"], t["c_in"], t["c_out"], t["c_cr"]], [
        [code("doubao-seed-2-1-pro") + f"<br><sub>{t['same']}: doubao-seed-2-1-pro-260915</sub>",
         "$6.00", "$30.00", "$1.20"],
    ]))

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


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "."
    for c in ORDER:
        with open(os.path.join(out, FILES[c]), "w", encoding="utf-8", newline="\n") as f:
            f.write(render(c))
        print("wrote", FILES[c])
