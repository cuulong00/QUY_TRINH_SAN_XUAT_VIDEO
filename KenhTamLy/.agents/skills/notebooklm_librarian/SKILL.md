---
name: notebooklm-librarian
description: "Community-standard NotebookLM MCP Agent Skill. The central research hub and knowledge synthesizer. MUST BE USED to search, store, and extract deep insights from NotebookLM."
---

# NotebookLM Librarian — Quản Gia Tri Thức (Central Knowledge Hub)

> 🛑 **MANDATORY INSTRUCTION (LƯU Ý CỐT LÕI):**
> NotebookLM không chỉ là công cụ đọc báo cáo tĩnh. Nó là **Trái Tim Dữ Liệu (Central Research Hub)** của tập video.
> Bất cứ khi nào bạn (Agent) cần nghiên cứu chuyên sâu, hãy dừng việc cào dữ liệu lắt nhắt về máy. Thay vào đó, hãy **ném mọi URL/tài liệu vào NotebookLM**, và để nó tổng hợp (Synthesize) giúp bạn.

## Quy tắc 0: 1 VIDEO = 1 MASTER NOTEBOOK DUY NHẤT (Tuyệt đối tuân thủ)
- **CẤM:** Tuyệt đối không dùng lệnh tạo Notebook mới cho mỗi lần truy vấn. Sự phân mảnh làm hỏng hoàn toàn khả năng xâu chuỗi dữ liệu vĩ mô.
- **BẮT BUỘC:** Mỗi video chỉ có MỘT (01) Master Notebook. Khi chạy `mcp_notebooklm-mcp_ask_question`, `deep_research`, hay `add_source`, BẮT BUỘC phải truyền cố định tham số `notebook_url` của Master Notebook đó. Mọi thứ phải được nhồi chung vào một "nồi lẩu" duy nhất.

### Cross-Session Persistence (BẮT BUỘC)
Notebook URL phải tồn tại vĩnh viễn trên đĩa, KHÔNG PHỤ THUỘC vào memory của chat session:
1. **GHI:** Ngay khi tạo hoặc xác định notebook cho episode → ghi URL vào `episodes/[slug]/.notebook_url`
2. **ĐỌC:** Trước MỌI lần gọi `deep_research`, `ask_question`, `add_source`, `batch_to_vault` → đọc file `.notebook_url` để lấy URL
3. **TRUYỀN:** Luôn truyền `notebook_url` parameter. KHÔNG BAO GIỜ dựa vào fallback/active notebook
4. **KIỂM TRA:** Nếu file `.notebook_url` không tồn tại → DỪNG và hỏi user

## Quy tắc 1: Vòng lặp "Bơm Tri Thức" (The Knowledge-Injection Loop)
Khi được yêu cầu đào sâu một chủ đề (hoặc khi tìm thấy lổ hổng dữ liệu):
1. **Search (Tìm kiếm):** Dùng `search_web` tìm các báo cáo, tài liệu uy tín nhất.
2. **Inject (Bơm vào):** Lập tức dùng lệnh `mcp_notebooklm-mcp_add_source` để nạp các URL đó thẳng vào Notebook của tập hiện tại.
3. **Query (Truy vấn):** Dùng lệnh `mcp_notebooklm-mcp_ask_question` để yêu cầu NotebookLM tổng hợp thông tin từ nguồn vừa nạp kết hợp với dữ liệu cũ.

## Quy tắc 2: Định dạng Trích xuất (Strict Grounding Rules)
- **CẤM:** Không bao giờ hỏi NotebookLM những câu chung chung như "Hãy tóm tắt tất cả". 
- **BẮT BUỘC:** Phải hỏi có tính định hướng (Ví dụ: "Hãy so sánh tỷ lệ... dựa trên báo cáo X và Y").
- **Citations:** BẮT BUỘC gọi `ask_question` kèm theo tham số `source_format: "json"` hoặc `"footnotes"`. Việc này bắt hệ thống phải trả về Mỏ neo trích dẫn (Citations), giúp chống ảo giác dữ liệu tuyệt đối.

## Quy tắc 3: Quản lý Phiên làm việc (Session Management)
- Giao thức MCP mở một trình duyệt ẩn để chat với NotebookLM (mất 10-15s tải trang).
- Để tiết kiệm thời gian, nếu bạn có nhiều câu hỏi nối tiếp nhau, **BẮT BUỘC phải dùng lại `session_id`** trả về từ câu hỏi trước đó.

## Quy tắc 4: An toàn Dữ liệu (Garbage In, Garbage Out)
- Chỉ nạp (`add_source`) các URL thuộc báo chí chính thống, báo cáo chính phủ (TCTK, World Bank) hoặc nghiên cứu học thuật. Tuyệt đối không nạp link blog, mxh rác vào NotebookLM làm bẩn Context.

## Quy tắc 5: Quy trình Tự động hóa Deep Research & Tổng hợp Dữ liệu (Deep Research & Extraction Pipeline)
Việc sử dụng tính năng Deep Research mới chỉ là bước tập hợp các nguồn tài liệu thô. Để biến nó thành dữ liệu phân tích cho video, BẮT BUỘC thực hiện quy trình sau:
1. **Khởi tạo thư mục Vault:** Tạo một thư mục lưu trữ tài liệu nghiên cứu riêng cho chủ đề (ví dụ: `episodes/[slug]/research_vault/`).
2. **Nghĩ ra bộ câu hỏi chiến lược:** Tự suy nghĩ và thiết kế bộ câu hỏi tổng hợp đa chiều, bao quát mọi góc cạnh thiết yếu của chủ đề video. **Lưu ý Cực Kỳ Quan Trọng:** 
   - BẮT BUỘC chèn thêm lệnh ép freshness VÀ format vào cuối MỖI câu hỏi: *"Ưu tiên dữ liệu mới nhất (2024-2026). Bỏ qua dữ liệu cũ trước 2023 trừ khi cần so sánh lịch sử. Trình bày dưới dạng báo cáo chuyên nghiệp: tiêu đề H2/H3, gạch đầu dòng, bảng biểu. TUYỆT ĐỐI KHÔNG trích xuất văn bản rác, nút share mạng xã hội, hoặc boilerplate website. Chỉ giữ phần lõi nội dung."*
   - Dữ liệu trả về không được luộm thuộm.
3. **Tổng hợp hàng loạt (Batch Extraction):** Yêu cầu NotebookLM phân tích các câu hỏi này dựa trên kho dữ liệu nó vừa tìm được (ưu tiên sử dụng tool `mcp_notebooklm-mcp_batch_to_vault` để lưu thẳng kết quả phân tích thành các file Markdown vào thư mục Vault đã tạo). Dữ liệu trả về sẽ làm nền tảng cốt lõi trước khi viết Brief hay Outline.

---
*Skill này được biên dịch và quy chuẩn dựa trên Best Practices của cộng đồng MCP (PleasePrompto/notebooklm-mcp) và hệ tiêu chuẩn agent prompts của Claude/Cursor.*
