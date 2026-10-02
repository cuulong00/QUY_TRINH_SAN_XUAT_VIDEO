# Kế hoạch nâng cấp toàn diện quy trình viết kịch bản và kho tri thức (bản Fable, 02/10/2026)

Viết cho: user duyệt; Opus thực thi theo từng phiếu (WO). Fable kiểm từng phiếu trước khi trình user.
Thay thế: `KE_HOACH_NANG_CAP_QUY_TRINH_VIET_20261002.md` (bản Opus). Bản Opus giữ lại làm phụ lục chứng cứ, không dùng để giao việc.
Trạng thái: toàn bộ việc viết tập đang tạm dừng (user chốt 02/10). Agent GSM đã được báo dừng (tin seq 32).

---

## 0. Kết luận kiểm tra bản của Opus

Tôi đối chiếu ba sản phẩm của Opus (kế hoạch, sổ vấn đề V01–V30, chẩn đoán bộ nhớ) với file thật.

### 0.1 Đúng và giữ nguyên
- Tám bản chất R1–R8 có bằng chứng thật. Tôi kiểm lại từng dòng bảng R1: 8/8 cặp mâu thuẫn tồn tại đúng như ghi.
- Sổ vấn đề V01–V30 ghi đúng cách (hiện tượng có file:dòng hoặc step log). Mục V17 (Opus tự nhận kết luận sai trước khi đọc log) là bài học đúng, đã vào memory.
- Chẩn đoán bộ nhớ ba tầng (nạp, công cụ đọc, agent dùng) đúng, và đúng khi nói lỗi cắt đầu ra nằm ở `kbq`, không phải ở mô hình dữ liệu kb_v2. Không cần đập kho lần nữa.
- Nghiên cứu về hook (30 giây đầu, mở-đóng-mở, nối thumbnail) và về cách chuyên gia tư duy (Story-Based Inquiry, ACH của Heuer, Pirolli-Card) đều đúng nguồn và đúng kết luận: không có "trên xuống hay dưới lên", chỉ có vòng lặp giả thuyết và bằng chứng.

### 0.2 Sai hoặc nói quá, cần sửa
| Chỗ | Opus viết | Thực tế | Hệ quả cho kế hoạch |
|---|---|---|---|
| R7, gạch đầu 1 | "Không có chuẩn nối thumbnail với câu đầu" | Đã có: `hook_engine` §3.5 "Khớp lời hứa đóng gói", `hook_lab` kiểm 4, template 01 và 04 có dòng "Lời hứa đóng gói" | Khoảng trống thật là cấu trúc 0–30 giây và khung hình mở đầu (I2V), không phải mắt xích hứa-hẹn |
| R6 | "Claim ledger tới Pha 10 mới có" | `rules/chapter-writing.md` bắt cập nhật `10_compliance_report.md` sau mỗi chương (từ Pha 7) | Vấn đề đúng là không có sổ từ Pha 1, nhưng ghi mốc cho chính xác |
| R2 | "18 file dùng BCTC/điểm hòa vốn làm tiêu chí chấm" | 18 là số file chứa cụm chữ, gồm cả skill KB và persona chuyên môn, không phải 18 tiêu chí chấm | Vẫn là thiên lệch thật, nhưng phạm vi sửa nhỏ hơn: 5 file cổng/rubric |
| Phần 4 | "Tập GSM đi tiếp với DNA hiện tại" | User đã dừng toàn bộ | Bỏ Phần 4; thay bằng kế hoạch chạy lại tập GSM như bài kiểm thử (mục 5) |

### 0.3 Thiếu, phải bổ sung
1. **Kế hoạch Opus không chứa form tư duy chuẩn.** Opus trả lời user đúng trong chat (vòng giả thuyết và bằng chứng, form 7 phần) nhưng không đưa vào kế hoạch. Đây là câu hỏi gốc của user. Tôi kiểm: cả 5 template trong `02_templates/masterpiece_pipeline/` có **0 lần** chữ "giả thuyết". Luật "≥3 giả thuyết cạnh tranh" chỉ tồn tại trong memory của Claude (`thesis-hidden-strategy-not-pnl`), chưa vào DNA. Pha 1 hiện chốt một luận điểm, Pha 2 đi tìm bằng chứng xác nhận: đúng thiên kiến xác nhận mà ACH được sinh ra để chặn.
2. **Không dựa trên đợt rà DNA 29/09** (`01_management/dna_audit_20260929.md`, 82 dòng). Đợt đó đã sửa nhiều mâu thuẫn và ghi rõ hai việc còn mở: luật cấu trúc chép lặp ở nhiều persona; Loại B 1 hay 2 case study. Kế hoạch mới phải nối tiếp đợt đó, không rà lại từ đầu. Bài học lớn hơn: DNA vừa được viết lại 3 ngày trước mà tập GSM vẫn sinh 30 lỗi, nghĩa là **sửa chữ không đủ, phải sửa cơ chế** (công cụ, cổng máy, sổ xuyên tập).
3. **Không có bước nào cho kho và công cụ đọc.** V01–V10, V27, V28, V30 không có phiếu B nào tương ứng. User yêu cầu kế hoạch phủ cả ba khâu: đẩy, tổ chức, sử dụng dữ liệu.
4. **Không có bước cho kỹ năng điều phối** (V17, V18): phiếu giao việc chuẩn, cách chấm, đọc step log, không tin tự báo (V14). Hiện quy tắc điều phối nằm rải ở memory và `kg_research/QUY_TAC_TU_DIEU_PHOI.md` (viết cho luồng KB, không cho luồng viết).
5. **Không có bộ đo và cách kiểm thử.** "Chạy lại trên một tập thật" chưa nói: chạy bằng agent mới (hội thoại mới, không nhiễm ngữ cảnh cũ), đo gì, so với mốc nào.
6. **Không có nhật ký thay đổi DNA.** Ba đợt rà lớn trong 1 tuần (29/09, 02/10 Opus, nay) đều viết tài liệu mới thay vì nối vào một dòng lịch sử. Không có changelog thì lần sau lại rà từ đầu.
7. **Bỏ sót ba mâu thuẫn:**
   - CTA ở chương kết: `longform_blueprint` §3 (dòng 145–150), §10, §13 vẫn bắt "CTA dẫn sang video tiếp theo", trái hằng số `AGENTS.md` mục 4 (đúng 1 CTA, cuối Ch.2). Đợt 29/09 sửa ở `chapter_writer` nhưng sót `longform_blueprint`.
   - Hai workflow cho Pha 1 cùng tồn tại: `init_episode.md` (bảng pha trỏ tới) và `build_global_vision.md` (orchestration-protocol trỏ tới), hard gate đọc hai bộ persona khác nhau.
   - Persona khai báo khác persona được đọc: `hook_lab` hard gate đọc `hook_engine` + `the_macro_strategist`, nhưng pre-flight khai "Viral Alchemist + Critical Auditor"; `build_outline` hard gate đọc `macro_strategist` + `narrative_director` + `script_architect`, pre-flight khai "Editorial Strategist + Dialectic Architect + Critical Auditor". Agent đọc một bộ, tự xưng bộ khác.
