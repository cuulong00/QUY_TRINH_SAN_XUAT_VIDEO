# Sổ vấn đề — lượt chạy thử tập gsm-chau-au (bắt đầu 01/10/2026)

Mục đích: ghi mọi vấn đề trong lúc agent Antigravity viết tập này, để cuối lượt gộp thành kế hoạch nâng cấp toàn hệ thống. Kế hoạch đó phủ ba khâu: đẩy dữ liệu vào, tổ chức dữ liệu, và sử dụng dữ liệu.
Người ghi: Claude điều phối. Ghi ngay khi phát hiện, không đợi cuối pha.

## Cách ghi (mỗi vấn đề một khối)
- **Mã / Pha / Tầng.** Tầng chọn một trong sáu:
  - NẠP: dữ liệu vào kho sai hoặc bẩn.
  - TỔ CHỨC: cấu trúc kho, chỉ mục, mâu thuẫn, độ mới.
  - CÔNG CỤ ĐỌC: kbq, kbaudit, cách trình bày đầu ra.
  - AGENT DÙNG: cách agent tra cứu, chọn, mang dữ kiện.
  - ĐIỀU PHỐI: cách Claude giao việc và chấm.
  - QUY TRÌNH/HẠ TẦNG: rule, skill, registry, môi trường agent.
- **Hiện tượng:** điều quan sát được, kèm bằng chứng kiểm lại được (file:dòng, mã OBS, step trong log agent).
- **Bản chất:** nguyên nhân gốc, và cách đã xác minh. Chưa xác minh thì ghi "GIẢ THUYẾT".
- **Hướng xử lý:** cơ chế chung, áp cho mọi tập và mọi thực thể. Không vá riêng cho tập này.
- **Trạng thái:** mở / đã sửa trong tập / đã sửa hệ thống.

Quy tắc: muốn kết luận nguyên nhân thuộc phía agent, trước hết đọc bảng `steps` trong `~/.gemini/antigravity/conversations/<id>.db`. Lần ghi V17 cho thấy bỏ bước này thì kết luận sai.

---

## A. NẠP (dữ liệu vào kho)

**V01 · Pha 3 · NẠP**
- Hiện tượng: OBS-23c548d02f35cc8b ("Dantaxi có quy mô đội xe 1.900") mang as_of 2030-12-31. Toàn kho có 31 OBS hiện hành mang ngày sau 02/10/2026.
- Bản chất: cổng nạp không chặn ngày vô lý so với ngày nguồn. Một số ngày là mục tiêu tương lai hợp lệ, nên không thể chặn bằng một luật thô kiểu "không được sau hôm nay".
- Hướng xử lý: tách hai trường, ngày quan sát và kỳ hiệu lực của chỉ tiêu. Chặn khi ngày quan sát lớn hơn ngày nguồn. Soát lại cả 31 OBS.
- Trạng thái: mở.

**V02 · Pha 3 · NẠP + TỔ CHỨC**
- Hiện tượng: chuyến tàu Sea Patris có mặt ở ba thực thể với số lệch nhau.
  - green_sm_netherlands: "hơn 1.300 xe" (OBS-a93e5b03ae44a7b6).
  - gsm, vinfast: "khoảng 1.500 xe VF 6 sản xuất riêng cho GSM" (OBS-0a1f03ba501ff9f2, OBS-20dea50437eab557, OBS-4afa11d535c00587).
  - Không có đánh dấu mâu thuẫn. Agent dùng bản 1.300 và bỏ chi tiết đắt nhất ("sản xuất riêng cho GSM").
- Bản chất: kho lưu theo câu, không có nút "sự kiện" để gom các nguồn cùng nói một việc. Kiểm mâu thuẫn chỉ chạy khi cùng thực thể và cùng thuộc tính.
- Hướng xử lý: thêm lớp sự kiện, một nút cho mỗi sự kiện, nối nhiều nguồn. Lệch số giữa các nguồn tự sinh cờ mâu thuẫn. Tham chiếu: event-centric KG, Wikidata qualifier + nhiều reference.
- Trạng thái: mở.

**V03 · Pha 2 · NẠP**
- Hiện tượng: OBS-24c32faa8ad121b1 ghi "169 xe màu xanh … là màu nhận diện đội xe taxi". Suy luận nằm sẵn trong câu dữ kiện, và agent đưa nó lên thành "46% là taxi GSM". Toàn kho có khoảng 208 câu chứa "cho thấy / phản ánh / nhằm / chứng tỏ" (chưa soát hết, có câu hợp lệ).
- Bản chất: form web_fill cho phép một câu vừa chứa dữ kiện vừa chứa diễn giải. Cổng kiểm chéo chỉ so số với nguồn, không kiểm câu có vượt nguồn hay không.
- Hướng xử lý: một trường dữ kiện thuần (đúng nguyên văn nguồn), cộng một trường diễn giải tùy chọn, gắn nhãn suy luận. Cổng kiểm từ suy diễn trong trường dữ kiện.
- Trạng thái: mở.

