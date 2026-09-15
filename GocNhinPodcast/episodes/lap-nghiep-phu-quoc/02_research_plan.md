<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/lap-nghiep-phu-quoc/02_research_plan.md
- Activated Persona: The Socio-Economic Researcher (.agents/personas/the_socio_economic_researcher.md) & The Policy Analyst (.agents/personas/the_policy_analyst.md)
- Activated Skill: Deep Researcher (.agents/skills/deep_researcher/SKILL.md)
- Source Documents Consulted:
  * episodes/lap-nghiep-phu-quoc/vault/00_tham_chieu_3_tap_truoc.md
  * Dữ liệu khảo sát chi phí sinh hoạt, giá thuê mặt bằng, thang lương resort Phú Quốc 2025-2026
- Execution Timestamp: 2026-09-05 13:15
-->

# KẾ HOẠCH NGHIÊN CỨU SÂU (DEEP RESEARCH PLAN) — NOTEBOOKLM DIRECT RPC
## TẬP PHIM: BÀI TOÁN LẬP NGHIỆP & SINH SỐNG TẠI ĐẶC KHU PHÚ QUỐC 2026
### (Khảo sát Đa chiều: Cơ hội, Chi phí ngầm, Cơn ác mộng Mùa mưa và Quy luật Sàng lọc Thị trường)

---

## 1. MỤC TIÊU NGHIÊN CỨU & LẰN RANH AN TOÀN YMYL (OBJECTIVE & GUARDRAILS)
* **Mục tiêu tối thượng:** Cung cấp một bản báo cáo phân tích kinh tế - xã hội học thực chứng, khách quan, đa chiều và có tính phản biện cao nhất về việc chuyển dịch dòng vốn cá nhân và lao động ra Đặc khu Phú Quốc trong giai đoạn 2025–2026 hướng tới APEC 2027 và tầm nhìn 2040.
* **Lằn ranh bảo vệ YMYL (Your Money or Your Life):**
  - **Không đóng vai "tư vấn tài chính / dạy làm giàu":** Tuyệt đối không dùng các phát ngôn chỉ đạo: "Bạn nên ra đảo", "Đừng dại đầu tư", "Mua đất phân khúc X chắc thắng".
  - **Chuyển dịch sang "Kinh tế học Hành vi & Đô thị học Hải đảo":** Định vị video như một nghiên cứu tình huống (Case Study) khoa học về sự đánh đổi giữa cơ hội việc làm/kinh doanh với "thuế hải đảo" (Island Tax) và chu kỳ thời tiết gió mùa.
  - **Tuyên bố miễn trừ trách nhiệm (Legal Disclaimer):** Mọi số liệu đều nhằm mục đích giáo dục, phản ánh hiện tượng thị trường và không cấu thành lời khuyên đầu tư hay khuyến nghị nghề nghiệp.

---

## 2. PROMPT NẠP NGUỒN CẤU TRÚC (STRUCTURED DEEP RESEARCH INGESTION PROMPT)
> *Prompt này sẽ được truyền trực tiếp vào lệnh CLI `notebooklm source add-research "<PROMPT>" --mode deep --import-all` để máy chủ NotebookLM tự động càn quét các nguồn tài liệu báo chí chính thống, báo cáo thống kê, nghiên cứu học thuật và văn bản pháp luật mới nhất.*

