<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/vinfast-an-do-thay-doi-chien-luoc/vault/00_Global_Vision_Synthesis.md
- Activated Persona: the_editorial_director (.agents/personas/the_editorial_director.md) + the_macro_strategist (.agents/personas/the_macro_strategist.md) + the_industrial_economist (.agents/personas/the_industrial_economist.md)
- Activated Skill: script_architect (.agents/skills/script_architect/SKILL.md) / Global Vision Synthesis Protocol (4-Tier Blueprint)
- Source Documents Consulted:
  * episodes/vinfast-an-do-thay-doi-chien-luoc/chapter_01.md
  * episodes/vinfast-an-do-thay-doi-chien-luoc/chapter_02.md
  * episodes/vinfast-an-do-thay-doi-chien-luoc/research_vault/01_su_kien_nha_cung_ung_va_chi_phi_tooling.md
  * episodes/vinfast-an-do-thay-doi-chien-luoc/research_vault/02_hien_trang_nha_may_thoothukudi_va_logistics_ckd.md
  * episodes/vinfast-an-do-thay-doi-chien-luoc/research_vault/03_ma_tran_canh_tranh_tata_mg_mahindra_vahan_08_2026.md
  * episodes/vinfast-an-do-thay-doi-chien-luoc/research_vault/04_chinh_sach_smec_va_bai_toan_thue_dva.md
  * episodes/vinfast-an-do-thay-doi-chien-luoc/research_vault/05_chuyen_dich_giai_doan_2_xe_2_banh_va_xe_buyt.md
  * episodes/vinfast-an-do-thay-doi-chien-luoc/research_vault/06_chien_luoc_xe_may_do_india_specific.md
- Execution Timestamp: 2026-09-04 07:42
-->

# BẢN QUY HOẠCH TẦM NHÌN TOÀN CẢNH (GLOBAL VISION SYNTHESIS)
## EPISODE: VINFAST ẤN ĐỘ — THAY ĐỔI CHIẾN LƯỢC & NƯỚC CỜ CHUỖI CUNG ỨNG

> 🛑 **SINGLE COGNITIVE ANCHOR (MỎ NEO TƯ DUY BẤT BIẾN):**
> 1. Tệp này là Hiến pháp Tự sự của tập phim. 100% tài liệu hạ nguồn (`03_brief.md`, `05_thesis_map.md`, `07_outline.md`, `08_chapter_briefs.md`, và các tệp kịch bản thoại `chapter_01.md` đến `chapter_07.md`) BẮT BUỘC tuân thủ cấu trúc, logic nhân quả và danh mục số liệu tại đây.
> 2. **Sợi chỉ đỏ tối thượng:** Quyết định nội bộ tháng 7/2026 — VinFast tạm dừng các dự án thử nghiệm khuôn mẫu (tooling/dies) với hơn 300 nhà cung cấp Ấn Độ và bồi thường chi phí thực tế — không phải là sự thoái lui hoảng loạn, mà là một bước cắt lỗ chi phí chìm (Sunk Cost) cực kỳ tỉnh táo của kinh tế học công nghiệp, nhằm chuyển trục từ "ép bản vẽ xe toàn cầu vào xưởng bản địa" sang "chiến lược may đo chuyên biệt kết hợp quy mô 1 triệu xe máy điện để vượt rào cản thể chế SMEC".

---

## TẦNG 1: SYSTEM META-INSTRUCTIONS & COMPLIANCE GUARDRAILS

