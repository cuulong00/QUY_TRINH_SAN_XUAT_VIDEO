# Veo 3.1 Video Specification & Prompts — bong-toi-triet-ly

Tài liệu đặc tả hệ thống prompt tạo video tối ưu cho Google Veo 3.1 (tối đa 8.0s/video) tương ứng với thời lượng thực tế của các file ghi âm trong thư mục `audio_v2`.

---

## 1. Hướng Dẫn Phong Cách Nghệ Thuật Đồng Bộ (Visual Style Guide)
Tất cả các prompt tạo video cho Veo 3.1 phải tuân thủ nghiêm ngặt các quy tắc sau:

*   **Style nghệ thuật chính:** `Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients, editorial style.`
*   **Bảng màu (Nordic Noir Palette):**
    *   Màu nền/Chủ đạo: Deep Navy (Xanh dương đậm), Charcoal Gray (Xám than), Stark White (Trắng tinh khiết).
    *   Màu nhấn cảm xúc: Warm Amber/Gold (Vàng hổ phách/Vàng kim) cho các trạng thái phục hồi, liên kết phó giao cảm hoặc oxytocin; Icy Blue (Xanh băng giá) cho các trạng thái cô độc, giải thể nhân cách, trơ lỳ hoặc đóng băng sinh học; Soft Crimson Red (Đỏ thẫm dịu) cho các trạng thái kích hoạt amygdala, stress, cortisol hoặc đau cơ thể hóa.
*   **Chất lượng chuyển động:** Chuyển động cực kỳ chậm, mượt mà, tối giản (subtle animation). Tránh các biến dạng hình học đột ngột để duy trì tính cinematic và ổn định vật lý.
*   **Camera:** Sử dụng các chuyển động camera mượt mà như `cinematic slow panning`, `slow dolly-in`, `slow tilt up/down`, hoặc `locked tripod shot`.

---

## 2. Bảng Đồng Bộ Nhân Vật (Character Consistency Sheet)
Để duy trì sự nhất quán của nhân vật qua các phân cảnh, các mô tả ngoại hình dưới đây phải được lặp lại chính xác trong prompt khi nhân vật xuất hiện:

1.  **Thiền giả / Người chồng (The Meditator):** `The Meditator, a slender Asian man with short clean-cut black hair, wearing a dark gray loose-fitting organic linen shirt and dark pants, showing a calm, expressionless face.`
2.  **Người vợ (The Wife):** `The Wife, a slender Asian woman with long black hair tied in a neat low ponytail, wearing a dark blue long-sleeve top, looking exhausted and sorrowful.`
3.  **Đứa con nhỏ (The Child):** `The Child, a toddler with short black hair, wearing simple plain clothing.`
4.  **Nhà khoa học (The Researcher):** `The Researcher, a professional Asian man with neat hair and thin-frame glasses, wearing a dark gray laboratory jacket.`

---

## 3. Bảng Phân Phối Thời Lượng Phân Cảnh (Scene Timing Distribution)

| Chương | File Audio | Thời lượng | Số lượng cảnh | Chi tiết phân bổ thời lượng Veo 3.1 |
| :--- | :--- | :--- | :--- | :--- |
| **Chapter 1** | `chapter_01_v2.wav` | 228.83s | 29 cảnh | 28 cảnh x 8.0s + 1 cảnh x 4.83s |
| **Chapter 2** | `chapter_02_v2.wav` | 175.53s | 22 cảnh | 21 cảnh x 8.0s + 1 cảnh x 7.53s |
| **Chapter 3** | `chapter_03_v2.wav` | 169.30s | 22 cảnh | 20 cảnh x 8.0s + 2 cảnh x 4.65s |
| **Chapter 4** | `chapter_04_v2.wav` | 200.02s | 26 cảnh | 24 cảnh x 8.0s + 2 cảnh x 4.01s |
| **Chapter 5** | `chapter_05_v2.wav` | 199.05s | 25 cảnh | 24 cảnh x 8.0s + 1 cảnh x 7.05s |
| **Chapter 6** | `chapter_06_v2.wav` | 212.86s | 27 cảnh | 26 cảnh x 8.0s + 1 cảnh x 4.86s |

---

## 4. Hệ Thống Prompt Tạo Video Chi Tiết Cho Từng Chương

