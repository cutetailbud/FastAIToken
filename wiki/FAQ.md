# 常见问题 / FAQ

### 1 元真的等于 1 美元吗？ / Is 1 CNY really 1 USD?

是的，充值的人民币按 1:1 兑换为美元额度，消费时再按 `标价 × 分组倍率` 扣除。
Yes. Top-ups convert CNY to USD credit at 1:1; usage is then charged at `list price × group multiplier`.

### Claude 倍率大于 1，还便宜吗？ / Claude multipliers are above 1. Is it still cheaper?

是的。由于 1 元 = 1 美元额度，1.5x 分组的人民币成本约为官方价的 21.1%（按 1 美元 ≈ 7.1 元估算）。
Yes. Because 1 CNY buys 1 USD of credit, a 1.5x group costs about 21.1% of the official price (at 1 USD ≈ 7.1 CNY).

### Base URL 在哪里？ / Where do I find the base URL?

登录官网控制台查看。示例与本 Wiki 都通过 `FASTAITOKEN_BASE_URL` 环境变量读取。
In the console on the website. The examples and this wiki read it from `FASTAITOKEN_BASE_URL`.

### 返回 401 / 鉴权失败 / I get 401 / authentication errors

检查 Key 是否完整、未被删除，Base URL 是否与控制台一致，请求头格式为 `Authorization: Bearer <key>`。
Check that the key is complete and not deleted, that the base URL matches the console, and that the header is `Authorization: Bearer <key>`.

### 提示模型不存在 / The model is reported as not found

确认模型 ID 拼写正确（见 [模型与价格 / Models and Pricing](Models-and-Pricing)），并且该模型在你 Key 所属的分组中可用。
Check the model ID spelling (see [模型与价格 / Models and Pricing](Models-and-Pricing)) and that the model is available in your key's group.

### 请求被限流或不稳定 / Requests are rate-limited or unstable

稍后重试并使用指数退避；对稳定性要求高的业务建议使用企业 SLA 线路，或为备用分组单独创建 Key。
Retry with exponential backoff. For workloads that need stability, use an enterprise SLA line or keep a key for a backup group.

### Key 泄露了怎么办？ / My key leaked. What now?

立即在控制台删除该 Key 并创建新 Key。请勿在 Issue、QQ 群等公开渠道粘贴 Key。
Delete it in the console right away and create a new one. Never paste keys in issues, the QQ group or other public places.

### 文档价格与官网不一致 / Prices here differ from the website

以官网实时价格为准。欢迎通过 [Issue](https://github.com/cutetailbud/FastAIToken/issues/new/choose) 告诉我们。
The live website prices prevail. Please let us know via an [issue](https://github.com/cutetailbud/FastAIToken/issues/new/choose).

### 如何开发票？ / How do I get an invoice?

登录后台提交工单，支持增值税专用发票与普通发票，详见 [发票与企业合作 / Invoices and Enterprise](Invoices-and-Enterprise)。
Open a ticket in the dashboard; VAT special and general invoices are supported. See [发票与企业合作 / Invoices and Enterprise](Invoices-and-Enterprise).

没有找到答案？见 [SUPPORT](https://github.com/cutetailbud/FastAIToken/blob/master/SUPPORT.md) 或加入 QQ 交流群 **1019537221**。
Still stuck? See [SUPPORT](https://github.com/cutetailbud/FastAIToken/blob/master/SUPPORT.md) or join QQ group **1019537221**.
