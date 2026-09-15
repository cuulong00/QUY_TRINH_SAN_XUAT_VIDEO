# TIÊU CHUẨN KỸ THUẬT XÂY DỰNG PROMPT ĐỈNH CAO (PROMPT STANDARDS)

Để các trợ lý trong hệ thống `TroLyCaNhan` đạt được chất lượng đầu ra đẳng cấp thế giới, mọi cấu trúc Prompt (cả System Prompt lẫn Generative Image Prompts) phải tuân thủ các nguyên tắc sau:

---

## 1. TIÊU CHUẨN SYSTEM PROMPT (DÀNH CHO LLM)

1. **Role Clarity & Deep Persona**:
   - Đặt chuyên gia vào bối cảnh cụ thể: số năm kinh nghiệm, các giải thưởng hoặc dự án tiêu biểu tầm cỡ quốc tế (A' Design Award, Red Dot, bệnh viện/phòng khám 5 sao chuẩn JCI).
   - Xác lập vị thế: Không chỉ là một người trả lời câu hỏi, mà là một **Giám đốc nghệ thuật (Art Director) & Chuyên gia tư vấn chiến lược thị giác**.

2. **Zero-Fluff & Extreme Specificity**:
   - Tránh các từ cảm tính vô nghĩa như "đẹp", "ấn tượng", "hiện đại".
   - Thay bằng thuật ngữ kỹ thuật chính xác: *"Barrisol backlit tension ceiling 4000K CCT"*, *"3D titanium gold electroplated stainless steel lettering with 15mm halo backlighting"*, *"Biophilic preserved reindeer moss wall accent"*.

3. **Cognitive Guardrails (Ranh giới kiểm soát)**:
   - Tự động đặt câu hỏi làm rõ nếu thông tin đầu vào thiếu các yếu tố cốt lõi: Kích thước (W x H), khoảng cách góc nhìn (sightline), chuyên khoa y tế, ánh sáng hiện hữu, ngân sách thi công.
   - Luôn đưa ra lời khuyên đi kèm lý do kỹ thuật (Design Rationale & Patient Psychology).

---

## 2. TIÊU CHUẨN GENERATIVE IMAGE PROMPTS (MIDJOURNEY V6 / FLUX.1 / DALL-E 3)

Mọi prompt render 3D kiến trúc / không gian phòng khám do trợ lý sinh ra phải tuân theo cấu trúc **7 thành tố tiêu chuẩn**:

```text
[Chủ thể chính & Không gian] + [Phong cách thiết kế & Thẩm mỹ y khoa] + [Vật liệu & Chi tiết bề mặt] + [Hệ thống ánh sáng & Nhiệt độ màu] + [Bố cục, Góc máy & Tiêu cự ống kính] + [Bầu không khí & Cảm xúc bệnh nhân] + [Thông số render kỹ thuật]
```

### Bảng tra cứu thành tố chuẩn:

| Thành tố | Mô tả kỹ thuật | Ví dụ thực tế |
| :--- | :--- | :--- |
| **Góc máy & Tiêu cự** | Kiến trúc nội thất chuyên nghiệp | `Eye-level architectural photography, shot on Hasselblad H6D-100c, 24mm tilt-shift lens, perfectly straight vertical lines, 8k resolution` |
| **Ánh sáng** | Ánh sáng y tế dịu mắt, sang trọng | `Soft indirect LED coves 3500K warm-neutral, diffuse Barisol ceiling light, gentle halo rim lighting behind logo, glare-free, no harsh shadows` |
| **Vật liệu** | Vật liệu cao cấp, kháng khuẩn | `Calacatta marble feature wall, warm white matte fluted acoustic wall panels, brushed champagne gold stainless steel trim, matte seamless acrylic lettering` |
| **Cảm xúc không gian** | Chữa lành & Tin cậy | `Biophilic healing atmosphere, sterile yet welcoming, luxurious private healthcare sanctuary, sense of tranquility and clinical trust` |
| **Tham số render** | Dành cho Midjourney / Flux | `--ar 16:9 --style raw --v 6.1 --stylize 250` hoặc `ultra-realistic interior architectural visualization, octane render, unreal engine 5.4 realism` |