```yaml
meta_protocol:
  episode_slug: "vinfast-an-do-thay-doi-chien-luoc"
  central_inciting_incident: "Giác thư nội bộ tháng 7/2026 (Reuters/ZingNews đưa tin đầu tháng 9/2026): VinFast yêu cầu hơn 300 nhà cung cấp Ấn Độ tạm dừng các dự án thử nghiệm khuôn dập linh kiện cho VF 3, VF 6, VF 7 và bồi hoàn chi phí thực tế đã thực hiện để cắt lỗ chi phí chìm."
  
  industrial_reality_anchors:
    thoothukudi_phase_1_status:
      type: "Assembly Plant (Cơ sở lắp ráp ô tô)"
      capex_commitment: "500 triệu USD (vốn cam kết tối thiểu)"
      design_capacity: "50.000 xe/năm"
      approved_shops:
        - "Xưởng hàn thân vỏ (Body Shop)"
        - "Xưởng sơn (Paint Shop)"
        - "Xưởng lắp ráp hoàn thiện (Assembly Shop)"
      missing_shops:
        - "KHÔNG CÓ xưởng dập tấm vỏ (Press Shop)"
        - "KHÔNG CÓ xưởng sản xuất tế bào hoặc đóng gói cụm pin (Battery Pack Shop)"
      current_production_reality: "100% xe VinFast bán ra tại thị trường Ấn Độ từ trước đến nay là lắp ráp CKD từ các cụm linh kiện và tấm thân vỏ dập sẵn nhập khẩu trực tiếp từ tổ hợp Cát Hải (Hải Phòng)."

    supplier_engagement_truth:
      supplier_count: "Hơn 300 nhà cung cấp cơ khí và phụ tùng Ấn Độ"
      engagement_stage: "Nghiên cứu kỹ thuật, R&D và chế tạo khuôn dập thử nghiệm (Tooling development & trial dies)"
      commercial_reality: "CHƯA HỀ CÓ bất kỳ hợp đồng bao tiêu hàng loạt hay bàn giao linh kiện thương mại chính thức nào (Chưa vào giai đoạn SOP - Start of Production)."
      vf3_status: "VF 3 CHƯA TỪNG MỞ BÁN THƯƠNG MẠI tại Ấn Độ; chưa có bất kỳ giao dịch mua bán linh kiện thành phẩm nào phát sinh giữa VinFast và chuỗi cung ứng liên quan đến mẫu xe này."

    scale_and_economics_deadlock:
      vahan_registration_data:
        july_2026: "1.530 xe"
        august_2026: "2.196 xe (Xếp hạng Top 4 toàn thị trường xe điện Ấn Độ, vượt Maruti Suzuki)"
      mathematical_breakdown: "Doanh số Vahan là tổng sản lượng của cả thương hiệu, chia đều cho 2 dòng xe đang bán thương mại là VF 6 và VF 7. Mỗi dòng xe chỉ đạt dưới 1.000 xe/tháng (~10.000 xe/năm)."
      supplier_breakeven_threshold: "Các nhà xưởng dập khuôn Ấn Độ yêu cầu sản lượng tối thiểu 25.000 xe/năm cho MỘT DÒNG XE để bù đắp chi phí gia công khuôn mẫu (Tooling CAPEX) trong 3 năm."
      unit_cost_consequence: "Khi sản lượng chỉ đạt ~10.000 xe/năm, phụ phí khấu hao khuôn dập (Tooling Amortization Surcharge) dội ngược vào đơn giá khiến linh kiện dập tại chỗ bị đội giá lên cao hơn nhiều so với linh kiện dập sẵn từ Cát Hải vốn đã khấu hao triệt để trên quy mô toàn cầu."

    strategic_pivot_logic:
      memo_action: "Bồi hoàn chi phí làm khuôn thử nghiệm dở dang cho đối tác = Cắt lỗ chi phí chìm (Sunk Cost), chặn đứng nguy cơ đội giá thành sản phẩm."
      three_stage_roadmap:
        stage_1_short_term: "Duy trì 100% dây chuyền lắp ráp CKD từ Cát Hải cho VF 6 và VF 7 để nuôi nhà máy Thoothukudi, đảm bảo việc làm cho 3.000 công nhân và giữ nhịp bán hàng cho mạng lưới hơn 60 đại lý 3S."
        stage_2_medium_term: "Đình chỉ mở bán VF 3; từ bỏ việc 'ép bản vẽ xe toàn cầu' vào xưởng bản địa; chuyển sang phát triển nền tảng xe may đo riêng cho Ấn Độ (India-Specific Architecture) thiết kế trực tiếp từ máy móc và linh kiện sẵn có của đối tác bản xứ."
        stage_3_long_term: "Mở rộng Giai đoạn 2 (7.000 crore INR / ~840 triệu USD) thêm 500 mẫu Anh để sản xuất 1 triệu xe máy điện và 2.000 xe buýt điện/năm; gom chung sản lượng mua sắm linh kiện điện tử và pack pin để kéo tỷ lệ nội địa hóa (DVA) toàn tổ hợp vượt 50% theo yêu cầu chính sách SMEC."

  voiceover_persona:
    role: "Nhà phân tích kinh tế công nghiệp & Điều tra chính sách độc lập"
    tone: "Điềm tĩnh, sắc lạnh, tri thức, tự sự điện ảnh (Cinematic Editorial Noir), giàu tính đối thoại thông minh bên bàn trà"
    forbidden_attitudes:
      - "PR doanh nghiệp, thanh minh hộ hãng, dùng từ đối đầu với báo chí (tin đồn thất thiệt, giật gân vội vã quy chụp)"
      - "Thuyết giáo đạo đức, phán xét một chiều, dùng từ bạo lực (đè bẹp, thảm sát, vỗ mặt)"
      - "Tư duy ngăn tủ (Silo Thinking) chia bài thành các bài giảng địa lý/lịch sử rời rạc"
      - "Burying the lede: Giấu nút thắt bản chất kỹ thuật xuống chương kết"
      - "Dùng từ ước lệ, hoa mỹ nghệ thuật làm mờ thông tin (ví dụ: 'nửa tỷ đô la' thay vì nói thẳng 'năm trăm triệu đô la'). Tôn chỉ tối thượng: Rõ ràng, dễ nghe, dễ nắm bắt, hiểu ngay lập tức!"

  narrative_spine_rules:
    spine_law: "100% các chương phải trực tiếp mổ xẻ, thử thách hoặc tháo ngòi Biến cố dừng thử nghiệm chuỗi cung ứng tháng 7/2026."
    causality_law: "Tất cả các chuyển chương bắt buộc kết nối bằng THEREFORE (Vì vậy) hoặc BUT (Nhưng). Tuyệt đối cấm AND THEN (Và rồi)."
    climax_placement: "Cú va chạm bản vẽ toàn cầu vs chuỗi cung ứng bản địa và việc đình chỉ VF 3 BẮT BUỘC nổ ra tại Chương 4 (Cao trào Màn 2)."
    russian_doll_depth: 4 # Tầng 1 (Bề mặt chi phí) ➔ Tầng 2 (Bẫy thuế SMEC) ➔ Tầng 3 (Va chạm bản vẽ lõi) ➔ Tầng 4 (Xoay trục quy mô & May đo)

  compliance_blacklist:
    - forbidden: "Dập khung gầm xe máy chung với ô tô"
      replacement: "Dùng chung cụm điện tử công suất, cáp điện, hệ thống quản lý pin BMS và dây chuyền đóng gói pack pin"
    - forbidden: "Hợp đồng bao tiêu dài hạn với 300 nhà cung cấp"
      replacement: "Hợp tác nghiên cứu kỹ thuật và chế tạo khuôn dập thử nghiệm ban đầu"
    - forbidden: "Chính phủ Ấn Độ phạt vi phạm thuế SMEC"
      replacement: "Kích hoạt thư bảo lãnh ngân hàng (Bank Guarantee) để thu hồi số tiền thuế đã được miễn giảm"
    - forbidden: "Đập tan đồn đoán thất thiệt"
      replacement: "Chính thức lên tiếng bác bỏ thông tin dừng hoạt động"
    - forbidden: "VF 3 bị ế ẩm / hủy đơn hàng linh kiện hàng loạt"
      replacement: "VF 3 chưa từng mở bán thương mại tại Ấn Độ; đình chỉ kế hoạch ra mắt để tái cấu trúc giá thành"

  immutable_data_policy:
    enforcement: "STRICT_LOCK"
    rule: "Mọi số liệu trong Tầng 4 là hằng số thực chứng bất biến. Cấm làm tròn tùy tiện, cấm bịa đặt số liệu."
```

---

## TẦNG 2: GLOBAL MACRO ARCHITECTURE (SƠ ĐỒ TRỌNG LỰC TỰ SỰ)

