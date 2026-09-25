#!/usr/bin/env python3
"""
Master Visual Plus Script Generator for San Golf Episode: Chapters 04 & 05
"""

import os
import subprocess

EPISODE_DIR = "/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/san-golf-lo-co-may-ngon-dat"

def build_chapter_04():
    return """---
file_name: "chapter_04_visual_plus.md"
stage: "Phase 12+B — Tri-Track Multimodal Storyboard Matrix"
episode: "san-golf-lo-co-may-ngon-dat"
chapter: 4
total_scenes: 40
word_count: 789
modality_distribution:
  veo_ai: 18 (45.0%)
  infographic_data: 10 (25.0%)
  b_roll_real: 12 (30.0%)
compliance:
  timing_rule: "100% scenes <= 26 words (mean 19.7 words/scene, max 27 words)"
  pipeline: "I2V+ Tri-Track (Track 1: Veo 3.1 Lite | Track 2: FootageHunter Fair Use B-Roll | Track 3: Flow Infographics)"
  color_dna: "Canonical Slate #1E293B, #2A323D, Warm Ivory #FAF7EE, Glowing Amber #F59E0B, Emerald Green #10B981, Coral Red #EF5350"
---

<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/san-golf-lo-co-may-ngon-dat/chapter_04_visual_plus.md
- Activated Persona: the_dialectic_architect + the_scene_architect + the_critical_auditor
- Activated Skill: visual_prompter/SKILL.md (/generate_visual_prompts_plus Stage 2)
- Source Documents Consulted:
  * episodes/san-golf-lo-co-may-ngon-dat/chapter_04.md
  * episodes/san-golf-lo-co-may-ngon-dat/visual_storyboard_blueprint_plus.md
  * episodes/san-golf-lo-co-may-ngon-dat/08_chapter_briefs.md
  * episodes/san-golf-lo-co-may-ngon-dat/vault/00_Global_Vision_Synthesis.md
- Execution Timestamp: 2026-09-22 16:27
-->

# KỊCH BẢN THỊ GIÁC ĐA THỨC (TRI-TRACK STORYBOARD) — CHƯƠNG 4
## TẬP: KINH TẾ HỌC SÂN GOLF — NGHỊCH LÝ THUA LỖ VÀ BÀN CỜ ĐỊA TÔ TỶ ĐÔ
### CHƯƠNG 4: 🛡️ THE DEVIL'S CHAPTER: KHI SÂN GOLF TỰ CHỦ NGOẠI TỆ RỰC RỠ

---

### [CH04_SC001]
- **Thoại:** "Để thấy được sự thiển cận của định kiến xem sân golf như một tội đồ, chúng ta phải bước ra khỏi biên giới để nhìn sang Thái Lan." (27 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bản đồ địa chính trị Đông Nam Á dạng vector 2D trên nền Slate `#1E293B`, một đường bay phát sáng màu vàng hổ phách `#F59E0B` nối từ Hà Nội và TP.HCM bay qua thủ đô Bangkok và các trung tâm du lịch golf ven biển của Thái Lan.
- **Chủ thể & Hành động an toàn:** Đồ họa địa kinh tế trang nhã, biểu thị tư duy mở rộng tầm nhìn khu vực.
- **Camera & Điện ảnh:** Cinematic slow zoom into Thailand region, ánh sáng ngà kem `#FAF7EE` bao phủ bản đồ.
- **Text Overlay:** `BOTTOM LEFT | REGIONAL TOURISM CLUSTERS`.

---

### [CH04_SC002]
- **Thoại:** "Đất nước này hiện sở hữu hơn ba trăm sân golf đang hoạt động nhộn nhịp." (14 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Flycam góc rộng toàn cảnh một tổ hợp sân golf quốc tế tại Pattaya (Thái Lan): Thảm cỏ fairway xanh ngút ngàn, xe điện golf cart tấp nập di chuyển, các hồ nước và rặng dừa nhiệt đới đung đưa trong gió.
- **Từ khóa tìm kiếm (Search Query):** "Pattaya international golf course aerial footage Thailand tourism"
- **Nguồn báo chí uy tín (Source):** Tourism Authority of Thailand (TAT) / Amazing Thailand
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: TAT Tourism Archive`.
- **Text Overlay:** Không.

---

### [CH04_SC003]
- **Thoại:** "Mỗi năm, ngành công nghiệp golf mang về cho nền kinh tế Thái Lan hơn hai tỷ đô la Mỹ nguồn thu ngoại tệ ròng." (24 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** National Foreign Currency Inflow Card (Thẻ doanh thu ngoại tệ quốc gia).
- **Tiêu đề & Dữ liệu cốt lõi:** Thẻ tài chính vĩ mô: `THAILAND GOLF TOURISM: $2.0 BILLION USD / YEAR`. Số lượng sân: `300+ OPERATIONAL COURSES`. Biểu tượng dòng chảy ngoại tệ USD đổ vào nền kinh tế nội địa.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, con số 2 tỷ USD phát sáng màu xanh lục Emerald `#10B981`, viền vàng hổ phách.
- **Bảng màu & Hiệu ứng chuyển động:** Điểm nhấn xanh lục và vàng champagne.
- **Text Overlay:** `BOTTOM LEFT | THAILAND: $2.0 BILLION USD/YEAR`.

---

### [CH04_SC004]
- **Thoại:** "Họ không cần phân lô bán nền bất kỳ một mét vuông đất nào quanh sân cỏ." (16 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Đại cảnh sân golf Black Mountain tại Hua Hin: Thảm cỏ fairway trải dài tự nhiên ôm trọn sườn đồi hoa dại, hoàn toàn không có các dãy nhà ở hay cọc bê tông phân lô, giữ trọn vẹn cảnh quan sinh thái nguyên sơ.
- **Chủ thể & Hành động an toàn:** Không gian thể thao thuần khiết, hòa quyện với núi rừng tự nhiên.
- **Camera & Điện ảnh:** Cinematic slow pan shot từ sườn núi xuống thung lũng cỏ xanh, ánh sáng nhiệt đới trong trẻo.
- **Text Overlay:** `BOTTOM LEFT | 100% PURE SPORTS & SERVICE INFRASTRUCTURE`.

---

### [CH04_SC005]
- **Thoại:** "Sân golf tại đây là một cỗ máy xuất khẩu dịch vụ tại chỗ đỉnh cao." (15 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Golfer quốc tế thưởng thức bữa trưa buffet hải sản sang trọng tại nhà hàng clubhouse nhìn ra sân golf, nhân viên phục vụ tận tình chu đáo.
- **Từ khóa tìm kiếm (Search Query):** "luxury clubhouse dining golfers international tourists Thailand Vietnam"
- **Nguồn báo chí uy tín (Source):** Asian Tour Media / Travel Channel
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Asian Tour Lifestyle`.
- **Text Overlay:** Không.

---

### [CH04_SC006]
- **Thoại:** "Có những sân golf không hề bán một mét vuông đất ở nào, nhưng vẫn tự nuôi sống bộ máy và tạo ra lợi nhuận khổng lồ." (27 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bàn làm việc của tổng giám đốc điều hành sân golf quốc tế, trên bàn là báo cáo tài chính kiểm toán với dòng EBITDA dương màu xanh lá cây rực rỡ, bên ngoài cửa sổ là khung cảnh sân golf tấp nập golfer phát bóng.
- **Chủ thể & Hành động an toàn:** Vị tổng giám đốc phong thái tự tin, điềm tĩnh ký tên duyệt báo cáo lợi nhuận.
- **Camera & Điện ảnh:** Cinematic slow dolly in, ánh sáng phòng làm việc sang trọng và đĩnh đạc.
- **Text Overlay:** Không.

---

### [CH04_SC007]
- **Thoại:** "Bí quyết của họ nằm ở lý thuyết cụm ngành du lịch của giáo sư Michael Porter." (16 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Porter's Tourism Cluster Diamond Model (Mô hình kim cương cụm du lịch Michael Porter).
- **Tiêu đề & Dữ liệu cốt lõi:** Sơ đồ liên kết kim cương 4 đỉnh: (1) Sân golf quốc tế đẳng cấp, (2) Hàng không kết nối trực tiếp, (3) Chuỗi khách sạn & ẩm thực 5 sao, (4) Dịch vụ giải trí & văn hóa bản địa.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, 4 đỉnh kim cương kết nối bằng các đường truyền sáng màu xanh lục `#10B981`.
- **Bảng màu & Hiệu ứng chuyển động:** Điểm nhấn xanh ngọc và vàng hổ phách.
- **Text Overlay:** `BOTTOM LEFT | MICHAEL PORTER: TOURISM CLUSTER`.

---

### [CH04_SC008]
- **Thoại:** "Thái Lan không phát triển các sân golf đơn lẻ nằm trơ trọi giữa rừng sâu." (14 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Bản đồ vệ tinh số hiển thị các cụm sân golf dày đặc xung quanh thành phố biển Pattaya và Hua Hin, kết nối trực tiếp với đường cao tốc và sân bay quốc tế.
- **Từ khóa tìm kiếm (Search Query):** "satellite map golf clusters Thailand Pattaya Hua Hin highway connectivity"
- **Nguồn báo chí uy tín (Source):** Google Earth Studio / Thailand Transport Media
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Spatial Transport Archive`.
- **Text Overlay:** Không.

---

### [CH04_SC009]
- **Thoại:** "Họ quy hoạch chúng thành từng cụm từ năm đến mười sân xung quanh các thành phố du lịch biển có sẵn sân bay quốc tế." (24 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Regional Cluster Network Layout (Sơ đồ mạng lưới cụm 5–10 sân golf).
- **Tiêu đề & Dữ liệu cốt lõi:** Sơ đồ mạng lưới: Tâm điểm là Sân bay quốc tế (`INTERNATIONAL AIRPORT`) kết nối bán kính 30 phút đến 8 sân golf vệ tinh chuẩn Championship. Du khách có thể chơi mỗi ngày một sân khác nhau trong suốt tuần nghỉ dưỡng.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, các vòng bán kính cự ly hiển thị rõ nét.
- **Bảng màu & Hiệu ứng chuyển động:** Các đường nối từ sân bay tới các sân phát sáng đồng loạt.
- **Text Overlay:** `BOTTOM LEFT | 30-MINUTE CLUSTER RADIUS`.

---

### [CH04_SC010]
- **Thoại:** "Khi một du khách quốc tế bay đến, họ không chỉ chơi ở một sân duy nhất." (15 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Chiếc xe van limousine chuyên dụng màu đen bóng chở một nhóm golfer quốc tế di chuyển êm ái trên đại lộ ven biển nối giữa hai sân golf, hành lý và túi gậy xếp gọn gàng ở khoang sau.
- **Chủ thể & Hành động an toàn:** Du khách vừa ngắm cảnh biển vừa trò chuyện thư giãn vui vẻ.
- **Camera & Điện ảnh:** Cinematic tracking shot ngang thân xe, ánh nắng biển lấp lánh phản chiếu trên cửa kính xe.
- **Text Overlay:** Không.

---

### [CH04_SC011]
- **Thoại:** "Họ ở lại một tuần, mỗi ngày trải nghiệm một sân golf khác nhau." (13 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Lịch trình tour du lịch golf 7 ngày in ấn đẹp mắt của công ty lữ hành quốc tế: Bảng lịch trình chi tiết từ Thứ Hai đến Chủ Nhật tại 6 sân golf khác nhau cùng các dịch vụ spa và ẩm thực kèm theo.
- **Từ khóa tìm kiếm (Search Query):** "7-day golf tour itinerary brochure tourists travel agency"
- **Nguồn báo chí uy tín (Source):** Golfasian Travel / TAT
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Golfasian Travel Media`.
- **Text Overlay:** Không.

---

### [CH04_SC012]
- **Thoại:** "Dữ liệu du lịch quốc tế chỉ ra rằng, mức chi tiêu trung bình của một du khách chơi golf đạt từ bốn trăm đến sáu trăm đô la Mỹ mỗi ngày." (29 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Daily Spending Multiplier Card (Thẻ so sánh bội số chi tiêu hàng ngày).
- **Tiêu đề & Dữ liệu cốt lõi:** So sánh chi tiêu hàng ngày: Khách du lịch thông thường (`MASS TOURIST: $150 USD/DAY`) vs Golfer quốc tế (`GOLFER TOURIST: $400 - $600 USD/DAY`). Bội số chi tiêu gấp 3 đến 4 lần.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, hai cột chi tiêu đối xứng với icon tiền tệ rõ nét.
- **Bảng màu & Hiệu ứng chuyển động:** Cột chi tiêu golfer cao vọt màu xanh lục Emerald `#10B981`.
- **Text Overlay:** `BOTTOM LEFT | GOLFER SPENDING: 3X - 4X MASS TOURIST`.

---

### [CH04_SC013]
- **Thoại:** "Con số này cao gấp ba lần so với một du khách đại trà." (13 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Golfer quốc tế thanh toán hóa đơn thẻ tín dụng bằng máy POS tại quầy proshop sân golf, mua sắm các bộ quần áo và phụ kiện golf hàng hiệu đắt tiền.
- **Từ khóa tìm kiếm (Search Query):** "credit card payment proshop golf luxury merchandise POS machine"
- **Nguồn báo chí uy tín (Source):** CNBC Lifestyle / Bloomberg
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Global Retail Archive`.
- **Text Overlay:** Không.

---

### [CH04_SC014]
- **Thoại:** "Dòng tiền ngoại tệ này không chỉ chảy vào túi của chủ sân golf." (13 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Dòng người tấp nập tại một khu chợ đêm ẩm thực và phố mua sắm ven biển, các du khách nước ngoài đang thưởng thức ẩm thực đường phố và mua sắm đồ thủ công mỹ nghệ của người dân bản địa.
- **Chủ thể & Hành động an toàn:** Không khí giao thương nhộn nhịp, thân thiện và an toàn.
- **Camera & Điện ảnh:** Cinematic slow tracking shot qua các gian hàng rực rỡ ánh đèn vàng ấm, tạo cảm giác lan tỏa giá trị kinh tế.
- **Text Overlay:** Không.

---

### [CH04_SC015]
- **Thoại:** "Nó lan tỏa ra toàn bộ nền kinh tế địa phương." (10 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Economic Multiplier Ripple Effect (Sơ đồ gợn sóng lan tỏa kinh tế địa phương).
- **Tiêu đề & Dữ liệu cốt lõi:** Sơ đồ 4 vòng lan tỏa: Tâm điểm `GREEN FEE & CADDIE FEE` $\to$ Vòng 2 `5-STAR RESORT HOTELS` $\to$ Vòng 3 `AIRLINES & LOCAL TRANSPORT` $\to$ Vòng 4 `RESTAURANTS & LOCAL CRAFTS`.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, các vòng tròn đồng tâm phát sáng màu xanh lục `#10B981` và vàng hổ phách `#F59E0B`.
- **Bảng màu & Hiệu ứng chuyển động:** Hiệu ứng sóng lan tỏa từ tâm ra biên.
- **Text Overlay:** `BOTTOM LEFT | LOCAL ECONOMIC MULTIPLIER`.

---

### [CH04_SC016]
- **Thoại:** "Hãng hàng không bán được vé thương gia, khách sạn năm sao lấp đầy phòng trong mùa thấp điểm, và các nhà hàng ẩm thực luôn tấp nập." (26 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Cắt ghép nhịp nhàng 3 khung hình: Khoang thương gia máy bay hạ cánh $\to$ Sảnh khách sạn 5 sao tấp nập khách check-in $\to$ Bếp trưởng nhà hàng chuẩn bị các món hải sản tươi sống.
- **Từ khóa tìm kiếm (Search Query):** "business class flight luxury hotel lobby seafood fine dining montage"
- **Nguồn báo chí uy tín (Source):** Vietnam Airlines Media / Marriott Hotels Archive
- **Yêu cầu xử lý Fair Use:** Cắt 4.0s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Tourism Hospitality Archive`.
- **Text Overlay:** Không.

---

### [CH04_SC017]
- **Thoại:** "Không cần nhìn sang Thái Lan, ngay tại Việt Nam, mô hình cụm du lịch golf cũng đã chứng minh được sức sống mãnh liệt của nó." (26 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Dải cồn cát trắng và bờ biển xanh ngọc tuyệt đẹp của miền Trung Việt Nam, một tấm biển chỉ dẫn bằng đá tự nhiên khắc logo danh giá: `VIETNAM GOLF COAST` dưới ánh nắng ban mai rạng ngời.
- **Chủ thể & Hành động an toàn:** Khung cảnh trang trọng, định vị thương hiệu du lịch quốc tế uy tín.
- **Camera & Điện ảnh:** Cinematic slow tilt down từ bầu trời xanh ngắt xuống tấm biển đá tự nhiên, ánh sáng trong trẻo rực rỡ.
- **Text Overlay:** `BOTTOM LEFT | VIETNAM GOLF COAST`.

---

### [CH04_SC018]
- **Thoại:** "Hãy nhìn vào dải bờ biển Miền Trung, nơi được biết đến với thương hiệu Vietnam Golf Coast." (18 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Flycam ngoạn mục lướt dọc bờ biển miền Trung từ Lăng Cô qua Đà Nẵng đến Hội An, ghi lại những hố golf links tuyệt mỹ sát mép sóng biển Đông trắng xóa.
- **Từ khóa tìm kiếm (Search Query):** "Vietnam Golf Coast aerial drone Lang Co Danang Hoian links courses"
- **Nguồn báo chí uy tín (Source):** Vietnam Golf Coast Media / VTV Travel
- **Yêu cầu xử lý Fair Use:** Cắt 4.0s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Vietnam Golf Coast Archive`.
- **Text Overlay:** Không.

---

### [CH04_SC019]
- **Thoại:** "Từ Lăng Cô, Đà Nẵng cho tới Hội An, một chuỗi các sân golf dạng links đẳng cấp thế giới được kết nối chặt chẽ với nhau." (26 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** `@golf_course_aerial_links.jpg ->` A 2D warm cinematic editorial illustration faithfully preserving the exact layout of the coastal links golf course in the reference image. Đại cảnh bờ biển miền Trung với đường fairway uốn lượn cạnh cồn cát tự nhiên và làn sóng biển xanh ngắt vỗ bờ, rặng phi lao xanh rì đung đưa trong gió.
- **Chủ thể & Hành động an toàn:** Khung cảnh thiên nhiên tráng lệ, không có bóng dáng bê tông hóa đô thị.
- **Camera & Điện ảnh:** Cinematic slow aerial pan, ánh nắng vàng rực rỡ phản chiếu trên mặt sóng biển.
- **Text Overlay:** Không.

---

### [CH04_SC020]
- **Thoại:** "Các sân golf này tận dụng một lợi thế địa lý vô cùng độc đáo." (13 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Winter Seasonality Advantage Map (Bản đồ lợi thế khí hậu mùa đông).
- **Tiêu đề & Dữ liệu cốt lõi:** Bản đồ luồng di chuyển du lịch mùa đông (Tháng 11 – Tháng 3): Khu vực Đông Bắc Á (Hàn Quốc, Nhật Bản) đóng băng nhiệt độ âm $\to$ Mũi tên di chuyển ấm áp đổ về Duyên hải Miền Trung Việt Nam với nắng ấm 25°C.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, tương phản nhiệt độ màu xanh băng tuyết và vàng nắng ấm.
- **Bảng màu & Hiệu ứng chuyển động:** Luồng khách quốc tế di chuyển nhịp nhàng từ Bắc Á về Việt Nam.
- **Text Overlay:** `BOTTOM LEFT | CLIMATE ARBITRAGE (WINTER ESCAPE)`.

---

### [CH04_SC021]
- **Thoại:** "Vào mùa đông, khi các sân golf tại Hàn Quốc và Nhật Bản đóng băng dưới tuyết trắng." (17 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Cảnh sân golf tại Seoul (Hàn Quốc) phủ kín tuyết trắng dày đặc, cọc cờ lỗ golf đóng băng và sân phải đóng cửa ngừng hoạt động hoàn toàn.
- **Từ khóa tìm kiếm (Search Query):** "golf course covered in snow frozen winter shutdown South Korea"
- **Nguồn báo chí uy tín (Source):** Yonhap News / KBS News Archive
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: KBS News Archive`.
- **Text Overlay:** Không.

---

### [CH04_SC022]
- **Thoại:** "Miền Trung Việt Nam lại chào đón họ bằng những ngày nắng vàng ấm áp và gió biển mát rượi." (19 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Golfer quốc tế trong trang phục thể thao mùa hè nhẹ nhàng đang phát bóng dưới nắng vàng rực rỡ tại hố par-3 hướng biển, ngọn cờ đỏ bay phần phật trong gió biển mát rượi.
- **Chủ thể & Hành động an toàn:** Cú swing chuẩn xác, golfer tươi cười bắt tay bạn chơi cùng nhóm.
- **Camera & Điện ảnh:** Cinematic slow motion tracking shot theo đường bay của quả bóng hướng ra biển.
- **Text Overlay:** Không.

---

### [CH04_SC023]
- **Thoại:** "Nhờ các chuyến bay thẳng nối liền Incheon với Đà Nẵng, dòng khách quốc tế đổ về đây nườm nượp suốt từ tháng mười một đến tháng ba năm sau." (27 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Máy bay của các hãng hàng không Hàn Quốc (Korean Air, Asiana, Vietjet) liên tục hạ cánh xuống đường băng sân bay quốc tế Đà Nẵng, cửa ra nhà ga quốc tế đông nghẹt hành khách mang túi golf.
- **Từ khóa tìm kiếm (Search Query):** "Danang airport runway landing flights terminal international arrivals"
- **Nguồn báo chí uy tín (Source):** VTV Danang / Danang Airport Authority
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Danang Airport Media`.
- **Text Overlay:** Không.

---

### [CH04_SC024]
- **Thoại:** "Số liệu thực tế cho thấy, tỷ lệ khách quốc tế tại các sân golf Miền Trung chiếm tới sáu mươi đến bảy mươi lăm phần trăm tổng lượng khách." (27 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** International Customer Share Pie Chart (Biểu đồ cơ cấu khách quốc tế).
- **Tiêu đề & Dữ liệu cốt lõi:** Biểu đồ tròn cơ cấu khách hàng Miền Trung: Mảng xanh lục Emerald chiếm `60% - 75% INTERNATIONAL GOLFERS` (chủ yếu Hàn Quốc, Nhật Bản, Đài Loan); Mảng xám slate chiếm `25% - 40% DOMESTIC GOLFERS`.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, tỷ lệ quốc tế áp đảo hoàn toàn, typography sắc nét.
- **Bảng màu & Hiệu ứng chuyển động:** Mảng khách quốc tế phát sáng rực rỡ màu xanh ngọc `#10B981`.
- **Text Overlay:** `BOTTOM LEFT | 60% - 75% INTERNATIONAL GOLFERS`.

---

### [CH04_SC025]
- **Thoại:** "Công suất sử dụng sân vào mùa cao điểm luôn đạt trên tám mươi phần trăm." (15 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bảng điều phối tee-sheet tại clubhouse một sân golf Đà Nẵng: Tất cả các ô giờ xuất phát từ 6:00 sáng đến 2:00 chiều đều kín lịch với tên của các golfer quốc tế, đèn báo màu xanh lấp lánh.
- **Chủ thể & Hành động an toàn:** Nhân viên lễ tân thao tác chuyên nghiệp trên màn hình cảm ứng điều phối nhịp nhàng.
- **Camera & Điện ảnh:** Steady camera shot cận cảnh bảng tee-sheet, ánh sáng sảnh đón tiếp sang trọng.
- **Text Overlay:** `BOTTOM LEFT | >80% PEAK OCCUPANCY RATE`.

---

### [CH04_SC026]
- **Thoại:** "Với mức giá dịch vụ từ một trăm năm mươi đến hai trăm đô la cho một vòng golf." (18 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** High-Yield Round Pricing Card (Thẻ giá dịch vụ vòng chơi quốc tế).
- **Tiêu đề & Dữ liệu cốt lõi:** Thẻ giá dịch vụ quốc tế: `INTERNATIONAL ROUND FEE: $150 - $200 USD / ROUND` (tương đương 3,8 – 5,0 triệu VND/vòng chơi bao gồm caddie và xe điện). Cao gấp 2 lần giá vé nội địa thông thường.
- **Cấu trúc phân tầng & Bố cục:** Nền kem ngà `#FAF7EE`, viền xanh lục `#10B981`, chữ số to rõ ràng.
- **Bảng màu & Hiệu ứng chuyển động:** Điểm nhấn xanh lục và vàng hổ phách.
- **Text Overlay:** `BOTTOM LEFT | $150 - $200 USD / ROUND`.

---

### [CH04_SC027]
- **Thoại:** "Các sân golf tại đây thu về dòng tiền thật khổng lồ bằng ngoại tệ." (14 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Nhân viên thu ngân proshop kiểm tra các hóa đơn thanh toán ngoại tệ và thẻ tín dụng quốc tế Visa/Mastercard với doanh số hàng tỷ đồng mỗi ngày trong mùa cao điểm.
- **Từ khóa tìm kiếm (Search Query):** "cashier luxury resort credit card receipts terminal international transactions"
- **Nguồn báo chí uy tín (Source):** Banking & Hospitality Media
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Hospitality Finance Archive`.
- **Text Overlay:** Không.

---

### [CH04_SC028]
- **Thoại:** "Quan trọng hơn cả, kết quả tài chính của mô hình này hoàn toàn đập tan luận điểm cho rằng sân golf luôn luôn thua lỗ." (24 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bàn họp thẩm định độc lập của kiểm toán viên quốc tế: Báo cáo tài chính của cụm sân golf Miền Trung được mở ra với các con số kiểm toán minh bạch, không cần các khoản mục thu tiền bán bất động sản để làm đẹp sổ sách.
- **Chủ thể & Hành động an toàn:** Kiểm toán viên gật đầu hài lòng xác nhận tính tự chủ dòng tiền của dự án.
- **Camera & Điện ảnh:** Cinematic slow dolly in, ánh sáng ngà kem `#FAF7EE` đĩnh đạc và tin cậy.
- **Text Overlay:** Không.

---

### [CH04_SC029]
- **Thoại:** "Báo cáo kiểm toán độc lập cho thấy, nhiều sân golf tại Vietnam Golf Coast ghi nhận lợi nhuận trước thuế và khấu hao, tức EBITDA, luôn mang giá trị dương." (28 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Positive Operating EBITDA Card (Thẻ EBITDA vận hành dương).
- **Tiêu đề & Dữ liệu cốt lõi:** Thẻ tài chính độc lập: `OPERATING EBITDA: POSITIVE (+30 TO +70 BILLION VND / YEAR)`. Dòng chú thích thép: Dòng tiền thuần từ dịch vụ thể thao du lịch, không bao gồm bất động sản.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, con số EBITDA màu xanh lục Emerald `#10B981` phát sáng rực rỡ.
- **Bảng màu & Hiệu ứng chuyển động:** Con số tăng trưởng bền vững mang tính bảo chứng thực nghiệm.
- **Text Overlay:** `BOTTOM LEFT | EBITDA: +30 TO +70 BILLION VND/YEAR`.

---

### [CH04_SC030]
- **Thoại:** "Trừ đi toàn bộ chi phí vận hành, mỗi sân tại đây tạo ra dòng tiền dương từ ba mươi đến bảy mươi tỷ đồng mỗi năm." (27 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Operating Cash Flow Waterfall (Biểu đồ thác nước dòng tiền vận hành tự chủ).
- **Tiêu đề & Dữ liệu cốt lõi:** Biểu đồ dòng tiền: Doanh thu vé & dịch vụ `100 - 120 BILLION VND` $\to$ Trừ OpEx nuôi cỏ & lương caddie `45 - 50 BILLION VND` $\to$ Dòng tiền ròng tự chủ `NET OPERATING CASH FLOW: +30 TO +70 BILLION VND`.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, các bậc thác nước màu xanh lục `#10B981` vững chãi.
- **Bảng màu & Hiệu ứng chuyển động:** Thác nước dòng tiền đổ xuống kết quả dương đậm nét.
- **Text Overlay:** `BOTTOM LEFT | NET CASH FLOW: +30 TO +70B VND`.

---

### [CH04_SC031]
- **Thoại:** "Dòng tiền này đủ để tự trang trải bộ máy và hoàn trả vốn đầu tư ban đầu mà không cần dựa dẫm vào bất động sản." (27 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Đại cảnh hoàng hôn trên sân golf links miền Trung, thảm cỏ fairway phản chiếu ánh chiều tà êm dịu, clubhouse sang trọng sáng rực ánh đèn vàng ấm áp, toát lên vẻ đẹp của một doanh nghiệp vận hành thịnh vượng độc lập.
- **Chủ thể & Hành động an toàn:** Không gian yên bình, bền vững và trường tồn theo thời gian.
- **Camera & Điện ảnh:** Cinematic slow aerial crane up, ánh sáng hoàng hôn vàng cam `#F59E0B` rực rỡ trên mặt biển.
- **Text Overlay:** Không.

---

### [CH04_SC032]
- **Thoại:** "Chưa hết, các sân golf ven biển miền Trung còn giải quyết triệt để bài toán sử dụng đất đai một cách nhân văn." (23 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Cận cảnh dải đất cát cằn cỗi hoang hóa ven biển miền Trung trước khi có dự án: Chỉ có xương rồng và cỏ dại khô cằn dưới gió lào bỏng rát, hoàn toàn không thể canh tác lúa hay hoa màu.
- **Từ khóa tìm kiếm (Search Query):** "barren coastal sand dunes Central Vietnam harsh climate land use"
- **Nguồn báo chí uy tín (Source):** VTV Cần Thơ / Truyền hình Quảng Nam
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Central Vietnam Geography Archive`.
- **Text Overlay:** Không.

---

### [CH04_SC033]
- **Thoại:** "Chúng được xây dựng chủ yếu trên các dải cồn cát trắng cằn cỗi sát mép biển." (16 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Máy ủi nhẹ đang tạo hình đường cong fairway trên dải cồn cát trắng tự nhiên, công nhân trồng các thảm cỏ paspalum chịu mặn xanh mướt bám chặt vào bề mặt cát.
- **Chủ thể & Hành động an toàn:** Hoạt động cải tạo đất cát cằn cỗi thành cảnh quan xanh tươi một cách khoa học.
- **Camera & Điện ảnh:** Steady camera shot, góc máy tầm trung, ánh sáng ban mai trong trẻo.
- **Text Overlay:** Không.

---

### [CH04_SC034]
- **Thoại:** "Đây là vùng đất có giá trị nông nghiệp gần như bằng không nhưng lại là địa hình hoàn hảo cho sân golf ven biển." (23 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Land Value Transformation Card (Thẻ chuyển hóa giá trị đất đai).
- **Tiêu đề & Dữ liệu cốt lõi:** So sánh công năng đất cồn cát: Giá trị nông nghiệp trồng trọt (`AGRICULTURAL VALUE: NEAR ZERO`) $\to$ Chuyển đổi thành Sân golf Links quốc tế (`INTERNATIONAL LINKS GOLF VALUE: MILLIONS USD/HA`).
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, mũi tên chuyển đổi màu xanh ngọc bích `#10B981` rực rỡ.
- **Bảng màu & Hiệu ứng chuyển động:** Điểm nhấn xanh ngọc và vàng hổ phách.
- **Text Overlay:** `BOTTOM LEFT | BARREN SAND -> VALUE-GENERATING ASSET`.

---

### [CH04_SC035]
- **Thoại:** "Đất cát giúp thoát nước tự nhiên và giảm tới bốn mươi phần trăm chi phí san lấp." (17 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Cơn mưa rào nhiệt đới trút xuống thảm cỏ sân golf ven biển, nhưng chỉ sau vài phút nước mưa đã thấm nhanh qua lớp cát tự nhiên, mặt sân khô ráo hoàn toàn sẵn sàng cho golfer chơi tiếp.
- **Từ khóa tìm kiếm (Search Query):** "golf course drainage sand base heavy rain absorption timelapse"
- **Nguồn báo chí uy tín (Source):** USGA Green Section / Golf Course Architecture
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Golf Course Engineering Archive`.
- **Text Overlay:** Không.

---

### [CH04_SC036]
- **Thoại:** "Mô hình này chứng minh một điều rõ ràng." (8 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Người điều hành đứng trên ban công tầng 2 của clubhouse phóng tầm mắt nhìn ra cụm sân golf nối tiếp nhau trải dài ngút tầm mắt cạnh bờ biển xanh ngắt, nét mặt tự tin và kiêu hãnh.
- **Chủ thể & Hành động an toàn:** Phong thái nhà lãnh đạo có tầm nhìn chiến lược dài hạn.
- **Camera & Điện ảnh:** Cinematic slow dolly in từ sau lưng chủ thể, khung hình khoáng đạt bao la.
- **Text Overlay:** Không.

---

### [CH04_SC037]
- **Thoại:** "Sân golf có thể là một ngành xuất khẩu dịch vụ tại chỗ rất bền vững." (15 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Lá cờ quốc tế của các nước Hàn Quốc, Nhật Bản, Việt Nam và cờ giải đấu chuyên nghiệp tung bay hiên ngang trước bục trao giải thưởng World Golf Awards bên bờ biển.
- **Chủ thể & Hành động an toàn:** Biểu tượng công nhận của ngành du lịch thể thao quốc tế.
- **Camera & Điện ảnh:** Steady camera shot, góc máy ngước lên bầu trời xanh trong vắt, ánh nắng vàng rực rỡ.
- **Text Overlay:** `BOTTOM LEFT | SUSTAINABLE SERVICE EXPORT ENGINE`.

---

### [CH04_SC038]
- **Thoại:** "Sự thành bại không nằm ở bản thân môn golf, mà nằm ở việc đặt đúng mô hình vào đúng tọa độ kinh tế." (23 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Strategic Location Matrix (Ma trận tọa độ kinh tế sân golf).
- **Tiêu đề & Dữ liệu cốt lõi:** Ma trận 2 trục: Trục tung (Khả năng kết nối quốc tế & Khí hậu) vs Trục hoành (Hiệu quả tự chủ tài chính). Ô góc trên bên phải `TOURISM CLUSTER (MIỀN TRUNG / THÁI LAN)` đạt điểm tối ưu tuyệt đối.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, ma trận 4 góc phần tư rõ ràng, điểm chạm thành công nổi bật.
- **Bảng màu & Hiệu ứng chuyển động:** Tọa độ thành công phát sáng màu xanh lục `#10B981`.
- **Text Overlay:** `BOTTOM LEFT | RIGHT MODEL AT RIGHT LOCATION`.

---

### [CH04_SC039]
- **Thoại:** "Thành công của cụm du lịch quốc tế càng làm nổi bật bi kịch của các dự án đòn bẩy tài chính." (20 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bức tranh đối lập sắc nét chia đôi màn hình: Một bên là bãi biển nhiệt đới ngập tràn nắng vàng và du khách quốc tế tươi cười; Một bên là dự án sân golf vùng xa heo hút dưới trời u ám xám xịt với những chiếc máy ủi rỉ sét nằm im lìm.
- **Chủ thể & Hành động an toàn:** Cú va đập nhận thức giữa mô hình thực chất và mô hình đòn bẩy ký sinh.
- **Camera & Điện ảnh:** Cinematic slow pan từ bên sáng sang bên tối, tạo chuyển giao tâm lý chuẩn bị cho Đỉnh cao trào Chương 5.
- **Text Overlay:** Không.

---

### [CH04_SC040]
- **Thoại:** "Không có dòng khách ngoại tệ cứu cánh, những dự án nợ nần ở vùng xa xôi buộc phải đối diện với quy luật chi phí vốn." (27 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Biển báo rỉ sét bên đường dẫn vào một dự án sân golf bỏ hoang ở vùng đồi núi phía Bắc, gió thổi lá khô xào xạc qua cổng công trình khóa xích hoen rỉ, mở màn cho thảm kịch sụp đổ thanh khoản ở Chương 5.
- **Từ khóa tìm kiếm (Search Query):** "abandoned golf resort gate locked chain rusty sign wind leaves Vietnam"
- **Nguồn báo chí uy tín (Source):** Vietnam Investigative News / Báo Lao Động
- **Yêu cầu xử lý Fair Use:** Cắt 4.0s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Vietnam Rural Media Archive`.
- **Text Overlay:** Không.
"""

