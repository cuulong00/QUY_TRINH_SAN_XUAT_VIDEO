# BÁO CÁO ĐIỀU TRA CHUYÊN SÂU: CƠ CHẾ SĂN TƯ LIỆU B-ROLL & KIỂM ĐỊNH THỊ GIÁC (FOOTAGE HUNTER DEEPDIVE)

**Dự án:** X-Economic (Kênh: X-Economy)  
**Tác nhân thực hiện:** Antigravity (Heavy Technical Executor)  
**Mục đích:** Bóc tách trung thực 100% hiện trạng cơ chế sinh Search Query, script thực thi tìm kiếm, và quy trình audit/verify footage B-roll trước khi dựng video. Phục vụ Claude Code phân tích điểm nghẽn và tái thiết kế.

---

## 1. PHẦN MỀM / PROMPT / QUY CHUẨN SINH CÂU TÌM KIẾM (SEARCH QUERY) CHO B-ROLL

Trong hệ thống VPOS hiện tại, quy chuẩn hướng dẫn sinh câu tìm kiếm cho B-roll nằm tại 3 văn bản chính:
1. `00_core/footage_hunting_standard.md` (Quy chuẩn chung săn tư liệu điều tra).
2. `.agents/rules/broll-production-standard.md` (Quy chuẩn đạo diễn thị giác & B-roll thực chứng V7.0).
3. `.agents/skills/footage-hunter/SKILL.md` (Cẩm nang tư duy đạo diễn hình ảnh).

### A. Công thức tạo Search Query trong `00_core/footage_hunting_standard.md` (Dòng 72–88)
Văn bản này định nghĩa công thức tạo từ khóa tìm kiếm:
```text
[Tên Thực Thể / Nhân Vật] + [Sự Kiện / Hành Động Cụ Thể] + [Địa Danh] + [Năm / Tháng] + [Hãng Thông Tấn / Nguồn]
```
Nguyên văn các ví dụ được đưa ra:
* *Đúng chuẩn:* `"Sam Altman Senate hearing AI regulation opening statement May 2023 C-SPAN"`
* *Đúng chuẩn:* `"Jensen Huang holding Blackwell B200 GPU chip Computex Taipei June 2024 CNBC"`
* *Đúng chuẩn:* `"Thủ tướng Phạm Minh Chính phát biểu chiến lược bán dẫn NIC Hòa Lạc tháng 10 2024 VTV"`
* ❌ *Cấm:* `"Sam Altman"`, `"AI video"`, `"Nvidia chip"`, `"Thủ tướng Việt Nam"`.

### B. Cảnh báo "Bẫy dịch thô kịch bản" trong `.agents/rules/broll-production-standard.md` (Dòng 12–18)
Tài liệu quy định cảnh báo việc dịch chữ thô thiển nhưng thực tế quy tắc này đang bị vi phạm trong các manifest:
> *"Sai lầm nghiêm trọng nhất trong sản xuất tư liệu tự động là cố gắng **dịch sát nghĩa từng từ của kịch bản/prompt AI thành từ khóa tìm kiếm trên YouTube**:"*
> *- **Thực tế sai lầm:** Kịch bản viết 'Kỹ sư trưởng khảo sát địa hình hầm và cầu cạn' $\rightarrow$ Agent đi tìm: `'kỹ sư đội mũ bảo hộ chỉ tay hướng tuyến'`. Kịch bản viết 'Chuyên viên đối soát hồ sơ dự toán' $\rightarrow$ Agent đi tìm: `'cán bộ ghi chép số liệu dự toán'`.*
> *- **Hậu quả:** Không một cơ quan báo chí hay đài truyền hình nào đặt tiêu đề video như vậy. Thuật toán tìm kiếm trả về các video rác, tiểu phẩm hài, vlog học sinh, hoặc không tìm ra gì cả.*
> *- **Nguyên lý điện ảnh tài liệu:** **HÌNH VÀ TIẾNG KHÔNG BAO GIỜ PHẢI BẰNG NHAU CHẰN CHẶN TỪNG TỪ**."*