```
========================================================================================================
                      BẢN ĐỒ TIẾN TRÌNH NHÂN QUẢ 7 HỒI (THEREFORE / BUT MOMENTUM)
========================================================================================================

[CH01] PHÁT SÚNG THÁNG 7/2026: QUẢ BOM NỘI BỘ VÀ THỰC TẾ TRẦN TRỤI
  │ ➔ Bối cảnh: Bức tường thuế CBU 70-100% ➔ Chính sách SMEC ưu đãi thuế 15% kèm thòng lọng 50% DVA.
  │ ➔ Hiện trạng: Nhà máy Thoothukudi Giai đoạn 1 là cơ sở Lắp ráp (Assembly Plant) KHÔNG CÓ Press Shop;
  │    100% xe đang bán (VF 6 & VF 7) đều là linh kiện CKD nhập từ Cát Hải;
  │    Hơn 300 đối tác bản địa mới ở giai đoạn THỬ NGHIỆM KHUÔN MẪU; VF 3 chưa từng mở bán thương mại.
  │ ➔ Biến cố: Memo nội bộ phát lệnh dừng thử nghiệm khuôn và bồi thường chi phí thực tế cho đối tác.
  │    Thoothukudi vẫn chạy CKD, tháng 8 đạt Top 4 Vahan với gần 2.200 xe, nuôi 60+ đại lý.
  │
  ▼ [THEREFORE: Tại sao một dự án 500 triệu USD vừa khởi công lại chấp nhận bồi thường tiền mặt để dừng làm khuôn?]
  │
[CH02] BÀI TOÁN 25.000 XE: CƠ CHẾ BÓP NGHẸT CỦA TOÁN HỌC KHUÔN DẬP
  │ ➔ Lớp búp bê 1: Mổ xẻ cơ chế phân hóa 300 đối tác (linh kiện rời vs khuôn dập thân vỏ/khung gầm đòi Tooling CAPEX).
  │ ➔ Số liệu thực chứng: Doanh số Vahan tháng 7 (1.530 xe) và tháng 8 (2.196 xe, Top 4 Ấn Độ, vượt Maruti Suzuki);
  │    [NHƯNG] Mẫu số chia cho 2 dòng VF 6 và VF 7 thì mỗi mẫu chỉ đạt dưới 1.000 xe/tháng (~10.000 xe/năm).
  │ ➔ Tử huyệt: Nhà cung ứng đòi mốc hòa vốn tối thiểu 25.000 xe/năm cho MỘT DÒNG XE;
  │    Phụ phí khấu hao dội ngược khiến giá dập tại chỗ bị đội lên cao phi lý ➔ Bồi thường khuôn để cắt lỗ chi phí chìm.
  │
  ▼ [THEREFORE: Để né chiếc bẫy chi phí dập nội địa phi lý, VinFast buộc phải dùng tấm khiên phòng thủ CKD hàng hải]
  │
[CH03] HẢI TRÌNH 3.000 HẢI LÝ: TẤM KHIÊN CKD VÀ CHIẾC BẪY THỂ CHẾ SMEC
  │ ➔ Lớp búp bê 2: Hải trình Cát Hải - Tuticorin (3.000 hải lý, 7-10 ngày, thuế CKD 15%) né chi phí vận tải nội địa Ấn Độ;
  │ ➔ [NHƯNG] Đụng trúng chiếc bẫy thể chế SMEC (tháng 3/2024): Đòi 25% DVA năm 3 và 50% DVA năm 5 kèm Thư bảo lãnh ngân hàng;
  │    Bộ pin + motor chiếm 60% giá trị xe, trong khi Ấn Độ nhập 95% cell pin ➔ Lắp ráp CKD thực tế chỉ đạt 15-20% DVA;
  │    Nguy cơ mất trắng tiền bảo lãnh ngân hàng nếu không đạt chuẩn nội địa hóa.
  │
  ▼ [THEREFORE: Bị dồn vào thế tiến thoái lưỡng nan, nút thắt sâu xa nhất ở tầng cơ khí buộc phải phát nổ]
  │
[CH04 - CAO TRÀO MÀN 2] CÚ VA CHẠM DANH MỤC: VÌ SAO VF 3 BUỘC PHẢI RÚT LUI?
  │ ➔ TẦNG BÚP BÊ 3 (NÚT THẮT LÕI): Mở khuôn dập cho cả 3 nền tảng xe (VF 3, VF 6, VF 7) cùng lúc vượt quá ngân sách;
  │ ➔ Đối tác Ấn Độ chỉ đầu tư nếu cam kết sản lượng lớn; gánh nặng tiền khuôn dội ngược lại VinFast;
  │ ➔ VF 3 ước tính giá 7.5 - 10 Lakh, hoàn toàn bị kẹp chết giữa MG Comet (4.99 Lakh) và Tata Tiago EV (7.99 Lakh);
  │ ➔ Quyết định sinh tử: Đình chỉ kế hoạch ra mắt VF 3 tại Ấn Độ để chặn đứt thảm họa tài chính;
  │    Dồn lực cho VF 6 (từ 18 Lakh) và VF 7 (từ 28 Lakh) ở phân khúc giá cao hơn có dư địa hấp thu chi phí vận chuyển biển CKD tốt hơn; ký 1.000 xe Green SM Limo New Delhi.
  │
  ▼ [VÌ VẬY: Không thể dập khuôn xe ô tô nhỏ, buộc phải thay đổi quy mô của toàn bộ bàn cờ sản xuất]
  │
[CH05] BÀN CỜ 2 BÁNH: NƯỚC CỜ 840 TRIỆU USD CỨU SỐNG Ô TÔ
  │ ➔ Tầng búp bê 4: Bang Tamil Nadu phê duyệt mở rộng Giai đoạn 2 (7.000 crore INR / ~840 triệu USD, thêm 500 mẫu Anh SIPCOT);
  │ ➔ Bổ sung dây chuyền 1 triệu xe máy điện và 2.000 xe buýt điện mỗi năm;
  │    Tamil Nadu là thủ phủ xe 2 bánh (70% sản lượng, 76% DVA bản địa);
  │    Xe máy và ô tô dùng chung bộ điện tử công suất, cáp điện, BMS và dây chuyền đóng gói pack pin;
  │    1 triệu xe máy điện tạo mẫu số sản lượng khổng lồ gánh khấu hao, kéo DVA toàn tổ hợp vượt 50%, đón đầu trợ cấp PM E-Drive.
  │
  ▼ [THEREFORE: Giải quyết xong chi phí ở cửa nhà máy, triết lý sản phẩm buộc phải chuyển dịch toàn diện sang may đo]
  │
[CH06] BÀI HỌC MARUTI SUZUKI: TỪ BẢN VẼ NGOẠI LAI SANG "MAY ĐO BẢN ĐỊA"
  │ ➔ Chuyển từ "thích ứng xe toàn cầu" sang "thiết kế xe chuyên biệt cho Ấn Độ" (India-Specific Architecture / Design-to-Supply-Chain);
  │ ➔ Kỹ sư thiết kế xe từ chính máy móc, vật liệu sẵn có của 300 nhà xưởng bản địa;
  │    Pin LFP chịu nhiệt 50°C, chuẩn chống nước mùa mưa ngập lụt, gầm cao vượt địa hình Nam Á;
  │    Bài học 4 thập kỷ của Maruti Suzuki đạt 90% nội địa hóa nhờ kiên nhẫn may đo;
  │    Biến Thoothukudi thành cứ điểm xuất khẩu xanh quốc tế nhờ lợi thế cảng nước sâu và điện gió Tamil Nadu.
  │
  ▼ [BUT: Bức tranh chiến lược đã rõ ràng, nhưng thị trường tỷ dân vẫn còn vô vàn bài kiểm tra khắc nghiệt]
  │
[CH07] BƯỚC LÙI ĐỂ CẮM RỄ & KHÚC DẠO ĐẦU CỦA KẺ SỐNG SÓT
  │ ➔ Phản tư: Dừng nội địa hóa gượng ép không phải là thất bại, mà là dấu hiệu trưởng thành công nghiệp của kẻ sống sót;
  │    Đặt câu hỏi mở cho khán giả tự đánh giá bản lĩnh thích ứng của doanh nghiệp Việt Nam;
  │    Tuyên bố miễn trừ trách nhiệm pháp lý độc lập.
========================================================================================================
```

---

## TẦNG 3: ATOMIC CHAPTER BLUEPRINTS (CH01 ĐẾN CH07)

### [CH01] PHÁT SÚNG THÁNG 7/2026: QUẢ BOM NỘI BỘ VÀ THỰC TẾ TRẦN TRỤI
- **[1] THESIS:** Quyết định dừng các dự án thử nghiệm khuôn mẫu tháng 7/2026 là phát súng mở màn phá tan ảo tưởng về việc nội địa hóa dễ dàng tại Ấn Độ, đồng thời bộc lộ hiện trạng thực tế của dây chuyền lắp ráp CKD tại nhà máy Thoothukudi.
- **[2] CONTEXT & CONSTRAINTS:** 
  * Thị trường Ấn Độ áp thuế CBU 70–100%. Chính sách SMEC mở ra mức thuế ưu đãi 15% nhưng gắn chặt điều kiện đầu tư tối thiểu 500 triệu USD và cam kết DVA 25% năm 3, 50% năm 5.
  * Nhà máy Thoothukudi Giai đoạn 1 được phê duyệt là cơ sở lắp ráp (Assembly Plant) gồm xưởng hàn, sơn và lắp ráp hoàn thiện; hoàn toàn không có xưởng dập và xưởng pin tại chỗ. 100% xe bán ra thực tế đều là linh kiện CKD nhập từ Cát Hải (Hải Phòng).
  * Việc hợp tác với hơn 300 nhà xưởng bản địa mới ở khâu nghiên cứu kỹ thuật và làm khuôn dập thử nghiệm; VF 3 chưa từng mở bán thương mại.
  * Tháng 7/2026, VinFast phát giác thư nội bộ dừng các dự án thử nghiệm và cam kết bồi thường chi phí thực tế cho đối tác. Dù mạng xã hội đồn đoán rút lui, Thoothukudi vẫn chạy CKD, tháng 8 đạt Top 4 Vahan với gần 2.200 xe và bảo vệ mạng lưới hơn 60 đại lý 3S.
