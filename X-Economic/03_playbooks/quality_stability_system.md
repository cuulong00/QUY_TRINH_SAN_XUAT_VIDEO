# quality_stability_system.md

Muốn chất lượng ổn định, bạn phải tối ưu hệ thống chứ không tối ưu một prompt đơn lẻ.

## 1. Single source of truth
Mọi quyết định quan trọng phải được ghi vào file, không để tồn tại chỉ trong chat.

## 2. State over memory
Agent có thể quên. File state không quên.

## 3. One phase at a time
Viết sai thường đến từ việc model bị yêu cầu làm quá nhiều thứ cùng lúc.

## 4. Review gates
Chỉ chuyển pha khi đạt tiêu chí qua pha.

## 5. Encode learnings
Mỗi khi phát hiện lỗi lặp, lỗi tone, lỗi financial safety, lỗi retention, phải thêm vào `lessons_learned.md` hoặc cập nhật file lõi.

## 6. Reuse strong patterns
Hook tốt, transition tốt, case study hay, ending tốt phải được chuẩn hóa vào core files.

## 7. Human approval points
Bạn nên duyệt tay ở 6 điểm:
- duyệt topic qualification
- duyệt brief
- duyệt hook
- duyệt thesis + retention map + outline
- duyệt final voiceover
- duyệt financial QA + oral QA trước production

## 8. Quality gates phải tách riêng
Ít nhất phải có các gate sau:
- research sufficiency gate
- structure gate
- financial QA gate
- oral QA gate
- production handoff gate

## 9. Stability loop
Sau mỗi video:
- xem lại bình luận và retention
- ghi 3 điều hiệu quả
- ghi 3 điều yếu
- cập nhật core files nếu có pattern mới
- cập nhật `postmortem.md`, `episode_registry.csv`, `lessons_learned.md`

## 10. Nguyên tắc vận hành cuối
- No prose before proof.
- No hook without pain.
- No title without thesis alignment.
- No long-form without retention design.
- No finance virality without safety.
- No phase skipping.
