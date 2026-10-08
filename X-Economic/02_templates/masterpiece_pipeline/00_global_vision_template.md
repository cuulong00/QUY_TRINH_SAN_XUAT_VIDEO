# BẢN QUY HOẠCH TẦM NHÌN TOÀN CẢNH (GLOBAL VISION SYNTHESIS)
## KHUNG TƯ DUY PHỔ QUÁT 4 TẦNG (UNIVERSAL 4-TIER BLUEPRINT)

> ⚠️ **HƯỚNG DẪN DÀNH CHO AI AGENTS & SUBAGENTS (BẮT BUỘC TUÂN THỦ 100%):**
> 1. **BẢN ĐỒ ĐỊA HÌNH HIỆN THỰC (THE MAP OF REALITY):**
>    - Tệp này là **Bản đồ hiện thực khách quan** và là **Mỏ neo tư duy duy nhất (Single Cognitive Anchor)** của toàn bộ episode.
>    - Tệp mô tả khách quan vùng đất của đề tài: các chủ thể, động lực sinh tồn, quy luật vận hành ngầm, nghịch lý cốt lõi và kho dữ liệu thực chứng bất biến.
> 2. 🛑 **VÙNG CẤM TUYỆT ĐỐI (HARD REDLINE — CẤM CHIA CHƯƠNG TRƯỚC PHA 4):**
>    - **TUYỆT ĐỐI CẤM xuất hiện bất kỳ từ khóa cấu trúc kịch bản nào:** `CH01`, `CHXX`, `Chương`, `Hồi`, `Hook`, `Scene`, `Voiceover Tone`, `Narrative Bridge`, `Harvest`, `Seed`.
>    - Việc quyết định số chương (4 chương, 7 chương hay 12 chương), phân bổ thời lượng, nhịp điệu và chia nhỏ nội dung là **ĐẶC QUYỀN ĐỘC TÔN của Pha 4 (Master Outline Engine do `the_dialectic_architect` phụ trách)**.
>    - Tệp này **CHỈ VẼ BẢN ĐỒ HIỆN THỰC**, tuyệt đối không được kiêm nhiệm vai trò người dẫn tour (Guided Tour).
> 3. **TÍNH PHỔ QUÁT (UNIVERSAL APPLICATION):**
>    - Áp dụng cho **MỌI THỂ LOẠI ĐỀ TÀI**: Kinh tế vĩ mô, điều tra xã hội, hồ sơ nhân vật/vụ án, công nghệ, chính sách công hay tài chính cá nhân.
>    - Không ép buộc số lượng lực lượng hay hình học cố định; cấu trúc theo đúng bản chất cơ chế của đề tài.

---

## TẦNG 1: SYSTEM META-INSTRUCTIONS & COMPLIANCE GUARDRAILS

```yaml
meta_protocol:
  episode_slug: "[SLUG_CỦA_EPISODE]"
  topic_nature: "[KINH_TẾ_VĨ_MÔ / ĐIỀU_TRA_XÃ_HỘI / HỒ_SƠ_VỤ_ÁN / CHÍNH_SÁCH_CÔNG / CÔNG_NGHỆ]"
  core_phenomenon: "[HIỆN_TƯỢNG_BỀ_MẶT_HOẶC_BIẾN_CỐ_KHỞI_NGUỒN]"
  underlying_conflict: "[XUNG_ĐỘT_BẢN_CHẤT_GIỮA_CÁC_QUY_LUẬT_HOẶC_LỢI_ÍCH]"
  
editorial_dna:
  role: "Nhà quan sát độc lập / Phóng viên điều tra chính luận / Chuyên gia phân tích chính sách"
  tone: "Điềm tĩnh, sắc sảo, tri thức, tự sự điện ảnh (Cinematic Editorial Noir), giàu tính đối thoại thông minh"
  forbidden_attitudes:
    - "PR doanh nghiệp, thanh minh, bào chữa, quảng cáo thương mại"
    - "Thuyết giáo đạo đức, phán xét một chiều, hạ nhục cá nhân"
    - "Báo cáo hàn lâm khô khan, tiểu luận lý thuyết, từ đao to búa lớn sáo rỗng"
    - "Giật gân gián điệp, suy diễn thuyết âm mưu vô căn cứ"

compliance_blacklist:
  # Cặp từ cấm và từ ngữ thay thế an toàn chính luận
  - forbidden: "[TỪ_CẤM_NHẠY_CẢM_1]"
    replacement: "[TỪ_THAY_THẾ_CHUẨN_MỰC_1]"
  - forbidden: "[TỪ_CẤM_NHẠY_CẢM_2]"
    replacement: "[TỪ_THAY_THẾ_CHUẨN_MỰC_2]"

immutable_data_policy:
  enforcement: "STRICT_LOCK"
  rule: "Mọi số liệu, mốc sự kiện, văn bản pháp quy trong Tầng 4 là hằng số bất biến. Cấm tự ý bịa đặt, cấm làm tròn sai lệch bản chất."
```

