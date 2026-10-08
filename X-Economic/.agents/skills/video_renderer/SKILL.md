---
name: video-renderer
description: Huong dan dung hau ky va ghep noi video theo quy trinh I2V+.
---

# Video Renderer - Huong Dan Dung Hau Ky

> **Quy trinh dung tieu chuan:** Dựng video đi theo `/Users/pro16/Documents/VideoProject/.agents/contracts/i2v_quy_trinh_dung_video.md`: agent viet JSON infographic va chon canh broll, con render lo (`render_lo.py`), ghep chuong (`ghep_chuong.py`, chuyen canh lai, nen dong) va ghep tap (`ghep_tap_phim.py`) la script chay dong bo, in `KET_QUA:`. Mot tap mot mau nen tu dau den cuoi. Thu muc clip chuan la `videos/`. Duong dung thu cong tren phan mem dung phim chuyen nghiep (NLE) chi la du phong khi cong cu chuan loi; neu dung phai ghi ly do vao `production_notes.md`.

Ban chiu trach nhiem huong dan Operator va chuan bi tai nguyen de ghep noi cac phan canh video thanh mot video hoan thien duy nhat. Day la buoc hien thuc hoa san pham sau khi khau Hinh Anh va Thu Am ket thuc.

## Trach nhiem cot loi
Huong dan nguoi dung thuc hien dung phim theo quy trinh I2V+, dam bao su dong bo nhip nhang giua hinh anh va am thanh giong doc that.

## Bien Mac Dinh & Yeu Cau Dau Ra
Trong he thong [CHO USER XAC NHAN TEN VA HANDLE KENH], cau hinh mac dinh la:
- `Thu muc video dau vao`: `episodes/[slug]/videos/`
- `Thu muc voiceover`: `episodes/[slug]/` (chua cac file `chapter_XX.wav` da thu am va can chinh gio that)
- `Dinh dang xuat ra`: H.264, 1080p, 30fps, ty le 16:9.
- `File xuat ra`: `episodes/[slug]/video/slideshow_base.mp4`

## Duong du phong: dung thu cong tren NLE (chi khi cong cu chuan loi)
Nguoi dung thuc hien cac buoc sau tren phan mem dung chuyen nghiep (Premiere / DaVinci):
1. **Khoi tao Project**: Tao project moi co ty le khung hinh 16:9, do phan giai Full HD (1920x1080).
2. **Nhap tai nguyen (Import Assets)**:
   - Import toan bo file audio voiceover (`chapter_01.wav`, `chapter_02.wav`...) da thu am.
   - Import toan bo video clip `.mp4` tu thu muc `videos/` theo dung thu tu phan canh.
3. **Can chinh & Dong bo Timeline**:
   - Dat cac file voiceover lien tiep tren track audio.
   - Dat cac video clip tuong ung tren timeline video chinh (Main Track).
   - Co gian hoac cat tia (trim) thoi luong video clip sao cho khop chinh xac voi nhip doc thoai cua audio gio that.
4. **Nhac nen & Hieu ung am thanh**:
   - Import va long cac track nhac nen theo dung thiet ke am thanh tai Phase 13.
   - Dieu chinh am luong nhac nen nho xuong de ton giong doc thoai ro rang.
5. **Xuat video (Export)**:
   - Xuat video voi cau hinh: Resolution `1080p`, Frame rate `30fps`, Codec `H.264`, Format `MP4`.
   - Luu video da xuat vao duong dan `episodes/[slug]/video/slideshow_base.mp4`.

> **Luu y chat luong:**
> - **Giu nguyen chuyen dong camera goc**: Cac video clip duoc tao ra da co san chuyen dong camera dien anh. Khong tu y chen them hieu ung zoom/pan gia lap hoac cac transition re tien lam giam do tap trung cua nguoi xem.
> - **Khop nhip ke chuyen**: Cat canh (hard cut) dung vao diem ngat cau hoac chuyen y trong audio.

## Workflow Bat Buoc cua Agent
1. Nhan yeu cau huong dan ket xuat Video cho tap phim `[slug]`.
2. Kiem tra xem thu muc `videos/` co chua du cac clip `.mp4` tuong ung voi ban do nhip va cac file track hay khong.
3. Kiem tra xem file voiceover da duoc thu am va can chinh gio that chua.
4. Cung cap bang huong dan cu the (danh sach clip can ghep, thu tu va luu y nhip dieu) cho quy trinh ghep.
5. Cap nhat tien do va trang thai dung vao `episodes/[slug]/production_notes.md`.
6. Ban giao sang pha Production Handoff.
