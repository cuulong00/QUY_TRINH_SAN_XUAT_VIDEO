# visual_storyboard_blueprint.md — Kế Hoạch Trực Quan Tổng Thể & Giao Thức I2V (Pha 12)

> **Tập phim:** Thái Lan Vết Xe Đổ Nhật Bản: Sự Thật Đằng Sau Lãi Suất 1%  
> **Mã tập (Slug):** `thai-lan-vet-xe-do-nhat-ban`  
> **Phong cách trực quan chủ đạo:** Editorial Flat Noir (Đồ họa Noir Báo chí Phẳng 2D Vector kết hợp Cinematic Realistic Simulation)  
> **Tỷ lệ khung hình:** 16:9 Cinematic  

---

## 1. Triết Lý Nghệ Thuật & Không Gian Bối Cảnh (World Building Philosophy)

Không dùng hình khối trừu tượng vô hồn (cấm hoàn toàn bánh răng bay, núi tiền bốc cháy, quả bóng bay, cái phễu, cán cân ảo). Toàn bộ hình ảnh trong video phải là **mô phỏng hiện thực điện ảnh (Cinematic Realistic Simulation)**, đưa khán giả trực tiếp đến hiện trường của các quyết định kinh tế và hậu quả thực tế:

```
                               ┌──────────────────────────────────────────────────────────┐
                               │   4 KHÔNG GIAN BỐI CẢNH VẬT LÝ CHỦ ĐẠO (PHYSICAL REALMS) │
                               └────────────────────────────┬─────────────────────────────┘
                                                            │
         ┌───────────────────────────┬──────────────────────┴──────────────────────┬───────────────────────────┐
         ▼                           ▼                                             ▼                           ▼
┌──────────────────┐        ┌──────────────────┐                          ┌──────────────────┐        ┌──────────────────┐
│ 1. BANGKOK NOIR  │        │ 2. RAYONG RUINS  │                          │ 3. URBAN DEBT    │        │ 4. VIETNAM RISE  │
│ Hội trường BoT,  │        │ Nhà xưởng phụ    │                          │ Phố đêm Pattaya, │        │ Siêu cảng biển,  │
│ phòng họp kính,  │        │ tùng đóng cửa    │                          │ ứng dụng ví số   │        │ phòng lab chip,  │
│ két sắt ngân hàng│        │ theo Điều 75, bãi│                          │ Thang Rath tại   │        │ hạ tầng đường sắt│
│ ứ đọng tiền mặt. │        │ xe điện BYD.     │                          │ chuỗi 7-Eleven.  │        │ cao tốc tự cường.│
└──────────────────┘        └──────────────────┘                          └──────────────────┘        └──────────────────┘
```

---

## 2. Giao Thức Khóa Chặt Chủ Quyền Biển Đảo (Anti-Nine-Dash Line Fail-Safe Protocol — BẮT BUỘC)

Khi thể hiện các hải đồ Vịnh Thái Lan, Biển Đông hoặc bản đồ các tuyến vận tải container quốc tế:
* **Tuyệt đối cấm nét đứt đoạn (Zero Dashed Lines Rule):** Mọi tuyến đường hàng hải phải là dải sáng vector liền nét (`solid glowing cyan lines`). Cấm tuyệt đối nét đứt khúc (`dashed / dotted lines`) trên biển.
* **Mỏ neo chủ quyền bắt buộc trong prompt:** Mọi prompt bản đồ biển bắt buộc phải nhúng khối lệnh khóa chủ quyền:  
  > `showing authentic Vietnamese maritime sovereignty with clean undisputed boundaries and strictly zero dashed lines, no U-shaped lines, clean deep navy waters, crisp 2D vector flat style`
* **Kiểm toán tự động:** Script `check_boilerplate.py` sẽ tự động quét và đánh trượt `FAILED` ngay lập tức nếu phát hiện bất kỳ nguy cơ nào về chủ quyền.