- **[3] IMMUTABLE DATA ANCHORS:** `DATA-01` (Memo 7/2026), `DATA-02` (300+ nhà xưởng thử nghiệm khuôn), `DATA-03` (Vahan tháng 8: 2.196 xe, Top 4 & 60+ đại lý), `DATA-04` (Bồi hoàn chi phí tooling thực tế), `DATA-09` (Thoothukudi là Assembly Plant, 100% xe đang bán là CKD Hải Phòng), `DATA-10` (Thuế CBU 70-100% vs ưu đãi SMEC 15%).
- **[4] DIALECTIC OPPOSITION:** Tin đồn tháo lui hoảng loạn trên mạng xã hội vs Hiện trường kiểm soát thiệt hại, dây chuyền CKD vẫn vận hành đạt doanh số kỷ lục tháng 8.
- **[5] NARRATIVE BRIDGE:** 
  * *Harvest:* Thu hoạch sự tò mò từ lời mở đầu về quyết định thay đổi chiến lược đột ngột.
  * *Seed:* Tại sao một dự án 500 triệu USD vừa khởi công lại chấp nhận bồi thường tiền mặt để dừng làm khuôn linh kiện? Câu trả lời nằm ở phương trình toán học tàn nhẫn của ngành ô tô $\rightarrow$ Nối sang CH02 bằng **THEREFORE**.
- **[6] VOICEOVER TONE & EMOTION:** Sắc lạnh, điều tra, nhịp điệu dồn dập, gieo căng thẳng nhận thức nhưng kiểm soát thông tin chuẩn xác.
- **[7] COMPLIANCE & TERMINOLOGY:** Tuyệt đối không dùng từ "tin đồn thất thiệt" hay "đập tan đồn đoán"; dùng "chính thức lên tiếng bác bỏ việc dừng hoạt động". Khẳng định rõ 100% xe đang bán là CKD nhập từ Hải Phòng.

---

### [CH02] BÀI TOÁN 25.000 XE: CƠ CHẾ BÓP NGHẸT CỦA TOÁN HỌC KHUÔN DẬP
- **[1] THESIS:** Bản chất của quyết định dừng hợp tác thử nghiệm không phải vì thiếu vốn, mà là sự bóp nghẹt tàn nhẫn của phương trình khấu hao khuôn dập trên sản lượng thăm dò — việc bồi thường tiền khuôn là nước cờ cắt lỗ chi phí chìm chuẩn xác.
- **[2] CONTEXT & CONSTRAINTS:** 
  * Phân hóa hơn 300 nhà cung cấp: Các chi tiết sẵn có như lốp xe, kính chắn gió, ắc quy phụ thì dễ mua; nhưng các tấm vỏ kim loại, khung gầm (Body-in-White) đòi hỏi chế tạo bộ khuôn dập chuyên dụng (Tooling CAPEX) tiêu tốn hàng triệu USD.
  * Đối tác Ấn Độ mới ở giai đoạn gia công khuôn thử nghiệm, chưa bàn giao sản phẩm thương mại; VF 3 chưa mở bán thương mại.
  * Doanh số Vahan tháng 7 đạt 1.530 xe, tháng 8 đạt 2.196 xe (Top 4 toàn quốc, vượt Maruti Suzuki). Nhưng chia cho 2 dòng VF 6 và VF 7 thì mỗi dòng chỉ đạt dưới 1.000 xe/tháng (~10.000 xe/năm).
  * Trong khi đó, nhà xưởng dập vỏ đòi mốc hòa vốn tối thiểu 25.000 xe/năm cho một dòng xe. Mẫu số quá nhỏ khiến phụ phí khấu hao dội ngược (Tooling Amortization Surcharge) làm đơn giá dập linh kiện tại chỗ bị đội lên cao hơn nhiều so với nhập từ Cát Hải.
  * Quyết định bồi hoàn chi phí khuôn dở dang giúp VinFast cắt đứt chi phí chìm, thà chịu mất một khoản nhỏ tiền thử nghiệm còn hơn chịu lỗ dài hạn trên từng chiếc xe xuất xưởng.
- **[3] IMMUTABLE DATA ANCHORS:** `DATA-05` (Phụ phí dập nội địa bị đội cao do sản lượng nhỏ), `DATA-06` (Mốc hòa vốn tối thiểu 25.000 xe/năm cho một dòng xe), `DATA-07` (Mẫu số dưới 1.000 xe/tháng khiến Tooling Amortization Surcharge phát nổ), `DATA-15` (VF 3 chưa từng mở bán thương mại tại Ấn Độ).
- **[4] DIALECTIC OPPOSITION:** Kỳ vọng chính trị về "Make in India" tức thì vs Quy luật vật lý của máy dập và phương trình khấu hao dòng tiền không thể khoan nhượng.
- **[5] NARRATIVE BRIDGE:** 
  * *Harvest:* Gặt câu hỏi tại sao phải bồi thường tiền làm khuôn thử nghiệm từ CH01.
  * *Seed:* Càng cố nội địa hóa linh kiện dập tại chỗ khi chưa đủ sản lượng thì xe càng đắt phi lý. Vì vậy, để tự bảo vệ, VinFast buộc phải dùng tấm khiên phòng thủ tự nhiên $\rightarrow$ Nối sang CH03 bằng **THEREFORE**.
- **[6] VOICEOVER TONE & EMOTION:** Điềm tĩnh, phân tích toán học chi phí đanh thép, đĩnh đạc như một kế toán trưởng công nghiệp.
- **[7] COMPLIANCE & TERMINOLOGY:** Khuôn dập là chi phí cố định (CAPEX), sản lượng là mẫu số; phân định rõ giữa xe đã bán (CKD) và linh kiện đang thử nghiệm (Trial Dies).

---

### [CH03] HẢI TRÌNH 3.000 HẢI LÝ: TẤM KHIÊN CKD VÀ CHIẾC BẪY THỂ CHẾ SMEC
- **[1] THESIS:** Lắp ráp CKD từ cảng biển là tấm khiên phòng thủ tối ưu về chi phí và logistics, nhưng lập tức đụng trúng chiếc thòng lọng chính sách SMEC của chính phủ New Delhi.
- **[2] CONTEXT & CONSTRAINTS:** 
  * Thoothukudi nằm sát cảng biển nước sâu quốc tế V.O. Chidambaranar. Tàu biển chở linh kiện CKD từ Cát Hải (Hải Phòng) đi 3.000 hải lý mất 7–10 ngày. Tuyến đường này hưởng thuế CKD ưu đãi 15% (thay vì CBU 70–100%) và né được chi phí logistics nội địa đắt đỏ của Ấn Độ (chiếm 13–14% GDP).
  * NHƯNG chiếc thòng lọng SMEC (ban hành tháng 3/2024) quy định: Hưởng thuế 15% thì phải đầu tư tối thiểu 500 triệu USD, cam kết đạt tỷ lệ DVA 25% sau 3 năm và 50% sau 5 năm, nộp Thư bảo lãnh ngân hàng (Bank Guarantee) đối ứng 100% tiền thuế được miễn giảm.
  * Thực tế công nghệ: Cụm pin và động cơ điện chiếm tới 60% giá trị xe hơi điện. Toàn bộ Ấn Độ phụ thuộc 95% tế bào pin nhập khẩu từ Đông Á. Vì vậy, xe lắp ráp CKD đơn thuần thực tế chỉ đạt 15%–20% DVA.
  * Nếu tiếp tục thuần túy lắp ráp CKD mà không nội địa hóa được, VinFast sẽ đối mặt với nguy cơ bị chính phủ Ấn Độ kích hoạt bảo lãnh ngân hàng để thu hồi toàn bộ số tiền thuế đã miễn giảm.