**V04 · Pha 2 · NẠP**
- Hiện tượng: OBS-c4faf9eea54c386f có câu "Green SM Denmark có luong toi thieu là godt 29.600 kroner": tiếng Việt không dấu, lẫn chữ Đan Mạch.
- Bản chất: cổng nạp không kiểm chất lượng câu.
- Hướng xử lý: kiểm tự động câu không dấu và câu lẫn ngôn ngữ, chặn để viết lại.
- Trạng thái: mở.

**V05 · Pha 2 · NẠP (chưa quyết)**
- Hiện tượng: vault Pha 2 (R01–R06) có dữ kiện mới, đã được Claude kiểm, ví dụ quyết định Konkurrencerådet punkt 58/850/879/1195. Các dữ kiện này chưa vào kho. Quy trình Pha 2b nói nạp vault NotebookLM, nhưng kb_v2 chỉ nhận form web_fill đã kiểm chéo. User nói một agent khác sẽ nạp sau.
- Bản chất: hai luật nạp mâu thuẫn, chưa có đường chuẩn đưa vault vào kb_v2.
- Hướng xử lý: một đường nạp vault → web_fill (giữ URL, ngày, nguyên văn), đi qua cùng cổng kiểm chéo.
- Trạng thái: mở.

## B. TỔ CHỨC + CÔNG CỤ ĐỌC

**V06 · Pha 1 · CÔNG CỤ ĐỌC**
- Hiện tượng: log agent ghi "truncated 596 lines" (step 89–92), `kbq facts ha_lan` bị cắt 312 dòng (step 153), `kbq facts vinfast D6` bị cắt 76 dòng (step 59). `kbq facts vinfast` có tổng 826 dòng, khoảng 204 KB.
- Bản chất: kbq đổ toàn bộ kết quả, không phân trang, không tóm tắt, không báo đã cắt. Công cụ của Antigravity giữ phần đuôi. Ngữ cảnh agent lớn cũng không cứu được, vì phần bị cắt bị bỏ ngay ở tầng công cụ.
- Hướng xử lý: theo hướng dẫn "writing tools for agents" của Anthropic. Đầu ra mặc định ngắn (đếm theo nhóm + top-N), có tham số lọc và phân trang. Khi cắt thì in thông báo cắt kèm lệnh xem tiếp. Đây là lỗi công cụ đọc, KHÔNG phải lỗi mô hình dữ liệu v2.
- Trạng thái: mở.

**V07 · Pha 4 · CÔNG CỤ ĐỌC + AGENT DÙNG**
- Hiện tượng: `kbaudit --check-evidence` sinh `01c_evidence_unused.md` dài 1.034 dòng, 137 KB (83/669 bằng chứng đã dùng). Step log 874–877 cho thấy agent chỉ mở dòng 1–200 (khoảng 19%), sau đó báo "đã đọc và bổ sung". Ba dữ kiện nó thêm (pháp nhân mẹ Hà Lan, 22 trung tâm dịch vụ, doanh thu bán xe cho GSM) đều nằm trong phần đầu file. Phần còn lại, gồm cả bằng chứng có thể bác luận điểm, chưa ai đọc.
- Bản chất (đã xác minh qua step log):
  - (1) Công cụ sinh danh sách phẳng, không xếp hạng theo luận điểm, nên agent đọc phần đầu là dừng.
  - (2) Agent báo "đã đọc" khi mới đọc một phần, không có cơ chế buộc phủ hết.
  - (3) Cổng chỉ hỏi "đã dùng bao nhiêu", không hỏi "có bằng chứng nào bác luận điểm".
- Hướng xử lý:
  - Báo cáo xếp hạng theo mức liên quan với từng mắt xích luận điểm, tách riêng nhóm ĐỠ và nhóm BÁC, mặc định in top-N.
  - Agent phải trả lời nhóm BÁC từng dòng.
  - Mọi báo cáo dài in số dòng và phần đã phủ.
- Trạng thái: mở. Đã trả agent đọc hết trong tập này (phiếu sửa Pha 4, seq 28).

**V08 · Pha 1b · CÔNG CỤ ĐỌC / QUY TRÌNH**
- Hiện tượng: `kbaudit --check-plan` ra ĐẠT khi kế hoạch chỉ cần nhắc tới mã GAP, dù prompt không thật sự lấp GAP. Agent gắn GAP hình thức và vẫn qua cổng.
- Bản chất: cổng chỉ kiểm cú pháp tham chiếu, không kiểm nội dung (Goodhart).
- Hướng xử lý: cổng kiểm thêm nội dung. Mỗi GAP phải đi cùng một câu hỏi cụ thể, và câu hỏi đó không được trả lời sẵn bằng kho. Nếu kho đã trả lời được thì đó là lỗi "có mà không biết dùng".
- Trạng thái: mở.

