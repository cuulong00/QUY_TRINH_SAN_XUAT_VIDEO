---
name: visual_prompter_plus
description: Lập kế hoạch hình ảnh I2V+ cho từng chương theo nhịp ý cho kênh X-Economy. Đọc trọn chapter_XX.md, chia nhịp ý, chọn loại shot theo chức năng của ý (broll tư liệu lịch sử/hiện trường, báo chí/văn kiện, infographic dữ liệu/sơ đồ tĩnh hoặc động, video AI điện ảnh lịch sử), rồi viết bản đồ nhịp và 4 file track theo hợp đồng chung .agents/contracts/i2v_nhip_y.md.
---

# Visual Prompter Plus — lập kế hoạch hình theo nhịp ý — Kênh X-Economy

**Hợp đồng kỹ thuật:** `/Users/pro16/Documents/VideoProject/.agents/contracts/i2v_nhip_y.md`. Hợp đồng quy định tên file, định dạng trường, sàn và trần thời lượng, bảng trường hợp, số liệu, cách ráp. Skill này quy định cách **nghĩ**: chia nhịp thế nào, chọn hình thế nào trong bối cảnh phim tài liệu lịch sử, địa chính trị và kinh tế chính trị. Hai file mâu thuẫn nhau thì hợp đồng thắng về kỹ thuật, skill thắng về biên tập; báo Claude để sửa.

**Vì sao có bản 2.** Bản 1 lấy câu thoại làm đơn vị: trần 26 từ, cây quyết định chạy theo từng câu, phân tách cơ học. Hậu quả là video bị vụn nát, nhiều cảnh 1–3 giây vô nghĩa, infographic có số bịa, hoạt hình bị cắt giữa chừng. Bản 2 bãi bỏ hoàn toàn đơn vị câu thoại và các hạn ngạch số học cơ học, chuyển sang thiết kế theo nhịp ý trọn vẹn.

---

## 1. Nguyên tắc

1. **Hình phục vụ ý, không phục vụ câu.** Đơn vị là nhịp ý (một ý trọn vẹn trong tiến trình lịch sử/thể chế, thường 2–4 câu). Một nhịp có một hoặc vài shot.
2. **Chỉ đổi hình khi có lý do nhìn thấy được.** Lời thoại chuyển sang một đối tượng cụ thể mới (con số, văn kiện/hiệp định, địa danh/chiến trường/cảng biển, nhân vật lịch sử, tổ chức thể chế), hoặc sang ý khác. Hết câu không phải lý do đổi hình.
3. **Người xem phải kịp hiểu hình.** Thời lượng theo sàn của từng loại (hợp đồng mục 4), không theo độ dài câu chữ.
4. **Cụ thể thì hiện đúng thứ cụ thể, trừu tượng mới dùng ẩn dụ.** Lời thoại nói về Kênh đào Panama hay Funan Techo thì hiện đúng bản đồ và tư liệu công trình đó; nói về xung đột thể chế hay động lực ngầm mới dùng hình ảnh ý niệm.
5. **Số liệu trên màn hình chỉ là số trong lời thoại và sổ claim** (hợp đồng mục 5).
6. **Một agent làm cả chương**, từ đầu đến cuối, theo đúng `chapter_XX.md`. Không làm từ `voiceover.md`.

## 2. Đầu vào

Đọc theo thứ tự trước khi viết dòng nào:
1. `episodes/[slug]/chapter_XX.md`: đọc trọn chương, hai lần. Lần đầu để nắm bắt mạch lập luận lịch sử/địa chính trị, lần sau để đánh dấu chỗ ý đổi.
2. `07_outline.md`, phần của chương này: vai trò của chương trong toàn bộ đại chiến lược của tập phim.
3. `10_compliance_report.md`: sổ claim đối chiếu sử liệu và số liệu, để gắn mã kiểm chứng cho mọi con số/sự kiện.
4. `visual_storyboard_blueprint_plus.md` của tập: bảng màu (Ngà kem `#FAF7EE`, Slate `#1E293B`, Hổ phách `#F59E0B`), danh sách ảnh tham chiếu nhân vật/sử liệu, bối cảnh địa lý và niên đại lịch sử. Blueprint được tổng hợp từ các chương, không đọc `voiceover.md`.
5. Bản đồ nhịp của chương liền trước (nếu có), để nối mạch vận động thị giác liền mạch, không lặp lại góc máy hay loại hình.

