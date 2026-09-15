# HỆ THỐNG TRỢ LÝ CÁ NHÂN CHUYÊN NGHIỆP (PERSONAL ASSISTANTS ECOSYSTEM)

Hệ thống được thiết kế để quản trị, chuẩn hóa và vận hành các **Siêu Trợ Lý AI Chuyên Sâu (AI Specialists)** phục vụ công việc thiết kế, sáng tạo, tiếp thị và vận hành dự án. Mỗi trợ lý được đóng gói hoàn chỉnh gồm **DNA (Bản sắc cốt lõi), Bộ Kỹ Năng (Deep Skills), Quy trình thực thi (SOP/Frameworks), Thư viện Mẫu (Templates)** và **Master System Prompt**.

---

## 📁 Kiến Trúc Thư Mục Hệ Thống

```text
TroLyCaNhan/
├── README.md                              # Giới thiệu & Cẩm nang sử dụng hệ sinh thái
├── core/                                  # Khung tiêu chuẩn dùng chung cho mọi trợ lý
│   ├── assistant_template.md              # Khung mẫu (Standard Blueprint) tạo trợ lý mới
│   └── prompt_standards.md                # Tiêu chuẩn kỹ thuật thiết kế Prompt đỉnh cao
└── assistants/                            # Kho lưu trữ các Siêu Trợ Lý chuyên môn
    └── clinic_backdrop_master/            # Siêu Trợ Lý: Chuyên gia Thiết kế Backdrop Phòng Khám
        ├── README.md                      # Hướng dẫn nhanh cho trợ lý Backdrop Phòng Khám
        ├── system_prompt.md               # MASTER PROMPT (Sẵn sàng nạp vào AI: Claude, GPT, Gemini)
        ├── dna.md                         # Bản sắc cốt lõi, triết lý thẩm mỹ & chuẩn mực tư duy
        ├── skills/                        # Các kỹ năng chuyên sâu theo từng module
        │   ├── 01_patient_psychology_color.md  # Tâm lý bệnh nhân & bảng màu trị liệu
        │   ├── 02_spatial_materials_lighting.md # Kỹ thuật vật liệu, kiến trúc & chiếu sáng
        │   ├── 03_event_lobby_photowall.md      # Quy cách backdrop lễ tân, sự kiện & photo wall
        │   ├── 04_medical_compliance_branding.md # Tiêu chuẩn thương hiệu & đạo đức y tế
        │   └── 05_ai_render_prompting.md        # Công thức prompt 3D Photorealistic mockup
        ├── frameworks/                    # Quy trình xử lý công việc từ A - Z
        │   ├── brief_to_production_sop.md # SOP 6 bước từ Brief đến Bản vẽ in ấn & thi công
        │   └── client_intake_form.md      # Bộ câu hỏi khảo sát nhu cầu phòng khám
        └── templates/                     # Thư viện Prompt & mẫu thiết kế thực chiến
            ├── grand_opening_prompts.md   # Mẫu backdrop lễ khai trương / ra mắt
            ├── lobby_reception_prompts.md # Mẫu vách backdrop logo quầy lễ tân chuẩn 5 sao
            └── medical_cme_prompts.md     # Mẫu backdrop hội thảo chuyên đề y khoa (CME/Workshop)
```

---

## 🚀 Cách Thức Sử Dụng

### 1. Kích hoạt một Trợ Lý có sẵn
- Mở thư mục của trợ lý trong `assistants/<assistant_name>/`.
- Mở file `system_prompt.md` và sao chép toàn bộ nội dung.
- Dán vào phần **Custom Instructions / System Prompt / Project Instructions** trên ChatGPT, Claude Projects, Gemini Advanced, hoặc Cursor/Antigravity.
- Bắt đầu giao việc theo quy trình chuẩn đã định nghĩa.

### 2. Tạo một Trợ Lý Mới
1. Sao chép khung mẫu từ `core/assistant_template.md`.
2. Tạo thư mục mới trong `assistants/<ten_tro_ly_moi>/`.
3. Điền đầy đủ: Hồ sơ (Profile), DNA, Skills chuyên môn, Quy trình và Mẫu prompt thực thi.
4. Tham khảo `core/prompt_standards.md` để đảm bảo chất lượng prompt đạt tiêu chuẩn hàng đầu thế giới.

---

## 📋 Danh Mục Trợ Lý Hiện Tại

| Mã Trợ Lý | Tên Định Danh | Lĩnh Vực Chuyên Sâu | Trạng Thái |
| :--- | :--- | :--- | :--- |
| `CLINIC-BKP-01` | **Dr. Visio – Master Clinical Spatial & Backdrop Director** | Thiết kế Backdrop, Vách sảnh Lễ tân, Check-in Wall, Sự kiện phòng khám cao cấp | ✅ Sẵn sàng sử dụng |

---

*Hệ thống được thiết kế theo tiêu chuẩn cấu trúc mô-đun hóa, dễ dàng mở rộng và tương thích với tất cả các dòng mô hình ngôn ngữ lớn (LLM).*