- **[3] IMMUTABLE DATA ANCHORS:** `DATA-08` (3.000 hải lý, 7-10 ngày từ Cát Hải sang Tuticorin), `DATA-10` (Chính sách SMEC 3/2024: 500 triệu USD, 25% DVA năm 3, 50% DVA năm 5), `DATA-11` (Thư bảo lãnh ngân hàng Bank Guarantee đối ứng), `DATA-12` (Pin + motor chiếm 60%, Ấn Độ nhập 95% cell pin), `DATA-13` (DVA CKD thực tế chỉ đạt 15% - 20%).
- **[4] DIALECTIC OPPOSITION:** Sự ưu việt tối ưu của chuỗi cung ứng hàng hải xuyên biên giới vs Chiếc bẫy thể chế bảo hộ đe dọa tịch thu toàn bộ tiền bảo lãnh ngân hàng.
- **[5] NARRATIVE BRIDGE:** 
  * *Harvest:* Gặt giải pháp tấm khiên phòng thủ CKD từ CH02.
  * *Seed:* Nhập linh kiện CKD thì chết vì vi phạm thòng lọng SMEC, tự làm khuôn dập tại chỗ thì chết vì chi phí đội giá. Thế tiến thoái lưỡng nan này bắt nguồn từ đâu? Tử huyệt kỹ thuật buộc phải lộ diện $\rightarrow$ Nối sang CH04 bằng **THEREFORE**.
- **[6] VOICEOVER TONE & EMOTION:** Kịch tính, vạch trần thế kẹt thể chế, hồi hộp, mang chiều sâu phân tích luật pháp quốc tế.
- **[7] COMPLIANCE & TERMINOLOGY:** Phân định rõ cơ chế bảo lãnh ngân hàng thu hồi thuế miễn giảm (Duty Foregone Recovery), không gọi là tiền phạt hành chính hay tội phạm hình sự.

---

### [CH04 - CAO TRÀO MÀN 2] CÚ VA CHẠM DANH MỤC: VÌ SAO VF 3 BUỘC PHẢI RÚT LUI?
- **[1] THESIS:** Nút thắt cốt lõi của toàn bộ cuộc khủng hoảng là sự phình to chi phí khi mở khuôn dập cho cả 3 nền tảng xe (VF 3, VF 6, VF 7) cùng lúc — buộc VinFast phải phân hóa danh mục: Rút VF 6 và VF 7 về phòng thủ bằng tàu biển CKD và đình chỉ dự án VF 3 để cắt lỗ chi phí chìm.
- **[2] CONTEXT & CONSTRAINTS:** 
  * Quyết định dừng nội địa hóa tháng 7/2026 áp dụng cho cả 3 dòng xe (VF 3, VF 6, VF 7) với 3 nền tảng kỹ thuật riêng biệt. Việc cùng lúc mở khuôn cho cả 3 mẫu xe đòi hỏi Tooling CAPEX khổng lồ, khiến chi phí vượt xa ngân sách dự kiến.
  * Ngành phụ trợ Tamil Nadu rất phát triển, nhưng các đối tác Tier-1 chỉ đầu tư nếu cam kết sản lượng lớn; doanh số dưới 1.000 xe/tháng khiến không đối tác nào dám chịu rủi ro, gánh nặng tiền khuôn dội ngược lại VinFast.
  * Thỏa hiệp vận hành (Operational Compromise): VF 6 (từ 18 Lakh) và VF 7 (từ 28 Lakh) nằm ở khoảng giá cao hơn, nơi chi phí cố định vận chuyển biển và thuế CKD 15% chiếm tỷ trọng tương đối nhỏ hơn trong giá bán lẻ, giúp duy trì bán hàng để nuôi nhà máy Thoothukudi và mở van B2B 1.000 xe Green SM Limo New Delhi. Ngược lại, ở phân khúc xe đô thị cỡ nhỏ (sub-10 Lakh), chi phí vận chuyển biển và thuế CKD ăn trực tiếp vào trần giá bán lẻ hạn hẹp, khiến VF 3 (dự kiến 7.5 - 10 Lakh) không còn dư địa cạnh tranh kinh tế trước MG Comet (4.99 Lakh) và Tata Tiago EV (7.99 Lakh) ➔ Buộc phải đình chỉ kế hoạch ra mắt để tránh thâm hụt tài chính.
- **[3] IMMUTABLE DATA ANCHORS:** `DATA-14` (Lệch pha quy mô & động lực đầu tư khuôn dập của đối tác bản địa), `DATA-15` (VF 3 ước tính 7.5 - 10 Lakh bị kẹp giá), `DATA-16` (Đối thủ MG Comet 4.99 Lakh, Tata Tiago EV 7.99 Lakh), `DATA-17` (Đình chỉ ra mắt VF 3 tại Ấn Độ), `DATA-18` (VF 6 từ 18 Lakh, VF 7 từ 28 Lakh ở phân khúc cao hơn có dư địa hấp thu cước biển CKD tốt hơn), `DATA-19` (1.000 xe Green SM Limo x Routematic 5/6/2026).
- **[4] DIALECTIC OPPOSITION:** Tham vọng phủ kín mọi phân khúc xe điện cùng lúc vs Thực tế kinh tế quy mô nghiệt ngã buộc phải tinh giản danh mục sản phẩm.
- **[5] NARRATIVE BRIDGE:** 
  * *Harvest:* Giải mã nút thắt cốt lõi được gieo từ Hook và CH03.
  * *Seed:* Đình chỉ VF 3 giúp chặn đứt thảm họa tài chính, nhưng làm sao đạt 50% DVA cho cả tổ hợp nếu không thể dập khuôn xe ô tô nhỏ? Buộc phải thay đổi toàn bộ quy mô của bàn cờ $\rightarrow$ Nối sang CH05 bằng **VÌ VẬY**.
- **[6] VOICEOVER TONE & EMOTION:** Sâu sắc, sắc bén, bóc trần sự thật cơ khí trần trụi, điềm tĩnh nhưng gây chấn động nhận thức.
- **[7] COMPLIANCE & TERMINOLOGY:** Trình bày việc đình chỉ VF 3 như một quyết định quản trị chi phí tỉnh táo, không dùng từ "thất bại thảm hại" hay "bỏ chạy".

---

