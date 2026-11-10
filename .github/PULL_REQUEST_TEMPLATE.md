## 变更说明 / Summary

<!-- 这次改了什么、为什么改 / What changed and why -->

## 类型 / Type

- [ ] 价格更新 / Price update
- [ ] 新增模型 / New model
- [ ] 文档或翻译 / Docs or translation
- [ ] 脚本或 CI / Script or CI

## 自查 / Checklist

- [ ] 只修改了 `scripts/readme/*.py`，README 与 `pricing.json` 由 `python scripts/readme/gen.py .` 生成
      Edited only `scripts/readme/*.py`; READMEs and `pricing.json` were regenerated
- [ ] `python -m unittest discover -s tests` 通过 / tests pass
- [ ] 已在 `CHANGELOG.md` 的 Unreleased 下记录 / Added an entry under Unreleased in `CHANGELOG.md`
