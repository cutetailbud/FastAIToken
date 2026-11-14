# 计费说明 / Billing

## 计费公式 / Formula

```
实付价 = 标价 × 分组倍率
Price paid = List price × Group multiplier
```

价格单位为 **美元 / 每 1M tokens**，视频按秒计费的为 **美元 / 秒**。价格可能随时调整，**请以官网实时价格为准**。
Prices are in **USD per 1M tokens**, or **USD per second** for per-second video. Prices may change at any time; **the live prices on the website prevail**.

## 相当于官方价几折 / Compared with official prices

官方按美元计价，而本平台 **1 元 = 1 美元额度**。按 1 美元 ≈ 7.1 元估算，**实际人民币成本 ≈ 官方价 × 倍率 ÷ 7.1**。
Official prices are in USD, but here **1 CNY buys 1 USD of credit**. Assuming 1 USD ≈ 7.1 CNY, **actual cost ≈ official price × multiplier ÷ 7.1**.

例如官方价 $10 的请求，在 0.3x 分组扣除 $3 额度，即 3 元人民币，约为官方价（71 元）的 4.2%。
E.g. a request costing $10 at official prices uses $3 of credit in a 0.3x group, which is 3 CNY, about 4.2% of the official 71 CNY.

国产模型本身按人民币计价，不存在汇率差：标价按 **1 元 = 1 美元** 直接与厂商官方人民币价对比，即「相当于官方价」= 标价 ÷ 官方价。多数模型低于官方价，见各表最后一列（官方价取自厂商价格页，2026-11）。
Chinese models are priced in CNY, so there is no exchange-rate gap: the list price is compared directly with the vendor's official CNY price at **1 CNY = 1 USD**, i.e. vs. official = list price ÷ official price. Most models are below the official price; see the last column of each table (official prices from vendor pricing pages, 2026-11).

## 分组 / Groups

| 分组 | Group | 倍率 Multiplier | 相当于官方价 vs. official | `pricing.json` id |
| :--- | :--- | ---: | ---: | :--- |
| OpenAI 福利分组 | OpenAI Welfare Group | 0.06x | 约 0.08 折（0.85%） | `openai-welfare` |
| OpenAI 普通分组 | OpenAI Standard Group | 0.2x | 约 0.28 折（2.8%） | `openai-standard` |
| OpenAI 备用渠道 | OpenAI Backup Channel | 0.25x | 约 0.35 折（3.5%） | `openai-backup` |
| OpenAI Pro 线路 | OpenAI Pro Line | 0.3x | 约 0.42 折（4.2%） | `openai-pro` |
| OpenAI Pro 企业线路 | OpenAI Pro Enterprise Line | 0.5x | 约 0.70 折（7.0%） | `openai-pro-enterprise` |
| Claude Max 分组 | Claude Max Group | 1.5x | 约 2.11 折（21.1%） | `claude-max` |
| Claude Max 企业线路 | Claude Max Enterprise Line | 1.9x | 约 2.68 折（26.8%） | `claude-max-enterprise` |
| Gemini Chat / Coding | Gemini Chat / Coding | 0.3x | 约 0.42 折（4.2%） | `gemini-chat-coding` |
| 国模分组 - Deepseek / Glm（含 Kimi / 豆包） | CN Models – DeepSeek / GLM (incl. Kimi / Doubao) | 1x | 约 5–10 折（因模型而异） | `cn-models` |
| 视频生成分组 - seedance/h3 | Video Generation – seedance/h3 | 1x | 约 1.41 折（14.1%） | `video` |

### 如何选择分组 / Choosing a group

- **倍率越低越便宜**。标注「限时」的分组价格可能调整或下线。<br>**Lower multiplier = cheaper.** Groups tagged *limited-time* may change or be withdrawn.
- **企业线路**（OpenAI Pro 企业线路、Claude Max 企业线路）为专属分组，提供 SLA 保障，适合生产环境。<br>**Enterprise lines** (OpenAI Pro Enterprise, Claude Max Enterprise) are dedicated and come with an SLA; use them in production.
- 同一模型可在多个分组中使用；可以为不同用途创建不同分组的 Key。<br>The same model is available in several groups; create separate keys per group for different workloads.

## 计费细节 / Details

| 项目 Item | 说明 Notes |
| :--- | :--- |
| 缓存读取 / Cache read | 命中缓存的输入 token 按「缓存读取」价计费，通常远低于输入价 / Cached input tokens are billed at the cache-read price, usually far below input |
| 缓存写入 / Cache write | 写入缓存的 token 按「缓存写入」价计费；1 小时缓存写入：claude-opus-5-5 为 $12.00，claude-haiku-5-5 为 $0.30。 / Tokens written to cache use the cache-write price; 1-hour cache write: claude-opus-5-5 $12.00, claude-haiku-5-5 $0.30. |
| 长上下文 / Long context | 部分 OpenAI 模型超过 272K 上下文后单价更高 / Some OpenAI models cost more above 272K context |
| GLM | 输入 <32K / 输入 ≥32K 价格不同 / Input <32K and Input ≥32K are priced differently |
| DeepSeek | 工作日高峰时段 09:00–12:00、14:00–18:00（GMT+8）价格 ×2 / Weekday peak hours 09:00–12:00 and 14:00–18:00 (GMT+8): price ×2 |
| 视频 / Video | 按秒（美元 / 秒）或按 token 计费，价格随分辨率变化 / Billed per second (USD/s) or per token, varying by resolution |

各模型价格见 [模型与价格 / Models and Pricing](Models-and-Pricing)，**最终以官网实时价格为准**。
See [模型与价格 / Models and Pricing](Models-and-Pricing) for every price. **Live prices on the website prevail.**