```text
Nghiên cứu toàn diện, đa chiều và thực chứng về thực trạng sinh sống, lập nghiệp, kinh doanh và thị trường lao động tại Đặc khu Phú Quốc (tỉnh An Giang mới) giai đoạn 2024 - 2026, với các nội dung trọng tâm sau:

1. DỮ LIỆU ĐỊNH LƯỢNG VỀ CHI PHÍ SINH HOẠT & MẶT BẰNG KINH DOANH TẠI PHÚ QUỐC (2025-2026):
- Khảo sát giá thuê phòng trọ bình dân và căn hộ/phòng tiện nghi tại Dương Đông, An Thới, Dương Tơ, Cửa Cạn.
- Giá thuê mặt bằng kinh doanh, kiot, shophouse mặt tiền đường lớn (ĐT.975, Trần Hưng Đạo, 30/4) và các khu đô thị mới. Yêu cầu đặt cọc (mấy tháng), chu kỳ thanh toán (3-6 tháng).
- Chi phí sinh hoạt hàng ngày (giá thực phẩm, rau củ, thịt cá, điện nước, cước viễn thông, chi phí y tế khám chữa bệnh) so sánh với TP.HCM và Hà Nội.
- Phân tích "thuế hải đảo" (Island Tax): Chi phí vận tải biển/hàng không đội giá vốn hàng bán (COGS) lên bao nhiêu %?

2. THỰC TRẠNG THỊ TRƯỜNG LAO ĐỘNG & THANG LƯƠNG ĐÃI NGỘ:
- Cơ cấu tuyển dụng tại các tập đoàn và resort 4-5 sao (Sun Group, Vingroup, BIM Group, Regent, JW Marriott, Vinmec...): Thang lương cho lao động phổ thông (buồng phòng, phục vụ, bảo vệ), chuyên môn/giám sát (lễ tân ngoại ngữ, kỹ thuật cơ điện, đầu bếp) và quản lý cấp trung/cao.
- Chính sách đãi ngộ cốt tử: Tỷ lệ doanh nghiệp bao ăn ở (ký túc xá) hoặc trợ cấp nhà trọ; mức thu nhập từ phí phục vụ (service charge) và tiền tip.
- Lợi thế cạnh tranh của lao động đa ngôn ngữ: Nhu cầu thực tế đối với nhân sự thông thạo tiếng Hàn, tiếng Trung, tiếng Nga, tiếng Anh tại Phú Quốc.
- Tỷ lệ nhảy việc và đào thải (turnover rate) của lao động dịch vụ trên đảo do xa gia đình, đời sống tinh thần hạn chế và chi phí đắt đỏ.

3. RỦI RO CHU KỲ MÙA MƯA & BẪY KINH DOANH F&B / HOMESTAY NHỎ LẺ:
- Tác động của mùa mưa (gió mùa Tây Nam từ tháng 5 đến tháng 10) lên doanh thu các cơ sở kinh doanh dịch vụ ngoài trời, tour đảo, bến tàu cao tốc. Mức độ sụt giảm lượng khách và doanh thu (ước tính % sụt giảm).
- Hiện tượng "chết yểu" của các mô hình quán cà phê "chill", homestay tự phát sau mùa khô đầu tiên do cạn kiệt vốn dự phòng.
- Cơ chế cạnh tranh và "bẫy hoa hồng": Sự phụ thuộc của các quán ăn, cửa hàng độc lập vào hoa hồng chiết khấu cho tài xế taxi và hướng dẫn viên du lịch (20% - 40%).
- Sự lấn át của mô hình khu nghỉ dưỡng phức hợp khép kín (Integrated Resorts: Grand World, Sunset Town, Corona Casino) đối với dòng khách tour trọn gói (all-inclusive).

4. CƠ HỘI BỀN VỮNG CHO NGƯỜI LẬP NGHIỆP TRONG CHU KỲ MỚI 2026-2040:
- Mô hình B2B (Business-to-Business): Cung ứng chuỗi thực phẩm sạch, giặt ủi công nghiệp, bảo trì hệ thống cơ điện chống ăn mòn muối biển, cảnh quan cây xanh cho các khu resort 5 sao.
- Dịch vụ đô thị thường trú đón đầu quy hoạch 700.000 dân đến năm 2040: Nhu cầu giáo dục mầm non, trung tâm ngoại ngữ, phòng khám y tế gia đình, siêu thị dân sinh phục vụ cư dân định cư dài hạn.
- Khung thể chế & Pháp lý: Nghị quyết số 41/2026/QH16 về cơ chế đặc thù tháo gỡ dự án APEC 2027; Đề án thí điểm Khu thương mại tự do (FTZ) 10 năm; Tác động của việc Phú Quốc thành Đặc khu và bảng giá đất mới 2026 lên việc thuê đất, đăng ký hộ kinh doanh cá thể.

5. BÀI HỌC SO SÁNH QUỐC TẾ:
- Kinh nghiệm lập nghiệp và chuyển dịch dân số tại các đảo đặc khu quốc tế: Đảo Jeju (Hàn Quốc), Bali (Indonesia), Okinawa (Nhật Bản) — bài toán người từ đất liền ra đảo sinh sống (Islander vs Mainlander), rào cản thích nghi văn hóa, cô lập địa lý và chi phí y tế/giáo dục.
```

---

## 3. DANH SÁCH 10 CÂU HỎI TRÍCH XUẤT CHUYÊN SÂU (BATCH EXTRACTION QUESTIONS)
*Sau khi nạp nguồn thành công vào Master Notebook, hệ thống sẽ thực thi trích xuất 10 tệp nghiên cứu độc lập tương ứng lưu vào thư mục `episodes/lap-nghiep-phu-quoc/research_vault/`:*

1. **`01_living_costs_and_island_tax.md`:**  
   *Câu hỏi:* Phân tích chi tiết cấu trúc chi phí sinh hoạt tại Phú Quốc giai đoạn 2025–2026 (giá thuê phòng trọ, giá điện nước, thực phẩm, sinh hoạt phí hàng tháng). "Thuế hải đảo" (Island Tax) do chi phí vận tải biển làm tăng giá vốn hàng hóa và đời sống so với đất liền bao nhiêu phần trăm?

2. **`02_commercial_rental_market.md`:**  
   *Câu hỏi:* Thực trạng giá thuê mặt bằng kinh doanh (kiot, nhà phố, shophouse) tại các khu vực trọng điểm của Phú Quốc (Dương Đông, An Thới, các trục đường lớn ĐT.975, Trần Hưng Đạo). Điều kiện hợp đồng thuê (tiền cọc bao nhiêu tháng, chu kỳ thanh toán, rủi ro trượt giá hợp đồng) thực tế ra sao?