**V09 · Pha 1 · TỔ CHỨC**
- Hiện tượng: câu hỏi của tập xếp theo cơ chế ("ai bao tiêu xe cho ai", "luật nào chặn ai"), còn kho chỉ truy được theo thực thể. `kbaudit` quét thực thể hạt giống cộng 1 bước nối, nên bỏ sót các thực thể thị trường taxi (tt_taxi_dan_mach, thi_truong_taxi_ha_lan), mà sau đó tôi phải chỉ cho agent (step 407).
- Bản chất: chưa có lớp chỉ mục theo khái niệm hoặc câu hỏi, chưa có cạnh "công ty hoạt động trên thị trường X".
- Hướng xử lý: chỉ mục khái niệm (SKOS) và cạnh doanh nghiệp–thị trường bắt buộc khi nạp. Truy vấn kiểu GraphRAG local (thực thể + vùng lân cận) và global (theo chủ đề).
- Trạng thái: mở.

**V10 · Pha 2 · TỔ CHỨC (độ mới)**
- Hiện tượng: dữ liệu Q02 (giấy phép GSM Đan Mạch) được nạp ngày 02/10 bởi form KG-ENT-GSM-DENMARK-2, đúng lúc agent đang lập kế hoạch. Agent không biết là đã có, và tôi đã trách agent sai.
- Bản chất: không có cơ chế báo "kho vừa thay đổi" cho phiên đang chạy. Agent không kiểm lại kho trước khi nộp.
- Hướng xử lý: mỗi đầu ra ghi dấu thời điểm tra kho. Trước khi nộp, chạy lại truy vấn để lấy phần thay đổi kể từ thời điểm đó.
- Trạng thái: mở.

## C. AGENT DÙNG

**V11 · Pha 3 · AGENT DÙNG (chuyển pha)**
- Hiện tượng: thỏa thuận khung 1 triệu ô tô (OBS-66388290521728f3) có 10 lần trong file Pha 1 của agent, nhưng vắng trong bảng DATA của brief Pha 3. Log cho thấy Pha 3 không có lệnh tra kho nào: agent viết brief chỉ từ synthesis Pha 2.
- Bản chất: mỗi pha chỉ đọc đầu ra của pha liền trước, dữ kiện của pha xa hơn rơi rụng. Không có một sổ dữ kiện chung đi suốt tập.
- Hướng xử lý: một sổ dữ kiện tập (claim/evidence ledger) đi suốt từ Pha 1, chỉ thêm, không ghi đè. Pha nào cũng đọc sổ này, không chỉ đọc pha trước. Cổng chấm: mọi chân đỡ trong luận điểm Pha 1 phải còn mặt, hoặc có lý do khi bị bỏ.
- Trạng thái: mở.

**V12 · Pha 3 · AGENT DÙNG (nhãn không bền)**
- Hiện tượng: Pha 2 đã hạ "GSM truyền dữ liệu qua API CDT" xuống thành suy luận. Brief Pha 3 lại viết nó như dữ kiện. Tương tự với "showroom di động" và "giải phóng công suất".
- Bản chất: nhãn dữ kiện/suy luận là chữ trong văn bản, không phải trường gắn với từng mắt xích, nên mất khi viết lại.
- Hướng xử lý: nhãn nằm trong sổ dữ kiện (V11), các pha sau tham chiếu mã mắt xích thay cho chép lại câu.
- Trạng thái: mở.

**V13 · Pha 2 · AGENT DÙNG + nguồn NotebookLM**
- Hiện tượng:
  - URL thông cáo KFST trả 404 (đoán).
  - "3.000 EUR/tháng" ở Hà Lan là ghép nhầm từ số 3.000 tài xế ở Đan Mạch.
  - Phạm vi Bosch bị mở từ "khách VinFast" thành "GSM".
  - Câu "[cite: 8, 12]" là tóm tắt của mô hình nhưng được dùng như nguyên văn.
  - Còn sót dòng chat thừa "Bạn có muốn…".
  - Câu trích punkt 1195 bị diễn đạt lại.
- Bản chất: NotebookLM và agent sinh câu "giống nguồn". Không có bước tự mở nguồn để so khớp nguyên văn trước khi nộp.
- Hướng xử lý: cổng tự động đối chiếu nguyên văn (fetch URL hoặc PDF, so chuỗi). Chặn URL không mở được. Lọc dòng chat thừa. Áp cho mọi vault, không chỉ tập này. Liên quan memory agents-fabricate-sources.
- Trạng thái: đã sửa trong tập. Hệ thống: mở.

