<div align="center">

<a href="https://www.fastaitoken.com/"><img src="./sponsor-fastai.png" alt="FastAIToken" width="560"></a>

<p><b>One-stop LLM API aggregation platform</b></p>

<p><a href="https://www.fastaitoken.com/">Website</a> &nbsp;|&nbsp; QQ Group: <b>1019537221</b></p>

<p><sub><a href="./README.md">简体中文</a> · <b>English</b> · <a href="./README.ja.md">日本語</a> · <a href="./README.ko.md">한국어</a> · <a href="./README.ru.md">Русский</a> · <a href="./README.kk.md">Қазақша</a> · <a href="./README.vi.md">Tiếng Việt</a> · <a href="./README.th.md">ภาษาไทย</a> · <a href="./README.id.md">Bahasa Indonesia</a> · <a href="./README.ms.md">Bahasa Melayu</a></sub></p>

<p>
  <a href="https://github.com/cutetailbud/FastAIToken/actions/workflows/ci.yml"><img src="https://github.com/cutetailbud/FastAIToken/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/cutetailbud/FastAIToken/releases"><img src="https://img.shields.io/github/v/release/cutetailbud/FastAIToken" alt="Release"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/github/license/cutetailbud/FastAIToken" alt="License"></a>
  <a href="./pricing.json"><img src="https://img.shields.io/badge/pricing-JSON-blue" alt="pricing.json"></a>
</p>

</div>

<br>

FastAIToken aggregates mainstream large language models and video generation models from China and around the world. With one account and one API key you can call GPT, Claude, Gemini, Grok, DeepSeek, GLM and Kimi, as well as video models such as Seedance, MiniMax H3, Wan 3.0 and Veo 3.1.

## Why FastAIToken

- **1 CNY = 1 USD**: top up in RMB and get USD credit at a 1:1 rate — great value
- **Full model lineup**: GPT / Claude / Gemini / Grok / DeepSeek / GLM / Kimi / Doubao Seed
- **Video models**: Seedance 2.0 / 2.5, MiniMax H3, Wan 3.0, Veo 3.1, billed per second or per token
- **Self-service invoicing**: submit a ticket in the dashboard to get Chinese **VAT special** or **general** invoices
- **Enterprise partnership**: dedicated enterprise lines with SLA; corporate bank transfers supported
- **Multiple groups**: each model is offered on several lines / groups, so you can balance price and stability

## Billing

```
Price paid = List price × Group multiplier
```

All prices below are in **USD per 1M tokens** (except per-second video pricing), shown as `price paid (list price)`. Prices may change at any time — **the live prices on the website prevail**.

**How much cheaper than official?** Official prices are in USD, but here **1 CNY buys 1 USD of credit**, and usage is then multiplied by the group multiplier. Assuming 1 USD ≈ 7.1 CNY:

**Actual cost ≈ official price × multiplier ÷ 7.1**

E.g. a 0.3x group: 0.3 ÷ 7.1 ≈ **4.2%** of the official price.

### Effective discount by group

| Group | Multiplier | vs. official price |
| :--- | ---: | ---: |
| OpenAI Welfare Group | 0.06x | ≈ 0.85% |
| OpenAI Standard Group | 0.2x | ≈ 2.8% |
| OpenAI Backup Channel | 0.25x | ≈ 3.5% |
| OpenAI Pro Line | 0.3x | ≈ 4.2% |
| OpenAI Pro Enterprise Line | 0.5x | ≈ 7.0% |
| Claude Max Group | 1.5x | ≈ 21.1% |
| Claude Max Enterprise Line | 1.9x | ≈ 26.8% |
| Gemini Chat / Coding | 0.3x | ≈ 4.2% |
| CN Models – DeepSeek / GLM (incl. Kimi / Doubao) | 1x | ≈ 50–100% (varies by model) |
| Video Generation – seedance/h3 | 1x | ≈ 14.1% |

## OpenAI

