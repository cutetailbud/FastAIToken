# 模型与价格 / Models and Pricing

单位：**美元 / 每 1M tokens**（另有说明除外）。带折扣的表格格式为 `实付价（标价）`，按表头所注分组折算；其他分组请用 `标价 × 倍率` 自行计算（见 [计费说明 / Billing](Billing)）。
Unit: **USD per 1M tokens** unless noted. Discounted tables show `price paid (list price)` for the group named above the table; for other groups compute `list price × multiplier` (see [计费说明 / Billing](Billing)).

## OpenAI

> 以下按「OpenAI Pro 线路 0.3x」折算 / Prices below are at the “OpenAI Pro Line” 0.3x rate

| 模型 Model | 上下文 Context | 输入 Input | 输出 Output | 缓存写入 Cache write | 缓存读取 Cache read |
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

> gpt-5.6-luna 采用 Terra 模型，并按 terra 计费（与 gpt-5.6-terra 同价）。<br>gpt-5.6-luna runs on the Terra model and is billed as terra (same price as gpt-5.6-terra).

## Claude (Anthropic)

> 以下按「Claude Max 分组 1.5x」折算 / Prices below are at the “Claude Max Group” 1.5x rate

| 模型 Model | 同价模型 Same price | 输入 Input | 输出 Output | 缓存写入 Cache write | 缓存读取 Cache read |
| :--- | :--- | ---: | ---: | ---: | ---: |
| `claude-fable-5` | `claude-fable-5-1` | $15.00 <sub>($10.00)</sub> | $75.00 <sub>($50.00)</sub> | $18.75 <sub>($12.50)</sub> | $1.50 <sub>($1.00)</sub> |
| `claude-opus-5-5` | — | $6.00 <sub>($4.00)</sub> | $30.00 <sub>($20.00)</sub> | $7.50 <sub>($5.00)</sub> | $0.30 <sub>($0.20)</sub> |
| `claude-opus-4-6` | `claude-opus-4-7 / 4-8 / 5` | $7.50 <sub>($5.00)</sub> | $37.50 <sub>($25.00)</sub> | $9.375 <sub>($6.25)</sub> | $0.75 <sub>($0.50)</sub> |
| `claude-sonnet-5` | `claude-sonnet-5-5` | $3.00 <sub>($2.00)</sub> | $15.00 <sub>($10.00)</sub> | $3.75 <sub>($2.50)</sub> | $0.30 <sub>($0.20)</sub> |
| `claude-sonnet-4-5` | `claude-sonnet-4-6` | $4.50 <sub>($3.00)</sub> | $22.50 <sub>($15.00)</sub> | $5.625 <sub>($3.75)</sub> | $0.45 <sub>($0.30)</sub> |
| `claude-haiku-5-5` | — | $0.15 <sub>($0.10)</sub> | $0.75 <sub>($0.50)</sub> | $0.1875 <sub>($0.125)</sub> | $0.015 <sub>($0.01)</sub> |
| `claude-haiku-4-5` | `claude-haiku-4-6` | $0.375 <sub>($0.25)</sub> | $1.875 <sub>($1.25)</sub> | $0.45 <sub>($0.30)</sub> | $0.045 <sub>($0.03)</sub> |

## Gemini (Google)

> 以下按「Gemini Chat / Coding 0.3x」折算 / Prices below are at the “Gemini Chat / Coding” 0.3x rate

| 模型 Model | 输入 Input | 输出 Output | 缓存读取 Cache read |
| :--- | ---: | ---: | ---: |
| `gemini-3.8-flash` | $0.225 <sub>($0.75)</sub> | $1.125 <sub>($3.75)</sub> | $0.0225 <sub>($0.075)</sub> |
| `gemini-4-argon` | $0.60 <sub>($2.00)</sub> | $3.00 <sub>($10.00)</sub> | $0.03 <sub>($0.10)</sub> |

## 国产模型（DeepSeek / GLM / Kimi / 豆包） / Chinese models

倍率 1x，实付价即标价。国产模型本身按人民币计价，不存在汇率差：标价按 **1 元 = 1 美元** 直接与厂商官方人民币价对比，即「相当于官方价」= 标价 ÷ 官方价。多数模型低于官方价，见各表最后一列（官方价取自厂商价格页，2026-11）。
Multiplier 1x: the price paid is the list price. Chinese models are priced in CNY, so there is no exchange-rate gap: the list price is compared directly with the vendor's official CNY price at **1 CNY = 1 USD**, i.e. vs. official = list price ÷ official price. Most models are below the official price; see the last column of each table (official prices from vendor pricing pages, 2026-11).

### DeepSeek

> 工作日高峰时段 09:00–12:00、14:00–18:00（GMT+8）价格 ×2：`deepseek-v4-flash`, `deepseek-v4-pro`, `deepseek-v4.1-flash`<br>Weekday peak hours 09:00–12:00 and 14:00–18:00 (GMT+8): price ×2: `deepseek-v4-flash`, `deepseek-v4-pro`, `deepseek-v4.1-flash`