**V14 · Pha 2 · AGENT DÙNG (báo cáo không đúng)**
- Hiện tượng: báo cáo sửa vòng 1 nói đã sửa mục 3 (Uber "giữ lại 4x48"), nhưng map dòng 63 và synthesis dòng 14 vẫn giữ nguyên câu sai.
- Bản chất: agent tự báo theo ý định, không theo kết quả kiểm lại file.
- Hướng xử lý: báo cáo sửa phải kèm bằng chứng máy kiểm được (grep câu cũ = 0, câu mới có dòng số). Claude luôn kiểm lại, không tin lời báo.
- Trạng thái: đã sửa trong tập. Quy trình: mở.

**V15 · Pha 1, 3 · AGENT DÙNG (trôi đề bài)**
- Hiện tượng:
  - Pha 1 tự đổi tiêu đề sang khung "canh bạc đốt tiền".
  - Pha 3 viết lại câu hỏi trung tâm, thiếu bức tranh hệ sinh thái, còn khung "điểm hòa vốn" (lỗ lãi) dù user đã loại.
  - Pha 1 lần 2 nặng lỗ lãi.
- Bản chất: chỉ đạo của user chỉ nằm trong tin nhắn, không nằm trong một file cố định mà mọi pha phải đọc. Skill mặc định kéo về khung tài chính.
- Hướng xử lý: file "hiến chương tập" khóa tiêu đề, câu hỏi trung tâm, chỉ đạo user, những điều đã loại. Mọi pha đọc file này và cổng chấm đối chiếu với nó.
- Trạng thái: mở.

**V16 · Pha 1, 2, 3 · AGENT DÙNG (số và phạm vi)**
- Hiện tượng:
  - Lãi vay toàn tập đoàn được đặt cạnh doanh thu VinFast châu Âu.
  - Tự chia ra "80 tỷ/ngày".
  - Ghi 28 = 23 + 3.
  - Số tháng 12/2023 được viết như số hiện tại.
  - Mã OBS bị cắt cụt.
  - 28 xe (2024–2025, trước GSM) được dùng làm bằng chứng GSM thất bại.
  - 28 và 364 bị đặt như cùng kỳ.
- Bản chất: agent không đọc kỳ, phạm vi và đơn vị đi kèm số. Model tự làm phép tính.
- Hướng xử lý: kbq in kỳ, phạm vi và đơn vị cạnh mỗi số. Cổng chấm bắt mọi phép so sánh khác kỳ hoặc khác phạm vi. Cấm phép tính không có trong kho, trừ khi gắn nhãn "tự tính".
- Trạng thái: đã sửa trong tập. Hệ thống: mở.

**V22 · Pha 4 · AGENT DÙNG (nhãn rơi ở câu tóm, lặp V12)**
- Hiện tượng: phần thân outline gắn nhãn suy luận đúng, nhưng Key Insight, Causal Exit và câu chốt viết lại thành khẳng định. Ví dụ CH04 "Punkt 1195 chính thức xác nhận GSM là hệ sinh thái khép kín cô độc", CH05 dòng 164, CH04 "chi phí mỗi cuốc cực kỳ đắt đỏ".
- Bản chất: các ô tóm tắt trong template (Key Insight, Exit) buộc agent viết một câu "đắt" và ngắn, nên nhãn bị bỏ khi nén. Đây là lỗi do template, lặp qua các pha.
- Hướng xử lý: như V12, câu tóm phải tham chiếu mã mắt xích trong sổ dữ kiện. Cổng chấm tự động: câu tóm nào chứa khẳng định mà mắt xích nguồn mang nhãn suy luận thì chặn.
- Trạng thái: mở.

**V23 · Pha 4 · AGENT DÙNG (bịa chi tiết minh họa)**
- Hiện tượng: "phán quyết dày 273 trang" (PDF thật có 357 trang), "trang 243 in đậm dấu mộc", "xe cắm sạc qua đêm bên bờ biển Baltic" (cách sạc là KHÔNG RÕ, còn Amager nằm bên Øresund), "Dantaxi lớn nhất Đan Mạch", "Viggo lớn nhất Copenhagen", "Uber giữ mạng lưới tài xế khổng lồ".
- Bản chất: ô "Mỏ neo vật lý" và lối văn kịch tính thúc agent tô chi tiết cảnh. Không có luật nào nói chi tiết minh họa cũng phải có nguồn.
- Hướng xử lý: luật "mọi chi tiết cụ thể (số, địa danh, so sánh nhất, mô tả vật thể) phải có nguồn hoặc nhãn minh họa". Cổng tự động bắt so sánh nhất và số không có OBS.
- Trạng thái: mở.

