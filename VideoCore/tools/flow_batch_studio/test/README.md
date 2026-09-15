# 🧪 HƯỚNG DẪN TEST PIPELINE THAM CHIẾU (IMAGE-TO-IMAGE -> VIDEO)

Thư mục này chứa bộ tài nguyên thử nghiệm tính năng **nạp ảnh tham chiếu** và **tạo chuỗi Image -> Video** trên Google Flow Batch Studio.

---

## 📁 Danh sách tệp tin trong thư mục `test/`

1. **`tbt_tolam.jpg`**: Ảnh chân dung Tổng Bí thư Tô Lâm (Việt Nam).
2. **`thutuongthailan.jpg`**: Ảnh chân dung Thủ tướng Paetongtarn Shinawatra (Thái Lan).
3. **`philipin.jpg`**: Ảnh chân dung Tổng thống Ferdinand Marcos Jr. (Philippines).
4. **`indonesia.jpg`**: Ảnh chân dung Tổng thống Prabowo Subianto (Indonesia - đã upscale và chuyển JPG).
5. **`test_reference_prompts.txt`**: File kịch bản prompt chuẩn hóa gồm 4 phân cảnh (`TEST_SC001` đến `TEST_SC004`).

---

## 🚀 Các bước thực hiện trên ứng dụng Google Flow Batch Studio

1. **Bước 1 — Nạp ảnh tham chiếu (Reference Asset Bin):**
   - Mở giao diện ứng dụng Flow Batch Studio.
   - Kéo thả cả 4 file ảnh (`tbt_tolam.jpg`, `thutuongthailan.jpg`, `philipin.jpg`, `indonesia.webp`) vào vùng **Reference Asset Bin** (hoặc click chọn file).
   - Xác nhận 4 ảnh hiển thị trong danh sách asset đã nạp.

2. **Bước 2 — Nạp file kịch bản prompt:**
   - Click nút **Upload Storytrack (.txt)** và chọn file `test_reference_prompts.txt`.
   - Hệ thống tự động parse 4 phân cảnh vào hàng đợi (Queue):
     * `TEST_SC001`: Step 1 tham chiếu `@tbt_tolam.jpg` $\rightarrow$ Step 2 Veo nhận `@TEST_SC001.png`
     * `TEST_SC002`: Step 1 tham chiếu `@thutuongthailan.jpg` $\rightarrow$ Step 2 Veo nhận `@TEST_SC002.png`
     * `TEST_SC003`: Step 1 tham chiếu `@philipin.jpg` $\rightarrow$ Step 2 Veo nhận `@TEST_SC003.png`
     * `TEST_SC004`: Step 1 tham chiếu `@indonesia.webp` $\rightarrow$ Step 2 Veo nhận `@TEST_SC004.png`

3. **Bước 3 — Kiểm tra cấu hình Model & Bắt đầu:**
   - **Video Model:** `Veo 3.1 - Lite [Lower Priority]` (0 credit tier).
   - **Image Model:** `🍌 Nano Banana 2`.
   - **Mode:** `Chained: Image → Video`.
   - Click **Start Batch Production**.
   - Quan sát tab **Activity Logs Console** và hàng đợi chạy mượt mà từng scene.
