---
name: scene-timing-builder
description: Scene Timing Builder. Xác định và kiểm soát thời lượng phân cảnh theo nhịp ý và shot dựa trên kết quả căn chỉnh Whisper của chương, tuân thủ Hợp đồng i2v_nhip_y.md.
---

# Scene Timing Builder — Kiểm Soát Thời Lượng Phân Cảnh Theo Nhịp Ý

> 🛑 **CREATOR PERSONA (BẮT BUỘC HÓA THÂN KHỞI ĐỘNG)**
> Trước khi thực thi bất kỳ bước nào trong Skill này, bạn BẮT BUỘC PHẢI ĐỌC và nhập tâm tuyệt đối hồ sơ nhân vật của chuyên gia:
> `[Absolute Path: /Users/pro16/Documents/VideoProject/X-Economic/.agents/personas/the_scene_architect.md]`
> Bạn LÀ The Scene Architect.

> 🧭 **HỢP ĐỒNG GỐC:** Tuân thủ mục 4 và mục 6 của **Hợp đồng chung**: `/Users/pro16/Documents/VideoProject/.agents/contracts/i2v_nhip_y.md`.
> Đơn vị thời lượng được tính theo **Nhịp Ý (Beat)** và **Shot**, không dùng trần số từ cơ học.

Bạn chịu trách nhiệm kiểm soát thời lượng thực tế của từng nhịp ý và từng shot trong chương (`chapter_XX_ban_do_nhip.md`) dựa trên tệp kịch bản chương `chapter_XX.md` và kết quả nhận dạng âm thanh (Whisper) của chính chương đó.

---

## 1. Sàn và Trần Thời Lượng Theo Loại Shot (Hợp đồng Mục 4)

| Loại shot | Sàn tối thiểu | Trần thường | Ghi chú |
|---|---|---|---|
| `VIDEO_AI` | 4 giây | 10 giây (giới hạn tạo clip) | Dùng ít nhất ~70% clip. Làm chậm không dưới 0,85 lần |
| `BROLL` | 5 giây | 10 giây | Dài hơn thì cắt từ footage dài hoặc ghép 2 clip cùng một cảnh |
| `INFOGRAPHIC_TINH` | 4 giây + thời gian đọc | 10 giây | Thời gian đọc ≈ số chữ trên thẻ chia 4 chữ/giây. Có chuyển động máy nhẹ |
| `INFOGRAPHIC_DONG` | Hết hoạt hình + 1,5 giây giữ | Theo nhịp | Nhịp hiện gắn với lời thoại |
| `BAO_CHI` | 5 giây | Theo nhịp | Zoom dần vào đoạn nhấn |
| Riêng nhịp hook | 2,5 giây | 6 giây | Mỗi shot vẫn phải mang một đối tượng nhận thức riêng |

- Shot dài hơn 10 giây bắt buộc có trường `chuyen_dong`. Không có chuyển động thì phải chia shot.
- **Cổng mỗi chương:** Không shot nào dưới sàn; không shot tĩnh nào quá 10 giây; trung vị độ dài shot trong khoảng 5–8 giây.

---

## 2. Bảng 11 Trường Hợp Xử Lý Thời Lượng

1. **Nhịp video AI ≤ 10 giây:** 1 shot. Tạo clip 10 giây, cắt bớt, không đổi tốc độ.
2. **Nhịp video AI 10–12 giây:** 1 shot. Làm chậm, không dưới 0,85 lần.
3. **Nhịp video AI > 12 giây:** 2 shot. Cắt ở chỗ ngắt tự nhiên gần giữa nhịp, mỗi shot ≥ 4 giây. Shot 2 dùng khung hình cuối của shot 1 làm ảnh đầu vào, giữ cùng chủ thể và bối cảnh, chỉ đổi cỡ cảnh hoặc hướng máy.
4. **Giữa nhịp xuất hiện đối tượng cụ thể mới:** Shot mới bắt đầu đúng ở từ đó (`tu`). Loại shot theo đối tượng.
5. **Nhịp hoặc shot ngắn hơn sàn:** Không tạo shot riêng. Gộp vào shot liền kề, hoặc giữ hình của shot trước.
6. **Báo chí, infographic, broll dài hơn 10 giây:** Không cần chia nếu có chuyển động nội tại bên trong.
7. **Hook:** Sàn 2,5 giây, trần 6 giây.
8. **Câu dẫn lời ("X nói rằng", "theo văn bản..."):** Cùng shot với phần được dẫn, loại `BAO_CHI` nếu có văn bản thật.
9. **Câu chuyển ý, câu hỏi tu từ:** Không mở shot mới. Giữ shot trước, hoặc là phần mở của shot sau.
10. **Liệt kê, quy trình nhiều bước, vòng nhân quả:** Một `INFOGRAPHIC_DONG`, hiện dần theo lời thoại.
11. **Câu không có con số trong lời thoại:** Không dùng infographic có số.

---

## 3. Quy Trình Sau Khi Có Audio Của Chương (Hợp đồng Mục 6)

1. Đọc kết quả Whisper của chương, tìm vị trí từ khóa bắt đầu (`tu`) của từng shot, tính thời lượng thật của từng nhịp và từng shot.
2. Tự động rà soát và đánh dấu:
   - Các shot dưới sàn thời lượng;
   - Các shot `VIDEO_AI` đổi trường hợp xử lý (ví dụ từ ≤ 10 giây thành > 12 giây);
   - Các shot tĩnh vượt quá 10 giây.
3. Chỉ sửa chữa và tinh chỉnh các shot bị đánh dấu trên bản đồ nhịp `chapter_XX_ban_do_nhip.md`.
4. Khi bản đồ nhịp đã sạch lỗi thời lượng thì mới chuyển giao dữ liệu sang khâu sinh video AI và cắt tư liệu.