### [CH05] BÀN CỜ 2 BÁNH: NƯỚC CỜ 840 TRIỆU USD CỨU SỐNG Ô TÔ
- **[1] THESIS:** Khi ô tô bị kẹt bài toán khuôn mẫu, nước cờ bổ sung 1 triệu xe máy điện chính là chiếc phao cứu sinh giải phóng toàn diện bài toán tỷ lệ nội địa hóa (DVA 50%) cho toàn bộ tổ hợp Thoothukudi.
- **[2] CONTEXT & CONSTRAINTS:** 
  * Chính quyền bang Tamil Nadu chính thức phê duyệt mở rộng Giai đoạn 2: Giải ngân khoản vốn 7.000 crore INR (~840 triệu USD / 21.000 tỷ VNĐ) từ gói cam kết dài hạn 2 tỷ USD, bàn giao thêm 500 mẫu Anh đất công nghiệp SIPCOT (nâng tổng diện tích lên 908 mẫu Anh).
  * Tổ hợp bổ sung dây chuyền sản xuất 1 triệu xe máy điện và 2.000 xe buýt điện mỗi năm.
  * Cơ sở hạ tầng bản địa: Tamil Nadu sản xuất 70% xe máy điện toàn Ấn Độ, chuỗi cung ứng phụ trợ xe hai bánh tại đây đạt tỷ lệ nội địa hóa tới 76%.
  * Cơ chế dùng chung linh kiện (Aggregate Volume): Xe máy điện và ô tô điện dùng chung bộ điều khiển công suất, cáp điện cao áp, hệ thống quản lý pin BMS và dây chuyền đóng gói pack pin.
  * Mẫu số 1 triệu xe máy điện tạo ra lực mua khổng lồ giúp nhà cung ứng đạt điểm hòa vốn, kéo tỷ lệ DVA toàn tổ hợp vượt 50% để giải tỏa thòng lọng SMEC mà không bị phụ thuộc vào khuôn dập ô tô; đồng thời đón đầu dòng tiền từ gói trợ cấp quốc gia PM E-Drive trị giá gần 33.000 tỷ VNĐ.
- **[3] IMMUTABLE DATA ANCHORS:** `DATA-20` (Giai đoạn 2: 7.000 crore INR / ~840 triệu USD / 21.000 tỷ VNĐ), `DATA-21` (Thêm 500 mẫu Anh SIPCOT, tổng 908 mẫu Anh), `DATA-22` (1 triệu xe máy điện + 2.000 xe buýt điện/năm), `DATA-23` (Tamil Nadu 70% xe máy điện, 76% DVA), `DATA-24` (Linh kiện dùng chung: điện tử công suất, BMS, pack pin), `DATA-25` (PM E-Drive gần 33.000 tỷ VNĐ ưu tiên xe buýt và 2 bánh).
- **[4] DIALECTIC OPPOSITION:** Tư duy làm ô tô đơn thuần bị bế tắc thể chế vs Chiến lược sinh thái đa phương tiện dùng xe hai bánh cứu xe bốn bánh.
- **[5] NARRATIVE BRIDGE:** 
  * *Harvest:* Gặt lời giải cho bài toán DVA 50% từ thế kẹt ở CH04.
  * *Seed:* Giải quyết xong bài toán DVA ở cửa nhà máy, nhưng làm sao để sản phẩm thực sự sống sót và cắm rễ lâu dài trên thị trường Nam Á? Triết lý sản phẩm phải thay đổi toàn diện $\rightarrow$ Nối sang CH06 bằng **THEREFORE**.
- **[6] VOICEOVER TONE & EMOTION:** Khởi sắc, trí tuệ chiến lược, mở rộng không gian tư duy, bừng sáng giải pháp.
- **[7] COMPLIANCE & TERMINOLOGY:** Phân định rõ các linh kiện điện tử dùng chung; tuyệt đối CẤM nói dập khung sườn xe máy chung với khung gầm ô tô.

---

### [CH06] BÀI HỌC MARUTI SUZUKI: TỪ BẢN VẼ NGOẠI LAI SANG "MAY ĐO BẢN ĐỊA"
- **[1] THESIS:** Lời giải căn cơ lâu dài không phải là áp đặt bản vẽ từ công ty mẹ, mà là kiên nhẫn may đo xe từ chính năng lực chuỗi cung ứng bản địa — bài học 4 thập kỷ của Maruti Suzuki và tầm nhìn biến Thoothukudi thành cứ điểm xuất khẩu xanh.
- **[2] CONTEXT & CONSTRAINTS:** 
  * VinFast công bố chuyển dịch chiến lược dài hạn: Thiết kế các dòng xe điện chuyên biệt cho thị trường Ấn Độ (India-Specific Architecture / Design-to-Supply-Chain). Kỹ sư thiết kế xe dựa trên thông số máy móc, thép dập và dung sai sẵn có của 300 nhà xưởng bản địa ngay từ nét vẽ đầu tiên.
  * Bộ tiêu chuẩn nhiệt đới hóa: Pin LFP chịu nhiệt độ mùa hè 50°C, tiêu chuẩn chống nước ngập lụt mùa mưa gió mùa, gầm xe nâng cao để chịu tải và vượt qua ổ gà đường sá nông thôn.
  * Bài học lịch sử: Maruti Suzuki mất 4 thập kỷ kiên nhẫn cùng ăn cùng ngủ với thợ cơ khí bản xứ để đạt tỷ lệ nội địa hóa 90%. VinFast đang tái lập hành trình đó một cách thần tốc hơn.
  * Tầm nhìn xuất khẩu toàn cầu: Thoothukudi được định vị là cứ điểm xuất khẩu xe điện xanh ra thị trường quốc tế nhờ tận dụng lợi thế cảng biển nước sâu và nguồn năng lượng tái tạo dồi dào của bang Tamil Nadu.
- **[3] IMMUTABLE DATA ANCHORS:** `DATA-26` (Chuyển sang xe may đo chuyên biệt Ấn Độ), `DATA-27` (Pin LFP chịu nhiệt 50°C, chuẩn chống nước ngập lụt, gầm cao), `DATA-28` (Maruti Suzuki: 4 thập kỷ đạt 90% nội địa hóa), `DATA-29` (Cứ điểm xuất khẩu xanh quốc tế nhờ cảng nước sâu và năng lượng sạch Tamil Nadu).
- **[4] DIALECTIC OPPOSITION:** Sự kiêu ngạo của các tập đoàn toàn cầu muốn áp đặt nguyên mẫu sản phẩm vs Sự khiêm nhường công nghiệp kiên trì may đo cùng nhà xưởng bản xứ.
- **[5] NARRATIVE BRIDGE:** 
  * *Harvest:* Gặt sự chuyển dịch sang triết lý may đo bản địa từ CH05.
  * *Seed:* Bức tranh chiến lược đã hoàn chỉnh và đầy sức thuyết phục, nhưng tương lai có thực sự dễ dàng trên thị trường tỷ dân? $\rightarrow$ Nối sang CH07 bằng **BUT**.
- **[6] VOICEOVER TONE & EMOTION:** Chiêm nghiệm sâu sắc, giàu sức nặng lịch sử và văn hóa công nghiệp, tôn vinh tư duy thực tiễn.
- **[7] COMPLIANCE & TERMINOLOGY:** Nêu gương Maruti Suzuki khách quan như một chuẩn mực công nghiệp kinh điển, không tâng bốc thái quá hay hạ thấp đối thủ.

---

### [CH07] BƯỚC LÙI ĐỂ CẮM RỄ & KHÚC DẠO ĐẦU CỦA KẺ SỐNG SÓT
- **[1] THESIS:** Quyết định dừng chuỗi cung ứng tháng 7/2026 không phải là thất bại, mà là bước lùi chiến thuật cần thiết để cắm rễ dài hạn — bài kiểm tra bản lĩnh của một doanh nghiệp công nghiệp biết đối diện với thực tế khắc nghiệt.
- **[2] CONTEXT & CONSTRAINTS:** 
  * Nhìn thẳng vào phương trình chi phí: Một hãng xe không thể tiếp tục đổ tiền làm khuôn dập khi thị trường chưa đủ lớn, cũng không thể ép người tiêu dùng chấp nhận bản vẽ xa lạ.
  * Biết dừng nội địa hóa gượng ép, biết chấp nhận bồi thường để cắt lỗ chi phí chìm, biết dùng xe 2 bánh giải vây cho ô tô và biết may đo xe từ bản vẽ gốc chính là bản lĩnh trưởng thành của kẻ sống sót.
  * Cuộc chơi phía trước tại Ấn Độ vẫn còn vô vàn biến số khắc nghiệt. Đặt câu hỏi mở cho khán giả tự suy ngẫm về năng lực thích ứng của thương hiệu Việt. Tuyên bố miễn trừ trách nhiệm pháp lý độc lập.