8. **Thứ tự bước chưa khớp nguyên tắc của chính Opus** ("thứ gây sai luận điểm làm trước"). B0–B3 là dọn nhà; thứ làm sai luận điểm (form tư duy, sổ dữ kiện, cổng máy) nằm ở B4, B7. Vì user đã dừng viết, không còn áp lực tập đang chạy, nên sắp lại theo giai đoạn (mục 4).

---

## 1. Tiêu chí "quy trình đủ tốt để quay lại viết"
User muốn "quy trình hoàn hảo nhất thì mới dừng". Hoàn hảo không đo được; đặt tiêu chí đo được thay vào:

| # | Tiêu chí | Cách đo |
|---|---|---|
| T1 | Pha 1 ra ≥3 giả thuyết cạnh tranh, mỗi giả thuyết ≥3 dữ kiện có mã OBS từ ≥2 thực thể, có ma trận đỡ/bác | Cổng máy đếm |
| T2 | Kế hoạch nghiên cứu Pha 2 chỉ nhắm bằng chứng phân biệt giả thuyết; không có GAP mà kho đã trả lời được | `kbaudit --check-plan` bản mới |
| T3 | 100% chân đỡ luận điểm ở Pha 1 còn mặt ở Pha 3–4, hoặc có dòng lý do bỏ | Cổng máy so sổ dữ kiện |
| T4 | 0 mã OBS sai hoặc lệch câu; 0 số không nguồn; 0 so sánh nhất không nguồn; 0 nhãn suy luận rơi ở câu tóm | Cổng máy |
| T5 | Mỗi bằng chứng BÁC có dòng "đặt ở chương nào, luận điểm đổi gì" | Cổng máy + Fable |
| T6 | Mỗi pha ≤1 vòng sửa khi chạy lại tập GSM bằng agent mới | Đếm tin mailbox |
| T7 | Agent mới đọc đủ DNA của một pha trong một lượt (không cắt) | Step log: 0 dòng "truncated" khi đọc DNA |
| T8 | Hook tập GSM qua phép thử tắt tiếng và đặt cạnh thumbnail; có cấu trúc 0–30 giây; không mở bằng cảnh AI tĩnh | Fable + user |
| T9 | Chạy trên đề tài thứ hai khác loại (A hoặc C) đạt T1–T7 | Lặp lại |
| T10 | Hồ sơ đề tài có đủ 5 nút N1–N5 kèm tín hiệu đo; các pha sau làm đúng hệ quả của nút (số giả thuyết, độ sâu Pha 2, chế độ kết, lăng kính) | Cổng máy (3.3 mục nút vặn) |

Mốc so sánh: lượt GSM vừa rồi, 30 vấn đề (phụ lục A), 2–3 vòng sửa mỗi pha.

---

## 2. Nguyên tắc sửa (giữ 6 của Opus, thêm 4)
1. Mỗi luật một nơi; file khác chỉ trỏ tới.
2. Gỡ trước, thêm sau.
3. Cổng phải chạy bằng máy hoặc do người khác chấm; không tự chấm, không chấm "trong suy nghĩ".
4. Ví dụ trung tính về đề tài, hoặc có mã nguồn đã kiểm.
5. Mỗi bước được đo trước và sau trên tập thật.
6. Dong_Chay chuyển theo nghĩa.
7. **Nối tiếp `dna_audit_20260929.md`**, không rà lại từ đầu. Mọi sửa đổi ghi vào `.agents/CHANGELOG.md` kèm mã V hoặc R làm lý do.
8. **Cơ chế trước, chữ sau.** Lỗi lặp ở GSM dù DNA vừa viết lại chứng minh thêm luật không chặn được lỗi; chỉ công cụ và cổng máy chặn được.
9. **Người viết không chấm mình.** Agent viết, cổng máy chấm trước, Claude chấm sau, user quyết gate.
10. **Kiểm thử bằng agent mới.** Mọi lần đo đều dùng hội thoại Antigravity mới (theo `KHOI_TAO_AGENT_MOI.md`), không dùng agent đã nhiễm ngữ cảnh.

---

## 3. Trạng thái đích

### 3.1 Form tư duy chuẩn (áp cho mọi đề tài)
| Phần | Nội dung | Chiều | Pha hiện hành |
|---|---|---|---|
| A. Đề bài | Câu hỏi trung tâm, vì sao lúc này, điều user đã loại. Khóa, agent không tự đổi | — | 0 → file hiến chương |
| B. Bản đồ nền | Từ kho: thực thể, quan hệ, dòng chảy, luật chơi. Mỗi ý có mã OBS. Ghi rõ đã biết / chưa biết | Trên xuống | 1, 1b |
| C. Giả thuyết cạnh tranh | ≥3 cách giải thích, gồm cả cách "nhàm" nhất; mỗi cái nêu dữ kiện nào sẽ bác nó | Trên xuống | 1 |
| D. Ma trận bằng chứng | Hàng = bằng chứng, cột = giả thuyết, ô = khớp / ngược / không phân biệt. Nghiên cứu chỉ nhắm ô phân biệt | Dưới lên | 2 |
| E. Cập nhật | Bằng chứng mới thì loại, thu hẹp hoặc đổi giả thuyết; giữ lịch sử | Vòng lặp | 2 → 4 |
| F. Kết luận | Giả thuyết còn đứng (ít bằng chứng ngược nhất), mức chắc chắn, điều kiện sai | — | 3 |
| G. Cách kể | Nghịch lý mở đầu, đáp án lộ dần, cao trào là bằng chứng quyết định. Tách khỏi cách nghĩ | Cấu trúc tò mò | 3–4 |

