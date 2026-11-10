import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import *
from i18n import T, ORDER
from extra import E, RATE, disc, pct

URL = "https://www.fastaitoken.com/"
FILES = {c: ("README.md" if c == "zh" else f"README.{c}.md") for c in ORDER}


def pp(s):
    if s == "-":
        return "—"
    a, b = s.split("/")
    return f"${a} (${b})"


def d(s):
    return "—" if s == "-" else f"${s}"


def row(cells):
    return "| " + " | ".join(cells) + " |"


def table(head, rows):
    out = [row(head), row(["---"] * len(head))]
    out += [row(r) for r in rows]
    return "\n".join(out)


def render(code):
    t = dict(T[code]); t.update(E[code])
    D = lambda m: disc(code, m)
    L = []
    a = L.append
    a('<p align="center">\n  <a href="https://www.fastaitoken.com/"><img src="./sponsor-fastai.png" alt="FastAIToken" width="600"></a>\n</p>\n')
    sw = " | ".join(
        f"**{T[c]['lang']}**" if c == code else f"[{T[c]['lang']}](./{FILES[c]})" for c in ORDER
    )
    a(f'<p align="center">\n\n{sw}\n\n</p>\n')
    a("# FastAIToken\n")
    a(f"> {t['tagline']} —— **[{URL}]({URL})**\n")
    a(t["intro"] + "\n")

    a(f"## ✨ {t['adv_title']}\n")
    for e, s in zip("💱🧠🎬🧾🏢🔀", t["adv"]):
        a(f"- {e} {s}")
    a("")

    a(f"## 🧮 {t['billing_title']}\n")
    a(f"**{t['formula']}**\n")
    a(t["units_note"] + "\n")
    a(t["disc_explain"].format(rate=RATE, ex_pct=pct(0.3), ex_zhe=f"{0.3 / RATE * 10:.2f} 折") + "\n")
    G0 = t["g"]
    a(f"### {t['sum_title']}\n")
    a(table([t["c_group"], t["c_mult"], t["c_disc"]], [[n, f"{m}x", D(m)] for n, m in [
        (G0["oai_welfare"], 0.06), (G0["oai_std"], 0.2), (G0["oai_backup"], 0.25), (G0["oai_pro"], 0.3),
        (G0["oai_ent"], 0.5), (G0["cl_max"], 1.5), (G0["cl_ent"], 1.9), (t["gem"], 0.3), (t["cn"], 1), (t["vid"], 1)]]) + "\n")
    a("---\n")

    G = t["g"]
    gh = [t["c_group"], t["c_mult"], t["c_disc"], t["c_tags"]]
    tg = t["tag"]

    # OpenAI
    a("## 🤖 OpenAI ChatGPT\n")
    a(t["oai_desc"] + "\n")
    a(table(gh, [
        [G["oai_welfare"], "0.06x", D(0.06), f"{tg['lowest']} · {tg['limited']}"],
        [G["oai_std"], "0.2x", D(0.2), tg["limited"]],
        [G["oai_backup"], "0.25x", D(0.25), tg["limited"]],
        [G["oai_pro"], "0.3x", D(0.3), tg["limited"]],
        [G["oai_ent"], "0.5x", D(0.5), f"{tg['exclusive']} · SLA"],
    ]) + "\n")
    a(f"> {t['luna_note']}\n")
    a(t["rate_note"].format(g=G["oai_pro"], x="0.3x") + "\n")
    a(table([t["c_model"], t["c_ctx"], t["c_in"], t["c_out"], t["c_cw"], t["c_cr"]],
            [[m, c, pp(i), pp(o), pp(w), pp(r)] for m, c, i, o, w, r in OAI]) + "\n")
    a("---\n")

    # Claude
    a("## 🟠 Claude Max (Anthropic)\n")
    a(t["claude_desc"] + "\n")
    a(table(gh, [
        [G["cl_max"], "1.5x", D(1.5), tg["lowest"]],
        [G["cl_ent"], "1.9x", D(1.9), f"{tg['exclusive']} · SLA"],
    ]) + "\n")
    a(t["rate_note"].format(g=G["cl_max"], x="1.5x") + "\n")
    a(table([t["c_model"], t["c_same"], t["c_in"], t["c_out"], t["c_cw"], t["c_cr"]],
            [[m, s, pp(i), pp(o), pp(w), pp(r)] for m, s, i, o, w, r in CLAUDE]) + "\n")
    a(f"> {t['claude_1h']}\n")
    a("---\n")

    # Gemini
    a("## 🔷 Gemini (Google)\n")
    a(t["gemini_desc"] + "\n")
    a(table([t["c_model"], t["c_in"], t["c_out"], t["c_cr"]],
            [[m, pp(i), pp(o), pp(r)] for m, i, o, r in GEMINI]) + "\n")
    a("---\n")

    # Chinese models
    a(f"## 🇨🇳 {t['cn_title']}\n")
    a(t["cn_desc"] + "\n")
    a("### DeepSeek\n")
    a(f"> ⏰ {t['ds_peak']}\n")
    a(table([t["c_model"], t["c_in"], t["c_out"], t["c_cr"]],
            [[m + (f" ({t['same']}: {s})" if s else ""), d(i), d(o), d(r)] for m, s, i, o, r in DEEPSEEK]) + "\n")
    a(f"### {t['glm_title']}\n")
    cond = {"lt": t["in_lt32"], "ge": t["in_ge32"], None: "—"}
    a(table([t["c_model"], t["c_cond"], t["c_in"], t["c_out"], t["c_cr"]],
            [[m, cond[c], d(i), d(o), d(r)] for m, c, i, o, r in GLM]) + "\n")
    a(f"### {t['kimi_title']}\n")
    a(table([t["c_model"], t["c_in"], t["c_out"], t["c_cw"], t["c_cr"]], [
        ["kimi-k3", "$19.00", "$95.00", "—", "$1.90"],
        ["kimi-k3.1-pro", "$13.00", "$68.00", f"$13.00 ({t['h1']}: $26.00)", "$1.30"],
    ]) + "\n")
    a(f"### {t['doubao_title']}\n")
    a(table([t["c_model"], t["c_in"], t["c_out"], t["c_cr"]], [
        [f"doubao-seed-2-1-pro ({t['same']}: doubao-seed-2-1-pro-260915)", "$6.00", "$30.00", "$1.20"],
    ]) + "\n")
    a("---\n")

    # Video
    a(f"## 🎬 {t['video_title']}\n")
    a(t["video_desc"] + "\n")
    a(f"### {t['per_sec']}\n")
    a(table([t["c_model"], t["c_mid"], t["c_default"], "480p", "720p", "768p", "1080p", "2K", "4K"],
            [[n, mid] + [d(x) for x in xs] for n, mid, *xs in VIDEO_SEC]) + "\n")
    a(f"### {t['per_tok']}\n")
    a(t["tok_format"] + "\n")

    def rn(s):
        if s == "-":
            return "—"
        x, y = s.split("/")
        return f"${x} / ${y}"
    a(table([t["c_model"], t["c_mid"], "480p", "720p", "1080p", "4K"],
            [[n, mid] + [rn(x) for x in xs] for n, mid, *xs in VIDEO_TOK]) + "\n")
    a("---\n")

    # Quick start
    a(f"## 🚀 {t['qs_title']}\n")
    for i, s in enumerate(t["qs"], 1):
        a(f"{i}. " + s.format(url=f"[{URL}]({URL})"))
    a("")
    a("```python\nfrom openai import OpenAI\n\nclient = OpenAI(\n"
      f"    api_key=\"sk-xxxxxxxx\",  # {t['code_key']}\n"
      f"    base_url=\"{t['code_base']}\",\n)\n\n"
      "resp = client.chat.completions.create(\n    model=\"gpt-5.5\",\n"
      f"    messages=[{{\"role\": \"user\", \"content\": \"{t['code_hello']}\"}}],\n)\n"
      "print(resp.choices[0].message.content)\n```\n")

    a(f"## 🧾 {t['inv_title']}\n")
    for s in t["inv"]:
        a(f"- {s}")
    a("")
    a(f"## 📮 {t['contact_title']}\n")
    a(f"{t['website']}: [{URL}]({URL})\n")
    a("---\n")
    a(f"> {t['disclaimer']}")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    out = sys.argv[1]
    for c in ORDER:
        with open(os.path.join(out, FILES[c]), "w", encoding="utf-8", newline="\n") as f:
            f.write(render(c))
        print("wrote", FILES[c])