### CHAPTER 1: CÁI BẪY LẢNG TRÁNH TÂM LINH & GIẢI THỂ NHÂN CÁCH
*Tổng thời lượng: 228.83s. Gồm 29 phân cảnh:*

#### `chapter_01_scene_01.mp4` (Duration: 8.0s)
> Cinematic slow panning medium shot. The Wife, a slender Asian woman with long black hair tied in a neat low ponytail, wearing a dark blue long-sleeve top, sits on a couch in a dimly lit, cluttered living room, trembling and wiping tears. In the out-of-focus background, a toddler with short black hair plays with scattered toys. Deep navy and charcoal gray tones, soft shadows. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_02.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in close-up shot. The Wife, a slender Asian woman with long black hair tied in a neat low ponytail, looking exhausted and sorrowful, with soft shadow cast on her face. Her chest rises and falls slowly with heavy breathing. Cold gray and deep navy tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_03.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A closed dark wooden bedroom door. A cold ray of icy blue light leaks from the narrow gap under the door onto the dark wooden floorboards. Moody, silent, and desolate atmosphere. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_04.mp4` (Duration: 8.0s)
> Cinematic slow panning medium shot. Inside a dark bedroom, The Meditator, a slender Asian man with short clean-cut black hair, wearing a dark gray loose-fitting organic linen shirt and dark pants, sits in a cross-legged lotus meditation pose. He is in half-shadow, with a cold spotlight hitting his closed eyes. Extremely still and rigid posture. Charcoal gray and icy blue tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_05.mp4` (Duration: 8.0s)
> Cinematic locked tripod close-up shot. The Meditator's calm, expressionless face during meditation. His eyes remain shut, and his features are completely blank and frozen, despite faint blue soundwave lines suggesting noise coming from the outside room. Flat gray and cold blue tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_06.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in macro shot. Close-up on The Meditator's jaw, showing subtle muscle tension under a harsh side-lighting setup. Volumetric gray dust particles float slowly in the dark air. Charcoal and deep navy tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_07.mp4` (Duration: 8.0s)
> Cinematic slow pull-back wide shot. The Meditator sitting in a lotus position, looking like a rigid, gray stone statue in the middle of a vast, empty concrete room. Nordic Noir moody color grading, deep navy and charcoal gray tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_08.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A clinical laboratory desk with a paper medical report illuminated by a harsh white surgical lamp. The rest of the desk and room are covered in deep, dark navy shadows. Cold, sterile atmosphere. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_09.mp4` (Duration: 8.0s)
> Cinematic slow tilt-down macro shot. Vintage typewriter keys striking a sheet of off-white paper, typing the letters 'SPIRITUAL BYPASSING' in dark navy ink. Shallow depth of field, heavy dark shadows in the background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_10.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. An empty dark hallway with a closed door at the end. Cold blue moonlight filters through a high window, casting long geometric window-frame shadows on the dark wooden floor. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_11.mp4` (Duration: 8.0s)
> Cinematic slow panning medium shot. A clean clinical laboratory. The Researcher, a professional Asian man with neat hair and thin-frame glasses, wearing a dark gray laboratory jacket, adjusts a modern digital microscope. Clinical blue and stark white tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_12.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. The Researcher's hand adjusting the microscope in the foreground, while a digital monitor in the background displays the text 'Brown University Study 2021' in a clean white sans-serif font. Clinical navy and white tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_13.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A dark flat screen showing a clean statistic bar graph rising sharply. Bright gold numbers '58% Side Effects' and '37% Impairment' glow softly on the dark screen. High contrast, dark navy background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_14.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in shot. The glowing gold data points on the dark clinical monitor reflect off a highly polished metallic counter in a dark laboratory. Deep navy and gold tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_15.mp4` (Duration: 8.0s)
> Cinematic locked tripod close-up shot. A person looking down at their own palms. The skin is rendered in flat, desaturated gray tones, looking completely lifeless and disconnected from the body. Cold overhead white lighting. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_16.mp4` (Duration: 8.0s)
> Cinematic slow panning low-angle shot. A busy city street at dusk. Cars passing by are stylized as flat, paper-thin geometric cutouts sliding horizontally across a hazy, desaturated gray-blue background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_17.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A single dark silhouette of a person standing frozen on the curb of the flattened city street at dusk, looking disconnected from the sliding traffic. Moody blue and gray tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_18.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in shot. An empty clinical medical room with a single white chair placed under a flickering fluorescent tube. Cold, sterile, and lonely atmosphere. Muted grays and icy blue tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_19.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. On a dark wall-mounted monitor, a simplified 2D brain scan shows decreased light activity in the insular cortex. Icy blue and charcoal color scheme. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_20.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. An old, rusty metal pipe leaking water slowly under intense internal pressure. A small red warning bulb nearby blinks rhythmically, casting a pulse of red light. Dark, damp concrete floor. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_21.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in shot. A sleek, dark studio with a vintage camera lens slowly focusing on a centered white text that reads 'Đạo & Khoa Học'. Low-key lighting, amber accents. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_22.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. Split-screen: On the left, a traditional zen circular brush stroke (Enso) drawn in black ink. On the right, a glowing gold 2D rendering of the human central nervous system. Dark charcoal background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_23.mp4` (Duration: 8.0s)
> Cinematic slow panning close-up shot. Ancient scriptures with Sanskrit symbols lying next to a modern neuroscience book. A single spotlight from above illuminates them on a dark oak table. Deep shadows. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_24.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A thin candle flame burning steadily in a pitch-black room. Slowly, a gentle breeze blows the flame out, leaving a thin white line of smoke rising. Minimalist chiaroscuro. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_25.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A sharp, thin red laser beam slicing through a dark gray stone block, dividing it clean in two halves. Volumetric gray shadows, industrial aesthetic. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_26.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A simplified 2D model of the human brain. The prefrontal cortex is highlighted in bright white, while the amygdala glows in a warning soft crimson red color. Dark charcoal background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_27.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in shot. A mechanical vice grip clamping down tightly on a soft blue rubber sphere, compressing and flattening it. Strong shadow lines on the concrete floor. Muted industrial tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_28.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. An electrical wire snapping with a small bright spark, cutting off light to a green indicator bulb. The room dims instantly. Cold industrial aesthetic, charcoal and gray tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_01_scene_29.mp4` (Duration: 4.83s)
> Cinematic slow panning shot. A window pane covered in a thick layer of ice crystals. Behind the glass, a very blurry silhouette of a person standing still. Icy blue and dark navy color grading. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 4.83s]

---

### CHAPTER 2: PHÂN LY CẢM XÚC & KIỂU GẮN BÓ LẢNG TRÁNH (MAMMALIAN ATTACHMENT)
*Tổng thời lượng: 175.53s. Gồm 22 phân cảnh:*

#### `chapter_02_scene_01.mp4` (Duration: 8.0s)
> Cinematic slow panning close-up shot. Two warm-toned hands gently holding each other. A soft gold glow radiates from the contact point, symbolizing secure attachment. Warm gray background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_02_scene_02.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in shot. A mother's warm silhouette gently cradling a baby. A slow wave of warm golden light (oxytocin) spreads from her chest outwards. Soft lines, peaceful and cozy mood. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_02_scene_03.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A diagram showing a simplified human nervous system transitioning from a warning soft crimson red color to a calm, deep navy blue state. Dark charcoal background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_02_scene_04.mp4` (Duration: 8.0s)
> Cinematic slow panning wide shot. A zen practitioner meditating in a forest, but his body is surrounded by a thick, transparent shield of ice, separating him from the surrounding green trees. Moody, icy blue and deep navy tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_02_scene_05.mp4` (Duration: 8.0s)
> Cinematic slow panning close-up shot. A person sitting at a dark wooden table, staring blankly at a family photo frame. The frame is desaturated gray, while the room around is deep navy. Moody and melancholy lighting. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_02_scene_06.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in medium shot. Inside a dark room, The Meditator, a slender Asian man with short clean-cut black hair, wearing a dark gray linen shirt, sitting in meditation. Outside his window, the silhouette of a woman walking away in the rain is faint. Deep navy tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_02_scene_07.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A clinical screen displaying the letters 'Spiritual Bypass Scale (SBS)' next to a bar graph showing high levels of emotional suppression. Charcoal and clinical blue tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_02_scene_08.mp4` (Duration: 8.0s)
> Cinematic slow panning close-up shot. Close-up on The Meditator's face meditating. A cold blue light shines on his forehead (PFC), while a lock icon is superimposed over his chest. Charcoal gray tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_02_scene_09.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A hand reaches out to touch another person's shoulder, but stops a few inches away, freezing in mid-air. Moody gray shadow casting, cold atmosphere. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_02_scene_10.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A brain scan diagram showing a complete lack of synapse signals in the Insular Cortex. Cold, desaturated icy blue and charcoal color scheme. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_02_scene_11.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. An empty swingset swaying gently in a foggy, gray field at twilight. Melancholy and desolate atmosphere, Nordic Noir aesthetic. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_02_scene_12.mp4` (Duration: 8.0s)
> Cinematic slow tilt-down shot. A brick wall slowly building up in front of a warm fireplace, eventually blocking out all the warm light and leaving the room in cold charcoal shadow. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_02_scene_13.mp4` (Duration: 8.0s)
> Cinematic slow panning medium shot. The Researcher, a professional Asian man with neat hair and thin-frame glasses, wearing a dark gray laboratory jacket, pointing to a brain chart highlighting the vagus nerve system. Clinical blue tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_02_scene_14.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A diagram displaying two contrasting paths on a screen: one glowing in warm amber labeled 'Secure Attachment', and the other in icy blue labeled 'Avoidant Attachment'. Dark charcoal background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_02_scene_15.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A glass partition dividing a room. On one side, a warm family dinner is in progress; on the other, a lone man sits meditating in cold gray shadow. Moody and high contrast lighting. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_02_scene_16.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in close-up shot. A flower made of glass, standing in a sterile gray room. A drop of water hits the glass petal, but instead of absorbing, it slides off and freezes. Icy blue grading. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_02_scene_17.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A scientific graph showing oxytocin levels dropping down to zero, represented by a flat-lining gold line on a dark clinical screen. High contrast, clinical navy background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_02_scene_18.mp4` (Duration: 8.0s)
> Cinematic locked tripod close-up shot. Close-up of The Meditator's closed eyes. A subtle tear forms but immediately freezes into a small blue crystal on his cheek. Cold gray lighting. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_02_scene_19.mp4` (Duration: 8.0s)
> Cinematic slow panning wide shot. A lone wolf standing on a cliff at night under a cold crescent moon, looking down at a distant, warm village in the valley. High contrast chiaroscuro. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_02_scene_20.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in shot. A bird cage with its doors wide open, but the bird inside remains sitting frozen on the perch, refusing to fly out. Charcoal gray and icy blue tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_02_scene_21.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A heart silhouette slowly turning into a solid block of dark ice, with tiny cracks radiating outwards. Deep navy background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_02_scene_22.mp4` (Duration: 7.53s)
> Cinematic slow tilt-up shot. A dark room with a single window. The dawn light slowly begins to break, casting a very faint warm orange line across the cold floorboards. Muted gray and amber tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 7.53s]

---

### CHAPTER 3: NGHỊCH LÝ VÔ NGÃ & HỐ SÂU TRỐNG RỖNG (ANATTA)
*Tổng thời lượng: 169.30s. Gồm 22 phân cảnh:*

#### `chapter_03_scene_01.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A stylized 2D human body silhouette containing a glowing amber core. The core acts as a shield, deflecting chaotic gray particles (entropy) flying in from the outside dark space. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_03_scene_02.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in close-up shot. Close-up on the glowing amber core inside the silhouette, showing it composed of complex geometric patterns (predictive coding) pulsating slowly. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_03_scene_03.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A scale weighing a heavy solid stone representing 'Ego' against a feather. The stone suddenly crumbles into fine gray sand. Dark charcoal background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_03_scene_04.mp4` (Duration: 8.0s)
> Cinematic slow panning medium shot. The Meditator, a slender Asian man with short clean-cut black hair, wearing a dark gray loose linen shirt, sitting in meditation. Slowly, his hands and arms begin to dissolve into tiny, desaturated gray dust particles. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_03_scene_05.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A brain scan model highlighting the Default Mode Network (DMN) in the center, which slowly fades from bright gold to complete darkness. Charcoal background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_03_scene_06.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A 2D brain model showing the Salience Network (Anterior Insula) flashing in a warning red, indicating de-synchronization. Dark charcoal background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_03_scene_07.mp4` (Duration: 8.0s)
> Cinematic slow panning wide shot. A person's silhouette standing at the edge of a bottomless dark void. The void is pitch black, swallowing all light. Minimalist composition, deep navy tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_03_scene_08.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in shot. The silhouette slowly steps into the bottomless void, immediately dissolving into the empty dark space. Deep navy and charcoal tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_03_scene_09.mp4` (Duration: 8.0s)
> Cinematic locked tripod close-up shot. Close-up on The Meditator's face. The face is split down the middle: the left side is calm, the right side is a dark void with floating dust. Charcoal gray tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_03_scene_10.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A wall clock with its hands running backward rapidly, then the hands detach and float away in the dark space, representing the loss of time perception. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_03_scene_11.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in shot. A mirror reflecting a person meditating, but the reflection slowly fades away to nothing, leaving only the empty background room in the reflection. Gray and navy tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_03_scene_12.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. The text 'PIT OF THE VOID' written in a clean, clinical white sans-serif font, slowly sinking into a deep pool of black ink. Moody lighting. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_03_scene_13.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A clinical file showing the words 'Depersonalization Disorder' next to a drawing of a human outline detached from its shadow. Stark white and gray tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_03_scene_14.mp4` (Duration: 8.0s)
> Cinematic locked tripod close-up shot. A person looking down at their feet, but their feet appear transparent, showing the empty wooden floorboards below them. Gray and blue tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_03_scene_15.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A detailed brain fMRI graphic showing disconnected neural pathways, represented by broken blue lines on a dark background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_03_scene_16.mp4` (Duration: 8.0s)
> Cinematic slow panning wide shot. A wooden house losing its outer walls one by one, leaving the internal furniture exposed to a cold, dark storm. Deep navy and gray tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_03_scene_17.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. An hourglass where the sand flows upward instead of downward, defying gravity in a pitch-black room. Minimalist chiaroscuro. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_03_scene_18.mp4` (Duration: 8.0s)
> Cinematic locked tripod close-up shot. Close-up on The Meditator's closed eyes. A cold, flat blue grid pattern is cast over his eyelids, symbolizing simulation. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_03_scene_19.mp4` (Duration: 8.0s)
> Cinematic slow panning wide shot. A single gray stone pillar standing in a vast, foggy gray landscape under an overcast sky. Deep sense of isolation, Nordic Noir. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_03_scene_20.mp4` (Duration: 8.0s)
> Cinematic slow dolly-out shot. The concrete walls of a room slowly expanding outward in all directions, leaving the meditating person in an infinite, cold gray space. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_03_scene_21.mp4` (Duration: 4.65s)
> Cinematic slow panning shot. A glowing golden thread representing consciousness, slowly fraying and breaking into separate segments in the dark. Charcoal background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 4.65s]