Chuỗi 16 pha giữ số, đổi ruột Pha 1–4 theo bảng này.

### 3.1b Năm nút vặn: form cố định, độ sâu đổi theo tín hiệu đo được
Bốn phương pháp tham chiếu (Story-Based Inquiry, Minto/McKinsey, ACH, Pirolli-Card) không phải bốn lối đi để chọn một; mỗi cái góp một bộ phận của cùng một vòng lặp. Form 3.1 vì vậy **không đổi theo chủ đề**. Cái đổi là năm nút vặn dưới đây, và nút vặn do **tín hiệu đo được** ở Pha 0–1 quyết định, không do agent tự cảm. Năm nút điền vào mục "Hồ sơ đề tài" của hiến chương (WO-07); form (WO-06) đọc hồ sơ để quyết độ sâu; cổng máy (WO-09) kiểm agent có làm đúng nút đã vặn không.

| Nút | Tín hiệu (nguồn) | Giá trị | Hệ quả bắt buộc |
|---|---|---|---|
| N1. Độ phủ nền | `kbaudit <slug> <mã>`: % thực thể trọng tâm có dữ kiện; số GAP P1 | Cao (≥70% thực thể có dữ kiện, GAP P1 ≤5) / Thấp | Cao: Pha 1 đặt giả thuyết đủ chắc; Pha 2 chỉ nhắm bằng chứng phân biệt, không chạy template khía cạnh. Thấp: Pha 2 thêm vòng "gom nền" trước, rồi mới lập ma trận |
| N2. Số lời giải hợp lý | Sau phần B, đếm cách giải thích đều khớp dữ kiện hiện có | 1 / 2–4 / >4 | 1: bắt buộc ép thêm ≥2 giả thuyết đối lập, kể cả giả thuyết "nhàm" (ví dụ "công ty làm đúng điều họ công bố"). 2–4: lập ma trận thẳng. >4: gom bằng cây câu hỏi MECE trước |
| N3. Loại câu hỏi | Câu hỏi trung tâm thuộc cơ chế kinh tế / công nghiệp, hay thuộc giá trị, chính trị, pháp lý chưa phán quyết, biến số tương lai | Cơ chế / Giá trị-tương lai | Cơ chế: chế độ kết A (`stance_and_judgment` §1). Giá trị-tương lai: chế độ B với đủ 4 phần §1b. Có thể hỗn hợp: chốt câu phụ, mở câu lớn |
| N4. Bằng chứng phân biệt có tồn tại | Với mỗi ô ma trận "chưa phân biệt được": có nguồn công khai lấp được không (hồ sơ pháp lý, báo cáo kiểm toán, dữ liệu đăng ký, quyết định cơ quan quản lý) | Có / Không | Có: kế hoạch nghiên cứu nhắm thẳng nguồn đó. Không: thu hẹp luận điểm về phần phân biệt được; phần còn lại thành điều kiện sai, không thành khẳng định |
| N5. Điểm tựa khán giả | Loại A/B/C theo `content_principles` §2 | A / B / C | Quyết hook, Ch.2, lăng kính Devil's chapter. Lăng kính dòng tiền chỉ bật khi đề tài là doanh nghiệp hoặc thị trường vốn và được ghi vào hiến chương; không bật mặc định |

Ví dụ áp ngược vào GSM: N1 cao, N2 = 1 (agent chỉ có H2), N3 cơ chế, N4 có, N5 = B. Nếu vặn đúng từ đầu: Pha 2 ngắn và nhắm thẳng quyết định cạnh tranh Đan Mạch, 20-F, đăng ký RDW; N2 ép thêm hai giả thuyết đối lập, nên bằng chứng 72,7% xe giao cho khách ngoài lộ ở Pha 1 thay vì Pha 4; N5 tắt lăng kính dòng tiền, chặn "canh bạc đốt tiền" ngay Pha 1. Một đề Loại C (già hóa dân số): N1 thấp hơn, N2 nhiều, N3 giá trị-tương lai → Pha 2 dài, ma trận rộng, chế độ B. Cùng form, khác nút.

### 3.2 Ba sổ xuyên tập (tạo ở Pha 0–1, mọi pha đọc, chỉ thêm không ghi đè)
- `00_hien_chuong.md`: phần A. Cổng chấm đối chiếu từng pha với file này.
- `00_bang_gia_thuyet.md`: phần C, D, E. Mỗi giả thuyết có mã H1…; mỗi ô ma trận trỏ mã dữ kiện.
- `00_so_du_kien.md`: mọi mắt xích dùng trong tập, mỗi dòng: mã mắt xích, câu, nhãn (`verified_data` / `market_analysis` / `opinion_commentary`), mã OBS hoặc nguồn vault, pha đưa vào, trạng thái. Các pha sau **trỏ mã mắt xích**, không chép câu. `10_compliance_report.md` sinh từ sổ này.