## 3. Quy trình

### Bước 1: Chia nhịp ý
Đi qua chương, đánh dấu chỗ ý đổi. Mỗi đoạn giữa hai dấu là một nhịp.
Các quy tắc gộp:
- **Câu dẫn lời/văn kiện đi cùng phần được dẫn.** "Bản mật ước năm 1898 nêu rõ..." và nội dung thỏa thuận là một nhịp.
- **Câu hỏi tu từ, câu hỏi chiến lược đi cùng câu phân tích/trả lời ngay sau nó**, trừ khi là câu hỏi chốt hồi ở cuối chương.
- **Câu chuyển ý, câu cầu nối không mở nhịp mới.** "Nhưng bàn cờ địa chính trị không dừng lại ở đó" là phần mở của nhịp sau hoặc phần đuôi của nhịp trước.
- **Quy trình nhiều bước, mạch truyền dẫn thể chế/tiền tệ, diễn biến chiến dịch là một nhịp**, hiện dần qua sơ đồ động hoặc chuỗi tư liệu.
- **Hai câu đối chiếu lịch sử/thể chế là một nhịp.** "Trên danh nghĩa là hiệp định hòa bình. Dưới mặt đất là sự chuẩn bị cho cuộc viễn chinh tiếp theo."

Nhịp ước tính dài hơn khoảng 15 giây thì xem lại: có phải chứa hai ý tách biệt không?

### Bước 2: Chọn loại shot theo chức năng của ý

Hỏi theo thứ tự. Câu đầu tiên trả lời "có" quyết định loại.

| Câu hỏi | Có thì | Ghi chú cho X-Economy |
|---|---|---|
| Ý này **không cần hình mới** (chuyển ý, đệm, nhắc lại)? | **Giữ shot trước** hoặc gộp vào shot sau | Giữ nguyên khung hình hoặc chuyển động máy tiếp diễn |
| Ý **trích dẫn văn bản, điều ước, hiệp định, luật, bài báo lịch sử, phát ngôn có thật**? | `BAO_CHI` | Cần nguồn, mộc văn bản hoặc URL bài báo có thật. Khóa tiêu cự vào chữ |
| Ý **nêu số liệu, so sánh tương quan, dòng ngân sách, cán cân** có trong lời thoại? | `INFOGRAPHIC_DONG` nếu so sánh, biến đổi theo mốc năm, nhiều số; `INFOGRAPHIC_TINH` nếu một con số then chốt | Câu không có số thì không dùng infographic có số |
| Ý **là cơ chế thể chế, chuỗi giá trị, mạch truyền dẫn vốn, sơ đồ liên minh**? | `INFOGRAPHIC_DONG` dạng sơ đồ/sankey/flow, hiện dần | Chỉ dùng nhãn chữ và mũi tên định hướng, không bịa số |
| Ý **nói về nơi chốn, địa danh, công trình, vũ khí, tàu thuyền, sự kiện lịch sử có tư liệu lưu trữ/quay được**? | `BROLL` | Hiện đúng đối tượng lịch sử/hiện trường thật (Fair Use, scale 104%, bỏ audio gốc) |
| Còn lại: không khí sử thi, phòng họp chiến lược kín, tâm trạng lãnh đạo, bối cảnh cổ xưa không thể quay | `VIDEO_AI` | Theo mục 4.4, đúng niên đại và địa lý |

