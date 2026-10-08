# CONTEXT TIER VOCABULARY — KHO TỪ VỰNG BỐI CẢNH DÙNG CHUNG CHO B-ROLL
## Master Documentary Context Lexicon (VPOS Standard V1.0)

> **Mục đích:** Bộ từ điển bối cảnh chuẩn hóa dùng chung cho mọi episode trong dự án.  
> **Nguyên tắc cốt lõi:** Khi LLM (`the_scene_architect`, `the_footage_hunter`) sinh `search_query` trong `broll_manifest_chapter_XX.json`, **BẮT BUỘC PHẢI CHỌN TỪ HOẶC TỔ HỢP TỪ TRONG DANH SÁCH NÀY**, kết hợp với `[Tên Thực Thể / Dự Án]` và `[Nguồn tin Tier 1]`.  
> ⛔ **CẤM TUYỆT ĐỐI:** Tự ý bịa ra các hành động vi mô ("đội mũ bảo hộ chỉ tay"), thông số kỹ thuật vi mô ("SCADA", "màn hình lớn"), tính từ cảm xúc ("khẩn trương", "50 percent"), hay góc quay camera ("close up", "flycam").

---

## 🏛️ 1. CỤM TÀI CHÍNH, TIỀN TỆ & CÔNG QUYỀN VĨ MÔ (`TAI_CHINH_CONG_QUYEN`)

Áp dụng cho các phân cảnh về chính sách tài khóa, tiền tệ, ngân sách nhà nước, nợ công, lãi suất, điều hành vĩ mô, nghị trường và thể chế:

| Từ Vựng Bối Cảnh Chuẩn (Context Keywords) | Không Khí Thị Giác Khán Giả Thấy | Cụm Truy Vấn Mẫu (YouTube Tier 1) |
|---|---|---|
| `kỳ họp quốc hội` / `nghị trường` | Hội trường Diên Hồng, đại biểu bấm nút biểu quyết, thảo luận đoàn | `"kỳ họp quốc hội vtv1"`, `"biểu quyết quốc hội vtv"` |
| `phiên họp chính phủ` / `họp thường kỳ` | Bàn họp chữ U, lãnh đạo chủ trì, bộ trưởng phát biểu | `"phiên họp chính phủ thường kỳ vtv"`, `"họp thường kỳ chính phủ vnews"` |
| `họp báo chính phủ` / `họp báo đối thoại` | Bục phát biểu, phóng viên tác nghiệp, micro họp báo | `"họp báo chính phủ thường kỳ vtv"`, `"họp báo bộ tài chính"` |
| `kho bạc nhà nước` / `ngân sách nhà nước` | Trụ sở kho bạc, quầy giao dịch vốn nhà nước, công quỹ | `"kho bạc nhà nước vtv"`, `"thời sự kho bạc nhà nước vnews"` |
| `ngân hàng trung ương` / `ngân hàng nhà nước` | Trụ sở 49 Lý Thái Tổ, phòng họp điều hành chính sách tiền tệ | `"ngân hàng nhà nước vtv"`, `"điều hành lãi suất ngân hàng nhà nước vtv24"` |
| `kho quỹ ngân hàng` / `kiểm đếm tiền tệ` | Máy đếm tiền tốc độ cao, đóng thếp tiền, kho quỹ kiên cố | `"kho quỹ ngân hàng vtv"`, `"kiểm đếm tiền mặt ngân hàng vtv24"` |
| `thị trường chứng khoán` / `sàn giao dịch` | Bảng điện tử nhấp nháy xanh đỏ, sàn giao dịch tài chính | `"thị trường chứng khoán vtv24"`, `"sàn chứng khoán hose vtv"` |
| `wall street financial district` | Phố tài chính Wall Street, sàn NYSE, người đi bộ tài chính Mỹ | `"Wall Street financial district 4k bloomberg"`, `"NYSE trading floor cnbc"` |
| `federal reserve central bank` | Trụ sở Fed Washington, phòng họp Jerome Powell | `"Federal Reserve press conference cnbc"`, `"Jerome Powell speech bloomberg"` |

