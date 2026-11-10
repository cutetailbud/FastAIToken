# Security Policy / 安全策略

## 报告漏洞 / Reporting a vulnerability

请**不要**在公开 Issue 或 QQ 群中披露安全问题。
Please **do not** disclose security issues in public issues or the QQ group.

- GitHub：通过 [Private vulnerability reporting](https://github.com/cutetailbud/FastAIToken/security/advisories/new) 私下提交
- 平台本身的问题（账户、API Key、计费）：登录 [https://www.fastaitoken.com/](https://www.fastaitoken.com/) 后台提交工单，并注明「安全」

我们会在 3 个工作日内确认收到，并在修复后告知你。
We aim to acknowledge reports within 3 business days and will notify you once fixed.

## API Key 泄露 / Leaked API key

如果你的 API Key 被提交到了公开仓库或聊天记录中：

1. 立即在控制台删除该 Key 并重新创建
2. 检查控制台用量记录是否有异常调用
3. 如有异常扣费，提交工单说明情况

If your key was exposed, delete and recreate it in the console immediately, check usage logs, and open a ticket for any unexpected charges.

## 范围 / Scope

本仓库包含文档、价格数据与示例代码。示例从环境变量读取 Key，请勿将 Key 写入代码。
This repository holds docs, pricing data and examples. Examples read the key from environment variables — never hard-code it.
