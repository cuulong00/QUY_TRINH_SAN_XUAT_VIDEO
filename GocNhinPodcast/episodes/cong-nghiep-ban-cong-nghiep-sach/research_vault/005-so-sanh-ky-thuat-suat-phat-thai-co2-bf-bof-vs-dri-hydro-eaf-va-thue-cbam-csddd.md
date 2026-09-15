---
title: "So sánh chi tiết về mặt kỹ thuật, suất tiêu hao năng lượng và lượng phát thải CO2 trên mỗi tấn thép giữa Lò cao than cốc truyền thống (BF-BOF) và Lò hoàn nguyên trực tiếp dùng Hydro kết hợp lò hồ quang điện (DRI-EAF). Tính toán chi phí thuế carbon EU CBAM (từ 01/01/2026 với giá 75-100 EUR/tấn CO2) và tác động của Chỉ thị CSDDD Scope 3 lên giá thành thép."
type: nblm-answer
asked_at: 2026-08-25T01:20:32.835957+00:00
notebook_url: "https://notebooklm.google.com/notebook/b9fad8a3-c8de-44e7-bedd-49a08b3f1e83"
session_id: "fa816c2c-4bd9-48ed-9f4b-554c26f79b64"
citations_count: 46
---

# So sánh chi tiết về mặt kỹ thuật, suất tiêu hao năng lượng và lượng phát thải CO2 trên mỗi tấn thép giữa Lò cao than cốc truyền thống (BF-BOF) và Lò hoàn nguyên trực tiếp dùng Hydro kết hợp lò hồ quang điện (DRI-EAF). Tính toán chi phí thuế carbon EU CBAM (từ 01/01/2026 với giá 75-100 EUR/tấn CO2) và tác động của Chỉ thị CSDDD Scope 3 lên giá thành thép.

