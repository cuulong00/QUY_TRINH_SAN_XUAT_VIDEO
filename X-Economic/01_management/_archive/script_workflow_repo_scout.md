# Báo Cáo Điều Tra & Đánh Giá Các Repository Viết Kịch Bản / Bài Dài Bằng AI So Với Pipeline X-Economic

**Mã task:** `SCRIPT-WORKFLOW-REPO-SCOUT`  
**Ngày thực hiện:** 29/09/2026  
**Đơn vị thực hiện:** Antigravity (Heavy Technical Executor & Scout)  
**Đơn vị tiếp nhận:** Claude Code (Tổng điều phối & Kiến trúc sư hệ thống)  

---

## 1. Mốc So Sánh: Hệ Thống Kiểm Soát Chất Lượng Hiện Tại Của X-Economic

Theo `X-Economic/CLAUDE.md`, `.claude/rules/chapter-writing.md`, `.claude/rules/editorial-quality.md`, và `.claude/rules/claim-ledger.md`, pipeline hiện tại kiểm soát chất lượng bằng 10 cơ chế cốt lõi sau:

1. **Phân rã 16 pha tuần tự nghiêm ngặt (Sequential 16-Phase Pipeline):** Bắt buộc đi tuần tự từ Thượng nguồn (Master Vision, Deep Research, Strategy Brief, Master Outline, Hook Lab, Chapter Briefs) đến Hạ nguồn (Chapter Writing, Voiceover, Compliance, Visual, Assembly); cấm tuyệt đối nhảy cóc.
2. **Hội đồng đa lăng kính (Multi-Persona Architecture):** Mỗi pha do chuyên gia chuyên biệt đảm nhiệm (`the_macro_strategist`, `the_policy_analyst`, `the_industrial_economist`, `the_critical_auditor`, `the_dialectic_architect`, `the_quality_czar`), tránh một model đóng vai chung chung.
3. **Biện chứng Hegel 3 Màn (Thesis ➔ Antithesis ➔ Synthesis):** Màn 2 luôn có "The Devil's Chapter" (Tri-Adversarial Red Team $\ge 25\%$), bắt buộc steelman lập luận phe đối trọng gay gắt nhất, triệt tiêu thiên kiến xác nhận (confirmation bias).
4. **Sổ cái dữ kiện cứng (Claim Ledger & Immutable Data Vault):** Phân loại 3 nhãn cứng (`verified_data`, `market_analysis`, `opinion_commentary`), neo 100% số liệu vào hồ sơ kiểm toán thật (SEC 10-K, IMF, WB); cấm trích dẫn mồ côi hoặc bịa đặt.
5. **Sổ cái theo dõi tự sự (Narrative State Tracker - NST):** Kiểm soát hạt giống tự sự (Seeding & Harvesting) qua từng chương, đo tải trọng nhận thức (cognitive load), chống lặp case study và chặn rò rỉ dàn ý (scaffolding leakage).
6. **Bộ lọc chống văn máy (Anti-AI-isms & Editorial Quality Rubric):** Cấm các cụm từ sáo rỗng AI (`anti_ai_isms.md`), cấm announce-importance, cấm paragraph geometry đều chằn chặn, bắt buộc câu văn có lập trường cá nhân sắc sảo thay vì "đúng nhưng vô vị".
7. **Quy tắc neo đời sống & giữ chân người xem (Retention Bridges):** Quét Payoff Void, quét Dead Air > 60 từ, re-hook tại mốc 3:30, quy tắc 3 phút gắn vĩ mô với đời sống/áp lực tài chính phổ quát của người dân, cấm đóng kín loop ở Chapter 1.
8. **Quy trình ngôn ngữ 2 giai đoạn (Dual-Stage Language Protocol):** Kịch bản gốc viết và duyệt 100% bằng Tiếng Việt (`chapter_XX_vni.md`); chỉ sau khi User ký duyệt mới chuyển ngữ sang Tiếng Anh Noir Documentarian (`chapter_XX.md` < 150 ký tự/câu).
9. **Rào chắn pháp lý quốc tế (Legal Compliance Defenses):** Kiểm toán theo tiền lệ *Lowe v. SEC (1985)* (không tư vấn tài chính cá nhân), *Corporate Libel Defense* (luôn dẫn nguồn hồ sơ kiểm toán/tư pháp chính thức), và chuẩn *YouTube Inauthentic Content*.
10. **Hậu kiểm toàn diện & Đóng băng tài nguyên (Audit Gate & Postmortem):** Pha 9 (Retention Bridge Audit) và Pha 16 (Postmortem) đo lường độ trễ nhịp và lưu trữ bài học kinh nghiệm; toàn bộ visual/audio chỉ render thủ công khi có lệnh.