#### `chapter_03_scene_22.mp4` (Duration: 4.65s)
> Cinematic slow fade shot. The screen slowly and smoothly fades into a solid charcoal gray color, leaving a cold, quiet feeling. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 4.65s]

---

### CHAPTER 4: CAM CHỊU NGHIỆP QUẢ & ĐỊNH LUẬT ENTROPY (KARMA)
*Tổng thời lượng: 200.02s. Gồm 26 phân cảnh:*

#### `chapter_04_scene_01.mp4` (Duration: 8.0s)
> Cinematic slow panning medium shot. An older Asian man bowing his head under a heavy cracked stone block on his back. The block has ancient symbols etched on it. Dark gray background, high contrast shadows. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_02.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in close-up shot. Close-up on the heavy rusted iron chains binding the man's hands to the heavy stone block. High contrast chiaroscuro, charcoal tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_03.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A scale balancing glowing gold coins against a pile of dark ash. The pan with the ash sinks down heavily. Dark charcoal background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_04.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A person sitting cross-legged on the concrete floor, head bowed in submission. A giant shadow of a hand looms over them, pointing down accusingly. Moody shadows. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_05.mp4` (Duration: 8.0s)
> Cinematic locked tripod close-up shot. A clinical patient file with the handwritten word 'Karma' on a dark desk. A cold surgical spotlight hits the paper. Deep shadows around. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_06.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A vintage copy of Erwin Schrödinger's book 'What is Life?' lying on a dark table next to a glowing model of a double helix DNA. Charcoal and gold tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_07.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A diagram showing a closed system filling up with chaotic gray dots (entropy) until it is completely filled and static. Charcoal background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_08.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A stylized cell drawing absorbing glowing yellow energy particles from its surroundings, maintaining its organized structure. Deep navy and gold tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_09.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in shot. The Researcher's hand drawing the equation 'dS = d_iS + d_eS' on a clean blackboard with white chalk. High contrast. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_10.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A diagram showing a red arrow representing d_iS (internal entropy) rising, while a blue arrow representing d_eS (exchanged energy) is blocked. Dark background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_11.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A mechanical gear system slowing down, rusting, and eventually grinding to a complete halt. Cold metallic grays and charcoal tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_12.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A portrait of Ilya Prigogine rendered in flat geometric vector style next to a diagram of a 'Dissipative Structure' showing energy flow. Charcoal background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_13.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A vortex of blue water constantly spinning and maintaining its shape, while receiving a stream of energy from the top. Deep navy and cyan tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_14.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in shot. The vortex slowly stops spinning as the energy stream is cut off, collapsing into flat, still water. Gray and navy tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_15.mp4` (Duration: 8.0s)
> Cinematic slow panning medium shot. A dog sitting inside an open cage, but it refuses to step out, looking down with a sad expression (Learned Helplessness). Gray background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_16.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in close-up shot. Close-up on the dog's collar showing a tag that reads 'Helplessness'. Moody gray background, cold lighting. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_17.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A human brain diagram showing a flat line of activity in the prefrontal cortex, indicating loss of control. Charcoal background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_18.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A heart rate monitor showing a flat-lining blue line (reduced Heart Rate Variability), reflecting biological freezing. Cold blue and navy tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_19.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. An icy landscape where a small green plant is slowly covered by frost and dies. Desaturated gray and icy blue color palette. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_20.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A grandfather clock with its pendulum swinging slower and slower until it stops completely. Charcoal gray tones, soft shadows. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_21.mp4` (Duration: 8.0s)
> Cinematic slow panning medium shot. A person sitting at a desk with their head resting on their hands, looking completely depleted of energy. Moody and dark lighting. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_22.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in shot. A glowing light bulb slowly dimming and turning dark as the electrical filament inside snaps. High contrast. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_23.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A dry leaf being blown away by the wind across a barren concrete ground under a dark gray sky. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_24.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A heavy metal safe door closing slowly and locking shut with a loud click. High contrast lighting, charcoal tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_04_scene_25.mp4` (Duration: 4.01s)
> Cinematic slow tilt-down shot. A heavy iron lock hanging on the metal safe door, casting a long shadow on the steel surface. Cold gray tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 4.01s]

#### `chapter_04_scene_26.mp4` (Duration: 4.01s)
> Cinematic slow fade shot. The screen slowly and smoothly fades into a deep, silent black space. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 4.01s]

---

### CHAPTER 5: ĐAU CƠ THỂ HÓA & MẶC CẢM TỰ TRÁCH ĐẠO ĐỨC (SOMATIZATION)
*Tổng thời lượng: 199.05s. Gồm 25 phân cảnh:*

#### `chapter_05_scene_01.mp4` (Duration: 8.0s)
> Cinematic slow panning close-up shot. Close-up on The Meditator's chest. A warning soft crimson red glow starts to emanate from his chest, representing rising internal tension and moral guilt. Charcoal background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_02.mp4` (Duration: 8.0s)
> Cinematic slow panning medium shot. The Meditator sits meditating, but a red grid of lasers wraps tightly around his shoulders, squeezing him. High contrast, charcoal and red tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_03.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A clinical definition on a screen reading 'Moral Scrupulosity OCD' next to a drawing of a person trapped inside a cage of their own thoughts. Stark white and gray. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_04.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A person standing in front of a mirror. Instead of a normal reflection, the mirror shows a large accusing eye staring back. Moody lighting. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_05.mp4` (Duration: 8.0s)
> Cinematic locked tripod close-up shot. Close-up of a hand tightly gripping a stomach in pain. A warning soft crimson red light flashes over the stomach area. Dark navy background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_06.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A diagram showing the HPA-axis (hypothalamus-pituitary-adrenal) flooding the bloodstream with red cortisol droplets. Charcoal background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_07.mp4` (Duration: 8.0s)
> Cinematic slow panning close-up shot. A glass cup slowly cracking under the heat of boiling water. The cracks spread outward slowly. Moody lighting, high contrast. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_08.mp4` (Duration: 8.0s)
> Cinematic slow panning medium shot. A person sitting at a desk, looking completely exhausted. A battery icon above their head shows only a single blinking red bar. Charcoal tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_09.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A brain model showing a complete lack of activity in the prefrontal cortex, representing executive depletion. Charcoal and gray tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_10.mp4` (Duration: 8.0s)
> Cinematic slow panning close-up shot. Close-up of a neck and shoulders. The muscles are rendered in tense, rigid gray geometric blocks, representing somatization. High contrast shadow lines. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_11.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A person tossing and turning in bed in a dark room, unable to sleep. A blue digital clock on the nightstand shows '3:00 AM'. Moody navy tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_12.mp4` (Duration: 8.0s)
> Cinematic slow panning close-up shot. A doctor's hand writing clinical notes on a patient chart titled 'Psychosomatic Pain / Somatization'. Clinical blue and white tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_13.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A diagram illustrating David Malan's Triangle of Conflict, showing Anxiety and Defense blocking the Core Emotion. Charcoal background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_14.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. The Triangle of Conflict slowly rotates, showing the block of 'Defense' crumbling under a warm golden spotlight. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_15.mp4` (Duration: 8.0s)
> Cinematic slow panning close-up shot. A person writing their feelings in a journal. As they write, the tense red lines around their shoulders slowly turn into soft gold waves. Cozy lighting. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_16.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A clinical monitor showing a heart rate recovering its healthy variability, represented by a flexible wave line transition. Blue and white tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_17.mp4` (Duration: 8.0s)
> Cinematic slow panning medium shot. A person standing up from their meditation mat, stretching their arms and looking out of a window at a sunrise. Warm golden lighting. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_18.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in close-up shot. Close-up of a person's chest. The warning red glow is replaced by a warm, soothing golden light. Warm gray background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_19.mp4` (Duration: 8.0s)
> Cinematic slow tilt-down shot. A dry clay vessel being filled with fresh, clear water, the cracks on its surface slowly closing. Warm amber tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_20.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A metal cage slowly dissolving into thin air, freeing the person meditating inside. Warm golden light. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_21.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A diagram showing cortisol levels dropping steadily on a dark screen, replaced by glowing gold oxytocin indicators. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_22.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in close-up shot. Close-up of a person's face showing a subtle, genuine smile of relief. Warm and cozy lighting. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_23.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A serene forest stream flowing over smooth stones under a warm sun. Soft green moss on the stones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_24.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. The camera slowly pans up from the stream to the green canopy of trees, letting in golden rays of light. Warm forest atmosphere. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_05_scene_25.mp4` (Duration: 7.05s)
> Cinematic slow dolly-in close-up shot. A single green leaf covered in dew drops glistening in the morning sun. Warm golden bokeh. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 7.05s]

