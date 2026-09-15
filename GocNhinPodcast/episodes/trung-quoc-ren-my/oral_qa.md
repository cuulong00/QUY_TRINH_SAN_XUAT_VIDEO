# Oral QA Report

**Episode:** trung-quoc-ren-my (Địa Chính Trị Mỹ - Trung: Răn Đe và Giới Hạn Quyền Lực)
**Chuyên gia thực hiện:** The Voice Architect + Oral Polisher
**Ngày kiểm định:** 2026-06-20

## 1. Kết quả kiểm tra tổng quan
- **Giới hạn độ dài câu (<150 ký tự):** **100% PASS**. Toàn bộ kịch bản đã được viết lại với các câu ngắn, rõ chủ vị, giúp mô hình TTS local chạy dính chữ chuẩn, không bị chú ý trôi (attention drift) hay ngắt hơi sai vị trí.
- **Rhythmic Pacing (Nhịp điệu dồn dập):** **PASS**. Có sự trộn lẫn chủ ý giữa câu cực ngắn nhấn mạnh (Ví dụ: "7,92 triệu ca sinh.", "Không ai dám nổ súng trước.", "Bán tháo là tự sát tài chính.") và các câu phân tích cơ chế trung bình (12-18 từ).
- **Anti-AI-isms:** **100% PASS**. Đã lọc bỏ toàn bộ các từ cấm vĩ mô hoặc transition sáo rỗng ("bóc tách", "cứu trợ", "gã khổng lồ", "lá bài đối trọng", "bàn cờ địa chính trị", "hoãn và giả vờ").
- **Dọn dẹp sản xuất:** **PASS**. Cả 7 file `chapter_XX.md` đã được dọn sạch hoàn toàn tiêu đề chương, chú thích kỹ thuật và các bảng biểu kiểm chứng ở cuối. Chỉ giữ lại phần đọc thoại sạch 100%.

---

## 2. Hướng dẫn phát âm và Việt hóa danh từ riêng cho TTS
Để đảm bảo mô hình TTS đọc chuẩn xác các tên riêng quốc tế và tên viết tắt, dưới đây là bảng ánh xạ phát âm khuyến nghị:

| Từ gốc | Cách viết trong kịch bản | Khuyến nghị phát âm (hoặc cấu hình từ điển TTS) |
|---|---|---|
| **Weiwen** | Weiwen | "vây uân" (hoặc đọc chuẩn bính âm: wéiwěn) |
| **Luzon** | Luzon | "lu-dông" / "lu-xơn" (lưu ý đọc nhẹ) |
| **Yingji-17** | Yingji-17 | "inh-ghi mười bảy" |
| **G7** | G7 | "gê bảy" |
| **USD** | USD | "u-ét-đê" / "đô la Mỹ" |
| **VND** | VND | "việt nam đồng" |
| **FDI** | FDI | "ép-đê-i" / "vốn đầu tư nước ngoài" |
| **ASML** | ASML | "a-ét-em-lờ" |
| **EUV** | EUV | "e-u-vê" |
| **DUV** | DUV | "đê-u-vê" |
| **Cymer** | Cymer | "sai-mơ" |
| **HiSilicon** | HiSilicon | "hai-si-li-côn" |
| **DeepSeek** | DeepSeek | "đíp-xích" / "đíp-xick" |
| **IMF** | IMF | "i-em-ép" |
| **GDP** | GDP | "gê-đê-pê" |
| **LGFV** | LGFV | "lờ-gê-ép-vê" |

---

## 3. Cầu nối chương (Bridge Audit)
Kiểm tra tính liên kết nhân quả (Luật But/Therefore) và câu hở tiềm thức (Subconscious Loop) ở các điểm giao chương:
- **Bridge 1-2 (Weiwen -> Luzon):**
  - *Chương 1 kết:* "...đối phó rạn nứt bên trong để giữ thế thủ dẻo dai. Sự ổn định này ảnh hưởng trực tiếp kinh tế Việt Nam. Hãy cùng phân tích cơ chế này ngay sau đây."
  - *Chương 2 mở:* "Hãy đứng ở đảo Luzon của Philippines..."
  - *Đánh giá:* Tạo một chuyển cảnh không gian đột ngột nhưng logic, từ bàn phân tích vĩ mô sang thực địa quân sự (Scene Specificity).
- **Bridge 2-3 (Luzon -> Dollar Dilemma):**
  - *Chương 2 kết:* "...Bắc Kinh còn phải đối mặt với những ràng buộc tài chính khổng lồ khác."
  - *Chương 3 mở:* "Trung Quốc đang nắm giữ 3.442,2 tỷ USD dự trữ ngoại hối..."
  - *Đánh giá:* Đạt luật **Therefore/But** xuất sắc. Nối trực tiếp từ "ràng buộc tài chính" sang con số dự trữ ngoại hối khổng lồ.
- **Bridge 3-4 (Dollar Dilemma -> Malacca):**
  - *Chương 3 kết:* "...thế bẫy đô la Mỹ vẫn là thế kẹt mang tính cấu trúc. Bên cạnh điểm nghẽn về dòng tiền, Trung Quốc còn đối mặt với những nút thắt vật lý nguy hiểm khác."
  - *Chương 4 mở:* "Hạ tầng nhân tạo có thể xây dựng bằng tiền. Nhưng địa lý là một định mệnh bất biến..."
  - *Đánh giá:* Tạo sự tò mò vật lý (nút thắt Malacca) ngay sau khi phân tích nút thắt tài chính.
- **Bridge 4-5 (Malacca -> Bán dẫn ASML):**
  - *Chương 4 kết:* "...Hồi chuông cảnh báo về năng lượng và lương thực cho thấy Bắc Kinh nhạy cảm thế nào. Nhưng bức tường lớn nhất ngăn họ bứt phá, lại là một công nghệ siêu vi."
  - *Chương 5 mở:* "Trong kỷ nguyên số, tiền bạc không thể mua được chủ quyền công nghệ..."
  - *Đánh giá:* Kéo người nghe qua vạch bằng khái niệm "công nghệ siêu vi" và mở đầu bằng "chủ quyền công nghệ".
- **Bridge 5-6 (Bán dẫn ASML -> Nợ ẩn LGFV):**
  - *Chương 5 kết:* "...Nhưng để đón đầu làn sóng này, chúng ta cần hiểu rõ những rạn nứt tài chính sâu sắc ngay bên trong lòng Trung Quốc."
  - *Chương 6 mở:* "Vết rạn nứt nghiêm trọng nhất của một siêu cường thường không nằm ở biên giới quân sự..."
  - *Đánh giá:* Subconscious loop mượt mà, chuyển từ "rạn nứt tài chính sâu sắc" sang "bảng cân đối kế toán của địa phương".
- **Bridge 6-7 (LGFV -> Đối trọng & Vàng, DeepSeek):**
  - *Chương 6 kết:* "...Điều này buộc Bắc Kinh phải duy trì trạng thái kiềm chế chiến lược."
  - *Chương 7 mở:* "Nhưng sẽ là sai lầm nếu cho rằng Bắc Kinh sẽ dễ dàng nhượng bộ..."
  - *Đánh giá:* Đối lập trực tiếp bằng liên từ nghịch bộ, tăng tension cực độ trước khi chốt hạ.
