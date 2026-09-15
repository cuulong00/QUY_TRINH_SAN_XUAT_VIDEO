# BẢNG TIÊU CHÍ TỰ KIỂM DUYỆT PROMPT (PRE-HANDOFF PROMPT AUDIT CHECKLIST)
> **Dự án:** GocNhinPodcast — Đảo Ngọc Phú Quốc Vươn Mình Thành "Singapore Thứ Hai"
> **Áp dụng cho:** Tất cả các tệp `chapter_XX_visual.md` và `prompts_chapter_XX.txt` trước khi báo cáo User.
> **Quy tắc cốt lõi:** 100% Prompt phải do chính LLM của IDE tự tay phân tích ngữ cảnh và biên soạn trực tiếp, tuyệt đối không dùng code Python loop hay API bên ngoài để sinh prompt tự động.

---

## 📋 10 CỔNG KIỂM DUYỆT BẮT BUỘC (MANDATORY AUDIT GATES)

Trước khi gửi bất kỳ tệp prompt nào cho User, Agent bắt buộc phải tự rà soát từng phân cảnh qua 10 tiêu chí dưới đây:

### 0. 🎨 Cổng 0: Bắt Buộc Front-Load Tranh Vẽ 2D Báo Chí Tươi Sáng & Nét Mềm Mịn (Luminous Refined Editorial Gate - TỐI THƯỢNG)
- [ ] **Mở đầu bắt buộc:** 100% prompt `[IMAGE]` **BẮT BUỘC BẮT ĐẦU BẰNG**: `A 2D modern cinematic editorial illustration of [Subject], vibrant high-end graphic novel aesthetic, delicate ultra-fine ink outlines, smooth elegant linework, soft clean matte vector textures, crisp luminous natural daylight, vibrant tropical atmospheric depth...`.
- [ ] **CẤM TỪ NOIR & BÓNG TỐI U ÁM (Strictly No Noir / No Gloomy Shadows):** Tuyệt đối CẤM dùng các từ `noir`, `deep noir shadows`, `dark charcoal`, `gloomy`, `heavy black shadows` (khiến hình ảnh bị xám xịt, tối tăm, mất hết sức sống đảo ngọc).
- [ ] **CẤM NÉT VẼ DÀY CỘP (No Bold/Heavy Lines):** Tuyệt đối CẤM dùng từ `bold ink outlines` hay `heavy outlines`. Bắt buộc dùng `delicate ultra-fine ink outlines` và `smooth elegant linework` để nét vẽ thanh mảnh, mềm mịn, chuẩn tạp chí báo chí quốc tế cao cấp.
- [ ] **ÁNH SÁNG & SỨC SỐNG TƯƠI MÁT:** Hình ảnh phải ngập tràn ánh sáng tự nhiên trong trẻo (`crisp natural daylight`, `sunlit clarity`), biển xanh ngọc bích trong vắt (`vibrant turquoise ocean`), rừng nguyên sinh xanh mướt mát (`lush vibrant emerald greenery`), và kiến trúc hiện đại phản chiếu nắng vàng (`sunlit glass and warm timber reflections`).
- [ ] **CHUẨN HÓA NHÂN CHỦNG HỌC & ĐỊA LÝ:** 
  * Bối cảnh Việt Nam: Bắt buộc ghi rõ `Vietnamese male [chief engineer / structural steel workers / civil engineers / senior policy advisors]`.
  * Bối cảnh quốc tế: Bắt buộc ghi rõ đúng chủng tộc bản địa (`Southeast Asian and Chinese dockworkers in Singapore`, `international arbitrators with East Asian features`).

### 1. 🚫 Cổng 1: Kiểm Tra Chủ Nghĩa Hiện Thực Vật Lý 100% (Anti-Abstract & Physical Realism Gate)
- [ ] **KHÔNG CÓ Hologram viễn tưởng:** Không có sa bàn số phát sáng lơ lửng, tia laser ma trận, dòng hạt dữ liệu bay trên trời.
- [ ] **KHÔNG CÓ Biểu tượng trừu tượng:** Không có cái cân công lý, chìa khóa vàng, bánh răng khổng lồ trên mây, bàn tay vô hình.
- [ ] **KHÔNG CÓ Không gian hư vô (Void Space):** Không có nhân vật hay vật thể đứng giữa khoảng không đen tuyền trừu tượng.
- [ ] **BỐI CẢNH ĐỜI THỰC:** 100% phân cảnh diễn ra tại các địa điểm vật lý có thật ngoài đời trong ánh sáng tự nhiên trong lành.