#### 1.3. Bản Cáo Trạng Phản Đề Thép (The Strongest Opposing Thesis — Tri-Adversarial Red Team)
*(Bắt buộc xây dựng phiên bản phản biện sắc sảo, thông minh nhất từ phe đối lập trước khi tiến hành nghiên cứu sâu)*
- **1. Phản biện Lăng kính Thị trường & Chi phí cơ hội (The Market Skeptic):** [Luận điểm phản bác mạnh nhất: Méo mó phân bổ vốn, bao cấp làm triệt tiêu cạnh tranh lành mạnh, nguy cơ tạo doanh nghiệp xác sống, chi phí cơ hội của nền kinh tế].
- **2. Phản biện Lăng kính Thể chế & Địa chính trị (The Institutional Realist):** [Luận điểm phản bác mạnh nhất: Trắc trở thực thi bộ máy, xung đột lợi ích nội bộ, rủi ro bị điều tra chống bán phá giá / trả đũa thuế quan từ các đối tác thương mại lớn].
- **3. Phản biện Lăng kính Kế toán Dòng tiền & Thanh khoản (The Forensic Cash Auditor):** [Luận điểm phản bác mạnh nhất: Dòng tiền hoạt động kinh doanh âm kéo dài, lấy đòn bẩy nợ vay ngắn hạn tài trợ đầu tư dài hạn, áp lực tái cấp vốn và điểm hòa vốn phi thực tế].
- **Điều kiện sụp đổ của luận điểm chính (Falsification / Kill-Condition):** [Ngưỡng dữ liệu hoặc sự kiện thực tế nào nếu xảy ra sẽ chứng minh luận điểm chủ đạo của video là sai lầm?].

---

## TẦNG 2: MACRO LANDSCAPE & SYSTEMIC FORCES (BẢN ĐỒ KHÔNG GIAN & CÁC LỰC LƯỢNG)

### 1. Sơ đồ ASCII Không gian Hệ thống & Mạch vận động Lực lượng (Systemic Topography)
*(Vẽ sơ đồ ASCII thể hiện các chủ thể chính, các luồng tương tác — dòng tiền, quyền lực, thông tin, hàng hóa — và các điểm nghẽn/xung đột trọng điểm)*

```
[CHỦ THỂ A: VỊ THẾ & NGUỒN LỰC] ════ (Mạch vận động / Áp lực) ════► [ĐIỂM NGHẼN / CHIẾN TRƯỜNG TRUNG TÂM]
            ▲                                                                   │
            │ (Quy định / Rào cản)                                              │ (Tác động phản hồi)
            │                                                                   ▼
[CHỦ THỂ B: ĐỘNG LỰC SINH TỒN] ◄════ (Dòng tiền / Rủi ro) ═════ [CHỦ THỂ C: NẠN NHÂN / THỰC THI]
```

### 2. Ma trận Chủ thể & Động lực Cốt lõi (Actors & Incentives Matrix)
*(Liệt kê tất cả các bên tham gia trên bàn cờ, làm rõ vị thế quyền lực, mục tiêu tối thượng và áp lực sinh tồn)*

| Chủ thể (Actor) | Vị thế & Nguồn lực (Position & Leverage) | Động lực Sinh tồn / Kinh tế (Core Incentive) | Rủi ro Tử huyệt (Vulnerability) |
|---|---|---|---|
| **[Chủ thể 1]** | [Nắm giữ quyền hạn/vốn/công nghệ gì?] | [Được lợi gì từ trạng thái hiện tại?] | [Sợ điều gì nhất? Chi phí gì nuốt chửng?] |
| **[Chủ thể 2]** | [Nắm giữ quyền hạn/vốn/công nghệ gì?] | [Được lợi gì từ trạng thái hiện tại?] | [Sợ điều gì nhất? Chi phí gì nuốt chửng?] |
| **[Chủ thể 3]** | [Nắm giữ quyền hạn/vốn/công nghệ gì?] | [Được lợi gì từ trạng thái hiện tại?] | [Sợ điều gì nhất? Chi phí gì nuốt chửng?] |

---

## TẦNG 3: UNDERLYING MECHANICS & CENTRAL PARADOXES (QUY LUẬT VẬN HÀNH & NGHỊCH LÝ CỐT LÕI)

*(Phần này giải phẫu các quy luật khách quan, cơ chế kinh tế/xã hội/kỹ thuật chi phối toàn bộ sự việc. TUYỆT ĐỐI KHÔNG chia chương ở đây)*

