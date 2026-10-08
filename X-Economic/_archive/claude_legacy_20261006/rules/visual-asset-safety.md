# visual-asset-safety

Áp dụng cho thumbnail, visual prompts, scene timing, và mọi output phục vụ tạo ảnh/video.

## Core rule
- Không gọi thẳng tên người nổi tiếng, lãnh đạo, hoặc nhân vật công chúng trong prompt tạo ảnh nếu không thật sự bắt buộc cho bước sản xuất.
- Khi có thể, dùng mô tả vai trò, bối cảnh, hoặc đặc điểm nhận diện an toàn thay cho tên riêng.

## Why
- Giảm rủi ro filter của các công cụ tạo ảnh/video.
- Giữ prompt linh hoạt hơn giữa các engine.
- Tránh biến visual prompt thành prompt công kích, tuyên truyền, hoặc lệch khỏi lane kinh tế của episode.

## How to apply
- Nếu dùng ảnh gốc của một nhân vật công chúng, mô tả theo kiểu: `the provided real oath-taking photo of a senior Vietnamese leader` thay vì gọi thẳng tên trong prompt.
- Nếu không dùng ảnh gốc, chuyển sang mô tả chức năng/vai trò như: `a senior state leader`, `a calculating corporate titan`, `a young tech founder`, `a veteran macro strategist`.
- Chỉ giữ tên riêng ở layer file management, notes nội bộ, hoặc metadata ngoài prompt nếu thật sự cần.

## Must not do
- Không biến prompt ảnh thành danh sách tên thật.
- Không lạm dụng tên riêng để bù cho việc thiếu mô tả bối cảnh, mood, hay visual tension.
- Không để việc gọi tên kéo visual sang lane chính trị công kích khi video đang ở lane kinh tế.
- TUYỆT ĐỐI CẤM sử dụng code, thuật toán tự động hoặc script ghép nối từ khóa để sinh prompt tự động. Việc chuyển thể từ kịch bản sang prompt video bắt buộc phải được thực hiện bằng suy luận nghệ thuật của mô hình AI (LLM) để đảm bảo chất lượng chuyển thể hoàn hảo nhất.