### 2. 👥 Cổng 2: Kiểm Tra Chuẩn Hóa Nhân Vật (Cast Sheet Consistency Gate)
- [ ] Nhân vật trong bối cảnh Việt Nam **bắt buộc là người Việt Nam** và tuân thủ mô tả cố định trong Cast Sheet.
- [ ] Kỹ sư trưởng mặc áo phản quang cam-navy + mũ cứng trắng; Cố vấn thể chế mặc vest than chì thanh lịch + kính gọng tối; Sĩ quan hải quân mặc quân phục hải quân chỉnh tề.
- [ ] Dòng `[VIDEO]` **tuyệt đối không dùng tên riêng người thật**, chỉ dùng danh từ chung (`the chief engineer`, `the policy advisor`, `the man`).

### 3. 🏷️ Cổng 3: Kiểm Tra Tôn Trọng Thương Hiệu & Địa Danh Thực (Brand Integrity Gate)
- [ ] Giữ nguyên 100% tên thương hiệu và địa danh có thật trong kịch bản: `Phu Quoc`, `Singapore`, `APEC 2027`, `Corona Casino`, `IPPG Factory Outlet`, `Bai Vong`, `An Thoi Port`, `Kien Binh`, `Tho Chu Island`, `Boeing 787`, `Airbus A350`.
- [ ] Tuyệt đối không tự ý đổi tên thành các thương hiệu giả định.

### 4. 🔤 Cổng 4: Kiểm Tra Tỷ Lệ & Định Dạng Text Overlay (Selective Typography Gate)
- [ ] **Tỷ lệ chọn lọc:** Chỉ có **20% - 25%** phân cảnh quan trọng nhất có chữ overlay tiếng Việt có dấu. **75% - 80%** phân cảnh còn lại ghi `[TEXT OVERLAY]: Không` (không mô tả text trong prompt).
- [ ] **Định dạng chữ:** Chữ overlay luôn nhìn trực diện song song ống kính (`facing the camera directly, perfectly horizontal and straight 3D text overlay`), có bóng đổ nhẹ nhàng, sắc nét (`clean subtle drop shadow`).
- [ ] **Khóa tĩnh chữ ở Video Prompt:** 100% phân cảnh có chữ ở ảnh gốc thì dòng `[VIDEO]` phải có câu lệnh: `preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations`.

### 5. ⏱️ Cổng 5: Kiểm Tra Phân Cảnh Thoại & Thời Lượng 8 Giây (Scene Timing & Math Sync Gate)
- [ ] Mỗi phân cảnh đơn hoặc cảnh phụ (`a`, `b`) trong `chapter_XX_visual.md` **chứa tối đa 26 từ thoại**.
- [ ] Không có câu thoại nào bị cắt cụt vô nghĩa; không có phân cảnh phụ bị bỏ trống thoại `[]` khi cảnh trước quá tải từ.

### 6. 🔄 Cổng 6: Đồng Bộ Tuyệt Đối 1-1 Giữa Visual Script & Prompts (Strict 1-to-1 Mapping Gate)
- [ ] Số lượng và mã Scene ID (`CHXX_SCYYY`) trong `chapter_XX_visual.md` khớp chính xác 100% với các cặp prompt `[IMAGE]` / `[VIDEO]` trong `prompts_chapter_XX.txt`.
- [ ] Không có Scene ID ma, không nhảy cóc chỉ số, không thiếu cảnh nào.