| 模型 Model | 输入 Input | 输出 Output | 缓存写入 Cache write | 缓存读取 Cache read | 相当于官方价 vs. official price |
| :--- | ---: | ---: | ---: | ---: | ---: |
| `deepseek-v4-flash` | $1.05 | $3.15 | $1.05 | $0.035 | 输入 105%<br>输出 7.88 折<br>缓存读取 175%<br>Input 105%<br>Output 78.75%<br>Cache read 175% |
| `deepseek-v4-pro` | $3.15 | $9.45 | $3.15 | $0.105 | 7 折<br>70% |
| `deepseek-v4.1-flash`<br><sub>同价 same price: deepseek-v4.1-flash-1017, deepseek/deepseek-flash</sub> | $0.70 | $2.80 | $0.70 | $0.014 | 7 折<br>70% |
| `hy4` | $3.00 | $9.00 | $3.00 | $0.15 | 5 折<br>50% |

### 智谱 GLM / Zhipu GLM

| 模型 Model | 条件 Condition | 输入 Input | 输出 Output | 缓存写入 Cache write | 缓存读取 Cache read | 相当于官方价 vs. official price |
| :--- | :---: | ---: | ---: | ---: | ---: | ---: |
| `glm-5` | 输入 <32K<br>Input <32K | $4.00 | $18.00 | — | $1.00 | 与官方价相同<br>Same as official |
| `glm-5` | 输入 ≥32K<br>Input ≥32K | $6.00 | $22.00 | — | $1.50 | 与官方价相同<br>Same as official |
| `glm-5-turbo` | 输入 <32K<br>Input <32K | $5.00 | $22.00 | — | $1.20 | 与官方价相同<br>Same as official |
| `glm-5-turbo` | 输入 ≥32K<br>Input ≥32K | $7.00 | $26.00 | — | $1.80 | 与官方价相同<br>Same as official |
| `glm-5.1` | 输入 <32K<br>Input <32K | $3.60 | $14.40 | — | $0.78 | 6 折<br>60% |
| `glm-5.1` | 输入 ≥32K<br>Input ≥32K | $4.80 | $16.80 | — | $1.20 | 6 折<br>60% |
| `glm-5.2` | — | $5.60 | $19.60 | — | $1.40 | 7 折<br>70% |
| `glm-5.3` | — | $6.40 | $22.40 | $6.40 | $1.60 | 8 折<br>80% |
| `glm-5.3-flash` | — | $0.64 | $2.24 | $0.64 | $0.184 | 8 折<br>80% |

### Kimi（月之暗面） / Kimi (Moonshot AI)

| 模型 Model | 输入 Input | 输出 Output | 缓存写入 Cache write | 缓存读取 Cache read | 相当于官方价 vs. official price |
| :--- | ---: | ---: | ---: | ---: | ---: |
| `kimi-k3` | $19.00 | $95.00 | $19.00<br><sub>1 小时 / 1-hour: $38.00</sub> | $1.90 | 9.5 折<br>95% |
| `kimi-k3.1-pro` | $13.00 | $68.00 | $13.00<br><sub>1 小时 / 1-hour: $26.00</sub> | $1.30 | 与官方价相同<br>Same as official |

### 豆包 Seed（字节跳动） / Doubao Seed (ByteDance)

| 模型 Model | 输入 Input | 输出 Output | 缓存写入 Cache write | 缓存读取 Cache read | 相当于官方价 vs. official price |
| :--- | ---: | ---: | ---: | ---: | ---: |
| `doubao-seed-2-1-pro`<br><sub>同价 same price: doubao-seed-2-1-pro-260915</sub> | $5.40 | $27.00 | $5.40 | $1.08 | 9 折<br>90% |

## 视频模型 / Video Models

### 按秒计费（美元 / 秒） / Per-second billing (USD / second)

| 模型 Model | 默认 Default | 480p | 720p | 768p | 1080p | 2K | 4K |
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

### 按 token 计费（美元 / 每 1M tokens） / Per-token billing (USD / 1M tokens)

格式：`带视频参考 / 无参考` / Format: `with video reference / without reference`

| 模型 Model | 480p | 720p | 1080p | 4K |
| :--- | ---: | ---: | ---: | ---: |
| Seedance 2.0 Mini<br><sub>seedance-2.0-mini-token</sub> | $12.60 / $20.70 | $12.60 / $20.70 | $13.95 / $22.95 | — |
| Seedance 2.0 Fast<br><sub>seedance-2.0-fast-token</sub> | $19.80 / $33.30 | $19.80 / $33.30 | $22.05 / $37.80 | — |
| Seedance 2.0 Pro<br><sub>seedance-2.0-pro-token</sub> | $25.20 / $41.40 | $25.20 / $41.40 | $27.90 / $45.90 | $14.40 / $23.40 |
| Seedance 2.0<br><sub>seedance-2.0-token</sub> | $28.00 / $46.00 | $28.00 / $46.00 | $31.00 / $51.00 | $16.00 / $26.00 |
| Seedance 2.5 Pro<br><sub>seedance-2.5-pro-token</sub> | — | $37.80 / $63.00 | $41.85 / $69.30 | — |
| Seedance 2.5<br><sub>seedance-2.5-token</sub> | $42.00 / $70.00 | $42.00 / $70.00 | $33.12 / $55.44 | — |

<sub>本仓库价格信息仅供参考，实际价格、模型列表与分组倍率以官网实时显示为准。<br>Pricing in this repository is for reference only. Actual prices, model list and group multipliers are subject to the live website.</sub>