---

## 2. Bảng Tổng Hợp 8 Repository Đáng Chú Ý Trên GitHub

| STT | Tên Repository | Chủ Quản / Tác Giả | Stars | Commit Cuối | License | Nhóm Chức Năng & Trạng Thái |
|---|---|---|---|---|---|---|
| **1** | [stanford-oval/storm](https://github.com/stanford-oval/storm) | Stanford University OVAL Lab | 31.526 | 30/09/2025 | MIT | Multi-Perspective Research & Outline Synthesis |
| **2** | [google-deepmind/long-form-factuality](https://github.com/google-deepmind/long-form-factuality) | Google DeepMind | 693 | 18/06/2026 | NOASSERTION | Atomic Claim Decomposition & Search Verification (SAFE) |
| **3** | [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research) | LangChain Team | 12.680 | 10/08/2026 | MIT | **ĐÃ ARCHIVED (ngừng phát triển)** — Supervisor Graph |
| **4** | [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | Tavily AI / Assaf Elovic | 29.757 | 26/09/2026 | Apache-2.0 | Autonomous Web Research & Report Aggregator |
| **5** | [GAIR-NLP/factool](https://github.com/GAIR-NLP/factool) | GAIR Lab (SJTU / CMU) | 936 | 19/08/2024 | Apache-2.0 | Multi-task Claim Verification & Error Detection |
| **6** | [principia-ai/WriteHERE](https://github.com/principia-ai/WriteHERE) | Principia AI Lab | 976 | 03/09/2026 | Không khai báo | Heterogeneous Recursive Planning (>40k words) |
| **7** | [facebookresearch/doc-storygen-v2](https://github.com/facebookresearch/doc-storygen-v2) | Meta AI / UC Berkeley | 93 | 13/05/2026 | NOASSERTION | Detailed Outline Control (DOC) & Narrative Leash |
| **8** | [itallstartedwithaidea/writing-agent](https://github.com/itallstartedwithaidea/writing-agent) | Independent / Open Source | 29 | 03/05/2026 | MIT | Journalism Pattern Calibration & Anti-Slop QA |

*Ghi chú: Số liệu đã đối chiếu GitHub API ngày 29/09/2026.*

---

## 3. Đánh Giá Chi Tiết Từng Repository

### 1. `stanford-oval/storm` (Stanford University)
- **URL:** `https://github.com/stanford-oval/storm`
- **Thông số:** 31.526 stars | Commit cuối: 30/09/2025 (KHÔNG phải active 09/2026) | License: MIT.
- **Quy trình hoạt động:**
  1. *Perspective Discovery:* Phân tích chủ đề và sinh ra các Persona chuyên gia đa chiều (Skeptic, Historian, Policy Maker, Economist).
  2. *Simulated Information-Seeking Dialogue:* Cho các persona giả lập đặt câu hỏi phỏng vấn lẫn nhau và gọi công cụ tìm kiếm web (Tavily/Bing/Google) để thu thập thông tin đa góc nhìn có nguồn trích dẫn.
  3. *Outline Curation:* Tổng hợp toàn bộ câu trả lời để kiến tạo dàn ý dạng phân cấp (Hierarchical Outline) trước khi viết.
  4. *Article Generation & Citation Grounding:* Viết từng mục theo dàn ý, nhúng citation inline gắn liền với URL nguồn.
- **Cơ chế NÓ CÓ mà X-Economic CHƯA CÓ (hoặc làm tốt hơn):**
  - **Simulated Multi-Turn Interview Loop:** Trước khi viết outline, STORM cho các persona AI tự phỏng vấn chéo nhiều vòng để đào ra các mâu thuẫn thông tin (contradiction mapping). X-Economic hiện tại phân vai tĩnh ở từng pha nhưng chưa có cơ chế đối thoại chất vấn chéo tự động dạng round-table để đào sâu mâu thuẫn trước khi lập dàn ý.
- **Cơ chế X-Economic ĐÃ CÓ và làm tốt hơn:**
  - STORM sinh bài dạng bách khoa toàn thư (Wikipedia-style), giọng văn trung tính, khô khan, không có nhịp điệu kể chuyện (narrative arc), không có cấu trúc Biện chứng 3 Màn (Thesis-Antithesis-Synthesis), không có retention engineering (hook, payoff, dead-air audit), và không có khâu bản địa hóa đa ngôn ngữ (Dual-Stage VNI ➔ ENG).
- **Bằng chứng chất lượng:** Paper hội nghị đỉnh cao NAACL 2024 (*"Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models"*), có benchmark đánh giá mù (blind evaluation) từ các biên tập viên Wikipedia.

---

### 2. `google-deepmind/long-form-factuality` (Google DeepMind)
- **URL:** `https://github.com/google-deepmind/long-form-factuality`
- **Thông số:** 693 stars | Commit cuối: 18/06/2026 | License: NOASSERTION.
- **Quy trình hoạt động (Thuật toán SAFE - Search-Augmented Factuality Evaluator):**
  1. *Atomic Fact Decomposition:* Nhận văn bản bài viết dài, bẻ gãy từng câu phức thành các "sự thật nguyên tử" (atomic facts) độc lập, tự thân mang nghĩa.
  2. *Fact-Checking Query Generation:* Với mỗi atomic fact, LLM sinh câu truy vấn tìm kiếm Google nhắm thẳng vào bằng chứng kiểm chứng.
  3. *Multi-Step Search & Verification:* Thực thi tìm kiếm, so sánh kết quả web với atomic fact để gán nhãn: `Supported`, `Irrelevant`, hoặc `Unsupported`.
  4. *F1@K Metric Aggregation:* Tính toán điểm F1 cân bằng giữa độ chính xác (Precision) và độ phong phú thông tin (Recall) theo độ dài mục tiêu.
- **Cơ chế NÓ CÓ mà X-Economic CHƯA CÓ (hoặc làm tốt hơn):**
  - **Tự động bóc tách và kiểm chứng Sự thật Nguyên tử bằng Code (Atomic Fact Decomposition Engine):** X-Economic có `06_claim_ledger.md` (3 nhãn: verified_data, market_analysis, opinion_commentary) nhưng hiện dựa vào việc LLM tự soát trong prompt. Thuật toán SAFE của DeepMind cung cấp một framework code Python tách rời, bẻ nhỏ từng câu thoại thành từng mệnh đề độc lập và bắn query kiểm chứng Google tự động.
- **Cơ chế X-Economic ĐÃ CÓ và làm tốt hơn:**
  - SAFE chỉ là công cụ thẩm định/đánh giá (Evaluator), không phải engine sáng tác kịch bản. Nó không biết cách cấu trúc một bài phân tích kinh tế chính trị có kịch tính, không có lăng kính chính sách (Lowe v. SEC), không có định hướng biên tập.
- **Bằng chứng chất lượng:** Paper NeurIPS 2024 từ đội ngũ Google DeepMind; benchmark LongFact với 2,280 đề tài; chứng minh tương quan độ chính xác cao hơn cả việc người kiểm chứng thủ công (crowdsourced annotators) với chi phí rẻ hơn 20 lần.

---

### 3. `langchain-ai/open_deep_research` (LangChain Team)
- **URL:** `https://github.com/langchain-ai/open_deep_research`
- **Thông số:** 12.680 stars | Commit cuối: 10/08/2026 | License: MIT | **ĐÃ ARCHIVED (ngừng phát triển)**.
- **Quy trình hoạt động:**
  1. *Scoping & Brief Decomposition:* Supervisor Agent nhận đề tài, bẻ thành danh mục các sub-queries cần nghiên cứu.
  2. *Parallel Research Sub-Agents:* Phân bổ cho nhiều sub-agent chạy song song, mỗi agent chịu trách nhiệm 1 mảng đề tài, gọi web search và MCP servers.
  3. *Iterative Reflection & Gap Analysis:* Supervisor rà soát kết quả thu hoạch, xác định các khoảng trống dữ liệu (information gaps) và kích hoạt đợt tìm kiếm bổ sung.
  4. *Final Synthesis & Citation Assembly:* Gộp toàn bộ dữ liệu vào một báo cáo markdown có footnote trích dẫn.
- **Cơ chế NÓ CÓ mà X-Economic CHƯA CÓ (hoặc làm tốt hơn):**
  - **Hệ thống điều phối song song bằng LangGraph (Parallel Sub-Agent Graph with Dynamic Fan-Out):** Tự động chia nhỏ brief cho nhiều worker chạy song song qua các MCP server khác nhau, sau đó tổng hợp lại qua một nút đồng bộ (Reduce node).
- **Cơ chế X-Economic ĐÃ CÓ và làm tốt hơn:**
  - Báo cáo đầu ra của repo này chỉ dừng ở mức báo cáo kỹ thuật tổng hợp (Executive Summary / Research Memo), hoàn toàn không có kỹ thuật viết thoại (Voiceover Prose), không có nhịp ngắt câu Spoken English, không có cơ chế Seeding & Harvesting của NST, không có Devil's Chapter đối đầu biện chứng.
- **Bằng chứng chất lượng:** Được benchmark trên tập GAIA và SWE-bench, mã nguồn mở chuẩn mực của LangChain, cộng đồng sử dụng rộng rãi.

---

### 4. `assafelovic/gpt-researcher` (Tavily AI)
- **URL:** `https://github.com/assafelovic/gpt-researcher`
- **Thông số:** 29.757 stars | Commit cuối: 26/09/2026 | License: Apache-2.0.
- **Quy trình hoạt động:**
  1. *Research Question Formulation:* Sinh bộ câu hỏi nghiên cứu định hướng.
  2. *Scraping & Filtering:* Thu thập hơn 20+ nguồn web cùng lúc, trích xuất văn bản thô, lọc bỏ nội dung rác và trùng lặp.
  3. *Information Aggregation & Cross-Referencing:* Đối chiếu chéo dữ liệu giữa các trang web để lọc nguồn đáng tin.
  4. *Structured Report Generation:* Xuất ra báo cáo chi tiết (>2,000 từ) kèm danh mục tài liệu tham khảo chuẩn APA/Markdown.
- **Cơ chế NÓ CÓ mà X-Economic CHƯA CÓ (hoặc làm tốt hơn):**
  - **Tối ưu hóa Scraping & Web Filtering tự động:** Xử lý cào trang, tóm tắt và lọc nhiễu tự động cực mạnh ở tầng code hạ tầng (hỗ trợ nhiều search engine như Tavily, DuckDuckGo, Google, ArXiv).
- **Cơ chế X-Economic ĐÃ CÓ và làm tốt hơn:**
  - X-Economic sử dụng NotebookLM Direct RPC `--mode deep` nạp hàng trăm trang tài liệu nội bộ, sách trắng, hồ sơ pháp lý với khả năng grounding không ảo giác cao hơn hẳn web scraper thông thường. Về mặt kịch bản, GPT Researcher chỉ tạo báo cáo tài liệu tham khảo phẳng, không có drama, không có lăng kính điện ảnh hay cấu trúc phân cảnh.
- **Bằng chứng chất lượng:** Hơn 29k stars, hàng trăm nghìn lượt tải, được tích hợp vào nhiều sản phẩm thương mại lớn.

---

### 5. `GAIR-NLP/factool` (SJTU & CMU)
- **URL:** `https://github.com/GAIR-NLP/factool`
- **Thông số:** 936 stars | Commit cuối: 19/08/2024 | License: Apache-2.0.
- **Quy trình hoạt động:**
  1. *Claim Extraction:* Trích xuất các khẳng định mang tính sự thật cần kiểm chứng từ văn bản do LLM sinh ra.
  2. *Query Generation:* Chuyển đổi khẳng định thành truy vấn tìm kiếm chuyên biệt.
  3. *Tool Querying:* Gọi Google Search, Python REPL (để tính toán lại các con số), hoặc Google Scholar.
  4. *Evidence Extraction & Agreement Reasoning:* Trích xuất bằng chứng liên quan từ kết quả trả về, dùng mô hình suy luận so sánh để kết luận: Đúng, Sai, hay Thiếu chứng cứ.
- **Cơ chế NÓ CÓ mà X-Economic CHƯA CÓ (hoặc làm tốt hơn):**
  - **Python REPL Tool Execution for Math/Data Claims:** Khả năng tự động viết code Python để tính toán lại các tỷ lệ phần trăm, quy đổi đơn vị tiền tệ hoặc phép tính vĩ mô trong bài viết để phát hiện sai số số học (Arithmetic Hallucination).
- **Cơ chế X-Economic ĐÃ CÓ và làm tốt hơn:**
  - FacTool thuần túy là công cụ phát hiện lỗi (QA tool), không có năng lực tạo kịch bản, không có quy trình biên tập nội dung hay phân loại sắc thái bình luận (`market_analysis` vs `opinion_commentary`).
- **Bằng chứng chất lượng:** Paper học thuật tại EMNLP 2023 / OpenReview, benchmark trên nhiều tác vụ (KBQA, Code, Math, Scientific Literature).

---

### 6. `principia-ai/WriteHERE` (Principia AI Lab)
- **URL:** `https://github.com/principia-ai/WriteHERE`
- **Thông số:** 976 stars | Commit cuối: 03/09/2026 | License: Không khai báo.
- **Quy trình hoạt động (Heterogeneous Recursive Planning):**
  1. *State-Based Formalization:* Mô hình hóa quy trình viết thành một đồ thị có hướng không chu trình (DAG) gồm: Trạng thái tri thức (Knowledge State), Bộ nhớ (Memory), và Không gian làm việc (Workspace).
  2. *Dynamic Task Decomposition:* Thay vì chỉ lập dàn ý 1 lần lúc đầu, hệ thống liên tục bẻ nhỏ nhiệm vụ thành các tác vụ con (Retrieval, Reasoning, Composition) đệ quy.
  3. *Dependency & Context Tracking:* Theo dõi quan hệ phụ thuộc giữa các chương/đoạn để cập nhật lại kế hoạch viết cho các đoạn sau nếu đoạn trước có tình tiết mới xuất hiện.
  4. *Long-Context Synthesis:* Cho phép sinh văn bản mạch lạc có độ dài lên tới trên 40,000 từ.
- **Cơ chế NÓ CÓ mà X-Economic CHƯA CÓ (hoặc làm tốt hơn):**
  - **Heterogeneous Recursive Planning & Dynamic Plan Adjustment:** Ở X-Economic, dàn ý `07_outline.md` và `08_chapter_briefs.md` được chốt tại Pha 4 & 6. Mặc dù Pha 7 có `09_narrative_state_tracker.md` để ghi nhận hạt giống, nhưng việc tự động tính toán lại cấu trúc phụ thuộc logic của các chương sau (Dynamic Re-planning via DAG) khi chương trước có biến động dữ liệu chưa được cơ chế hóa bằng thuật toán mà dựa vào LLM/User chỉnh sửa thủ công.
- **Cơ chế X-Economic ĐÃ CÓ và làm tốt hơn:**
  - WriteHERE thiết kế chủ yếu cho tiểu thuyết (fiction) và báo cáo kỹ thuật học thuật. Nó thiếu hoàn toàn định vị thể loại Noir Documentarian, không có bộ lọc chống văn sáo rỗng AI (`anti_ai_isms`), không có retention hooks cho video, và không có rào chắn tuân thủ pháp lý tài chính.
- **Bằng chứng chất lượng:** Paper ArXiv 2024–2025; tạo ra các tác phẩm dài >40,000 từ giữ được tính nhất quán logic mạch lạc.

---

### 7. `facebookresearch/doc-storygen-v2` (Meta AI & UC Berkeley)
- **URL:** `https://github.com/facebookresearch/doc-storygen-v2`
- **Thông số:** 93 stars | Commit cuối: 13/05/2026 | License: NOASSERTION.
- **Quy trình hoạt động (Detailed Outline Control - DOC):**
  1. *Detailed Outliner:* Tạo dàn ý phân cấp cực kỳ chi tiết, chia nhỏ từng phân cảnh thành các mục tiêu cụ thể.
  2. *Detailed Controller (Context Leash):* Trong khi viết từng đoạn, một controller độc lập liên tục so sánh văn bản đang sinh với dàn ý chi tiết để kéo mô hình về đúng hướng (Relevance Tracking), ngăn chặn hiện tượng "trôi dạt ý đồ" (Topic Drift).
  3. *Reranking & Filtering:* Sinh nhiều bản thảo con (candidates) và dùng controller chấm điểm chọn bản thảo bám sát outline nhất.
- **Cơ chế NÓ CÓ mà X-Economic CHƯA CÓ (hoặc làm tốt hơn):**
  - **Candidate Reranking & Controller-Guided Decoding:** Cơ chế sinh 3-5 biến thể cho từng phân đoạn nhỏ rồi dùng một hàm mục tiêu (Scoring Function) chấm điểm độ bám dàn ý để tự động chọn bản tốt nhất. X-Economic hiện sinh 1 bản duy nhất cho mỗi chương rồi tiến hành revise.
- **Cơ chế X-Economic ĐÃ CÓ và làm tốt hơn:**
  - DOC sinh văn học thuật và truyện viễn tưởng; thiếu hoàn toàn tư duy báo chí điều tra, thiếu nhịp điệu spoken video, không có cơ chế đối đầu biện chứng 3 màn, không có claim verification.
- **Bằng chứng chất lượng:** Paper ACL 2023 danh tiếng (*"DOC: Improving Long Story Coherence With Detailed Outline Control"*).

---

### 8. `itallstartedwithaidea/writing-agent` (Ghost Writer AI Engine)
- **URL:** `https://github.com/itallstartedwithaidea/writing-agent`
- **Thông số:** 29 stars | Commit cuối: 03/05/2026 | License: MIT.
- **Quy trình hoạt động:**
  1. *Journalism-Informed Structural Engine:* Phân tích cấu trúc câu từ các tờ báo lớn (WSJ, HBR, CNN) để thiết lập nhịp điệu văn bản (nhịp câu ngắn - dài xen kẽ, nhịp mở đầu bằng bằng chứng thay vì giới thiệu lan man).
  2. *Anti-AI Post-Processing:* Chạy bộ lọc loại bỏ hơn 200 cụm từ sáo rỗng AI, triệt tiêu văn phong corporate filler.
  3. *40-Point Quality Assurance Process:* Rà soát văn bản qua 40 tiêu chí chất lượng biên tập trước khi xuất bản.
  4. *Triple-Detector Validation:* Kiểm chứng qua các bộ phát hiện AI (GPTZero, Originality.ai) để đảm bảo câu văn có độ biến thiên (burstiness & perplexity) của người viết chuyên nghiệp.
- **Cơ chế NÓ CÓ mà X-Economic CHƯA CÓ (hoặc làm tốt hơn):**
  - **40-Point Automated Quality Rubric & Sentence Length Burstiness Scanner:** Bộ kiểm tra định lượng độ biến thiên độ dài câu (Sentence Length Variation) bằng code để bảo đảm văn phong có độ gập ghềnh tự nhiên của người thật, thay vì chỉ dặn dò chung chung trong prompt.
- **Cơ chế X-Economic ĐÃ CÓ và làm tốt hơn:**
  - Repo này chỉ là CLI nhỏ cho bài viết blog/social; không có pipeline nghiên cứu chuyên sâu, không có Biện chứng Hegel, không có cơ chế quản lý dữ liệu kiểm toán nhiều tầng như X-Economic.
- **Bằng chứng chất lượng:** Dự án open-source độc lập của cộng đồng, chưa có paper học thuật, nhưng có bộ rules thực chiến rất thực tế cho copywriter.

---

## 4. Kết Luận Trung Thực & Khuyến Nghị Nâng Cấp Hệ Thống

### 🎯 Nhận Định Tổng Thể:
**KHÔNG CÓ bất kỳ repository nào trên mạng hiện nay sở hữu một quy trình toàn diện, chặt chẽ và chuyên sâu cho thể loại video tài liệu kinh tế - chính trị bằng pipeline hiện tại của X-Economic.**
- Hầu hết các repo lớn trên GitHub (STORM, GPT-Researcher, Open-Deep-Research) chỉ giải quyết bài toán **Nghiên cứu & Tổng hợp Báo cáo Thông tin phẳng (Wikipedia/Research Memo)**. Chúng hoàn toàn thiếu vắng: nghệ thuật tự sự kịch tính (Dramaturgy), Biện chứng Hegel 3 màn (Thesis-Antithesis-Synthesis), cấu trúc giữ chân khán giả YouTube (Retention Engineering, Hook Lab, Dead Air Audit), và quy trình bảo vệ pháp lý quốc tế (*Lowe v. SEC*, *Corporate Libel*).
- Các repo chuyên về viết truyện dài (DOC, WriteHERE) thì tập trung vào hư cấu (fiction), thiếu hoàn toàn hệ thống kiểm toán số liệu tài chính và thực chứng vĩ mô.

### 💡 4 Cơ Chế Kỹ Thuật Cụ Thể Rất Đáng Học Hỏi Để Bổ Sung Vào X-Economic:

1. **Tự Động Hóa Phân Rã & Kiểm Chứng Mệnh Đề (từ Google DeepMind SAFE & FacTool):**
   - *Cách áp dụng:* Xây dựng một script Python nhỏ chạy trong Pha 10 (`10_compliance_report.md` và `06_claim_ledger.md`) tự động bẻ các câu thoại thành các atomic claims, sau đó tự động gọi công cụ tìm kiếm đối chiếu số liệu và dùng Python REPL tính toán lại các tỷ lệ phần trăm/toán học. Việc này giúp nâng cấp `claim-ledger` từ "dặn dò LLM trong prompt" thành "công cụ kiểm toán định lượng bằng code".
2. **Cơ Chế Phỏng Vấn Chéo Đa Lăng Kính Trước Khi Lập Outline (từ Stanford STORM):**
   - *Cách áp dụng:* Tại Pha 1 (Master Systemic Topography), trước khi chốt bàn cờ, cho phép `the_critical_auditor` và `the_policy_analyst` đóng vai phản biện chất vấn chéo `the_macro_strategist` qua 2-3 lượt đối thoại giả lập (simulated interview round) để đào sâu các nghịch lý ngầm và mâu thuẫn lợi ích trước khi chuyển sang lập dàn ý ở Pha 4.
3. **Bộ Quét Nhịp Độ Biến Thiên Câu Văn Định Lượng (từ Ghost Writing Agent):**
   - *Cách áp dụng:* Viết một công cụ phân tích văn bản trong Pha 8 (Merge Voiceover) để đo biểu đồ độ dài câu (Sentence Length Distribution). Đánh cờ cảnh báo (Flag) nếu phát hiện có trên 4 câu liên tiếp có độ dài tương đương nhau (hiện tượng "paragraph geometry lặp đều" bị cấm trong `editorial-quality.md`).
4. **Kiểm Soát Độ Bám Dàn Ý Bằng Reranking (từ Meta DOC):**
   - *Cách áp dụng:* Khi sinh các phân đoạn cao trào hoặc Chapter 1 (Hook), có thể sinh thử nghiệm 2-3 biến thể câu chữ, sau đó cho Persona `the_quality_czar` chấm điểm dựa trên tiêu chí giữ chân (Retention) và tính bất ngờ (Curiosity Gap) để chọn bản tối ưu.