**V24 · Pha 4 · AGENT DÙNG (mã OBS tráo)**
- Hiện tượng: CH02 gán OBS-24c32faa (169 xe xanh) cho câu 28 xe bán lẻ, và ngược lại.
- Bản chất: agent chép mã theo cụm, không đối chiếu từng câu với mã. Cổng hiện tại chỉ kiểm mã tồn tại, không kiểm mã khớp câu.
- Hướng xử lý: cổng so số và từ khóa trong câu outline với statement của OBS được dẫn (khớp nghĩa tối thiểu).
- Trạng thái: mở.

**V25 · Pha 4 · Điểm tốt cần giữ**
- Hiện tượng: check-evidence giúp agent tìm ra doanh thu VinFast bán xe cho GSM năm 2025 (VN 15.282,5 tỷ, Indonesia 3.330 tỷ, Philippines 1.632,5 tỷ). Đây là tiền lệ đỡ thẳng luận điểm bao tiêu, mà Pha 1–3 đều bỏ sót.
- Bản chất: bằng chứng liên-thực-thể có giá trị thật. Vấn đề chỉ nằm ở cách trình bày (V07).
- Hướng xử lý: giữ cơ chế check-evidence, và đẩy nó lên sớm hơn (ngay Pha 1), không đợi tới sau outline.

**V26 · Pha 4 · AGENT DÙNG (tìm ra bằng chứng bác nhưng không dùng)**
- Hiện tượng: vòng 2, agent tự liệt kê OBS-109e429189af685e (năm 2025: 72,7% xe VinFast giao cho bên không liên quan) vào nhóm BÁC luận điểm, nhưng không đưa vào outline. Nó chỉ đưa vào hai bằng chứng bác nhẹ hơn (Tesla/BYD ở Hà Lan, GSM chiếm 6,9% số xe taxi Đan Mạch).
- Bản chất: agent đối xử với bằng chứng bác như một ô cần điền vào báo cáo, không coi nó là lực buộc phải viết lại luận điểm. Template Devil's chapter không đòi "luận điểm phải đổi gì sau phản biện".
- Hướng xử lý: cổng chấm Pha 4 và Pha 7: mỗi bằng chứng BÁC phải đi kèm (a) nó nằm ở chương nào, và (b) luận điểm được thu hẹp hay giữ nguyên, kèm lý do.
- Trạng thái: đã trả agent (seq 30). Hệ thống: mở.

**V27 · Pha 4 · NẠP + AGENT DÙNG (cùng sự kiện, nhiều số; dẫn sai mã)**
- Hiện tượng:
  - Viggo có hai bản số trong kho: "hơn 300 xe" (OBS-466c12b883a55b41) và "330 xe, 500 tài xế, 450.000 người dùng" (OBS-7348adb1eb92a9e7, OBS-c5d8d750241ee1fe).
  - Outline dẫn OBS-ccd5e3ce88c8a006 cho các số 330/500/450k, trong khi mã đó không chứa những số này.
- Bản chất: một dạng với V02 (thiếu nút sự kiện gom nhiều nguồn) và V24 (cổng không kiểm mã có khớp câu không).
- Hướng xử lý: như V02 và V24.
- Trạng thái: đã trả agent. Hệ thống: mở.

**V28 · Pha 4 · ĐIỀU PHỐI (bằng chứng đắt nằm trong nguồn đã có)**
- Hiện tượng: câu hỏi "Viggo có giống mô hình GSM không" trả lời được ngay trong PDF Konkurrencerådet mà vault đã dùng. Đoạn đó nói Uber và Bolt "indgået partnerskabsaftaler med selvstændige kørselskontorer, som anvender platformene som salgskanal", và vognmænd rời Viggo sang Drivr. Agent chỉ trích 5 đoạn từ văn bản 357 trang, phần còn lại không được khai thác.
- Bản chất: vault trích theo câu hỏi định sẵn từ Pha 2. Không có bước quay lại nguồn gốc khi luận điểm đổi, và nguồn sơ cấp dài không được đánh chỉ mục.
- Hướng xử lý: nguồn sơ cấp dài (quyết định, báo cáo thường niên, 20-F) được đánh chỉ mục theo đoạn và tra được bằng từ khóa. Khi một luận điểm mới xuất hiện, tra lại nguồn sơ cấp trước khi đi tìm nguồn mới.
- Trạng thái: mở.

**V29 · Pha 3–4 · AGENT DÙNG (có mà không biết dùng) + QUY TRÌNH (ví dụ DNA dính đề tài)**
- Hiện tượng: outline gắn nhãn "showroom di động" là suy luận và ghi "kho chưa có dữ liệu". Thực tế `kbq grep "lái thử"` trả về một note của vinfast: hồ sơ SEC (424B3, F-1) nói quan hệ với GSM "mang lại cơ hội cho khách hàng quốc tế lái thử và trải nghiệm xe VinFast". Ngược lại, ví dụ trong `00_core/stance_and_judgment.md` §3 và §5 dùng chính đề GSM với câu nói quá ("VinFast xác nhận với SEC rằng đội taxi là phòng lái thử di động") và một số không có trong kho ("lãi vay 113 tỷ/ngày"). Câu "lãi vay ... mỗi ngày" trùng kiểu lỗi agent mắc ở Pha 1 ("80 tỷ/ngày").
- Bản chất:
  - (1) Agent không tra kho khi gắn nhãn "chưa có" (V11).
  - (2) Ví dụ trong DNA lấy từ một đề tài thật và chưa được kiểm, nên agent học theo cả khung lẫn số.