---

## 🏗️ 2. CỤM ĐẠI CÔNG TRƯỜNG & HẠ TẦNG KỸ THUẬT (`DAI_CONG_TRUONG_HA_TANG`)

Áp dụng cho các phân cảnh về đầu tư công, xây dựng cao tốc, hầm đèo, cầu cạn, giải ngân hạ tầng, địa chất:

| Từ Vựng Bối Cảnh Chuẩn (Context Keywords) | Không Khí Thị Giác Khán Giả Thấy | Cụm Truy Vấn Mẫu (YouTube Tier 1) |
|---|---|---|
| `tiến độ cao tốc` / `đại công trường` | Đại cảnh công trường trải dài, đoàn xe máy xúc ủi hoạt động | `"tiến độ cao tốc bắc nam vtv"`, `"đại công trường cao tốc vnews"` |
| `thi công hầm đường bộ` / `khoan hầm qua núi` | Miệng hầm xuyên núi, máy khoan hầm, gương hầm rực sáng | `"thi công hầm đèo cả vnews"`, `"khoan hầm cao tốc bắc nam vtv"` |
| `lao lắp dầm cầu` / `cầu cạn vượt sông` | Cẩu tháp khổng lồ lao dầm Super-T, trụ cầu cạn sừng sững | `"thi công cầu vượt sông vtv"`, `"lao dầm cầu cao tốc báo giao thông"` |
| `thảm nhựa cao tốc` / `mặt đường bê tông nhựa` | Xe rải nhựa nóng bốc khói, lu rung san phẳng mặt đường | `"thảm nhựa cao tốc bắc nam báo lao động"`, `"thi công thảm nhựa vtv"` |
| `khảo sát hiện trường` / `kiểm tra tiến độ` | Đoàn kiểm tra trên công trường, bản đồ thiết kế thực địa | `"kiểm tra tiến độ công trình vtv"`, `"lãnh đạo thị sát cao tốc vnews"` |
| `megaproject construction 4k` | Đại công trường hạ tầng quốc tế, cầu dây văng, hầm ngầm | `"infrastructure megaproject construction b-roll 4k"`, `"highway construction b-roll"` |

---

## 🏭 3. CỤM CÔNG NGHIỆP NẶNG & CHẾ TẠO CƠ KHÍ (`CONG_NGHIEP_NANG`)

Áp dụng cho các phân cảnh về luyện kim, sản xuất ô tô, cơ khí chính xác, tự chủ công nghiệp, hóa chất:

| Từ Vựng Bối Cảnh Chuẩn (Context Keywords) | Không Khí Thị Giác Khán Giả Thấy | Cụm Truy Vấn Mẫu (YouTube Tier 1) |
|---|---|---|
| `luyện thép lò cao` / `dòng thép lỏng` | Dòng thép nóng chảy 1500°C tuôn trào, tia lửa rực sáng xưởng đúc | `"thép hòa phát dung quất vtv"`, `"nhà máy luyện thép hòa phát vnews"` |
| `dây chuyền cán thép` / `phôi thép cuộn` | Băng chuyền cán phôi thép đỏ rực, cuộn thép thành phẩm | `"dây chuyền cán thép vtv"`, `"xuất khẩu thép cuộn hòa phát vtv24"` |
| `robot hàn thân vỏ` / `lắp ráp ô tô` | Cánh tay robot tự động phát tia lửa hàn khung gầm/cabin | `"nhà máy vinfast hải phòng vtv"`, `"khu liên hợp thaco chu lai vtv"` |
| `xưởng cơ khí chế tạo` / `gia công chính xác` | Máy cắt laser CNC, phay tiện chi tiết cơ khí lớn | `"công nghiệp cơ khí việt nam vtv"`, `"nhà máy cơ khí chế tạo thaco industries"` |
| `semiconductor fab cleanroom` | Phòng sạch bán dẫn ánh sáng vàng, kỹ sư đồ bảo hộ trắng | `"semiconductor fabrication cleanroom b-roll 4k"`, `"tsmc chip fab bloomberg"` |
| `industrial manufacturing automation` | Dây chuyền tự động hóa công nghiệp robot hiện đại toàn cầu | `"advanced manufacturing robotic automation 4k"`, `"smart factory b-roll 4k"` |