3. **`03_labor_market_wages_and_benefits.md`:**  
   *Câu hỏi:* Cơ cấu thị trường lao động tại các resort 4-5 sao và doanh nghiệp lớn tại Phú Quốc hiện nay: Mức lương cứng cho từng cấp bậc (lao động phổ thông, chuyên môn kỹ thuật, quản lý), tỷ lệ phụ cấp ăn ở (ký túc xá), service charge, và nhu cầu khẩn thiết về nhân sự ngoại ngữ (Hàn, Trung, Nga, Anh)?

4. **`04_seasonal_monsoon_impact.md`:**  
   *Câu hỏi:* Tác động cụ thể của chu kỳ thời tiết mùa mưa (gió mùa Tây Nam từ tháng 5 đến tháng 10) lên hoạt động kinh doanh tại Phú Quốc. Doanh thu của các cơ sở du lịch, nhà hàng, homestay nhỏ lẻ sụt giảm bao nhiêu phần trăm? Tỷ lệ các cửa hàng phải đóng cửa hoặc chuyển nhượng sau 1 mùa mưa là bao nhiêu?

5. **`05_all_inclusive_resorts_vs_local_smbs.md`:**  
   *Câu hỏi:* Phân tích sự xung đột thị phần giữa mô hình "hệ sinh thái khép kín" (Integrated Resorts / All-inclusive tours của các tập đoàn lớn) và các hộ kinh doanh độc lập bên ngoài. Thực trạng cuộc chiến trích hoa hồng cho taxi, tài xế và hướng dẫn viên (20%-40%) tác động ra sao đến biên lợi nhuận của người kinh doanh nhỏ lẻ?

6. **`06_b2b_and_supply_chain_opportunities.md`:**  
   *Câu hỏi:* Những mô hình kinh doanh B2B (bán cho doanh nghiệp/resort) nào đang chứng minh hiệu quả cao và bền vững tại Phú Quốc (cung ứng thực phẩm tươi sống, giặt ủi công nghiệp, bảo dưỡng kỹ thuật, vật liệu xây dựng, dịch vụ hỗ trợ APEC 2027)?

7. **`07_permanent_resident_services_2040.md`:**  
   *Câu hỏi:* Dựa trên Quyết định 150/QĐ-TTg về quy hoạch 700.000 dân thường trú đến 2040, đâu là các ngành dịch vụ phục vụ đời sống dân cư đô thị đang có dư địa phát triển lớn (giáo dục mầm non, trường học, chăm sóc sức khỏe, dịch vụ tiện ích cộng đồng) thay vì chỉ trông chờ vào khách du lịch vãng lai?

8. **`08_institutional_legal_framework.md`:**  
   *Câu hỏi:* Khung pháp lý và cơ chế quản lý kinh doanh tại Đặc khu Phú Quốc (trực thuộc tỉnh An Giang mới) sau khi Quốc hội ban hành Nghị quyết số 41/2026/QH16 và thí điểm Khu thương mại tự do (FTZ). Việc áp dụng bảng giá đất mới 2026 và siết chặt kiểm tra nguồn gốc đất ảnh hưởng như thế nào đến người thuê mặt bằng và đăng ký kinh doanh?

9. **`09_international_island_benchmarks.md`:**  
   *Câu hỏi:* Phân tích bài học kinh nghiệm từ các đảo du lịch và đặc khu quốc tế (Jeju - Hàn Quốc, Bali - Indonesia, Okinawa - Nhật Bản, Phuket - Thái Lan) về làn sóng người từ đất liền ra đảo lập nghiệp: Tỷ lệ thất bại trong 3 năm đầu, cú sốc chi phí y tế/học tập cho con cái và rào cản thích nghi văn hóa hải đảo?

10. **`10_steelman_audit_and_survival_playbook.md`:**  
    *Câu hỏi:* Phản biện đối lập mạnh nhất (Steelman Counter-Thesis): Những ngộ nhận chết người nào khiến người mang vốn ra Phú Quốc dễ bị mất trắng? Đâu là bản quy tắc sinh tồn (kỷ luật vốn dự phòng, kỹ năng chuyên môn, mạng lưới liên kết) dành cho một cá nhân muốn lập nghiệp thành công và an cư lâu dài tại Phú Quốc?

---

## 4. QUY CHUẨN THỰC THI NOTEBOOKLM DIRECT RPC
* **Môi trường:** Python script chạy trong `.venv_notebooklm/bin/python`.
* **Tham số lệnh nạp:** `BypassSandbox: true`, `--mode deep`, `--import-all`.
* **Notebook Metadata Binding:**
  - File lưu ID: `episodes/lap-nghiep-phu-quoc/.notebook_id`
  - File lưu URL: `episodes/lap-nghiep-phu-quoc/.notebook_url`
* **Tiến trình:**
  1. Tạo Master Notebook mới: `Đặc khu Phú Quốc 2026 — Bài toán Lập nghiệp & Sinh sống`.
  2. Nạp Structured Deep Research Ingestion Prompt qua lệnh CLI.
  3. Kiểm tra danh mục tài liệu nạp về và tiến hành Batch Extraction 10 báo cáo Vault.
