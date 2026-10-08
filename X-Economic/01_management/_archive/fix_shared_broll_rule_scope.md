# BÁO CÁO KHẮC PHỤC PHẠM VI QUY CHUẨN THỊ GIÁC B-ROLL (FIX SHARED B-ROLL RULE SCOPE)

> **Mã công việc:** `FIX-SHARED-BROLL-RULE-SCOPE`  
> **Ngữ cảnh:** `x-economy-master` (Dự án `X-Economic`)  
> **Đơn vị thực thi:** Antigravity (Heavy Technical Executor)  
> **Đơn vị điều phối:** Claude Code  
> **Ngày thực hiện:** 28/09/2026  

---

## 📌 1. NGUYÊN NHÂN SỰ CỐ & HÀNH ĐỘNG KHẮC PHỤC TỔNG THỂ

Trong task `VISUAL-PIPELINE-REDESIGN-V1` trước đó, Antigravity đã ghi đè trực tiếp các sửa đổi đặc thù của kênh X-Economy (3 trụ cột, bỏ Video AI Veo, thêm Contact Sheet Gate, thêm phản-ví dụ audit) vào tệp dùng chung toàn hệ sinh thái:
`file:///Users/pro16/Documents/VideoProject/.agents/rules/broll-production-standard.md`.

Ngay sau khi nhận chỉ đạo khẩn từ Claude Code và Người dùng (*"cho antigravity sửa, nhưng lưu ý đây chỉ là quy trình của x-economy, không phải của gocnhinpodcast nhé"*), Antigravity đã:
1. **Khôi phục 100% nguyên văn bản gốc của tệp dùng chung** [`/Users/pro16/Documents/VideoProject/.agents/rules/broll-production-standard.md`](file:///Users/pro16/Documents/VideoProject/.agents/rules/broll-production-standard.md) từ bản ghi lịch sử `transcript_full.jsonl` tại Bước 390 (lần đọc file toàn văn trước khi xảy ra bất kỳ thao tác chỉnh sửa nào).
2. **Tách riêng bản chuẩn hóa cục bộ** cho kênh X-Economy tại [`X-Economic/.agents/rules/broll-production-standard.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/.agents/rules/broll-production-standard.md).
3. **Cập nhật lại các liên kết tham chiếu** trong dự án X-Economic (như [`00_core/footage_hunting_standard.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/00_core/footage_hunting_standard.md)).
4. **Kiểm toán đối chiếu grep** để làm rõ sự thật về các khối luật an toàn AI.

---

## 🔍 2. BẰNG CHỨNG XÁC MINH NGUỒN GỐC KHÔI PHỤC (100% CHÍNH XÁC)

Antigravity **KHÔNG phải tái dựng từ trí nhớ ước lượng**, mà đã trích xuất lại **chính xác 100% từng dòng, từng ký tự, từng công thức toán học** từ nhật ký hệ thống:
- **Tệp nguồn phục hồi:** `/Users/pro16/.gemini/antigravity-ide/brain/ead42b0d-1b45-4f31-bf36-7f175416ffb5/.system_generated/logs/transcript_full.jsonl`
- **Bước thực thi (Step Index):** `Step 390` (thực hiện lúc `2026-09-28T13:29:27+07:00`).
- **Quy mô tệp khôi phục:** Đúng `112 dòng`, `13.816 bytes` nguyên vẹn của **VPOS Standard V7.0**.

