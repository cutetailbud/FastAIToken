# Language-neutral price data
OAI = [
    ("gpt-5.4", "—", "0.75/2.50", "4.50/15.00", "-", "0.075/0.25"),
    ("gpt-5.4-mini", "—", "0.225/0.75", "1.35/4.50", "-", "0.0225/0.075"),
    ("gpt-5.5", "≤272K", "1.50/5.00", "9.00/30.00", "-", "0.15/0.50"),
    ("gpt-5.5", ">272K", "3.00/10.00", "18.00/60.00", "-", "0.30/1.00"),
    ("gpt-5.6-luna / terra", "≤272K", "0.60/2.00", "3.60/12.00", "0.75/2.50", "0.06/0.20"),
    ("gpt-5.6-luna / terra", ">272K", "1.20/4.00", "7.20/24.00", "1.50/5.00", "0.12/0.40"),
    ("gpt-5.6-sol", "≤272K", "1.50/5.00", "9.00/30.00", "1.875/6.25", "0.15/0.50"),
    ("gpt-5.6-sol", ">272K", "3.00/10.00", "13.50/45.00", "3.75/12.50", "0.30/1.00"),
    ("gpt-6-astra", "≤272K", "3.00/10.00", "15.00/50.00", "3.75/12.50", "0.30/1.00"),
    ("gpt-6-astra", ">272K", "6.00/20.00", "22.50/75.00", "7.50/25.00", "0.60/2.00"),
    ("gpt-6-sol", "≤272K", "0.60/2.00", "3.00/10.00", "0.75/2.50", "0.06/0.20"),
    ("gpt-6-sol", ">272K", "1.20/4.00", "6.00/20.00", "1.50/5.00", "0.12/0.40"),
    ("gpt-6.1-sol", "≤272K", "0.60/2.00", "3.00/10.00", "0.75/2.50", "0.03/0.10"),
    ("gpt-6.1-sol", ">272K", "1.20/4.00", "6.00/20.00", "1.50/5.00", "0.06/0.20"),
    ("gpt-6.1-terra", "—", "0.30/1.00", "1.50/5.00", "0.375/1.25", "0.015/0.05"),
]

CLAUDE = [
    ("claude-fable-5", "claude-fable-5-1", "15.00/10.00", "75.00/50.00", "18.75/12.50", "1.50/1.00"),
    ("claude-opus-5-5", "—", "6.00/4.00", "30.00/20.00", "7.50/5.00", "0.30/0.20"),
    ("claude-opus-4-6", "claude-opus-4-7 / 4-8 / 5", "7.50/5.00", "37.50/25.00", "9.375/6.25", "0.75/0.50"),
    ("claude-sonnet-5", "claude-sonnet-5-5", "3.00/2.00", "15.00/10.00", "3.75/2.50", "0.30/0.20"),
    ("claude-sonnet-4-5", "claude-sonnet-4-6", "4.50/3.00", "22.50/15.00", "5.625/3.75", "0.45/0.30"),
    ("claude-haiku-5-5", "—", "0.15/0.10", "0.75/0.50", "0.1875/0.125", "0.015/0.01"),
    ("claude-haiku-4-5", "claude-haiku-4-6", "0.375/0.25", "1.875/1.25", "0.45/0.30", "0.045/0.03"),
]

GEMINI = [
    ("gemini-3.8-flash", "0.225/0.75", "1.125/3.75", "0.0225/0.075"),
    ("gemini-4-argon", "0.60/2.00", "3.00/10.00", "0.03/0.10"),
]

# Chinese models are priced in CNY: 1 CNY = 1 USD of credit, so no exchange-rate gap. The discount is
# list price / the vendor's official CNY price (OFFICIAL_CNY below).
# Cache write is the vendor group's price; the "CN access point" group has no cache write.

# (model, same-price aliases or None, weekday peak x2, in, out, cache write, cache read)
DEEPSEEK = [
    ("deepseek-v4-flash", None, True, "1.05", "3.15", "1.05", "0.035"),
    ("deepseek-v4-pro", None, True, "3.15", "9.45", "3.15", "0.105"),
    ("deepseek-v4.1-flash", "deepseek-v4.1-flash-1017, deepseek/deepseek-flash", True, "0.70", "2.80", "0.70", "0.014"),
    ("hy4", None, False, "3.00", "9.00", "3.00", "0.15"),
]

# (model, cond key: lt / ge / None, in, out, cache write, cache read)
GLM = [
    ("glm-5", "lt", "4.00", "18.00", "-", "1.00"),
    ("glm-5", "ge", "6.00", "22.00", "-", "1.50"),
    ("glm-5-turbo", "lt", "5.00", "22.00", "-", "1.20"),
    ("glm-5-turbo", "ge", "7.00", "26.00", "-", "1.80"),
    ("glm-5.1", "lt", "3.60", "14.40", "-", "0.78"),
    ("glm-5.1", "ge", "4.80", "16.80", "-", "1.20"),
    ("glm-5.2", None, "5.60", "19.60", "-", "1.40"),
    ("glm-5.3", None, "6.40", "22.40", "6.40", "1.60"),
    ("glm-5.3-flash", None, "0.64", "2.24", "0.64", "0.184"),
]

