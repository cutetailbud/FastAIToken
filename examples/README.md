# Examples / 示例

FastAIToken 兼容 OpenAI 接口，可直接使用官方 OpenAI SDK。
FastAIToken is OpenAI-compatible, so the official OpenAI SDKs work as-is.

所有示例都从环境变量读取配置 / All examples read their settings from environment variables:

| 变量 Variable | 说明 Description |
| :--- | :--- |
| `FASTAITOKEN_API_KEY` | 控制台创建的 API Key / API key from the console |
| `FASTAITOKEN_BASE_URL` | 控制台显示的 Base URL / Base URL shown in the console |
| `FASTAITOKEN_MODEL` | 可选，默认 `gpt-5.5` / Optional, defaults to `gpt-5.5` |

| 语言 Language | 文件 File | 运行 Run |
| :--- | :--- | :--- |
| Python | [`python/chat.py`](./python/chat.py) | `pip install openai && python examples/python/chat.py "你好"` |
| Node.js | [`node/chat.mjs`](./node/chat.mjs) | `npm install openai && node examples/node/chat.mjs "你好"` |
| curl | [`curl/chat.sh`](./curl/chat.sh) | `bash examples/curl/chat.sh` |

可用模型与价格见 [README](../README.md) 或 [`pricing.json`](../pricing.json)。
