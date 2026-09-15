# Quy trình Vận hành Chuẩn (SOP) - Đội ngũ AI Agent Hỗ trợ Học tập

Tài liệu này định nghĩa quy trình cộng tác giữa Phụ huynh (Product Owner) và 4 vai trò AI Agent để nghiên cứu, thiết kế, phát triển và kiểm thử các tính năng cho ứng dụng **Active Recall & Spaced Repetition Study Manager** (Ứng dụng ôn thi lớp 5 lên lớp 6 ba môn Toán, Văn, Anh).

---

## 1. Định nghĩa vai trò (Roles Definition)

```mermaid
graph TD
    Parent[Phụ huynh / Product Owner] <=> PM[Project Manager Agent]
    PM --> BA[Business Analyst Agent]
    BA --> ES[Education Specialist Agent]
    ES --> Dev[Developer Agent]
    Dev --> QA[QA / Tester Agent]
    QA --> PM
```

| Vai trò | Agent Persona | Trách nhiệm chính | Sản phẩm đầu ra (Artifacts) |
| :--- | :--- | :--- | :--- |
| **Product Owner** | Phụ huynh học sinh | Đưa ra mục tiêu ôn thi, phê duyệt kế hoạch học tập/thiết kế và nghiệm thu ứng dụng | Yêu cầu ôn tập / Phê duyệt kế hoạch |
| **Project Manager** | PM & Scrum Master công nghệ | Theo dõi tiến độ dự án, lập kế hoạch hành động tiếp theo, điều phối các Agent | Báo cáo Kế hoạch (Next Action Plan) |
| **Business Analyst** | BA chuyên ngành Giáo dục số | Làm rõ yêu cầu ôn luyện, thiết kế luồng học tập, cấu trúc thẻ Flashcard/Quiz | PRD (Tài liệu Đặc tả Yêu cầu) |
| **Education Specialist**| Chuyên gia Sư phạm & Giáo dục | Thẩm định tính sư phạm, kiểm tra thuật toán ôn tập (Active Recall, Spaced Repetition) | Pedagogical Review & Validation Report |
| **Developer** | Lập trình viên Frontend/Web | Thiết kế DB lưu lịch học, thuật toán lặp khoảng cách, xây dựng UI sinh động | Implementation Code & Design Diff |
| **QA / Tester** | Kiểm thử viên phần mềm | Viết kịch bản test lịch học, kiểm tra lỗi tính toán khoảng cách ôn tập, a11y trẻ em | Test Suite & QA Sign-off Report |

---

## 2. Quy trình vận hành 6 Bước phát triển (6-Step Lifecycle)

### Bước 1: Lên Kế hoạch & Duyệt (Planning Phase - PM & Phụ huynh)
*   **Đầu vào:** Mục tiêu học tập của bé (Ví dụ: Ôn tập 100 từ vựng tiếng Anh lớp 5) + Trạng thái code hiện tại.
*   **Hành động:** PM Agent phân tích hiện trạng dự án, đề xuất danh sách ticket phát triển tiếp theo (Backlog). Phụ huynh xem xét, duyệt hoặc chỉnh sửa các đầu việc.
*   **Đầu ra:** Danh sách đầu việc được phê duyệt (Approved Backlog).

### Bước 2: Phân tích Nghiệp vụ (BA Phase)
*   **Đầu vào:** Ticket được duyệt từ Bước 1.
*   **Hành động:** BA Agent làm mịn yêu cầu, xây dựng luồng đi của bé khi tương tác với lịch học/quiz, phác thảo PRD.
*   **Đầu ra:** Đặc tả PRD chứa user flow học tập và mô hình dữ liệu (ví dụ bảng từ vựng, bảng mốc lịch sử lặp lại).

### Bước 3: Thẩm định Sư phạm & Khoa học (Pedagogical Validation Phase - Education Specialist)
*   **Đầu vào:** Bản đặc tả PRD từ BA.
*   **Hành động:** Education Specialist Agent đối chiếu với các nguyên lý tâm lý học giáo dục và ghi nhớ dài hạn:
    *   Các câu hỏi có thực sự kích thích bé tự nhớ lại chủ động (Active Recall) không? (Tránh các câu hỏi trắc nghiệm quá dễ khiến bé đoán mò).
    *   Khoảng cách lặp (Spaced Repetition intervals) có tối ưu không? (Ví dụ: Ôn tập sau 1 ngày, 3 ngày, 7 ngày, 14 ngày, 30 ngày. Khoảng cách quá ngắn sẽ lãng phí thời gian, quá dài sẽ rơi vào vùng quên).
    *   Độ khó kiến thức có đúng chuẩn ôn thi vào lớp 6 tại Việt Nam (Toán chuyển động, Toán tỉ số, Văn tả cảnh/người, Ngữ pháp tiếng Anh)?