---

## 3. Bảng Màu Thương Hiệu Dòng Chảy (Signature 60-30-10 Color Scheme)

```
[ 60% NỀN TỐI SLATE / CHARCOAL ]       [ 30% HẠ TẦNG & CƠ KHÍ BẠC/ĐEN ]      [ 10% ĐIỂM NHẤN DẪN MẮT ]
Deep Slate Navy (#0F172A)              Solid Black Silhouette (#000000)      Warning Amber (#FF9800) ➔ Nợ nần, bẫy thanh khoản
Dark Charcoal Grey (#1E293B)           Stark White Outlines (#FFFFFF)        Electric Cyan (#00F0FF) ➔ Công nghệ, chip, Việt Nam
Industrial Concrete (#334155)          Silver Grey Steel (#94A3B8)           Crimson Red (#E60000) ➔ Đóng cửa xưởng, giảm phát
```

* **60% Chủ đạo (Nền không gian):** Xám than chì trầm tối (`#0F172A`) và xanh phiến thạch đậm (`#1E293B`). Tạo không khí điều tra chính luận, lạnh lùng và uy quyền.
* **30% Bổ trợ (Chủ thể & Kiến trúc):** Bóng đen tuyền đặc khối (`#000000`), nét viền vector trắng sắc cạnh (`#FFFFFF`) và ánh bạc kim loại của khối máy móc cơ khí (`#94A3B8`).
* **10% Điểm nhấn dẫn mắt (Strategic Visual Hook):**
  * **Warning Amber / Cam cháy (`#FF9800`):** Đại diện cho khối nợ hộ gia đình 90% GDP, nợ công 66,1%, và chiếc bẫy thanh khoản 1% của Thái Lan.
  * **Electric Cyan / Xanh tương lai (`#00F0FF`):** Đại diện cho chuỗi bán dẫn, AI, trung tâm dữ liệu và vận hội bứt phá của Việt Nam.
  * **Crimson Red / Đỏ cảnh báo (`#E60000`):** Đại diện cho sự sụp đổ của chuỗi phụ tùng ô tô truyền thống, thông báo Điều 75 và nguy cơ giảm phát.

---

## 4. Dàn Nhân Vật Thống Nhất (Cast Sheet — Demographic Anchor Lock)

Khóa chặt nhân chủng học người Đông Nam Á, triệt tiêu 100% lỗi Tây hóa hình ảnh:

| Nhân vật | Vai trò trong phim | Mô tả Prompt Tiếng Anh Bắt Buộc (Cast Sheet Lock) |
| :--- | :--- | :--- |
| **Thống đốc BoT** | Chủ trì hội đồng hạ lãi suất 1% (Chương 1) | `A distinguished senior Thai central banker in his late 50s with Southeast Asian features, neatly groomed silver-streaked dark hair, wearing a tailored dark charcoal business suit and crisp white dress shirt with no tie, looking solemn and stressed...` |
| **Thợ cơ khí Rayong** | Thợ phụ tùng mất việc theo Điều 75 (Chương 4) | `A Thai male automotive mechanic in his early 40s with weathered Southeast Asian features, tanned skin, tired and anxious eyes, wearing a grease-stained navy blue factory uniform with roll-up sleeves, standing inside an idle assembly plant...` |
| **Tài xế công nghệ Bangkok** | Người trẻ ngập trong nợ mua sắm trả góp (Chương 2, 6) | `A young Thai gig-worker in his late 20s with Southeast Asian facial features, wearing a dark green delivery jacket, staring intensely at his glowing smartphone screen displaying a digital debt notice in a dim Bangkok alley...` |
| **Nữ kỹ sư công nghệ cao Việt Nam** | Kỹ sư thiết kế chip / xe điện tự cường (Chương 7, 8) | `A professional Vietnamese female technology engineer in her late 20s with Southeast Asian features, straight dark hair tied back, wearing a cleanroom antistatic white suit and clear protective goggles, examining a glowing semiconductor wafer...` |

