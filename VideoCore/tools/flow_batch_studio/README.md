# 🎬 Google Flow Batch Studio — Production Engine Management

Trung tâm phát triển và quản lý ứng dụng **Google Flow Batch Studio**. Thư mục này lưu trữ, quản lý phiên bản các file Master Prompt, tài liệu kiến trúc, template code và các mẫu prompt đầu vào theo tiêu chuẩn chuyên nghiệp.

---

## 📂 Cấu Trúc Thư Mục

```text
tools/flow_batch_studio/
├── README.md                                 # Bản đồ hướng dẫn & tổng quan dự án
├── prompts/
│   ├── 00_MASTER_BUILDER_PROMPT.md           # Master Prompt (Source of Truth) dùng nạp vào Flow Tool Builder
│   ├── 01_INCREMENTAL_UPDATE_TEMPLATE.md     # Mẫu prompt cập nhật có khóa chống ghi đè (Regression Lock)
│   ├── 02_PROMPT_INPUT_FORMAT_SPEC.md        # Chuẩn định dạng file prompt đầu vào (.txt)
│   └── sample_prompts/
│       └── sample_ch01_daidung.txt           # File prompt mẫu chuẩn hóa từ tập Đại Dũng
├── docs/
│   ├── ARCHITECTURE_AND_BEST_PRACTICES.md    # Phân tích kiến trúc 6 luồng, Circuit Breaker, RAM cleanup
│   └── TROUBLESHOOTING_GUIDE.md              # Hướng dẫn xử lý lỗi 429, treo luồng Veo Lower Priority
└── src_templates/
    ├── config.ts                             # Hằng số bất biến (SYSTEM_CONFIG) dán vào tab "Mã"
    └── types.ts                              # Định nghĩa TypeScript data models cho dự án
```

---

## 🚀 Quy Trình Làm Việc Chuẩn (Standard Workflow)

1. **Khởi tạo Tool mới trên Google Flow:**
   * Mở file `prompts/00_MASTER_BUILDER_PROMPT.md`.
   * Sao chép toàn bộ nội dung và dán vào ô chat Tool Builder của Google Flow.
2. **Nếu cần bổ sung tính năng mới:**
   * Mở file `prompts/01_INCREMENTAL_UPDATE_TEMPLATE.md`.
   * Điền yêu cầu mới vào phần `[NEW FEATURE REQUEST]`.
   * Gửi cho AI để tránh tình trạng bị đổi model hoặc mất tính năng cũ.
3. **Nếu muốn sửa nhanh model/hằng số mà không qua chat:**
   * Vào tab **"Mã" (Code / Monaco Editor)** trên Google Flow.
   * Tham khảo file `src_templates/config.ts` để sửa trực tiếp trong code một cách an toàn 100%.