- **[3] IMMUTABLE DATA ANCHORS:** `DATA-30` (Tổng kết chi phí và tương quan quy mô thị trường xe điện Ấn Độ), `DATA-31` (Tuyên bố miễn trừ trách nhiệm pháp lý độc lập).
- **[4] DIALECTIC OPPOSITION:** Áp lực danh tiếng và dư luận giật gân trước mắt vs Bản năng sinh tồn và tầm nhìn công nghiệp thực tế dài hạn.
- **[5] NARRATIVE BRIDGE:** Khép lại toàn bộ vòng lặp tự sự đã mở ra từ Hook và Chương 1; giải mã trọn vẹn bản chất của quyết định tháng 7/2026.
- **[6] VOICEOVER TONE & EMOTION:** Điềm đạm, lắng đọng, đĩnh đạc, để lại dư ba nhận thức sâu sắc cho người nghe.
- **[7] COMPLIANCE & TERMINOLOGY:** Bắt buộc chốt lại bằng tuyên bố miễn trừ trách nhiệm pháp lý độc lập của kênh Góc Nhìn Podcast.

---

## TẦNG 4: IMMUTABLE DATA VAULT & SOURCE CROSS-REFERENCE MATRIX

| Mã Số Liệu | Giá Trị Số Liệu Cụ Thể | Trích Dẫn Ý Nghĩa Thực Chứng | Nguồn File (`research_vault/`) | Mã Footnote / Đoạn Trích Gốc (≤ 15 từ) |
|---|---|---|---|---|
| `DATA-01` | Giác thư nội bộ tháng 7/2026 | VinFast yêu cầu dừng các dự án phát triển khuôn dập thử nghiệm VF 3, VF 6, VF 7; hoàn trả chi phí thực tế cho đối tác | `01_su_kien_nha_cung_ung_va_chi_phi_tooling.md` | `[^VAULT-01.1]` "hold all activities... related to VF 3, VF 6, VF 7 localization" |
| `DATA-02` | Hơn 300 nhà cung cấp linh kiện | Số lượng nhà xưởng Ấn Độ ở giai đoạn R&D, thử nghiệm khuôn mẫu (chưa có linh kiện sản xuất hàng loạt SOP) | `01_su_kien_nha_cung_ung_va_chi_phi_tooling.md` | `[^VAULT-01.2]` "over 300 tier-1 component suppliers across India" |
| `DATA-03` | Vahan T8/2026: 2.196 xe, Top 4 & 60+ đại lý | Doanh số đăng ký thực tế tháng 8/2026 xếp Top 4 toàn thị trường Ấn Độ (vượt Maruti Suzuki) và mạng lưới bán lẻ | `03_ma_tran_canh_tranh_tata_mg_mahindra_vahan_08_2026.md` | `[^VAULT-03.1]` "Vahan registrations 2,196 units rank 4th above Maruti" |
| `DATA-04` | Bồi thường chi phí tooling thực tế | VinFast cam kết thanh toán chi phí gia công khuôn dập đã thực hiện để cắt lỗ chi phí chìm (Sunk Cost) | `01_su_kien_nha_cung_ung_va_chi_phi_tooling.md` | `[^VAULT-01.3]` "audit of tooling, engineering and materials costs incurred" |
| `DATA-05` | Phụ phí dập nội địa bị đội cao | Giá thành chi tiết dập tại chỗ ở Ấn Độ bị đội cao do sản lượng nhỏ so với linh kiện dập sẵn nhập từ Cát Hải | `01_su_kien_nha_cung_ung_va_chi_phi_tooling.md` | `[^VAULT-01.4]` "tooling amortization surcharge renders domestic parts uncompetitive" |
| `DATA-06` | Mốc hòa vốn 25.000 xe/năm | Sản lượng tối thiểu nhà cung cấp khuôn dập yêu cầu cho MỘT DÒNG XE để khấu hao khuôn trong 3 năm | `01_su_kien_nha_cung_ung_va_chi_phi_tooling.md` | `[^VAULT-01.5]` "minimum viable scale 25,000 units per model annually" |
| `DATA-07` | Mẫu số <1.000 xe/tháng mỗi dòng xe | Tổng Vahan T7 (1.530 xe) và T8 (2.196 xe) chia 2 mẫu VF 6 và VF 7 khiến Tooling Amortization Surcharge phát nổ | `01_su_kien_nha_cung_ung_va_chi_phi_tooling.md` | `[^VAULT-01.6]` "monthly volume under 1,000 units per model" |
| `DATA-08` | 3.000 hải lý, 7-10 ngày transit | Tuyến hàng hải chuyên dụng từ Cát Hải (Hải Phòng) đến cảng V.O. Chidambaranar (Thoothukudi) | `02_hien_trang_nha_may_thoothukudi_va_logistics_ckd.md` | `[^VAULT-02.1]` "maritime transit 3,000 nautical miles, 7 to 10 days" |
| `DATA-09` | Hồ sơ Thoothukudi là Assembly Plant | Nhà máy Giai đoạn 1 gồm xưởng hàn, sơn, lắp ráp (không có xưởng dập và xưởng pin); 100% xe đang bán là CKD Hải Phòng | `02_hien_trang_nha_may_thoothukudi_va_logistics_ckd.md` | `[^VAULT-02.2]` "Thoothukudi Phase 1 approved as assembly plant without press shop" |
| `DATA-10` | Bức tường thuế CBU 70-100% vs SMEC 15% | Thuế nhập khẩu xe nguyên chiếc so với thuế ưu đãi theo chính sách SMEC tháng 3/2024 (tối đa 8.000 xe/năm) | `04_chinh_sach_smec_va_bai_toan_thue_dva.md` | `[^VAULT-04.1]` "CBU tariff 70-100% versus SMEC 15% concession" |
| `DATA-11` | Thư bảo lãnh ngân hàng (Bank Guarantee) | Nộp bảo lãnh đối ứng 100% số thuế được ưu đãi; bị kích hoạt thu hồi nếu không đạt chỉ tiêu DVA 50% năm 5 | `04_chinh_sach_smec_va_bai_toan_thue_dva.md` | `[^VAULT-04.2]` "bank guarantee 100% duty foregone recovery risk" |
| `DATA-12` | Pin + motor chiếm 60%, nhập 95% cell | Cơ cấu giá trị xe điện và thực tế Ấn Độ phụ thuộc 95% tế bào pin nhập khẩu từ Đông Á | `04_chinh_sach_smec_va_bai_toan_thue_dva.md` | `[^VAULT-04.3]` "battery pack and motor 60% value, 95% cell imported" |
| `DATA-13` | DVA thực tế CKD chỉ 15% - 20% | Tỷ lệ giá trị nội địa tối đa đạt được nếu chỉ thuần túy lắp ráp các cụm linh kiện nhập khẩu | `04_chinh_sach_smec_va_bai_toan_thue_dva.md` | `[^VAULT-04.4]` "CKD assembly achieves only 15% to 20% domestic value add" |
| `DATA-14` | Lệch pha quy mô & động lực đầu tư khuôn dập | Mở khuôn dập cho cả 3 nền tảng (VF 3, VF 6, VF 7) cùng lúc ở quy mô dưới 1.000 xe/tháng khiến đối tác bản địa không dám đầu tư | `01_su_kien_nha_cung_ung_va_chi_phi_tooling.md` | `[^VAULT-01.7]` "tooling capex across three distinct platforms simultaneous investment" |
| `DATA-15` | VF 3 chưa mở bán, giá tính toán 7.5 - 10 Lakh | VF 3 chưa từng mở bán thương mại tại Ấn Độ; giá dự kiến bị đội cao do chi phí linh kiện | `03_ma_tran_canh_tranh_tata_mg_mahindra_vahan_08_2026.md` | `[^VAULT-03.2]` "VF 3 estimated price band 7.5 to 10 Lakh INR" |
| `DATA-16` | MG Comet 4.99 Lakh, Tata Tiago 7.99 Lakh | Mức giá niêm yết của hai mẫu xe điện thống trị phân khúc xe nhỏ Ấn Độ | `03_ma_tran_canh_tranh_tata_mg_mahindra_vahan_08_2026.md` | `[^VAULT-03.3]` "MG Comet at 4.99 Lakh, Tata Tiago EV at 7.99 Lakh" |
| `DATA-17` | Đình chỉ ra mắt VF 3 tại Ấn Độ | Quyết định dừng kế hoạch thương mại hóa dòng xe mini để tránh thảm họa cạnh tranh giá | `01_su_kien_nha_cung_ung_va_chi_phi_tooling.md` | `[^VAULT-01.8]` "defer commercial launch of VF 3 in Indian market" |
| `DATA-18` | VF 6 từ 18 Lakh, VF 7 từ 28 Lakh | Giá niêm yết hai dòng SUV cao cấp ở phân khúc cao hơn có dư địa hấp thu cước biển và chi phí CKD | `03_ma_tran_canh_tranh_tata_mg_mahindra_vahan_08_2026.md` | `[^VAULT-03.4]` "VF 6 at 18 Lakh, VF 7 at 28 Lakh higher price headroom" |
| `DATA-19` | 1.000 xe Green SM Limo x Routematic (5/6/2026) | Hợp đồng cung cấp đội xe dịch vụ di chuyển B2B tại thủ đô New Delhi | `03_ma_tran_canh_tranh_tata_mg_mahindra_vahan_08_2026.md` | `[^VAULT-03.5]` "1,000 Green SM Limo units partnership with Routematic" |
| `DATA-20` | Vốn Giai đoạn 2: 7.000 crore INR (~840 triệu USD) | Khoản đầu tư mở rộng từ gói cam kết dài hạn 2 tỷ USD tại Thoothukudi (~21.000 tỷ VNĐ) | `05_chuyen_dich_giai_doan_2_xe_2_banh_va_xe_buyt.md` | `[^VAULT-05.1]` "Phase 2 expansion 7,000 crore INR (~840M USD)" |
| `DATA-21` | Thêm 500 mẫu Anh SIPCOT, tổng 908 mẫu Anh | Quỹ đất mở rộng nhà máy được chính quyền bang Tamil Nadu bàn giao | `05_chuyen_dich_giai_doan_2_xe_2_banh_va_xe_buyt.md` | `[^VAULT-05.2]` "additional 500 acres SIPCOT land allocation total 908 acres" |
| `DATA-22` | 1 triệu xe máy điện + 2.000 xe buýt điện/năm | Quy mô công suất bổ sung hàng năm của tổ hợp sản xuất Giai đoạn 2 | `05_chuyen_dich_giai_doan_2_xe_2_banh_va_xe_buyt.md` | `[^VAULT-05.3]` "1 million e-two-wheelers and 2,000 e-buses annual capacity" |
| `DATA-23` | Tamil Nadu: 70% xe máy điện, 76% nội địa hóa | Năng lực cụm công nghiệp phụ trợ xe 2 bánh điện tại bang đặt nhà máy | `05_chuyen_dich_giai_doan_2_xe_2_banh_va_xe_buyt.md` | `[^VAULT-05.4]` "Tamil Nadu produces 70% e-two-wheelers, 76% local supply chain" |
| `DATA-24` | Linh kiện dùng chung: điện tử công suất, BMS, pack pin | Cơ chế chia sẻ linh kiện giữa xe 2 bánh và ô tô giúp gom sản lượng và gánh chi phí khấu hao | `05_chuyen_dich_giai_doan_2_xe_2_banh_va_xe_buyt.md` | `[^VAULT-05.5]` "shared power electronics, BMS and pack assembly infrastructure" |
| `DATA-25` | PM E-Drive gần 33.000 tỷ VNĐ (109 tỷ INR) | Gói trợ cấp xe điện quốc gia Ấn Độ ưu tiên dòng tiền cho xe buýt và xe hai bánh | `05_chuyen_dich_giai_doan_2_xe_2_banh_va_xe_buyt.md` | `[^VAULT-05.6]` "PM E-Drive scheme 10,900 crore INR prioritizing e-buses and 2W" |
| `DATA-26` | Chuyển sang xe may đo chuyên biệt Ấn Độ | Chiến lược chuyển đổi từ thích ứng xe toàn cầu sang Design-to-Supply-Chain | `06_chien_luoc_xe_may_do_india_specific.md` | `[^VAULT-06.1]` "strategic pivot to India-specific design-to-supply-chain models" |
| `DATA-27` | Pin LFP 50°C, chống nước ngập lụt, gầm cao | Bộ tiêu chuẩn kỹ thuật nhiệt đới hóa cho điều kiện hạ tầng và khí hậu Nam Á | `06_chien_luoc_xe_may_do_india_specific.md` | `[^VAULT-06.2]` "LFP thermal resilience 50C, monsoon water ingress, high ground clearance" |
| `DATA-28` | Maruti Suzuki: 90% nội địa hóa sau 4 thập kỷ | Bài học lịch sử của hãng xe Nhật kiên nhẫn may đo cùng nhà xưởng bản địa | `06_chien_luoc_xe_may_do_india_specific.md` | `[^VAULT-06.3]` "Maruti Suzuki four decades to achieve 90% domestic localization" |
| `DATA-29` | Cứ điểm xuất khẩu xanh quốc tế Thoothukudi | Lợi thế cảng nước sâu và năng lượng sạch Tamil Nadu phục vụ xuất khẩu | `06_chien_luoc_xe_may_do_india_specific.md` | `[^VAULT-06.4]` "Thoothukudi green maritime export base with deepwater port" |
| `DATA-30` | Thị trường xe 2 bánh 20 triệu chiếc/năm | Quy mô thị trường hấp thụ dầu mỏ và động lực điện hóa chiếm >75% phương tiện tại Ấn Độ | `05_chuyen_dich_giai_doan_2_xe_2_banh_va_xe_buyt.md` | `[^VAULT-05.7]` "annual Indian two-wheeler market exceeding 20 million units" |
| `DATA-31` | Tuyên bố miễn trừ trách nhiệm độc lập | Chuẩn mực pháp lý: Nội dung chia sẻ kiến thức kinh tế, không phải lời khuyên đầu tư | `00_core/brand_safety_guidelines.md` | `[^CORE-01]` "independent educational analysis disclaimer non-investment advice" |