Tại Dòng 37–39 của cùng tệp tin, công thức được rút gọn thành:
$$\text{Query} = \text{[Chủ thể Vĩ mô / Tên Dự án Trọng điểm]} + \text{[Kênh Truyền hình Cấp phép (Tier 1)]} + \text{"-shorts -tiktok"}$$
*Ví dụ:* `"cao tốc bắc nam VTV -shorts -tiktok"`, `"kho bạc nhà nước VNEWS -shorts -tiktok"`.

### C. Cơ chế sinh Manifest trong Pha 12+C (`.agents/skills/visual_prompter_plus/SKILL.md` dòng 183)
Trong quy trình làm việc của LLM (Pha 12+B và 12+C):
* LLM (`the_scene_architect` phối hợp với `the_footage_hunter`) đọc câu thoại $\le 26$ từ từ kịch bản phân cảnh `chapter_XX_visual_plus.md`.
* LLM tự động suy luận và ghi ra tệp `broll_manifest_chapter_XX.json` với cấu trúc:
  ```json
  {
    "id": "CHXX_SCYYY",
    "text": "Câu thoại gốc...",
    "duration": "4.0s",
    "core_visual_intent": "Ý đồ thị giác...",
    "flexible_search_terms": ["từ khóa 1", "từ khóa 2..."],
    "visual_alternatives": ["phương án góc quay 1...", "phương án 2..."],
    "fair_use_transforms": "..."
  }
  ```
Như vậy: **CÂU TÌM KIẾM BAN ĐẦU ĐƯỢC SINH HOÀN TOÀN BỞI LLM KHI SOẠN THẢO MANIFEST**, dựa trên câu thoại của từng phân cảnh.

---

## 2. CƠ CHẾ VÀ SCRIPT THỰC THI TÌM KIẾM THỰC TẾ

Hiện tại có sự phân tách giữa script tại repo `X-Economic` và cỗ máy chuyên dụng `FootageHunter`:

### A. Script cục bộ tại `X-Economic/tools/footage_processor/process_broll.py`
* **Bản chất:** Script này **HOÀN TOÀN KHÔNG CÓ TÍNH NĂNG TÌM KIẾM HOẶC GỌI YT-DLP**.
* **Nguyên lý hoạt động (Dòng 31–73):**
  Nó chỉ nhận đầu vào là `broll_manifest_chapter_XX.json` đã có sẵn trường `"url"`, sau đó chạy thẳng lệnh FFmpeg:
  ```bash
  ffmpeg -y -ss {start} -to {end} -i {url} -an -vf "scale=1.04*iw:-1,crop=1920:1080" -c:v libx264 -preset fast -crf 20 {out_file}
  ```
  Nếu tệp manifest chưa có sẵn URL video thực tế, script sẽ in ra: `⚠️ [BỎ QUA] Phân cảnh {scene_id} chưa có URL video thực tế.` (Dòng 51).

### B. Cỗ máy săn tư liệu thực tế tại `/Users/pro16/Documents/VideoProject/FootageHunter/`
Đây là engine thực sự tìm kiếm và tải clip. Có hai kịch bản chạy chính:

#### 1. Engine đa tầng: `universal_hunter.py` kết hợp `core/visual_query_planner.py`
* **Input Search Query:** Đọc trực tiếp từ `broll_manifest_chapter_XX.json`:
  ```python
  # universal_hunter.py, Dòng 849-855:
  queries = s.get("multi_queries") or s.get("flexible_search_terms") or []
  if not queries and s.get("query"):
      queries = [s.get("query")]
  ```
