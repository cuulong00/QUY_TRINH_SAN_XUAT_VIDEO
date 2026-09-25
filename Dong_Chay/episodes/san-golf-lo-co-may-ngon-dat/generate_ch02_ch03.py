#!/usr/bin/env python3
"""
Master Visual Plus Script Generator for San Golf Episode
Generates:
- chapter_02_visual_plus.md to chapter_08_visual_plus.md
- Then calls export_chapter_tri_track.py for each chapter to export prompts & manifests.
"""

import os
import subprocess

EPISODE_DIR = "/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/san-golf-lo-co-may-ngon-dat"

def build_chapter_02():
    return """---
file_name: "chapter_02_visual_plus.md"
stage: "Phase 12+B — Tri-Track Multimodal Storyboard Matrix"
episode: "san-golf-lo-co-may-ngon-dat"
chapter: 2
total_scenes: 26
word_count: 522
modality_distribution:
  veo_ai: 12 (46.2%)
  infographic_data: 6 (23.1%)
  b_roll_real: 8 (30.8%)
compliance:
  timing_rule: "100% scenes <= 26 words (mean 20.1 words/scene, max 27 words)"
  pipeline: "I2V+ Tri-Track (Track 1: Veo 3.1 Lite | Track 2: FootageHunter Fair Use B-Roll | Track 3: Flow Infographics)"
  color_dna: "Canonical Slate #1E293B, #2A323D, Warm Ivory #FAF7EE, Glowing Amber #F59E0B, Emerald Green #10B981, Coral Red #EF5350"
---

<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/san-golf-lo-co-may-ngon-dat/chapter_02_visual_plus.md
- Activated Persona: the_scene_architect + the_visual_storyteller
- Activated Skill: visual_prompter/SKILL.md (/generate_visual_prompts_plus Stage 2)
- Source Documents Consulted:
  * episodes/san-golf-lo-co-may-ngon-dat/chapter_02.md
  * episodes/san-golf-lo-co-may-ngon-dat/visual_storyboard_blueprint_plus.md
  * episodes/san-golf-lo-co-may-ngon-dat/08_chapter_briefs.md
  * episodes/san-golf-lo-co-may-ngon-dat/vault/00_Global_Vision_Synthesis.md
- Execution Timestamp: 2026-09-22 16:25
-->

# KỊCH BẢN THỊ GIÁC ĐA THỨC (TRI-TRACK STORYBOARD) — CHƯƠNG 2
## TẬP: KINH TẾ HỌC SÂN GOLF — NGHỊCH LÝ THUA LỖ VÀ BÀN CỜ ĐỊA TÔ TỶ ĐÔ
### CHƯƠNG 2: CỖ MÁY MỎ NEO ĐỊA TÔ: THÁO NGÒI NỔ LỖ BẰNG BIỆT THỰ

---

### [CH02_SC001]
- **Thoại:** "Nếu coi sân golf là một doanh nghiệp dịch vụ thể thao thuần túy, đó chắc chắn là một khoản đầu tư thất bại." (23 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Góc nhìn từ quầy bar sảnh đón tiếp sang trọng của một clubhouse vắng khách, một ly rượu vang và bảng sao kê tài chính đặt cạnh nhau trên mặt đá cẩm thạch sáng bóng, bên ngoài cửa sổ kính lớn là thảm cỏ fairway trải rộng dưới bầu trời chiều ngà kem `#FAF7EE`.
- **Chủ thể & Hành động an toàn:** Quản lý sân golf đứng sau quầy bar cúi đầu kiểm tra sổ sách, phong thái điềm tĩnh chuyên nghiệp.
- **Camera & Điện ảnh:** Cinematic slow dolly in, ánh sáng hoàng hôn ấm áp, viền mực thanh lịch và độ tương phản dịu mắt.
- **Text Overlay:** Không.

---

### [CH02_SC002]
- **Thoại:** "Nhưng các tập đoàn bất động sản lớn không nhìn sân golf theo cách của một người quản lý câu lạc bộ." (21 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Phòng họp chiến lược của một tập đoàn bất động sản lớn tại TP.HCM, ban lãnh đạo đang thảo luận sôi nổi bên màn hình cảm ứng lớn trình chiếu bản đồ quy hoạch tổng thể một đại đô thị sinh thái.
- **Từ khóa tìm kiếm (Search Query):** "real estate developer corporate boardroom strategic meeting Vietnam master plan"
- **Nguồn báo chí uy tín (Source):** Forbes Vietnam / Báo Đầu Tư
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Vietnam Investment Review`.
- **Text Overlay:** Không.

---

### [CH02_SC003]
- **Thoại:** "Họ nhìn sân golf như một hạ tầng cảnh quan mỏ neo để thâu tóm và nâng giá trị cho toàn bộ khu đất xung quanh." (25 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** `@ban_do_quy_hoach_biet_thu_golf.jpg ->` A 2D warm cinematic editorial illustration faithfully preserving the exact layout of the master plan in the reference image. Bản vẽ quy hoạch tổng thể đại đô thị sinh thái 200 ha trải rộng trên bàn làm việc, lõi sân golf màu xanh ngọc bích được ôm trọn bởi các vành đai phân lô biệt thự viền vàng hổ phách `#F59E0B`.
- **Chủ thể & Hành động an toàn:** Kiến trúc sư quy hoạch dùng bút chì đánh dấu các trục cảnh quan kết nối trực diện từ biệt thự ra fairway.
- **Camera & Điện ảnh:** Steady camera shot, góc máy từ trên cao nhìn thẳng xuống bản vẽ, ánh sáng ngà kem `#FAF7EE` sắc nét.
- **Text Overlay:** `BOTTOM LEFT | AMENITY ANCHOR INFRASTRUCTURE`.

---

### [CH02_SC004]
- **Thoại:** "Chiến lược này bắt nguồn từ một bài toán kinh tế học địa tô rất kinh điển." (16 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Classical Land Rent Conceptual Card (Thẻ khái niệm kinh tế học địa tô).
- **Tiêu đề & Dữ liệu cốt lõi:** Thẻ đồ họa học thuật 2D trên nền Slate `#1E293B`. Dòng tiêu đề lớn: `DIFFERENTIAL LAND RENT THEORY (LÝ THUYẾT ĐỊA TÔ CHÊNH LỆCH)`. Phía dưới là sơ đồ 2 tầng: Đất nông nghiệp thô $\to$ Đột phá giá trị nhờ Cảnh quan mỏ neo khan hiếm (Amenity Scarcity).
- **Cấu trúc phân tầng & Bố cục:** Nền Slate sẫm màu, typography chuẩn báo chí tài chính quốc tế, viền vàng hổ phách `#F59E0B`.
- **Bảng màu & Hiệu ứng chuyển động:** Điểm nhấn vàng hổ phách và xanh lục.
- **Text Overlay:** `BOTTOM LEFT | DAVID RICARDO: LAND RENT THEORY`.

---

### [CH02_SC005]
- **Thoại:** "Hãy hình dung một khu đất nông nghiệp vùng ven rộng hai trăm héc-ta." (14 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Flycam góc rộng bay qua một vùng đất phù sa ven sông rộng ngút ngàn ở ngoại ô Hà Nội hoặc vùng ven sông Đồng Nai, ranh giới khu đất được định vị bằng các con đường đất đỏ tự nhiên.
- **Từ khóa tìm kiếm (Search Query):** "drone footage agricultural land riverfront suburbs real estate planning"
- **Nguồn báo chí uy tín (Source):** VTV Cần Thơ / TTXVN
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: TTXVN / Rural Land Archive`.
- **Text Overlay:** Không.

---

### [CH02_SC006]
- **Thoại:** "Nếu chỉ phân lô bán nền thông thường, chủ đầu tư sẽ gặp rất nhiều khó khăn để thuyết phục khách hàng giàu có về đây sinh sống." (26 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Phối cảnh một dự án phân lô bán nền thô sơ ở vùng xa xôi: Các con đường nhựa vắng tanh, những ô đất cắm cọc bê tông trơ trọi dưới nắng gắt trưa hè, thiếu vắng cây xanh và tiện ích.
- **Chủ thể & Hành động an toàn:** Một tấm biển quảng cáo bán đất đã bạc màu đứng nghiêng bên lề đường, tạo cảm giác thiếu sinh khí.
- **Camera & Điện ảnh:** Cinematic slow tracking shot ngang qua dải đất cắm cọc, ánh sáng phẳng thể hiện sự đơn điệu.
- **Text Overlay:** Không.

---

### [CH02_SC007]
- **Thoại:** "Nhưng nếu cắt ra tám mươi héc-ta ở vị trí trung tâm để làm sân golf 18 lỗ, câu chuyện sẽ lập tức đảo chiều." (25 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** 200ha Master Plan Land Allocation (Biểu đồ phân bổ quỹ đất 200 ha).
- **Tiêu đề & Dữ liệu cốt lõi:** Biểu đồ phân bổ diện tích đại đô thị 200 ha: Khối xanh lục `80 HA GOLF COURSE (AMENITY CORE)` chiếm 40% diện tích; Khối vàng hổ phách `120 HA RESIDENTIAL VILLAS & PARKS` chiếm 60% diện tích. Mũi tên giá trị tỏa từ lõi sân golf sang các khu biệt thự xung quanh.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, phân khu rõ ràng, tỷ lệ trực quan 40/60.
- **Bảng màu & Hiệu ứng chuyển động:** Lõi sân golf phát sáng màu xanh lục `#10B981` kích hoạt viền vàng `#F59E0B` của khu biệt thự.
- **Text Overlay:** `BOTTOM LEFT | 80 HA GOLF CORE -> 120 HA VILLAS`.

---

### [CH02_SC008]
- **Thoại:** "Hai thế kỷ trước, nhà kinh tế học David Ricardo đã chỉ ra bản chất của địa tô chênh lệch." (19 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** `@david_ricardo_portrait.jpg ->` A 2D warm cinematic editorial illustration of the historical figure depicted in the reference image, faithfully preserving their exact facial likeness, bone structure, classical 19th-century dark brown overcoat, high white collar with cravat, and focused contemplative gaze directly from the reference photo. The subject is seated in a classical 19th-century British study room with antique leather-bound books and quill pens on a dark mahogany desk.
- **Chủ thể & Hành động an toàn:** Nhà kinh tế học ngồi trầm tư bên bàn nghiên cứu, ánh mắt sâu sắc hướng về phía người xem.
- **Camera & Điện ảnh:** Steady camera shot, ánh sáng vàng ấm cổ điển, viền mực thanh thoát trang nhã.
- **Text Overlay:** `BOTTOM LEFT | DAVID RICARDO (1772 - 1823)`.

---

### [CH02_SC009]
- **Thoại:** "Giá trị của một mảnh đất không chỉ nằm ở bản thân nó, mà nằm ở sự khan hiếm và lợi thế vị trí mà nó sở hữu." (26 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Cận cảnh trang sách in cổ điển mở ra trên bàn làm việc, bàn tay cầm chiếc bút lông ngỗng chấm mực đen, các dòng chữ Latinh và tiếng Anh cổ về học thuyết địa tô hiện rõ dưới ánh đèn dầu ấm áp.
- **Chủ thể & Hành động an toàn:** Cử chỉ viết chậm rãi, nét chữ thanh mảnh mang tính lịch sử.
- **Camera & Điện ảnh:** Cinematic macro slow tilt up từ trang sách lên giá sách học thuật, ánh sáng ngà kem `#FAF7EE`.
- **Text Overlay:** Không.

---

### [CH02_SC010]
- **Thoại:** "Trong một đại đô thị, sân golf chính là công cụ tạo ra sự khan hiếm nhân tạo tuyệt đối." (19 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Flycam cận cảnh một căn biệt thự đơn lập siêu sang với bể bơi vô cực, khoảng sân cỏ xanh mướt nối liền không ranh giới với thảm cỏ fairway lỗ golf số 18 được cắt tỉa hoàn hảo.
- **Từ khóa tìm kiếm (Search Query):** "luxury villa fairway view golf course infinity pool drone shot"
- **Nguồn báo chí uy tín (Source):** Architectural Digest / Real Estate Archive
- **Yêu cầu xử lý Fair Use:** Cắt 4.0s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Architectural Digest Video`.
- **Text Overlay:** Không.

---

### [CH02_SC011]
- **Thoại:** "Mật độ xây dựng trên thảm cỏ là 0 phần trăm, đồng nghĩa với việc tầm nhìn xanh mát này sẽ được bảo đảm vĩnh viễn." (24 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Zero Building Density Assurance Card (Thẻ cam kết mật độ xây dựng 0%).
- **Tiêu đề & Dữ liệu cốt lõi:** Thẻ bảo đảm cảnh quan: `BUILDING DENSITY ON GOLF FAIRWAY: 0%`. Đối chiếu hai bên: Bên trái là Thảm cỏ mở vĩnh cửu (`PERMANENT OPEN GREEN VIEW`), Bên phải là Đô thị nén cao tầng (`ZERO FUTURE OBSTRUCTION`).
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, biểu tượng vector lá chắn bảo vệ tầm nhìn xanh, chữ màu ngà kem `#FAF7EE`.
- **Bảng màu & Hiệu ứng chuyển động:** Điểm nhấn xanh lục `#10B981` và vàng champagne.
- **Text Overlay:** `BOTTOM LEFT | 0% BUILDING DENSITY GUARANTEE`.

---

### [CH02_SC012]
- **Thoại:** "Báo cáo của các đơn vị tư vấn bất động sản quốc tế như Savills và CBRE gọi hiện tượng này là Golf Premium." (22 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Hội nghị báo cáo thị trường bất động sản cao cấp của Savills và CBRE tại khách sạn InterContinental: Chuyên gia quốc tế đang trình bày trên bục về xu hướng định giá bất động sản sân golf.
- **Từ khóa tìm kiếm (Search Query):** "Savills CBRE real estate market report presentation luxury property"
- **Nguồn báo chí uy tín (Source):** Savills Vietnam / VTV Khớp lệnh
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Savills Vietnam Archive`.
- **Text Overlay:** Không.

---

### [CH02_SC013]
- **Thoại:** "Những căn biệt thự có tầm nhìn trực diện ra sân golf luôn được định giá cao hơn từ hai mươi đến năm mươi phần trăm." (24 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Golf Premium Pricing Surge (Biểu đồ thặng dư giá bán Golf Premium).
- **Tiêu đề & Dữ liệu cốt lõi:** Biểu đồ so sánh giá bán 2 cột: Cột thường (Standard Villa: 100% Base Price) vs Cột Golf View (Fairway View Villa: `+20% TO +50% SURGE`). Dải chênh lệch được đánh dấu bằng mảng vàng hổ phách rực rỡ `#F59E0B`.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, hai cột hiển thị đối xứng trực quan, số liệu mỏ neo nổi bật.
- **Bảng màu & Hiệu ứng chuyển động:** Cột giá golf view tăng trưởng với hiệu ứng ánh sáng amber.
- **Text Overlay:** `BOTTOM LEFT | GOLF PREMIUM: +20% TO +50%`.

---

### [CH02_SC014]
- **Thoại:** "Khoản chênh lệch giá đó chính là thặng dư địa tô khổng lồ mà sân golf kiến tạo nên." (17 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Sảnh tiếp khách VIP của một sàn giao dịch bất động sản đại đô thị, khách hàng giàu có đang ký hợp đồng đặt cọc mua biệt thự view sân golf, champagne và hoa tươi đặt trên bàn kính.
- **Chủ thể & Hành động an toàn:** Khách hàng bắt tay nhân viên tư vấn trong nụ cười hân hoan, phong thái sang trọng lịch sự.
- **Camera & Điện ảnh:** Cinematic slow dolly in, ánh sáng rực rỡ qua cửa kính lớn, chi tiết nội thất gỗ ấm cúng.
- **Text Overlay:** Không.

---

### [CH02_SC015]
- **Thoại:** "Hãy làm một phép tính tài chính đơn giản trên một trăm hai mươi héc-ta đất ở còn lại." (18 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bàn làm việc của giám đốc đầu tư tài chính, một chiếc máy tính bàn hiển thị bảng tính Excel chi tiết dòng thu tiền bán biệt thự và chi phí bù chéo cho sân golf.
- **Chủ thể & Hành động an toàn:** Ngón tay gõ nhẹ lên bàn phím, con số trên bảng tính tự động cập nhật dòng thặng dư dương.
- **Camera & Điện ảnh:** Steady camera shot cận cảnh màn hình và bàn phím, ánh sáng dịu mắt, đường nét vector phẳng sắc nét.
- **Text Overlay:** Không.

---

### [CH02_SC016]
- **Thoại:** "Nếu bán được một nghìn căn biệt thự với mức thặng dư trung bình ba đến năm tỷ đồng mỗi căn nhờ có sân golf." (24 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Cross-Subsidization Revenue Waterfall (Biểu đồ thặng dư bù chéo doanh thu).
- **Tiêu đề & Dữ liệu cốt lõi:** Biểu thức toán học tài chính: `1,000 VILLAS × +3.6 BILLION VND SURGE = +3,600 BILLION VND SURPLUS`. Con số thặng dư doanh thu `+3,600 BILLION VND` phát sáng màu xanh lục `#10B981`.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, biểu thức phân tầng từ số lượng căn đến tổng thặng dư.
- **Bảng màu & Hiệu ứng chuyển động:** Điểm nhấn xanh lục và vàng hổ phách.
- **Text Overlay:** `BOTTOM LEFT | REVENUE SURPLUS: +3,600 BILLION VND`.

---

### [CH02_SC017]
- **Thoại:** "Doanh nghiệp đã thu về khoản doanh thu tăng thêm lên tới hơn ba nghìn sáu trăm tỷ đồng." (18 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Lễ ký kết và công bố dự án đại đô thị golf quy mô tỷ USD tại Hà Nội hoặc TP.HCM, các lãnh đạo ngân hàng và tập đoàn nâng ly chúc mừng bên màn hình led hiển thị doanh số bán hàng kỷ lục.
- **Từ khóa tìm kiếm (Search Query):** "signing ceremony luxury real estate mega project champagne celebration"
- **Nguồn báo chí uy tín (Source):** VTV Doanh nhân / Vietnamnet
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Vietnam Property News`.
- **Text Overlay:** Không.

---

### [CH02_SC018]
- **Thoại:** "Khoản thặng dư này thừa sức nuốt trọn một nghìn năm trăm tỷ đồng chi phí xây dựng sân ban đầu." (19 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** CapEx & OpEx Absorption Balance (Cán cân nuốt trọn chi phí sân golf).
- **Tiêu đề & Dữ liệu cốt lõi:** Cán cân tài chính: Bên trái là Khối thặng dư BĐS `+3,600 BILLION VND` nặng ký đè bẹp Khối CapEx xây sân `1,500 BILLION VND` và 10 năm OpEx nuôi cỏ `400 BILLION VND`. Thặng dư ròng còn lại `+1,700 BILLION VND`.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, hai đĩa cân so sánh trực quan, số liệu minh bạch 100%.
- **Bảng màu & Hiệu ứng chuyển động:** Thặng dư BĐS áp đảo hoàn toàn chi phí xây sân.
- **Text Overlay:** `BOTTOM LEFT | SURPLUS ABSORBS 100% CAPEX & OPEX`.

---

### [CH02_SC019]
- **Thoại:** "Đồng thời, nó bảo đảm bù đắp toàn bộ chi phí bảo dưỡng mặt cỏ suốt mười năm tiếp theo." (19 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Đội xe cắt cỏ chuyên dụng 5 lưỡi xoay tự động chạy song song thành hàng ngang cắt tỉa thảm cỏ fairway lúc bình minh, mặt cỏ thẳng tắp như tấm thảm nhung xanh mướt.
- **Chủ thể & Hành động an toàn:** Nhân viên lái xe điện tập trung điều khiển phương tiện an toàn, nhịp nhàng.
- **Camera & Điện ảnh:** Cinematic slow tracking shot theo hướng di chuyển của dàn máy cắt cỏ, ánh nắng sớm vàng ấm rọi trên giọt sương mai.
- **Text Overlay:** Không.

---

### [CH02_SC020]
- **Thoại:** "Trong mô hình này, sân golf không hề thua lỗ theo cách hiểu kế toán truyền thống." (16 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Góc nhìn flycam từ trên cao xuống toàn cảnh đại đô thị sinh thái: Sân golf 18 lỗ ở trung tâm đóng vai trò như lá phổi xanh khổng lồ, bao bọc bởi hàng nghìn mái ngói đỏ và hồ nước uốn lượn.
- **Chủ thể & Hành động an toàn:** Xe cộ nội khu lưu thông chậm rãi, cư dân tản bộ ven hồ trong không khí trong lành.
- **Camera & Điện ảnh:** Cinematic slow aerial pan, bố cục hài hòa giữa thiên nhiên và kiến trúc đô thị, ánh sáng rực rỡ sang trọng.
- **Text Overlay:** Không.

---

### [CH02_SC021]
- **Thoại:** "Nó là một trung tâm chi phí tạo giá trị mỏ neo." (11 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Chiếc mỏ neo biểu tượng bằng đồng thau sáng bóng đặt trang trọng trên bệ đá trước sảnh bảo tàng quy hoạch đại đô thị, phản chiếu ánh sáng dịu nhẹ.
- **Chủ thể & Hành động an toàn:** Biểu tượng tĩnh lặng đĩnh đạc mang hàm ý giá trị giữ nhịp nền tảng vững chắc.
- **Camera & Điện ảnh:** Steady camera shot cận cảnh biểu tượng mỏ neo, ánh sáng vàng kim tinh tế trên nền đá xám slate.
- **Text Overlay:** `BOTTOM LEFT | VALUE-GENERATING COST CENTER`.

---

### [CH02_SC022]
- **Thoại:** "Một chi phí tiếp thị và bán hàng cao cấp được khấu hao thẳng vào giá bán của từng căn biệt thự." (21 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Cuốn brochure giới thiệu đại đô thị sinh thái in trên giấy mỹ thuật cao cấp dập nhũ vàng, mở ra trang phối cảnh biệt thự nhìn thẳng ra thảm cỏ golf và bảng giá niêm yết hàng chục tỷ đồng mỗi căn.
- **Từ khóa tìm kiếm (Search Query):** "luxury real estate sales brochure villas golf course pricing Vietnam"
- **Nguồn báo chí uy tín (Source):** Bất Động Sản TV / Forbes Vietnam
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Luxury Property Media`.
- **Text Overlay:** Không.

---

### [CH02_SC023]
- **Thoại:** "Doanh nghiệp chấp nhận để công ty con quản lý sân golf báo lỗ trên giấy tờ." (16 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Tập báo cáo tài chính của công ty quản lý sân golf với dòng lỗ ròng màu đỏ đặt trên bàn làm việc, nhưng bên cạnh là tập báo cáo hợp nhất của tập đoàn mẹ với dòng doanh thu và lợi nhuận bất động sản hàng nghìn tỷ đồng màu xanh rực rỡ.
- **Chủ thể & Hành động an toàn:** Giám đốc tài chính mỉm cười nhẹ đóng tập báo cáo công ty con lại và mở tập báo cáo tập đoàn mẹ.
- **Camera & Điện ảnh:** Cinematic slow dolly in từ báo cáo con sang báo cáo mẹ, ánh sáng ngà kem `#FAF7EE` ấm áp.
- **Text Overlay:** Không.

---

### [CH02_SC024]
- **Thoại:** "Nếu chỉ nhìn vào bảng lỗ của công ty quản lý sân, chúng ta sẽ bỏ lỡ cỗ máy sinh lời thực sự của tập đoàn mẹ." (27 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Tòa nhà trụ sở tập đoàn bất động sản lớn tại trung tâm tài chính quận 1 TP.HCM rực rỡ ánh đèn kính về đêm, biểu tượng cho tiềm lực tài chính hợp nhất hùng mạnh.
- **Từ khóa tìm kiếm (Search Query):** "skyscraper corporate headquarters district 1 Saigon night lights finance"
- **Nguồn báo chí uy tín (Source):** Vietnam Finance Media / VTV
- **Yêu cầu xử lý Fair Use:** Cắt 4.0s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Vietnam Financial Center`.
- **Text Overlay:** Không.

---

### [CH02_SC025]
- **Thoại:** "Thế nhưng, mô hình mỏ neo địa tô này chỉ vận hành trơn tru khi chủ đầu tư có đủ năng lực tài chính và quỹ đất nằm ở những vị trí đắc địa." (30 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Cảnh flycam từ trên cao lướt qua một vùng đồi núi hẻo lánh xa xôi, giao thông chia cắt, đất đai khô cằn, hoàn toàn không có dân cư hay tiện ích đô thị.
- **Từ khóa tìm kiếm (Search Query):** "remote mountainous rural landscape Vietnam isolated land no infrastructure"
- **Nguồn báo chí uy tín (Source):** Vietnam Geography / VTV Travel
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Vietnam Rural Media`.
- **Text Overlay:** Không.

---

### [CH02_SC026]
- **Thoại:** "Đối với những doanh nghiệp không có năng lực làm đại đô thị nhưng vẫn muốn thâu tóm đất đai, họ buộc phải chuyển sang một chiêu thức tài chính nguy hiểm hơn rất nhiều." (32 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bàn họp thẩm định tín dụng ngân hàng với ánh sáng đèn huỳnh quang lạnh, tập hồ sơ "Dự Án Đầu Tư Sân Golf Độc Lập" đặt cạnh hợp đồng thế chấp quyền sử dụng đất và các chồng trái phiếu doanh nghiệp, tạo cầu nối kịch tính sang Chương 3.
- **Chủ thể & Hành động an toàn:** Chuyên viên thẩm định dùng dấu mộc đỏ đóng mạnh lên hợp đồng tín dụng.
- **Camera & Điện ảnh:** Cinematic slow tilt up từ con dấu đỏ lên ánh mắt nghiêm nghị của người thẩm định, chuyển đổi ánh sáng sang tông Slate lạnh `#1E293B`.
- **Text Overlay:** Không.
"""

