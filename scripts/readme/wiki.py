"""Generate the GitHub Wiki pages (bilingual: 简体中文 + English) into wiki/.

Called from gen.build(); the publish workflow (.github/workflows/wiki.yml) copies wiki/ to the
repository's GitHub Wiki. Page links use wiki page names (file name without .md).
"""
import gen as g
from data import CLAUDE, DEEPSEEK, DOUBAO, GEMINI, GLM, KIMI, OAI, VIDEO_SEC, VIDEO_TOK
from data import OFFICIAL_AS_OF as OFFICIAL
from extra import E, RATE, cn_range, disc, pct
from i18n import T

REPO = "https://github.com/cutetailbud/FastAIToken"
BLOB = f"{REPO}/blob/master"
LOGO = "https://raw.githubusercontent.com/cutetailbud/FastAIToken/master/sponsor-fastai.png"

# (page name, 中文标题, English title) -- order is the sidebar order
PAGES = [
    ("Home", "首页", "Home"),
    ("Quick-Start", "快速开始", "Quick Start"),
    ("Billing", "计费说明", "Billing"),
    ("Models-and-Pricing", "模型与价格", "Models and Pricing"),
    ("Pricing-JSON", "pricing.json 说明", "pricing.json reference"),
    ("Invoices-and-Enterprise", "发票与企业合作", "Invoices and Enterprise"),
    ("FAQ", "常见问题", "FAQ"),
    ("Contributing", "参与贡献", "Contributing"),
]
TITLE = {p: f"{zh} / {en}" for p, zh, en in PAGES}


def link(page):
    return f"[{TITLE[page]}]({page})"


def bi(zh, en):
    """A bilingual paragraph: Chinese line, then English line."""
    return f"{zh}\n{en}\n"


def item(zh, en):
    """A bilingual bullet."""
    return f"- {zh}<br>{en}"


def head(page):
    return f"# {TITLE[page]}\n"


def gdisc(gid, m):
    """'vs. official' cell for a group (zh): CN models are compared per model with the official CNY price."""
    return cn_range("zh", *g.cn_span()) if gid == "cn-models" else disc("zh", m)


def groups():
    """(zh name, en name, multiplier, pricing.json id) for every group."""
    zh, en = dict(T["zh"]["g"]), dict(T["en"]["g"])
    for k in ("gem", "cn", "vid"):
        zh[k], en[k] = E["zh"][k], E["en"][k]
    keys = ["oai_welfare", "oai_std", "oai_backup", "oai_pro", "oai_ent", "cl_max", "cl_ent", "gem", "cn", "vid"]
    ids = g.pricing()["groups"]
    assert len(ids) == len(keys)
    return [(zh[k], en[k], x["multiplier"], x["id"]) for k, x in zip(keys, ids, strict=True)]


# ---------------------------------------------------------------- pages

def home():
    L = [
        '<div align="center">\n',
        f'<a href="{g.URL}"><img src="{LOGO}" alt="FastAIToken" width="480"></a>\n',
        f"<p><b>{T['zh']['tagline']} · {T['en']['tagline']}</b></p>\n",
        "</div>\n",
        bi(T["zh"]["intro"], T["en"]["intro"]),
        "## 从这里开始 / Start here\n",
        g.table(["页面 Page", "内容 What you will find"], [
            [link("Quick-Start"), "注册、充值、创建 Key、第一次调用 / Sign up, top up, create a key, first request"],
            [link("Billing"), "计费公式、分组倍率、相当于官方价几折 / Formula, group multipliers, effective discount"],
            [link("Models-and-Pricing"), "全部模型与价格表 / Every model and its price"],
            [link("Pricing-JSON"), "机器可读价格数据的字段说明 / Field reference for the machine-readable prices"],
            [link("Invoices-and-Enterprise"), "开票、企业 SLA、对公打款 / Invoices, enterprise SLA, corporate transfer"],
            [link("FAQ"), "常见问题与报错排查 / Common questions and troubleshooting"],
            [link("Contributing"), "如何修改本文档 / How to change these docs"],
        ], "ll"),
        "## 一句话了解 / In short\n",
        "- **1 元 = 1 美元额度** / **1 CNY = 1 USD of credit**",
        f"- `{T['zh']['formula']}` / `{T['en']['formula']}`",
        "- 兼容 OpenAI 接口，可直接使用官方 OpenAI SDK / OpenAI-compatible: the official OpenAI SDKs work as-is",
        f"- 官网 Website: [{g.URL}]({g.URL}) · QQ 交流群 QQ group: **{g.QQ_GROUP}**\n",
        bi(f"其他语言的完整价格表见仓库 [README]({REPO}#readme)。",
           f"Full price tables in 10 languages are in the repository [README]({REPO}#readme)."),
    ]
    return "\n".join(L)