### Toàn văn các tiêu đề mục được khôi phục nguyên trạng:
```markdown
# QUY CHUẨN ĐẠO DIỄN THỊ GIÁC & KỸ THUẬT SẢN XUẤT B-ROLL THỰC CHỨNG
## Master Directives for Real-world B-Roll Production (VPOS Standard V7.0)

> **Tài liệu chuẩn hóa chính thức của Hệ sinh thái VPOS (Video Production Operating System).**  
> Áp dụng bắt buộc cho toàn bộ các kênh và dự án: Dòng Chảy, Góc Nhìn Podcast, X-Economics, công cụ FootageHunter và mọi Agent tham gia sản xuất.

## 🏛️ I. NGUYÊN LÝ CỐT LÕI: TƯ DUY ĐIỆN ẢNH VÀ NGỮ CẢNH THỊ GIÁC
### 1. Phá Vỡ "Bẫy Dịch Thô Kịch Bản" (The Literal Translation Trap)
## 🎨 II. MA TRẬN 5 CỤM BỐI CẢNH ĐIỆN ẢNH THỰC TẾ (THE 5 REAL-WORLD CONTEXT ARCHETYPES)
## 🔍 III. NGUYÊN TẮC HÌNH THÀNH TRUY VẤN YOUTUBE (QUERY SYNTHESIS ENGINE)
## 💎 IV. KHÓA ĐỘ PHÂN GIẢI THÉP & CHẤT LƯỢNG RENDER (RESOLUTION AXIOMS)
## 🎬 V. QUY TRÌNH BÓC TÁCH FOOTAGE HIỆN TRƯỜNG & LOẠI BỎ MC PHÒNG THU
## 🛡️ VI. BỘ LỌC KIỂM TOÁN TRỰC QUAN & CƠ CHẾ CIRCUIT BREAKER (VISUAL AUDIT GATE)
```

---

## ⚖️ 3. LÀM RÕ VỀ CÁC KHỐI LUẬT `VEO_AI`, `CELEBRITY`, `ANTHROPOLOGICAL`, `ACTION BLACKLIST`

Claude Code đặt câu hỏi về việc grep các từ khóa `VEO_AI`, `Celebrity`, `Anthropological`, `Action Blacklist` trong file dùng chung. Antigravity đã rà soát toàn bộ lịch sử tệp gốc và làm rõ chân tướng khách quan như sau:

1. **Bản chất của tệp `broll-production-standard.md` dùng chung:**
   - Đây là quy chuẩn **săn B-roll thực tế ngoài đời** bằng công cụ `FootageHunter` tải video phóng sự thật từ YouTube (VTV, VNEWS, báo chí chính thống).
   - Vì là quy chuẩn tư liệu người thật/việc thật ngoài đời, tệp gốc này **CHƯA TỪNG chứa** các khối luật an toàn dành cho video AI tạo hình như `Celebrity Filter Defense` (né filter tên lãnh đạo của AI), `Anthropological Fidelity Gate` (chống vẽ người Tây cho prompt AI) hay `Action Blacklist Veo` (danh sách cấm ngón tay cử động/xe drift của Veo).