10 models across 5 groups:

| Group | Multiplier | vs. official price | Tags |
| :--- | ---: | ---: | :--- |
| OpenAI Welfare Group | 0.06x | ≈ 0.85% | Lowest · Limited-time |
| OpenAI Standard Group | 0.2x | ≈ 2.8% | Limited-time |
| OpenAI Backup Channel | 0.25x | ≈ 3.5% | Limited-time |
| OpenAI Pro Line | 0.3x | ≈ 4.2% | Limited-time |
| OpenAI Pro Enterprise Line | 0.5x | ≈ 7.0% | Exclusive · SLA |

Prices below are at the “OpenAI Pro Line” 0.3x rate:

| Model | Context | Input | Output | Cache write | Cache read |
| :--- | :---: | ---: | ---: | ---: | ---: |
| `gpt-5.4` | — | $0.75 <sub>($2.50)</sub> | $4.50 <sub>($15.00)</sub> | — | $0.075 <sub>($0.25)</sub> |
| `gpt-5.4-mini` | — | $0.225 <sub>($0.75)</sub> | $1.35 <sub>($4.50)</sub> | — | $0.0225 <sub>($0.075)</sub> |
| `gpt-5.5` | ≤272K | $1.50 <sub>($5.00)</sub> | $9.00 <sub>($30.00)</sub> | — | $0.15 <sub>($0.50)</sub> |
| `gpt-5.5` | >272K | $3.00 <sub>($10.00)</sub> | $18.00 <sub>($60.00)</sub> | — | $0.30 <sub>($1.00)</sub> |
| `gpt-5.6-luna / terra` | ≤272K | $0.60 <sub>($2.00)</sub> | $3.60 <sub>($12.00)</sub> | $0.75 <sub>($2.50)</sub> | $0.06 <sub>($0.20)</sub> |
| `gpt-5.6-luna / terra` | >272K | $1.20 <sub>($4.00)</sub> | $7.20 <sub>($24.00)</sub> | $1.50 <sub>($5.00)</sub> | $0.12 <sub>($0.40)</sub> |
| `gpt-5.6-sol` | ≤272K | $1.50 <sub>($5.00)</sub> | $9.00 <sub>($30.00)</sub> | $1.875 <sub>($6.25)</sub> | $0.15 <sub>($0.50)</sub> |
| `gpt-5.6-sol` | >272K | $3.00 <sub>($10.00)</sub> | $13.50 <sub>($45.00)</sub> | $3.75 <sub>($12.50)</sub> | $0.30 <sub>($1.00)</sub> |
| `gpt-6-astra` | ≤272K | $3.00 <sub>($10.00)</sub> | $15.00 <sub>($50.00)</sub> | $3.75 <sub>($12.50)</sub> | $0.30 <sub>($1.00)</sub> |
| `gpt-6-astra` | >272K | $6.00 <sub>($20.00)</sub> | $22.50 <sub>($75.00)</sub> | $7.50 <sub>($25.00)</sub> | $0.60 <sub>($2.00)</sub> |
| `gpt-6-sol` | ≤272K | $0.60 <sub>($2.00)</sub> | $3.00 <sub>($10.00)</sub> | $0.75 <sub>($2.50)</sub> | $0.06 <sub>($0.20)</sub> |
| `gpt-6-sol` | >272K | $1.20 <sub>($4.00)</sub> | $6.00 <sub>($20.00)</sub> | $1.50 <sub>($5.00)</sub> | $0.12 <sub>($0.40)</sub> |
| `gpt-6.1-sol` | ≤272K | $0.60 <sub>($2.00)</sub> | $3.00 <sub>($10.00)</sub> | $0.75 <sub>($2.50)</sub> | $0.03 <sub>($0.10)</sub> |
| `gpt-6.1-sol` | >272K | $1.20 <sub>($4.00)</sub> | $6.00 <sub>($20.00)</sub> | $1.50 <sub>($5.00)</sub> | $0.06 <sub>($0.20)</sub> |
| `gpt-6.1-terra` | — | $0.30 <sub>($1.00)</sub> | $1.50 <sub>($5.00)</sub> | $0.375 <sub>($1.25)</sub> | $0.015 <sub>($0.05)</sub> |