def quick_start():
    zh, en = T["zh"]["qs"], T["en"]["qs"]
    url = f"[{g.URL}]({g.URL})"
    L = [head("Quick-Start"), "## 1. 开通账号 / Get an API key\n"]
    L += [f"{i}. {a.format(url=url)}<br>{b.format(url=url)}" for i, (a, b) in enumerate(zip(zh, en, strict=True), 1)]
    L += [
        "",
        bi("不同分组价格与稳定性不同，选择方法见 " + link("Billing") + "。",
           "Groups differ in price and stability; see " + link("Billing") + " for how to choose."),
        "## 2. 配置环境变量 / Set environment variables\n",
        bi("仓库中的示例统一从环境变量读取配置，请勿把 Key 写进代码或提交到仓库。",
           "All examples read their settings from environment variables. Never hard-code a key or commit it."),
        g.table(["变量 Variable", "说明 Description"], [
            ["`FASTAITOKEN_API_KEY`", "控制台创建的 API Key / API key from the console"],
            ["`FASTAITOKEN_BASE_URL`", "控制台显示的 Base URL / Base URL shown in the console"],
            ["`FASTAITOKEN_MODEL`", "可选，默认 `gpt-5.5` / Optional, defaults to `gpt-5.5`"],
        ], "ll"),
        "```bash\nexport FASTAITOKEN_API_KEY=sk-...\nexport FASTAITOKEN_BASE_URL=...   # 从控制台复制 / copy from the console\n```\n",
        "## 3. 发起请求 / Make a request\n",
        "### Python\n",
        "```python\nimport os\nfrom openai import OpenAI\n\n"
        "client = OpenAI(\n    api_key=os.environ[\"FASTAITOKEN_API_KEY\"],\n"
        "    base_url=os.environ[\"FASTAITOKEN_BASE_URL\"],\n)\n\n"
        "resp = client.chat.completions.create(\n    model=\"gpt-5.5\",\n"
        "    messages=[{\"role\": \"user\", \"content\": \"你好！Hello!\"}],\n)\n"
        "print(resp.choices[0].message.content)\n```\n",
        "### Node.js\n",
        "```js\nimport OpenAI from \"openai\";\n\n"
        "const client = new OpenAI({\n  apiKey: process.env.FASTAITOKEN_API_KEY,\n"
        "  baseURL: process.env.FASTAITOKEN_BASE_URL,\n});\n\n"
        "const resp = await client.chat.completions.create({\n  model: \"gpt-5.5\",\n"
        "  messages: [{ role: \"user\", content: \"你好！Hello!\" }],\n});\n"
        "console.log(resp.choices[0].message.content);\n```\n",
        "### curl\n",
        "```bash\ncurl -sS \"${FASTAITOKEN_BASE_URL%/}/chat/completions\" \\\n"
        "  -H \"Authorization: Bearer ${FASTAITOKEN_API_KEY}\" \\\n"
        "  -H \"Content-Type: application/json\" \\\n"
        "  -d '{\"model\": \"gpt-5.5\", \"messages\": [{\"role\": \"user\", \"content\": \"Hello!\"}]}'\n```\n",
        bi(f"完整可运行的示例（含流式输出）见 [examples/]({REPO}/tree/master/examples)。",
           f"Complete runnable examples (with streaming) are in [examples/]({REPO}/tree/master/examples)."),
        "## 4. 在其他工具中使用 / Use it in other tools\n",
        bi("任何支持「OpenAI 兼容接口」或可自定义 Base URL 的客户端、SDK、编程工具都可以接入：填入控制台的 Base URL 与 API Key，"
           "模型名使用 " + link("Models-and-Pricing") + " 中的模型 ID 即可。",
           "Any client, SDK or coding tool that supports an OpenAI-compatible API or a custom base URL works: enter the "
           "console's base URL and your API key, and use a model ID from " + link("Models-and-Pricing") + "."),
        bi("官方 OpenAI SDK 也会读取 `OPENAI_API_KEY` 与 `OPENAI_BASE_URL` 环境变量。",
           "The official OpenAI SDKs also read the `OPENAI_API_KEY` and `OPENAI_BASE_URL` environment variables."),
        "```bash\nexport OPENAI_API_KEY=\"$FASTAITOKEN_API_KEY\"\nexport OPENAI_BASE_URL=\"$FASTAITOKEN_BASE_URL\"\n```\n",
        bi("遇到报错请看 " + link("FAQ") + "。", "Hitting errors? See " + link("FAQ") + "."),
    ]
    return "\n".join(L)


