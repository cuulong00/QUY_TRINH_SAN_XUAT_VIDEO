# episodes-general

Áp dụng cho mọi công việc trong `episodes/**`.

## Rule
- Chỉ làm việc trong một episode cụ thể.
- Mỗi lần chỉ làm đúng một pha.
- Không được nhảy cóc sang pha sau khi upstream state chưa tồn tại.
- Không được trả full script one-shot từ raw topic.
- Sau mỗi pha phải cập nhật file state của pha đó.
- Sau mỗi pha phải cập nhật `01_management/episode_registry.csv`.
- Sau mỗi pha phải cập nhật visibility layer theo `.claude/rules/operator-visibility.md`.
- Nếu phát hiện user đang xin output cuối khi episode chưa đến pha hợp lệ, phải điều hướng về pha kế tiếp hợp lệ.

## Editorial quality rule
- Mỗi pha tạo nội dung phải ưu tiên chiều sâu thật, không chỉ độ sạch của workflow.
- Nếu output nghe công nghiệp, generic, AI-ish, hoặc không có lập trường đủ rõ, phải tự coi đó là vấn đề chất lượng cần sửa.
- Một output đúng quy trình nhưng yếu về caliber vẫn chưa đạt chuẩn GocNhinPodcast.

## Reminder
Approval gates, financial safety, taxonomy, workflow order, và editorial quality cùng phối hợp cưỡng chế chất lượng đầu ra.