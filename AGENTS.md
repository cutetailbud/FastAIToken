# AGENTS.md

Guidance for AI coding agents working in this repository.

## What this repo is

Documentation for FastAIToken (https://www.fastaitoken.com/), an LLM and video-model API gateway.
It contains multilingual READMEs, machine-readable pricing (`pricing.json`), and usage examples.
There is no application code; the only code is the README generator and its tests.

## Golden rule

`README*.md`, `pricing.json` and `wiki/*.md` are **generated**. Never edit them by hand
(and never edit the GitHub Wiki in the browser: the `Wiki` workflow overwrites it from `wiki/`).

| To change | Edit |
| :--- | :--- |
| Prices, models | `scripts/readme/data.py` |
| Wording in any language | `scripts/readme/i18n.py` |
| Exchange rate, discount wording | `scripts/readme/extra.py` |
| Layout, QQ group, JSON schema | `scripts/readme/gen.py` |
| Wiki pages (zh + en) | `scripts/readme/wiki.py` |

Then run:

```bash
python scripts/readme/gen.py .            # regenerate
python -m unittest discover -s tests      # must pass
python scripts/readme/gen.py . --check    # what CI runs
```

## Data conventions

- Prices are USD per 1M tokens unless the unit says otherwise (video: USD per second).
- In `data.py`, `"a/b"` means `discounted/list`; `"-"` means not applicable.
- Discounted price must equal list price × group multiplier (OpenAI Pro line 0.3, Claude Max 1.5, Gemini 0.3). Tests enforce this.
- Users pay 1 CNY per 1 USD of credit; `RATE` in `extra.py` is only used to estimate the discount vs. official prices.
- Chinese models are priced in CNY, so `RATE` does not apply: their discount is list price ÷ the vendor's official CNY price (`OFFICIAL_CNY` in `data.py`, one entry per table row). Update it together with the prices.

## Other rules

- Python standard library only; keep compatibility with Python 3.10+.
- Keep all 10 languages in sync: tests fail if a key is missing in one language.
- The wiki is bilingual (简体中文 + English) and reuses the zh / en strings from `i18n.py` where possible.
- Do not add emoji to the READMEs.
- Examples read the key from `FASTAITOKEN_API_KEY` and the endpoint from `FASTAITOKEN_BASE_URL`. Never hard-code keys.
- Commit messages follow Conventional Commits. Add user-facing changes to `CHANGELOG.md` under `[Unreleased]`.
