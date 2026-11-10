<div align="center">

<a href="https://www.fastaitoken.com/"><img src="./sponsor-fastai.png" alt="FastAIToken" width="560"></a>

<p><b>Nền tảng tổng hợp API mô hình ngôn ngữ lớn trọn gói</b></p>

<p><a href="https://www.fastaitoken.com/">Website</a> &nbsp;|&nbsp; Nhóm QQ: <b>1019537221</b></p>

<p><sub><a href="./README.md">简体中文</a> · <a href="./README.en.md">English</a> · <a href="./README.ja.md">日本語</a> · <a href="./README.ko.md">한국어</a> · <a href="./README.ru.md">Русский</a> · <a href="./README.kk.md">Қазақша</a> · <b>Tiếng Việt</b> · <a href="./README.th.md">ภาษาไทย</a> · <a href="./README.id.md">Bahasa Indonesia</a> · <a href="./README.ms.md">Bahasa Melayu</a></sub></p>

<p>
  <a href="https://github.com/cutetailbud/FastAIToken/actions/workflows/ci.yml"><img src="https://github.com/cutetailbud/FastAIToken/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/cutetailbud/FastAIToken/releases"><img src="https://img.shields.io/github/v/release/cutetailbud/FastAIToken" alt="Release"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/github/license/cutetailbud/FastAIToken" alt="License"></a>
  <a href="./pricing.json"><img src="https://img.shields.io/badge/pricing-JSON-blue" alt="pricing.json"></a>
</p>

</div>

<br>

FastAIToken tổng hợp các mô hình ngôn ngữ lớn và mô hình tạo video hàng đầu trong và ngoài Trung Quốc. Chỉ với một tài khoản và một API key, bạn có thể gọi GPT, Claude, Gemini, Grok, DeepSeek, GLM, Kimi cùng các mô hình video như Seedance, MiniMax H3, Wan 3.0, Veo 3.1.

## Ưu điểm nền tảng

- **1 NDT = 1 USD**: nạp tiền bằng Nhân dân tệ quy đổi 1:1 sang hạn mức USD, giá cả phải chăng
- **Đầy đủ mô hình**: GPT / Claude / Gemini / Grok / DeepSeek / GLM / Kimi / Doubao Seed
- **Mô hình video**: Seedance 2.0 / 2.5, MiniMax H3, Wan 3.0, Veo 3.1, tính phí theo giây hoặc theo token
- **Tự xuất hóa đơn**: gửi ticket trong trang quản trị để nhận hóa đơn VAT **chuyên dụng** hoặc **thông thường** của Trung Quốc
- **Hợp tác doanh nghiệp**: tuyến riêng cho doanh nghiệp có SLA, hỗ trợ chuyển khoản công ty
- **Nhiều nhóm**: mỗi mô hình có nhiều tuyến / nhóm, tùy chọn cân bằng giữa giá và độ ổn định

## Cách tính phí

```
Giá thực trả = Giá niêm yết × Hệ số nhóm
```

Đơn vị giá bên dưới là **USD / 1M tokens** (trừ video tính theo giây), định dạng `giá thực trả (giá niêm yết)`. Giá có thể thay đổi bất cứ lúc nào — **giá trên website là chuẩn**.

**Rẻ hơn giá chính thức bao nhiêu?** Giá chính thức tính bằng USD, còn tại đây **1 NDT = 1 USD hạn mức**, sau đó nhân với hệ số nhóm. Với tỷ giá 1 USD ≈ 7.1 NDT:

**Chi phí thực ≈ giá chính thức × hệ số ÷ 7.1**

Ví dụ nhóm 0.3x: 0.3 ÷ 7.1 ≈ **4.2%** giá chính thức.

### Mức giảm thực tế theo nhóm

