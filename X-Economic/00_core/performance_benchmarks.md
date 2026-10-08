# Performance Benchmarks — X-Economy

> **Mục đích:** File này là nguồn sự thật duy nhất cho baseline performance của kênh. Mọi postmortem và planning đều so sánh với file này.
> **Cập nhật:** Sau mỗi postmortem hoặc khi có sự thay đổi lớn về performance do User cung cấp từ YouTube Studio.

---

## 1. Baseline Metrics

| Chỉ số | Baseline hiện tại | Mục tiêu | Ghi chú |
|--------|-------------------|----------|---------|
| CTR trung bình | [CHỜ USER CUNG CẤP TỪ YOUTUBE STUDIO] | [CHỜ USER XÁC ĐỊNH] | Cập nhật từ YouTube Studio |
| AVD trung bình | [CHỜ USER CUNG CẤP TỪ YOUTUBE STUDIO] | [CHỜ USER XÁC ĐỊNH] | Tính trên video dài |
| AVD % trung bình (Long) | [CHỜ USER CUNG CẤP TỪ YOUTUBE STUDIO] | [CHỜ USER XÁC ĐỊNH] | Tỷ lệ giữ chân thực tế |
| Views/48h trung bình | [CHỜ USER CUNG CẤP TỪ YOUTUBE STUDIO] | [CHỜ USER XÁC ĐỊNH] | |
| Subscriber conversion | [CHỜ USER CUNG CẤP TỪ YOUTUBE STUDIO] | [CHỜ USER XÁC ĐỊNH] | |
| Comment rate | [CHỜ USER CUNG CẤP TỪ YOUTUBE STUDIO] | [CHỜ USER XÁC ĐỊNH] | Tối ưu bằng Comment Hook cuối tập |

---

## 2. Retention Curve Patterns

### Pattern đã xác nhận
- **Độ dài ngọt ngào (Length Sweet Spot):** [CHỜ USER CUNG CẤP TỪ YOUTUBE STUDIO]. Các video dài hơn 20 phút dễ bị hụt hơi trừ khi có kịch tính đối đầu và cơ chế dữ liệu đa tầng cao.
- **Drop phút 5 (Lỗi Data Dumping):** Xảy ra khi Chương 2 không có điểm chạm liên quan (Relevance Anchor), nhồi nhét lý thuyết thuần túy. Khán giả rời đi vì không thấy mâu thuẫn hay cơ chế thiết thực.
- **Giữ chân cao (Personal Stakes / Relevance Hook):** Chuyển dịch một vấn đề vĩ mô thành áp lực tài chính, chi phí, hoặc bài toán đánh đổi trực tiếp đè lên đời sống và hoạt động kinh doanh của người xem.
- **Lỗi Đề tài Trừu tượng:** Các chủ đề thiếu dữ liệu thực chứng và cơ chế thị trường cụ thể dễ bị người xem bỏ qua hoặc rơi rớt giữ chân nghiêm trọng.
- **Kịch tính Địa kinh tế & Chuỗi cung ứng:** Khai thác sự va đập giữa các mô hình kinh tế, cạnh tranh công nghệ và dòng chảy tiền tệ quốc tế để tạo sự chú ý bền bỉ.
- **Lỗi Hypothetical Stakes:** Bắt người xem tưởng tượng rủi ro xa xôi ở một thị trường không có sợi dây liên kết nào về xuất khẩu, tỷ giá hay chuỗi giá trị trong nước, làm giảm độ quan tâm.

### Ngưỡng nguy hiểm
- Nếu retention rơi > 15% trong 1 phút: có đoạn chết nhịp hoặc nhồi nhét lý thuyết không có dữ liệu dẫn dắt.
- Nếu AVD < 30%: cấu trúc kịch bản và sự kết nối giữa các chương có vấn đề nghiêm trọng.
- Nếu CTR < 3%: title và thumbnail chưa tạo được câu đố mở hoặc mâu thuẫn sắc bén.

---

## 3. Title & Thumbnail Performance

### Title patterns hoạt động tốt
| Pattern | Ví dụ | CTR trung bình |
|---------|-------|----------------|
| [THU THẬP DỮ LIỆU] | | |

### Title patterns hoạt động kém
| Pattern | Ví dụ | CTR trung bình | Lý do |
|---------|-------|----------------|-------|
| Thuật ngữ chuyên gia quá hẹp | Tiêu đề dùng từ kỹ thuật khó hiểu | Thấp | Khán giả đại chúng không tìm kiếm |

### Thumbnail patterns
| Pattern | CTR | Ghi chú |
|---------|-----|---------|
| [THU THẬP DỮ LIỆU] | | |

---

## 4. Content Category Performance

| Loại nội dung | Số episodes | AVD trung bình | CTR trung bình | Ghi chú |
|---------------|-------------|----------------|----------------|---------|
| Loại A (Đời sống kinh tế) | [ĐẾM] | | | |
| Loại B (Chiến lược doanh nghiệp / Ngành) | [ĐẾM] | | | |
| Loại C (Quy luật vĩ mô / Toàn cầu) | [ĐẾM] | | | |

---

## 5. Hook Strategy Performance

| Hook strategy | Lần dùng | CTR trung bình | Retention phút 1 | Hiệu quả |
|---------------|----------|----------------|-------------------|----------|
| Data contrast | [ĐẾM] | | | |
| Common vs sharper reading | [ĐẾM] | | | |
| Quiet expert question | [ĐẾM] | | | |
| Persona pain + structure | [ĐẾM] | | | |
| Historical mirror | [ĐẾM] | | | |

---

## 6. Quy tắc cập nhật
1. Sau mỗi postmortem: cập nhật các bảng trên dựa trên số liệu thực tế do User cung cấp.
2. Sau mỗi 10 episodes: tính lại baseline trung bình.
3. Khi phát hiện pattern mới: bổ sung vào Mục 2 hoặc Mục 3.
4. Khi baseline thay đổi > 20%: rà soát lại toàn bộ quy trình để tối ưu hóa.
