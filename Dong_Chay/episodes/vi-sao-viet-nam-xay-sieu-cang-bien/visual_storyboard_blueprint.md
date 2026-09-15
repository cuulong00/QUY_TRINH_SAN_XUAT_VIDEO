# visual_storyboard_blueprint.md — Kế Hoạch Trực Quan Tổng Thể & Giao Thức Khóa Chủ Quyền Biển Đảo (Pha 12)

> **Tập phim:** Vì sao Việt Nam ồ ạt xây siêu cảng biển?  
> **Mã tập (Slug):** `vi-sao-viet-nam-xay-sieu-cang-bien`  
> **Phong cách trực quan chủ đạo:** Editorial Flat Noir (Đồ họa Noir Báo chí Phẳng 2D Vector)  
> **Tỷ lệ khung hình:** 16:9 Cinematic  

---

## 1. Giao Thức Khóa Chặt Chủ Quyền Biển Đảo & Triệt Tiêu Bản Đồ Đường Lưỡi Bò (Anti-Nine-Dash Line Fail-Safe Protocol — BẮT BUỘC 100%)

Biển Đông là không gian bối cảnh xuất hiện xuyên suốt trong video. Để **triệt tiêu 100% nguy cơ AI sinh ra hình ảnh sai lệch về chủ quyền hoặc nét đứt đoạn phi pháp (đường lưỡi bò)**, toàn bộ kịch bản visual và prompt phải tuân thủ nghiêm ngặt 4 nguyên tắc kỹ thuật sau:

```
                  ┌─────────────────────────────────────────────────────────┐
                  │   GIAO THỨC KHÓA CHỦ QUYỀN BIỂN ĐẢO (MARITIME PROTOCOL) │
                  └────────────────────────────┬────────────────────────────┘
                                               │
         ┌─────────────────────────────────────┴─────────────────────────────────────┐
         ▼                                                                           ▼
┌─────────────────────────────────┐                                 ┌─────────────────────────────────┐
│ 1. CHUYỂN ĐỔI BẢN CHẤT HÌNH ẢNH │                                 │  2. MỎ NEO TỪ KHÓA BẮT BUỘC     │
│ KHÔNG vẽ bản đồ biên giới chính │                                 │ 100% prompt bản đồ biển PHẢI    │
│ trị mập mờ.                     │                                 │ chứa mỏ neo khóa chủ quyền và   │
│ ➔ CHỈ vẽ HẢI ĐỒ ĐỘ SÂU HÀNG HẢI │                                 │ cấm nét đứt đoạn.               │
│ (Nautical Bathymetric Chart)    │                                 │                                 │
└─────────────────────────────────┘                                 └─────────────────────────────────┘
         │                                                                           │
         ▼                                                                           ▼
┌─────────────────────────────────┐                                 ┌─────────────────────────────────┐
│ 3. KHÓA HÌNH DẠNG DÒNG CHẢY     │                                 │  4. RÀ SOÁT TỰ ĐỘNG BẰNG SCRIPT │
│ Mọi luồng tàu chạy PHẢI là      │                                 │ Chạy check_boilerplate.py với   │
│ DẢI SÁNG LIỀN NÉT (SOLID GLOW), │                                 │ bộ lọc cấm để chặn đứng từ gốc. │
│ CẤM TUYỆT ĐỐI NÉT ĐỨT (DASHED). │                                 │                                 │
└─────────────────────────────────┘                                 └─────────────────────────────────┘
```

### Chi tiết 4 chốt chặn kỹ thuật:
1. **Chuyển đổi bản chất bản đồ (From Political to Nautical Bathymetric):**
   * Tuyệt đối không vẽ bản đồ phân chia ranh giới hành chính mập mờ trên biển.
   * Tất cả các cảnh bản đồ biển đều được thể hiện dưới dạng **Hải đồ Hàng hải Quốc tế (Nautical Bathymetric Navigation Chart)** hoặc **Bản đồ Luồng Dòng chảy Thương mại (Global Trade Flow Map)** với nền đại dương xanh thẫm thuần khiết.