def billing():
    L = [
        head("Billing"),
        "## 计费公式 / Formula\n",
        f"```\n{T['zh']['formula']}\n{T['en']['formula']}\n```\n",
        bi("价格单位为 **美元 / 每 1M tokens**，视频按秒计费的为 **美元 / 秒**。价格可能随时调整，**请以官网实时价格为准**。",
           "Prices are in **USD per 1M tokens**, or **USD per second** for per-second video. Prices may change at any "
           "time; **the live prices on the website prevail**."),
        "## 相当于官方价几折 / Compared with official prices\n",
        bi(f"官方按美元计价，而本平台 **1 元 = 1 美元额度**。按 1 美元 ≈ {RATE} 元估算，"
           f"**实际人民币成本 ≈ 官方价 × 倍率 ÷ {RATE}**。",
           f"Official prices are in USD, but here **1 CNY buys 1 USD of credit**. Assuming 1 USD ≈ {RATE} CNY, "
           f"**actual cost ≈ official price × multiplier ÷ {RATE}**."),
        bi(f"例如官方价 $10 的请求，在 0.3x 分组扣除 $3 额度，即 3 元人民币，约为官方价（{10 * RATE:.0f} 元）的 {pct(0.3)}。",
           f"E.g. a request costing $10 at official prices uses $3 of credit in a 0.3x group, which is 3 CNY, "
           f"about {pct(0.3)} of the official {10 * RATE:.0f} CNY."),
        bi(E["zh"]["cn_fx"].format(date=OFFICIAL), E["en"]["cn_fx"].format(date=OFFICIAL)),
        "## 分组 / Groups\n",
        g.table(["分组", "Group", "倍率 Multiplier", "相当于官方价 vs. official", "`pricing.json` id"],
                [[zh, en, f"{m}x", gdisc(i, m), f"`{i}`"] for zh, en, m, i in groups()], "llrrl"),
        "### 如何选择分组 / Choosing a group\n",
        item("**倍率越低越便宜**。标注「限时」的分组价格可能调整或下线。",
             "**Lower multiplier = cheaper.** Groups tagged *limited-time* may change or be withdrawn."),
        item("**企业线路**（OpenAI Pro 企业线路、Claude Max 企业线路）为专属分组，提供 SLA 保障，适合生产环境。",
             "**Enterprise lines** (OpenAI Pro Enterprise, Claude Max Enterprise) are dedicated and come with an SLA; "
             "use them in production."),
        item("同一模型可在多个分组中使用；可以为不同用途创建不同分组的 Key。",
             "The same model is available in several groups; create separate keys per group for different workloads."),
        "",
        "## 计费细节 / Details\n",
        g.table(["项目 Item", "说明 Notes"], [
            ["缓存读取 / Cache read", "命中缓存的输入 token 按「缓存读取」价计费，通常远低于输入价 / "
                                     "Cached input tokens are billed at the cache-read price, usually far below input"],
            ["缓存写入 / Cache write", "写入缓存的 token 按「缓存写入」价计费；"
                                      + T["zh"]["claude_1h"] + " / Tokens written to cache use the cache-write price; "
                                      + T["en"]["claude_1h"]],
            ["长上下文 / Long context", "部分 OpenAI 模型超过 272K 上下文后单价更高 / "
                                       "Some OpenAI models cost more above 272K context"],
            ["GLM", f"{T['zh']['in_lt32']} / {T['zh']['in_ge32']} 价格不同 / "
                    f"{T['en']['in_lt32']} and {T['en']['in_ge32']} are priced differently"],
            ["DeepSeek", f"{T['zh']['ds_peak']} / {T['en']['ds_peak']}"],
            ["视频 / Video", "按秒（美元 / 秒）或按 token 计费，价格随分辨率变化 / "
                            "Billed per second (USD/s) or per token, varying by resolution"],
        ], "ll"),
        bi("各模型价格见 " + link("Models-and-Pricing") + "，**最终以官网实时价格为准**。",
           "See " + link("Models-and-Pricing") + " for every price. **Live prices on the website prevail.**"),
    ]
    return "\n".join(L)