### 3.3 Cổng máy `scripts/kiem_pha.py <slug> <pha>`
Chạy trước mọi lần Claude chấm. Mỗi kiểm in ĐẠT/LỖI kèm dòng:
- Mã OBS: tồn tại, `current`, **số và từ khóa trong câu dẫn khớp statement** (V24, V27).
- Số không có mã OBS hoặc nguồn vault (V16, V23); phép tính tự làm không gắn nhãn "tự tính".
- So sánh nhất, địa danh, chi tiết vật thể không nguồn và không nhãn minh họa (V23).
- Nhãn suy luận: câu tóm (Key Insight, Exit, chốt) chứa khẳng định mà mắt xích nguồn mang nhãn suy luận (V12, V22).
- Chân đỡ Pha 1 vắng ở pha sau mà không có dòng lý do (V11).
- Hiến chương: tiêu đề, câu hỏi trung tâm nguyên văn; từ khóa đã loại (ví dụ "điểm hòa vốn", "bảng cân đối") không xuất hiện (V15).
- Nút vặn: số giả thuyết trong `00_bang_gia_thuyet.md` ≥ mức N2 quy định; chế độ kết trong brief khớp N3; lăng kính dòng tiền chỉ xuất hiện khi N5 cho phép; kế hoạch nghiên cứu Pha 2 chỉ chứa câu hỏi trỏ tới ô ma trận "chưa phân biệt" khi N1 cao (3.1b).
- Bằng chứng BÁC trong `01c_evidence_unused` chưa có dòng xử lý (V26).
- Báo cáo sửa của agent: câu cũ grep = 0, câu mới có dòng (V14).
- Đọc đủ file: với file dài, agent phải nộp danh sách đoạn đã mở; cổng so với step log (V07).

### 3.4 Kho và công cụ đọc
- `kbq`: mặc định tóm tắt (số dữ kiện theo nhóm + top-N), tham số `--trang`, `--loc`, `--tu`; in dòng "đã cắt, xem tiếp bằng …" khi vượt ngưỡng; mỗi số in kèm kỳ, phạm vi, đơn vị (V06, V16).
- `kbaudit --check-evidence`: xếp theo mức liên quan với từng giả thuyết H, tách nhóm ĐỠ và BÁC, mặc định top-N (V07, V26). `--check-plan`: mỗi GAP phải kèm câu hỏi cụ thể và câu hỏi đó chưa trả lời được bằng kho (V08). Chạy check-evidence ngay sau Pha 1, không đợi Pha 4 (V25).
- Cổng nạp: ngày quan sát ≤ ngày nguồn, tách kỳ hiệu lực (V01); quote phải chứa số và từ khóa của statement (V30); trường dữ kiện thuần tách trường diễn giải (V03); chặn câu không dấu, lẫn ngôn ngữ (V04).
- Lớp sự kiện: nhiều nguồn cùng sự kiện gom một nút, lệch số sinh cờ mâu thuẫn (V02, V27).
- Đường nạp vault → web_fill qua cùng cổng (V05). Chỉ mục đoạn cho nguồn sơ cấp dài (V28).
- Độ mới: mỗi đầu ra ghi thời điểm tra kho; trước khi nộp chạy lại lấy phần đổi (V10).
- Mặc định `KB_GRAPH=kb_v2` (V21); hook kiểm số cột registry (V20).

### 3.5 Skill điều phối (`.agents/skills/orchestrator/SKILL.md`, dùng cho Claude)
- Phiếu giao chuẩn: kết quả cần đạt, tiêu chí đạt, skill/persona phải đọc, không viết lệnh thay agent (V18).
- Trình tự chấm: cổng máy → đọc step log → tự mở nguồn với mọi câu trích → đối chiếu hiến chương → trình user vài dòng (V14, V17).
- Giới hạn vòng sửa; mẫu phiếu sửa (mục có số, mỗi mục một dòng, kèm bằng chứng).
- Ghi sổ vấn đề ngay khi phát hiện (memory `test-run-issue-log`).

---

## 4. Phiếu công việc (WO) theo giai đoạn

Mỗi phiếu ghi: mục tiêu, file, thao tác, điều kiện đạt (kiểm được), người kiểm, phụ thuộc, mã V/R khắc phục. Opus làm đúng một phiếu rồi dừng; Fable kiểm; user quyết ở 4 gate (mục 6).

### Giai đoạn P0: Quyết định (user)
**WO-00 · Bảng quyết định**
- Mục tiêu: user chốt mọi mâu thuẫn còn mở trước khi sửa chữ.
- Thao tác: lập một bảng, mỗi dòng một mâu thuẫn, hai phương án, đề xuất của Fable, ô user chọn. Nguồn: bảng R1 (8 dòng), mục 0.3.7 (3 dòng), hai việc còn mở của `dna_audit_20260929`, cộng các câu hỏi thiết kế: Devil's chapter có bắt buộc lăng kính dòng tiền không; chương kết đóng loop hay giữ tension; chuẩn dài câu (150 ký tự giữ, bỏ 8–15 từ); gợi hình giữ ở mức nào; hai workflow Pha 1 giữ cái nào.
- Điều kiện đạt: mọi dòng có lựa chọn của user.
- Kiểm: user. Phụ thuộc: không. Khắc phục: R1.

### Giai đoạn P1: Dọn nền (gỡ, không thêm)
**WO-01 · Gom luật về một nơi**
- File: `AGENTS.md` (hằng số), `content_principles.md` (luật theo loại A/B/C), `longform_blueprint.md`, `rules/chapter-writing.md`, `chapter_writer/SKILL.md`, `build_outline.md`, `retention_gate_checklist.md`, `golden_samples/golden_hook.md`.
- Thao tác: theo kết quả WO-00, giữ một bản, các chỗ còn lại thay bằng một dòng trỏ. Sửa riêng: CTA chương kết trong `longform_blueprint` §3/§10/§13 → trỏ `AGENTS.md` mục 4. Theo lựa chọn của user: **Q6 = B (cấm tả cảnh)** → gỡ tiêu chí "gợi hình điện ảnh, ngôn từ có màu sắc, ánh sáng, chất liệu" ở `masterpiece` 5.1 và `chapter_quality` 2.3 (cùng phần "Chiaroscuro" trong lời văn), giữ luật cấm của `chapter_writer` mục 7 làm bản duy nhất; **Q7 = A (đọc toàn bộ chương trước)** → giữ luật ở `AGENTS.md` Pha 7 và `chapter_writer`, sửa `rules/chapter-writing.md` cho khớp (bỏ câu "không mặc định đọc lại nếu NST đã đủ"), và bỏ lý do gắn model ("Gemini 3.8 Flash, 1 triệu token") thay bằng lý do thật: kịch bản chỉ vài nghìn từ.
- Điều kiện đạt: script `scripts/kiem_dna.py --mau-thuan` (viết trong WO-05) ra 0 cặp lệch cho các hằng số và luật đã chốt.
- Kiểm: Fable chạy script + đọc diff. Khắc phục: R1, 0.3.7.