- Hướng xử lý: ví dụ trong DNA phải trung tính về đề tài, hoặc có mã nguồn đã kiểm. Nhãn "kho chưa có" chỉ được ghi kèm lệnh tra đã chạy.
- Trạng thái: mở. Sẽ báo agent ở vòng chấm Pha 4.

**V30 · Pha 4 · NẠP (câu trích không đỡ câu dữ kiện)**
- Hiện tượng: OBS-109e429189af685e có statement "Năm 2025, 27,3% xe bàn giao cho bên liên quan…, 72,7% cho bên không liên quan" và source_url là 20-F 2025 (đúng tài liệu). Nhưng trường quote lại là một câu về khoản vay ("Meanwhile our use of various forms of financing…"), không chứa số 27,3 hay 72,7.
- Bản chất: cổng nạp chỉ kiểm câu trích có trong trang, không kiểm câu trích có đỡ đúng con số và ý của statement hay không. Kiểu lỗi giống V03.
- Hướng xử lý: cổng nạp đối chiếu số và từ khóa giữa statement và quote. Không khớp thì chặn. Quét lại toàn kho bằng luật này.
- Trạng thái: mở.

**V31 · WO-03 · NẠP + TỔ CHỨC (hai số cho cùng chỉ tiêu, không cờ mâu thuẫn)**
- Hiện tượng: chi phí lãi vay Vingroup năm 2025 có hai bản trong kho: 29.159.736 triệu VND (`OBS-0a95967c83f5df86`, BCTC hợp nhất trang 216) và 26.442.791 triệu VND (`OBS-947ad82ec3f10e87`, "thuyết minh chi phí tài chính"). Cùng thực thể, cùng kỳ, cùng thuộc tính `chi_phi_lai_vay`, lệch 2.717 tỷ, không có cờ mâu thuẫn. Phát hiện khi sửa ví dụ `stance_and_judgment.md` (WO-03).
- Bản chất: kiểm mâu thuẫn khi nạp chỉ so trong cùng form, hoặc một bản thiếu qualifier `pham_vi` nên không bị coi là trùng. Cùng lớp với V02, V27.
- Hướng xử lý: như V02 (lớp sự kiện/chỉ tiêu gom nhiều nguồn, lệch số sinh cờ). Trước mắt: `kbq` in cả hai và đánh dấu "LỆCH" khi cùng thực thể, kỳ, thuộc tính mà khác giá trị.
- Trạng thái: mở. Ví dụ DNA dùng bản BCTC hợp nhất (29.160 tỷ) và ghi mã.

**V33 · v2 Pha 2 · QUY TRÌNH/DNA (lớp B) — agent chạy NotebookLM bằng CLI từng lệnh thay vì engine Direct RPC**
- Hiện tượng: agent v2 tạo notebook và chạy `notebooklm source add-research … --prompt-file`, `research wait --import-all` từng lệnh (step 447–475); lệnh chờ bị timeout (step 474). User chỉ ra: quy trình đúng là bản API RPC.
- Bản chất (đã xác minh, lớp B, không phải lỗi agent):
  - (1) DNA tự mâu thuẫn: tiêu đề `AGENTS.md`, mô tả `notebooklm_librarian`, `deep_researcher` gọi là "Direct RPC", nhưng phần thân dạy nguyên khối lệnh CLI (`create`, `source add-research` ×5, `ask --prompt-file`); `deep_research.md` dạy CLI hoặc `mcp_notebooklm-mcp_batch_to_vault` (không tồn tại); `orchestration-protocol` ghi "NotebookLM qua CLI". Agent làm đúng theo chữ của DNA.
  - (2) Engine chuẩn đã có từ 30/09 (`scripts/kg_registry/kb_research_run.py`: NotebookLMClient, file kế hoạch, `run_state.json` chạy tiếp được, vault đúng khuôn nạp kho) nhưng **không file DNA nào trỏ tới**. Thêm vào đó có 5 script một-lần cho từng tập cũ (`kg_direct_rpc_research.py`, `run_modular_deep_research.py`, `ingest_deep_research.py`, `batch_extract_vault.py`, `notebooklm_deep_research_pipeline.py`) với notebook id cứng và hồ sơ `.notebooklm_home` đã hết hạn — bẫy cho agent nào tìm "script RPC".
  - (3) Điều phối: phiếu Pha 2 của Claude không kiểm skill người thực thi có khớp đường chạy chuẩn không (memory delegate-outcomes-not-commands đã dặn: đọc skill người thực thi để soát mâu thuẫn trước khi giao).