def models():
    zh, en = T["zh"], T["en"]

    def h(k):
        return f"{zh[k]} {en[k]}"

    def rate(t, grp, x):
        return t["rate_note"].format(g=t["g"].get(grp, grp), x=x).rstrip("：:")

    pp, d, code = g.pp, g.d, g.code
    peak = ", ".join(code(m) for m, _, pk, *_ in DEEPSEEK if pk)
    tz, te = T["zh"], T["en"]

    def vs(m, c, i, o, r):
        zh_, en_ = g.cn_disc("zh", tz, m, c, i, o, r), g.cn_disc("en", te, m, c, i, o, r)
        return zh_ if zh_ == en_ else f"{zh_}<br>{en_}"

    cnh = [h("c_model"), h("c_in"), h("c_out"), h("c_cw"), h("c_cr"), f"{E['zh']['c_disc']} {E['en']['c_disc']}"]
    L = [
        head("Models-and-Pricing"),
        bi("单位：**美元 / 每 1M tokens**（另有说明除外）。带折扣的表格格式为 `实付价（标价）`，按表头所注分组折算；"
           "其他分组请用 `标价 × 倍率` 自行计算（见 " + link("Billing") + "）。",
           "Unit: **USD per 1M tokens** unless noted. Discounted tables show `price paid (list price)` for the group named "
           "above the table; for other groups compute `list price × multiplier` (see " + link("Billing") + ")."),
        "## OpenAI\n",
        f"> {rate(zh, 'oai_pro', '0.3x')} / {rate(en, 'oai_pro', '0.3x')}\n",
        g.table([h("c_model"), h("c_ctx"), h("c_in"), h("c_out"), h("c_cw"), h("c_cr")],
                [[code(m), c, pp(i), pp(o), pp(w), pp(r)] for m, c, i, o, w, r in OAI], "lcrrrr"),
        f"> {zh['luna_note']}<br>{en['luna_note']}\n",
        "## Claude (Anthropic)\n",
        f"> {rate(zh, 'cl_max', '1.5x')} / {rate(en, 'cl_max', '1.5x')}\n",
        g.table([h("c_model"), h("c_same"), h("c_in"), h("c_out"), h("c_cw"), h("c_cr")],
                [[code(m), s if s == "—" else code(s), pp(i), pp(o), pp(w), pp(r)] for m, s, i, o, w, r in CLAUDE],
                "llrrrr"),
        "## Gemini (Google)\n",
        f"> {rate(zh, 'Gemini Chat / Coding', '0.3x')} / {rate(en, 'Gemini Chat / Coding', '0.3x')}\n",
        g.table([h("c_model"), h("c_in"), h("c_out"), h("c_cr")],
                [[code(m), pp(i), pp(o), pp(r)] for m, i, o, r in GEMINI]),
        f"## {zh['cn_title']} / Chinese models\n",
        bi("倍率 1x，实付价即标价。" + E["zh"]["cn_fx"].format(date=OFFICIAL),
           "Multiplier 1x: the price paid is the list price. " + E["en"]["cn_fx"].format(date=OFFICIAL)),
        "### DeepSeek\n",
        f"> {zh['ds_peak']}：{peak}<br>{en['ds_peak']}: {peak}\n",
        g.table(cnh,
                [[code(m) + (f"<br><sub>{zh['same']} {en['same']}: {s}</sub>" if s else ""), d(i), d(o), d(w), d(r),
                  vs(m, None, i, o, r)] for m, s, _, i, o, w, r in DEEPSEEK]),
        f"### {zh['glm_title']} / {en['glm_title']}\n",
        g.table(cnh[:1] + [h("c_cond")] + cnh[1:],
                [[code(m), {"lt": f"{zh['in_lt32']}<br>{en['in_lt32']}", "ge": f"{zh['in_ge32']}<br>{en['in_ge32']}",
                            None: "—"}[c], d(i), d(o), d(w), d(r), vs(m, c, i, o, r)] for m, c, i, o, w, r in GLM], "lcrrrrr"),
        f"### {zh['kimi_title']} / {en['kimi_title']}\n",
        g.table(cnh,
                [[code(m), d(i), d(o), d(w) + f"<br><sub>{zh['h1']} / {en['h1']}: {d(w1)}</sub>", d(r),
                  vs(m, None, i, o, r)] for m, i, o, w, w1, r in KIMI]),
        f"### {zh['doubao_title']} / {en['doubao_title']}\n",
        g.table(cnh,
                [[code(m) + (f"<br><sub>{zh['same']} {en['same']}: {s}</sub>" if s else ""), d(i), d(o), d(w), d(r),
                  vs(m, None, i, o, r)] for m, s, i, o, w, r in DOUBAO]),
        f"## {zh['video_title']} / {en['video_title']}\n",
        f"### {zh['per_sec']} / {en['per_sec']}\n",
        g.table([h("c_model"), h("c_default"), "480p", "720p", "768p", "1080p", "2K", "4K"],
                [[f"{n}<br><sub>{mid}</sub>"] + [d(x) for x in xs] for n, mid, *xs in VIDEO_SEC]),
        f"### {zh['per_tok']} / {en['per_tok']}\n",
        f"{zh['tok_format']} / {en['tok_format']}\n",
        g.table([h("c_model"), "480p", "720p", "1080p", "4K"],
                [[f"{n}<br><sub>{mid}</sub>"] + [" / ".join(f"${v}" for v in x.split("/")) if x != "-" else "—"
                                                for x in xs] for n, mid, *xs in VIDEO_TOK]),
        f"<sub>{zh['disclaimer']}<br>{en['disclaimer']}</sub>\n",
    ]
    return "\n".join(L)


