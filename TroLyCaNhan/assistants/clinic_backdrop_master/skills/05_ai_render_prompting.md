# KỸ NĂNG 05: KỸ THUẬT PROMPT AI RENDER MOCKUP 3D ĐỈNH CAO (AI 3D RENDER PROMPTING)

Để thuyết phục chủ phòng khám phê duyệt ý tưởng ngay trong buổi thuyết trình đầu tiên, chuyên gia Dr. Visio sử dụng kỹ thuật viết Prompt AI đỉnh cao dành cho các mô hình tạo ảnh tiên tiến nhất hiện nay (Midjourney v6.1, Flux.1 Pro, DALL-E 3).

---

## 📸 1. CÔNG THỨC PROMPT CHUẨN KIẾN TRÚC Y TẾ 5 SAO

Mỗi câu prompt được cấu thành từ 6 khối thông số độc lập, sắp xếp theo thứ tự ưu tiên nhận diện của AI:

$$\text{Prompt} = [\text{Scene}] + [\text{Focal Subject}] + [\text{Materials \& Textures}] + [\text{Lighting \& Atmosphere}] + [\text{Camera Specs}] + [\text{Rendering Engine}]$$

### Chi tiết các khối thông số:

1. **Scene & Context (Bối cảnh không gian)**:
   - `Luxurious modern aesthetic clinic reception lobby`, `High-end dental clinic check-in interior`, `VIP medical center grand foyer`.
2. **Focal Subject (Chủ thể backdrop)**:
   - `Curved biophilic feature backdrop wall with 3D floating backlit logo`, `Monumental arched sintered stone reception wall with brushed brass logo emblem`.
3. **Materials & Textures (Vật liệu & Bề mặt)**:
   - `Calacatta gold Italian marble with subtle warm grey veining`, `fluted warm oak wood vertical slats`, `ultra-matte off-white microcement`, `brushed champagne titanium stainless steel lettering`, `preserved organic emerald reindeer moss accents`.
4. **Lighting & Atmosphere (Ánh sáng & Cảm xúc)**:
   - `Indirect cove LED lighting at 3500K warm-neutral white`, `soft diffuse halo rim glow behind the 3D logo`, `glare-free translucent Barrisol ceiling panel`, `sterile yet deeply welcoming and soothing healing ambiance`, `photogenic, pristine, 5-star hospitality clinic feel`.
5. **Camera & Photography Specs (Thông số máy ảnh kiến trúc)**:
   - `Eye-level wide architectural shot, captured on Hasselblad H6D-100c, 24mm tilt-shift lens, perfectly straight vertical perspective lines, zero barrel distortion, f/8 aperture, depth of field`.
6. **AI Engine Parameters (Tham số render)**:
   - *Dành cho Midjourney*: `--ar 16:9 --style raw --v 6.1 --stylize 200`
   - *Dành cho Flux.1*: `hyper-realistic interior photography, 8k uhd, photorealistic interior design portfolio shot, octane render realism`.

---

## 🧪 2. BỘ PROMPT MẪU THỰC CHIẾN (PRODUCTION-READY PROMPTS)

### Mẫu 1: Vách Backdrop Quầy Lễ Tân Nha Khoa Quốc Tế (Dental Clinic Reception)
```text
Eye-level professional architectural photograph of a high-end luxury dental clinic reception area. The centerpiece is a monumental curved feature wall made of seamless off-white matte microcement, intersected by a panel of backlit white translucent onyx stone and fluted warm blonde oak slats. Floating elegantly in the center is a 3D minimalist tooth emblem and logo crafted from brushed silver stainless steel, with soft 4000K pure white halo rim lighting glowing softly behind each letter. Clean curved reception desk with a white quartz countertop in the foreground. Soft recessed cove ceiling lights, pristine air, serene zen-like healing atmosphere, perfectly straight perspective lines, shot on Hasselblad H6D-100c, 24mm tilt-shift lens, architectural digest interior style --ar 16:9 --style raw --v 6.1
```

### Mẫu 2: Backdrop Check-in & Photo Wall Viện Thẩm Mỹ Da Liễu Cao Cấp (Aesthetic Dermatology)
```text
Editorial architectural photography of a VIP aesthetic dermatology clinic photo-wall backdrop. An organic multi-layered arched partition with soft blush beige stucco finish, framed by recessed indirect warm LED strip lighting (3200K). Accented with luxurious brushed rose-gold titanium metal trim and an asymmetrical vertical garden panel of preserved natural moss and delicate white orchids. In the upper center, an elegant embossed logo with delicate serif typography "DERMA LUMIÈRE" glows with subtle backlighting. Polished ivory terrazzo flooring reflecting soft light, elegant cylinder display pedestals flanking the side. Glare-free, skin-flattering beauty lighting, high fashion interior aesthetic, 8k resolution, shot with 35mm lens at f/5.6, ultra photorealistic --ar 16:9 --v 6.1
```

### Mẫu 3: Backdrop Sự Kiện Hội Thảo Y Khoa & Chuyển Giao Công Nghệ (Medical CME Event Stage)
```text
Wide stage perspective of an international medical dermatology symposium stage backdrop, 6-meter width. Clean, authoritative, and academic hi-tech design. Deep medical navy blue matte fabric backdrop framed by subtle geometric neon blue light accents and brushed aluminum trim. High-definition LED video wall embedded seamlessly in the center displaying medical molecular illustrations. Above the screen, crisp white 3D cut-out typography reads "INTERNATIONAL CLINICAL DERMATOLOGY SUMMIT 2026", flanked by discreet sponsor logos. Warm stage wash spotlights (CRI 98) illuminating speaker podium, polished dark wood stage floor, ultra-professional academic medical atmosphere, shot on Canon EOS R5 with 24-70mm f/2.8 lens --ar 16:9 --v 6.1
```

---

## 🛠️ 3. KỸ THUẬT INPAINTING VÀ XỬ LÝ CHỮ LOGO

Khi sử dụng AI để tạo ảnh mẫu cho khách:
1. **Bước 1 - Tạo bối cảnh không gian 3D**: Dùng Midjourney hoặc Flux với các prompt trên để sinh ra ảnh không gian và chất liệu hoàn hảo.
2. **Bước 2 - Ghép Logo thực tế (Photoshop / Illustrator)**:
   - Dùng lệnh `Ctrl/Cmd + T` biến dạng phối cảnh (Perspective Transform) để đặt logo vector thật của phòng khám lên đúng vị trí vách backdrop đã render.
   - Thêm hiệu ứng `Drop Shadow` hoặc `Outer Glow` (màu vàng nhạt hoặc trắng ấm, Opacity 30-50%, Size 15-25px) để mô phỏng ánh sáng đèn LED hắt tường chân thật 100%.
