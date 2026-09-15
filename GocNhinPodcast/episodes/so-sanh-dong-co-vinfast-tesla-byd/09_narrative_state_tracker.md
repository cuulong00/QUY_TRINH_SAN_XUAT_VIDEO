# Narrative State Tracker (NST) — so-sanh-dong-co-vinfast-tesla-byd

Tệp tin theo dõi trạng thái mạch kể chuyện, quản lý vòng lặp câu hỏi (Loops) và đăng ký "gieo hạt - gặt hạt" (Seeding-Harvesting) giữa các chương kịch bản để đảm bảo dòng chảy logic liền mạch 100%.

---

## I. Câu Hỏi Bỏ Ngỏ & Vòng Lặp Trí Tuệ (Question Loops)

| ID | Câu hỏi / Vòng lặp nhận thức | Được mở ở | Được đóng ở | Trạng thái | Ghi chú |
|:---|:-----------------------------|:----------|:------------|:-----------|:--------|
| **L01**| Tiếng rít gầm xe trên cao tốc bắt nguồn từ cơ chế vật lý nào? | Chương 1 | Chương 2 | Đã hoàn thành | Giải thích bằng lực ly tâm hướng vòng ở 20.000 RPM. |
| **L02**| Làm thế nào để giữ chặt nam châm vĩnh cửu trong rotor không bị vỡ tung? | Chương 2 | Chương 3 | Đang mở | Giải thích qua giải pháp bọc carbon AFP của Tesla. |
| **L03**| BYD làm thế nào để tối ưu chi phí và tăng mật độ công suất mà không dùng carbon đắt tiền? | Chương 3 | Chương 4 | Đang chờ viết | Phân tích cơ chế 12-trong-1, thép 0.2mm ghép keo Backlack. |
| **L04**| Rủi ro sửa chữa của 12-in-1 là gì? VinFast giải bài toán độ bền cơ khí này ra sao? | Chương 4 | Chương 5 | Đang chờ viết | Phân tích stator X-pin Haosen, bánh răng mài mịn và bi gốm ZF. |
| **L05**| Sự đánh đổi giữa an toàn gầm chắc và hao điện năng của VinFast được giải thế nào? | Chương 5 | Chương 6 | Đang chờ viết | So sánh VF 8 cũ nặng 2.5 tấn với VF 8 All-New giảm 600kg. |
| **L06**| Cuộc chiến tản nhiệt dưới trưa nắng nóng 40 độ tại Việt Nam bên nào tối ưu hơn? | Chương 6 | Chương 7 | Đang chờ viết | So sánh dầu ATF trực tiếp (Tesla/BYD) và glycol ITM kết nối HVAC (VinFast). |
| **L07**| Làm thế nào để người tiêu dùng không bị rơi vào bẫy quảng cáo mã lực? | Chương 7 | Chương 8 | Đang chờ viết | Rút ra triết lý đánh đổi cơ học và hướng dẫn tiêu dùng thông thái. |
|

---

## II. Đăng Ký Gieo Hạt & Gặt Hạt (Seeding-Harvesting Registry)

```
 Chương 1: Hook Chính
   ├── [Gieo hạt H01] (2 câu cuối): Làm thế nào để giữ nam châm vĩnh cửu trong lõi không bị vỡ tung ở tua máy cao?
   ▼
 Chương 2: Thế Kẹt Của Những Khối Nam Châm
   ├── [Gặt hạt H01] (2 câu đầu): "Gặt" hạt H01 bằng việc mô tả lực ly tâm giống đu quay văng mạnh.
   ├── [Gieo hạt H02] (2 câu cuối): Tesla đã phải mượn vật liệu hàng không vũ trụ nào để bó chặt rotor?
   ▼
 Chương 3: Tesla và Sợi Carbon Giới Hạn Cực Hạn
   ├── [Gặt hạt H02] (2 câu đầu): "Gặt" hạt H02 bằng cách chỉ ra áo giáp sợi carbon quấn tự động AFP.
   ├── [Gieo hạt H03] (2 câu cuối): Quấn carbon quá đắt đỏ cho xe bình dân, vậy đối thủ Trung Quốc BYD giải bài toán này thế nào?
   ▼
 Chương 4: BYD và Cú Bắt Tay Tích Hợp "12 Trong 1"
   ├── [Gặt hạt H03] (2 câu đầu): "Gặt" hạt H03 bằng cách giới thiệu cấu trúc tích hợp 12-trong-1 siêu gọn giá rẻ.
   ├── [Gieo hạt H04] (2 câu cuối): Tích hợp sâu có rủi ro chi phí sửa chữa khổng lồ. Vậy VinFast chọn hướng đi cơ khí truyền thống nào để phát triển bền bỉ?
   ▼
 Chương 5: VinFast và Lực Vặn Cơ Khí Thực Dụng
   ├── [Gặt hạt H04] (2 câu đầu): "Gặt" hạt H04 bằng cách chỉ ra cú bắt tay cơ khí với ZF và công nghệ quấn dây X-pin Haosen.
   ├── [Gieo hạt H05] (2 câu cuối): Tuy nhiên, nền tảng cơ khí đầm chắc này lại đẩy xe vào một bài toán khó về cân nặng. Nó đã móc túi người tiêu dùng thế nào?
   ▼
 Chương 6: Khi Khung Gầm Gánh Nặng Trọng Lực
   ├── [Gặt hạt H05] (2 câu đầu): "Gặt" hạt H05 bằng cách mổ xẻ trọng lượng 2.5 tấn của VF 8 cũ và cú giảm cân 600kg của bản All-New.
   ├── [Gieo hạt H06] (2 câu cuối): Việc giảm cân và tải nặng sinh ra lượng nhiệt lớn khi sạc nhanh. Hai phương pháp tản nhiệt nào đang đối đầu nhau dưới nắp capo?
   ▼
 Chương 7: Cuộc Chiến Tản Nhiệt: Dầu ATF vs Hệ Thống ITM
   ├── [Gặt hạt H06] (2 câu đầu): "Gặt" hạt H06 bằng cách đối đầu trực diện giữa làm mát dầu ATF trực tiếp và glycol ITM gián tiếp.
   ├── [Gieo hạt H07] (2 câu cuối): Vậy sau tất cả các cơ chế vật lý đó, đâu mới là chiếc chìa khóa giúp bạn đưa ra lựa chọn mua xe thông thái nhất?
   ▼
 Chương 8: Lăng Kính Năng Lượng Đằng Sau Mã Lực
   └── [Gặt hạt H07] (2 câu đầu): "Gặt" hạt H07 bằng cách định nghĩa lại giá trị của mã lực và triết lý cơ khí phù hợp nhu cầu.
```

---

## III. Nhật Ký Trạng thái Biên Tập Đang Chạy
- **Chapter 1:** Đã hoàn thành.
- **Chapter 2:** Đã hoàn thành.
- **Chapter 3:** Chưa viết.
- **Chapter 4:** Chưa viết.
- **Chapter 5:** Chưa viết.
- **Chapter 6:** Chưa viết.
- **Chapter 7:** Chưa viết.
- **Chapter 8:** Chưa viết.
