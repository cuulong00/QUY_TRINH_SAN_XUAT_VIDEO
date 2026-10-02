---
name: kb-ingest
description: "Nạp vào kb_main từ research vault NotebookLM của một tập (Pha 2b) hoặc một đợt vault: kế hoạch → NotebookLM Direct RPC → gói đọc → điền JSON → cổng kiểm → nạp. KHÔNG dùng cho cập nhật kho thường xuyên theo thực thể — việc đó theo skill kb_entity_update."
---

# KB Ingest — Nạp tri thức từ research vault vào kho dùng chung

> **Phạm vi (30/09/2026):** skill này chỉ cho đường vault NotebookLM (Pha 2b của một tập, hoặc một đợt vault). Cập nhật kho thường xuyên theo thực thể, lấy từ web, dùng `.agents/skills/kb_entity_update/SKILL.md`. Rà và sửa lỗi kho dùng `.agents/skills/kb_auditor/SKILL.md`. Nguyên tắc chung cho mọi đường nạp: đúng trước đủ sau, không có gì bắt buộc phải tìm ra, đã tìm mà không có thì ghi lại.

> 🛑 **CHUYÊN GIA (BẮT BUỘC HÓA THÂN)**
> - Dẫn dắt mọi bước: `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/personas/the_knowledge_curator.md` (chọn cái cần nạp, đặt câu hỏi, gán chủ thể, xét quan hệ, giữ danh mục).
> - Viết câu hỏi theo lớp: thế giới, khối, quốc gia (W/K/Q) → `the_macro_strategist.md`; chính sách, văn bản pháp luật (P) → `the_policy_analyst.md`; ngành, thị trường (N/T) → `the_industrial_economist.md`; tài chính doanh nghiệp, đánh giá tín nhiệm, quan hệ vốn (D6, D10, OWNS, LENDS_TO) → `the_capital_markets_analyst.md`.
> - Soát mẫu trước khi nạp (bước 5): `the_data_auditor.md`.
> - Agent điền JSON (bước 4) làm theo hướng dẫn đầu `part_01.md` của gói; đó là bản rút gọn kỷ luật của `the_knowledge_curator`, không cần đọc thêm persona.

Kho `kb_main` (FalkorDB) lưu **dữ kiện kiểm chứng được** (con số, sự kiện có thời điểm, văn bản pháp lý, quan hệ sở hữu/cung ứng/cho vay/quản lý), mỗi dữ kiện có câu nguồn và URL. Không lưu nhận định. Script ở `/Users/pro16/Documents/VideoProject/GocNhinPodcast/scripts/`.

## Phân vai
| Việc | Ai |
|---|---|
| Chọn thực thể, mã thuộc tính, viết kế hoạch (bước 0–1) | Claude |
| Chạy nghiên cứu, dựng gói, điền JSON, `--check` (bước 2–4) | Antigravity |
| Soát mẫu, thêm thực thể mới vào danh mục, hỏi user, nạp thật (bước 5) | Claude + user |

## Bước 0 — Chọn cái cần nạp (không đoán)
- **Đi từ trên xuống:** thế giới → khối/khu vực → quốc gia → ngành, thị trường → doanh nghiệp. Lớp dưới chỉ mở khi lớp trên đã đủ ở mức cơ bản. Mỗi đợt hẹp, không lan rộng.
- **Chọn theo dữ liệu:** số tập hai kênh đã làm về thực thể (bộ nhớ tập, cạnh `COVERS`) so với số dữ kiện và quan hệ kho đang có; ma trận phủ theo mã thuộc tính (`scripts/kbaudit`, hoặc đếm theo `o.attribute`). Nói nhiều mà kho mỏng thì làm trước.
- **Không thêm thực thể suy đoán** (chưa có tập nào cần) vào danh mục. Thực thể mới chỉ thêm khi đợt trích xuất cho thấy nó quan trọng (nằm trong `unmapped`).
- Tên chính sách, văn bản, khẩu hiệu: xác minh là có thật và tìm tên văn bản chính thức trước khi đưa vào câu hỏi (ví dụ "hóa rồng" → Chiến lược phát triển KT-XH 2021–2030, tầm nhìn 2045). Không để agent đi tìm một văn bản mang tên tự đặt.