def build_chapter_03():
    return """---
file_name: "chapter_03_visual_plus.md"
stage: "Phase 12+B — Tri-Track Multimodal Storyboard Matrix"
episode: "san-golf-lo-co-may-ngon-dat"
chapter: 3
total_scenes: 31
word_count: 592
modality_distribution:
  veo_ai: 14 (45.2%)
  infographic_data: 8 (25.8%)
  b_roll_real: 9 (29.0%)
compliance:
  timing_rule: "100% scenes <= 26 words (mean 19.1 words/scene, max 25 words)"
  pipeline: "I2V+ Tri-Track (Track 1: Veo 3.1 Lite | Track 2: FootageHunter Fair Use B-Roll | Track 3: Flow Infographics)"
  color_dna: "Canonical Slate #1E293B, #2A323D, Warm Ivory #FAF7EE, Glowing Amber #F59E0B, Emerald Green #10B981, Coral Red #EF5350"
---

<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/san-golf-lo-co-may-ngon-dat/chapter_03_visual_plus.md
- Activated Persona: the_scene_architect + the_visual_storyteller
- Activated Skill: visual_prompter/SKILL.md (/generate_visual_prompts_plus Stage 2)
- Source Documents Consulted:
  * episodes/san-golf-lo-co-may-ngon-dat/chapter_03.md
  * episodes/san-golf-lo-co-may-ngon-dat/visual_storyboard_blueprint_plus.md
  * episodes/san-golf-lo-co-may-ngon-dat/08_chapter_briefs.md
  * episodes/san-golf-lo-co-may-ngon-dat/vault/00_Global_Vision_Synthesis.md
- Execution Timestamp: 2026-09-22 16:26
-->

# KỊCH BẢN THỊ GIÁC ĐA THỨC (TRI-TRACK STORYBOARD) — CHƯƠNG 3
## TẬP: KINH TẾ HỌC SÂN GOLF — NGHỊCH LÝ THUA LỖ VÀ BÀN CỜ ĐỊA TÔ TỶ ĐÔ
### CHƯƠNG 3: ẢO ẢNH ĐỊNH GIÁ DCF 50 NĂM VÀ BẪY ĐÒN BẨY TRÁI PHIẾU

---

### [CH03_SC001]
- **Thoại:** "Khi một dự án sân golf được vẽ ra ở một vùng đất xa xôi hẻo lánh, nơi không có người dân nào đủ tiền mua biệt thự nghỉ dưỡng." (27 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Flycam góc rộng bay qua một thung lũng miền núi hoang vắng, đất đai cằn cỗi xa trung tâm đô thị, chỉ có vài ngôi nhà tranh thưa thớt bên con đường đất đỏ gập ghềnh.
- **Từ khóa tìm kiếm (Search Query):** "remote valley barren rural landscape Vietnam mountainous undeveloped area"
- **Nguồn báo chí uy tín (Source):** VTV Cần Thơ / Truyền hình Vĩnh Long
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Vietnam Rural Landscape Archive`.
- **Text Overlay:** Không.

---

### [CH03_SC002]
- **Thoại:** "Thì mục tiêu của doanh nghiệp chắc chắn không phải là bán nhà như mô hình mỏ neo địa tô." (19 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bàn họp kính của ban lãnh đạo doanh nghiệp đầu tư tài chính, trên bàn trải ra bản đồ quy hoạch một sân golf vùng sâu, nhưng bên cạnh không hề có bản vẽ thiết kế biệt thự hay phân khu đô thị nào.
- **Chủ thể & Hành động an toàn:** Chủ tịch doanh nghiệp ngồi dựa lưng vào ghế da, ngón tay gõ nhẹ vào xấp hồ sơ pháp lý dự án.
- **Camera & Điện ảnh:** Cinematic slow dolly in, ánh sáng phòng họp xám slate `#1E293B` đĩnh đạc, viền mực thanh lịch.
- **Text Overlay:** Không.

---

### [CH03_SC003]
- **Thoại:** "Ở những tọa độ này, sân golf biến thành một công cụ tài chính hoàn hảo để kích hoạt cỗ máy đòn bẩy tín dụng." (24 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Financial Asset Transformation (Sơ đồ biến hóa công cụ tài chính).
- **Tiêu đề & Dữ liệu cốt lõi:** Sơ đồ 3 bước chuyển hóa tài sản: `LAND USE RIGHTS (QUYỀN SỬ DỤNG ĐẤT)` $\to$ `GOLF PROJECT APPROVAL (PHÊ DUYỆT DỰ ÁN SÂN GOLF)` $\to$ `BANK COLLATERAL & BONDS (TÀI SẢN THẾ CHẤP & TRÁI PHIẾU)`.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, các mũi tên chuyển dịch màu vàng hổ phách `#F59E0B` phát sáng tuần tự.
- **Bảng màu & Hiệu ứng chuyển động:** Điểm nhấn vàng hổ phách và cam cảnh báo.
- **Text Overlay:** `BOTTOM LEFT | FINANCIAL LEVERAGE ACTIVATION`.

---

### [CH03_SC004]
- **Thoại:** "Bản chất của chiêu thức này nằm ở kỹ thuật định giá dòng tiền chiết khấu, hay còn gọi là mô hình DCF." (22 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Màn hình máy tính trong phòng thẩm định rủi ro ngân hàng hiển thị công thức chiết khấu dòng tiền tài chính: $PV = \sum \frac{CF_t}{(1+r)^t}$ với các dòng tiền tương lai kéo dài suốt 50 năm dự án.
- **Chủ thể & Hành động an toàn:** Chuyên viên tài chính gõ các tham số lãi suất chiết khấu và dòng tiền giả định trên bàn phím.
- **Camera & Điện ảnh:** Steady camera shot cận cảnh màn hình và các công thức toán tài chính, ánh sáng xanh dịu mắt.
- **Text Overlay:** `BOTTOM LEFT | DCF VALUATION MODEL (50 YEARS)`.

---

### [CH03_SC005]
- **Thoại:** "Một khu đất thô rộng một trăm héc-ta ở vùng sâu vùng xa, chi phí đền bù giải phóng mặt bằng thực tế chỉ tốn khoảng vài ba trăm tỷ đồng." (29 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Initial Land Cost Breakdown (Biểu đồ chi phí đền bù đất ban đầu).
- **Tiêu đề & Dữ liệu cốt lõi:** Thẻ chi phí đất thô 100 ha: `ACTUAL LAND CLEARANCE COST: 300 - 400 BILLION VND`. Ghi chú bên dưới: Giá đền bù đất nông nghiệp thô theo khung giá cũ của địa phương.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, cột chi phí màu xám bạc nhỏ gọn ở góc dưới.
- **Bảng màu & Hiệu ứng chuyển động:** Điểm nhấn xám slate và ngà kem.
- **Text Overlay:** `BOTTOM LEFT | ACTUAL LAND COST: ~400 BILLION VND`.

---

### [CH03_SC006]
- **Thoại:** "Nếu để nguyên trạng là đất nông nghiệp, không một ngân hàng nào chấp nhận định giá khu đất này quá năm trăm tỷ đồng để cho vay." (27 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Phòng thẩm định hồ sơ tín dụng ngân hàng: Cán bộ ngân hàng lật giở cuốn sổ đỏ đất nông nghiệp và đóng dấu từ chối hoặc áp hạn mức định giá rất thấp.
- **Từ khóa tìm kiếm (Search Query):** "bank credit risk appraisal land title collateral valuation Vietnam"
- **Nguồn báo chí uy tín (Source):** VTV Khớp lệnh / Báo Đầu Tư
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Banking Risk Archive`.
- **Text Overlay:** Không.

---

### [CH03_SC007]
- **Thoại:** "Thế nhưng, khi khu đất được phê duyệt quy hoạch thành dự án sân golf thương mại với thời hạn sử dụng đất năm mươi năm, chiếc đũa phép tài chính bắt đầu phát huy tác dụng." (34 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bàn làm việc của cơ quan quản lý nhà nước, một quyết định phê duyệt chủ trương đầu tư dự án sân golf 50 năm được đóng dấu mộc đỏ tươi, bên cạnh bản đồ quy hoạch 18 lỗ với các đường vẽ uốn lượn sắc màu.
- **Chủ thể & Hành động an toàn:** Cán bộ quản lý nâng tài liệu lên kiểm tra lần cuối trước khi bàn giao cho chủ đầu tư.
- **Camera & Điện ảnh:** Cinematic slow dolly out, ánh sáng ban ngày trang trọng, độ sắc nét cao của văn bản hành chính.
- **Text Overlay:** `BOTTOM LEFT | 50-YEAR COMMERCIAL LAND USE`.

---

### [CH03_SC008]
- **Thoại:** "Đơn vị thẩm định giá sẽ không định giá dự án dựa trên chi phí đất thực tế đã bỏ ra." (19 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** `@dcf_valuation_report.jpg ->` A 2D warm cinematic editorial illustration faithfully preserving the exact appearance of the appraisal report depicted in the reference photo. Một cuốn chứng thư thẩm định giá bìa da màu xanh thẫm dày hàng trăm trang mở ra các bảng tính dòng tiền chiết khấu 50 năm với dấu mộc thẩm định đỏ rực rỡ.
- **Chủ thể & Hành động an toàn:** Thẩm định viên độc lập lật từng trang bảng tính dòng tiền dự báo.
- **Camera & Điện ảnh:** Steady camera shot cận cảnh bề mặt văn bản và dấu mộc đỏ, ánh sáng ngà kem `#FAF7EE`.
- **Text Overlay:** Không.

---

### [CH03_SC009]
- **Thoại:** "Họ định giá dựa trên dòng tiền giả định trong tương lai suốt nửa thế kỷ tới." (16 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** 50-Year Discounted Cash Flow Projection (Đồ thị dòng tiền giả định 50 năm).
- **Tiêu đề & Dữ liệu cốt lõi:** Đồ thị dải sóng dòng tiền giả định suốt 50 năm: Các thanh cột doanh thu bán thẻ hội viên và vé chơi golf màu xanh ngọc `#10B981` tăng trưởng đều đặn 8%/năm, tạo ra tổng dòng tiền tích lũy khổng lồ được chiết khấu về hiện tại.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, trục thời gian từ Năm 1 đến Năm 50, đường cong chiết khấu mượt mà.
- **Bảng màu & Hiệu ứng chuyển động:** Các cột dòng tiền tương lai dâng cao kích hoạt con số định giá hiện tại.
- **Text Overlay:** `BOTTOM LEFT | 50-YEAR PROJECTED CASH FLOWS`.

---

### [CH03_SC010]
- **Thoại:** "Trên bảng tính máy tính, các chuyên viên thẩm định đưa vào những giả định vô cùng màu hồng." (18 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bàn tay chuyên viên tài chính đang điều chỉnh thanh trượt giả định tỷ lệ lấp đầy (Occupancy Rate) từ 50% lên 90% trên phần mềm phân tích tài chính, các con số doanh thu lập tức nhảy vọt xanh rực.
- **Chủ thể & Hành động an toàn:** Cử chỉ kéo chuột dứt khoát trên phần mềm bảng tính.
- **Camera & Điện ảnh:** Steady camera shot góc cận màn hình máy tính, phản chiếu ánh sáng dịu mắt.
- **Text Overlay:** Không.

---

### [CH03_SC011]
- **Thoại:** "Họ giả định sân golf sẽ luôn kín lịch chơi quanh năm suốt ba trăm sáu mươi ngày." (17 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Rosy Operational Assumptions Card (Thẻ tham số giả định màu hồng).
- **Tiêu đề & Dữ liệu cốt lõi:** Thẻ 3 tham số giả định phi thực tế: (1) `OCCUPANCY: 100% CAPACITY (360 DAYS/YEAR)`, (2) `MEMBERSHIP SALES: 1,000 CARDS @ $50,000`, (3) `ANNUAL REVENUE GROWTH: 8% PERPETUAL`.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, 3 khối hộp viền vàng hổ phách `#F59E0B`, chữ màu ngà kem.
- **Bảng màu & Hiệu ứng chuyển động:** Điểm nhấn vàng hổ phách và cam cảnh báo.
- **Text Overlay:** `BOTTOM LEFT | ROSY DCF ASSUMPTIONS`.

---

### [CH03_SC012]
- **Thoại:** "Họ giả định doanh nghiệp sẽ bán hết hàng nghìn thẻ hội viên dài hạn với giá hàng chục nghìn đô la một thẻ." (23 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Lễ công bố bán thẻ hội viên danh dự VIP của một sân golf mới tại khách sạn 5 sao: Các tấm thẻ mạ vàng sáng bóng được trao cho khách hàng danh dự trong ánh đèn flash rực sáng.
- **Từ khóa tìm kiếm (Search Query):** "golf club membership card launch VIP gala dinner Vietnam"
- **Nguồn báo chí uy tín (Source):** Vietnam Golf Magazine / Vietnamnet
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Vietnam Golf Archive`.
- **Text Overlay:** Không.

---

### [CH03_SC013]
- **Thoại:** "Và họ giả định chi phí vận hành sẽ luôn giữ ở mức tối thiểu bất chấp lạm phát." (17 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Cận cảnh bảng sao kê chi phí vận hành phẳng lì trên màn hình máy tính với dòng chi phí bảo dưỡng cỏ bị cố định ở mức phi lý, tương phản với thực tế giá điện nước và phân bón tăng vọt ngoài đời thực.
- **Chủ thể & Hành động an toàn:** Người phân tích nhìn vào bảng số liệu với ánh mắt hoài nghi.
- **Camera & Điện ảnh:** Cinematic slow dolly in, góc máy tập trung vào các con số giả định chi phí cố định.
- **Text Overlay:** Không.

---

### [CH03_SC014]
- **Thoại:** "Bằng cách cộng dồn dòng tiền giả định của năm mươi năm và chiết khấu về hiện tại, khu đất đền bù bốn trăm tỷ bỗng nhiên biến thành một dự án có giá trị định giá lên tới ba nghìn tỷ đồng." (39 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Valuation Surge Waterfall (Biểu đồ thác nước thổi phồng định giá DCF).
- **Tiêu đề & Dữ liệu cốt lõi:** Biểu đồ thác nước chuyển dịch giá trị: Cột 1 `ACTUAL LAND COST: 400 BILLION VND` $\to$ Cột 2 `50-YEAR DCF ASSUMPTIONS (+2,600 BILLION VND)` $\to$ Cột 3 `APPRAISED VALUATION: 3,000 BILLION VND`.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, cột kết quả cao vọt gấp hơn 7 lần cột ban đầu.
- **Bảng màu & Hiệu ứng chuyển động:** Cột định giá 3.000 tỷ vươn cao với viền cam cảnh báo `#FF7043`.
- **Text Overlay:** `BOTTOM LEFT | VALUATION SURGE: 400B -> 3,000B VND`.

---

### [CH03_SC015]
- **Thoại:** "Con số ba nghìn tỷ này được đóng dấu đỏ bởi các công ty thẩm định giá hợp pháp." (17 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Cận cảnh dấu mộc đỏ tròn của công ty thẩm định giá độc lập đóng dứt khoát lên trang cuối của bản chứng thư thẩm định giá, mực đỏ tươi in rõ chữ "ĐỦ ĐIỀU KIỆN LÀM TÀI SẢN BẢO ĐẢM".
- **Chủ thể & Hành động an toàn:** Thẩm định viên ký tên dứt khoát bên cạnh con dấu đỏ.
- **Camera & Điện ảnh:** Steady camera shot cận cảnh văn bản, ánh sáng ngà kem `#FAF7EE` sắc nét.
- **Text Overlay:** Không.

---

### [CH03_SC016]
- **Thoại:** "Với chứng thư định giá ba nghìn tỷ trong tay, doanh nghiệp mang dự án này đến ngân hàng để thế chấp vay vốn." (23 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Trụ sở một ngân hàng thương mại cổ phần lớn tại Hà Nội: Khách hàng doanh nghiệp và cán bộ tín dụng ngồi đàm phán hợp đồng vay vốn tại phòng giao dịch khách hàng doanh nghiệp lớn.
- **Từ khóa tìm kiếm (Search Query):** "commercial bank headquarters corporate credit negotiation meeting Vietnam"
- **Nguồn báo chí uy tín (Source):** VTV Tài chính Kinh doanh / TTXVN
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Banking News Archive`.
- **Text Overlay:** Không.

---

### [CH03_SC017]
- **Thoại:** "Ngay cả khi ngân hàng áp dụng tỷ lệ an toàn nghiêm ngặt là chỉ cho vay sáu mươi phần trăm giá trị định giá." (23 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Loan-to-Value (LTV) Credit Line Card (Thẻ tỷ lệ an toàn vốn vay LTV).
- **Tiêu đề & Dữ liệu cốt lõi:** Thẻ tỷ lệ giải ngân ngân hàng: `LOAN-TO-VALUE (LTV): 60%`. Trên tổng định giá 3.000 tỷ VND, hạn mức tín dụng được duyệt là `BANK DEBT CREDIT: 1,800 BILLION VND`.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, thanh đo tỷ lệ 60% màu vàng hổ phách `#F59E0B`.
- **Bảng màu & Hiệu ứng chuyển động:** Điểm nhấn vàng hổ phách và xanh lục.
- **Text Overlay:** `BOTTOM LEFT | 60% LTV: 1,800 BILLION VND CREDIT`.

---

### [CH03_SC018]
- **Thoại:** "Doanh nghiệp vẫn dễ dàng giải ngân được khoản tín dụng một nghìn tám trăm tỷ đồng tiền mặt." (18 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Máy đếm tiền tự động đếm các cọc tiền mệnh giá 500 nghìn đồng chạy xoẹt xoẹt trong kho tiền ngân hàng, các cọc tiền niêm phong được xếp ngay ngắn vào xe đẩy chuyển tiền.
- **Từ khóa tìm kiếm (Search Query):** "automated cash counting machine money vault bank transfer Vietnam"
- **Nguồn báo chí uy tín (Source):** VTV Thời sự / Vietnamnet
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Banking Operation Archive`.
- **Text Overlay:** Không.

---

### [CH03_SC019]
- **Thoại:** "Hãy nhìn lại tỷ lệ đòn bẩy kinh hoàng này." (9 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Mô hình cán cân tài chính bằng kim loại trên bàn giám đốc kiểm toán: Một viên sỏi nhỏ tượng trưng cho 400 tỷ vốn đất thực tế nâng bổng một tảng đá khổng lồ tượng trưng cho 1.800 tỷ tiền vay nợ.
- **Chủ thể & Hành động an toàn:** Cán cân nghiêng hẳn về một bên tạo cảm giác chông chênh, rủi ro chực chờ sụp đổ.
- **Camera & Điện ảnh:** Cinematic slow dolly in cận cảnh độ nghiêng mất thăng bằng của cán cân, ánh sáng tông Slate lạnh `#1E293B`.
- **Text Overlay:** Không.

---

### [CH03_SC020]
- **Thoại:** "Bỏ ra bốn trăm tỷ tiền vốn thật để gom đất, doanh nghiệp rút về một nghìn tám trăm tỷ đồng tiền mặt từ ngân hàng." (25 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Cash Extraction Leverage Ratio (Biểu đồ đòn bẩy rút tiền mặt ròng).
- **Tiêu đề & Dữ liệu cốt lõi:** So sánh đối xứng: Bỏ ra Vốn thực `REAL EQUITY: 400 BILLION VND` $\to$ Rút về Tiền mặt ngân hàng `CASH EXTRACTED: 1,800 BILLION VND`. Thặng dư tiền mặt rút ròng tức thì: `NET CASH SURPLUS: +1,400 BILLION VND` (Đòn bẩy 4,5 lần vốn tự có).
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, hai cột đối xứng màu đỏ san hô `#EF5350` và vàng hổ phách `#F59E0B`.
- **Bảng màu & Hiệu ứng chuyển động:** Dòng tiền mặt rút ròng vươn cao.
- **Text Overlay:** `BOTTOM LEFT | 4.5X CASH LEVERAGE EXTRACTED`.

---

### [CH03_SC021]
- **Thoại:** "Chưa dừng lại ở đó, khu đất dự án tiếp tục được dùng làm tài sản bảo đảm để phát hành các lô trái phiếu doanh nghiệp." (25 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bản cáo bạch phát hành trái phiếu doanh nghiệp riêng lẻ in ấn sang trọng trên bàn giao dịch chứng khoán, tiêu đề in đậm mã trái phiếu và lãi suất cam kết hấp dẫn.
- **Chủ thể & Hành động an toàn:** Môi giới trái phiếu đang thuyết trình cho các nhà đầu tư cá nhân giàu có.
- **Camera & Điện ảnh:** Steady camera shot, ánh sáng vàng ấm phản chiếu từ sảnh giao dịch tài chính.
- **Text Overlay:** `BOTTOM LEFT | CORPORATE BOND ISSUANCE`.

---

### [CH03_SC022]
- **Thoại:** "Hàng nghìn tỷ đồng trái phiếu với lãi suất từ mười một đến mười hai phần trăm được bán ra cho các nhà đầu tư." (23 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** High-Yield Bond Structure Card (Thẻ cấu trúc trái phiếu lãi suất cao).
- **Tiêu đề & Dữ liệu cốt lõi:** Thẻ thông tin trái phiếu: `COUPON RATE: 11% - 12% / YEAR`. Quy mô phát hành: `TOTAL BOND VALUE: 1,500 - 2,000 BILLION VND`. Nghĩa vụ trả lãi hàng năm: `ANNUAL INTEREST EXPENSE: ~160 - 200 BILLION VND / YEAR`.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, viền đỏ san hô `#EF5350`, cảnh báo áp lực nợ lớn.
- **Bảng màu & Hiệu ứng chuyển động:** Con số lãi suất phát sáng màu cam cảnh báo `#FF7043`.
- **Text Overlay:** `BOTTOM LEFT | BOND COUPON: 11% - 12%/YEAR`.

---

### [CH03_SC023]
- **Thoại:** "Dòng tiền khổng lồ huy động được từ ngân hàng và trái phiếu không được tái đầu tư nhiều vào việc chăm sóc mặt cỏ." (23 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Đại công trường một dự án sân golf tại vùng xa: Vài chiếc máy ủi nằm im lìm phủ bụi, đường dẫn vào sân ngổn ngang đá dăm, tiến độ thi công đình trệ suốt nhiều tháng.
- **Từ khóa tìm kiếm (Search Query):** "delayed construction golf resort heavy equipment idle dust Vietnam"
- **Nguồn báo chí uy tín (Source):** VTV Thời sự / Báo Lao Động
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Vietnam Construction Archive`.
- **Text Overlay:** Không.

---

### [CH03_SC024]
- **Thoại:** "Nó được doanh nghiệp rút ra để đảo nợ, mua bán sáp nhập hoặc tài trợ cho các dự án bất động sản khác." (23 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Sơ đồ dòng tiền nhiều nhánh vẽ trên bảng kính phòng họp tài chính: Dòng tiền từ dự án sân golf được mũi tên chỉ sang mua cổ phần công ty con, thâu tóm quỹ đất khác và thanh toán các khoản nợ ngắn hạn.
- **Chủ thể & Hành động an toàn:** Giám đốc tài chính xóa bớt một mũi tên và vẽ tiếp đường dẫn dòng tiền sang dự án mới.
- **Camera & Điện ảnh:** Cinematic slow dolly in, góc máy ngang tầm mắt, nét vẽ mực đen sắc sảo trên mặt kính trong suốt.
- **Text Overlay:** Không.

---

### [CH03_SC025]
- **Thoại:** "Sân golf lúc này chỉ là một tấm bình phong tài sản bảo đảm." (12 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Một tấm bình phong bằng gỗ sẫm màu chạm khắc hoa văn sân golf đặt giữa phòng làm việc, nhưng phía sau tấm bình phong là một két sắt ngân hàng mở toang với các chồng hồ sơ nợ vay xếp lớp.
- **Chủ thể & Hành động an toàn:** Cử chỉ ẩn dụ tinh tế thể hiện vai trò lá chắn tài sản trên bảng cân đối.
- **Camera & Điện ảnh:** Cinematic slow tracking shot từ trước bình phong lướt ra sau bình phong, ánh sáng ngà kem và xám slate.
- **Text Overlay:** Không.

---

### [CH03_SC026]
- **Thoại:** "Một công cụ kỹ thuật tài chính để tạo ra thanh khoản ảo từ việc định giá đất đai trong tương lai." (20 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Sàn giao dịch trái phiếu doanh nghiệp riêng lẻ: Đồ thị thanh khoản và bảng giá khớp lệnh trái phiếu bất động sản nhảy số liên tục, nhà đầu tư theo dõi với nét mặt căng thẳng.
- **Từ khóa tìm kiếm (Search Query):** "corporate bond trading platform electronic screen financial market Vietnam"
- **Nguồn báo chí uy tín (Source):** VTV Khớp lệnh / HNX
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: HNX Bond Market Archive`.
- **Text Overlay:** Không.

---

### [CH03_SC027]
- **Thoại:** "Khi nhìn vào bức tranh này, nhiều người dễ đi đến kết luận rằng mọi sân golf đều là công cụ đầu cơ và lừa dối." (25 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Một góc phố quán cà phê nơi những người dân và nhà đầu tư đang đọc báo giấy tài chính với các dòng tít giật gân về nợ trái phiếu sân golf, nét mặt đầy vẻ hoài nghi và bức xúc.
- **Chủ thể & Hành động an toàn:** Người đọc báo trầm ngâm lắc đầu, đặt tách cà phê xuống bàn.
- **Camera & Điện ảnh:** Cinematic slow dolly out, ánh sáng ban mai nhẹ nhàng, không khí đời thường sâu lắng.
- **Text Overlay:** Không.

---

### [CH03_SC028]
- **Thoại:** "Dư luận xã hội thường mặc định sân golf là một cỗ máy ngốn đất vô tích sự và chỉ làm lợi cho giới đầu cơ." (24 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Cảnh hàng rào thép gai và cổng khóa kín của một dự án sân golf bị người dân địa phương và báo chí phản ánh vì chiếm dụng đất nông nghiệp nhưng để hoang nhiều năm.
- **Từ khóa tìm kiếm (Search Query):** "fenced off abandoned golf project gate sign protest Vietnam news"
- **Nguồn báo chí uy tín (Source):** VTV Chuyển động 24h / Báo Dân Trí
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Vietnam Investigative News`.
- **Text Overlay:** Không.

---

### [CH03_SC029]
- **Thoại:** "Thế nhưng, sự thật có hoàn toàn là một màu đen như vậy?" (12 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bức tranh phong cảnh chia đôi: Nửa bên trái là dự án bỏ hoang xám xịt dưới trời mưa giông, nửa bên phải bừng sáng nắng vàng rực rỡ với thảm cỏ xanh mướt và bờ biển cát trắng nhiệt đới.
- **Chủ thể & Hành động an toàn:** Chuyển giao nhận thức từ sự hoài nghi sang góc nhìn đa chiều biện chứng.
- **Camera & Điện ảnh:** Cinematic slow pan từ vùng tối sang vùng sáng, ánh sáng mặt trời rọi qua mây tạo hiệu ứng hy vọng.
- **Text Overlay:** Không.

---

### [CH03_SC030]
- **Thoại:** "Liệu có mô hình sân golf nào thực sự tạo ra giá trị kinh tế bền vững mà không cần dựa dẫm vào phân lô bán nền hay đòn bẩy tài chính?" (29 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** `@golf_course_aerial_links.jpg ->` A 2D warm cinematic editorial illustration faithfully preserving the exact landscape depicted in the reference photo. Đại cảnh flycam ngoạn mục một sân golf dạng links đẳng cấp thế giới ven bờ biển Miền Trung, cồn cát trắng tự nhiên ôm trọn thảm cỏ xanh uốn lượn cạnh làn sóng biển Đông xanh ngắt dưới nắng vàng rực rỡ.
- **Chủ thể & Hành động an toàn:** Không gian thiên nhiên tráng lệ, tôn vinh giá trị dịch vụ du lịch thể thao đích thực.
- **Camera & Điện ảnh:** Cinematic slow crane up góc rộng, gió biển thổi nhẹ hàng dừa và thảm cỏ, mở màn cho Chương Phản Đề Thép CH04.
- **Text Overlay:** Không.

---

### [CH03_SC031]
- **Thoại:** "Câu trả lời nằm ở một dải bờ biển Miền Trung đầy nắng gió và bài học trị giá hai tỷ đô la của người Thái." (24 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Biển chỉ dẫn quốc tế tại sân bay quốc tế Suvarnabhumi (Bangkok, Thái Lan) và sân bay quốc tế Đà Nẵng: "WELCOME TO INTERNATIONAL GOLF DESTINATION", đoàn golfer quốc tế tấp nập kéo túi gậy rảo bước.
- **Từ khóa tìm kiếm (Search Query):** "golf tourism welcome sign airport Bangkok Danang international travelers"
- **Nguồn báo chí uy tín (Source):** Tourism Authority of Thailand (TAT) / Danang Tourism
- **Yêu cầu xử lý Fair Use:** Cắt 4.0s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: TAT Tourism Archive`.
- **Text Overlay:** `BOTTOM LEFT | DESTINATION GOLF CLUSTERS`.
"""

def main():
    chapters = {
        2: build_chapter_02(),
        3: build_chapter_03(),
    }
    
    for ch_num, content in chapters.items():
        ch_str = f"{ch_num:02d}"
        file_path = os.path.join(EPISODE_DIR, f"chapter_{ch_str}_visual_plus.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Written: {file_path}")
        # Run export
        cmd = ["python3", os.path.join(EPISODE_DIR, "export_chapter_tri_track.py"), str(ch_num)]
        subprocess.run(cmd, check=True)

if __name__ == "__main__":
    main()