| Nhóm | Hệ số | So với giá chính thức |
| :--- | ---: | ---: |
| Nhóm ưu đãi OpenAI | 0.06x | ≈ 0.85% |
| Nhóm thường OpenAI | 0.2x | ≈ 2.8% |
| Kênh dự phòng OpenAI | 0.25x | ≈ 3.5% |
| Tuyến OpenAI Pro | 0.3x | ≈ 4.2% |
| Tuyến doanh nghiệp OpenAI Pro | 0.5x | ≈ 7.0% |
| Nhóm Claude Max | 1.5x | ≈ 21.1% |
| Tuyến doanh nghiệp Claude Max | 1.9x | ≈ 26.8% |
| Gemini Chat / Coding | 0.3x | ≈ 4.2% |
| Mô hình TQ – DeepSeek / GLM (gồm Kimi / Doubao) | 1x | ≈ 14.1% |
| Tạo video – seedance/h3 | 1x | ≈ 14.1% |

## OpenAI

10 mô hình, 5 nhóm:

| Nhóm | Hệ số | So với giá chính thức | Nhãn |
| :--- | ---: | ---: | :--- |
| Nhóm ưu đãi OpenAI | 0.06x | ≈ 0.85% | Thấp nhất · Có thời hạn |
| Nhóm thường OpenAI | 0.2x | ≈ 2.8% | Có thời hạn |
| Kênh dự phòng OpenAI | 0.25x | ≈ 3.5% | Có thời hạn |
| Tuyến OpenAI Pro | 0.3x | ≈ 4.2% | Có thời hạn |
| Tuyến doanh nghiệp OpenAI Pro | 0.5x | ≈ 7.0% | Riêng · SLA |

Giá bên dưới tính theo «Tuyến OpenAI Pro» 0.3x:

| Mô hình | Ngữ cảnh | Đầu vào | Đầu ra | Ghi cache | Đọc cache |
| :--- | :---: | ---: | ---: | ---: | ---: |
| `gpt-5.4` | — | $0.75 <sub>($2.50)</sub> | $4.50 <sub>($15.00)</sub> | — | $0.075 <sub>($0.25)</sub> |
| `gpt-5.4-mini` | — | $0.225 <sub>($0.75)</sub> | $1.35 <sub>($4.50)</sub> | — | $0.0225 <sub>($0.075)</sub> |
| `gpt-5.5` | ≤272K | $1.50 <sub>($5.00)</sub> | $9.00 <sub>($30.00)</sub> | — | $0.15 <sub>($0.50)</sub> |
| `gpt-5.5` | >272K | $3.00 <sub>($10.00)</sub> | $18.00 <sub>($60.00)</sub> | — | $0.30 <sub>($1.00)</sub> |
| `gpt-5.6-luna / terra` | ≤272K | $0.60 <sub>($2.00)</sub> | $3.60 <sub>($12.00)</sub> | $0.75 <sub>($2.50)</sub> | $0.06 <sub>($0.20)</sub> |
| `gpt-5.6-luna / terra` | >272K | $1.20 <sub>($4.00)</sub> | $7.20 <sub>($24.00)</sub> | $1.50 <sub>($5.00)</sub> | $0.12 <sub>($0.40)</sub> |
| `gpt-5.6-sol` | ≤272K | $1.50 <sub>($5.00)</sub> | $9.00 <sub>($30.00)</sub> | $1.875 <sub>($6.25)</sub> | $0.15 <sub>($0.50)</sub> |
| `gpt-5.6-sol` | >272K | $3.00 <sub>($10.00)</sub> | $13.50 <sub>($45.00)</sub> | $3.75 <sub>($12.50)</sub> | $0.30 <sub>($1.00)</sub> |
| `gpt-6-astra` | ≤272K | $3.00 <sub>($10.00)</sub> | $15.00 <sub>($50.00)</sub> | $3.75 <sub>($12.50)</sub> | $0.30 <sub>($1.00)</sub> |
| `gpt-6-astra` | >272K | $6.00 <sub>($20.00)</sub> | $22.50 <sub>($75.00)</sub> | $7.50 <sub>($25.00)</sub> | $0.60 <sub>($2.00)</sub> |
| `gpt-6-sol` | ≤272K | $0.60 <sub>($2.00)</sub> | $3.00 <sub>($10.00)</sub> | $0.75 <sub>($2.50)</sub> | $0.06 <sub>($0.20)</sub> |
| `gpt-6-sol` | >272K | $1.20 <sub>($4.00)</sub> | $6.00 <sub>($20.00)</sub> | $1.50 <sub>($5.00)</sub> | $0.12 <sub>($0.40)</sub> |
| `gpt-6.1-sol` | ≤272K | $0.60 <sub>($2.00)</sub> | $3.00 <sub>($10.00)</sub> | $0.75 <sub>($2.50)</sub> | $0.03 <sub>($0.10)</sub> |
| `gpt-6.1-sol` | >272K | $1.20 <sub>($4.00)</sub> | $6.00 <sub>($20.00)</sub> | $1.50 <sub>($5.00)</sub> | $0.06 <sub>($0.20)</sub> |
| `gpt-6.1-terra` | — | $0.30 <sub>($1.00)</sub> | $1.50 <sub>($5.00)</sub> | $0.375 <sub>($1.25)</sub> | $0.015 <sub>($0.05)</sub> |