* **Bổ sung và ghi đè bằng `VisualQueryPlanner` (`core/visual_query_planner.py`):**
  Nếu không có query trong manifest hoặc khi xử lý domain, `VisualQueryPlanner` sử dụng hệ thống Regex ranh giới từ tiếng Việt `has_vn_word()` chia thành 9 Domain tĩnh:
  - Domain 0: Lấy query gốc từ manifest, cắt bớt từ thừa (`CAMERA_FLUFF` như *"cú máy flycam"*, *"khung cảnh"*, *"đại cảnh"*...), ghép tên đài truyền hình (VTV, VNEWS, TTXVN).
  - Domain 1–9: **Hardcode theo các đề tài cụ thể** (Ví dụ dòng 215–285: Trần Đình Long, Trần Bá Dương, Chuối Thagrico, Heo Hòa Phát, Lò cao Dung Quất, Cảng Chu Lai...).
* **Cách gọi `yt-dlp` tìm kiếm (`universal_hunter.py` dòng 235–255):**
  ```python
  cmd = [
      YT_DLP_BIN,
      f"ytsearch{limit}:{query}",
      "--flat-playlist",
      "--no-warnings",
      "--print", "%(id)s\t%(title)s\t%(channel)s\t%(duration)s"
  ]
  ```

#### 2. Engine nhắm bắn trực tiếp: `hunt_direct.py`
* **Nguyên lý (Dòng 488–496):**
  1. Đọc `search_queries` từ manifest của scene, loại bỏ các chữ `broll, 4k, flycam...`, ghép thêm hậu tố `VTV -shorts -tiktok` hoặc `VNEWS -shorts -tiktok` (Dòng 184–185).
  2. Bổ sung các query tĩnh theo 5 Cụm Bối cảnh (Archetype):
     - `CONG_NGHIEP_NANG`: `"thép hòa phát dung quất vtv"`, `"nhà máy vinfast hải phòng vtv"`...
     - `DAI_CONG_TRUONG_HA_TANG`: `"họp tiến độ cao tốc bắc nam vtv"`, `"đại công trường cao tốc bắc nam vtv"`...
     - `TAI_CHINH_CONG_QUYEN`: `"kỳ họp quốc hội vtv1"`, `"kho bạc nhà nước vtv"`...
  3. Gọi `yt-dlp` lấy danh sách 4–5 kết quả:
     ```python
     # hunt_direct.py, Dòng 241-248:
     cmd = [
         YT_DLP, "--flat-playlist", f"ytsearch{limit}:{query}",
         "--no-cookies", "--print", "%(id)s|||%(channel)s|||%(title)s|||%(duration)s"
     ]
     ```
  4. Lọc tiêu đề: So khớp kênh trong `TRUSTED_CHANNELS`, loại bỏ kênh trong `BLACKLIST_CHANNELS` và từ cấm trong `BLACKLIST_TITLE_WORDS` (tai nạn, giang hồ, hài, án mạng...).

---

## 3. CÓ HAY KHÔNG BƯỚC AUDIT/VERIFY CLIP TRƯỚC KHI ĐƯA VÀO VIDEO?

### Kết luận kiểm toán:
* **CÓ** các bước kiểm tra tự động bằng thuật toán heuristic và Computer Vision truyền thống.
* **KHÔNG CÓ** bước nào sử dụng mô hình trí tuệ nhân tạo thị giác (LLM Multimodal / Vision AI như Gemini Vision hay GPT-4V) để hiểu nội dung thực tế của video hoặc đối chiếu ngữ cảnh video với câu thoại.

### Chi tiết các bước verify hiện có trong mã nguồn:

#### Bước 1: Bộ lọc siêu dữ liệu (Metadata Filtering)
* Script kiểm tra tên kênh có thuộc danh sách báo chí cấp phép (VTV, VNEWS, Bloomberg...).
* Script quét tiêu đề video loại bỏ từ khóa giật gân, tai nạn, giang hồ.

#### Bước 2: Nhận diện khuôn mặt tránh MC phòng thu (`core/visual_gatekeeper.py` dòng 69–100)
* Dùng mô hình ONCV YuNet (`face_detection_yunet.onnx`).
* Trích xuất 2 frame mẫu tại giây $1.0s$ và $2.5s$.
* Nếu tỷ lệ diện tích khuôn mặt trên khung hình $> 1.5\%$ (`max_face_area_ratio = 0.015`) $\rightarrow$ Đánh dấu là Talking Head (MC ngồi đọc tin trường quay) và loại bỏ hoặc dịch mốc thời gian $+4.5s$.

