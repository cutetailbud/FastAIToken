# pricing.json 说明 / pricing.json reference

[`pricing.json`](https://github.com/cutetailbud/FastAIToken/blob/master/pricing.json) 是机器可读的价格数据，由与 README 相同的数据源生成，每次发布也会作为 Release 附件提供。
[`pricing.json`](https://github.com/cutetailbud/FastAIToken/blob/master/pricing.json) holds machine-readable prices generated from the same source as the README, and is attached to every release.

其中的价格均为 **标价（美元）**，实付价需乘以分组倍率。
All prices are **list prices in USD**; multiply by the group multiplier to get the price paid.

## 顶层字段 / Top-level fields

| 字段 Field | 类型 Type | 说明 Description |
| :--- | :--- | :--- |
| `website` | string | 官网地址 / Website URL |
| `note` | string | 说明文字 / Human-readable note |
| `assumed_usd_cny` | number | 估算折扣所用汇率（当前 7.1）/ Exchange rate used for discount estimates (now 7.1) |
| `groups` | array | 分组列表 / Groups |
| `models` | array | 模型列表 / Models |

## groups[]

| 字段 Field | 类型 Type | 说明 Description |
| :--- | :--- | :--- |
| `id` | string | 分组标识 / Group id |
| `provider` | string | `openai` · `anthropic` · `google` · `cn` · `video` |
| `multiplier` | number | 分组倍率 / Group multiplier |
| `tags` | string[] | `lowest` · `limited` · `exclusive` · `sla` · `dynamic-discount` |
| `vs_official_price` | number | ≈ multiplier ÷ assumed_usd_cny；国模为 null，见 `vs_official_price_range` / null for CN models, see `vs_official_price_range` |
| `vs_official_price_range` | number[] | 仅国模：各模型输出价 ÷ 官方人民币价的最低、最高值 / CN models only: lowest and highest output price ÷ official CNY price |
| `official_cny` | object | 仅国模：厂商官方人民币价 / CN models only: vendor's official CNY price |
| `vs_official` | object | 仅国模：标价 ÷ 官方价（input / output / cache_read）/ CN models only: list ÷ official price |

## models[]

| 字段 Field | 类型 Type | 说明 Description |
| :--- | :--- | :--- |
| `model` | string | 调用时使用的模型 ID / Model ID used in requests |
| `provider` | string | `openai` · `anthropic` · `google` · `deepseek` · `zhipu` · `moonshot` · `bytedance` · `video` |
| `unit` | string | `USD/1M tokens` 或 or `USD/second` |
| `input` `output` | number \| null | 输入 / 输出标价 / Input and output list price |
| `cache_write` `cache_read` | number \| null | 缓存写入 / 读取标价，`null` 表示不适用 / Cache prices, `null` = n/a |
| `cache_write_1h` | number | 可选，1 小时缓存写入 / Optional, 1-hour cache write |
| `context` | string \| null | OpenAI 上下文档位，如 `≤272K` / OpenAI context tier, e.g. `≤272K` |
| `condition` | string | 可选，如 GLM 的 `input<32K` / Optional, e.g. GLM `input<32K` |
| `same_price` | string[] | 可选，同价模型 ID / Optional, model IDs with the same price |
| `peak` | string | 可选，DeepSeek 高峰时段规则 / Optional, DeepSeek peak-hour rule |
| `name` | string | 视频模型显示名 / Display name (video) |
| `prices` | object | 视频：分辨率 → 价格；按 token 计费时为 `{with_reference, without_reference}` / Video: resolution → price; per-token video uses `{with_reference, without_reference}` |

同一模型可能出现多次（例如不同上下文档位）。
A model may appear more than once (e.g. one entry per context tier).

## 示例条目 / Sample entry

```json
{
  "model": "gpt-5.5",
  "provider": "openai",
  "unit": "USD/1M tokens",
  "input": 5.0,
  "output": 30.0,
  "cache_write": null,
  "cache_read": 0.5,
  "context": "≤272K"
}
```

## 计算实付价 / Computing the price paid

```python
import json, urllib.request

url = "https://raw.githubusercontent.com/cutetailbud/FastAIToken/master/pricing.json"
p = json.load(urllib.request.urlopen(url))
mult = {g["id"]: g["multiplier"] for g in p["groups"]}

for m in p["models"]:
    if m["provider"] == "openai" and m["input"] is not None:
        paid = m["input"] * mult["openai-pro"]
        print(m["model"], m.get("context"), f"input ${paid:.4f} / 1M tokens")
```