### 1. Chuỗi Mắt Xích Nhân Quả Gốc Rễ (Root Causes & Causal Chains)
- **Mắt xích 1 (Nguyên nhân khởi phát):** [Điều kiện tiền đề / Thể chế / Động lực ban đầu tạo ra trạng thái hiện nay].
- **Mắt xích 2 (Cơ chế dẫn truyền):** [Hệ thống vận hành như thế nào? Dòng tiền và nguồn lực dịch chuyển qua các van điều tiết nào?].
- **Mắt xích 3 (Điểm tích tụ rủi ro):** [Tại sao các rủi ro không tự triệt tiêu mà lại cộng dồn qua thời gian?].

### 2. Nghịch Lý Trung Tâm & Khoảng Cách Bề Mặt vs. Bản Chất (The Central Paradox)
- **Ảo tưởng Bề mặt (The Surface Illusion):** [Những gì truyền thông, dư luận hoặc báo cáo sơ bộ nhìn thấy và lầm tưởng].
- **Hiện thực Nghiệt ngã (The Structural Reality):** [Bản chất cơ học/tài chính/luật pháp thực sự đang diễn ra dưới gầm bàn].
- **Điểm gãy Cấu trúc (Structural Break Point):** [Khoảnh khắc hoặc ngưỡng giới hạn mà tại đó mô hình cũ bắt buộc phải vỡ trận hoặc biến đổi].

### 3. Các Quy Luật Khách Quan Chi Phối (Governing First Principles)
*(Chỉ ra 2-4 quy luật cốt lõi giải thích vì sao các bên hành động như vậy — ví dụ: Quy luật chi phí giao dịch, Nghịch lý kẻ hưởng lợi miễn phí, Bẫy thanh khoản, Bất cân xứng thông tin, Động lực thể chế...)*
- **Quy luật 1:** [Tên quy luật & cách nó bẻ lái hành vi các chủ thể].
- **Quy luật 2:** [Tên quy luật & cách nó bẻ lái hành vi các chủ thể].

---

## TẦNG 4: TARGET GROUND-TRUTH EVIDENCE CHECKLIST & IMMUTABLE DATA VAULT

> ⚠️ **HÓA GIẢI NGHỊCH LÝ CON GÀ & QUẢ TRỨNG (TWO-STAGE LEDGER PROTOCOL):**
> - **Giai đoạn 1 (Tại Pha 1):** Bảng này là **DANH MỤC MỎ NEO DỮ LIỆU CẦN ĐIỀU TRA (Target Evidence Checklist)**: Liệt kê các chỉ tiêu định lượng, báo cáo kiểm toán, văn bản pháp quy cần truy lùng độc lập trong Deep Research. ⛔ TUYỆT ĐỐI CẤM đoán mò hoặc tự bịa số liệu chi tiết.
> - **Giai đoạn 2 (Sau Pha 2 Deep Research):** Cập nhật chính thức thành **SỔ CÁI BẰNG CHỨNG THỰC CHỨNG BẤT BIẾN (`DATA-01` đến `DATA-XX`)** bằng 100% số liệu thật đã kiểm toán từ `research_vault/`.

| Mã Số Liệu | Chỉ Tiêu Đo Đạc / Giá Trị Thực Tế | Ý Nghĩa Thực Chứng / Cơ Chế Khách Quan | Nguồn Chỉ Định / Tên File (`research_vault/`) | Trạng Thái / Ghi Chú Kiểm Chứng |
|---|---|---|---|---|
| `DATA-01` | `[Pha 1: Chỉ tiêu cần đo / Pha 2: Giá trị thật]` | `[Ý nghĩa kinh tế/kỹ thuật/pháp lý]` | `[Nguồn chỉ định / File vault]` | `[Pha 1: PENDING ➔ Pha 2: VERIFIED]` |
| `DATA-02` | `[Pha 1: Chỉ tiêu cần đo / Pha 2: Giá trị thật]` | `[Ý nghĩa kinh tế/kỹ thuật/pháp lý]` | `[Nguồn chỉ định / File vault]` | `[Pha 1: PENDING ➔ Pha 2: VERIFIED]` |
| `DATA-03` | `[Pha 1: Chỉ tiêu cần đo / Pha 2: Giá trị thật]` | `[Ý nghĩa kinh tế/kỹ thuật/pháp lý]` | `[Nguồn chỉ định / File vault]` | `[Pha 1: PENDING ➔ Pha 2: VERIFIED]` |
| `DATA-04` | `[Pha 1: Chỉ tiêu cần đo / Pha 2: Giá trị thật]` | `[Ý nghĩa kinh tế/kỹ thuật/pháp lý]` | `[Nguồn chỉ định / File vault]` | `[Pha 1: PENDING ➔ Pha 2: VERIFIED]` |
| ... | ... | ... | ... | ... |