#### Bước 3: Đo chuyển động tránh ảnh tĩnh (`core/visual_gatekeeper.py` dòng 102–135)
* Lấy frame ở $15\%, 50\%, 85\%$ thời lượng video, tính sai phân khung hình để loại bỏ ảnh podcast tĩnh hoặc slideshow đứng hình.

#### Bước 4: Kiểm tra độ lệch chuẩn màu sắc (`hunt_direct.py` dòng 395–435)
* Trích xuất frame giữa clip, chuyển sang ảnh xám (`L`), tính `std_val = float(np.std(np.array(im)))`.
* Nếu `std_val < 18.0`: Kết luận là khung hình hỏng, màn hình màu đơn sắc (vàng trơn, cam trơn, đen trơn) $\rightarrow$ Loại bỏ.
* Kiểm tra dung lượng file: Bắt buộc $> 1.2\text{ MB}$ (để đảm bảo không bị lấy nhầm luồng 360p).

#### Bước 5: Ghép Contact Sheet để Người/Agent hậu kiểm thủ công (`core/audit_matrix.py`)
* Ghép 1 frame đại diện tại giây $1.5s$ của toàn bộ các cảnh trong chương thành 1 file ảnh lưới duy nhất (`contact_sheet.png`).
* Trên văn bản quy chuẩn (`broll-production-standard.md` Mục VI.1), Agent được yêu cầu dùng công cụ `view_file` để xem tấm ảnh này trước khi ráp timeline. Tuy nhiên, bước này hoàn toàn mang tính thủ công, không có cơ chế tự động chặn (blocking hook) nếu Agent bỏ qua.

---

## 4. CÁC VÍ DỤ SEARCH QUERY THỰC TẾ TRONG CÁC EPISODE ĐÃ CHẠY

Dưới đây là các trích dẫn nguyên văn từ các file manifest thực tế trong hệ thống, minh chứng cho sự mâu thuẫn giữa việc "dịch sát chữ kịch bản" và "tìm kiếm ngữ cảnh thực tế":

### Ví dụ 1: Máy móc hóa từng chữ trong câu thoại tiếng Anh
* **Nguồn:** `GocNhinPodcast/episodes/cuoc-chien-phan-cuc-ai-i2vplus/broll_manifest_chapter_01.json`
* **Phân cảnh `CH01_SC002`:**
  - *Câu thoại:* "Geoffrey Hinton, người được ví như cha đẻ của A I hiện đại,"
  - *Hunting Query:* `"Geoffrey Hinton 60 Minutes interview AI godfather CBS News October 2023"`
  - *Đánh giá:* Query rất chi tiết và trúng đích do chỉ định rõ phỏng vấn 60 Minutes.
* **Phân cảnh `CH01_SC003` (Bị dính bẫy dịch chữ):**
  - *Câu thoại:* "từng cảnh báo nguy cơ cỗ máy này xóa sổ loài người lên tới 50%."
  - *Hunting Query:* `"Geoffrey Hinton 60 Minutes close up AI existential risk 50 percent CBS News"`
  - *Thực tế:* Bê nguyên cả cụm `"50 percent"` và `"close up"` vào truy vấn YouTube của CBS News $\rightarrow$ Thuật toán YouTube khó tìm thấy tiêu đề nào chứa trọn vẹn cụm từ dài và chi tiết như vậy.