> gpt-5.6-luna runs on the Terra model and is billed as terra (same price as gpt-5.6-terra).

## Claude (Anthropic)

Full-power channel based on the official MAX plan. 14 models across 2 groups:

| Group | Multiplier | vs. official price | Tags |
| :--- | ---: | ---: | :--- |
| Claude Max Group | 1.5x | ≈ 21.1% | Lowest |
| Claude Max Enterprise Line | 1.9x | ≈ 26.8% | Exclusive · SLA |

Prices below are at the “Claude Max Group” 1.5x rate:

| Model | Same price | Input | Output | Cache write | Cache read |
| :--- | :--- | ---: | ---: | ---: | ---: |
| `claude-fable-5` | `claude-fable-5-1` | $15.00 <sub>($10.00)</sub> | $75.00 <sub>($50.00)</sub> | $18.75 <sub>($12.50)</sub> | $1.50 <sub>($1.00)</sub> |
| `claude-opus-5-5` | — | $6.00 <sub>($4.00)</sub> | $30.00 <sub>($20.00)</sub> | $7.50 <sub>($5.00)</sub> | $0.30 <sub>($0.20)</sub> |
| `claude-opus-4-6` | `claude-opus-4-7 / 4-8 / 5` | $7.50 <sub>($5.00)</sub> | $37.50 <sub>($25.00)</sub> | $9.375 <sub>($6.25)</sub> | $0.75 <sub>($0.50)</sub> |
| `claude-sonnet-5` | `claude-sonnet-5-5` | $3.00 <sub>($2.00)</sub> | $15.00 <sub>($10.00)</sub> | $3.75 <sub>($2.50)</sub> | $0.30 <sub>($0.20)</sub> |
| `claude-sonnet-4-5` | `claude-sonnet-4-6` | $4.50 <sub>($3.00)</sub> | $22.50 <sub>($15.00)</sub> | $5.625 <sub>($3.75)</sub> | $0.45 <sub>($0.30)</sub> |
| `claude-haiku-5-5` | — | $0.15 <sub>($0.10)</sub> | $0.75 <sub>($0.50)</sub> | $0.1875 <sub>($0.125)</sub> | $0.015 <sub>($0.01)</sub> |
| `claude-haiku-4-5` | `claude-haiku-4-6` | $0.375 <sub>($0.25)</sub> | $1.875 <sub>($1.25)</sub> | $0.45 <sub>($0.30)</sub> | $0.045 <sub>($0.03)</sub> |

> 1-hour cache write: claude-opus-5-5 $12.00, claude-haiku-5-5 $0.30.

## Gemini (Google)

Supports Gemini 3.8 Flash / Gemini 4 Argon. Group “Gemini Chat / Coding [argon4 new]”, multiplier **0.3x**:

| Model | Input | Output | Cache read |
| :--- | ---: | ---: | ---: |
| `gemini-3.8-flash` | $0.225 <sub>($0.75)</sub> | $1.125 <sub>($3.75)</sub> | $0.0225 <sub>($0.075)</sub> |
| `gemini-4-argon` | $0.60 <sub>($2.00)</sub> | $3.00 <sub>($10.00)</sub> | $0.03 <sub>($0.10)</sub> |

## Chinese Models (DeepSeek / GLM / Kimi / Doubao)

28 models, including DeepSeek V4 Pro and GLM 5.2. Groups “CN Models – DeepSeek / GLM” and “CN access point”, multiplier **1x** (dynamic discount) — the price paid equals the list price.

Chinese models are priced in CNY, so there is no exchange-rate gap: the list price is compared directly with the vendor's official CNY price at **1 CNY = 1 USD**, i.e. vs. official = list price ÷ official price. Most models are below the official price; see the last column of each table (official prices from vendor pricing pages, 2026-11).