---

## 🚢 4. CỤM LOGISTICS, HÀNH LANG & CẢNG BIỂN (`LOGISTICS_HANG_HAI`)

Áp dụng cho các phân cảnh về chuỗi cung ứng, xuất nhập khẩu, đường sắt cao tốc, vận tải hàng hải, kho bãi:

| Từ Vựng Bối Cảnh Chuẩn (Context Keywords) | Không Khí Thị Giác Khán Giả Thấy | Cụm Truy Vấn Mẫu (YouTube Tier 1) |
|---|---|---|
| `cảng biển container` / `bốc dỡ hàng hải` | Cẩu giàn STS bốc dỡ container, tàu mẹ viễn dương cập cầu | `"cảng biển chu lai vtv"`, `"cảng cái mép thị vải vtv"`, `"cảng hải phòng vnews"` |
| `kho bãi logistics` / `trung tâm phân phối` | Xe nâng hàng di chuyển pallet, bãi container cao ngút ngàn | `"kho bãi logistics vtv"`, `"trung tâm logistics thilogi chu lai"` |
| `đoàn tàu bắc nam` / `hành lang đường sắt` | Tuyến ray đôi, đoàn tàu lướt qua đèo Hải Vân hoặc biển | `"tàu hỏa bắc nam đèo hải vân 4k"`, `"đường sắt việt nam vtv"` |
| `đường sắt tốc độ cao` / `shinkansen` | Đoàn tàu viên đạn lướt với vận tốc 300+ km/h, nhà ga hiện đại | `"shinkansen bullet train 4k"`, `"high speed rail station b-roll 4k"` |
| `vận tải hàng hóa đường bộ` / `đoàn xe container` | Đoàn xe đầu kéo chạy trên cao tốc, cửa khẩu thông thương | `"vận tải hàng hóa cửa khẩu vtv"`, `"đoàn xe container cảng biển vnews"` |

---

## ⚡ 5. CỤM NĂNG LƯỢNG, ĐIỆN LỰC & HẠ TẦNG SỐ (`NANG_LUONG_CONG_NGHE`)

Áp dụng cho các phân cảnh về an ninh năng lượng, điện than, điện khí, điện hạt nhân, trung tâm dữ liệu AI:

| Từ Vựng Bối Cảnh Chuẩn (Context Keywords) | Không Khí Thị Giác Khán Giả Thấy | Cụm Truy Vấn Mẫu (YouTube Tier 1) |
|---|---|---|
| `nhà máy nhiệt điện` / `điện khí lng` | Tháp làm mát bốc hơi, đường ống dẫn khí, tuabin khí phát điện | `"nhà máy điện khí lng vtv"`, `"nhiệt điện thái bình vnews"` |
| `trạm biến áp cao thế` / `đường dây 500kv` | Cột điện thép sừng sững, chuỗi sứ cách điện, trạm 500kV | `"đường dây 500kv mạch 3 vtv"`, `"trạm biến áp 500kv vnews"` |
| `trang trại năng lượng tái tạo` | Cánh đồng điện gió ngoài khơi, tấm pin mặt trời trải dài | `"điện gió ngoài khơi vtv"`, `"cánh đồng điện mặt trời vnews"` |
| `nuclear power plant cooling tower` | Tháp làm mát nhà máy điện hạt nhân hình hyperbol khổng lồ | `"nuclear power plant cooling tower steam b-roll 4k bloomberg"` |
| `ai data center server farm` | Dàn server nhấp nháy đèn LED xanh/hổ phách, luồng khí lạnh | `"data center server room b-roll 4k"`, `"supercomputer server racks b-roll"` |

---

## 🏢 6. CỤM QUẢN TRỊ TẬP ĐOÀN & ĐẠI HỘI DOANH NGHIỆP (`QUAN_TRI_TAP_DOAN`)

Áp dụng cho các phân cảnh về ban lãnh đạo, đại hội đồng cổ đông, chiến lược doanh nghiệp, ký kết đầu tư:

| Từ Vựng Bối Cảnh Chuẩn (Context Keywords) | Không Khí Thị Giác Khán Giả Thấy | Cụm Truy Vấn Mẫu (YouTube Tier 1) |
|---|---|---|
| `đại hội đồng cổ đông` / `đhđcđ` | Khán phòng hội nghị lớn, cổ đông giơ thẻ biểu quyết, chủ tịch | `"đại hội đồng cổ đông hòa phát"`, `"đhđcđ thaco"` |
| `tòa nhà trụ sở` / `trụ sở tập đoàn` | Kiến trúc ngoại thất kính hiện đại, sảnh đón tiếp uy nghi | `"tòa nhà trụ sở tập đoàn vtv"`, `"trụ sở sala thaco thủ thiêm"` |
| `lễ ký kết hợp tác` / `thỏa thuận chiến lược` | Hai bên trao đổi văn kiện ký kết, bắt tay trước backdrop | `"lễ ký kết hợp tác đầu tư vtv"`, `"ký kết thỏa thuận chiến lược vnews"` |
| `corporate boardroom meeting` | Phòng họp hội đồng quản trị kính sang trọng, thuyết trình số liệu | `"corporate boardroom meeting b-roll 4k"`, `"executive business meeting 4k"` |

---

## 🌾 7. CỤM ĐỜI SỐNG DÂN SINH, MẶT BẰNG & XÃ HỘI (`DOI_SONG_XA_HOI`)

Áp dụng cho các phân cảnh về an sinh, tái định cư, thu hồi đất, nông nghiệp thực tế, người tiêu dùng:

| Từ Vựng Bối Cảnh Chuẩn (Context Keywords) | Không Khí Thị Giác Khán Giả Thấy | Cụm Truy Vấn Mẫu (YouTube Tier 1) |
|---|---|---|
| `giải phóng mặt bằng` / `cắm mốc ranh giới` | Cán bộ đo đạc ranh giới đất đai, cắm cọc tiêu, đối thoại | `"giải phóng mặt bằng cao tốc vtv"`, `"bàn giao mặt bằng thi công vnews"` |
| `khu tái định cư` / `nhà ở khang trang` | Khu dân cư mới đường nhựa sạch sẽ, nhà kiên cố, trẻ em chơi | `"khu tái định cư cao tốc bắc nam vtv"`, `"an sinh tái định cư vnews"` |
| `mùa màng đồng lúa` / `nông thôn việt nam` | Cánh đồng lúa thanh bình, máy gặt đập liên hợp thu hoạch | `"mùa vàng đồng lúa miền trung vtv"`, `"nông dân thu hoạch lúa vtv"` |
| `siêu thị tiêu dùng` / `sức mua thị trường` | Khách hàng mua sắm thực phẩm, quầy kệ hàng hóa đầy ắp | `"sức mua thị trường bán lẻ vtv24"`, `"người tiêu dùng siêu thị vtv"` |

---

## 📋 NGUYÊN TẮC ÁP DỤNG TRONG PIPELINE

1. **Khi soạn `broll_manifest_chapter_XX.json`:**
   - Trường `visual_intent`: Thoải mái mô tả chi tiết hình tượng, hành động, không khí phục vụ audit (Ví dụ: *"Kỹ sư vận hành hệ thống điều khiển trung tâm giám sát luồng nhiệt lò cao"*).
   - Trường `search_query`: **BẮT BUỘC** rút gọn theo công thức:
     ```text
     [Chủ thể vĩ mô / Doanh nghiệp] + [Context Keyword từ bảng này] + [Nguồn Tier 1]
     ```
     *Ví dụ chuẩn:* `"lò cao thép hòa phát dung quất vtv"`, `"tiến độ cao tốc bắc nam vnews"`, `"kho bạc nhà nước vtv"`.
2. **Loại trừ tuyệt đối:**
   - Cấm ghép các thuật ngữ SCADA, PLC, micromet, close-up, drone, flycam, 50 percent, đóng bó thanh khoản vào trường `search_query`.
