RATE = 7.1  # assumed USD/CNY exchange rate used to estimate discount vs official price
# Chinese models are priced in CNY, so RATE does not apply to them: see OFFICIAL_CNY in data.py.

# c_disc: column header; disc_explain: paragraph ({rate}, {ex_pct}, {ex_zhe}); sum_title; group names
E = {
    "zh": dict(cn_eq="与官方价相同", cn_range="约 {lo}–{hi} 折（因模型而异）",
               cn_fx="国产模型本身按人民币计价，不存在汇率差：标价按 **1 元 = 1 美元** 直接与厂商官方人民币价对比，即「相当于官方价」= 标价 ÷ 官方价。多数模型低于官方价，见各表最后一列（官方价取自厂商价格页，{date}）。",
               c_disc="相当于官方价", sum_title="各分组折扣一览",
               disc_explain="💡 **相当于官方价几折？** 官方按美元计价，而本平台 **1 元 = 1 美元额度**，消费时再乘以分组倍率。按 1 美元 ≈ {rate} 元估算：\n\n**实际人民币成本 = 官方价（美元）× 分组倍率 × 1 元 ≈ 官方价 × 倍率 ÷ {rate}**\n\n例如 0.3x 分组：0.3 ÷ {rate} ≈ {ex_pct}，约 **{ex_zhe}**。",
               gem="Gemini Chat / Coding", cn="国模分组 - Deepseek / Glm（含 Kimi / 豆包）", vid="视频生成分组 - seedance/h3"),
    "en": dict(cn_eq="Same as official", cn_range="≈ {lo}–{hi}% (varies by model)",
               cn_fx="Chinese models are priced in CNY, so there is no exchange-rate gap: the list price is compared directly with the vendor's official CNY price at **1 CNY = 1 USD**, i.e. vs. official = list price ÷ official price. Most models are below the official price; see the last column of each table (official prices from vendor pricing pages, {date}).",
               c_disc="vs. official price", sum_title="Effective discount by group",
               disc_explain="💡 **How much cheaper than official?** Official prices are in USD, but here **1 CNY buys 1 USD of credit**, and usage is then multiplied by the group multiplier. Assuming 1 USD ≈ {rate} CNY:\n\n**Actual cost ≈ official price × multiplier ÷ {rate}**\n\nE.g. a 0.3x group: 0.3 ÷ {rate} ≈ **{ex_pct}** of the official price.",
               gem="Gemini Chat / Coding", cn="CN Models – DeepSeek / GLM (incl. Kimi / Doubao)", vid="Video Generation – seedance/h3"),
    "ja": dict(cn_eq="公式価格と同じ", cn_range="公式価格の約 {lo}–{hi}%（モデルにより異なる）",
               cn_fx="中国製モデルはもともと人民元建てのため為替差はありません。定価を **1 人民元 = 1 米ドル** でメーカー公式の人民元価格と直接比較し、公式価格比 = 定価 ÷ 公式価格です。多くのモデルが公式価格より安く、各表の最後の列をご覧ください（公式価格は各社料金ページ、{date} 時点）。",
               c_disc="公式価格比", sum_title="グループ別の実質割引率",
               disc_explain="💡 **公式価格の何割？** 公式価格は米ドル建てですが、当プラットフォームは **1 人民元 = 1 米ドル分**、利用時にグループ倍率を掛けます。1 米ドル ≈ {rate} 人民元とすると：\n\n**実質コスト ≈ 公式価格 × 倍率 ÷ {rate}**\n\n例：0.3x グループは 0.3 ÷ {rate} ≈ 公式価格の **{ex_pct}**。",
               gem="Gemini Chat / Coding", cn="中国モデル - DeepSeek / GLM（Kimi / Doubao 含む）", vid="動画生成 - seedance/h3"),
    "ko": dict(cn_eq="공식가와 동일", cn_range="공식가의 약 {lo}–{hi}% (모델별 상이)",
               cn_fx="중국 모델은 원래 위안화 기준이라 환율 차이가 없습니다. 정가를 **1위안 = 1달러**로 제조사 공식 위안화 가격과 직접 비교하며, 공식가 대비 = 정가 ÷ 공식가입니다. 대부분 모델이 공식가보다 저렴하며 각 표의 마지막 열을 참고하세요(공식가는 제조사 요금 페이지 기준, {date}).",
               c_disc="공식가 대비", sum_title="그룹별 실질 할인율",
               disc_explain="💡 **공식가 대비 얼마나 저렴한가요?** 공식가는 달러 기준이지만 본 플랫폼은 **1위안 = 1달러 크레딧**이며, 사용 시 그룹 배율을 곱합니다. 1달러 ≈ {rate}위안 기준:\n\n**실제 비용 ≈ 공식가 × 배율 ÷ {rate}**\n\n예: 0.3x 그룹은 0.3 ÷ {rate} ≈ 공식가의 **{ex_pct}**.",
               gem="Gemini Chat / Coding", cn="중국 모델 - DeepSeek / GLM (Kimi / Doubao 포함)", vid="동영상 생성 - seedance/h3"),
    "ru": dict(cn_eq="Как официальная", cn_range="≈ {lo}–{hi}% (зависит от модели)",
               cn_fx="Китайские модели изначально тарифицируются в юанях, поэтому курсовой разницы нет: базовая цена напрямую сравнивается с официальной ценой производителя в CNY по курсу **1 CNY = 1 USD**, т. е. «от официальной цены» = базовая цена ÷ официальная. Большинство моделей дешевле официальной цены — см. последний столбец таблиц (официальные цены со страниц производителей, {date}).",
               c_disc="От официальной цены", sum_title="Фактическая скидка по группам",
               disc_explain="💡 **Насколько дешевле официальной цены?** Официальные цены указаны в долларах, а у нас **1 юань = 1 доллар баланса**, затем расход умножается на множитель группы. При курсе 1 USD ≈ {rate} CNY:\n\n**Фактическая стоимость ≈ официальная цена × множитель ÷ {rate}**\n\nНапример, группа 0.3x: 0.3 ÷ {rate} ≈ **{ex_pct}** от официальной цены.",
               gem="Gemini Chat / Coding", cn="Китайские модели – DeepSeek / GLM (вкл. Kimi / Doubao)", vid="Генерация видео – seedance/h3"),
    "kk": dict(cn_eq="Ресми бағамен бірдей", cn_range="≈ {lo}–{hi}% (модельге байланысты)",
               cn_fx="Қытай модельдері бастапқыдан юаньмен бағаланады, сондықтан бағам айырмасы жоқ: баға өндірушінің ресми юань бағасымен **1 CNY = 1 USD** бойынша тікелей салыстырылады, яғни «ресми бағадан» = баға ÷ ресми баға. Модельдердің көбі ресми бағадан арзан — кестелердің соңғы бағанын қараңыз (ресми бағалар өндірушілер беттерінен, {date}).",
               c_disc="Ресми бағадан", sum_title="Топтар бойынша нақты жеңілдік",
               disc_explain="💡 **Ресми бағадан қаншалықты арзан?** Ресми бағалар долларда, ал бізде **1 юань = 1 доллар баланс**, кейін шығын топ коэффициентіне көбейтіледі. 1 USD ≈ {rate} CNY бағамымен:\n\n**Нақты құн ≈ ресми баға × коэффициент ÷ {rate}**\n\nМысалы, 0.3x тобы: 0.3 ÷ {rate} ≈ ресми бағаның **{ex_pct}**.",
               gem="Gemini Chat / Coding", cn="Қытай модельдері – DeepSeek / GLM (Kimi / Doubao қоса)", vid="Бейне генерациялау – seedance/h3"),
    "vi": dict(cn_eq="Bằng giá chính thức", cn_range="≈ {lo}–{hi}% (tùy mô hình)",
               cn_fx="Mô hình Trung Quốc vốn tính bằng NDT nên không có chênh lệch tỷ giá: giá niêm yết được so sánh trực tiếp với giá NDT chính thức của nhà cung cấp theo **1 NDT = 1 USD**, tức so với giá chính thức = giá niêm yết ÷ giá chính thức. Phần lớn mô hình rẻ hơn giá chính thức, xem cột cuối của mỗi bảng (giá chính thức lấy từ trang giá của nhà cung cấp, {date}).",
               c_disc="So với giá chính thức", sum_title="Mức giảm thực tế theo nhóm",
               disc_explain="💡 **Rẻ hơn giá chính thức bao nhiêu?** Giá chính thức tính bằng USD, còn tại đây **1 NDT = 1 USD hạn mức**, sau đó nhân với hệ số nhóm. Với tỷ giá 1 USD ≈ {rate} NDT:\n\n**Chi phí thực ≈ giá chính thức × hệ số ÷ {rate}**\n\nVí dụ nhóm 0.3x: 0.3 ÷ {rate} ≈ **{ex_pct}** giá chính thức.",
               gem="Gemini Chat / Coding", cn="Mô hình TQ – DeepSeek / GLM (gồm Kimi / Doubao)", vid="Tạo video – seedance/h3"),
    "th": dict(cn_eq="เท่าราคาทางการ", cn_range="≈ {lo}–{hi}% (แตกต่างตามโมเดล)",
               cn_fx="โมเดลจีนคิดราคาเป็นหยวนอยู่แล้ว จึงไม่มีส่วนต่างอัตราแลกเปลี่ยน ราคาตั้งเทียบตรงกับราคาหยวนทางการของผู้ให้บริการที่ **1 หยวน = 1 ดอลลาร์** คือ เทียบราคาทางการ = ราคาตั้ง ÷ ราคาทางการ โมเดลส่วนใหญ่ถูกกว่าราคาทางการ ดูคอลัมน์สุดท้ายของแต่ละตาราง (ราคาทางการจากหน้าราคาของผู้ให้บริการ {date})",
               c_disc="เทียบราคาทางการ", sum_title="ส่วนลดจริงแยกตามกลุ่ม",
               disc_explain="💡 **ถูกกว่าราคาทางการเท่าไร?** ราคาทางการเป็นดอลลาร์ แต่ที่นี่ **1 หยวน = เครดิต 1 ดอลลาร์** แล้วคูณด้วยตัวคูณกลุ่มตอนใช้งาน ที่อัตรา 1 USD ≈ {rate} CNY:\n\n**ต้นทุนจริง ≈ ราคาทางการ × ตัวคูณ ÷ {rate}**\n\nเช่น กลุ่ม 0.3x: 0.3 ÷ {rate} ≈ **{ex_pct}** ของราคาทางการ",
               gem="Gemini Chat / Coding", cn="โมเดลจีน – DeepSeek / GLM (รวม Kimi / Doubao)", vid="สร้างวิดีโอ – seedance/h3"),
    "id": dict(cn_eq="Sama dengan resmi", cn_range="≈ {lo}–{hi}% (berbeda per model)",
               cn_fx="Model Tiongkok memang dihargai dalam CNY, jadi tidak ada selisih kurs: harga daftar dibandingkan langsung dengan harga resmi CNY vendor pada **1 CNY = 1 USD**, yaitu dibanding harga resmi = harga daftar ÷ harga resmi. Sebagian besar model lebih murah dari harga resmi; lihat kolom terakhir tiap tabel (harga resmi dari halaman harga vendor, {date}).",
               c_disc="Dibanding harga resmi", sum_title="Diskon efektif per grup",
               disc_explain="💡 **Seberapa murah dibanding harga resmi?** Harga resmi dalam USD, sedangkan di sini **1 CNY = kredit 1 USD**, lalu pemakaian dikalikan pengali grup. Dengan kurs 1 USD ≈ {rate} CNY:\n\n**Biaya nyata ≈ harga resmi × pengali ÷ {rate}**\n\nContoh grup 0.3x: 0.3 ÷ {rate} ≈ **{ex_pct}** dari harga resmi.",
               gem="Gemini Chat / Coding", cn="Model CN – DeepSeek / GLM (termasuk Kimi / Doubao)", vid="Pembuatan Video – seedance/h3"),
    "ms": dict(cn_eq="Sama dengan rasmi", cn_range="≈ {lo}–{hi}% (berbeza mengikut model)",
               cn_fx="Model China memang dihargakan dalam CNY, jadi tiada perbezaan kadar tukaran: harga senarai dibandingkan terus dengan harga rasmi CNY vendor pada **1 CNY = 1 USD**, iaitu berbanding harga rasmi = harga senarai ÷ harga rasmi. Kebanyakan model lebih murah daripada harga rasmi; lihat lajur terakhir setiap jadual (harga rasmi daripada halaman harga vendor, {date}).",
               c_disc="Berbanding harga rasmi", sum_title="Diskaun efektif mengikut kumpulan",
               disc_explain="💡 **Berapa murah berbanding harga rasmi?** Harga rasmi dalam USD, tetapi di sini **1 CNY = kredit 1 USD**, kemudian penggunaan didarab dengan pengganda kumpulan. Pada kadar 1 USD ≈ {rate} CNY:\n\n**Kos sebenar ≈ harga rasmi × pengganda ÷ {rate}**\n\nContoh kumpulan 0.3x: 0.3 ÷ {rate} ≈ **{ex_pct}** daripada harga rasmi.",
               gem="Gemini Chat / Coding", cn="Model CN – DeepSeek / GLM (termasuk Kimi / Doubao)", vid="Penjanaan Video – seedance/h3"),
}


def pct(m, rate=RATE):
    p = m / rate * 100
    return f"{p:.2f}%" if p < 1 else f"{p:.1f}%"


def disc(code, m, rate=RATE):
    if code == "zh":
        return f"约 {m / rate * 10:.2f} 折（{pct(m, rate)}）"
    return f"≈ {pct(m, rate)}"


def _g(x):
    return f"{x:.2f}".rstrip("0").rstrip(".")


def ratio(code, r):
    """list price / official CNY price, e.g. 0.7 -> '7 折' (zh) or '70%'."""
    if abs(r - 1) < 1e-9:
        return E[code]["cn_eq"]
    if code == "zh" and r < 1:
        return f"{_g(r * 10)} 折"
    return f"{_g(r * 100)}%"


def cn_range(code, lo, hi):
    k = 10 if code == "zh" else 100
    return E[code]["cn_range"].format(lo=_g(lo * k), hi=_g(hi * k))