### DeepSeek

> Weekday peak hours 09:00–12:00 and 14:00–18:00 (GMT+8): price ×2: `deepseek-v4-flash`, `deepseek-v4-pro`, `deepseek-v4.1-flash`

| Model | Input | Output | Cache write | Cache read | vs. official price |
| :--- | ---: | ---: | ---: | ---: | ---: |
| `deepseek-v4-flash` | $1.05 | $3.15 | $1.05 | $0.035 | Input 105%<br>Output 78.75%<br>Cache read 175% |
| `deepseek-v4-pro` | $3.15 | $9.45 | $3.15 | $0.105 | 70% |
| `deepseek-v4.1-flash`<br><sub>same price: deepseek-v4.1-flash-1017, deepseek/deepseek-flash</sub> | $0.70 | $2.80 | $0.70 | $0.014 | 70% |
| `hy4` | $3.00 | $9.00 | $3.00 | $0.15 | 50% |

### Zhipu GLM

| Model | Condition | Input | Output | Cache write | Cache read | vs. official price |
| :--- | :---: | ---: | ---: | ---: | ---: | ---: |
| `glm-5` | Input <32K | $4.00 | $18.00 | — | $1.00 | Same as official |
| `glm-5` | Input ≥32K | $6.00 | $22.00 | — | $1.50 | Same as official |
| `glm-5-turbo` | Input <32K | $5.00 | $22.00 | — | $1.20 | Same as official |
| `glm-5-turbo` | Input ≥32K | $7.00 | $26.00 | — | $1.80 | Same as official |
| `glm-5.1` | Input <32K | $3.60 | $14.40 | — | $0.78 | 60% |
| `glm-5.1` | Input ≥32K | $4.80 | $16.80 | — | $1.20 | 60% |
| `glm-5.2` | — | $5.60 | $19.60 | — | $1.40 | 70% |
| `glm-5.3` | — | $6.40 | $22.40 | $6.40 | $1.60 | 80% |
| `glm-5.3-flash` | — | $0.64 | $2.24 | $0.64 | $0.184 | 80% |

### Kimi (Moonshot AI)

| Model | Input | Output | Cache write | Cache read | vs. official price |
| :--- | ---: | ---: | ---: | ---: | ---: |
| `kimi-k3` | $19.00 | $95.00 | $19.00<br><sub>1-hour: $38.00</sub> | $1.90 | 95% |
| `kimi-k3.1-pro` | $13.00 | $68.00 | $13.00<br><sub>1-hour: $26.00</sub> | $1.30 | Same as official |

### Doubao Seed (ByteDance)

| Model | Input | Output | Cache write | Cache read | vs. official price |
| :--- | ---: | ---: | ---: | ---: | ---: |
| `doubao-seed-2-1-pro`<br><sub>same price: doubao-seed-2-1-pro-260915</sub> | $5.40 | $27.00 | $5.40 | $1.08 | 90% |

## Video Models

18 models, including Seedance 2.5 / MiniMax H3 / Veo 3.1 / Wan 3.0. Group “Video Generation – seedance/h3”, multiplier **1x**.

### Per-second billing (USD / second)