---

### CHAPTER 6: HẠ VŨ KHÍ CỦA Ý CHÍ & TỰ TRẮC ẨN (SELF-COMPASSION)
*Tổng thời lượng: 212.86s. Gồm 27 phân cảnh:*

#### `chapter_06_scene_01.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A portrait of Albert Einstein next to a false quote graphic. A red 'X' mark is stamped over the quote, correcting the myth. Stark gray and red. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_02.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A portrait of Steve Jobs meditating, next to a chaotic, flickering graph representing his real-life emotional instability. Gray and blue tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_03.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A person putting down a heavy steel sword on the ground, representing surrendering the battle of will. Dark gray concrete floor, long shadows. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_04.mp4` (Duration: 8.0s)
> Cinematic slow panning close-up shot. Close-up on a person's hands placing a warm, glowing golden cloth over their own shoulders. Cozy lighting. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_05.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A diagram illustrating Paul Gilbert's three emotion systems: Threat (Red), Drive (Blue), and Soothing (Green). Charcoal background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_06.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in shot. The green Soothing circle expands slowly, wrapping around the vibrating red Threat circle and calming its vibrations. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_07.mp4` (Duration: 8.0s)
> Cinematic slow panning medium shot. A person meditating, with a gentle green aura radiating from their body, representing the activation of the parasympathetic system. Soft, soothing lighting. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_08.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. The Researcher's hand pointing to an EEG monitor showing increased activity in the prefrontal cortex during self-compassion practice. Clinical blue and white tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_09.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in close-up shot. Close-up of a person gently touching their own chest with their hand, feeling their heartbeat. Soft, warm golden light, cozy mood. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_10.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A white bird flying freely out of an open cage into a bright, clear sky. Minimalist, clean lines, peaceful atmosphere. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_11.mp4` (Duration: 8.0s)
> Cinematic slow panning medium shot. Two friends sitting together at a cozy coffee table, talking and laughing. The room is filled with warm, cozy lighting. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_12.mp4` (Duration: 8.0s)
> Cinematic locked tripod close-up shot. Close-up of a hand-shake or physical touch between two people, releasing warm golden particles. Soft gray background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_13.mp4` (Duration: 8.0s)
> Cinematic slow tilt-down shot. A person writing their feelings in a journal, the words 'EXPERIENCE, EXPRESSION, RESOLUTION' appearing in gold ink. Warm lighting. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_14.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A heart silhouette opening like a door, letting out a stream of dark particles which then disperse and disappear into the warm air. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_15.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A diagram showing Mihaly Csikszentmihalyi's Flow model, indicating the optimal state of focus and engagement. Charcoal background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_16.mp4` (Duration: 8.0s)
> Cinematic slow panning medium shot. A person completely absorbed in painting on a canvas. The brush strokes glow in vibrant colors. Warm studio lighting. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_17.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A brain scan model showing decreased amygdala activation and increased prefrontal cortex connectivity. Clinical blue and gold tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_18.mp4` (Duration: 8.0s)
> Cinematic slow dolly-in close-up shot. A single green plant sprouting from a crack in a concrete sidewalk, bathed in warm sunshine. High contrast. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_19.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A serene lake reflecting a soft pink and purple sunset sky. Perfect calm, minimalist landscape. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_20.mp4` (Duration: 8.0s)
> Cinematic slow panning wide shot. A person walking down a peaceful forest pathway under tall pine trees. Dappled golden sunlight. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_21.mp4` (Duration: 8.0s)
> Cinematic locked tripod shot. A cup of hot tea steaming on a wooden table next to an open book. Cozy home interior, warm light. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_22.mp4` (Duration: 8.0s)
> Cinematic slow panning close-up shot. A person gently hugging themselves, eyes closed, with a soft smile of self-acceptance. Cozy and warm lighting. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_23.mp4` (Duration: 8.0s)
> Cinematic locked tripod close-up shot. Close-up of water droplets merging on a window pane during a gentle summer rain. Soft grey-blue background. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_24.mp4` (Duration: 8.0s)
> Cinematic slow panning shot. A river winding its way through a green valley, flowing smoothly around obstacles. Soft green and blue tones. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_25.mp4` (Duration: 8.0s)
> Cinematic slow panning wide shot. The camera slowly pans across the green valley toward a sunrise over distant mountains. Warm golden morning sun. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_26.mp4` (Duration: 8.0s)
> Cinematic locked tripod close-up shot. A close-up of a seedling growing in rich dark soil, watered by a gentle hand. Warm light. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 8.0s]

#### `chapter_06_scene_27.mp4` (Duration: 4.86s)
> Cinematic slow panning wide shot. A wide, majestic shot of a forest at sunrise. The fog rises, and the warm sun casts a golden glow over the entire landscape. Minimalist 2D vector illustration style, flat design, clean lines, geometric shapes, limited color palette, soft subtle gradients. [Length: 4.86s]

---

## 5. Hướng Dẫn Kỹ Thuật Đọc Và Ghép Nối (Rendering Instruction)
*   **Frame rate:** 24fps.
*   **Format:** 16:9 widescreen.
*   **Resolution:** 1080p hoặc 4K.
*   **Trình tự dựng:** Dựng các clip mp4 theo đúng số thứ tự cảnh `scene_XX` của từng chương, sau đó ghép nối trực tiếp với file wav tương ứng (`chapter_XX_v2.wav`). Tổng thời lượng video đầu ra sẽ khớp 100% với file âm thanh mà không cần thực hiện giãn hay tua nhanh khung hình.