> gpt-5.6-luna sử dụng mô hình Terra và tính phí theo terra (cùng giá với gpt-5.6-terra).

## Claude (Anthropic)

Kênh đầy đủ sức mạnh từ gói MAX chính thức. 14 mô hình, 2 nhóm:

| Nhóm | Hệ số | So với giá chính thức | Nhãn |
| :--- | ---: | ---: | :--- |
| Nhóm Claude Max | 1.5x | ≈ 21.1% | Thấp nhất |
| Tuyến doanh nghiệp Claude Max | 1.9x | ≈ 26.8% | Riêng · SLA |

Giá bên dưới tính theo «Nhóm Claude Max» 1.5x:

| Mô hình | Cùng giá | Đầu vào | Đầu ra | Ghi cache | Đọc cache |
| :--- | :--- | ---: | ---: | ---: | ---: |
| `claude-fable-5` | `claude-fable-5-1` | $15.00 <sub>($10.00)</sub> | $75.00 <sub>($50.00)</sub> | $18.75 <sub>($12.50)</sub> | $1.50 <sub>($1.00)</sub> |
| `claude-opus-5-5` | — | $6.00 <sub>($4.00)</sub> | $30.00 <sub>($20.00)</sub> | $7.50 <sub>($5.00)</sub> | $0.30 <sub>($0.20)</sub> |
| `claude-opus-4-6` | `claude-opus-4-7 / 4-8 / 5` | $7.50 <sub>($5.00)</sub> | $37.50 <sub>($25.00)</sub> | $9.375 <sub>($6.25)</sub> | $0.75 <sub>($0.50)</sub> |
| `claude-sonnet-5` | `claude-sonnet-5-5` | $3.00 <sub>($2.00)</sub> | $15.00 <sub>($10.00)</sub> | $3.75 <sub>($2.50)</sub> | $0.30 <sub>($0.20)</sub> |
| `claude-sonnet-4-5` | `claude-sonnet-4-6` | $4.50 <sub>($3.00)</sub> | $22.50 <sub>($15.00)</sub> | $5.625 <sub>($3.75)</sub> | $0.45 <sub>($0.30)</sub> |
| `claude-haiku-5-5` | — | $0.15 <sub>($0.10)</sub> | $0.75 <sub>($0.50)</sub> | $0.1875 <sub>($0.125)</sub> | $0.015 <sub>($0.01)</sub> |
| `claude-haiku-4-5` | `claude-haiku-4-6` | $0.375 <sub>($0.25)</sub> | $1.875 <sub>($1.25)</sub> | $0.45 <sub>($0.30)</sub> | $0.045 <sub>($0.03)</sub> |

> Ghi cache 1 giờ: claude-opus-5-5 là $12.00, claude-haiku-5-5 là $0.30.

## Gemini (Google)

Hỗ trợ Gemini 3.8 Flash / Gemini 4 Argon. Nhóm «Gemini Chat / Coding [argon4 mới]», hệ số **0.3x**:

| Mô hình | Đầu vào | Đầu ra | Đọc cache |
| :--- | ---: | ---: | ---: |
| `gemini-3.8-flash` | $0.225 <sub>($0.75)</sub> | $1.125 <sub>($3.75)</sub> | $0.0225 <sub>($0.075)</sub> |
| `gemini-4-argon` | $0.60 <sub>($2.00)</sub> | $3.00 <sub>($10.00)</sub> | $0.03 <sub>($0.10)</sub> |