2. **Khối lệnh Mỏ neo Bắt buộc trong 100% Prompt Bản đồ Biển (Prompt Sovereignty Anchor):**
   * Mọi câu lệnh prompt có xuất hiện bản đồ biển bắt buộc phải nhúng đoạn mã khóa sau:
     > `nautical bathymetric sea chart showing clean undisputed international shipping corridors across the East Sea, clean open deep navy waters with authentic Vietnamese sovereign maritime baseline, strictly zero dashed lines, no U-shaped lines, solid glowing cyan shipping routes, crisp 2D vector flat style`
3. **Cấm tuyệt đối nét đứt đoạn trên mặt biển (Zero Dashed Lines Rule):**
   * Các tuyến đường tàu chạy, luồng hàng hải 5.300 tỷ USD chỉ được vẽ bằng **dải vector phát sáng liền mạch (Solid Glowing Cyan Line)** hoặc **mũi tên chuyển động đặc (Solid Arrow)**. Tuyệt đối cấm các nét vẽ ngắt quãng, đứt khúc (dashed/dotted lines) trên toàn bộ bề mặt đại dương.
4. **Kiểm toán tự động:**
   * Script `check_boilerplate.py` sẽ tự động quét và đánh trượt `FAILED` ngay lập tức nếu phát hiện bất kỳ từ khóa nào có nguy cơ gây hiểu nhầm về chủ quyền.

---

## 2. Bảng Màu Thương Hiệu Dòng Chảy (Signature 60-30-10 Color Scheme)

Để phản ánh không khí chính luận, lạnh lùng, sang trọng và đậm chất điều tra kinh tế biển:

```
[ 60% NỀN TỐI SLATE / CHARCOAL ]       [ 30% HẠ TẦNG & CƠ KHÍ BẠC/ĐEN ]      [ 10% ĐIỂM NHẤN CHIẾN LƯỢC ]
Deep Slate Navy (#0F172A)              Solid Black Silhouette (#000000)      Electric Sea Cyan (#00F0FF) ➔ Biển sâu / Cảng VN
Dark Charcoal Grey (#1E293B)           Stark White Outlines (#FFFFFF)        Warning Amber (#FF9800) ➔ Điểm nghẽn / Chi phí
Ocean Trench Blue (#0A0F1D)            Silver Grey Steel (#94A3B8)           Crimson Red (#E60000) ➔ Rủi ro / Vòng vây
```

* **60% Chủ đạo (Nền không gian):** Màu xanh biển thẳm Noir (`#0A0F1D`) và xám than chì trầm tối (`#0F172A`). Tạo cảm giác đại dương sâu thẳm, tĩnh lặng và uy quyền.
* **30% Bổ trợ (Chủ thể & Khung cảnh):** Màu đen tuyền bóng đổ (`#000000`), nét viền trắng sắc cạnh (`#FFFFFF`) và ánh bạc kim loại của cẩu trục, vỏ tàu container (`#94A3B8`).
* **10% Điểm nhấn dẫn mắt (Strategic Accent):**
  * **Electric Sea Cyan (`#00F0FF`):** Đại diện cho dòng tiền, luồng nước sâu -18m, tuyến tàu mẹ Direct Call và vị thế siêu cảng Việt Nam.
  * **Warning Amber / Coral (`#FF9800` / `#FF5722`):** Đại diện cho chi phí "thuế ẩn" 18% GDP, điểm nghẽn QL51, và thách thức sinh thái Cần Giờ.
  * **Crimson Red (`#E60000`):** Đại diện cho áp lực địa chính trị bao quanh (Funan Techo, Ream, bẫy nợ Hambantota).

---

## 3. Dàn Nhân Vật Thống Nhất (Cast Sheet — Demographic Anchor Lock)

Mọi cảnh xuất hiện con người đều bị khóa chặt nhân chủng học người Việt Nam / Đông Nam Á, triệt tiêu hoàn toàn lỗi Tây hóa hình ảnh:

| Nhân vật | Vai trò trong phim | Mô tả Prompt Bắt Buộc (Prompt Cast Lock) |
| :--- | :--- | :--- |
| **Thợ cẩu STS Cái Mép** | Điều khiển cẩu bến 40m tại Cái Mép (Chương 4) | `A Vietnamese male crane operator in his late 30s with Southeast Asian features, tanned weathered skin, focused sharp eyes, wearing a navy-blue industrial reflective vest and white safety hardhat, sitting inside a high-tech glass cabin...` |
| **Tài xế container QL51** | Lái xe đêm thức trắng trên QL51 (Chương 4) | `A Vietnamese male container truck driver in his early 40s with rugged Southeast Asian facial features, tired yet determined expression, wearing a simple dark grey work t-shirt, sitting behind the steering wheel of a heavy-duty prime mover...` |
| **Lão ngư giữ rừng Cần Giờ** | Đại diện 3 thế hệ bảo vệ rừng ngập mặn (Chương 6) | `An elderly Vietnamese fisherman in his late 50s with deep sun-tanned skin, weathered wrinkles, calm resilient gaze, wearing traditional dark loose linen work clothes, standing amidst the massive mangrove roots of Can Gio...` |

---

## 4. Độ Chi Tiết Cơ Khí & Kỹ Thuật (Mechanical & Physical Granularity)

Triệt tiêu hoàn toàn các hình khối trừu tượng vô hồn (bánh răng bay, núi tiền, cán cân ảo). Mọi phân cảnh mô phỏng cơ khí chính xác 100%:
* **Siêu tàu container 24.000 TEU:** `Ultra Large Container Vessel (ULCV) with 24 rows of stacked colorful steel containers, gigantic bulbous bow submerged in deep -18m navy waters, massive single propeller wake, realistic hull markings`.
* **Cẩu giàn bờ Ship-to-Shore (STS):** `Super Post-Panamax STS container gantry crane towering 65 meters high, white and dark navy industrial steel lattice structure, heavy-duty spreader bar locking onto a 40ft shipping container`.
* **Mỏ neo vật lý (Chiếc container 40ft):** `Standard 40ft ISO shipping container with corrugated corten steel panels, crisp international tracking serial numbers, matte industrial paint`.

---

## 5. Quy Chuẩn Cinema Typography Layout (Text Overlay)

* **Tần suất:** Chỉ xuất hiện ở ~20-25% phân cảnh then chốt (chứa số liệu gây sốc, câu hỏi chiến lược). Các cảnh còn lại ghi `Không`.
* **Quy chuẩn chữ:** 100% TIẾNG ANH IN HOA, chữ đứng thẳng trực diện song song camera (`facing the camera directly, perfectly horizontal 3D overlay text`), viền đen sắc nét, bóng đổ dày.
* **Quy tắc định vị (Positioning):** Luôn chỉ định rõ vị trí không che mặt nhân vật hay chi tiết quan trọng (ví dụ: `TOP CENTER | 18% GDP LOGISTICS TOLL`, `BOTTOM RIGHT | 24,000 TEU MEGASHIP ERA`).

---

## 6. Lộ Trình Triển Khai Tuần Tự (Sequential Rollout Plan)

Theo quy định bắt biến của Pipeline:
1. **Bước 1:** Trình duyệt bản kế hoạch tổng thể `visual_storyboard_blueprint.md` (Tài liệu này).
2. **Bước 2:** Biên soạn Kịch bản Visual trung gian **Chương 1 (`chapter_01_visual.md`)** theo chuẩn Storyboard Matrix mẫu.
3. **Bước 3:** Trình duyệt Chương 1 $\rightarrow$ Viết tiếp `chapter_02_visual.md` cho đến hết Chương 8.
4. **Bước 4:** Biên soạn prompt cặp đôi `[IMAGE]` và `[VIDEO]` vào `prompts_master.txt` (hoặc `prompts_chXX.txt`) và kiểm toán bằng `check_boilerplate.py`.