Trong một nhịp, shot mới bắt đầu ở từ mà đối tượng mới xuất hiện (hợp đồng, trường hợp 4).
**Không có quota, không có luật xoay vòng.** Ba shot B-roll tư liệu liền nhau là hoàn toàn đúng nếu ba ý đều gắn với thực tế hiện trường lịch sử. Chống mỏi nhận thức bằng sự biến đổi góc máy, thời lượng đọc và chuyển động, không ép đổi loại shot cơ học.

### Bước 3: Ước thời lượng, áp bảng trường hợp
Ước thời lượng mỗi nhịp và mỗi shot bằng số tiếng chia tốc độ đọc chuẩn của kênh X-Economy (`223–235 từ/phút`, tức khoảng **3.7–3.9 từ/giây**, lấy chuẩn 3.8 từ/giây).
Áp bảng trường hợp của hợp đồng: shot dưới sàn thì gộp; nhịp video AI trên 12 giây thì chia 2 shot nối tiếp (`lien_mach`); shot trên 10 giây bắt buộc ghi chuyển động bên trong.

### Bước 4: Viết bản đồ nhịp, dừng ở cổng duyệt
Viết `chapter_XX_ban_do_nhip.md` đúng định dạng của hợp đồng mục 3, sau đó chạy script kiểm tra định dạng. Dừng lại chờ User và Claude duyệt. Tuyệt đối không viết 4 file track khi bản đồ nhịp chưa được phê duyệt.

### Bước 5: Viết 4 file track
Sau khi bản đồ nhịp được duyệt, viết:
- `chapter_XX_video_ai.md`
- `chapter_XX_broll.json`
- `chapter_XX_infographic.md`
- `chapter_XX_bao_chi.md`
Mỗi shot ứng đúng một khối theo quy chuẩn tại mục 4. Mọi prompt, từ khóa và mô tả phải do chính agent viết tay, thẩm thấu toàn bộ ngữ cảnh của nhịp. Tuyệt đối không dùng script tự động sinh prompt.

### Bước 6: Sau khi có audio
Chạy lại script kiểm tra với Whisper của chương (hợp đồng mục 6). Chỉ điều chỉnh các shot bị đánh dấu cảnh báo (dưới sàn, đổi trường hợp, tĩnh quá 10s).

---

## 4. Năm loại shot trong phim tài liệu X-Economy

### 4.1 `BROLL`: Hiện trường thực tế & Tư liệu lưu trữ lịch sử
- **Dùng cho:** Địa danh, công trình, tàu thuyền, nhà máy, cảng biển, hoặc các sự kiện lịch sử có tư liệu lưu trữ (footage kho lưu trữ, phim tài liệu lịch sử, lễ ký kết, phiên điều trần).
- **Trường bắt buộc:** `y_hinh` (hình cần thấy), `muc_khop` (`doi_tuong`: phải thấy đúng chủ thể; `boi_canh`: chỉ cần đúng nơi, loại cảnh, thời kỳ), `boi_canh_chap_nhan` (một câu tả bối cảnh nào là được), `tu_khoa_san` (ít nhất 2 ngôn ngữ, chọn theo `i2v_quy_trinh_broll.md` mục 1b: tên chủ thể viết theo tiếng bản địa, từ loại cảnh nhìn thấy được, không đưa từ trừu tượng của lời thoại vào), `phuong_an_thay` (phương án góc máy hoặc chủ thể dự phòng), `fair_use` (cắt tối thiểu 5s, scale 104%, tước bỏ 100% audio gốc `-an`, chỉnh tông Warm Slate Tone).
- **Chỉ gán `BROLL` khi đối tượng có khả năng có tư liệu thật** (nguồn chính chủ, đài và hãng tin, kho tư liệu). Ý không quay được thì chọn loại khác ngay trong bản đồ nhịp. Quy trình săn chi tiết: `/Users/pro16/Documents/VideoProject/.agents/contracts/i2v_quy_trinh_broll.md`.
- **Thời lượng:** Sàn 5 giây, trần thường 10 giây (chuẩn 5.5s–7.0s). Dài hơn thì cắt từ footage dài hoặc ghép 2 clip cùng một bối cảnh.
- Không có tư liệu thật cho đối tượng cụ thể thì ghi rõ trong file để tìm phương án thay thế, không tự ý chuyển sang ảnh AI giả mạo tư liệu lịch sử.