### Ví dụ 2: Dịch tả thực hành động thay vì bối cảnh
* **Nguồn:** `Dong_Chay/episodes/ra-soat-von-duong-sat-cao-toc/broll_manifest_chapter_01.json`
* **Phân cảnh `CH01_SC004`:**
  - *Ý đồ cảnh:* Công nhân và máy móc thi công nền đường cao tốc.
  - *Search Queries:*
    1. `"công nhân thi công cao tốc xe lu máy ủi san gạt đất"`
    2. `"hiện trường thi công hạ tầng giao thông khẩn trương"`
  - *Thực tế:* Không có bản tin VTV/TTXVN nào đặt tiêu đề chứa đủ cụm *"xe lu máy ủi san gạt đất"* hay *"thi công hạ tầng giao thông khẩn trương"*. Tiêu đề thực tế của đài truyền hình chỉ là *"Tiến độ cao tốc Bắc Nam"* hoặc *"Thi công gói thầu số..."*.
* **Phân cảnh `CH01_SC008`:**
  - *Ý đồ cảnh:* Hoạt động kho quỹ kiểm đếm tiền mặt ngân hàng.
  - *Search Queries:*
    1. `"kho quỹ ngân hàng kiểm đếm tiền mặt đóng bó thanh khoản"`
    2. `"giao dịch kho quỹ ngân hàng thương mại nhà nước"`
  - *Thực tế:* Từ khóa *"đóng bó thanh khoản"* là thuật ngữ tài chính chuyên sâu được LLM ghép vào, khiến `ytsearch` bị bóp nghẹt kết quả.

### Ví dụ 3: Ghép thuật ngữ kỹ thuật kén video
* **Nguồn:** `GocNhinPodcast/episodes/hoa-phat-thaco-nghich-ly-cong-nong/broll_manifest_chapter_01.json`
* **Phân cảnh `CH01_SC003`:**
  - *Câu thoại:* "Ở thế giới cơ khí, họ từng nắm thế chủ động điều tiết nhịp độ thị trường."
  - *Flexible Search Terms:*
    1. `"phòng điều hành SCADA nhà máy thép Dung Quất"`
    2. `"trung tâm điều khiển sản xuất tự động Thaco"`
    3. `"kỹ sư vận hành hệ thống điều khiển công nghiệp màn hình lớn"`
    4. `"industrial automation control room Vietnam"`
  - *Thực tế:* Từ khóa `"SCADA"` hoặc `"màn hình lớn"` rất hiếm khi nằm trong tiêu đề video truyền hình chính thống, dẫn đến việc không tìm được video nào khớp, buộc hệ thống phải rơi vào cơ chế `forensic_fallback` hoặc dùng query tĩnh.

---

## 5. TỔNG KẾT ĐẶC TÍNH HỆ THỐNG HIỆN TẠI

1. **Khâu sinh Query:** Do LLM sinh ra ở Pha 12+C dựa vào câu thoại và mô tả của `the_scene_architect`. LLM có xu hướng đưa quá nhiều chi tiết mô tả thị giác (hành động nhân vật, thuật ngữ kỹ thuật, tính từ cảm xúc) vào từ khóa tìm kiếm.
2. **Khâu tiền xử lý Query của Script:** `FootageHunter` nhận thấy điểm yếu này nên đã cố gắng "chữa cháy" bằng code: gọt bớt từ đệm camera (`CAMERA_FLUFF`), hardcode các query mẫu theo từng tập (`visual_query_planner.py`), hoặc bổ sung query tĩnh theo 5 cụm bối cảnh (`hunt_direct.py`).
3. **Khâu thực thi tải & cắt:** Sử dụng `yt-dlp` tìm kiếm `ytsearch{limit}:{query}`, sau đó lọc theo whitelist kênh và blacklist tiêu đề. Tải video và cắt bằng FFmpeg.
4. **Khâu kiểm duyệt:** Hoàn toàn dựa vào các chỉ số kỹ thuật thô (kích thước file, nhận diện mặt bằng YuNet, đo độ biến thiên màu sắc qua PIL, đo đứng hình qua FFmpeg). Hoàn toàn chưa có cơ chế AI xem và hiểu nội dung ngữ cảnh video trước khi đưa vào thư mục `videos/` và `footages/`.