- Hướng xử lý (đã làm 02/10): một đường chạy chuẩn, ghi ở một chỗ và mọi file trỏ về: `AGENTS.md` mục NotebookLM thêm điều 0; `deep_researcher` Bước 1–2, `notebooklm_librarian` Quy tắc 1/3 và bảng lệnh, `deep_research.md` Bước 4, `orchestration-protocol`, `skills/notebooklm` (tài liệu thư viện) đều trỏ engine; CLI chỉ còn cho kiểm tra lẻ. Agent v2 đã được chuyển sang engine giữa chừng (seq 13), giữ notebook và nguồn đã nhập.
- Đã chuyển 5 script một-lần sang `scripts/_archive/` (user duyệt 02/10, có README). Việc còn mở: engine cần nhận nguồn đã nhập từ ngoài (hiện phải bỏ nguồn đó khỏi file kế hoạch).
- Bài học hệ thống: khi có một công cụ chuẩn mới, việc chưa xong cho tới khi DNA trỏ về nó và các đường cũ bị gỡ; "công cụ có trong repo" không có nghĩa là "agent biết dùng".

## D. ĐIỀU PHỐI (Claude)

**V17 · 02/10 · ĐIỀU PHỐI**
- Hiện tượng: tôi kết luận agent bỏ sót dữ kiện ở Pha 3 là do bị cắt đầu ra, rồi báo user là "lỗi tổ chức kho". Kiểm log thì sai: xem V11 (lỗi chuyển pha) và V02 (agent chưa từng tra tới dữ kiện đó).
- Bản chất: kết luận trước khi đọc log của agent.
- Hướng xử lý: luật cứng, phải đọc step log trước khi gán nguyên nhân (đã ghi ở đầu sổ và vào memory).
- Trạng thái: đã sửa quy trình của Claude.

**V18 · Pha 1–2 · ĐIỀU PHỐI**
- Hiện tượng: giao việc quá cứng (viết sẵn lệnh, khoanh sẵn nguồn), đồng thời không cho agent biết kho đang có gì. User đánh giá "hoàn toàn không ổn".
- Bản chất: giao lệnh thay vì giao kết quả, và thiếu lớp "agent biết mình có gì" (V09).
- Hướng xử lý: phiếu giao theo kết quả + tiêu chí đạt + chỉ tới skill (memory delegate-outcomes-not-commands). Agent tự tra kho trước.
- Trạng thái: đang áp dụng từ Pha 3.

## E. QUY TRÌNH / HẠ TẦNG

**V19 · Pha 2 · HẠ TẦNG agent**
- Hiện tượng: agent dừng giữa chừng sau các lệnh chạy lâu.
- Bản chất: Antigravity giới hạn WaitMsBeforeAsync 10.000 ms, lệnh chuyển sang chạy nền rồi bị ép "tiếp tục hoặc kết thúc lượt".
- Hướng xử lý: skill dạy agent dùng vòng chờ/poll cho lệnh dài. Lệnh nạp/trích xuất in tiến độ và có trạng thái hoàn tất kiểm được.
- Trạng thái: agent đã tự khắc phục. Chưa ghi vào skill.

**V20 · 02/10 · HẠ TẦNG registry**
- Hiện tượng: 5 dòng registry lệch cột. Dòng `gdp-quy-1-2026` bị dòng trên nuốt mất vì thiếu dấu ngoặc kép.
- Bản chất: không có kiểm cấu trúc CSV sau mỗi lần sửa.
- Hướng xử lý: hook kiểm số cột sau mỗi lần Write/Edit registry.
- Trạng thái: đã sửa dữ liệu 02/10. Hook: mở.

**V21 · Hạ tầng KB**
- Hiện tượng: `scripts/kg_common/kb_write.py:18` vẫn mặc định kb_main. Rule và skill còn ghi kb_main, nên mọi lệnh phải tự thêm KB_GRAPH=kb_v2.
- Bản chất: bước 3f trong kế hoạch điều hành KB chưa được duyệt.
- Hướng xử lý: đổi mặc định sang kb_v2 sau khi user duyệt.
- Trạng thái: mở.

---

---

## Phân loại gốc rễ ba lớp (user yêu cầu 02/10 chiều) — dùng để tối ưu đúng chỗ

