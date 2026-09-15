# 📜 QUY CHUẨN ĐỊNH DẠNG FILE PROMPT ĐẦU VÀO (.txt)

Tài liệu này định nghĩa cấu trúc của file text chứa prompt (ví dụ: `prompts_ch01.txt`) để phần mềm parse tự động 100% không bị lỗi.

---

## 1. Cấu Trúc Cơ Bản Của Một Phân Cảnh (Scene)

Mỗi phân cảnh bao gồm 2 dòng tương ứng: Dòng `[IMAGE]` và dòng `[VIDEO]`, dùng chung một `Scene ID` (ví dụ: `CH01_SC001`).

* **Quy chuẩn khoảng cách:**
  - Trong **cùng 1 phân cảnh**: Dòng `[IMAGE]` và dòng `[VIDEO]` viết **LIỀN KỀ NHAU** (không để dòng trắng ở giữa).
  - Giữa **2 phân cảnh khác nhau**: Cách nhau đúng **1 dòng trắng** để dễ phân tách thị giác.

```text
CH01_SC001 [IMAGE]: <Mô tả hình ảnh tạo ra>
CH01_SC001 [VIDEO]: @CH01_SC001.png -> <Mô tả chuyển động video> --ar 16:9 --dur 8s

CH01_SC002 [IMAGE]: <Mô tả hình ảnh tạo ra>
CH01_SC002 [VIDEO]: @CH01_SC002.png -> <Mô tả chuyển động video> --ar 16:9 --dur 8s
```

---

## 2. Các Trường Hợp Sử Dụng (Use Cases)

### Trường hợp A: Tạo ảnh hoàn toàn mới -> Lấy ảnh đó làm tham chiếu tạo video
```text
CH01_SC001 [IMAGE]: A flat 2D vector illustration of a colossal suction bucket foundation on sea barge, titanium grey steel, dramatic morning sunlight, no text.
CH01_SC001 [VIDEO]: @CH01_SC001.png -> Slow cinematic tracking shot as the sea barge cruises forward, subtle water ripples, 8-second continuous documentary video --ar 16:9
```
* **Cơ chế:** Ký hiệu `@CH01_SC001.png ->` ở dòng video báo cho hệ thống biết **video này phải chờ ảnh của CH01_SC001 tạo xong**, sau đó lấy ảnh đó nạp làm input cho Veo 3.1.

---

### Trường hợp B: Dùng ảnh tham chiếu do bạn tải lên để tạo ảnh -> Sau đó tạo video
```text
CH01_SC002 [IMAGE]: @engineer_portrait.png -> A flat 2D vector illustration of the Vietnamese engineer standing in the fabrication bay, wearing safety hardhat and navy jumpsuit.
CH01_SC002 [VIDEO]: @CH01_SC002.png -> Slow camera tilt-up from boots to face as the engineer examines digital tablet, warm ambient lighting --ar 16:9
```
* **Cơ chế:** 
  * Bạn kéo thả file `engineer_portrait.png` vào ô **Reference Asset Bin** trên giao diện.
  * Hệ thống phát hiện tag `@engineer_portrait.png` ở dòng `[IMAGE]` và tự động gắn file này làm tham chiếu cho `🍌 Nano Banana 2`.
  * Sau khi sinh ra ảnh mới của phân cảnh, hệ thống tiếp tục dùng ảnh mới đó tạo video.

---

## 3. Các Cờ Tham Số Bổ Trợ (Inline Flags)

* `--ar 16:9` (hoặc `9:16`, `1:1`): Ép tỉ lệ khung hình cho phân cảnh đó.
* `--dur 8s` (hoặc `5s`, `6s`): Ép thời lượng video.