---

## 5. Đặc Tả Chi Tiết Cơ Khí & Kỹ Thuật (Mechanical & Physical Granularity)

Triệt tiêu hoàn toàn các mô tả mơ hồ ("máy móc", "khung gầm xe"). Mọi phân cảnh kỹ thuật phải chỉ định chính xác cụm cơ khí:
* **Động cơ đốt trong truyền thống (ICE):** `Heavy cast iron 4-cylinder engine block, exposed forged crankshaft, aluminum cylinder head, catalytic converter exhaust manifold, precision metallic gears with grease textures`.
* **Khung gầm xe điện dạng ván trượt (EV Skateboard Platform):** `Low-profile EV skateboard chassis featuring integrated prismatic blade battery pack cells, dual e-axle electric motors, liquid cooling ribbon serpentine tubes, and high-voltage orange insulated wiring`.
* **Trụ sạc DC & Hạ tầng điện:** `Liquid-cooled 250kW DC fast charging terminal with heavy CCS2 charging cable and digital kilowatt display, connected to an industrial power inverter`.
* **Phòng sạch bán dẫn:** `ISO Class 1 semiconductor cleanroom environment with laminar yellow-filtered lighting, automated overhead wafer track system (FOUP), and advanced precision robotic photolithography arm`.

---

## 6. Quy Chuẩn Cinema Typography Layout (Text Overlay)

* **Tần suất hiển thị:** Chỉ xuất hiện ở **~20-25% phân cảnh then chốt** (chứa số liệu gây sốc, câu hỏi bản lề). Các cảnh còn lại ghi `Không`.
* **Quy chuẩn chữ:** 
  * 100% TIẾNG ANH IN HOA.
  * Chữ đứng thẳng trực diện song song với ống kính (`facing the camera directly, perfectly horizontal 3D text overlay`), không nghiêng méo theo phối cảnh tường.
  * Viền đen sắc nét (`crisp black outline`), bóng đổ đen dày (`heavy black drop shadow`). CẤM chữ neon phát sáng rẻ tiền.
* **Quy tắc định vị không che chủ thể:**
  * `TOP CENTER | POLICY RATE: 1.00%`
  * `BOTTOM LEFT | HOUSEHOLD DEBT: 90% GDP`
  * `TOP RIGHT | SPECIAL MENTION LOANS: 7.0%`
  * `CENTER | THE UNEMPLOYED FACTORIES`

---

## 7. Lộ Trình Triển Khai Tuần Tự (Sequential Rollout Plan)

1. **Giai đoạn 1 (Hiện tại):** Trình duyệt bản Kế Hoạch Trực Quan Tổng Thể (`visual_storyboard_blueprint.md`).
2. **Giai đoạn 2 (Tuần tự từng chương):** Biên soạn Kịch bản Visual Trung gian `chapter_01_visual.md` theo chuẩn Storyboard Matrix mẫu (gồm 3 trường: `[THOẠI]`, `[BỐI CẢNH]`, `[TEXT OVERLAY]`).
3. **Giai đoạn 3 (Duyệt & Kế thừa):** Sau khi người dùng duyệt Chương 1 $\rightarrow$ Viết tiếp Chương 2, kế thừa dàn nhân vật và bối cảnh từ Chương 1 theo nguyên tắc Cửa sổ Ngữ cảnh 3 Phân cảnh (Tri-Scene Context Window).
4. **Giai đoạn 4 (Tạo prompt & Kiểm toán):** Sinh các cặp prompt `[IMAGE]` và `[VIDEO]` vào `prompts_master.txt` (hoặc `prompts_chXX.txt`) và chạy kiểm toán tự động qua `scripts/check_boilerplate.py` để đảm bảo 100% PASS 6 Trụ Cột.