## Bước 1 — Kế hoạch: `01_management/kg_research/kb_plans/<đợt>.json`
```json
{"batch": "kb-<tên-đợt>", "notebook_title": "KB — ...",
 "sources": [{"id": "S1", "gaps": ["D8"], "query": "câu tìm nguồn tiếng Anh"}],
 "extractions": [{"file": "01_<thuc_the>_<nhom>.md", "entity": "<object_id>", "codes": ["D8"], "gaps": ["D8"], "prompt": "câu hỏi trích xuất"}]}
```
- **Câu nạp nguồn** (deep research): tiếng Anh; một thực thể × một nhóm thuộc tính; có mốc năm; nêu loại nguồn muốn có (báo cáo thường niên, công bố thông tin, IMF/WB/GSO, văn bản pháp luật). Luôn có ít nhất một câu nhắm phản biện, số liệu đối lập khi đợt có luận điểm gây tranh cãi.
- **Câu trích xuất**: một thực thể × 1–3 mã nhóm; liệt kê cụ thể các chỉ số, sự kiện cần lấy; hỏi đối tác, quan hệ nếu có; yêu cầu mốc thời gian. **Không ép khuôn trả lời** (bảng N cột cố định, mục tách riêng): khuôn ép làm thư viện notebooklm-py trả về rỗng (đã kiểm 30/09/2026). Script tự nối một dặn nhẹ: chi tiết, có số, có mốc, giữ chú thích [n].
- Tạo sẵn `01_management/kg_research/file_fill/packs/gnp__<đợt>/priority.json` = các object_id trọng tâm của đợt. Thiếu file này, gói chỉ đánh dấu ◆ cho danh sách mặc định (đã từng chỉ còn 13 câu thay vì 478).

## Bước 2 — Nghiên cứu (Antigravity)
`/Users/pro16/Documents/VideoProject/GocNhinPodcast/.venv_notebooklm/bin/python scripts/kg_registry/kb_research_run.py 01_management/kg_research/kb_plans/<đợt>.json`
- Chỉ dùng NotebookLM **Direct RPC** qua script này. Không dùng lệnh CLI `notebooklm`.
- Chạy lại được khi dở (`episodes/<đợt>/run_state.json`). Log cuối phải là "XONG. Nguồn chưa nạp: không · File chưa trích: không".
- Câu trả lời rỗng hoặc timeout: chạy lại đúng lệnh. Lặp lại lỗi trên cùng một câu thì báo Claude (thường phải tách câu hỏi hẹp hơn), không tự đổi cách.
- Vault ra `episodes/<đợt>/research_vault/`, có "Bảng số trích dẫn" `[n] tiêu đề URL`; câu hỏi lưu ở `.meta.json`, không nằm trong vault.

## Bước 3 — Gói đọc (Antigravity)
`python3 scripts/kg_registry/annotate_vault.py` → `index_vaults.py` → `load_file.py --orders` → `make_packs.py gnp__<đợt>`. Các script này quét chung mọi tập; gặp lỗi đọc JSON vì agent khác đang chạy cùng lúc thì chờ một phút chạy lại.