def pricing_json():
    p = g.pricing()
    sample = next(m for m in p["models"] if m["model"] == "gpt-5.5")
    import json
    L = [
        head("Pricing-JSON"),
        bi(f"[`pricing.json`]({BLOB}/pricing.json) 是机器可读的价格数据，由与 README 相同的数据源生成，每次发布也会作为 Release 附件提供。",
           f"[`pricing.json`]({BLOB}/pricing.json) holds machine-readable prices generated from the same source as the README, "
           "and is attached to every release."),
        bi("其中的价格均为 **标价（美元）**，实付价需乘以分组倍率。",
           "All prices are **list prices in USD**; multiply by the group multiplier to get the price paid."),
        "## 顶层字段 / Top-level fields\n",
        g.table(["字段 Field", "类型 Type", "说明 Description"], [
            ["`website`", "string", "官网地址 / Website URL"],
            ["`note`", "string", "说明文字 / Human-readable note"],
            ["`assumed_usd_cny`", "number", f"估算折扣所用汇率（当前 {RATE}）/ Exchange rate used for discount estimates (now {RATE})"],
            ["`groups`", "array", "分组列表 / Groups"],
            ["`models`", "array", "模型列表 / Models"],
        ], "lll"),
        "## groups[]\n",
        g.table(["字段 Field", "类型 Type", "说明 Description"], [
            ["`id`", "string", "分组标识 / Group id"],
            ["`provider`", "string", "`openai` · `anthropic` · `google` · `cn` · `video`"],
            ["`multiplier`", "number", "分组倍率 / Group multiplier"],
            ["`tags`", "string[]", "`lowest` · `limited` · `exclusive` · `sla` · `dynamic-discount`"],
            ["`vs_official_price`", "number", "≈ multiplier ÷ assumed_usd_cny；国模为 null，见 `vs_official_price_range` / "
                                              "null for CN models, see `vs_official_price_range`"],
            ["`vs_official_price_range`", "number[]", "仅国模：各模型输出价 ÷ 官方人民币价的最低、最高值 / "
                                                     "CN models only: lowest and highest output price ÷ official CNY price"],
            ["`official_cny`", "object", "仅国模：厂商官方人民币价 / CN models only: vendor's official CNY price"],
            ["`vs_official`", "object", "仅国模：标价 ÷ 官方价（input / output / cache_read）/ "
                                        "CN models only: list ÷ official price"],
        ], "lll"),
        "## models[]\n",
        g.table(["字段 Field", "类型 Type", "说明 Description"], [
            ["`model`", "string", "调用时使用的模型 ID / Model ID used in requests"],
            ["`provider`", "string", "`openai` · `anthropic` · `google` · `deepseek` · `zhipu` · `moonshot` · `bytedance` · `video`"],
            ["`unit`", "string", "`USD/1M tokens` 或 or `USD/second`"],
            ["`input` `output`", "number \\| null", "输入 / 输出标价 / Input and output list price"],
            ["`cache_write` `cache_read`", "number \\| null", "缓存写入 / 读取标价，`null` 表示不适用 / Cache prices, `null` = n/a"],
            ["`cache_write_1h`", "number", "可选，1 小时缓存写入 / Optional, 1-hour cache write"],
            ["`context`", "string \\| null", "OpenAI 上下文档位，如 `≤272K` / OpenAI context tier, e.g. `≤272K`"],
            ["`condition`", "string", "可选，如 GLM 的 `input<32K` / Optional, e.g. GLM `input<32K`"],
            ["`same_price`", "string[]", "可选，同价模型 ID / Optional, model IDs with the same price"],
            ["`peak`", "string", "可选，DeepSeek 高峰时段规则 / Optional, DeepSeek peak-hour rule"],
            ["`name`", "string", "视频模型显示名 / Display name (video)"],
            ["`prices`", "object", "视频：分辨率 → 价格；按 token 计费时为 `{with_reference, without_reference}` / "
                                   "Video: resolution → price; per-token video uses `{with_reference, without_reference}`"],
        ], "lll"),
        bi("同一模型可能出现多次（例如不同上下文档位）。", "A model may appear more than once (e.g. one entry per context tier)."),
        "## 示例条目 / Sample entry\n",
        "```json\n" + json.dumps(sample, ensure_ascii=False, indent=2) + "\n```\n",
        "## 计算实付价 / Computing the price paid\n",
        "```python\nimport json, urllib.request\n\n"
        "url = \"https://raw.githubusercontent.com/cutetailbud/FastAIToken/master/pricing.json\"\n"
        "p = json.load(urllib.request.urlopen(url))\n"
        "mult = {g[\"id\"]: g[\"multiplier\"] for g in p[\"groups\"]}\n\n"
        "for m in p[\"models\"]:\n"
        "    if m[\"provider\"] == \"openai\" and m[\"input\"] is not None:\n"
        "        paid = m[\"input\"] * mult[\"openai-pro\"]\n"
        "        print(m[\"model\"], m.get(\"context\"), f\"input ${paid:.4f} / 1M tokens\")\n```\n",
    ]
    return "\n".join(L)