> Asked on 2026-08-25T01:20:32.835957+00:00 against [NotebookLM Master Notebook](https://notebooklm.google.com/notebook/b9fad8a3-c8de-44e7-bedd-49a08b3f1e83)

## Answer

### I. Đối Chiếu Kỹ Thuật, Suất Tiêu Hao Năng Lượng và Phát Thải: BF-BOF vs. \\(H_2\\)-DRI-EAF

Sự khác biệt giữa hai lộ trình luyện thép này nằm ở bản chất phản ứng hóa học (tác nhân hoàn nguyên), mức độ điện hóa và các loại nguyên liệu đầu vào chính:

| Chỉ số Kỹ thuật & Năng lượng | Lò cao than cốc truyền thống (BF-BOF) [1, 2] | Lò hoàn nguyên trực tiếp bằng Hydro (H2-DRI-EAF) [1, 2] |
| :--- | :--- | :--- |
| **Tác nhân hoàn nguyên** | Cacbon oxit (CO) sinh ra từ việc đốt **than cốc** trong lò cao [1, 3]. | Khí **hydro xanh** (\\(H_2\\)) phản ứng thể rắn bên trong lò trục đứng [2, 4]. |
| **Phản ứng & Sản phẩm phụ** | Khử oxy trong quặng sắt bằng cacbon, giải phóng khí thải **\\(CO_2\\)** trực tiếp [5, 6]. | Khử oxy trong quặng sắt bằng hydro, giải phóng **hơi nước** (\\(H_2O\\)) [4, 5]. |
| **Suất phát thải trực tiếp (Scope 1)** | Rất cao: trung bình từ **1.64 đến 1.67 \\(tCO_2\\)/tấn thép thô** [7, 8] (chiếm khoảng 80% lượng phát thải của quy trình tích hợp [7]). | Cực thấp: chỉ dao động từ **0.02 đến 0.1 \\(tCO_2\\)/tấn thép thô** [9] (giảm tới hơn 95% so với BF-BOF [9, 10]). |
| **Suất phát thải tổng hợp (Scope 1 & 2)** | Khoảng **1.9 đến 2.4 \\(tCO_2\\)/tấn thép thành phẩm** [1, 9] (phụ thuộc vào hiệu suất vận hành của lò cao [1]). | Dưới **0.2 \\(tCO_2\\)/tấn thép** (nếu sử dụng hoàn toàn điện tái tạo để điện phân và chạy lò EAF) [11, 12]. |
| **Tiêu hao năng lượng điện** | Rất thấp: mua ngoài chỉ khoảng **0.4% đến 0.6 MWh/tấn** nhờ tận dụng lượng khí lò cao để tự phát điện [11, 13]. | Cực cao: tiêu tốn khoảng **~3.48 MWh/tấn thép lỏng** [14, 15] (chủ yếu phục vụ quá trình điện phân nước tách hydro [14]). |
| **Yêu cầu quặng sắt đầu vào** | Linh hoạt, chấp nhận hầu hết các loại quặng thiêu kết (Sinter) và quặng vê viên thông thường [16, 17]. | Khắt khe: chỉ sử dụng **quặng viên chất lượng cao cấp DR** (DR-grade pellets, chiếm ~3% trữ lượng toàn cầu) [2, 16]. |
| **Yếu tố nhạy cảm kinh tế** | Giá than mỡ, than cốc, quặng sắt đầu vào và chính sách thuế carbon [1]. | Giá điện năng tái tạo, hiệu suất/CAPEX của máy điện phân và giá quặng viên cấp DR [1]. |

---

### II. Tính Toán Chi Phí Thuế Carbon EU CBAM (Từ 01/01/2026)

Cơ chế EU CBAM chính thức áp đặt nghĩa vụ tài chính bắt buộc kể từ ngày **01/01/2026** [18, 19]. Số lượng chứng chỉ CBAM nhà nhập khẩu phải nộp được tính trên lượng phát thải tích tụ trực tiếp (Scope 1) sau khi đã trừ đi hạn ngạch miễn phí tương đương của các nhà sản xuất nội địa EU (Phase-in Factor) [20, 21].

#### 1. Cơ chế tính phí lũy tiến theo các giai đoạn:
*   **Giai đoạn 2026 – 2027:** Do các nhà sản xuất nội địa EU vẫn được giữ **97.5%** hạn ngạch miễn phí để tránh sốc thị trường, các nhà xuất khẩu ngoài EU sang châu Âu **chỉ phải nộp thuế cho 2.5%** lượng phát thải thực tế [21, 22].
*   **Lộ trình tăng tốc:** Tỷ lệ nộp thuế này sẽ tăng dần lên mức xấp xỉ **48.5% vào năm 2030** và áp thuế **100% vào năm 2034** khi hạn ngạch miễn phí bị loại bỏ hoàn toàn [22].
*   **Rủi ro từ dữ liệu mặc định (Default Values):** Nếu không cung cấp được dữ liệu phát thải thực tế được kiểm toán độc lập [23], nhà nhập khẩu bị áp mức phát thải mặc định (thường lấy theo mức phát thải cao nhất của các nhà máy kém hiệu quả nhất tại EU) [24] kèm hệ số phạt markup lũy tiến: **+10% (năm 2026)**, **+20% (năm 2027)**, và **+30% (từ năm 2028 trở đi)** [25].

#### 2. Bảng tính toán chi phí CBAM trên mỗi tấn thép thành phẩm:
*(Giả định suất phát thải Scope 1 trực tiếp của **BF-BOF là 1.67 \\(tCO_2\\)/tấn** [8] và **\\(H_2\\)-DRI-EAF là 0.05 \\(tCO_2\\)/tấn** [9])*

##### Kịch bản 1: Giá carbon EU ETS ở mức trung bình 75 EUR/tấn \\(CO_2\\) [26, 27]
*   **Lộ trình lò cao BF-BOF:**
    *   **Năm 2026 (Nghĩa vụ 2.5%):** \\(1.67 \times 75 \times 2.5\% = \mathbf{3.13\text{ EUR/tấn thép}}\\) [20, 22].
    *   **Năm 2034 (Nghĩa vụ 100%):** \\(1.67 \times 75 \times 100\% = \mathbf{125.25\text{ EUR/tấn thép}}\\) [20, 22].
*   **Lộ trình thép xanh \\(H_2\\)-DRI-EAF:**
    *   **Năm 2026 (Nghĩa vụ 2.5%):** \\(0.05 \times 75 \times 2.5\% = \mathbf{0.09\text{ EUR/tấn thép}}\\) [20, 22].
    *   **Năm 2034 (Nghĩa vụ 100%):** \\(0.05 \times 75 \times 100\% = \mathbf{3.75\text{ EUR/tấn thép}}\\) [20, 22].

##### Kịch bản 2: Giá carbon tăng cao đạt mức 100 EUR/tấn \\(CO_2\\) [28, 29]
*   **Lộ trình lò cao BF-BOF:**
    *   **Năm 2026 (Nghĩa vụ 2.5%):** \\(1.67 \times 100 \times 2.5\% = \mathbf{4.18\text{ EUR/tấn thép}}\\) [20, 22].
    *   **Năm 2034 (Nghĩa vụ 100%):** \\(1.67 \times 100 \times 100\% = \mathbf{167.00\text{ EUR/tấn thép}}\\) [20, 22].
*   **Lộ trình thép xanh \\(H_2\\)-DRI-EAF:**
    *   **Năm 2026 (Nghĩa vụ 2.5%):** \\(0.05 \times 100 \times 2.5\% = \mathbf{0.13\text{ EUR/tấn thép}}\\) [20, 22].
    *   **Năm 2034 (Nghĩa vụ 100%):** \\(0.05 \times 100 \times 100\% = \mathbf{5.00\text{ EUR/tấn thép}}\\) [20, 22].

**Nhận xét tài chính:** Ở giai đoạn 2026, mức chênh lệch thuế carbon giữa hai lộ trình là rất nhỏ (chỉ khoảng **3.04 – 4.05 EUR/tấn**). Tuy nhiên, đến năm 2034, lò cao truyền thống sẽ phải đối mặt với gánh nặng thuế khổng lồ từ **121.50 đến 162.00 EUR cho mỗi tấn thép** xuất khẩu sang EU, hủy hoại hoàn toàn khả năng cạnh tranh về giá [22].

---

### III. Tác Động Của Chỉ Thị CSDDD và Kiểm Toán Scope 3 Lên Giá Thành Thép

Chỉ thị **Thẩm định Chuỗi cung ứng Bền vững (CSDDD)** của EU quy định trách nhiệm pháp lý bắt buộc lên các tập đoàn lớn trong việc rà soát và triệt tiêu các tác động tiêu cực đến môi trường dọc theo chuỗi giá trị của họ [30, 31]. Điều này đẩy áp lực kiểm soát phát thải trực tiếp sang **phát thải gián tiếp Phạm vi 3 (Scope 3)** [32, 33].

#### 1. Sự phân hóa sâu sắc về dấu chân carbon Scope 3:
Thép là vật liệu thượng nguồn chiếm tỷ trọng phát thải cực lớn trong sản phẩm của các ngành chế tạo hạ nguồn (như ô tô, điện tử, xây dựng) [34-36].
*   **Sản phẩm thép dẹt cán nóng (HRC) truyền thống (BF-BOF):** Có lượng phát thải tích lũy Scope 1, 2 và 3 lên tới **2.40 \\(tCO_2\\)/tấn thép** (trong đó phát thải thượng nguồn từ khai thác quặng, tuyển than, và vận chuyển Scope 3 chiếm tới **0.46 \\(tCO_2\\)/tấn**) [37].
*   **Sản phẩm thép lò hồ quang điện (EAF) dùng thép phế liệu:** Có lượng phát thải tổng thể chỉ khoảng **0.83 - 0.97 \\(tCO_2\\)/tấn thép** [37].
*   Chênh lệch dấu chân carbon dòng thép cuộn cán nóng (HRC) giữa lò cao truyền thống và lò điện lên tới **hơn 147%** [37]. Dưới áp lực của CSDDD, các thương hiệu lớn buộc phải chuyển dịch sang thu mua thép xanh nhằm hạ thấp phát thải Scope 3 của chính họ, nếu không sẽ bị loại khỏi chuỗi cung ứng toàn cầu [38].

#### 2. Tác động biên dòng tiền của "Phí xanh" (Green Premium) lên sản phẩm cuối cùng:
Để sử dụng thép xanh hoàn nguyên hydro (\\(H_2\\)-DRI-EAF), các doanh nghiệp phải trả một mức phí chênh lệch (Green Premium) dao động từ **50 đến 200 EUR/tấn thép** ở giai đoạn đầu [39]. Tuy nhiên, phân tích thực chứng cho thấy mức phí này khi kết chuyển vào giá thành sản phẩm tiêu dùng hạ nguồn là **không đáng kể (marginal)**:

*   **Xe hơi điện (Automotive):** Thép cấu thành nên toàn bộ hệ thống khung gầm và vỏ pin chiếm khối lượng lớn [34]. Với mức "Phí xanh" của thép hydro là **226 USD/tấn** (khi giá hydro đạt 5 USD/kg), chi phí tăng thêm cho một chiếc xe điện chỉ rơi vào khoảng **203 – 208 USD/xe** [34, 40], tương đương **chưa đầy 1% giá trị xe** (giả định mức giá trung bình của xe điện từ 28,000 USD đến hơn 40,000 USD) [34, 40]. Mức tăng giá này hoàn toàn có thể được hấp thụ dễ dàng bởi tệp khách hàng phân khúc cao cấp [41].
*   **Thiết bị gia dụng (Washing Machine):** Thép chiếm 25% lượng carbon phát thải của một chiếc máy giặt [36]. Việc chuyển đổi hoàn toàn sang thép xanh chỉ làm tăng giá bán của sản phẩm máy giặt từ **2% đến 4%** (tương đương tăng **dưới 12 EUR/máy**) [36].
*   **Công trình xây dựng dân dụng (Construction):** Đóng góp tới 52% tổng nhu cầu thép thế giới [42]. Khi áp dụng hoàn toàn thép xanh hydro, chi phí vật tư tăng thêm khoảng **563 - 565 USD** cho một căn hộ chung cư diện tích 50 \\(m^2\\) (định mức tiêu chuẩn 50kg thép/\\(m^2\\)) [35, 42], đây là một tỷ lệ cực nhỏ so với tổng chi phí đầu tư xây dựng hay giá mua căn hộ [35, 42].
*   **Công nghiệp đóng tàu (Shipbuilding):** Là ngành chịu ảnh hưởng lớn nhất vì thép chiếm tới **95% trọng lượng tàu** [43]. Việc sử dụng thép xanh hydro sẽ làm tăng giá thành chế tạo một tàu chở hàng rời (Bulk Carrier) tải trọng 40.000 DWT thêm khoảng **3 triệu USD** [44], tương đương mức **tăng xấp xỉ 10% giá trị tàu** (trên tổng mức đầu tư 30 triệu USD) [44].

**Kết luận chiến lược:** Trừ ngành đóng tàu, tất cả các ngành công nghiệp hạ nguồn then chốt như ô tô, điện gia dụng và xây dựng đều có **mức sẵn lòng chi trả (Willingness-to-pay) rất cao** đối với thép xanh [38, 45]. CSDDD đang biến dữ liệu phát thải Scope 3 từ một báo cáo tuân thủ mang tính hình thức thành một **yếu tố quyết định tính sinh tử của hợp đồng thương mại** [38, 46].

***

🎧 Bạn có muốn tôi khởi tạo việc xây dựng một **Tập Podcast (Audio Overview)** theo định dạng tranh luận sâu (Debate) dài khoảng 10-15 phút để phân tích cuộc đối đầu công nghệ này giữa các chuyên gia luyện kim lò cao truyền thống và các kỹ sư điện hóa thép xanh không?

## Citations & References

### [1] Source ID: `b5301831-463b-49a9-bea6-69c7fef88287`

> white storage tanks against a blue skyBenchmark: BF–BOFBF–BOF (blast furnace–basic oxygen furnace) is the classic ore-to-steel route. A widely used reference point is:Emissions: commonly around ~2.2 tCO₂ per tonne of crude steel (varies by plant efficiency and electricity mix)Energy: on the order of ~15 GJ per tonne of liquid steel (IEA, 2020)Comparison table: BF–BOF as the baselinePathwayTypical CO₂ intensity (indicator)Typical CO₂ reduction vs BF–BOFMain energy exposureEconomics are most sensitive toPractical benefits beyond CO₂BF–BOF~2.0–2.4 tCO₂/t steelBaselineCoal/coke (energy + chemistry)Coal/coke price, ore/coke quality, carbon policyVery large scale; mature supply chainsModern scrap-EAFOften ~0.3–0.6 tCO₂/t steelOften ~60–85% lowerElectricity + scrapElectricity tariff, scrap price, scrap sorting qualityHigh flexibility; Fewer large, capital-intensive processing facilities compared with fully integrated steelmaking routes; strong process controlNatural gas DRI–EAFOften ~1.1–1.6 tCO₂/t steelOften ~20–50% lowerNatural gas + electricity + pelletsGas price, DR-grade pellet premium, power priceMore predictable chemistry than all-scrap; dilutes residualsHydrogen DRI–EAFPotentially near-zero if electricity and H₂ are low-carbonPotentially ~90%+ lowerElectricity (electrolysis + EAF) + pelletsClean power price, electrolyser capex/efficiency, utilisation, pelletsNear-zero compatible primary steel; tight chemistry controlIron-ore briquettes in BF chainsIncremental improvement vs BF–BOFTypically single-digit % lowerStill coal/coke-basedBriquette availability, substitution rate, sinter/pellet balanceLower disruption than route replacement

### [2] Source ID: `b5301831-463b-49a9-bea6-69c7fef88287`

> Operational control: EAF-based routes offer faster start-up, flexible output, and fewer large process units.Transition options: Incremental measures—such as iron-ore briquettes in blast-furnace supply chains—can deliver near-term reductions where legacy assets continue to operate (Mathieson, 2025).DefinitionsBF–BOF: blast furnace followed by basic oxygen furnace; traditional ore-to-steel route.EAF: electric arc furnace; melts scrap and/or DRI using electricity.DRI: direct reduced iron; solid iron produced by reducing iron ore before melting.Hydrogen DRI: DRI produced using hydrogen as the reducing gas.Electrolysis: process that uses electricity to split water into hydrogen and oxygen.DR-grade pellets: iron ore pellets optimized for direct reduction performance.

### [3] Source ID: `702b74f9-37f7-4dc7-b1e4-ef8a51cb40c2`

> Carbon Emissions & Environmental ImpactHow much CO 2 does EAF route steel produce compared to BOF route steel?Scope 1 (direct) emissions from EAF steelmaking are approximately 0.2 tonnes CO₂ per tonne of steel compared to roughly 2.0 tonnes CO 2 per tonne for integrated BOF route steel—a reduction of about 90%. However, total emissions depend heavily on the electricity source for EAF operations and the scrap feedstock used. When Scope 2 (indirect) emissions from electricity generation are included, EAF steel powered by coal-fired electricity may produce 0.7-0.8 tonnes CO₂ per tonne, whilst EAF powered entirely by renewable electricity can achieve emissions below 0.3 tonnes CO₂ per tonne. The BOF route's high emissions stem primarily from blast furnace operations where metallurgical coal serves as both fuel and reducing agent. Use our Steel Production Emissions Calculator to model Scope 1 and Scope 2 emissions by process route, casting method, and product type. For comprehensive emissions data by process route, see our CO2 Emissions Analysis. The EAF route's low-carbon advantage depends heavily on scrap availability — see Steel Scrap & Recycling.

### [4] Source ID: `b5301831-463b-49a9-bea6-69c7fef88287`

> Hydrogen DRI–EAF: what it is and why it is future-proofHydrogen DRI–EAF is widely regarded as the most future-proof option for new, ore-based primary steel capacity aiming at near-zero emissions. It replaces carbon in the iron-reduction chemistry with hydrogen, producing water rather than CO₂ (IEA, 2020; Vogl et al., 2018).Step 1: Hydrogen production (electrolysis)Low-carbon hydrogen is commonly produced by splitting water using electricity:2H₂O → 2H₂ + O₂(Vogl et al., 2018)Inputs: water, electricity, electrolyser

### [5] Source ID: `65554701-052f-4a23-859c-f24350265b54`

>  17 of 46 Green H2, electrolysis, and CCUS could reduce steelmaking CO2 emissions by over 85% if implemented at scale 100% Green Hydrogen (H2) DRI-EAF Iron Ore Electrolysis Carbon Capture, Utilization, and Storage (CCUS) Description  Green hydrogen replaces natural gas as an iron ore reductant in DRI shaft; the rest of the process remains the same  Generates water as a byproduct instead of CO2  Two different processes are possible: Molten oxide electrolysis: High current runs through mixture of iron ore and liquid electrolyte to split ore into pure molten iron Electrowinning-EAF: Iron from iron ore is dissolved in acid. Iron-rich solution is then electrified to form pure solid iron  CCUS equipment can be added to existing steel-producing infrastructure to capture emitted CO2  Captured CO2 is then sequestered underground or reused 

### [6] Source ID: `4b43e37c-1622-48f8-ae78-e6b5010a6472`

> 7% CO2 20% CO2 Fines Lump & pellets Scope 3 boundary Metallurgical coal Iron ore Iron ore Blast furnace Steel converter Liquid steel Sinter plant DRI shaft furnace CO2 emissions from power supply CO2 Pellets Scope 3 boundary Natural gas Iron ore Electric arc furnace Liquid steel Calculation methodology We use typical industry parameters when modelling to consider the energy needed in each step of the steelmaking process relative to the grade of iron ore, flux materials and the corresponding volume of coke required. Our approach to calculating emissions from steelmaking attributes emissions to four elements of the integrated process: the production of coke, ore sintering, blast furnace operations and final steel conversion. 

### [7] Source ID: `ffa19d43-ac23-4758-91e6-abe0e6cb92bf`

> scrap-based EAF steelmakers. EAF steelmakers currently contribute 70% of total US crude steel production ► Average Scope 1 & 2 CO2 emissions for BOFs reached 1.67 t CO2 / tcs, of which 80% is associated with the BF ironmaking stage ► Coke rates in the BF and scrap rates in the BOF are the key emissions intensity differentiators between US BOFs ► Scope 1 & 2 emissions for all EAFs reached 0.37 t CO2 / tcs, of which 67% is associated with Scope 2 emissions (purchased electricity) ► The carbon intensity of local purchased electricity, which varies widely based on mill 

### [8] Source ID: `ffa19d43-ac23-4758-91e6-abe0e6cb92bf`

> 1.8 Scope 1 Scope 2 1.5 1.6 1.8 1.7 Brazil 0.0 US 0.0 Russia 0.0 0.0 Ukraine 1.5 1.6 1.71.8 Scope 1 Scope 2 Pig iron carbon intensities DATA: CRU US steelmaking Scope 1, 2 & 3 emissions: key metrics summary 14 Production level Mill type in the US US Scope 1 average t CO2 / t US Scope 2 average t CO2 / t US Scope 3 average t CO2 / t Total Scope 1+2+3 t CO2 / t Crude Steel BOF (Total) 1.64 0.03 0.44 2.11 EAF (Flat Products) 0.13 0.26 0.43 0.84 EAF (Long Products) 0.11 0.23 0.13 0.47 EAF (Total) 0.12 0.25 0.31 0.68 

### [9] Source ID: `702b74f9-37f7-4dc7-b1e4-ef8a51cb40c2`

> Green Steel Production Routes ComparisonProduction RouteCO₂ Emissions (tonnes per tonne steel)Technology MaturityKey AdvantagesKey ChallengesCost Premium (vs conventional BOF)Conventional BOF (Blast Furnace + Basic Oxygen Furnace)1.9–2.3 (Scope 1 + 2)Established technology Dominant route globally 70% of production• Proven reliability • High product quality • Established infrastructure • Low operating complexity• Very high emissions • Rising carbon costs • Stranded asset risk • Limited reduction pathwayBaseline Rising due to carbon pricingEAF with Scrap (Electric Arc Furnace + Grid Power)0.4–0.8 (varies with grid mix)Established technology Mature worldwide 30% of production• 60-75% lower emissions • Lower capital cost • Flexible operation • Uses recycled material• Scrap quality variability • Scrap supply constraints • Residual element build-up • Grid carbon dependency-10% to +5% Competitive with BOFEAF with Renewable Power (Electric Arc Furnace + Wind/Solar/Hydro)0.2–0.3 (minimal Scope 2)Proven technology Commercial deployment Growing rapidly• 85-90% emission reduction • Existing EAF infrastructure • Near-term deployable • Lower capital requirement• Scrap availability limits • Premium renewable power cost • Quality limitations • Can't serve all applications+€50–100/t Renewable power premiumH₂-DRI + EAF (Hydrogen Direct Reduced Iron + EAF)0.02–0.1 (near-zero with green H₂)Pilot/demonstration Commercial by 2026-2030 HYBRIT, H2GS leading• 95%+ emission reduction • High product quality • No scrap dependency • True "green steel"• Massive H₂ infrastructure needed • High capital cost ($1.5-2.5B) • Green H₂ supply constraints • Renewable power requirement+€100–200/t Current (declining to parity by 2030-35)BOF with CCS (Carbon Capture & Storage)0.2–0.5 (90% capture possible)Pilot stage Limited deployment Technical challenges• Extends BOF asset life • Uses existing infrastructure • 70-90% emission reduction • Avoids full plant rebuild• High energy penalty (15-20%) • CO₂ transport/storage needed • Economics uncertain • Still produces emissions+€80–150/t CCS costs + energy penaltyBOF with Biomass (Charcoal/Torrefied Wood Injection)1.5–1.8 (20-30% reduction)Emerging technology Limited commercial use Brazil leading• Renewable carbon source • Partial coal substitution • Existing BF compatible • Incremental approach• Limited emission reduction • Biomass sustainability concerns • Supply chain complexity • Only partial solution+€30–60/t Biomass cost premium

### [10] Source ID: `677f0a17-85dd-4b2e-840b-fbae7612e049`

> The primary advantage of the DRI-EAF route is that it eliminates the need for coking coal, reducing the overall carbon intensity of the steelmaking process. If natural gas is used, emissions from the DRI-EAF route (using reformed natural gas) are estimated between 1.50 – 1.70 tCO 2 per tonne of steel produced. If hydrogen is used, this figure can be reduced by as much as 95% 3.Addressing grid integration challengesH2-based DRI plants need a continuous supply of hydrogen. In the case of green hydrogen, the construction of a giga-watt scale electrolysis plant is required (if the hydrogen is not available via a nearby pipeline). This can present significant challenges for steel producers, particularly when it comes to connection to the high-voltage grid.

### [11] Source ID: `4a162255-eab6-4313-ae6c-edc3024a464b`

> Chỉ số Kỹ thuật & Phát thảiLộ trình Truyền thống (BF-BOF)Lộ trình Thép vụn (Scrap-EAF)Lộ trình Hoàn nguyên Khí tự nhiên (NG-DRI-EAF)Lộ trình Hoàn nguyên Hydro xanh (H2-DRI-EAF)Cường độ phát thải trực tiếp1,9 - 2,7 \text{tCO}_2/\text{t thép} [cite: 1, 4, 5]0,3 - 0,6 \text{tCO}_2/\text{t thép} [cite: 4]1,1 - 1,6 \text{tCO}_2/\text{t thép} [cite: 4]< 0,2 \text{tCO}_2/\text{t thép} [cite: 10, 13]Tiêu thụ điện năngThấp (~0,6 MWh/t)0,35 - 0,60 MWh/t [cite: 4]0,45 - 0,80 MWh/t [cite: 4]~3,48 MWh/t [cite: 4]Yêu cầu nguyên liệu chínhQuặng sắt và than cốc [cite: 4, 5]Thép vụn và điện sạch [cite: 4]Quặng viên cấp DR và khí thiên nhiên [cite: 4, 12]Quặng viên cấp DR và hydro xanh [cite: 4, 12]Độ nhạy cảm kinh tếGiá than cốc và quặng sắt [cite: 4]Giá điện và chất lượng thép vụn [cite: 4]Giá khí thiên nhiên và giá điện [cite: 4]Giá điện sạch và hiệu suất điện phân [cite: 4]

### [12] Source ID: `65554701-052f-4a23-859c-f24350265b54`

> an abundance of green electricity, which is required for both powering electrolysis and the production of green hydrogen – Assuming the current global electricity mix does not change, H2 DRI-EAF would have a decarbonization potential of only 60% instead of >85% when 100% green electricity is used  The 90% CO2 reduction for CCUS is a hypothetical best-case scenario, which at present has not been proven at scale 19 of 46 Steel decarbonization technologies, however, often come with a green premium and require large amounts of green energy 

### [13] Source ID: `4f899035-8b28-41ac-97b7-48c4d72bc028`

> Green Steel EconomicsUnderstanding the economic feasibility of low-carbon steel production is crucial for informed decision-making. Detailed below is a techno-economic analysis comparing the costs associated with different steel production methods. This assessment evaluates the financial implications of green scrap-EAF, green H 2-HBI-EAF and green H 2-DRI-EAF processes relative to the traditional BF-BOF route. 19Figure 2&3. BF-BOF & Scrap-EAF LCOS Bridge in Vietnam  Source: TA analysisIn the BF-BOF steel production process, the cost of fuel and reductants, primarily coal and natural gas, constitutes the largest share at approximately 37% of total expenses. This is followed by expenditures on iron ore, which account for about 28% of the total cost. Other costs, including OPEX and labour, make up around 12%, while CAPEX represents only 10% of total costs. Additionally, the reliance on self-generated electricity in the BF-BOF process keeps the cost of purchased electricity relatively low, at around 0.4%.

### [14] Source ID: `4a162255-eab6-4313-ae6c-edc3024a464b`

> \text{2H}_2\text{O} \rightarrow \text{2H}_2 + \text{O}_2 \quad (\text{Điện phân}) \text{Fe}_2\text{O}_3 + \text{3H}_2 \rightarrow \text{2Fe} + \text{3H}_2\text{O} \quad (\text{Hoàn nguyên})Về mặt tiêu thụ năng lượng, lộ trình \text{H}_2\text{-DRI-EAF} yêu cầu lượng điện năng cực kỳ lớn, chủ yếu phục vụ quá trình điện phân nước để thu khí hydro [cite: 4]. Một đánh giá kỹ thuật cho thấy lộ trình hydro này tiêu thụ khoảng 3,48 MWh điện năng trên mỗi tấn thép lỏng sản xuất, cao hơn nhiều so với mức 0,35 đến 0,60 MWh của lò hồ quang điện thông thường chạy bằng 100% thép vụn (Scrap-EAF) [cite: 4]. Tuy nhiên, do nguồn cung thép vụn sạch trên toàn cầu bị giới hạn và không thể đáp ứng hoàn toàn nhu cầu sản xuất các mác thép chất lượng cao, việc phát triển các nhà máy hoàn nguyên trực tiếp dùng quặng sắt cấp DR chất lượng cao (DR-grade pellets) kết hợp nạp liệu nóng vào lò EAF là hướng đi không thể đảo ngược đối với phân khúc thép nguyên sinh [cite: 4, 11, 12].

### [15] Source ID: `b5301831-463b-49a9-bea6-69c7fef88287`

> Because energy prices, feedstock availability, and carbon policies vary widely by region, outcomes differ by site and market (Rootzén & Johnsson, 2016).Electricity exposure by routeElectricity use provides a clear view of operational sensitivity for EAF-based routes:Scrap-EAF: commonly on the order of ~0.35–0.60 MWh per tonne of steelNatural gas DRI–EAF: often ~0.45–0.80 MWh per tonne, with additional gas energy used in the DRI plantHydrogen DRI–EAF: substantially higher electricity use because electrolysis dominates total energy demand; one assessment estimates ~3.48 MWh per tonne of liquid steel (Vogl et al., 2018; IEA, 2020)

### [16] Source ID: `835862c6-a3cb-43dd-802a-8f6b07b560bb`

> Các công nghệ như NG-DRI-EAF và H2-DRI-EAF bị hạn chế là phải sử dụng nguồn quặng chất lượng cao (chỉ có ~ 3 % trữ lượng trên thế giới). Ngược lại, các công nghệ như BF-BOF có thể sử dụng tất cả các loại quặng nhưng cơ bản là không giảm được phát thải CO 2. Sản xuất sắt bằng công nghệ MOE có thể sử dụng tất cả các loại quặng với tổng lượng sắt nhỏ hơn rất nhiều, đảm bảo rằng công nghệ này có tiềm năng để sử dụng toàn bộ trữ lượng quặng sắt trên thế giới.

### [17] Source ID: `d213bace-b883-4db4-a3a1-223d0676f965`

> Table 1. Pilot technologies for source-stage carbon reduction in BF-BOF long-process steelmaking. Table 1. Pilot technologies for source-stage carbon reduction in BF-BOF long-process steelmaking.Technology NameDescriptionIndustrial Maturity3R Carbon-Hydrogen BF Technology [ 9]Recirculates reducing gases from furnace gas and enhances reduction via carbon–hydrogen coupling, reducing coke consumptionPilot stage (partial demonstration)Top Gas Recycling and Full-Oxygen Smelting [ 10]Injects hydrogen-enriched gas after CO 2 separation and reduces coke ratio through full-oxygen blastDemonstration stage (under validation)Fluxed Pellets and Composite Iron Coke [ 11]Replaces traditional sinter with low-carbon burden to reduce flux demandSmall-scale applicationHydrogen-Blended Injection [ 12]Co-injects hydrogen with natural gas/pulverized coal to progressively replace fossil fuelsPilot stage (exploratory development)High-Grade Ore & Pellets [ 13]Reduces sintering energy consumption by adopting high-grade ore and pelletsGradual adoption (partial industrial use)Biomass Fuel Substitution [ 14]Substitutes coke breeze/anthracite with charcoal/biomass to reduce fossil carbon relianceLimited pilot trialsPlasma Blast Heating [ 15, 16]Enhances blast temperature using green electricity-driven plasma to lower coke demandDemonstration stage

### [18] Source ID: `f993e794-55aa-4feb-af28-d529dcc55198`

> PlayCBAM: A guide to Carbon Border Adjustment MechanismAI-generated audio24: 14 What is CBAM?The European Union's Carbon Border Adjustment Mechanism (CBAM) is a regulatory tool designed to ensure that carbon-intensive imported goods are subject to the same carbon costs as products manufactured within the EU. Its main goal is to prevent carbon leakage by applying a carbon price to imports of carbon-intensive goods from regions with less strict climate policies.CBAM entered its definitive phase on January 1, 2026. From this moment, compliance began for importers and certificate obligations apply.

### [19] Source ID: `4a162255-eab6-4313-ae6c-edc3024a464b`

> 
--------------------------------------------------------------------------------
Quy định Tài chính CBAM và Quản trị Phát thải các Phạm vi Scope 1, 2, 3Cơ chế điều chỉnh biên giới carbon của Liên minh Châu Âu (EU CBAM) đã bước vào giai đoạn tuân thủ tài chính bắt buộc kể từ ngày 1 tháng 1 năm 2026, đặt ra những yêu cầu nghiêm ngặt về đo lường và xác minh lượng phát thải carbon tích tụ trong hàng hóa nhập khẩu [cite: 17, 18, 19].Phân loại Ranh giới Phát thải trong Chuỗi Giá trị Sắt thépSự phân định ranh giới phát thải giữa ba phạm vi (Scope 1, 2, 3) đóng vai trò quyết định trong việc định giá nghĩa vụ thuế CBAM và các nghĩa vụ báo cáo liên quan [cite: 10].

### [20] Source ID: `454a46aa-1f42-4b8c-9e48-d51b8fd3a880`

> How can I calculate my CBAM certificate costs?The CBAM certificate costs depend on the number of certificates you need to purchase and the CBAM certificate price. In 2026, the CBAM certificate price will be set quarterly, and from 2027 onwards, it will be set weekly, always based on the average price of a European emissions trading certificate (EU ETS).The number of certificates can be calculated using the following formula:(Embedded Emissions − (CBAM Benchmark × Phase-in Factor) −Carbon Price Paid Overseas) × Quantity of Goods =

### [21] Source ID: `4a162255-eab6-4313-ae6c-edc3024a464b`

> Quy tắc Thực thi và Cách tính thuế CBAM từ năm 2026Trong giai đoạn thực hiện ban đầu từ năm 2026, CBAM áp dụng cơ chế tính toán và thực thi tài chính có độ chi tiết kỹ thuật cao [cite: 17, 18]:Chế độ tính toán phát thải trực tiếp và xử lý đặc biệt đối với Sintered Ore: CBAM chỉ áp dụng nghĩa vụ tài chính đối với lượng phát thải trực tiếp (Scope 1) đối với các sản phẩm sắt thép nhập khẩu thuộc Annex II [cite: 21, 22, 23]. Lượng điện tiêu thụ trong lò EAF để nấu chảy thép thô (phát thải Scope 2) tạm thời được miễn trừ tính phí nhằm tránh tính trùng thuế với cơ chế đền bù chi phí carbon gián tiếp của EU [cite: 23, 24]. Tuy nhiên, một ngoại lệ kỹ thuật quan trọng là quặng thiêu kết (Sintered Ore, mã CN 2601 12 00) [cite: 23]. Đối với quặng thiêu kết, cả phát thải trực tiếp và gián tiếp (Scope 2) đều phải được tính toán đầy đủ; khi quặng thiêu kết này được sử dụng làm tiền chất (precursor) cho các sản phẩm gang hoặc thép hạ nguồn tại một cơ sở khác, toàn bộ lượng phát thải gián tiếp tích tụ từ khâu này sẽ được kết chuyển lũy kế vào sản phẩm thép cuối cùng [cite: 23].Nghĩa vụ tích lũy phát thải từ tiền chất (Precursor Emissions): Nhà nhập khẩu các sản phẩm thép phức tạp bắt buộc phải khai báo lượng phát thải tích tụ từ các tiền chất đầu vào, bao gồm gang lỏng (pig iron), sắt hoàn nguyên trực tiếp (DRI), quặng thiêu kết, hợp kim sắt và thép thô [cite: 23]. Toàn bộ dữ liệu này phải được chứng thực từ cơ sở sản xuất thượng nguồn, trong khi thép phế liệu sau tiêu dùng được gán mức phát thải bằng không [cite: 23].Lộ trình cắt giảm hạn ngạch miễn phí và Cơ chế phạt giá trị mặc định: Nghĩa vụ tài chính thực tế của CBAM được điều chỉnh tương ứng với tốc độ cắt giảm hạn ngạch phát thải miễn phí của hệ thống EU ETS đối với các nhà sản xuất nội địa [cite: 17, 25, 26]. Trong năm 2026 và 2027, hạn ngạch miễn phí chỉ bị cắt giảm 2,5% mỗi năm, đồng nghĩa với việc nhà nhập khẩu chỉ phải trả khoảng 2,5% tổng nghĩa vụ thuế carbon tích tụ [cite: 17, 25]. Lượng chứng chỉ CBAM cần surrender sẽ tăng vọt khi hạn ngạch miễn phí bị loại bỏ hoàn toàn vào năm 2034 [cite: 25, 26]. Đối với các doanh nghiệp không cung cấp được dữ liệu phát thải thực tế được xác minh bởi bên thứ ba được EU công nhận, hệ thống sẽ áp dụng mức phạt dựa trên giá trị mặc định có cộng thêm hệ số markup lũy tiến cực kỳ punitive: tăng thêm 10% trong năm 2026, 20% trong năm 2027, và 30% từ năm 2028 trở đi nhằm triệt tiêu hoàn toàn động cơ trốn tránh khai báo dữ liệu [cite: 17, 27, 28].Các quy định vận hành hành chính: Doanh nghiệp nhập khẩu có tổng khối lượng sản phẩm thuộc phạm vi CBAM dưới 50 tấn mỗi năm được miễn trừ nghĩa vụ nộp chứng chỉ để giảm gánh nặng hành chính (ngoại trừ mặt hàng hydro và điện) [cite: 21, 22, 29]. Từ năm 2027, các nhà khai báo CBAM được ủy quyền phải duy trì số lượng chứng chỉ CBAM trong tài khoản đăng ký tối thiểu đạt mức 50% tổng lượng phát thải tích tụ tính đến cuối mỗi quý [cite: 18, 21].

### [22] Source ID: `98b3a2f2-4b0e-4458-9849-77edd53b0a0c`

> Layer three, the 2026 number: smaller than the headlines suggest. Because EU producers still receive free ETS allowances during the phase-in, the CBAM bill is discounted by the same amount. For 2026, roughly 97.5% of free allocation remains in place, so only about 2.5% of the gross carbon cost is actually payable. On a gross default charge of, say, €80 per tonne of product, the net 2026 obligation is close to €2. That is the figure that gives false comfort.Because the trap is the trajectory. That 2.5% share was scheduled to climb to roughly 48.5% by 2030 and to 100% by 2034 as free allocation is withdrawn. The same shipment that costs €2 net today was on track to cost the full €80 within a decade. The 2026 invoice is a preview, not the price.

### [23] Source ID: `1b1ea1be-8f16-4f15-b4ff-7f4076208ef8`

> Embedded Emissions CalculationProper calculation of direct and indirect emissions is key to accurate CBAM reporting and cost management.Key elements include:Direct emissions from production processesIndirect emissions from electricity consumption, where requiredIndependent verification under accredited bodiesDefault values applied where verified data is unavailableIf verified emissions data is not provided, default values may apply, which may increase certificate liability.50-Tonne De Minimis ThresholdSmaller importers benefit from exemptions under the 50-tonne annual threshold, which reduces the administrative burden.

### [24] Source ID: `8765005a-140d-4a76-9226-576f515c72df`

> Which emissions scopes does EU CBAM cover?CBAM covers direct emissions (Scope 1) and indirect emissions from electricity (Scope 2) for steel products imported into the EU. For the steel sector specifically, both are included because electricity-intensive processes like EAF steelmaking have significant Scope 2 emissions. If you cannot provide verified actual emissions data, CBAM applies default values based on the exporting country's average or the worst-performing 10% of EU installations — which are intentionally punitive to incentivize actual measurement. Accurate measurement almost always results in lower CBAM costs than defaults.

### [25] Source ID: `0879fd75-5954-4cd4-bc94-160c6f1a21cd`

> CBAM financial obligations are live and escalating:Since January 1, 2026, companies importing iron, steel, aluminium, cement, fertilizers, or hydrogen into the EU must declare embedded emissions with their first filing due September 30, 2027. The penalty structure for relying on default values rather than actual supplier PCF data creates direct financial incentives for supply chain carbon data collection:2026: 10% markup on default values2027: 20% markup2028 and beyond: 30%+ markupCompanies without supplier-specific carbon data face escalating costs that make PCF data collection an immediate ROI calculation rather than a compliance exercise.

### [26] Source ID: `e041df6a-9370-43eb-b2df-28f7bbdab291`

> €65–80Current EU ETS carbon price per tonne CO₂ (Q1 2026 range)1.6–2.1tTypical CO₂ emissions per tonne of BF-BOF steel (varies by installation)€100–170Indicative CBAM cost per tonne of BF-BOF steel exported to EU€100Penalty per undeclared tonne of CO₂ — no cap, plus admin finesCritical: These costs increase annually as EU ETS free allowances phase out between 2026–2034. By full phase-out, steel exporters will bear the full EU carbon price on every tonne exported. Producers with lower emission intensities — EAF, DRI-based, or those using renewable energy — gain significant competitive advantage. Calculate your CBAM cost exposure

### [27] Source ID: `e041df6a-9370-43eb-b2df-28f7bbdab291`

> How are CBAM certificate prices determined?CBAM certificate prices are directly linked to EU ETS allowance auction prices. For the 2026 compliance year, certificate prices reflect the quarterly average of 2026 EU ETS auction closing prices. From 2027 onward, prices reflect weekly averages. As of early 2026, EU ETS prices range approximately €65–80 per tonne of CO₂. These prices are expected to increase over time as EU ETS free allowances phase out between 2026 and 2034. Steel producers should model their CBAM exposure under various carbon price scenarios. See certificate cost modeling

### [28] Source ID: `104e601d-72e0-45c6-94ca-6b71c6ace1bb`

> Ngành Công NghiệpPhát Thải Nhúng Ước Tính (tCO2e/sản lượng mẫu)Tác Động Chi Phí CBAM tại EU (Giai đoạn 2026 - Mức quota 25%)Tác Động Chi Phí CBAM (Giai đoạn áp dụng 100% quota)Sản xuất Thép (Mẫu: 10.000 tấn)~7.180 tCO2e (Do tiêu thụ điện lò EAF lớn)~17,95 tỷ đồng/năm~71,8 tỷ đồng/nămSản xuất Nhôm (Mẫu: 5.000 tấn)~40.100 tCO2e (Cường độ tiêu thụ điện cực cao)~25 tỷ đồng/năm~100 tỷ đồng/nămSản xuất Xi măng (Mẫu: 50.000 tấn)Phụ thuộc vào công nghệ nung Clinker~28 tỷ đồng/năm~112 tỷ đồng/năm*Ghi chú: Ước tính dựa trên giá chứng chỉ CBAM 100 EUR/tCO2e theo lộ trình siết chặt của EU ETS (dữ liệu tham chiếu).*36.

### [29] Source ID: `5d0d8b8f-5cae-4079-84e4-801207f50f0c`

> To measure how much carbon costs add to production—what we call the carbon-cost intensity—we use a price of USD100 per metric ton of carbon dioxide, which is roughly what companies pay in the EU's carbon market today. We multiply this price by the amount of carbon dioxide to get the carbon-cost intensity. So, for example, if a steel plant outside of the EU emits twice as much carbon dioxide as the average EU steel plant, it will face much higher carbon costs when selling to the bloc. This difference in carbon-cost intensity determines the change in competitiveness: who wins or loses under CBAM.

### [30] Source ID: `4a4bb2e7-f948-4818-9430-ab8af9d29a0c`

> IndexKey TakeawaysA Turning Point for Raw Material Supply ChainsA Directive Redefined: What CSDDD Now Looks LikeWhy CSDDD Still Drives Traceability in Raw MaterialsHow Other EU Frameworks Reinforce CSDDDWhat This Means for Procurement Teams in Metals and MiningHow Metalshub Supports CSDDD-Aligned TraceabilityCSDDD Makes Transparency a Strategic RequirementReferencesIndexKey TakeawaysThe CSDDD introduces a legally binding duty to identify, prevent, and mitigate human rights and environmental risks in raw material supply chains.

### [31] Source ID: `4a4bb2e7-f948-4818-9430-ab8af9d29a0c`

> CSDDD introduces a binding system of human rights and environmental due diligence that extends across a company's activities and those of its business partners. It establishes a duty to understand where materials come from, under which conditions they are produced, and how risks are mitigated. The scope and technical detail remain under negotiation, yet its strategic implications for metals and mining supply chains are already clear. The EU is signalling that visibility over origin, production practices, and potential impacts is essential for responsible procurement.

### [32] Source ID: `4a4bb2e7-f948-4818-9430-ab8af9d29a0c`

> For more information, visit our Procurement Solution page or explore our free white paper on Sustainable Procurement for Steel Mills.CTA to download sustainaility white paper for steel mills Download White PaperReferencesFirst omnibus package to relax CSDDD, CSRD and EU taxonomy obligations – KPMG-LawEU-Parlament beschließt finale Verhandlungsposition zu CSRD und CSDDD – KleebergSustainability reporting and due diligence: MEPs back simplification changes | News | European ParliamentCorporate Sustainability Due Diligence Directive (CSDDD) – CSR

### [33] Source ID: `8765005a-140d-4a76-9226-576f515c72df`

> Steel production is directly responsible for approximately 2.6 gigatonnes of CO₂ annually — roughly 7% of global emissions — with an additional 1.0 Gt from the sector's electricity usage. For steel companies navigating EU CBAM (fully operational January 2026), ETS free allowance phase-out, Science Based Targets initiative (SBTi) commitments, and buyer Scope 3 procurement requirements, accurate emissions measurement across all three scopes isn't optional — it's the foundation of every compliance obligation and commercial relationship. In 2023 the global steel industry average was 1.92 tonnes CO₂ per tonne of crude steel cast. But this average masks enormous variation: US EAF steelmakers average 0.37 tCO₂/t crude steel (Scope 1+2), while traditional BF-BOF steelmakers average 1.67 tCO₂/t — a 78% difference. At the hot-rolled phase including Scope 3, traditional steelmakers emit 2.4 tCO₂/t versus 0.83 tCO₂/t for EAF producers — 189% higher. WorldSteel's 2025 Sustainability Indicators now include upstream Scope 3 emissions from mining operations (including methane from metallurgical coal mining) for the first time, expanding coverage to align with the GHG Protocol and ISO standards. 75 steel companies contributed data across 19 indicators. For steel companies, measuring emissions accurately across Scope 1 (direct process emissions), Scope 2 (purchased electricity and energy), and Scope 3 (upstream raw materials and downstream product use) determines CBAM certificate costs, SBTi pathway compliance, customer qualification, and access to green steel premium markets. iFactory's carbon accounting platform helps steel companies measure, track, report, and reduce emissions across all three scopes with automated data collection, regulatory-aligned calculation methodologies, and audit-ready documentation. Book a free demo and get your emissions measurement right.

### [34] Source ID: `7f86ec2d-9492-470c-9894-f66d59970817`

> Impact of green steel premium on car pricesThe automotive industry accounts for 12% of global steel demand. The additional cost attributed to using green H 2-DRI-EAF steel in passenger vehicles—known as the green premium— is aligned with studies that estimated automotive sector as a likely first mover for green steel procurement and demonstrates minimal impact on overall vehicle pricing. For example, in the U.S., when the price of H 2 is at $5/kg, the green premium for steel produced via green H 2-DRI-EAF, compared to the traditional BF-BOF methods, stands at approximately $226 per ton steel. Assuming on average 0.9 ton of steel used in a passenger car, this translates to an additional cost of about $203 per passenger car, which represents a less than 1% price increase on the average price of passenger car in the U.S. (over $40,000), maintaining affordability and market stability. Future projections suggest that with H 2 costs potentially reducing to $1.4/kg, the green premium could effectively disappear, making green H 2-DRI-EAF steel economically comparable to conventionally produced steel. With the introduction of carbon price/credit, the green premium for H 2-DRI-EAF steel can substantially drop even further.

### [35] Source ID: `6c7c4874-9683-4c98-88a8-94b95da3ab0e`

> Similarly, the economic impact of using green H2-DRI-EAF steel in building construction is quite minor compared to traditional BF-BOF steelmaking. For example, in China, at a hydrogen cost of $5/kg, the green premium for steel is about $225 per ton. This translates into an additional cost of roughly $563 for a 50 m² new residential unit (assuming 50 kg of steel per m²), which is a small portion of the overall cost of purchasing such a residential unit. Future reductions in hydrogen costs or the implementation of carbon pricing could also reduce or eliminate this green premium, potentially making green H2-DRI-EAF steel a cost-effective alternative for construction in China and other countries. The construction industry (building and infrastructure) accounts for 52% of global steel demand.

### [36] Source ID: `a51b8d28-1e7f-4486-97b0-21923b25e17a`

> 1 / 1For example, in auto manufacturing the steel in a combustion engine vehicle is responsible for approximately 23% of the related carbon emissions and the conversion to 100% green steel would increase the vehicle price by only about 0.3% to 0.7%, or less than €250 for a midsize vehicle.In appliances, steel is responsible for approximately 25% of the carbon emissions related to the production of a washing machine; the conversion to 100% green steel would increase the machine's price by only some 2% to 4%, or less than €12.

### [37] Source ID: `ffa19d43-ac23-4758-91e6-abe0e6cb92bf`

> Hot-Rolled Products BOF (Total) 1.86 0.07 0.46 2.40 EAF (Flat Products) 0.17 0.34 0.45 0.97 EAF (Long Products) 0.18 0.29 0.13 0.61 EAF (Total) 0.19 0.32 0.32 0.83 Slab rerollers 0.04 0.05 2.50 2.59 Emissions Analysis 1.6 0.3 0.2 0.3 0.4 0.4 0.3 EAFs (Longs) 0.1 0.1 0.0 EAFs (Total)BOFs (Total) 0.1 EAFs (Flats) 0.1 2.1 0.8 0.5 0.7 1.9 0.3 0.3 0.3 0.5 0.5 0.3 2.5 0.2 BOFs (Total) EAFs (Flats) EAFs (Longs) EAFs (Total) Slab rerollers 0.2 0.1 0.2 0.1 0.0 0.1 2.4 1.0 0.6 0.8 Hot-rolled steel carbon intensities 2.6 

### [38] Source ID: `8765005a-140d-4a76-9226-576f515c72df`

> 04Buyer Scope 3 RequirementsAutomotive OEMs, construction firms, and infrastructure developers setting Scope 3 reduction targets require verified emissions data from steel suppliers. Your Scope 1+2 emissions become your customer's Scope 3. Suppliers who can't provide product-level emissions data lose qualification for green procurement programs.05Green Steel Premium MarketsVerified low-emission steel commands premiums of €20–80+ per tonne in European markets. Accessing these premiums requires product-level emissions data calculated with primary data and aligned with RMI, WorldSteel, or ResponsibleSteel methodologies. Accurate measurement isn't just compliance — it's revenue.

### [39] Source ID: `702b74f9-37f7-4dc7-b1e4-ef8a51cb40c2`

> Is there a green steel premium?The green steel premium varies significantly across markets and transactions, with quoted figures ranging from €50 per tonne to €200 per tonne in European markets. However, this wide variation reflects the reality that the green steel market remains extremely thin, with limited transaction volumes making reliable price discovery challenging. Premium levels depend heavily on product specification, certification requirements, contract volumes, and buyer urgency. Early procurement agreements for green steel from projects like H2 Green Steel and HYBRIT have commanded premiums at the upper end of this range, whilst some EAF producers using renewable electricity claim smaller premiums of €50-100 per tonne. The absence of standardised definitions and transparent spot markets means premiums are negotiated bilaterally, with large automotive or construction companies securing better terms than smaller buyers. As production volumes scale and competition increases, premiums are expected to compress toward the lower end of the range by 2028-2030.

### [40] Source ID: `6c7c4874-9683-4c98-88a8-94b95da3ab0e`

> Impacts on the End-use SectorsAs green steel incurs a cost premium, this directly affects the material costs of downstream use sectors. This report has analyzed the potential cost increases related to three notable downstream sectors: automobile, construction, and shipping, using steel produced via the H2-DRI-EAF method compared to conventional methods for those sectors.The global automotive industry accounts for 12% of global steel demand. The impact of the green steel premium on car prices demonstrates a minimal overall effect. For example, in Japan, when the price of H2 is $5/kg, the additional cost per ton of steel using the green H2-DRI-EAF method is about $231, leading to an extra $208 per passenger car, which represents less than a 1% increase on the average passenger car price of $28,000 in Japan. Projections indicate that with potential reductions in H2 costs to $1.3/kg, the green premium could vanish, making green H2-DRI-EAF prices comparable to traditional BF-BOF steel costs in Japan. Moreover, the introduction of a carbon pricing mechanism could further decrease this green premium, enhancing the affordability and market viability of using green H2-DRI-EAF steel in automotive manufacturing. Similar results in terms of the impact of H2 price and carbon pricing on green steel premiums in auto manufacturing were observed in other countries studied, as shown later in this report.

### [41] Source ID: `6cec731f-1d1f-4d5d-9aa3-2b842bf88070`

> Premium offtakersStegra found willing offtakers, largely in the premium end of the European automotive industry, customers for whom a 25% green premium on an electric vehicle's steel components would make business sense. For the end consumer, an overall price increase of around €500 on a product that, for the luxury brands, retails anywhere between €100,000 to €250,000 is not considered material. At the point of manufacturing, carbon costs for grey steel have been increasingly shown as an itemised line on invoices since 2023. Additionally, in line with the introduction of CBAM, from 2026, European steelmakers will start paying for emissions.

### [42] Source ID: `7f86ec2d-9492-470c-9894-f66d59970817`

> Impact of green steel premium on building construction costThe construction industry (building and infrastructure) accounts for 52% of global steel demand. In the context of building construction in the U.S., the economic effect of adopting green steel produced by H 2-DRI-EAF route can be considered minimal when compared to conventional BF-BOF steelmaking route. Using the green H2-DRI-EAF route, the additional cost of steel at a H 2 price of $5/kg is approximately $226 per ton of steel, translating into an added expense of about $565 for a 50 m 2 residential building unit (assuming 50 kg steel per m 2 used for low to mid-rise residential building). This represents a small fraction of the total cost of a residential building. In addition, with future reductions in H 2 cost or the introduction of carbon pricing, the green premium could diminish or even disappear, making green H2-DRI-EAF an economically viable alternative for building construction in the U.S..

### [43] Source ID: `7f86ec2d-9492-470c-9894-f66d59970817`

> The reason for this relatively higher green steel premium as a share of the total cost for shipbuilding compared to cars and buildings is higher share of steel cost in the shipbuilding cost. Over 95% of a ship consists of steel. Anticipated reductions in H 2 costs in the future could nullify this green premium, aligning the costs of green H 2-DRI-EAF steel with those of traditional BF-BOF steelmaking. Moreover, the introduction of carbon pricing could further reduce the green premium costs, enhancing the financial attractiveness of adopting green H 2-DRI-EAF steel in the maritime sector.

### [44] Source ID: `7f86ec2d-9492-470c-9894-f66d59970817`

> Impact of green steel premium on shipbuilding costIncorporating green H 2-DRI-EAF steel into shipbuilding shows a small cost increase for shipbuilding. While there are many types of ships in the global market. This study focused on bulk carrier ships which are built in large numbers every year around the world. For example, to build an average 40,000 DWT (Deadweight tonnage) bulk ship, approximately 13,200 tons of steel are needed. If green H 2-DRI-EAF at $5/kg H 2 is used in the U.S. to build this ship, the additional cost would be about $ 2.98 million per ship in the U.S.. Considering the average cost of a new 40,000 DWT bulk ship is over $30 million, this represents less than 10% increase in the ship's price for the U.S..

### [45] Source ID: `c7f3ff40-de82-4bd9-b88b-4e1e08fdab72`

> 1 2 3 3 9 13 2 1 1 1 1 7 1 3 4 1 11 2 1 6 26 South America North America Africa Australia Asia Europe 3 6 7 9 17 57 R&D partnership Demonstration Plant Pilot Full scale 17% 0% 33% 23% 2% 8% Legend: Capacity of demonstration and fullscale plants as a % of total steel capacity in region  Key Takeaways There is currently little incentive for Asian steelmakers to decarbonise Policy settings are insufficient to decarbonise the 73% of global steel emissions in Asia Asian steelmakers’ willingness-to-pay for low-emissions iron is currently too limited to catalyse investment in steel abatement. Exceptionally low-carbon prices see DRI adoption as a cost to the business in a highly competitive industry (Figure 10). In contrast to Asian markets, the combination of ETS and CBAM has insulated Europe from this dynamic while closing the cost gap for green steel. As carbon prices rise, the cost premium for H2 DRI green steel falls dramatically. In fact, the European dynamic may create a short-term green premium for DRI steel. 

### [46] Source ID: `4a4bb2e7-f948-4818-9430-ab8af9d29a0c`

> Nicholas Bolton Purchasing Manager, Eurac Poole LtdCSDDD Makes Transparency a Strategic RequirementCSDDD is evolving, yet its influence on supply chain transparency is already reshaping expectations in the metals and mining sector. The directive places responsibility on companies to understand the origin of their materials and how risks associated with them are addressed. Recent simplification proposals may reduce the number of companies directly subject to these obligations, yet the strategic direction remains unchanged.