**WO-02 · Gỡ thiên lệch Loại A và khung tài chính**
- File: `golden_hook.md` (#5), `longform_blueprint` §2 và §15, Hội đồng phản biện trong `AGENTS.md` và `content-os-pipeline.md`, `hook_engine` (biến thể 2), `retention_gate_checklist` Gate 2 Loại B, `masterpiece` 2.1, `chapter_quality` 2.2.
- Thao tác: Personal-First chỉ áp Loại A; lăng kính dòng tiền là một trong các lăng kính tùy đề, do Pha 1 chọn và ghi vào hiến chương; thay "điểm hòa vốn / BCTC" trong tiêu chí chấm chung bằng "cơ chế và đánh đổi"; biến thể hook 2 đổi thành "va chạm giữa hai mô hình" không gắn tài chính.
- Điều kiện đạt: grep các cụm "túi tiền", "điểm hòa vốn", "bảng cân đối", "FCF" trong tiêu chí chấm chung = 0 (chỉ còn trong persona chuyên môn và luật riêng Loại A).
- Kiểm: Fable. Khắc phục: R2, V15.

**WO-03 · Làm sạch ví dụ**
- File: `stance_and_judgment.md` §1b, §3, §5, mục ví dụ cuối; `hook_engine/examples/golden_hook.md`; `chapter_writer/examples/golden_chapter.md`; `.agents/examples/*`.
- Thao tác (user chốt Q12 = A: **giữ ví dụ GSM**, sửa cho đúng kho): mọi số và mọi câu gán cho nguồn trong ví dụ phải khớp một mã OBS hiện hành, ghi mã ngay cạnh. Cụ thể: "lãi vay tập đoàn 113 tỷ/ngày" không có trong kho → thay bằng số có OBS hoặc bỏ, và không đặt lãi vay toàn tập đoàn cạnh doanh thu một mảng (lệch phạm vi, V16); "VinFast xác nhận với SEC rằng đội taxi là phòng lái thử di động" → viết đúng phạm vi câu SEC (424B3/F-1: hợp tác với GSM cho khách quốc tế cơ hội lái thử và trải nghiệm xe); "~1.500 chiếc... gần như không chiếc nào đến tay người mua cá nhân" → ghi rõ hai nguồn lệch số 1.300/1.500 và kỳ của số bán lẻ. Ví dụ kết bài bỏ khung "bảng cân đối" (Q10, WO-02). Xóa hoặc điền file placeholder; ghi ở đầu mỗi file ví dụ: "ví dụ minh họa cấu trúc; số liệu có mã OBS".
- Điều kiện đạt: 0 số liệu hoặc câu gán nguồn nào trong file ví dụ thiếu mã OBS hiện hành; cổng máy (WO-09) chạy được trên file ví dụ.
- Kiểm: Fable. Khắc phục: R3, V29.

**WO-04 · Khớp persona và workflow**
- File: `hook_lab.md`, `build_outline.md`, `init_episode.md`, `build_global_vision.md`, `content-os-pipeline.md` bảng pha, `orchestration-protocol.md`, `specialist_map.md`.
- Thao tác: theo WO-00 chọn một workflow Pha 1, workflow kia thành tệp trỏ; danh sách file hard gate = danh sách persona khai báo trong pre-flight; bỏ chữ "dùng tool `view_file`" (gắn với một IDE) thay bằng "đọc".
- Điều kiện đạt: script kiểm: với mỗi workflow, tập persona trong hard gate == tập persona trong pre-flight == dòng tương ứng trong bảng pha.
- Kiểm: Fable. Khắc phục: 0.3.7.

**WO-05 · Rút gọn, changelog, script kiểm DNA**
- File: toàn `.agents/` (ngoài tools) và `00_core/`; tạo `.agents/CHANGELOG.md`; tạo `scripts/kiem_dna.py`.
- Thao tác: bỏ mệnh lệnh lặp ("BẮT BUỘC/TUYỆT ĐỐI" chỉ giữ ở cổng hard-fail); bỏ các chỗ còn gắn model sau WO-01 (`AGENTS.md:256`, `chapter_writer` dòng 79 và 187, `content-os-pipeline.md:117`: "Gemini 3.8 Flash có xu hướng…"); **Q13:** luật cấu trúc (Therefore/But, búp bê Nga, steelman, đối xứng 1-1) giữ một bản ở `script_architect/SKILL.md`, các persona `the_dialectic_architect`, `the_editorial_strategist`, `the_narrative_director`, `the_critical_auditor` chỉ trỏ; tách mỗi skill thành phần "nguyên tắc" (ngắn, đọc mọi lần) và "thủ tục" (đọc khi làm); `CHANGELOG.md` đã tạo ở WO-01, WO-05 bổ sung mục ghi lùi nếu thiếu. `kiem_dna.py`: đếm cặp lệch hằng số, persona lệch, tham chiếu file không tồn tại, cụm bị cấm theo WO-02.
- Điều kiện đạt: tổng dòng giảm ≥30%; `kiem_dna.py` ra 0 lỗi; mỗi file skill đọc hết trong một lượt của agent mới (thử trên 1 agent, step log không có "truncated" khi đọc DNA).
- Kiểm: Fable. Khắc phục: R8.

### Giai đoạn P2: Cơ chế đúng (thêm)
**WO-06 · Form tư duy vào Pha 1–3**
- File: `02_templates/masterpiece_pipeline/01_global_vision_synthesis_template.md`, `03_brief_template.md`, `build_global_vision.md` (hoặc `init_episode.md` theo WO-04), `deep_research.md`, `deep_researcher/SKILL.md`, `strategy_council/SKILL.md`, `the_macro_strategist.md`.
- Thao tác: thêm phần B (bản đồ nền từ kho, mọi ý có OBS), C (≥3 giả thuyết, mỗi cái ghi "dữ kiện nào sẽ bác tôi"), D (ma trận bằng chứng); Pha 2 kế hoạch nghiên cứu đi từ ô "chưa phân biệt được" của ma trận, không từ template 5 khía cạnh; Pha 3 phần F chọn giả thuyết còn đứng theo nguyên tắc "ít bằng chứng ngược nhất", ghi mức chắc chắn và điều kiện sai; tách phần G (cách kể) khỏi phần F. Chuyển luật "≥3 giả thuyết" từ memory vào DNA. **Form đọc "Hồ sơ đề tài" (năm nút N1–N5, mục 3.1b) từ hiến chương để quyết:** số giả thuyết tối thiểu (N2), có vòng gom nền hay không (N1), chế độ kết (N3), phạm vi luận điểm được khẳng định (N4), lăng kính phản biện và điểm tựa (N5). Mỗi hệ quả trong bảng 3.1b phải có một dòng tương ứng trong template, không để agent tự diễn giải.
- Điều kiện đạt: T1, T2 kiểm được bằng cổng máy trên một tập thử; template có đủ 5 nhánh rẽ theo N1–N5.
- Kiểm: Fable. Khắc phục: 0.3.1, V26.

**WO-07 · Hiến chương tập**
- File: template mới `00_hien_chuong_template.md`; `init_episode`/`build_global_vision`; mọi workflow Pha 2–11 thêm dòng "đọc hiến chương trước".
- Thao tác: trường: tiêu đề chính/phụ (khóa), câu hỏi trung tâm nguyên văn, loại đề tài, chỉ đạo user (nguyên văn, có ngày), điều đã loại (từ khóa cấm), lăng kính chọn, chế độ kết dự kiến. **Thêm mục "Hồ sơ đề tài" gồm năm nút N1–N5 (mục 3.1b): mỗi nút ghi giá trị, tín hiệu đã đo (số liệu `kbaudit`, số giả thuyết đếm được, loại câu hỏi), và hệ quả bắt buộc.** N1, N2, N4 được điền lại sau Pha 1 và Pha 2 khi tín hiệu đổi, có ghi ngày; N3, N5 do Claude và user chốt ở Pha 0. Chỉ user hoặc Claude sửa.
- Điều kiện đạt: cổng máy đối chiếu được (3.3 mục hiến chương); hồ sơ đề tài không có nút nào để trống hoặc thiếu tín hiệu.
- Kiểm: Fable. Khắc phục: R6, V15.

**WO-08 · Sổ dữ kiện xuyên tập**
- File: template `00_so_du_kien_template.md` (dạng bảng hoặc jsonl); `chapter-writing.md`, `claim-ledger.md`, `chapter_writer`, `compliance_council`, `final-merge.md`.
- Thao tác: như 3.2; Pha 1 tạo, mỗi pha thêm dòng; các câu tóm trong outline/brief trỏ mã mắt xích; `10_compliance_report.md` sinh từ sổ (script); `chapter_writer` đọc sổ + tra kho (`kbq`) chứ không chỉ vault.
- Điều kiện đạt: T3, T4 kiểm bằng cổng máy.
- Kiểm: Fable. Khắc phục: R6, V11, V12, V22.

**WO-09 · Cổng máy `kiem_pha.py`**
- File: `scripts/kiem_pha.py` mới; mô tả trong `orchestration-protocol.md`.
- Thao tác: toàn bộ danh mục 3.3. Đầu ra ngắn, mỗi lỗi một dòng có file:dòng. Có `--pha 1|1b|2|3|4|7|8`.
- Điều kiện đạt: chạy trên `episodes/gsm-chau-au` bản hiện có phải bắt lại được ít nhất các lỗi V12, V22, V23, V24, V26, V27 mà Fable/Opus đã bắt tay.
- Kiểm: Fable so với sổ vấn đề. Khắc phục: R4.

**WO-10 · Cổng chấm người: tách vai, bỏ tự chấm**
- File: `masterpiece_quality_standard.md`, `chapter_quality_standard.md` (§6 thiếu Gate 0), `compliance_council/SKILL.md`, `chapter_writer` bước 3 (14 tiêu chí ngầm), `retention_gate_checklist.md`.
- Thao tác: rubric rút còn các tiêu chí không máy kiểm được (lập trường, cách đọc riêng, giọng); người chấm là Claude hoặc agent khác agent viết; bỏ "tự chấm trong khối thinking"; thêm hard-fail "bịa chi tiết" và "suy luận viết như dữ kiện"; sửa mẫu báo cáo thiếu Gate 0; mọi cổng máy chạy trước cổng người.
- Điều kiện đạt: không còn chỗ nào bảo agent viết tự cho điểm mình; mẫu báo cáo đủ 6 gate.
- Kiểm: Fable. Khắc phục: R4, V14.

**WO-11 · Skill điều phối + phiếu giao chuẩn**
- File: `.agents/skills/orchestrator/SKILL.md` mới; `orchestration-protocol.md` trỏ tới; gộp nội dung còn đúng của `kg_research/QUY_TAC_TU_DIEU_PHOI.md` và các memory `delegate-outcomes-not-commands`, `return-fixes-keep-agents-busy`, `test-run-issue-log`.
- Thao tác: như 3.5. Kèm mẫu phiếu giao, mẫu phiếu sửa, mẫu tin báo của agent (phải có bằng chứng máy kiểm được).
- Điều kiện đạt: Fable đọc thử phiếu giao Pha 1 tập thử: không có lệnh viết sẵn, có tiêu chí đạt, có đường tới skill.
- Kiểm: Fable. Khắc phục: V14, V17, V18.

### Giai đoạn P3: Tay nghề
**WO-12 · Hook và Ch.1: chuẩn 30 giây đầu**
- File: `hook_engine/SKILL.md`, `hook_lab.md`, `golden_samples/golden_hook.md`, `04_hook_pack_template.md`, `longform_blueprint` §3 Ch.1.
- Thao tác: thống nhất số lượng (3 biến thể, bỏ "7 góc/10 câu"); cấu trúc 0–30 giây (xác nhận cú bấm trong 3 giây; đối nghịch; điều được mất; câu hỏi trung tâm + lộ trình ngắn); quy tắc mở-đóng-mở cho 30 giây đến 3:30 (đóng vòng nhỏ, giữ câu lớn); re-hook 3:30; cấm mở bằng niên biểu; phép thử tắt tiếng và đặt cạnh thumbnail; hook không kết luận (#3 `golden_hook` đã sửa ở WO-01; WO-12 sửa tiếp #2 "nhận định chuyên gia có lập trường trong 15 giây đầu" thành "câu diễn giải cho thấy cách đọc riêng, chưa kết luận", và #5 "gắn túi tiền" theo loại đề tài nếu WO-02 chưa làm).
- Điều kiện đạt: T8 trên tập thử.
- Kiểm: Fable + user. Khắc phục: R7.

**WO-13 · Giao thức khung mở đầu cho I2V và I2V+**
- File: `visual_prompter/SKILL.md`, `visual_prompter_plus/SKILL.md` (sửa dòng 173), `generate_visual_prompts*.md`, `thumbnail_prompter/SKILL.md`.
- Thao tác: 7 điểm Opus đã nêu (nối thumbnail 0–3 giây; cụ thể, có thật; đối nghịch nhìn thấy được; ưu tiên tư liệu thật cho cụm hook; chuyển động từ giây đầu, cảnh 3–5 giây; không vẽ điều KHÔNG RÕ; 3 phương án, chọn bằng hai phép thử). Thumbnail brief (Pha 6c) chuyển lên trước hoặc song song Pha 5 để hook có thứ để nối (Q14). **Mâu thuẫn hình ảnh phát hiện ở WO-01:** `AGENTS.md:363` dạy "chiaroscuro lighting, deep noir shadows" và `thumbnail_style_guide.md:28` dùng "chiaroscuro", trong khi `visual_style_guide.md:58`, `visual_prompter` dòng 33 và 116, `the_visual_storyteller.md:45` cấm đúng các từ đó → thống nhất theo Canonical Visual DNA (`AGENTS.md` mục "Sang trọng – Trầm – Ấm", cấm u ám), sửa hai chỗ dạy ngược.
- Điều kiện đạt: Fable đọc skill: không còn câu "hook ưu tiên VEO_AI lắng đọng"; có giao thức khung mở đầu dùng chung.
- Kiểm: Fable. Khắc phục: R7.

**WO-14 · Template outline và brief**
- File: `07_outline_template.md`, `08_chapter_briefs_template.md`, `script_architect/SKILL.md`.
- Thao tác: bỏ ô "Key Insight" và "Causal Exit" dạng câu tự do, thay bằng "mã mắt xích + một dòng"; "Mỏ neo vật lý" phải ghi nguồn hoặc nhãn minh họa; thêm ô "bằng chứng BÁC và luận điểm đổi gì"; gỡ ô trùng với sổ dữ kiện.
- Điều kiện đạt: outline tập thử: 0 nhãn rơi, 0 chi tiết bịa (cổng máy).
- Kiểm: Fable. Khắc phục: R5, V22, V23, V26.

### Giai đoạn P4: Kho và công cụ đọc (song song P1–P3, do Opus hoặc agent KB)
**WO-15 · `kbq` hợp đồng đầu ra** — `scripts/kg_registry/kb_query.py`: tóm tắt mặc định, phân trang, lọc, báo cắt, in kỳ/phạm vi/đơn vị cạnh số. Đạt: `kbq facts vinfast` mặc định < 150 dòng và có dòng "xem tiếp". (V06, V16)
**WO-16 · `kbaudit` xếp hạng và check-plan nội dung** — `kb_audit.py`: check-evidence tách ĐỠ/BÁC theo giả thuyết H, top-N; check-plan đòi câu hỏi cụ thể và thử trả lời bằng kho trước. Đạt: chạy trên gsm-chau-au, OBS-109e4291 nằm top nhóm BÁC. (V07, V08, V25, V26)
**WO-17 · Cổng nạp** — `load_core.py` và cổng web_fill: ngày quan sát ≤ ngày nguồn; quote chứa số/từ khóa của statement; chặn câu không dấu; cờ "suy luận" nếu có từ suy diễn; quét lại toàn kho (31 OBS ngày tương lai, 208 câu suy diễn, V30). Đạt: báo cáo quét, số lỗi còn lại = 0 hoặc có phiếu sửa. (V01, V03, V04, V30)
**WO-18 · Lớp sự kiện và cờ mâu thuẫn** — thiết kế theo chuẩn (Wikidata qualifier + nhiều reference, event-centric); thử trên 3 sự kiện: Sea Patris, Viggo, Dantaxi. Đạt: `kbq` hiện một sự kiện với các số lệch và nguồn tương ứng. (V02, V27)
**WO-19 · Đường nạp vault → web_fill, chỉ mục nguồn sơ cấp** — script chuyển R0X_*.md thành form web_fill (URL, ngày, nguyên văn), qua cùng cổng; đánh chỉ mục đoạn cho PDF/20-F đã tải. Đạt: vault GSM nạp được vào kb_v2 với 0 lỗi cổng. (V05, V28)
**WO-20 · Mặc định `KB_GRAPH=kb_v2`, hook registry, độ mới** — `kb_write.py:18`; cập nhật rule/skill còn ghi kb_main; hook kiểm số cột CSV; `kbq` in dấu thời gian kho. (V10, V20, V21). Cổng 🔒: cần user duyệt đổi mặc định.

### Giai đoạn P5: Kiểm thử và lan tỏa
**WO-21 · Chạy lại tập GSM bằng agent mới** — hội thoại Antigravity mới, phòng mới; đi Pha 0 → 4 với DNA đã sửa; Fable chấm bằng cổng máy; đo T1–T8; so với phụ lục A. Đạt: T1–T7.
**WO-22 · Đề tài thứ hai khác loại** — chọn từ `topic_backlog.md` một đề Loại A hoặc C; cùng cách đo. Đạt: T9.
**WO-23 · Dong_Chay** — chuyển theo nghĩa các WO đã đạt; giữ luật riêng kênh; chạy `kiem_dna.py` bên Dong_Chay.

---

## 5. Đo lường và cách kiểm thử
- **Mốc:** 30 vấn đề V01–V30 của lượt GSM, phân theo tầng: NẠP 6, TỔ CHỨC/CÔNG CỤ 5, AGENT DÙNG 12, ĐIỀU PHỐI 3, HẠ TẦNG 3 (một số mục thuộc hai tầng). Vòng sửa: Pha 2 = 2, Pha 3 = 1, Pha 4 = 2.
- **Cách chạy lại:** agent mới (không tái dùng hội thoại cũ), phòng `_agent_chat/` mới, thư mục tập mới, cùng đề bài GSM. Claude điều phối theo skill WO-11. Mọi lỗi mới ghi tiếp vào sổ vấn đề với mã V31+.
- **Chỉ số:** số lỗi theo tầng lọt qua cổng máy; số vòng sửa mỗi pha; số dòng "truncated" khi đọc DNA; số chân đỡ Pha 1 còn ở Pha 4; số giả thuyết và số ô ma trận được phân biệt sau Pha 2.
- **Đạt:** mục 1 (T1–T9). Không đạt thì quay lại WO tương ứng, không thêm luật mới.

---

## 6. Lịch gate với user (4 gate thay cho 10)
| Gate | Sau WO | User quyết gì |
|---|---|---|
| G1 | WO-00 | Chốt bảng quyết định |
| G2 | WO-05 | Duyệt nền đã dọn (đọc CHANGELOG + kết quả `kiem_dna.py`) |
| G3 | WO-14 | Duyệt cơ chế mới và tay nghề (xem tập thử nội bộ nhỏ của Fable trên Pha 1 bằng form mới) |
| G4 | WO-22 | Xem số đo trước/sau; quyết quay lại viết thật |
Các WO kho (P4) báo kết quả ở G2–G4, riêng WO-20 cần duyệt 🔒.

---

## 7. Cách giao cho Opus
- Một phiếu một lượt. Tin giao gồm: mã WO, mục tiêu, file, thao tác, điều kiện đạt, nhắc đọc `CHANGELOG.md` và `dna_audit_20260929.md` trước.
- **Opus không sửa trực tiếp file DNA (user chốt Q17 = B, 02/10).** Opus làm trên bản nháp (thư mục scratch hoặc nhánh git riêng), rồi trả: patch dạng trước/sau cho từng chỗ (unified diff), đầu ra nguyên văn của lệnh kiểm chạy trên bản nháp, và dòng CHANGELOG đề xuất. Không nhận báo "đã xong" không có patch và đầu ra lệnh.
- Fable đọc patch, áp vào file thật, chạy lại lệnh kiểm, ghi CHANGELOG, commit một WO một commit. Patch sai thì trả Opus kèm dòng lỗi, không tự vá thay.
- Script mới (`kiem_pha.py`, `kiem_dna.py`) Opus được viết thẳng vào `scripts/` vì không phải DNA, nhưng vẫn kèm đầu ra chạy thử.
- Thứ tự bắt buộc: WO-00 → WO-01…05 → WO-06…11 → WO-12…14 → WO-21…23. P4 chạy song song từ sau G1.

---

## Phụ lục A. Ánh xạ sổ vấn đề → phiếu
| V | WO | V | WO | V | WO |
|---|---|---|---|---|---|
| V01 | 17 | V11 | 08 | V21 | 20 |
| V02 | 18 | V12 | 08, 14 | V22 | 09, 14 |
| V03 | 17 | V13 | 09, 19 | V23 | 09, 14 |
| V04 | 17 | V14 | 09, 10, 11 | V24 | 09 |
| V05 | 19 | V15 | 02, 07 | V25 | 16 |
| V06 | 15 | V16 | 09, 15 | V26 | 06, 14, 16 |
| V07 | 09, 16 | V17 | 11 | V27 | 09, 18 |
| V08 | 16 | V18 | 11 | V28 | 19 |
| V09 | 16, 18 | V19 | 11 | V29 | 03, 08 |
| V10 | 20 | V20 | 20 | V30 | 17 |

## Phụ lục B. Ánh xạ bản chất Opus → phiếu
R1 → WO-00, 01, 04 · R2 → WO-02 · R3 → WO-03 · R4 → WO-09, 10 · R5 → WO-14 · R6 → WO-07, 08 · R7 → WO-12, 13 · R8 → WO-05. Bổ sung của Fable: form tư duy → WO-06; điều phối → WO-11; kho → WO-15…20; đo và kiểm thử → WO-21, 22; changelog → WO-05.

## Phụ lục C. File chạm tới (để Opus ước lượng)
`.agents/AGENTS.md`, `.agents/rules/{content-os-pipeline,orchestration-protocol,chapter-writing,claim-ledger,final-merge,editorial-quality}.md`, `.agents/workflows/{init_episode,build_global_vision,deep_research,build_brief,build_outline,hook_lab,write_chapter,generate_visual_prompts,generate_visual_prompts_plus}.md`, `.agents/skills/{strategy_council,deep_researcher,script_architect,hook_engine,chapter_writer,compliance_council,visual_prompter,visual_prompter_plus,thumbnail_prompter}/`, `.agents/skills/orchestrator/` (mới), `.agents/personas/{the_macro_strategist,the_critical_auditor,the_dialectic_architect}.md`, `.agents/CHANGELOG.md` (mới), `00_core/{content_principles,longform_blueprint,stance_and_judgment,masterpiece_quality_standard,chapter_quality_standard,retention_gate_checklist,golden_samples/golden_hook}.md`, `02_templates/masterpiece_pipeline/*` (+2 template mới), `scripts/{kiem_pha.py,kiem_dna.py}` (mới), `scripts/kg_registry/{kb_query,kb_audit,load_core}.py`, `scripts/kg_common/kb_write.py`, `scripts/claude_hooks/post_write_validate.js`.