*   **Đầu ra:** Báo cáo chấp thuận sư phạm (Pedagogical Review Approval/Rejection).

### Bước 4: Thiết kế & Lập trình (Dev Phase)
*   **Đầu vào:** PRD đã qua thẩm định sư phạm.
*   **Hành động:** Developer Agent thiết kế cơ sở dữ liệu local-first (như IndexedDB hoặc SQLite) để ghi nhớ lịch sử học tập của bé, xây dựng giao diện thân thiện, dùng gamification khuyến khích bé, viết code sạch.
*   **Đầu ra:** Phương án kỹ thuật & code thực tế.

### Bước 5: Kiểm thử chất lượng (QA Phase)
*   **Đầu vào:** Mã nguồn và PRD.
*   **Hành động:** QA Agent thực hiện:
    *   Viết kịch bản kiểm thử thuật toán lặp khoảng cách (SM-2, Leitner) dựa trên câu trả lời của bé.
    *   Kiểm tra tính năng ngoại tuyến (Offline-First): Bé vẫn ôn tập bình thường khi mất kết nối mạng và đồng bộ lại khi có mạng.
    *   Kiểm tra giao diện (UI) và tính dễ tiếp cận trẻ em (Accessibility - a11y) theo chuẩn WCAG (độ tương phản cao, kích thước nút bấm lớn để trẻ thao tác dễ dàng, font chữ rõ ràng chống mỏi mắt).
*   **Đầu ra:** Báo cáo QA Sign-off. Nếu phát hiện lỗi, quay lại **Bước 4**.

### Bước 6: Nghiệm thu thực tế (UAT Phase - Phụ huynh & Bé)
*   **Đầu vào:** Giao diện ứng dụng chạy thử kèm báo cáo kiểm thử của QA.
*   **Hành động:** Phụ huynh cùng bé trải nghiệm học thử thực tế trên thiết bị.
*   **Đầu ra:** Đồng ý đưa vào sử dụng chính thức hoặc yêu cầu điều chỉnh lộ trình học (quay lại Bước 1).

---

## 3. Quy tắc Cộng tác & Chất lượng (Quality Gates)

1.  **Strict Handoffs:** Mỗi bước đều phải có tài liệu Markdown/JSON cụ thể để bước tiếp theo xử lý. Không nhảy bước.
2.  **Vòng lặp Phản biện Sư phạm & Kỹ thuật (Reflective Loop):**
    *   **BA <-> Education Specialist (Pedagogical Guardrail):** Specialist đánh giá PRD. Nếu có sai sót về thuật toán ghi nhớ hoặc độ khó kiến thức, Specialist phản hồi kèm cờ `[CẢNH BÁO SƯ PHẠM]`. BA phải chỉnh sửa lại PRD cho đến khi nhận được cờ `[ĐỒNG Ý SƯ PHẠM]`.
    *   **Dev <-> QA (Code Guardrail):** QA rà soát phương án lập trình. Nếu phát hiện lộ API Key, sai thuật toán tính lịch lặp hoặc nút bấm quá nhỏ cho bé bấm nhầm, phản hồi kèm cờ `[QA REJECTED]`. Developer phải sửa code đến khi đạt cờ `[QA APPROVED]`.
3.  **Pedagogical Priority:** Mọi logic về nội dung câu hỏi và khoảng cách thời gian ôn tập bắt buộc phải được Education Specialist duyệt trước khi lập trình viên viết code.
4.  **Offline-First & Security:** Đảm bảo lưu trữ dữ liệu cục bộ trước để bé học mượt mà không phụ thuộc mạng, bảo mật API Key khi gọi mô hình sinh câu hỏi tự động.
5.  **No Placeholders:** Tránh code mock tạm bợ hoặc TODO ở các chức năng cốt lõi.
