# Contributing / 贡献指南

感谢你帮助改进 FastAIToken 的文档！ Thanks for helping improve the FastAIToken docs!

## 仓库结构 / Layout

| 路径 Path | 说明 Description |
| :--- | :--- |
| `scripts/readme/data.py` | 价格数据（唯一数据源）/ Pricing data — single source of truth |
| `scripts/readme/i18n.py` | 各语言文案 / Text for each language |
| `scripts/readme/extra.py` | 汇率与折扣文案 / Exchange rate and discount wording |
| `scripts/readme/gen.py` | 生成 README 与 `pricing.json` / Generates READMEs and `pricing.json` |
| `scripts/readme/wiki.py` | 生成 Wiki 页面（中英双语）/ Generates the wiki pages (zh + en) |
| `README*.md`, `pricing.json`, `wiki/` | **生成文件，请勿手改** / **Generated — do not edit by hand** |
| `examples/` | 调用示例 / Usage examples |
| `tests/` | 测试 / Tests |

## 修改流程 / Workflow

```bash
# 1. 修改 scripts/readme/ 下的文件 / edit files in scripts/readme/
# 2. 重新生成 / regenerate
python scripts/readme/gen.py .
# 3. 测试 / test
python -m unittest discover -s tests
# 4. 在 CHANGELOG.md 的 [Unreleased] 下记录 / add an entry under [Unreleased]
```

CI 会检查生成文件是否最新、价格是否满足 `实付价 = 标价 × 倍率`。
CI verifies generated files are current and that every price satisfies `paid = list × multiplier`.

## Wiki

`wiki/` 合并到 `master` 后由 `Wiki` 工作流同步到 [GitHub Wiki](https://github.com/cutetailbud/FastAIToken/wiki)，请勿在网页上直接编辑。
首次使用需在仓库设置中启用 Wiki，并在网页上随便创建一个页面以初始化 Wiki 仓库。
After a merge to `master`, the `Wiki` workflow syncs `wiki/` to the GitHub Wiki; do not edit it in the browser.
First-time setup: enable Wiki in the repository settings and create any page in the browser to initialise the wiki repository.

## 新增语言 / Adding a language

1. 在 `i18n.py` 的 `ORDER` 中加入语言代码，并复制一份 `T["en"]` 翻译
2. 在 `extra.py` 的 `E` 与 `gen.py` 的 `QQ_LABEL` 中加入对应条目
3. 运行生成与测试 —— 测试会检查所有键是否齐全

## 提交规范 / Commit messages

使用 [Conventional Commits](https://www.conventionalcommits.org/)：`docs:`、`feat:`、`fix:`、`ci:`、`chore:`。

## 发布 / Releasing

1. 将 `CHANGELOG.md` 中的 `[Unreleased]` 改为新版本号与日期
2. `git tag vX.Y.Z && git push --tags` —— Release 工作流会自动创建 GitHub Release 并附上 `pricing.json`

请遵守 [行为准则](./CODE_OF_CONDUCT.md)。 Please follow the [Code of Conduct](./CODE_OF_CONDUCT.md).