2. **Vị trí gốc thực sự của các khối luật AI đó trong hệ sinh thái:**
   - Các khối luật an toàn AI trên nằm tại:
     * [`.agents/AGENTS.md`](file:///Users/pro16/Documents/VideoProject/.agents/AGENTS.md) (Mục 2: *Kiểm toán và Bảo vệ Tài nguyên: Khóa Nhân chủng học thép, Google Vids Omni Video Engine, ComfyUI MiniMax H3 token neo `<Picture 1>`...*).
     * [`X-Economic/.agents/skills/visual_prompter_plus/SKILL.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/.agents/skills/visual_prompter_plus/SKILL.md) và [`01_management/i2v_pipeline_audit.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/01_management/i2v_pipeline_audit.md) (Mục 5: *Các quy tắc ràng buộc & rào cản bảo vệ pháp lý/nghệ thuật hiện hành*).
3. **Phần liên quan đến Video AI DUY NHẤT trong `broll-production-standard.md` bản gốc:**
   - Nằm tại **Mục VI.2 và VI.3**, và **ĐÃ ĐƯỢC PHỤC HỒI 100% NGUYÊN VẸN**:
     ```markdown
     2. Kỷ Luật Tách Biệt Kho Lưu Trữ VPOS:
        - Video AI (Google Vids 720p / ComfyUI MiniMax H3): Lưu trữ độc quyền tại thư mục videos/ai_videos/.
        - Footage B-roll thực tế (1080p Full HD): Lưu trữ tại videos/ và footages/.
        - Tuyệt đối không để xảy ra tình trạng copy đè video AI 720p lên video B-roll 1080p.
     3. Kích Hoạt Circuit Breaker:
        - Nếu tìm kiếm 4 ứng viên uy tín đều không đạt bối cảnh mong muốn: Chuyển sang The Forensic Callout (chụp bài báo có thật trên báo điện tử uy tín) hoặc chuyển giao sang VideoCore để tạo video AI điện ảnh. TUYỆT ĐỐI KHÔNG CHẤP NHẬN TƯ LIỆU RÁC HOẶC SAI LỆCH NGỮ CẢNH.
     ```

---

## 📊 4. KẾT QUẢ GREP XÁC MINH TRỰC TIẾP

### A. Kiểm toán Tệp Dùng Chung ([`.agents/rules/broll-production-standard.md`](file:///Users/pro16/Documents/VideoProject/.agents/rules/broll-production-standard.md))
Chạy script kiểm tra trực tiếp nội dung vừa khôi phục:
```
- VideoCore:            TRUE (Khôi phục circuit breaker sang VideoCore AI)
- Circuit Breaker:      TRUE (Nguyên bản)
- Google Vids:          TRUE (Nguyên bản kho lưu trữ videos/ai_videos/)
- MiniMax H3:           TRUE (Nguyên bản kho lưu trữ)
- videos/ai_videos:     TRUE (Kỷ luật VPOS)
- Dòng Chảy, Góc Nhìn: TRUE (Dòng 5: Áp dụng cho Dòng Chảy, Góc Nhìn Podcast, X-Economics...)
- Contact Sheet Gate:   FALSE (Đã gỡ bỏ khỏi file dùng chung, trả về bản gốc)
- Phản-ví dụ SCADA:     FALSE (Đã gỡ bỏ khỏi file dùng chung, trả về bản gốc)
```

### B. Kiểm toán Tệp Cục Bộ Mới ([`X-Economic/.agents/rules/broll-production-standard.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/.agents/rules/broll-production-standard.md))
Chạy script kiểm tra nội dung bản cục bộ kênh X-Economy:
```
- BẢN CỤC BỘ KÊNH X-ECONOMY: TRUE (Tuyên bố phạm vi chỉ cho X-Economy)
- 3-Pillar Multimodal:         TRUE (B-Roll + Forensic + Infographic ảnh tĩnh)
- visual_intent vs query:      TRUE (Tách bạch triệt để)
- Phản-ví dụ SCADA, đóng bó:   TRUE (Cảnh báo lỗi audit cụ thể)
- Contact Sheet Audit Gate:    TRUE (Cổng chặn cứng bắt buộc)
- VEO_AI ĐÃ BỊ LOẠI BỎ:        TRUE (Không fallback sang VideoCore/Veo)
```

---

## 🔗 5. DANH MỤC THAM CHIẾU ĐÃ CẬP NHẬT TRONG X-ECONOMIC

1. [`X-Economic/00_core/footage_hunting_standard.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/00_core/footage_hunting_standard.md):
   - Đổi dòng định danh kênh từ Góc Nhìn Podcast sang: `X-Economy (https://www.youtube.com/@X-Economy)`.
   - Cập nhật liên kết quy chuẩn sang: `[broll-production-standard.md](file:///Users/pro16/Documents/VideoProject/X-Economic/.agents/rules/broll-production-standard.md)` (Bản cục bộ X-Economy).
2. Các tệp khác của X-Economic (`visual_prompter_plus/SKILL.md`, `content-os-pipeline.md`, `CLAUDE.md`, `episode_workflow.md`): Không chứa đường dẫn cứng tuyệt đối tới file dùng chung gốc, tự động kế thừa theo scope thư mục `.agents/rules/` của dự án.
3. Tuyệt đối không can thiệp hay sửa đổi bất kỳ tệp tin nào thuộc dự án `Dong_Chay` và `GocNhinPodcast`.

---
*Báo cáo được hoàn thành và lưu trữ tại `01_management/fix_shared_broll_rule_scope.md`.*