def invoices():
    zh, en = T["zh"]["inv"], T["en"]["inv"]
    L = [head("Invoices-and-Enterprise")]
    L += [item(a, b) for a, b in zip(zh, en, strict=True)]
    L += [
        "",
        "## 企业线路 / Enterprise lines\n",
        g.table(["分组 Group", "倍率 Multiplier", "相当于官方价 vs. official"],
                [[f"{z} / {e}", f"{m}x", gdisc(i, m)]
                 for z, e, m, i in groups() if "enterprise" in i], "lrr"),
        "## 联系方式 / Contact\n",
        f"- 官网 Website: [{g.URL}]({g.URL})（后台工单 / tickets in the dashboard）",
        f"- QQ 交流群 QQ group: **{g.QQ_GROUP}**\n",
    ]
    return "\n".join(L)


def faq():
    qa = [
        ("1 元真的等于 1 美元吗？", "Is 1 CNY really 1 USD?",
         "是的，充值的人民币按 1:1 兑换为美元额度，消费时再按 `标价 × 分组倍率` 扣除。",
         "Yes. Top-ups convert CNY to USD credit at 1:1; usage is then charged at `list price × group multiplier`."),
        ("Claude 倍率大于 1，还便宜吗？", "Claude multipliers are above 1. Is it still cheaper?",
         f"是的。由于 1 元 = 1 美元额度，1.5x 分组的人民币成本约为官方价的 {pct(1.5)}（按 1 美元 ≈ {RATE} 元估算）。",
         f"Yes. Because 1 CNY buys 1 USD of credit, a 1.5x group costs about {pct(1.5)} of the official price "
         f"(at 1 USD ≈ {RATE} CNY)."),
        ("Base URL 在哪里？", "Where do I find the base URL?",
         "登录官网控制台查看。示例与本 Wiki 都通过 `FASTAITOKEN_BASE_URL` 环境变量读取。",
         "In the console on the website. The examples and this wiki read it from `FASTAITOKEN_BASE_URL`."),
        ("返回 401 / 鉴权失败", "I get 401 / authentication errors",
         "检查 Key 是否完整、未被删除，Base URL 是否与控制台一致，请求头格式为 `Authorization: Bearer <key>`。",
         "Check that the key is complete and not deleted, that the base URL matches the console, and that the header is "
         "`Authorization: Bearer <key>`."),
        ("提示模型不存在", "The model is reported as not found",
         "确认模型 ID 拼写正确（见 " + link("Models-and-Pricing") + "），并且该模型在你 Key 所属的分组中可用。",
         "Check the model ID spelling (see " + link("Models-and-Pricing") + ") and that the model is available in your "
         "key's group."),
        ("请求被限流或不稳定", "Requests are rate-limited or unstable",
         "稍后重试并使用指数退避；对稳定性要求高的业务建议使用企业 SLA 线路，或为备用分组单独创建 Key。",
         "Retry with exponential backoff. For workloads that need stability, use an enterprise SLA line or keep a key "
         "for a backup group."),
        ("Key 泄露了怎么办？", "My key leaked. What now?",
         "立即在控制台删除该 Key 并创建新 Key。请勿在 Issue、QQ 群等公开渠道粘贴 Key。",
         "Delete it in the console right away and create a new one. Never paste keys in issues, the QQ group or other "
         "public places."),
        ("文档价格与官网不一致", "Prices here differ from the website",
         f"以官网实时价格为准。欢迎通过 [Issue]({REPO}/issues/new/choose) 告诉我们。",
         f"The live website prices prevail. Please let us know via an [issue]({REPO}/issues/new/choose)."),
        ("如何开发票？", "How do I get an invoice?",
         "登录后台提交工单，支持增值税专用发票与普通发票，详见 " + link("Invoices-and-Enterprise") + "。",
         "Open a ticket in the dashboard; VAT special and general invoices are supported. See "
         + link("Invoices-and-Enterprise") + "."),
    ]
    L = [head("FAQ")]
    for qz, qe, az, ae in qa:
        L += [f"### {qz} / {qe}\n", bi(az, ae)]
    L.append(bi(f"没有找到答案？见 [SUPPORT]({BLOB}/SUPPORT.md) 或加入 QQ 交流群 **{g.QQ_GROUP}**。",
                f"Still stuck? See [SUPPORT]({BLOB}/SUPPORT.md) or join QQ group **{g.QQ_GROUP}**."))
    return "\n".join(L)


