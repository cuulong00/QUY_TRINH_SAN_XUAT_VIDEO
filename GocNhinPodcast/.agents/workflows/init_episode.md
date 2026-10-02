# /init_episode — Tạo thư mục tập (tệp trỏ)

Workflow tư duy của Pha 1 (bàn cờ, giả thuyết, bản đồ nền từ kho) nằm **duy nhất** ở `.agents/workflows/build_global_vision.md` (user chốt 02/10/2026, WO-00 Q9). File này chỉ còn việc tạo thư mục.

## Các bước
1. Hỏi episode slug nếu chưa có.
2. Nếu `episodes/[slug]` chưa tồn tại, copy `02_templates/episode_template/` vào `episodes/[slug]`; thay toàn bộ placeholder `__EPISODE_SLUG__` bằng slug thực.
3. Thêm dòng cho tập vào `01_management/episode_registry.csv` (bằng Edit/Write, không bằng Bash) và tạo `episodes/[slug]/00_pipeline_operator_log.md` theo `.agents/rules/operator-visibility.md`.
4. Chạy `/build_global_vision` để làm Pha 1. Không tạo `01_global_vision_synthesis.md` từ file này.
