# operator-visibility

Áp dụng cho mọi pha trong workflow `episodes/**`.

## Mục tiêu
User phải nhìn được ở mỗi bước:
- đang ở pha nào,
- chuyên gia nào đang active,
- skill canonical nào đang chạy,
- input/output chính là gì,
- gate hiện đang ở trạng thái nào.

## Rule
Sau mỗi pha, hệ thống phải cập nhật 2 lớp hiển thị:

### 1. Repo-wide snapshot
Cập nhật `01_management/episode_registry.csv` với các trường hiển thị vận hành:
- `active_specialist`
- `canonical_skill`
- `current_input_files`
- `current_output_file`
- `gate_status`

### 2. Episode-level operator log
Append vào `episodes/[slug]/00_pipeline_operator_log.md` một block ngắn gồm:
- timestamp
- phase
- specialist
- canonical_skill
- inputs
- output
- gate_status
- note

## Quy tắc dữ liệu
- Không đổi tên hoặc xóa các cột cũ của registry.
- Chỉ append cột mới ở cuối header để giữ backward compatibility.
- `current_input_files` phải là chuỗi ngắn, phân cách bằng ` | `.
- `gate_status` chỉ dùng vocabulary ngắn, nhất quán: `in_progress`, `awaiting_user`, `approved`, `blocked`, `completed`.
- Log cấp episode phải append-only, không overwrite lịch sử cũ.

## Observability boundary
Visibility layer chỉ là lớp quan sát vận hành.
Nó được dùng để cho user thấy hệ thống đang ở đâu, không được dùng để áp cách viết nội dung.
Registry, gate_status, specialist, canonical_skill, input/output tracking không được phép rò vào prose như một dạng cấu trúc ngầm.

## Must not do
- Không biến operator log thành nơi chép lại toàn bộ nội dung pha.
- Không ghi log dài dòng như postmortem.
- Không dùng visibility layer để thay thế state files chính của từng pha.
- Không để nhu cầu “show progress” làm chapter, hook, outline, hoặc final voiceover nghe như đang tự báo cáo tiến độ.
