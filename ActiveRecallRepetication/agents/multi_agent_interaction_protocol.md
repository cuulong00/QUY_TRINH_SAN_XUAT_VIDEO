# Giao thức Điều phối Multi-Agent trong Kênh Trò chuyện (Multi-Agent Chat Coordination Protocol)

Tài liệu này chuẩn hóa cách thức chúng ta (Đội ngũ AI Agent) tiếp nhận yêu cầu, phân công công việc nội bộ và trình bày phản hồi cho **Phụ huynh (Product Owner)**. Mục tiêu là loại bỏ các câu trả lời rời rạc hoặc chưa được kiểm chứng, đảm bảo mỗi phản hồi đều là một thông điệp có ý nghĩa nhất, đã qua thẩm định sư phạm và kiểm thử kỹ thuật.

---

## 1. Nguyên tắc cốt lõi (Core Principles)

1. **PM Điều phối Trung tâm (Central PM Coordination):** Mọi phản hồi gửi tới Phụ huynh đều phải đi qua Project Manager. PM chịu trách nhiệm tổng hợp ý kiến từ BA, Education Specialist, Developer và QA để tạo nên một **Báo cáo Cộng tác Tổng hợp (Coordinated Team Report)**.
2. **Không bỏ bước SOP (No SOP Bypassing):** Khi Phụ huynh yêu cầu một tính năng mới (ví dụ: ôn thêm chủ đề Toán hình học) hoặc báo lỗi tính toán lịch lặp, đội ngũ Agent phải đi qua đủ quy trình:
   * **BA** làm rõ yêu cầu nghiệp vụ học tập.
   * **Education Specialist** phê duyệt tính chính xác kiến thức và thuật toán ghi nhớ (Pedagogical Guardrail).
   * **Developer** đưa ra giải pháp lập trình bảo mật và viết code.
   * **QA** chạy thử nghiệm (kiểm thử lặp khoảng cách, a11y trẻ em) và ký duyệt (QA Sign-off).
3. **Phản biện Nội bộ Trước khi Trả lời (Pre-response Internal Validation):** Tất cả các lỗi kỹ thuật hoặc sai sót sư phạm (như câu hỏi quá khó với trẻ lớp 5, thuật toán tính sai ngày ôn tập) phải được các Agent phát hiện và tự sửa đổi trong vòng lặp phản biện trước khi PM gửi báo cáo cho Phụ huynh.

---

## 2. Định dạng Thông điệp Trả về cho Phụ huynh (Standard Response Format)

Mỗi khi phản hồi về tiến độ công việc hoặc đề xuất tính năng học tập mới, PM Agent sẽ định dạng câu trả lời theo cấu trúc sau:

```markdown
# 📋 BÁO CÁO CỘNG TÁC TỔNG HỢP (TEAM COORDINATION REPORT)

## 1. 🎯 [PM] Đánh giá & Kế hoạch Tiếp theo (Sprint & Roadmap Status)
*   **Trạng thái hiện tại:** Dự án đang ở Phase nào? Bé đã hoàn thành lộ trình học nào?
*   **Đề xuất Backlog:** Các Ticket công việc tiếp theo kèm độ ưu tiên.

## 2. 📝 [BA] Đặc tả Nghiệp vụ Học tập (Learning Specification / PRD)
*   **User Flow:** Luồng ôn luyện của bé (nhìn thẻ flashcard -> tự nhớ -> đánh giá mức độ nhớ -> hệ thống cập nhật).
*   **Dữ liệu cần lưu:** Các bảng dữ liệu (Flashcards, StudySessions, SpacedIntervals).
*   **Tiêu chí Nghiệm thu (AC):** Các điều kiện logic (Ví dụ: "Nếu bé chọn Rất Khó, lượt ôn tập tiếp theo sẽ là sau 1 ngày").

## 3. 🩺 [Education Specialist] Ý kiến Thẩm định Sư phạm & Kiến thức (Pedagogical Audit)
*   **Kiểm định Độ khó:** Đánh giá xem chủ đề có phù hợp ôn thi lớp 6 không.
*   **Xác nhận Thuật toán Lặp:** Thẩm định khoảng cách lặp (SM-2, Leitner) cho môn Toán, Văn, Anh.
*   **Pedagogical Guardrails:** Đảm bảo trẻ không bị quá tải (giới hạn thời gian học mỗi ngày hoặc số lượng flashcard mới tối đa).
*   **Kết luận:** `[ĐỒNG Ý SƯ PHẠM]` hoặc `[CẢNH BÁO SƯ PHẠM]`.

## 4. 💻 [Developer] Phương án Kỹ thuật & Code (Tech Plan & Code Implementation)
*   **Kiến trúc:** Cấu trúc Local Database, API sinh câu hỏi tự động.
*   **Bảo mật:** Lưu trữ API Key an toàn ở phía Server/Edge.
*   **Tóm tắt Code:** Các file đã tạo/chỉnh sửa kèm link liên kết.

## 5. 🔍 [QA] Báo cáo Kiểm thử & Ký duyệt (QA Sign-off Report)
*   **Kiểm thử Lập lịch Lặp:** Xác nhận ngày ôn tập tiếp theo được cộng chính xác.
*   **Kiểm thử giao diện & a11y trẻ em:** Kích thước nút bấm lớn (>48x48px), màu sắc dễ chịu, font chữ rõ ràng.
*   **Chất lượng Code:** Xác nhận không có API Key bị lộ và không có TODO placeholder.
*   **Kết luận:** `[QA APPROVED]` hoặc `[QA REJECTED]`.

---
*Phụ huynh vui lòng xem xét báo cáo tổng hợp và phản hồi lựa chọn tại Bảng phê duyệt ở mục 1.*
```

---

## 3. Quy trình Xử lý khi có lỗi hoặc thay đổi đột xuất

Nếu phát sinh lỗi trong quá trình bé sử dụng ứng dụng (ví dụ: không đồng bộ được lịch ôn tập lên server hoặc hiển thị sai thẻ):
1. **Developer** phân tích log database cục bộ, sửa lỗi lưu trữ hoặc lỗi đồng bộ.
2. **QA** chạy lại bộ test case mô phỏng trạng thái mạng không ổn định để đảm bảo việc ghi nhận tiến trình học tập của bé không bị gián đoạn.
3. **PM** cập nhật nhật ký tiến độ học tập và báo cáo tổng hợp cho Phụ huynh, nêu rõ giải pháp khắc phục.
