# 快速开始 / Quick Start

## 1. 开通账号 / Get an API key

1. 访问 [https://www.fastaitoken.com/](https://www.fastaitoken.com/) 注册账号<br>Sign up at [https://www.fastaitoken.com/](https://www.fastaitoken.com/)
2. 充值（1 元 = 1 美元额度）<br>Top up (1 CNY = 1 USD credit)
3. 在控制台创建 API Key，并选择所需分组<br>Create an API key in the console and choose a group
4. 将 Key 与控制台提供的 Base URL 配置到你的应用 / SDK / 编程工具中即可调用<br>Configure the key and the Base URL shown in the console in your app / SDK / coding tool

不同分组价格与稳定性不同，选择方法见 [计费说明 / Billing](Billing)。
Groups differ in price and stability; see [计费说明 / Billing](Billing) for how to choose.

## 2. 配置环境变量 / Set environment variables

仓库中的示例统一从环境变量读取配置，请勿把 Key 写进代码或提交到仓库。
All examples read their settings from environment variables. Never hard-code a key or commit it.

| 变量 Variable | 说明 Description |
| :--- | :--- |
| `FASTAITOKEN_API_KEY` | 控制台创建的 API Key / API key from the console |
| `FASTAITOKEN_BASE_URL` | 控制台显示的 Base URL / Base URL shown in the console |
| `FASTAITOKEN_MODEL` | 可选，默认 `gpt-5.5` / Optional, defaults to `gpt-5.5` |

```bash
export FASTAITOKEN_API_KEY=sk-...
export FASTAITOKEN_BASE_URL=...   # 从控制台复制 / copy from the console
```

## 3. 发起请求 / Make a request

### Python

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["FASTAITOKEN_API_KEY"],
    base_url=os.environ["FASTAITOKEN_BASE_URL"],
)

resp = client.chat.completions.create(
    model="gpt-5.5",
    messages=[{"role": "user", "content": "你好！Hello!"}],
)
print(resp.choices[0].message.content)
```

### Node.js

```js
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.FASTAITOKEN_API_KEY,
  baseURL: process.env.FASTAITOKEN_BASE_URL,
});

const resp = await client.chat.completions.create({
  model: "gpt-5.5",
  messages: [{ role: "user", content: "你好！Hello!" }],
});
console.log(resp.choices[0].message.content);
```

### curl

```bash
curl -sS "${FASTAITOKEN_BASE_URL%/}/chat/completions" \
  -H "Authorization: Bearer ${FASTAITOKEN_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-5.5", "messages": [{"role": "user", "content": "Hello!"}]}'
```

完整可运行的示例（含流式输出）见 [examples/](https://github.com/cutetailbud/FastAIToken/tree/master/examples)。
Complete runnable examples (with streaming) are in [examples/](https://github.com/cutetailbud/FastAIToken/tree/master/examples).

## 4. 在其他工具中使用 / Use it in other tools

任何支持「OpenAI 兼容接口」或可自定义 Base URL 的客户端、SDK、编程工具都可以接入：填入控制台的 Base URL 与 API Key，模型名使用 [模型与价格 / Models and Pricing](Models-and-Pricing) 中的模型 ID 即可。
Any client, SDK or coding tool that supports an OpenAI-compatible API or a custom base URL works: enter the console's base URL and your API key, and use a model ID from [模型与价格 / Models and Pricing](Models-and-Pricing).

官方 OpenAI SDK 也会读取 `OPENAI_API_KEY` 与 `OPENAI_BASE_URL` 环境变量。
The official OpenAI SDKs also read the `OPENAI_API_KEY` and `OPENAI_BASE_URL` environment variables.

```bash
export OPENAI_API_KEY="$FASTAITOKEN_API_KEY"
export OPENAI_BASE_URL="$FASTAITOKEN_BASE_URL"
```

遇到报错请看 [常见问题 / FAQ](FAQ)。
Hitting errors? See [常见问题 / FAQ](FAQ).