### 4.2 `BAO_CHI`: Văn kiện pháp lý, hiệp ước & chứng cứ báo chí
- **Dùng cho:** Tít báo tài chính/thời sự, điều ước quốc tế, văn bản nghị định, bản đồ hiệp định, báo cáo kiểm toán, phát ngôn chính thức.
- **Trường bắt buộc:** `nguon`, `url`, `tieu_de_goc`, `doan_nhan` (chép nguyên văn cụm từ trên tài liệu), `kieu_nhan` (gạch chân / viền khung đỏ/hổ phách), `anh_chup` (đường dẫn ảnh chụp thật từ nguồn gốc hoặc báo giấy).
- **Luật bản quyền & tính xác thực:**
  - Khóa tiêu cự vào chữ (tiêu đề, điều khoản, con số).
  - Ảnh phóng sự của bên thứ ba trong trang báo phải làm mờ hoặc crop bỏ để triệt tiêu rủi ro bản quyền.
  - Tuyệt đối cấm dùng script HTML/Canvas hay Pillow tự vẽ giả mạo trang báo/văn bản. Mọi callout phải xuất phát từ tài liệu thật.
- **Dựng:** HyperFrames ở chế độ phim tài liệu từ ảnh chụp thật.

### 4.3 `INFOGRAPHIC_TINH` và `INFOGRAPHIC_DONG`: Báo chí dữ liệu & Cấu trúc thể chế
- **Tĩnh:** Một con số trọng tâm (Hero Metric), một mốc năm lịch sử, hoặc một thẻ đối chiếu đơn giản. Có chuyển động máy nhẹ (subtle push-in).
- **Động (HyperFrames):** So sánh tương quan 2-3 đại lượng qua các thời kỳ, sơ đồ dòng vốn/thuế quan, trục tiến độ lịch sử (Roadmap Timeline), bản đồ phân bổ địa lý. Các thành phần xuất hiện tuần tự bám sát từng từ thoại (trường `nhip_hien`).
- **Trường bắt buộc:** `kieu` (`tinh` | `dong`), `mau` (một mã mẫu trong `/Users/pro16/Documents/VideoProject/.agents/contracts/i2v_quy_trinh_hyperframes.md`; ý không vừa mẫu nào thì đổi loại shot), `bo_cuc`, `so_lieu` (kèm mã claim trong `10_compliance_report.md`), `nhan_chu` (nhãn danh mục tiếng Việt đĩnh đạc), `nhip_hien` (cho thẻ động).
- Bãi bỏ quy tắc cơ học "một con số duy nhất mỗi thẻ". Một nhịp chứa nhiều số liệu đối chiếu thì trình bày trên một đồ thị/bảng so sánh thống nhất, hiện dần theo lời dẫn.
- Bảng màu: Nền Slate trầm `#1E293B` hoặc Than chì `#0F172A`, chữ màu ngà `#FAF7EE`, màu nhấn hổ phách `#F59E0B` hoặc Cyan `#00C2CB`.
- **Khóa Cương Vực Hải Đảo Thép:** Bất kỳ bản đồ nào có lãnh thổ Việt Nam bắt buộc mô tả đầy đủ quần đảo Hoàng Sa, quần đảo Trường Sa, đảo Phú Quốc, Côn Đảo; tuyệt đối cấm đường chín đoạn / đường lưỡi bò phi pháp.