## Bước 4 — Điền JSON (Antigravity)
Theo đúng hướng dẫn đầu `part_01.md` của gói: đọc bằng view_file, xét từng câu ◆, ghi `file_fill/gnp__<đợt>__p01.json`… theo từng phần, `load_file.py --check` tới khi "KẾT QUẢ: ĐẠT". Không dùng lệnh hay script để lọc câu; file JSON ghi và sửa bằng write_to_file / replace_file_content, không bằng lệnh; loader kiểm nhật ký làm việc và từ chối cả tập nếu vi phạm. Không nạp thật.
- **Bên tham gia (từ 30/09/2026):** mỗi dữ kiện có đúng một chủ thể (`object_id`), cộng trường `participants` liệt kê mọi thực thể khác trong danh mục có mặt trong dữ kiện, kèm vai trò (`ben_giao_dich`, `quan_ly`, `so_huu`, `so_sanh`, `dia_ban`, `nhac_toi`). Loader ghi cạnh `INVOLVES` để dữ kiện tra được từ mọi bên. Tổ chức, quốc gia, dự án có tên riêng và địa danh trong `places` của danh mục được loader tự nhận; ngành và thị trường phải ghi tay (tên chung, không tự nhận được).
- Lý do: trước đây dữ kiện chỉ treo vào chủ thể, nên "VinFast bán 72% xe cho GSM" không tra được từ GSM; bài thử vault-vs-kho 30/09 cho thấy tập dùng kho bỏ sót toàn bộ bằng chứng then chốt vì thế.

### `kb_extract.py` — công cụ phụ, KHÔNG phải mặc định (thử 29-30/09/2026, dừng lại)
`scripts/kg_registry/kb_extract.py` gọi Gemini API (`gemini-3.8-flash`) làm thay bước điền JSON, tái dùng `load_file.py`'s `check()`. Kết quả kỹ thuật tốt (nhanh, rẻ, hội tụ) nhưng **quota bản miễn phí chỉ 20 request/ngày/khóa/model** (`GenerateRequestsPerDayPerProjectPerModel-FreeTier`) — không đủ chạy một đợt trọn vẹn, cả 2 khóa hết quota giữa chừng ngày 30/09/2026. User quyết định quay lại Antigravity làm chuẩn. Chỉ dùng script này khi: đã bật billing cho khóa API (bỏ giới hạn 20/ngày), hoặc Claude tự thử một file lẻ tẻ còn quota — không giao làm mặc định cho một đợt đầy đủ.

## Bước 5 — Soát, nạp tự động (Claude; chốt 30/09/2026: không cần hỏi user mỗi đợt)
1. Soát mẫu: 5–10 dữ kiện đối chiếu câu nguồn (idx.json); xem `unmapped`, thêm thực thể quan trọng vào `entity_registry.json` rồi `apply_registry.py --dry-run` → `apply_registry.py`. Thêm thực thể mới hoặc thêm địa danh vào `places` thì chạy `backfill_involves.py` (thử khô, soát mẫu, rồi `--apply`) để dữ kiện cũ nối tới nó.
2. Nạp ngay: `~/.local/bin/uv run --with falkordb python scripts/kg_registry/load_file.py <các file JSON>` (MERGE, không xóa gì trong kho). Cổng nhật ký từ chối vì lý do đã tự đối chiếu tay sạch (cửa sổ theo dõi hết hạn, hoặc vi phạm cũ đã soát) → dùng `--reviewed "<ghi chú>"`.
3. Chạy lại `kbaudit` để xác nhận chỗ trống đã đóng. Xem trực quan: FalkorDB Browser `http://localhost:3000` (đọc trực tiếp kho, không cần xuất lại).
4. Chỉ hỏi user khi: thực thể mới không rõ có tập nào cần, dữ liệu chạm ranh giới tài chính/pháp lý, hoặc soát mẫu phát hiện sai lệch/bịa. Nêu lý do cụ thể, không hỏi "có nạp không" chung chung.

## Cấm
- Lệnh CLI `notebooklm`; script tự trích câu; tự đặt object_id trong đường vault (thực thể mới đi qua `unmapped`); lệnh xóa hàng loạt trong kho. (Nạp thật: theo bước 5, Claude tự nạp sau khi soát mẫu; chỉ hỏi user trong các trường hợp nêu ở bước 5.)
- Ghi nhận định, dự báo không nêu tổ chức dự báo, hay năm tự suy vào dữ kiện (loader tự bỏ năm không có trong câu nguồn).