## Mô hình Trung Quốc (DeepSeek / GLM / Kimi / Doubao)

28 mô hình, bao gồm DeepSeek V4 Pro, GLM 5.2. Nhóm «Mô hình TQ – DeepSeek / GLM» và «Điểm truy cập CN», hệ số **1x** (giảm giá động) — giá thực trả bằng giá niêm yết.

### DeepSeek

> Giờ cao điểm ngày làm việc 09:00–12:00 và 14:00–18:00 (GMT+8): giá ×2

| Mô hình | Đầu vào | Đầu ra | Đọc cache |
| :--- | ---: | ---: | ---: |
| `deepseek-v4-flash` | $1.05 | $3.15 | $0.035 |
| `deepseek-v4-pro` | $3.15 | $9.45 | $0.105 |
| `deepseek-v4.1-flash`<br><sub>cùng giá: deepseek-v4.1-flash-1017, deepseek/deepseek-flash</sub> | $0.70 | $2.80 | $0.014 |

### Zhipu GLM

| Mô hình | Điều kiện | Đầu vào | Đầu ra | Đọc cache |
| :--- | :---: | ---: | ---: | ---: |
| `glm-5` | Đầu vào <32K | $4.00 | $18.00 | $1.00 |
| `glm-5` | Đầu vào ≥32K | $6.00 | $22.00 | $1.50 |
| `glm-5-turbo` | Đầu vào <32K | $5.00 | $22.00 | $1.20 |
| `glm-5-turbo` | Đầu vào ≥32K | $7.00 | $26.00 | $1.80 |
| `glm-5.1` | Đầu vào <32K | $3.60 | $14.40 | $0.78 |
| `glm-5.1` | Đầu vào ≥32K | $4.80 | $16.80 | $1.20 |
| `glm-5.2` | — | $5.60 | $19.60 | $1.40 |
| `glm-5.3` | — | $6.40 | $22.40 | $1.60 |
| `glm-5.3-flash` | — | $0.64 | $2.24 | $0.184 |

### Kimi (Moonshot AI)

| Mô hình | Đầu vào | Đầu ra | Ghi cache | Đọc cache |
| :--- | ---: | ---: | ---: | ---: |
| `kimi-k3` | $19.00 | $95.00 | — | $1.90 |
| `kimi-k3.1-pro` | $13.00 | $68.00 | $13.00<br><sub>1 giờ: $26.00</sub> | $1.30 |

### Doubao Seed (ByteDance)

| Mô hình | Đầu vào | Đầu ra | Đọc cache |
| :--- | ---: | ---: | ---: |
| `doubao-seed-2-1-pro`<br><sub>cùng giá: doubao-seed-2-1-pro-260915</sub> | $6.00 | $30.00 | $1.20 |

## Mô hình video

18 mô hình, bao gồm Seedance 2.5 / MiniMax H3 / Veo 3.1 / Wan 3.0. Nhóm «Tạo video – seedance/h3», hệ số **1x**.

### Tính phí theo giây (USD / giây)

| Mô hình | Mặc định | 480p | 720p | 768p | 1080p | 2K | 4K |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| H-Seedance 2.0 Lite<br><sub>hseedance-2.0-lite-time</sub> | — | $0.297 | — | $0.375 | $0.50 | $0.625 | $0.75 |
| H-Seedance 2.0 Pro Mini<br><sub>hseedance-2.0-pro-mini-time</sub> | — | $0.209 | $0.412 | $0.412 | $0.90 | $0.99 | $1.089 |
| H-Seedance 2.0 Pro Fast<br><sub>hseedance-2.0-pro-fast-time</sub> | — | $0.335 | $0.645 | $0.645 | $1.40 | $1.54 | $1.694 |
| H-Seedance 2.0 Pro<br><sub>hseedance-2.0-pro-time</sub> | — | $0.416 | $0.795 | $0.795 | $1.73 | $4.30 | $4.90 |
| H-Seedance 2.5 Pro<br><sub>hseedance-2.5-pro-time</sub> | — | $0.606 | $1.188 | $1.188 | $2.587 | $6.37 | $7.007 |
| Seedance 2.0 Fast / Seedance 2.0<br><sub>seedance-2.0-fast-time</sub> | — | $0.45 | $0.59 | — | $0.70 | — | — |
| MiniMax H3<br><sub>minimax-h3-time</sub> | — | — | — | $0.07 | $0.08 | — | — |
| Wan 3.0 Video<br><sub>wan-3.0-time</sub> | — | $0.30 | $0.60 | — | $1.30 | — | — |
| Veo 3.1<br><sub>veo3.1-time</sub> | $0.14 | — | — | — | — | — | — |
| auto-video-hd<br><sub>auto-video-hd, ll2-auto-hd</sub> | — | — | $0.0001 | — | $0.0001 | $0.0001 | — |