### 4.4 `VIDEO_AI`: Không gian chiến lược & Hiện trường lịch sử tái hiện
- **Dùng cho:** Không gian nội tâm của các nhà hoạch định chiến lược, phòng họp kín bên sa bàn/bản đồ, đại cảnh địa kinh tế hùng vĩ, hoặc bối cảnh các thời kỳ lịch sử xa xưa không có máy quay ghi lại.
- **Không dùng cho:** Cảnh đời thường đã có tư liệu thực tế (dùng `BROLL`); văn bản, tài liệu lưu trữ (dùng `BAO_CHI`); biểu đồ, số liệu (dùng `INFOGRAPHIC`).
- **Trường bắt buộc:** `prompt_anh`, `prompt_video` (chỉ tả chuyển động quang học của camera và ánh sáng môi trường, tuyệt đối không ghi tên người thật), `anh_tham_chieu` (tag `@ref_image.jpg`), `lien_mach` (nếu nối tiếp shot trước), `thoi_luong` (≤ 10 giây).
- **Hành động an toàn:** Tuân thủ danh sách hành động an toàn trong `personas/the_scene_architect.md`. Không cử động ngón tay phức tạp, không tương tác vật lý va chạm mạnh, không xe cộ đánh lái gấp, nhân vật không mấp máy môi nói chuyện.
- **Bối cảnh và nhân chủng học theo đúng nơi và thời kỳ câu chuyện diễn ra:** Câu chuyện diễn ra ở châu Âu, Trung Đông hay thời phong kiến thì kiến trúc, con người, trang phục phải đúng chuẩn mực niên đại và địa lý đó. Không áp đặt nhân chủng học Việt Nam hiện đại cho các bối cảnh ngoại quốc hoặc lịch sử cổ xưa.
- **Shot nối tiếp (nhịp > 12 giây):** Shot 2 bắt buộc dùng khung hình cuối của Shot 1 làm ảnh đầu vào, giữ nguyên bối cảnh và chủ thể, chỉ thay đổi cỡ cảnh (từ Medium shot sang Close-up) hoặc hướng máy quay.

---

## 5. Tự kiểm trước khi nộp

**A. Máy kiểm (Script theo hợp đồng mục 7):**
- `cau_thoai` khớp 100% toàn văn chương.
- Mỗi shot có đúng một khối trong đúng một file track tương ứng.
- Thời lượng shot tuân thủ sàn và trần quy định.
- Mọi con số hiển thị đều có trong lời thoại của nhịp và có mã claim hợp lệ.

**B. Người kiểm (Biên tập viên tự rà soát):**
1. Mỗi shot có làm nổi bật một **đối tượng nhận thức cụ thể** không?
2. Shot có bị đổi tùy tiện khi **ý chưa đổi** không? Nếu cùng ý thì gộp lại.
3. Câu dẫn lời, trích dẫn văn kiện có đi liền với phần nội dung được dẫn không?
4. Khán giả có đủ thời gian đọc và tiếp thu thông tin trên thẻ đồ họa không?
5. Có con số nào xuất hiện trên màn hình mà **không được nói trong lời thoại** không?
6. Bối cảnh lịch sử, trang phục và nhân vật AI có đúng niên đại và địa lý không?

---

## 6. Ví dụ minh họa (Khuôn mẫu phân cảnh theo Nhịp Ý)

