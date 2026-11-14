# Changelog

本文件记录所有值得注意的变更，格式遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。
All notable changes are documented here, following Keep a Changelog and Semantic Versioning.

## [Unreleased]

### Changed

- 国产模型按人民币计价，不再按 1/7.1 汇率估算折扣：改为逐个模型用「标价 ÷ 厂商官方人民币价」计算「相当于官方价」（各表新增该列，分组汇总显示约 5–10 折）；`pricing.json` 中国模新增 `official_cny`、`vs_official`，`cn-models` 分组改用 `vs_official_price_range`
- 国产模型价格更新：新增 `hy4`；DeepSeek、GLM 5.3 / 5.3 Flash、Kimi K3、豆包补充缓存写入价；豆包 Seed 2.1 Pro 调整为 $5.40 / $27.00 / $1.08

### Added

- 中英双语 GitHub Wiki：首页、快速开始、计费说明、模型与价格、pricing.json 说明、发票与企业合作、常见问题、参与贡献（由 `scripts/readme/wiki.py` 生成于 `wiki/`）
- `Wiki` 工作流：合并到 `master` 后自动将 `wiki/` 同步到 GitHub Wiki

## [1.0.0] - 2026-11-10

### Added

- 10 种语言的 README：简体中文、English、日本語、한국어、Русский、Қазақша、Tiếng Việt、ภาษาไทย、Bahasa Indonesia、Bahasa Melayu
- OpenAI、Claude、Gemini、DeepSeek、GLM、Kimi、豆包及视频模型价格表，含各分组相当于官方价的折扣
- 机器可读的价格数据 `pricing.json`
- Python / Node.js / curl 调用示例（`examples/`）
- README 生成脚本、单元测试与 CI（检查生成文件是否最新、价格是否等于标价 × 倍率）
- 社区文件：LICENSE、SECURITY、CONTRIBUTING、CODE_OF_CONDUCT、SUPPORT、Issue / PR 模板
- 面向 AI 的项目说明：`llms.txt`、`AGENTS.md`

[Unreleased]: https://github.com/cutetailbud/FastAIToken/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/cutetailbud/FastAIToken/releases/tag/v1.0.0