# (model, in, out, cache write, 1-hour cache write, cache read)
KIMI = [
    ("kimi-k3", "19.00", "95.00", "19.00", "38.00", "1.90"),
    ("kimi-k3.1-pro", "13.00", "68.00", "13.00", "26.00", "1.30"),
]

# (model, same-price aliases or None, in, out, cache write, cache read)
DOUBAO = [
    ("doubao-seed-2-1-pro", "doubao-seed-2-1-pro-260915", "5.40", "27.00", "5.40", "1.08"),
]

# Vendor official CNY prices per 1M tokens: (in, out, cache read or None if unknown).
# DeepSeek: off-peak price (peak x2 on both sides). hy4: list price (vendor runs 50% off until 2026-12-31).
OFFICIAL_AS_OF = "2026-11"
OFFICIAL_CNY = {
    ("deepseek-v4-flash", None): ("1.00", "4.00", "0.02"),
    ("deepseek-v4-pro", None): ("4.50", "13.50", "0.15"),
    ("deepseek-v4.1-flash", None): ("1.00", "4.00", "0.02"),
    ("hy4", None): ("6.00", "18.00", "0.30"),
    ("glm-5", "lt"): ("4.00", "18.00", "1.00"),
    ("glm-5", "ge"): ("6.00", "22.00", "1.50"),
    ("glm-5-turbo", "lt"): ("5.00", "22.00", None),
    ("glm-5-turbo", "ge"): ("7.00", "26.00", None),
    ("glm-5.1", "lt"): ("6.00", "24.00", "1.30"),
    ("glm-5.1", "ge"): ("8.00", "28.00", None),
    ("glm-5.2", None): ("8.00", "28.00", "2.00"),
    ("glm-5.3", None): ("8.00", "28.00", "2.00"),
    ("glm-5.3-flash", None): ("0.80", "2.80", "0.23"),
    ("kimi-k3", None): ("20.00", "100.00", "2.00"),
    ("kimi-k3.1-pro", None): ("13.00", "68.00", "1.30"),
    ("doubao-seed-2-1-pro", None): ("6.00", "30.00", "1.20"),
}

# (name, model id, default, 480p, 720p, 768p, 1080p, 2k, 4k)
VIDEO_SEC = [
    ("H-Seedance 2.0 Lite", "hseedance-2.0-lite-time", "-", "0.297", "-", "0.375", "0.50", "0.625", "0.75"),
    ("H-Seedance 2.0 Pro Mini", "hseedance-2.0-pro-mini-time", "-", "0.209", "0.412", "0.412", "0.90", "0.99", "1.089"),
    ("H-Seedance 2.0 Pro Fast", "hseedance-2.0-pro-fast-time", "-", "0.335", "0.645", "0.645", "1.40", "1.54", "1.694"),
    ("H-Seedance 2.0 Pro", "hseedance-2.0-pro-time", "-", "0.416", "0.795", "0.795", "1.73", "4.30", "4.90"),
    ("H-Seedance 2.5 Pro", "hseedance-2.5-pro-time", "-", "0.606", "1.188", "1.188", "2.587", "6.37", "7.007"),
    ("Seedance 2.0 Fast / Seedance 2.0", "seedance-2.0-fast-time", "-", "0.45", "0.59", "-", "0.70", "-", "-"),
    ("MiniMax H3", "minimax-h3-time", "-", "-", "-", "0.07", "0.08", "-", "-"),
    ("Wan 3.0 Video", "wan-3.0-time", "-", "0.30", "0.60", "-", "1.30", "-", "-"),
    ("Veo 3.1", "veo3.1-time", "0.14", "-", "-", "-", "-", "-", "-"),
    ("auto-video-hd", "auto-video-hd, ll2-auto-hd", "-", "-", "0.0001", "-", "0.0001", "0.0001", "-"),
]

# (name, model id, 480p, 720p, 1080p, 4k) each "ref/noref"
VIDEO_TOK = [
    ("Seedance 2.0 Mini", "seedance-2.0-mini-token", "12.60/20.70", "12.60/20.70", "13.95/22.95", "-"),
    ("Seedance 2.0 Fast", "seedance-2.0-fast-token", "19.80/33.30", "19.80/33.30", "22.05/37.80", "-"),
    ("Seedance 2.0 Pro", "seedance-2.0-pro-token", "25.20/41.40", "25.20/41.40", "27.90/45.90", "14.40/23.40"),
    ("Seedance 2.0", "seedance-2.0-token", "28.00/46.00", "28.00/46.00", "31.00/51.00", "16.00/26.00"),
    ("Seedance 2.5 Pro", "seedance-2.5-pro-token", "-", "37.80/63.00", "41.85/69.30", "-"),
    ("Seedance 2.5", "seedance-2.5-token", "42.00/70.00", "42.00/70.00", "33.12/55.44", "-"),
]