### Tính phí theo token (USD / 1M tokens)

Định dạng: `có video tham chiếu / không tham chiếu`

| Mô hình | 480p | 720p | 1080p | 4K |
| :--- | ---: | ---: | ---: | ---: |
| Seedance 2.0 Mini<br><sub>seedance-2.0-mini-token</sub> | $12.60 / $20.70 | $12.60 / $20.70 | $13.95 / $22.95 | — |
| Seedance 2.0 Fast<br><sub>seedance-2.0-fast-token</sub> | $19.80 / $33.30 | $19.80 / $33.30 | $22.05 / $37.80 | — |
| Seedance 2.0 Pro<br><sub>seedance-2.0-pro-token</sub> | $25.20 / $41.40 | $25.20 / $41.40 | $27.90 / $45.90 | $14.40 / $23.40 |
| Seedance 2.0<br><sub>seedance-2.0-token</sub> | $28.00 / $46.00 | $28.00 / $46.00 | $31.00 / $51.00 | $16.00 / $26.00 |
| Seedance 2.5 Pro<br><sub>seedance-2.5-pro-token</sub> | — | $37.80 / $63.00 | $41.85 / $69.30 | — |
| Seedance 2.5<br><sub>seedance-2.5-token</sub> | $42.00 / $70.00 | $42.00 / $70.00 | $33.12 / $55.44 | — |

## Bắt đầu nhanh

1. Truy cập [https://www.fastaitoken.com/](https://www.fastaitoken.com/) để đăng ký
2. Nạp tiền (1 NDT = 1 USD hạn mức)
3. Tạo API key trong bảng điều khiển và chọn nhóm
4. Cấu hình key và Base URL hiển thị trong bảng điều khiển vào ứng dụng / SDK / công cụ lập trình

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-xxxxxxxx",  # tạo trong bảng điều khiển FastAIToken
    base_url="<Base URL trong bảng điều khiển>",
)

resp = client.chat.completions.create(
    model="gpt-5.5",
    messages=[{"role": "user", "content": "Xin chào!"}],
)
print(resp.choices[0].message.content)
```

[examples/](./examples) · [pricing.json](./pricing.json) · [CHANGELOG](./CHANGELOG.md) · [CONTRIBUTING](./CONTRIBUTING.md) · [SECURITY](./SECURITY.md) · [SUPPORT](./SUPPORT.md)

## Hóa đơn & hợp tác doanh nghiệp

- **Hóa đơn**: đăng nhập → gửi ticket để yêu cầu hóa đơn VAT chuyên dụng hoặc thông thường (Trung Quốc)
- **SLA doanh nghiệp**: các nhóm riêng như Tuyến doanh nghiệp OpenAI Pro, Tuyến doanh nghiệp Claude Max được đảm bảo SLA
- **Chuyển khoản công ty**: hỗ trợ nạp tiền bằng chuyển khoản công ty và hợp tác — liên hệ hỗ trợ qua website

## Liên hệ

- Website: [https://www.fastaitoken.com/](https://www.fastaitoken.com/)
- Nhóm QQ: **1019537221**

---

<sub>Thông tin giá trong kho này chỉ mang tính tham khảo. Giá thực tế, danh sách mô hình và hệ số nhóm theo hiển thị trên website.</sub>