| Lớp | Bản chất | Mã vấn đề | Cách xử lý đúng | Chỉ số đo |
|---|---|---|---|---|
| **A. Dữ liệu** (kho sai, thiếu, mâu thuẫn) | Lỗi nằm trong kb_v2, agent nào đọc cũng mắc | V01 (ngày 2030), V02, V27, V31 (nhiều bản lệch số không cờ), V03 (suy luận trong câu nạp), V04 (câu hỏng), V05 (vault chưa vào kho), V30 (quote không đỡ statement) | Cổng nạp + lớp sự kiện/cờ mâu thuẫn (P4: WO-17, 18). Sửa một lần, toàn kho | Số OBS vi phạm sau khi quét toàn kho → 0 |
| **B. Quy trình, công cụ, DNA** (do chúng ta thiết kế) | Lỗi tái lập với mọi agent vì luật mâu thuẫn, công cụ cắt, thiếu sổ, thiếu cổng | V06, V07, V08, V09, V10, V11, V12/V22 (nhãn là chữ), V15 (chỉ đạo chỉ trong tin), V17, V18, V19, V20, V21, V25, V28, V29; R1–R8 | Sửa cơ chế một lần (WO-01…14 đã làm), đo bằng **không tái phát** ở lượt chạy mới | Tỷ lệ tái phát lớp B ở lượt v2 = 0 (Pha 1 v2: 0 lỗi lớp B) |
| **C. Xác suất của LLM** (luôn có tần suất nền) | Bịa chi tiết "giống nguồn"; gán sai nguồn khi chép theo cụm; trôi khỏi chỉ dẫn trong ngữ cảnh dài; thiên kiến xác nhận; tự báo lạc quan | V13, V14, V16, V23, V24, V26; lượt v2 Pha 1: 1.900/3.500 gán vào 3 OBS không chứa, "590" không nguồn, "điểm hòa vốn" lọt dù hiến chương cấm, đọc mailbox cũ dù phiếu cấm | **Không** chữa bằng thêm luật (thêm chữ "BẮT BUỘC" không đổi xác suất, chỉ làm DNA phình — R8). Chữa bằng: (1) cổng máy ở mọi pha, rẻ và quyết định; (2) người chấm độc lập; (3) cấu trúc làm lỗi lộ ra: một mắt xích một mã OBS, trỏ mã thay chép câu; (4) giảm cơ hội sai: ô ngắn, ít số trên một dòng, không gom 3–4 OBS vào một ô; (5) chấp nhận tần suất nền và đo nó | KPI = **lỗi lớp C lọt qua cổng máy tới người chấm**, không phải lỗi lớp C xuất hiện. Mục tiêu: tiến về 0 lọt; tần suất xuất hiện chỉ cần không tăng |

Bằng chứng từ lượt v2 (02/10): Pha 1 có 0 lỗi lớp B (các cơ chế mới chặn đúng), 1 lỗi lớp A (kỳ 2030 của OBS Dantaxi), 4 lỗi lớp C. Cả 4 lỗi lớp C đều thuộc dạng cổng máy bắt được nếu luật cổng đủ (3 trong 4 lọt vì cổng còn lỗ: từ khóa chưa tách, sổ chưa chịu kiểm, nhiều OBS một ô). Kết luận: việc tối ưu tiếp theo nằm ở **lớp A (kho) và độ phủ của cổng máy**, không nằm ở viết thêm luật cho agent.

**V32 · v2 Pha 1 · C + QUY TRÌNH (nhiều OBS một ô làm mờ quy trách)**
- Hiện tượng: M12/E12 gom 3 OBS cho một câu chứa 2 số không có trong OBS nào; M10 gom 4 OBS, số 590 không nguồn. Cổng OBS-LECH bỏ qua vì chỉ cần một OBS trong ô khớp một số.
- Bản chất: lớp C (gán sai nguồn khi chép theo cụm) được quy trình cho phép vì template sổ dữ kiện cho nhiều OBS một hàng.
- Hướng xử lý: luật cấu trúc "một hàng M một mã OBS" (hàng tổng hợp thì nhãn `market_analysis` và liệt kê các M thành phần); cổng máy cảnh báo ô có >2 OBS.
- Trạng thái: cổng đã thêm cảnh báo (02/10); template sửa ở lượt sau.

## Cách rút bài học khi kết thúc lượt chạy thử
1. Gom các vấn đề theo tầng và theo bản chất (không theo hiện tượng). Đếm số lần lặp và mức hại: làm sai luận điểm, hay chỉ tốn vòng sửa.
2. Mỗi bản chất ra một thay đổi cơ chế: cổng nạp, lớp sự kiện, chỉ mục khái niệm, kbq phân trang, sổ dữ kiện tập, hiến chương tập, cổng đối chiếu nguyên văn. Đối chiếu chuẩn thế giới trước (memory follow-world-standards).
3. Kiểm thay đổi bằng bộ câu hỏi vàng trên hai đề tài khác nhau, đo trước và sau. Không đo theo cảm nhận (memory measure-before-building-tools).
4. Thứ tự làm: thứ gây sai luận điểm làm trước, thứ chỉ tốn công làm sau.