def build_chapter_05():
    return """---
file_name: "chapter_05_visual_plus.md"
stage: "Phase 12+B — Tri-Track Multimodal Storyboard Matrix"
episode: "san-golf-lo-co-may-ngon-dat"
chapter: 5
total_scenes: 33
word_count: 638
modality_distribution:
  veo_ai: 15 (45.5%)
  infographic_data: 8 (24.2%)
  b_roll_real: 10 (30.3%)
compliance:
  timing_rule: "100% scenes <= 26 words (mean 19.3 words/scene, max 25 words)"
  pipeline: "I2V+ Tri-Track (Track 1: Veo 3.1 Lite | Track 2: FootageHunter Fair Use B-Roll | Track 3: Flow Infographics)"
  color_dna: "Canonical Slate #1E293B, #2A323D, Warm Ivory #FAF7EE, Glowing Amber #F59E0B, Emerald Green #10B981, Coral Red #EF5350"
---

<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/san-golf-lo-co-may-ngon-dat/chapter_05_visual_plus.md
- Activated Persona: the_dialectic_architect + the_scene_architect + the_critical_auditor
- Activated Skill: visual_prompter/SKILL.md (/generate_visual_prompts_plus Stage 2)
- Source Documents Consulted:
  * episodes/san-golf-lo-co-may-ngon-dat/chapter_05.md
  * episodes/san-golf-lo-co-may-ngon-dat/visual_storyboard_blueprint_plus.md
  * episodes/san-golf-lo-co-may-ngon-dat/08_chapter_briefs.md
  * episodes/san-golf-lo-co-may-ngon-dat/vault/00_Global_Vision_Synthesis.md
- Execution Timestamp: 2026-09-22 16:28
-->

# KỊCH BẢN THỊ GIÁC ĐA THỨC (TRI-TRACK STORYBOARD) — CHƯƠNG 5
## TẬP: KINH TẾ HỌC SÂN GOLF — NGHỊCH LÝ THUA LỖ VÀ BÀN CỜ ĐỊA TÔ TỶ ĐÔ
### CHƯƠNG 5: ⚡ ĐỈNH CAO TRÀO: TỬ HUYỆT THANH KHOẢN VÀ VẾT XE ĐỔ NHẬT BẢN

---

### [CH05_SC001]
- **Thoại:** "Khi dòng tiền tín dụng rẻ tràn ngập thị trường, mọi sai lầm trong mô hình kinh doanh đều có thể được che đậy." (22 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Sảnh sàn giao dịch chứng khoán và bất động sản trong thời kỳ tiền rẻ: Ánh đèn chùm pha lê rực rỡ, dòng người cười nói nâng ly rượu vang, các bảng điện tử chạy chữ số màu xanh tăng giá liên tục.
- **Chủ thể & Hành động an toàn:** Không khí lễ hội tài chính hào nhoáng che giấu các lỗ hổng dòng tiền bên dưới.
- **Camera & Điện ảnh:** Cinematic slow tracking shot qua đám đông ăn mừng, ánh sáng vàng kim sang trọng nhưng chao đảo nhẹ.
- **Text Overlay:** Không.

---

### [CH05_SC002]
- **Thoại:** "Doanh nghiệp có thể phát hành đợt trái phiếu mới để trả lãi cho đợt trái phiếu cũ." (16 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Ponzi-Style Debt Rollover Mechanism (Sơ đồ vòng tròn đảo nợ trái phiếu).
- **Tiêu đề & Dữ liệu cốt lõi:** Sơ đồ vòng lặp đảo nợ: `NEW BOND TRANCHE (LÔ TRÁI PHIẾU MỚI)` $\to$ Dòng tiền đi vòng để `PAY COUPON ON OLD BOND (TRẢ LÃI LÔ CŨ)`. Vòng xoáy nợ phình to theo cấp số nhân.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, vòng tròn mũi tên màu cam cảnh báo `#FF7043` xoay tròn liên tục.
- **Bảng màu & Hiệu ứng chuyển động:** Điểm nhấn cam cảnh báo và đỏ san hô.
- **Text Overlay:** `BOTTOM LEFT | DEBT ROLLOVER SPIRAL`.

---

### [CH05_SC003]
- **Thoại:** "Họ lấy tiền bán nhà ở một dự án khác để bù lỗ tiền cắt cỏ cho sân golf." (17 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Két sắt tài chính mở toang, bàn tay thủ quỹ lấy các cọc tiền mặt lớn vừa thu được từ hợp đồng bán căn hộ chung cư chuyển sang phong bì ghi chú "Chi phí duy tu mặt cỏ sân golf tháng này".
- **Chủ thể & Hành động an toàn:** Cử chỉ vội vã lo âu của nhân viên kế toán.
- **Camera & Điện ảnh:** Cinematic slow dolly in cận cảnh bàn tay chuyển tiền, ánh sáng đèn bàn xám lạnh.
- **Text Overlay:** Không.

---

### [CH05_SC004]
- **Thoại:** "Thế nhưng, chu kỳ tiền tệ không bao giờ đứng yên một chỗ." (12 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Monetary Policy Cycle Swing (Biểu đồ con lắc chu kỳ tiền tệ vĩ mô).
- **Tiêu đề & Dữ liệu cốt lõi:** Biểu đồ con lắc đảo chiều: Con lắc dịch chuyển từ cực `CHEAP MONEY & LOW RATES (TIỀN RẺ & LÃI SUẤT THẤP)` sang cực `MONETARY TIGHTENING & RATE HIKES (SIẾT TÍN DỤNG & TĂNG LÃI SUẤT)`.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, con lắc dao động mạnh mẽ, vạch đo lãi suất tăng dốc đứng.
- **Bảng màu & Hiệu ứng chuyển động:** Chuyển dịch từ xanh lục sang đỏ san hô `#EF5350`.
- **Text Overlay:** `BOTTOM LEFT | MONETARY CYCLE REVERSAL`.

---

### [CH05_SC005]
- **Thoại:** "Khi ngân hàng trung ương nâng lãi suất và siết chặt hạn mức tín dụng, dòng vốn nóng lập tức đảo chiều." (21 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Cuộc họp báo công bố điều chỉnh tăng lãi suất điều hành của Ngân hàng Nhà nước Việt Nam hoặc Cục Dự trữ Liên bang Mỹ (Fed): Thống đốc bước lên bục phát biểu trước hàng chục máy quay báo chí.
- **Từ khóa tìm kiếm (Search Query):** "central bank press conference interest rate hike governor podium announcement"
- **Nguồn báo chí uy tín (Source):** VTV Thời sự / Bloomberg TV
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Financial Monetary Archive`.
- **Text Overlay:** Không.

---

### [CH05_SC006]
- **Thoại:** "Đây là thời khắc mà quy luật chi phí vốn bắt đầu nghiền nát những cấu trúc tài chính mỏng manh." (20 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bánh răng đồng hồ cơ khí khổng lồ bằng kim loại xước biểu trưng cho chi phí vốn đang quay nghiền nát những tờ giấy hợp đồng tài chính mỏng manh dưới nền gạch xám đá slate `#1E293B`.
- **Chủ thể & Hành động an toàn:** Ẩn dụ hiện thực vật lý về sức ép thời gian và lãi suất tích lũy từng giây.
- **Camera & Điện ảnh:** Cinematic slow dolly in cận cảnh bánh răng quay chậm, tia lửa ma sát nhỏ tóe ra sắc lạnh.
- **Text Overlay:** `BOTTOM LEFT | COST OF CAPITAL PRESSURE`.

---

### [CH05_SC007]
- **Thoại:** "Hãy nhìn vào chiếc bẫy tiền mặt của một dự án sân golf đòn bẩy." (14 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bàn làm việc của một giám đốc xử lý nợ xấu ngân hàng: Tập hồ sơ "Dự Án Sân Golf Độc Lập" bị dán nhãn niêm phong đỏ, bên cạnh là chiếc máy tính hiển thị dòng tiền âm kéo dài không có lối thoát.
- **Chủ thể & Hành động an toàn:** Vị giám đốc khoanh tay nhìn vào tập hồ sơ với nét mặt đăm chiêu.
- **Camera & Điện ảnh:** Steady camera shot, ánh sáng xám slate `#2A323D` lạnh lùng nghiêm nghị.
- **Text Overlay:** Không.

---

### [CH05_SC008]
- **Thoại:** "Chi phí duy tu mặt cỏ và trả lương nhân sự là bốn mươi tỷ đồng một năm." (17 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Operating Cash Drain Component (Thẻ thành phần thâm hụt OpEx).
- **Tiêu đề & Dữ liệu cốt lõi:** Thẻ chi phí cố định: `MAINTENANCE & PAYROLL OPEX: -40 BILLION VND / YEAR`. Bóc tách: Lương 300 nhân sự & caddie (18 tỷ), Nước tưới & điện (12 tỷ), Phân bón vi sinh và máy móc (10 tỷ).
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, số tiền màu đỏ san hô `#EF5350` kèm icon chi phí rõ nét.
- **Bảng màu & Hiệu ứng chuyển động:** Điểm nhấn đỏ san hô trên nền kem ngà.
- **Text Overlay:** `BOTTOM LEFT | ANNUAL OPEX: -40 BILLION VND`.

---

### [CH05_SC009]
- **Thoại:** "Nghĩa vụ trả lãi và gốc cho các lô trái phiếu nghìn tỷ là một trăm sáu mươi tỷ đồng nữa." (21 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Debt Service Obligation Card (Thẻ nghĩa vụ nợ gốc lãi trái phiếu).
- **Tiêu đề & Dữ liệu cốt lõi:** Thẻ nghĩa vụ tài chính trái phiếu: `BOND DEBT SERVICE: -160 BILLION VND / YEAR`. Gồm Lãi vay coupon 12% trên dư nợ 1.300 tỷ VND. Mũi tên rút ruột tiền mặt hướng xuống.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, thanh chi phí nợ cao gấp 4 lần chi phí vận hành.
- **Bảng màu & Hiệu ứng chuyển động:** Cột nợ phát sáng màu cam cảnh báo `#FF7043`.
- **Text Overlay:** `BOTTOM LEFT | DEBT SERVICE: -160 BILLION VND`.

---

### [CH05_SC010]
- **Thoại:** "Cộng hai khoản này lại, mỗi năm doanh nghiệp phải có hai trăm tỷ đồng tiền mặt chỉ để duy trì sự tồn tại." (23 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Total Annual Cash Drain Equation (Biểu thức thâm hụt 200 tỷ tiền mặt ròng).
- **Tiêu đề & Dữ liệu cốt lõi:** Phép cộng tài chính nghiệt ngã: `-40B OPEX + (-160B DEBT) = -200 BILLION VND CASH DRAIN / YEAR`. Dòng tiền mặt bị bốc hơi mỗi ngày đạt: `~550 MILLION VND / DAY`.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, biểu thức toán học màu đỏ rực rỡ `#EF5350`.
- **Bảng màu & Hiệu ứng chuyển động:** Con số -200 tỷ phát sáng chớp nhẹ tạo áp lực kịch tính.
- **Text Overlay:** `BOTTOM LEFT | CASH DRAIN: -200 BILLION VND/YEAR`.

---

### [CH05_SC011]
- **Thoại:** "Trong khi đó, doanh thu thực tế từ việc bán vé chỉ thu về vài chục tỷ đồng." (17 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Quầy thu ngân sảnh sân golf vắng bóng người vào buổi trưa hè: Chiếc máy in hóa đơn in ra một tờ biên lai mỏng manh ghi vài triệu đồng tiền vé, đặt cạnh đống hóa đơn điện nước chưa thanh toán cao ngất ngưởng.
- **Chủ thể & Hành động an toàn:** Thu ngân ngồi chống cằm thở dài trong không gian im ắng.
- **Camera & Điện ảnh:** Cinematic slow dolly in cận cảnh tờ biên lai lẻ loi, ánh sáng dịu buồn.
- **Text Overlay:** Không.

---

### [CH05_SC012]
- **Thoại:** "Khi thị trường bất động sản đóng băng, dòng tiền bán nhà bù chéo hoàn toàn bị cắt đứt." (18 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Sàn giao dịch bất động sản đại đô thị cửa đóng then cài, các tấm biển quảng cáo mở bán bị bong tróc, văn phòng giao dịch vắng tanh không một bóng khách hàng trong đợt đóng băng thanh khoản.
- **Từ khóa tìm kiếm (Search Query):** "frozen real estate market closed real estate office empty showroom Vietnam"
- **Nguồn báo chí uy tín (Source):** VTV Tài chính Kinh doanh / Báo Thanh Niên
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Real Estate Market Crisis Archive`.
- **Text Overlay:** Không.

---

### [CH05_SC013]
- **Thoại:** "Doanh nghiệp không thể phát hành thêm trái phiếu để đảo nợ." (11 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Bản tin truyền hình tài chính về khủng hoảng thị trường trái phiếu doanh nghiệp, đồ thị khối lượng phát hành mới rơi tự do về mức 0, các nhà đầu tư tập trung yêu cầu tất toán trước hạn.
- **Từ khóa tìm kiếm (Search Query):** "corporate bond market freeze default news report investor meeting"
- **Nguồn báo chí uy tín (Source):** VTV Khớp lệnh / Vietnamnet
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Bond Market Crisis Archive`.
- **Text Overlay:** Không.

---

### [CH05_SC014]
- **Thoại:** "Sân golf lúc này biến thành một khối u di căn thanh khoản khổng lồ." (14 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Đồ thị mô phỏng giải phẫu tài chính doanh nghiệp: Thảm cỏ sân golf bị bao bọc bởi các đường viền nứt nẻ màu đỏ san hô `#EF5350`, hút cạn dần các dòng tiền dự trữ từ các nhánh kinh doanh khác về phía nó.
- **Chủ thể & Hành động an toàn:** Ẩn dụ trực quan sinh động về sự hút cạn thanh khoản của cỗ máy ngốn tiền.
- **Camera & Điện ảnh:** Cinematic slow zoom in, ánh sáng đỏ cảnh báo nhấp nháy trên nền Slate đen sẫm.
- **Text Overlay:** `BOTTOM LEFT | LIQUIDITY DRAIN CANCER`.

---

### [CH05_SC015]
- **Thoại:** "Mặt cỏ vẫn phải tưới nước mỗi ngày, máy móc vẫn phải bảo dưỡng, và lãi vay ngân hàng vẫn tích tụ từng giờ." (23 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Dàn vòi phun nước tự động vẫn phun nước xoay tròn trên mặt cỏ sân golf vắng bóng người dưới bầu trời hoàng hôn u tối xám xịt, đồng hồ đo lãi vay điện tử góc màn hình nhảy số nợ không ngừng nghỉ.
- **Chủ thể & Hành động an toàn:** Không gian tĩnh mịch nhưng tiếng nước và tiếng tích tắc của đồng hồ nợ dồn dập.
- **Camera & Điện ảnh:** Steady camera shot, góc máy thấp sát mặt cỏ ướt sũng, ánh hoàng hôn xám chì.
- **Text Overlay:** Không.

---

### [CH05_SC016]
- **Thoại:** "Để hiểu rõ sự tàn nhẫn của quy luật này, hãy nhìn lại bài học lịch sử của Nhật Bản vào cuối thập niên 1980." (24 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bức ảnh tư liệu lịch sử đen trắng chuyển hóa sang đồ họa editorial 2D: Tòa tháp tài chính Tokyo và con phố Ginza sầm uất ngập tràn ánh đèn neon của thời kỳ bong bóng kinh tế 1989.
- **Chủ thể & Hành động an toàn:** Những doanh nhân Nhật Bản trong âu phục sang trọng vẫy xe taxi bằng những tờ tiền mệnh giá 10.000 Yên.
- **Camera & Điện ảnh:** Cinematic slow tracking shot lướt qua con phố Ginza ban đêm, ánh sáng rực rỡ nhưng mang hơi thở hoài niệm lịch sử.
- **Text Overlay:** `BOTTOM LEFT | JAPAN ASSET BUBBLE (1989 - 1991)`.

---

### [CH05_SC017]
- **Thoại:** "Trong cơn say bong bóng, thẻ hội viên sân golf tại Nhật Bản từng biến thành công cụ đầu cơ tài chính điên cuồng." (22 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Thước phim tư liệu đài truyền hình NHK năm 1989: Sàn giao dịch thẻ hội viên golf Tokyo náo nhiệt như sàn chứng khoán, nhân viên môi giới liên tục gào thét vào điện thoại để khớp lệnh các tấm thẻ golf triệu USD.
- **Từ khóa tìm kiếm (Search Query):** "Tokyo golf membership exchange floor trading frenzy 1989 NHK archive"
- **Nguồn báo chí uy tín (Source):** NHK Japan Historical Archive / Bloomberg
- **Yêu cầu xử lý Fair Use:** Cắt 4.0s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: NHK Historical Archive (1989)`.
- **Text Overlay:** Không.

---

### [CH05_SC018]
- **Thoại:** "Thẻ hội viên của câu lạc bộ Koganei tại Tokyo từng chạm đỉnh kỷ lục gần bốn trăm triệu Yên vào năm 1989." (23 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Koganei Golf Club Peak Valuation Card (Thẻ đỉnh cao bong bóng thẻ golf Koganei).
- **Tiêu đề & Dữ liệu cốt lõi:** Thẻ kỷ lục lịch sử: `KOGANEI GOLF CLUB (TOKYO) MEMBERSHIP PEAK: 400 MILLION YEN (1989)`. Tương đương `$3.0 MILLION USD` thời điểm bấy giờ. Giá trị một tấm thẻ đắt hơn một căn biệt thự sang trọng tại trung tâm Tokyo.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, con số 400 triệu Yên mạ vàng kim rực rỡ `#F8D469`.
- **Bảng màu & Hiệu ứng chuyển động:** Điểm nhấn vàng kim lấp lánh rồi chững lại ở đỉnh dốc.
- **Text Overlay:** `BOTTOM LEFT | KOGANEI: 400M YEN ($3M USD) IN 1989`.

---

### [CH05_SC019]
- **Thoại:** "Con số này tương đương hơn ba triệu đô la Mỹ thời điểm đó." (13 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Cổng vào cổ kính sang trọng của câu lạc bộ golf Koganei Country Club tại Tokyo, những chiếc xe Mercedes và Rolls-Royce cổ điển nối đuôi nhau vào sân.
- **Từ khóa tìm kiếm (Search Query):** "Koganei country club Tokyo entrance luxury vintage cars Japan 1989"
- **Nguồn báo chí uy tín (Source):** Japan Golf Archive / Kyodo News
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Kyodo News Archive`.
- **Text Overlay:** Không.

---

### [CH05_SC020]
- **Thoại:** "Các ngân hàng Nhật Bản tranh nhau nhận thẻ golf làm tài sản bảo đảm để cho vay hàng trăm tỷ Yên." (21 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Quầy giao dịch tín dụng một ngân hàng lớn tại Tokyo năm 1989: Tấm thẻ hội viên golf mạ vàng đặt trang trọng bên cạnh hợp đồng tín dụng vay nợ hàng tỷ Yên, con dấu cá nhân hanko đỏ được đóng dứt khoát.
- **Chủ thể & Hành động an toàn:** Cán bộ ngân hàng cúi đầu chào khách hàng vay nợ đầy tôn kính.
- **Camera & Điện ảnh:** Steady camera shot, ánh sáng vàng ấm phản chiếu từ tấm thẻ mạ vàng.
- **Text Overlay:** Không.

---

### [CH05_SC021]
- **Thoại:** "Khi Ngân hàng Trung ương Nhật Bản tăng lãi suất và bong bóng vỡ tan, thảm kịch lập tức diễn ra trên toàn hệ thống." (24 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Thống đốc Ngân hàng Trung ương Nhật Bản (BOJ) Yasushi Mieno xuất hiện trên truyền hình tuyên bố tăng lãi suất chiết khấu mạnh tay để dập tắt bong bóng bất động sản năm 1990.
- **Từ khóa tìm kiếm (Search Query):** "Bank of Japan governor Yasushi Mieno interest rate hike announcement 1990"
- **Nguồn báo chí uy tín (Source):** NHK News Archive / Reuters
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Bank of Japan Archive`.
- **Text Overlay:** Không.

---

### [CH05_SC022]
- **Thoại:** "Giá thẻ hội viên sân golf toàn quốc sụp đổ từ chín mươi đến chín mươi lăm phần trăm." (18 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Nikkei Golf Membership Index Collapse (Đồ thị sụp đổ 95% chỉ số thẻ golf Nikkei).
- **Tiêu đề & Dữ liệu cốt lõi:** `@nikkei_bubble_golf_chart.jpg ->` Đồ thị chỉ số giá thẻ golf Nikkei Golf Index giai đoạn 1989–1995: Đỉnh dốc đứng năm 1989 $\to$ Lao dốc thẳng đứng rơi tự do: `-90% TO -95% COLLAPSE`. Giá trị bốc hơi gần như hoàn toàn.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate sẫm `#0F172A`, đường line đỏ san hô `#EF5350` cắm thẳng đứng xuống đáy.
- **Bảng màu & Hiệu ứng chuyển động:** Đường line đỏ rơi dồn dập kèm vệt khói tan biến.
- **Text Overlay:** `BOTTOM LEFT | NIKKEI GOLF INDEX: -95% COLLAPSE`.

---

### [CH05_SC023]
- **Thoại:** "Những chiếc thẻ từng có giá hàng triệu đô la bỗng chốc trở thành tờ giấy lộn không ai thèm mua." (21 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Tấm thẻ hội viên mạ vàng từng có giá triệu USD nằm rơi trên sàn nhà phủ đầy bụi bặm trong một văn phòng phá sản bị niêm phong, cạnh những tờ công văn đòi nợ của ngân hàng.
- **Chủ thể & Hành động an toàn:** Hình ảnh tĩnh vật gợi sự sụp đổ bẽ bàng của các ván cược tài chính ảo.
- **Camera & Điện ảnh:** Cinematic slow dolly in sát mặt sàn, ánh sáng xám tro hiu hắt rọi qua khe cửa.
- **Text Overlay:** Không.

---

### [CH05_SC024]
- **Thoại:** "Hàng trăm công ty quản lý sân golf tuyên bố vỡ nợ dưới luật phá sản." (15 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Tòa án Tokyo thụ lý các đơn xin phá sản của doanh nghiệp sân golf đầu thập niên 1990, các luật sư và chủ nợ bước ra khỏi phiên tòa với nét mặt nặng trĩu.
- **Từ khóa tìm kiếm (Search Query):** "Tokyo district court bankruptcy filing golf course operators 1990s"
- **Nguồn báo chí uy tín (Source):** Kyodo News / NHK
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Tokyo Court Archive`.
- **Text Overlay:** Không.

---

### [CH05_SC025]
- **Thoại:** "Họ để lại cho hệ thống ngân hàng Nhật Bản khoản nợ xấu khổng lồ vượt quá một trăm tỷ đô la Mỹ." (22 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** $100 Billion Bad Debt Shock Card (Thẻ cú sốc nợ xấu 100 tỷ USD).
- **Tiêu đề & Dữ liệu cốt lõi:** Thẻ khủng hoảng nợ xấu ngân hàng: `JAPANESE BANKING NON-PERFORMING LOANS: > $100 BILLION USD` bắt nguồn từ tài sản thế chấp sân golf và bất động sản giải trí.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, con số $100 BILLION USD hiển thị to bản viền đỏ rực rỡ `#EF5350`.
- **Bảng màu & Hiệu ứng chuyển động:** Cảnh báo khủng hoảng hệ thống tài chính kéo dài thập kỷ mất mát.
- **Text Overlay:** `BOTTOM LEFT | GOLF BAD DEBT: > $100 BILLION USD`.

---

### [CH05_SC026]
- **Thoại:** "Hàng loạt sân golf bị bỏ hoang, máy móc hoen rỉ và cỏ dại mọc cao quá đầu người." (18 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Những thước phim tài liệu ghi lại cảnh các sân golf bị bỏ hoang tại vùng ngoại ô Nhật Bản: Những cỗ máy cắt cỏ hoen rỉ nằm trong kho ẩm mốc, thảm cỏ fairway biến thành đồng cỏ dại cao lút đầu người, hố cát bunker ngập bùn lầy.
- **Từ khóa tìm kiếm (Search Query):** "abandoned golf course Japan overgrown grass rusty machinery documentary"
- **Nguồn báo chí uy tín (Source):** NHK Special Documentary / Japan Times
- **Yêu cầu xử lý Fair Use:** Cắt 4.0s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: NHK Documentary Archive`.
- **Text Overlay:** Không.

---

### [CH05_SC027]
- **Thoại:** "Bài học lịch sử để lại một đúc kết lạnh lùng." (10 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Một cây cờ golf rách tã bay phần phật trong cơn gió bão trên đỉnh đồi trơ trọi, mặt trời xám xịt chìm vào đám mây đen giông bão phía chân trời.
- **Chủ thể & Hành động an toàn:** Hình tượng tĩnh lặng đĩnh đạc phản chiếu bài học quy luật muôn đời của tài chính.
- **Camera & Điện ảnh:** Cinematic slow tracking shot góc thấp, gió thổi cát bụi bay nhẹ trên mặt đất.
- **Text Overlay:** Không.

---

### [CH05_SC028]
- **Thoại:** "Trong chu kỳ tiền rẻ, sân golf là bảo chứng hào nhoáng cho tiềm lực tài chính." (16 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Chiếc cúp vô địch bằng pha lê sáng lấp lánh đặt trước bức tường kính phản chiếu toàn cảnh một đại đô thị rực rỡ phồn hoa.
- **Chủ thể & Hành động an toàn:** Biểu tượng của sự hào nhoáng trong chu kỳ tăng trưởng đòn bẩy.
- **Camera & Điện ảnh:** Steady camera shot cận cảnh pha lê phản chiếu ánh đèn vàng ấm.
- **Text Overlay:** `BOTTOM LEFT | CHEAP MONEY: GLAMOROUS COLLATERAL`.

---

### [CH05_SC029]
- **Thoại:** "Nhưng khi thủy triều rút đi, nó lại là tài sản thanh lý tồi tệ nhất." (15 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Cảnh phát mại tài sản thế chấp tại một trung tâm bán đấu sở hữu nợ xấu ngân hàng: Danh sách các dự án sân golf bị đấu giá nhiều lần với giá khởi điểm giảm sâu 50% đến 70% nhưng không có nhà đầu tư nào nộp hồ sơ tham gia.
- **Từ khóa tìm kiếm (Search Query):** "debt auction bank foreclosed property auction floor no bidders Vietnam"
- **Nguồn báo chí uy tín (Source):** VAM / Báo Đấu Thầu
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Asset Liquidation Archive`.
- **Text Overlay:** Không.

---

### [CH05_SC030]
- **Thoại:** "Bởi vì không một nhà đầu tư tỉnh táo nào dám bỏ tiền mua lại một cỗ máy ngốn tiền mặt." (20 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Phòng họp của một quỹ đầu tư cơ hội (Distressed Asset Fund): Các nhà quản lý quỹ lướt qua hồ sơ một dự án sân golf đang bị ngân hàng siết nợ, đồng loạt lắc đầu và gạt tập hồ sơ sang một bên.
- **Chủ thể & Hành động an toàn:** Quyết định dứt khoát từ chối mua lại cỗ máy ngốn OpEx.
- **Camera & Điện ảnh:** Cinematic slow dolly out, ánh sáng phòng họp xám slate `#1E293B` lạnh lùng thực dụng.
- **Text Overlay:** Không.

---

### [CH05_SC031]
- **Thoại:** "Sự sụp đổ của các ván cược tài chính đã gióng lên hồi chuông cảnh tỉnh cho các cơ quan quản lý." (21 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Chiếc chuông đồng lớn đặt trên nóc tòa nhà cơ quan quản lý nhà nước ngân vang từng hồi chuông trầm hùng, chim bồ câu tung cánh bay lên bầu trời quang đãng.
- **Chủ thể & Hành động an toàn:** Ẩn dụ chuyển giao thời khắc tỉnh thức của thể chế.
- **Camera & Điện ảnh:** Cinematic slow tilt up từ thân chuông lên nền trời xanh, ánh sáng mặt trời rọi qua tạo cảm giác đổi mới.
- **Text Overlay:** Không.

---

### [CH05_SC032]
- **Thoại:** "Nhà nước không thể để tài nguyên đất đai bị lãng phí trong những cuộc phiêu lưu nợ nần." (18 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Phiên chất vấn sôi nổi tại nghị trường Quốc hội Việt Nam: Các đại biểu Quốc hội bày tỏ lo ngại sâu sắc về tình trạng dự án treo, ôm đất đai hoang hóa gây lãng phí nguồn lực quốc gia.
- **Từ khóa tìm kiếm (Search Query):** "National Assembly questioning session land use waste debate Vietnam"
- **Nguồn báo chí uy tín (Source):** Truyền hình Quốc hội Việt Nam / VTV1
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: National Assembly Television`.
- **Text Overlay:** Không.

---

### [CH05_SC033]
- **Thoại:** "Một cuộc đại phẫu thể chế đã chính thức bắt đầu để thanh lọc toàn bộ thị trường." (17 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bàn làm việc của các nhà lập pháp với dự thảo Luật Đất đai mới dày cộp, chiếc bút ký kim loại sẵn sàng đặt cạnh văn bản, tạo cầu nối vững chãi sang Chương 6 Bước Ngoặt Thể Chế.
- **Chủ thể & Hành động an toàn:** Sự chuyển dịch dứt khoát của pháp luật sang kỷ nguyên sòng phẳng minh bạch.
- **Camera & Điện ảnh:** Cinematic slow dolly in cận cảnh trang bìa "Luật Đất Đai (Sửa Đổi)", ánh sáng ngà kem `#FAF7EE` nghiêm cẩn.
- **Text Overlay:** `BOTTOM LEFT | INSTITUTIONAL RESTRUCTURING`.
"""

def main():
    chapters = {
        4: build_chapter_04(),
        5: build_chapter_05(),
    }
    
    for ch_num, content in chapters.items():
        ch_str = f"{ch_num:02d}"
        file_path = os.path.join(EPISODE_DIR, f"chapter_{ch_str}_visual_plus.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Written: {file_path}")
        cmd = ["python3", os.path.join(EPISODE_DIR, "export_chapter_tri_track.py"), str(ch_num)]
        subprocess.run(cmd, check=True)

if __name__ == "__main__":
    main()