| Model | Default | 480p | 720p | 768p | 1080p | 2K | 4K |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| H-Seedance 2.0 Lite<br><sub>hseedance-2.0-lite-time</sub> | — | $0.297 | — | $0.375 | $0.50 | $0.625 | $0.75 |
| H-Seedance 2.0 Pro Mini<br><sub>hseedance-2.0-pro-mini-time</sub> | — | $0.209 | $0.412 | $0.412 | $0.90 | $0.99 | $1.089 |
| H-Seedance 2.0 Pro Fast<br><sub>hseedance-2.0-pro-fast-time</sub> | — | $0.335 | $0.645 | $0.645 | $1.40 | $1.54 | $1.694 |
| H-Seedance 2.0 Pro<br><sub>hseedance-2.0-pro-time</sub> | — | $0.416 | $0.795 | $0.795 | $1.73 | $4.30 | $4.90 |
| H-Seedance 2.5 Pro<br><sub>hseedance-2.5-pro-time</sub> | — | $0.606 | $1.188 | $1.188 | $2.587 | $6.37 | $7.007 |
| Seedance 2.0 Fast / Seedance 2.0<br><sub>seedance-2.0-fast-time</sub> | — | $0.45 | $0.59 | — | $0.70 | — | — |
| MiniMax H3<br><sub>minimax-h3-time</sub> | — | — | — | $0.07 | $0.08 | — | — |
| Wan 3.0 Video<br><sub>wan-3.0-time</sub> | — | $0.30 | $0.60 | — | $1.30 | — | — |
| Veo 3.1<br><sub>veo3.1-time</sub> | $0.14 | — | — | — | — | — | — |
| auto-video-hd<br><sub>auto-video-hd, ll2-auto-hd</sub> | — | — | $0.0001 | — | $0.0001 | $0.0001 | — |

### Per-token billing (USD / 1M tokens)

Format: `with video reference / without reference`

| Model | 480p | 720p | 1080p | 4K |
| :--- | ---: | ---: | ---: | ---: |
| Seedance 2.0 Mini<br><sub>seedance-2.0-mini-token</sub> | $12.60 / $20.70 | $12.60 / $20.70 | $13.95 / $22.95 | — |
| Seedance 2.0 Fast<br><sub>seedance-2.0-fast-token</sub> | $19.80 / $33.30 | $19.80 / $33.30 | $22.05 / $37.80 | — |
| Seedance 2.0 Pro<br><sub>seedance-2.0-pro-token</sub> | $25.20 / $41.40 | $25.20 / $41.40 | $27.90 / $45.90 | $14.40 / $23.40 |
| Seedance 2.0<br><sub>seedance-2.0-token</sub> | $28.00 / $46.00 | $28.00 / $46.00 | $31.00 / $51.00 | $16.00 / $26.00 |
| Seedance 2.5 Pro<br><sub>seedance-2.5-pro-token</sub> | — | $37.80 / $63.00 | $41.85 / $69.30 | — |
| Seedance 2.5<br><sub>seedance-2.5-token</sub> | $42.00 / $70.00 | $42.00 / $70.00 | $33.12 / $55.44 | — |

## Quick Start

1. Sign up at [https://www.fastaitoken.com/](https://www.fastaitoken.com/)
2. Top up (1 CNY = 1 USD credit)
3. Create an API key in the console and choose a group
4. Configure the key and the Base URL shown in the console in your app / SDK / coding tool

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-xxxxxxxx",  # created in the FastAIToken console
    base_url="<Base URL from the console>",
)

resp = client.chat.completions.create(
    model="gpt-5.5",
    messages=[{"role": "user", "content": "Hello!"}],
)
print(resp.choices[0].message.content)
```

[examples/](./examples) · [pricing.json](./pricing.json) · [CHANGELOG](./CHANGELOG.md) · [CONTRIBUTING](./CONTRIBUTING.md) · [SECURITY](./SECURITY.md) · [SUPPORT](./SUPPORT.md)

## Invoices & Enterprise

- **Invoices**: log in → submit a ticket to request Chinese VAT special or general invoices
- **Enterprise SLA**: dedicated groups such as OpenAI Pro Enterprise Line and Claude Max Enterprise Line come with SLA guarantees
- **Corporate transfer**: corporate bank-transfer top-ups and partnerships are supported — contact support via the website

## Contact

- Website: [https://www.fastaitoken.com/](https://www.fastaitoken.com/)
- QQ Group: **1019537221**

---

<sub>Pricing in this repository is for reference only. Actual prices, model list and group multipliers are subject to the live website.</sub>
