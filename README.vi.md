<p align="center">
  <a href="https://www.fastaitoken.com/"><img src="./sponsor-fastai.png" alt="FastAIToken" width="600"></a>
</p>

<p align="center">

[简体中文](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Русский](./README.ru.md) | [Қазақша](./README.kk.md) | **Tiếng Việt** | [ภาษาไทย](./README.th.md) | [Bahasa Indonesia](./README.id.md) | [Bahasa Melayu](./README.ms.md)

</p>

# FastAIToken

> Nền tảng tổng hợp API mô hình ngôn ngữ lớn trọn gói —— **[https://www.fastaitoken.com/](https://www.fastaitoken.com/)**

FastAIToken tổng hợp các mô hình ngôn ngữ lớn và mô hình tạo video hàng đầu trong và ngoài Trung Quốc. Chỉ với một tài khoản và một API key, bạn có thể gọi GPT, Claude, Gemini, Grok, DeepSeek, GLM, Kimi cùng các mô hình video như Seedance, MiniMax H3, Wan 3.0, Veo 3.1.

## ✨ Ưu điểm nền tảng

- 💱 **1 NDT = 1 USD**: nạp tiền bằng Nhân dân tệ quy đổi 1:1 sang hạn mức USD, giá cả phải chăng
- 🧠 **Đầy đủ mô hình**: GPT / Claude / Gemini / Grok / DeepSeek / GLM / Kimi / Doubao Seed
- 🎬 **Mô hình video**: Seedance 2.0 / 2.5, MiniMax H3, Wan 3.0, Veo 3.1, tính phí theo giây hoặc theo token
- 🧾 **Tự xuất hóa đơn**: gửi ticket trong trang quản trị để nhận hóa đơn VAT **chuyên dụng** hoặc **thông thường** của Trung Quốc
- 🏢 **Hợp tác doanh nghiệp**: tuyến riêng cho doanh nghiệp có SLA, hỗ trợ chuyển khoản công ty
- 🔀 **Nhiều nhóm**: mỗi mô hình có nhiều tuyến / nhóm, tùy chọn cân bằng giữa giá và độ ổn định

## 🧮 Cách tính phí

**Giá thực trả = Giá niêm yết × Hệ số nhóm**

Đơn vị giá bên dưới là **USD / 1M tokens** (trừ video tính theo giây), định dạng `giá thực trả (giá niêm yết)`. Giá có thể thay đổi bất cứ lúc nào — **giá trên website là chuẩn**.

💡 **Rẻ hơn giá chính thức bao nhiêu?** Giá chính thức tính bằng USD, còn tại đây **1 NDT = 1 USD hạn mức**, sau đó nhân với hệ số nhóm. Với tỷ giá 1 USD ≈ 7.1 NDT:

**Chi phí thực ≈ giá chính thức × hệ số ÷ 7.1**

Ví dụ nhóm 0.3x: 0.3 ÷ 7.1 ≈ **4.2%** giá chính thức.

### Mức giảm thực tế theo nhóm

| Nhóm | Hệ số | So với giá chính thức |
| --- | --- | --- |
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

---

## 🤖 OpenAI ChatGPT

10 mô hình, 5 nhóm:

| Nhóm | Hệ số | So với giá chính thức | Nhãn |
| --- | --- | --- | --- |
| Nhóm ưu đãi OpenAI | 0.06x | ≈ 0.85% | Thấp nhất · Có thời hạn |
| Nhóm thường OpenAI | 0.2x | ≈ 2.8% | Có thời hạn |
| Kênh dự phòng OpenAI | 0.25x | ≈ 3.5% | Có thời hạn |
| Tuyến OpenAI Pro | 0.3x | ≈ 4.2% | Có thời hạn |
| Tuyến doanh nghiệp OpenAI Pro | 0.5x | ≈ 7.0% | Riêng · SLA |

> gpt-5.6-luna sử dụng mô hình Terra và tính phí theo terra (cùng giá với gpt-5.6-terra).

Giá bên dưới tính theo «Tuyến OpenAI Pro» 0.3x:

| Mô hình | Ngữ cảnh | Đầu vào | Đầu ra | Ghi cache | Đọc cache |
| --- | --- | --- | --- | --- | --- |
| gpt-5.4 | — | $0.75 ($2.50) | $4.50 ($15.00) | — | $0.075 ($0.25) |
| gpt-5.4-mini | — | $0.225 ($0.75) | $1.35 ($4.50) | — | $0.0225 ($0.075) |
| gpt-5.5 | ≤272K | $1.50 ($5.00) | $9.00 ($30.00) | — | $0.15 ($0.50) |
| gpt-5.5 | >272K | $3.00 ($10.00) | $18.00 ($60.00) | — | $0.30 ($1.00) |
| gpt-5.6-luna / terra | ≤272K | $0.60 ($2.00) | $3.60 ($12.00) | $0.75 ($2.50) | $0.06 ($0.20) |
| gpt-5.6-luna / terra | >272K | $1.20 ($4.00) | $7.20 ($24.00) | $1.50 ($5.00) | $0.12 ($0.40) |
| gpt-5.6-sol | ≤272K | $1.50 ($5.00) | $9.00 ($30.00) | $1.875 ($6.25) | $0.15 ($0.50) |
| gpt-5.6-sol | >272K | $3.00 ($10.00) | $13.50 ($45.00) | $3.75 ($12.50) | $0.30 ($1.00) |
| gpt-6-astra | ≤272K | $3.00 ($10.00) | $15.00 ($50.00) | $3.75 ($12.50) | $0.30 ($1.00) |
| gpt-6-astra | >272K | $6.00 ($20.00) | $22.50 ($75.00) | $7.50 ($25.00) | $0.60 ($2.00) |
| gpt-6-sol | ≤272K | $0.60 ($2.00) | $3.00 ($10.00) | $0.75 ($2.50) | $0.06 ($0.20) |
| gpt-6-sol | >272K | $1.20 ($4.00) | $6.00 ($20.00) | $1.50 ($5.00) | $0.12 ($0.40) |
| gpt-6.1-sol | ≤272K | $0.60 ($2.00) | $3.00 ($10.00) | $0.75 ($2.50) | $0.03 ($0.10) |
| gpt-6.1-sol | >272K | $1.20 ($4.00) | $6.00 ($20.00) | $1.50 ($5.00) | $0.06 ($0.20) |
| gpt-6.1-terra | — | $0.30 ($1.00) | $1.50 ($5.00) | $0.375 ($1.25) | $0.015 ($0.05) |

---

## 🟠 Claude Max (Anthropic)

Kênh đầy đủ sức mạnh từ gói MAX chính thức. 14 mô hình, 2 nhóm:

| Nhóm | Hệ số | So với giá chính thức | Nhãn |
| --- | --- | --- | --- |
| Nhóm Claude Max | 1.5x | ≈ 21.1% | Thấp nhất |
| Tuyến doanh nghiệp Claude Max | 1.9x | ≈ 26.8% | Riêng · SLA |

Giá bên dưới tính theo «Nhóm Claude Max» 1.5x:

| Mô hình | Cùng giá | Đầu vào | Đầu ra | Ghi cache | Đọc cache |
| --- | --- | --- | --- | --- | --- |
| claude-fable-5 | claude-fable-5-1 | $15.00 ($10.00) | $75.00 ($50.00) | $18.75 ($12.50) | $1.50 ($1.00) |
| claude-opus-5-5 | — | $6.00 ($4.00) | $30.00 ($20.00) | $7.50 ($5.00) | $0.30 ($0.20) |
| claude-opus-4-6 | claude-opus-4-7 / 4-8 / 5 | $7.50 ($5.00) | $37.50 ($25.00) | $9.375 ($6.25) | $0.75 ($0.50) |
| claude-sonnet-5 | claude-sonnet-5-5 | $3.00 ($2.00) | $15.00 ($10.00) | $3.75 ($2.50) | $0.30 ($0.20) |
| claude-sonnet-4-5 | claude-sonnet-4-6 | $4.50 ($3.00) | $22.50 ($15.00) | $5.625 ($3.75) | $0.45 ($0.30) |
| claude-haiku-5-5 | — | $0.15 ($0.10) | $0.75 ($0.50) | $0.1875 ($0.125) | $0.015 ($0.01) |
| claude-haiku-4-5 | claude-haiku-4-6 | $0.375 ($0.25) | $1.875 ($1.25) | $0.45 ($0.30) | $0.045 ($0.03) |

> Ghi cache 1 giờ: claude-opus-5-5 là $12.00, claude-haiku-5-5 là $0.30.

---

## 🔷 Gemini (Google)

Hỗ trợ Gemini 3.8 Flash / Gemini 4 Argon. Nhóm «Gemini Chat / Coding [argon4 mới]», hệ số **0.3x**:

| Mô hình | Đầu vào | Đầu ra | Đọc cache |
| --- | --- | --- | --- |
| gemini-3.8-flash | $0.225 ($0.75) | $1.125 ($3.75) | $0.0225 ($0.075) |
| gemini-4-argon | $0.60 ($2.00) | $3.00 ($10.00) | $0.03 ($0.10) |

---

## 🇨🇳 Mô hình Trung Quốc (DeepSeek / GLM / Kimi / Doubao)

28 mô hình, bao gồm DeepSeek V4 Pro, GLM 5.2. Nhóm «Mô hình TQ – DeepSeek / GLM» và «Điểm truy cập CN», hệ số **1x** (giảm giá động) — giá thực trả bằng giá niêm yết.

### DeepSeek

> ⏰ Giờ cao điểm ngày làm việc 09:00–12:00 và 14:00–18:00 (GMT+8): giá ×2

| Mô hình | Đầu vào | Đầu ra | Đọc cache |
| --- | --- | --- | --- |
| deepseek-v4-flash | $1.05 | $3.15 | $0.035 |
| deepseek-v4-pro | $3.15 | $9.45 | $0.105 |
| deepseek-v4.1-flash (cùng giá: deepseek-v4.1-flash-1017, deepseek/deepseek-flash) | $0.70 | $2.80 | $0.014 |

### Zhipu GLM

| Mô hình | Điều kiện | Đầu vào | Đầu ra | Đọc cache |
| --- | --- | --- | --- | --- |
| glm-5 | Đầu vào <32K | $4.00 | $18.00 | $1.00 |
| glm-5 | Đầu vào ≥32K | $6.00 | $22.00 | $1.50 |
| glm-5-turbo | Đầu vào <32K | $5.00 | $22.00 | $1.20 |
| glm-5-turbo | Đầu vào ≥32K | $7.00 | $26.00 | $1.80 |
| glm-5.1 | Đầu vào <32K | $3.60 | $14.40 | $0.78 |
| glm-5.1 | Đầu vào ≥32K | $4.80 | $16.80 | $1.20 |
| glm-5.2 | — | $5.60 | $19.60 | $1.40 |
| glm-5.3 | — | $6.40 | $22.40 | $1.60 |
| glm-5.3-flash | — | $0.64 | $2.24 | $0.184 |

### Kimi (Moonshot AI)

| Mô hình | Đầu vào | Đầu ra | Ghi cache | Đọc cache |
| --- | --- | --- | --- | --- |
| kimi-k3 | $19.00 | $95.00 | — | $1.90 |
| kimi-k3.1-pro | $13.00 | $68.00 | $13.00 (1 giờ: $26.00) | $1.30 |

### Doubao Seed (ByteDance)

| Mô hình | Đầu vào | Đầu ra | Đọc cache |
| --- | --- | --- | --- |
| doubao-seed-2-1-pro (cùng giá: doubao-seed-2-1-pro-260915) | $6.00 | $30.00 | $1.20 |

---

## 🎬 Mô hình video

18 mô hình, bao gồm Seedance 2.5 / MiniMax H3 / Veo 3.1 / Wan 3.0. Nhóm «Tạo video – seedance/h3», hệ số **1x**.

### Tính phí theo giây (USD / giây)

| Mô hình | ID mô hình | Mặc định | 480p | 720p | 768p | 1080p | 2K | 4K |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| H-Seedance 2.0 Lite | hseedance-2.0-lite-time | — | $0.297 | — | $0.375 | $0.50 | $0.625 | $0.75 |
| H-Seedance 2.0 Pro Mini | hseedance-2.0-pro-mini-time | — | $0.209 | $0.412 | $0.412 | $0.90 | $0.99 | $1.089 |
| H-Seedance 2.0 Pro Fast | hseedance-2.0-pro-fast-time | — | $0.335 | $0.645 | $0.645 | $1.40 | $1.54 | $1.694 |
| H-Seedance 2.0 Pro | hseedance-2.0-pro-time | — | $0.416 | $0.795 | $0.795 | $1.73 | $4.30 | $4.90 |
| H-Seedance 2.5 Pro | hseedance-2.5-pro-time | — | $0.606 | $1.188 | $1.188 | $2.587 | $6.37 | $7.007 |
| Seedance 2.0 Fast / Seedance 2.0 | seedance-2.0-fast-time | — | $0.45 | $0.59 | — | $0.70 | — | — |
| MiniMax H3 | minimax-h3-time | — | — | — | $0.07 | $0.08 | — | — |
| Wan 3.0 Video | wan-3.0-time | — | $0.30 | $0.60 | — | $1.30 | — | — |
| Veo 3.1 | veo3.1-time | $0.14 | — | — | — | — | — | — |
| auto-video-hd | auto-video-hd, ll2-auto-hd | — | — | $0.0001 | — | $0.0001 | $0.0001 | — |

### Tính phí theo token (USD / 1M tokens)

Định dạng: `có video tham chiếu / không tham chiếu`

| Mô hình | ID mô hình | 480p | 720p | 1080p | 4K |
| --- | --- | --- | --- | --- | --- |
| Seedance 2.0 Mini | seedance-2.0-mini-token | $12.60 / $20.70 | $12.60 / $20.70 | $13.95 / $22.95 | — |
| Seedance 2.0 Fast | seedance-2.0-fast-token | $19.80 / $33.30 | $19.80 / $33.30 | $22.05 / $37.80 | — |
| Seedance 2.0 Pro | seedance-2.0-pro-token | $25.20 / $41.40 | $25.20 / $41.40 | $27.90 / $45.90 | $14.40 / $23.40 |
| Seedance 2.0 | seedance-2.0-token | $28.00 / $46.00 | $28.00 / $46.00 | $31.00 / $51.00 | $16.00 / $26.00 |
| Seedance 2.5 Pro | seedance-2.5-pro-token | — | $37.80 / $63.00 | $41.85 / $69.30 | — |
| Seedance 2.5 | seedance-2.5-token | $42.00 / $70.00 | $42.00 / $70.00 | $33.12 / $55.44 | — |

---

## 🚀 Bắt đầu nhanh

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

## 🧾 Hóa đơn & hợp tác doanh nghiệp

- **Hóa đơn**: đăng nhập → gửi ticket để yêu cầu hóa đơn VAT chuyên dụng hoặc thông thường (Trung Quốc)
- **SLA doanh nghiệp**: các nhóm riêng như Tuyến doanh nghiệp OpenAI Pro, Tuyến doanh nghiệp Claude Max được đảm bảo SLA
- **Chuyển khoản công ty**: hỗ trợ nạp tiền bằng chuyển khoản công ty và hợp tác — liên hệ hỗ trợ qua website

## 📮 Liên hệ

Website: [https://www.fastaitoken.com/](https://www.fastaitoken.com/)

---

> Thông tin giá trong kho này chỉ mang tính tham khảo. Giá thực tế, danh sách mô hình và hệ số nhóm theo hiển thị trên website.
