RATE = 7.1  # assumed USD/CNY exchange rate used to estimate discount vs official price

# c_disc: column header; disc_explain: paragraph ({rate}, {ex_pct}, {ex_zhe}); sum_title; group names
E = {
    "zh": dict(c_disc="相当于官方价", sum_title="各分组折扣一览",
               disc_explain="💡 **相当于官方价几折？** 官方按美元计价，而本平台 **1 元 = 1 美元额度**，消费时再乘以分组倍率。按 1 美元 ≈ {rate} 元估算：\n\n**实际人民币成本 = 官方价（美元）× 分组倍率 × 1 元 ≈ 官方价 × 倍率 ÷ {rate}**\n\n例如 0.3x 分组：0.3 ÷ {rate} ≈ {ex_pct}，约 **{ex_zhe}**。",
               gem="Gemini Chat / Coding", cn="国模分组 - Deepseek / Glm（含 Kimi / 豆包）", vid="视频生成分组 - seedance/h3"),
    "en": dict(c_disc="vs. official price", sum_title="Effective discount by group",
               disc_explain="💡 **How much cheaper than official?** Official prices are in USD, but here **1 CNY buys 1 USD of credit**, and usage is then multiplied by the group multiplier. Assuming 1 USD ≈ {rate} CNY:\n\n**Actual cost ≈ official price × multiplier ÷ {rate}**\n\nE.g. a 0.3x group: 0.3 ÷ {rate} ≈ **{ex_pct}** of the official price.",
               gem="Gemini Chat / Coding", cn="CN Models – DeepSeek / GLM (incl. Kimi / Doubao)", vid="Video Generation – seedance/h3"),
    "ja": dict(c_disc="公式価格比", sum_title="グループ別の実質割引率",
               disc_explain="💡 **公式価格の何割？** 公式価格は米ドル建てですが、当プラットフォームは **1 人民元 = 1 米ドル分**、利用時にグループ倍率を掛けます。1 米ドル ≈ {rate} 人民元とすると：\n\n**実質コスト ≈ 公式価格 × 倍率 ÷ {rate}**\n\n例：0.3x グループは 0.3 ÷ {rate} ≈ 公式価格の **{ex_pct}**。",
               gem="Gemini Chat / Coding", cn="中国モデル - DeepSeek / GLM（Kimi / Doubao 含む）", vid="動画生成 - seedance/h3"),
    "ko": dict(c_disc="공식가 대비", sum_title="그룹별 실질 할인율",
               disc_explain="💡 **공식가 대비 얼마나 저렴한가요?** 공식가는 달러 기준이지만 본 플랫폼은 **1위안 = 1달러 크레딧**이며, 사용 시 그룹 배율을 곱합니다. 1달러 ≈ {rate}위안 기준:\n\n**실제 비용 ≈ 공식가 × 배율 ÷ {rate}**\n\n예: 0.3x 그룹은 0.3 ÷ {rate} ≈ 공식가의 **{ex_pct}**.",
               gem="Gemini Chat / Coding", cn="중국 모델 - DeepSeek / GLM (Kimi / Doubao 포함)", vid="동영상 생성 - seedance/h3"),
    "ru": dict(c_disc="От официальной цены", sum_title="Фактическая скидка по группам",
               disc_explain="💡 **Насколько дешевле официальной цены?** Официальные цены указаны в долларах, а у нас **1 юань = 1 доллар баланса**, затем расход умножается на множитель группы. При курсе 1 USD ≈ {rate} CNY:\n\n**Фактическая стоимость ≈ официальная цена × множитель ÷ {rate}**\n\nНапример, группа 0.3x: 0.3 ÷ {rate} ≈ **{ex_pct}** от официальной цены.",
               gem="Gemini Chat / Coding", cn="Китайские модели – DeepSeek / GLM (вкл. Kimi / Doubao)", vid="Генерация видео – seedance/h3"),
    "kk": dict(c_disc="Ресми бағадан", sum_title="Топтар бойынша нақты жеңілдік",
               disc_explain="💡 **Ресми бағадан қаншалықты арзан?** Ресми бағалар долларда, ал бізде **1 юань = 1 доллар баланс**, кейін шығын топ коэффициентіне көбейтіледі. 1 USD ≈ {rate} CNY бағамымен:\n\n**Нақты құн ≈ ресми баға × коэффициент ÷ {rate}**\n\nМысалы, 0.3x тобы: 0.3 ÷ {rate} ≈ ресми бағаның **{ex_pct}**.",
               gem="Gemini Chat / Coding", cn="Қытай модельдері – DeepSeek / GLM (Kimi / Doubao қоса)", vid="Бейне генерациялау – seedance/h3"),
    "vi": dict(c_disc="So với giá chính thức", sum_title="Mức giảm thực tế theo nhóm",
               disc_explain="💡 **Rẻ hơn giá chính thức bao nhiêu?** Giá chính thức tính bằng USD, còn tại đây **1 NDT = 1 USD hạn mức**, sau đó nhân với hệ số nhóm. Với tỷ giá 1 USD ≈ {rate} NDT:\n\n**Chi phí thực ≈ giá chính thức × hệ số ÷ {rate}**\n\nVí dụ nhóm 0.3x: 0.3 ÷ {rate} ≈ **{ex_pct}** giá chính thức.",
               gem="Gemini Chat / Coding", cn="Mô hình TQ – DeepSeek / GLM (gồm Kimi / Doubao)", vid="Tạo video – seedance/h3"),
    "th": dict(c_disc="เทียบราคาทางการ", sum_title="ส่วนลดจริงแยกตามกลุ่ม",
               disc_explain="💡 **ถูกกว่าราคาทางการเท่าไร?** ราคาทางการเป็นดอลลาร์ แต่ที่นี่ **1 หยวน = เครดิต 1 ดอลลาร์** แล้วคูณด้วยตัวคูณกลุ่มตอนใช้งาน ที่อัตรา 1 USD ≈ {rate} CNY:\n\n**ต้นทุนจริง ≈ ราคาทางการ × ตัวคูณ ÷ {rate}**\n\nเช่น กลุ่ม 0.3x: 0.3 ÷ {rate} ≈ **{ex_pct}** ของราคาทางการ",
               gem="Gemini Chat / Coding", cn="โมเดลจีน – DeepSeek / GLM (รวม Kimi / Doubao)", vid="สร้างวิดีโอ – seedance/h3"),
    "id": dict(c_disc="Dibanding harga resmi", sum_title="Diskon efektif per grup",
               disc_explain="💡 **Seberapa murah dibanding harga resmi?** Harga resmi dalam USD, sedangkan di sini **1 CNY = kredit 1 USD**, lalu pemakaian dikalikan pengali grup. Dengan kurs 1 USD ≈ {rate} CNY:\n\n**Biaya nyata ≈ harga resmi × pengali ÷ {rate}**\n\nContoh grup 0.3x: 0.3 ÷ {rate} ≈ **{ex_pct}** dari harga resmi.",
               gem="Gemini Chat / Coding", cn="Model CN – DeepSeek / GLM (termasuk Kimi / Doubao)", vid="Pembuatan Video – seedance/h3"),
    "ms": dict(c_disc="Berbanding harga rasmi", sum_title="Diskaun efektif mengikut kumpulan",
               disc_explain="💡 **Berapa murah berbanding harga rasmi?** Harga rasmi dalam USD, tetapi di sini **1 CNY = kredit 1 USD**, kemudian penggunaan didarab dengan pengganda kumpulan. Pada kadar 1 USD ≈ {rate} CNY:\n\n**Kos sebenar ≈ harga rasmi × pengganda ÷ {rate}**\n\nContoh kumpulan 0.3x: 0.3 ÷ {rate} ≈ **{ex_pct}** daripada harga rasmi.",
               gem="Gemini Chat / Coding", cn="Model CN – DeepSeek / GLM (termasuk Kimi / Doubao)", vid="Penjanaan Video – seedance/h3"),
}


def pct(m):
    p = m / RATE * 100
    return f"{p:.2f}%" if p < 1 else f"{p:.1f}%"


def disc(code, m):
    if code == "zh":
        return f"约 {m / RATE * 10:.2f} 折（{pct(m)}）"
    return f"≈ {pct(m)}"