### 7. 🎨 Cổng 7: Tuân Thủ Phối Màu 60-30-10 Tươi Sáng Theo Từng Chương (Luminous Color Palette Gate)
- [ ] Prompt ảnh phản ánh đúng bảng màu tươi sáng, giàu sức sống và sang trọng:
  * CH01: Sunlit oceanic turquoise & clear sky (60%) + Crisp concrete & architectural white (30%) + Glowing sunlit amber (#FFB300) (10%).
  * CH02: Vibrant azure bay waters (60%) + Sunlit modern glass & warm timber (30%) + Radiant golden sunlight (#FFC107) (10%).
  * CH03: Airy sunlit boardroom & warm oak (60%) + Crisp white dossiers & executive navy (30%) + Fresh vibrant teal (#00897B) (10%).
  * CH04: Radiant sunlit sky & coastal blue (60%) + Modern engineering steel & clean concrete (30%) + Vivid safety orange (#FF7043) (10%).
  * CH05: Luminous champagne ivory & sunlit atrium (60%) + Polished warm teak & glass (30%) + Vivid emerald green & warm gold (#FFB300) (10%).
  * CH06: Lush vibrant emerald rainforest & crystal turquoise coral sea (60%) + Sunlit limestone rock (30%) + Vivid coral red warning accents (10%).
  * CH07: Brilliant deep maritime blue & sunlit sky (60%) + Runway tarmac & naval vessel grey (30%) + Radiant strategic cyan highlights (10%).

### 8. 🎥 Cổng 8: Khung Prompt 3 Lớp & Style Suffix Tươi Sáng (Luminous Style Suffix Gate)
- [ ] Dòng `[IMAGE]` gồm đủ 3 lớp ngăn cách bằng dấu phẩy: `[Subject & Physical Action]` + `[Environment & Crisp Natural Daylight]` + `[Camera & Mandatory Luminous Style Suffix]`.
- [ ] Style suffix chuẩn tươi sáng: `modern cinematic editorial illustration, vibrant graphic novel aesthetic, delicate ultra-fine ink outlines, smooth elegant linework, soft clean matte vector textures, crisp natural daylight, luminous atmospheric clarity, 16:9`.
- [ ] Dòng `[VIDEO]` theo chuẩn cú pháp: `@CHXX_SCYYY.png -> [Camera Movement & Subject Motion], preserving the details of the reference image, 8-second continuous documentary video --ar 16:9`.

### 9. 🧹 Cổng 9: Khử Sạch Rác Ngữ Cảnh & Ký Tự Lỗi (Anti-Boilerplate & Cleanliness Gate)
- [ ] Tuyệt đối KHÔNG có cụm từ sáo rỗng: *"representing the shadow system"*, *"in a dark space representing"*, *"symbolizing the financial"*.
- [ ] Tuyệt đối KHÔNG đưa mã ID phân cảnh (`CH01_SC001`) hoặc từ tham chiếu phi vật lý (`previous scene`, `next scene`) vào phần nội dung mô tả hình ảnh.
- [ ] Tệp `prompts_chapter_XX.txt` là file văn bản thuần túy (`.txt`), không dùng Markdown Table, dòng `[VIDEO]` không chứa bất kỳ ký tự tiếng Việt có dấu nào.

### 10. 🧠 Cổng 10: Tự Viết Bằng LLM Chuyên Sâu (IDE LLM Native Crafting Gate)
- [ ] Xác nhận: Toàn bộ prompt được chính LLM của IDE phân tích từ kịch bản gốc và tự tay viết, mang đầy đủ chiều sâu mỹ thuật, không thông qua bất kỳ script gom ghép máy móc nào.

---

## 📊 BẢNG MẪU BÁO CÁO TỰ DUYỆT (SELF-AUDIT REPORT TEMPLATE)
*Khi báo cáo tiến độ từng chương cho User, Agent bắt buộc phải đính kèm bảng tự duyệt tóm tắt:*

```markdown
### 🛡️ BÁO CÁO TỰ DUYỆT CHẤT LƯỢNG PROMPT (SELF-AUDIT GATE — CHƯƠNG XX)
- **Tổng số phân cảnh:** [Số cảnh] (100% $\le 26$ từ/cảnh, khớp 8.0s)
- **Tỷ lệ Text Overlay:** [X / Tổng số cảnh] (~20-25% chọn lọc, 100% khóa tĩnh ở video)
- **Kiểm tra 100% Hiện thực Vật lý:** [ĐẠT - Không có hologram/biểu tượng trừu tượng/hư vô]
- **Đồng bộ 1-1 Visual Script ↔ Prompts:** [ĐẠT 100% Scene ID khớp tuyệt đối]
- **Bảng màu 60-30-10 & Cast Sheet:** [ĐẠT chuẩn quy định của Chương XX]
- **Phương thức khởi tạo:** [100% IDE Native LLM, không dùng API/script ngoài]
```