def contributing():
    L = [
        head("Contributing"),
        bi("本 Wiki、README 与 `pricing.json` 都由 `scripts/readme/` 中的脚本生成，**请勿在 Wiki 网页上直接编辑**，"
           "否则下次同步时会被覆盖。",
           "This wiki, the READMEs and `pricing.json` are all generated by `scripts/readme/`. **Do not edit the wiki in "
           "the browser**: changes are overwritten on the next sync."),
        g.table(["修改内容 To change", "编辑文件 Edit"], [
            ["价格、模型 / Prices, models", "`scripts/readme/data.py`"],
            ["README 文案 / README wording", "`scripts/readme/i18n.py`"],
            ["汇率、折扣文案 / Exchange rate, discount wording", "`scripts/readme/extra.py`"],
            ["README 排版、`pricing.json` 结构 / README layout, `pricing.json` schema", "`scripts/readme/gen.py`"],
            ["Wiki 页面 / Wiki pages", "`scripts/readme/wiki.py`"],
        ], "ll"),
        "```bash\npython scripts/readme/gen.py .            # 重新生成 / regenerate\n"
        "python -m unittest discover -s tests      # 测试 / test\n"
        "python scripts/readme/gen.py . --check    # CI 检查 / what CI runs\n```\n",
        bi("合并到 `master` 后，`Wiki` 工作流会把 `wiki/` 目录同步到 GitHub Wiki。",
           "After merging to `master`, the `Wiki` workflow syncs the `wiki/` directory to the GitHub Wiki."),
        bi(f"完整说明见 [CONTRIBUTING.md]({BLOB}/CONTRIBUTING.md)。",
           f"Full guide: [CONTRIBUTING.md]({BLOB}/CONTRIBUTING.md)."),
    ]
    return "\n".join(L)


def sidebar():
    L = ["**FastAIToken Wiki**\n"]
    L += [f"- [{zh} {en}]({p})" for p, zh, en in PAGES]
    L += ["", "---\n", f"- [官网 Website]({g.URL})", f"- [README]({REPO}#readme)", f"- [pricing.json]({BLOB}/pricing.json)",
          f"- [CHANGELOG]({BLOB}/CHANGELOG.md)", f"- QQ: **{g.QQ_GROUP}**"]
    return "\n".join(L)


def footer():
    return (f"<sub>{T['zh']['disclaimer']} {T['en']['disclaimer']} "
            f"本页由脚本生成 / Generated from [scripts/readme/wiki.py]({BLOB}/scripts/readme/wiki.py).</sub>")


RENDER = {
    "Home": home, "Quick-Start": quick_start, "Billing": billing, "Models-and-Pricing": models,
    "Pricing-JSON": pricing_json, "Invoices-and-Enterprise": invoices, "FAQ": faq, "Contributing": contributing,
    "_Sidebar": sidebar, "_Footer": footer,
}


def pages():
    """Return {relative path: content} for every wiki page."""
    return {f"wiki/{name}.md": fn().rstrip("\n") + "\n" for name, fn in RENDER.items()}