**Bản đồ nhịp chuẩn:**
```markdown
### CH01_N01
- cau_thoai:
  > Năm mươi tỷ USD thâm hụt thương mại. Con số này không chỉ phản ánh cán cân xuất nhập khẩu đơn thuần.
  > Đằng sau nó là sự dịch chuyển của toàn bộ chuỗi cung ứng công nghệ toàn cầu.
- y: Mở đầu bằng quy mô thâm hụt thương mại và ý nghĩa chiến lược đối với chuỗi cung ứng.
- thoi_luong_uoc: 8
- shots:
  - CH01_N01_S1 | INFOGRAPHIC_TINH | tu: "Năm mươi tỷ USD" | ly_do: hiển thị biểu đồ thanh cán cân thương mại và giá trị 50 tỷ USD | so: 50 tỷ USD (DATA-01)
  - CH01_N01_S2 | BROLL | tu: "Đằng sau nó là" | ly_do: cảng biển quốc tế nhộn nhịp tàu hàng container chuyển động | so: không

### CH01_N02
- cau_thoai:
  > Kim ngạch xuất khẩu linh kiện vi điện tử ghi nhận mức kỷ lục.
  > Nhưng cùng lúc đó, tỷ lệ nội địa hóa thực tế của các nhà máy lắp ráp chỉ đạt dưới mười lăm phần trăm.
  > Một bên là sản lượng xuất khẩu ấn tượng. Một bên là giá trị gia tăng nội tại còn rất mỏng. Cả hai đều là số liệu chính thức từ báo cáo quản lý thương mại.
- y: Sự đối chiếu giữa kim ngạch xuất khẩu bề nổi và tỷ lệ giá trị gia tăng nội địa thực tế.
- thoi_luong_uoc: 14
- shots:
  - CH01_N02_S1 | INFOGRAPHIC_TINH | tu: "Kim ngạch xuất khẩu" | ly_do: biểu đồ phân rã cơ cấu giá trị gia tăng đối chiếu hai tỷ lệ | so: 15% (DATA-02)
  - CH01_N02_S2 | BAO_CHI | tu: "Một bên là sản lượng" | ly_do: trang bìa báo cáo thường niên của cơ quan quản lý thương mại quốc tế | so: không

### CH01_N06
- cau_thoai:
  > Mức thuế quan mới không chỉ là một quyết định hành chính tạm thời.
  > Nó định hình lại hiệp định khung thương mại song phương trong cả thập kỷ tới.
  > Đích xa hơn là năm 2035, khi các chuỗi cung ứng chiến lược hoàn tất việc tái định vị địa lý.
  > Cơ quan điều hành đặt mục tiêu tái cơ cấu ngay từ giai đoạn đầu.
  > Năm nay vì vậy là mốc khởi đầu của cả lộ trình chuyển dịch sản xuất.
- y: Tác động thể chế dài hạn của chính sách thuế quan và lộ trình tái cơ cấu chuỗi cung ứng.
- thoi_luong_uoc: 20
- shots:
  - CH01_N06_S1 | BAO_CHI | tu: "Mức thuế quan mới" | ly_do: bản chụp văn bản hiệp định thương mại song phương chính thức | so: không
  - CH01_N06_S2 | INFOGRAPHIC_TINH | tu: "Đích xa hơn là" | ly_do: trục thời gian lộ trình chuyển dịch chuỗi cung ứng qua các năm | so: 10 năm (DATA-03); 2035 (DATA-03)
  - CH01_N06_S3 | BROLL | tu: "Năm nay vì vậy là" | ly_do: dây chuyền đóng gói vi mạch tự động hóa cao trong nhà máy hiện đại | so: không
```

**Các lỗi nghiêm trọng của cách làm cũ - đã bỏ, tuyệt đối không lặp lại:**
- Tách mẩu câu dẫn lời ("Theo Cục Thống kê,", "Báo cáo chỉ rõ:") thành shot riêng 1–2 giây.
- Biến câu nối/chuyển ý ("Vậy câu chuyện thực sự là gì?") thành một shot riêng biệt vô nghĩa.
- Cắt vụn một cơ chế đối chiếu tương phản thành các mảnh rời rạc thay vì gom vào một thẻ đồ họa hoàn chỉnh.
- Tự bịa thêm các con số phần trăm không có trong lời thoại kịch bản vào thẻ đồ họa để "làm đẹp" khung hình.
- Cắt B-roll dưới 5 giây khiến hình ảnh giật cục, vi phạm sàn thời lượng B-roll.

