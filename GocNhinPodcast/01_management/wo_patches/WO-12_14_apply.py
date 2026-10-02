import sys,os,re
ROOT=sys.argv[1]; E=[]
def R(f,old,new): E.append(('R',f,old,new))
def X(f,pattern,new,minc=1): E.append(('X',f,pattern,new,minc))   # regex theo dòng, >= minc lần
# ===== WO-12 hook / Ch.1 =====
R('.agents/skills/hook_engine/SKILL.md',"### Chặng 3: Thẩm Định Thẩm Mỹ & Ký Duyệt Master Hook (Critical Aesthetic Audit)",
"""### Chặng 2b: Cấu Trúc 30 Giây Đầu Và Chương 1 (chuẩn giữ chân, WO-12)
Người xem mới bấm vào vẫn đang thẩm định; đường giữ chân tụt mạnh nhất ở 30 giây đầu (YouTube Studio đo đoạn này ở mục Intro). Hook phải làm ba việc trong 20–30 giây, theo thứ tự:
1. **Xác nhận cú bấm (0–3 giây):** câu đầu cùng chủ thể, cùng điểm căng với tiêu đề và thumbnail đã chốt trong `00_hien_chuong.md`. Không chào hỏi, không giới thiệu kênh, không mở bằng niên biểu ("Năm 2015…").
2. **Đối nghịch nhìn thấy được:** điều người ta tưởng ≠ điều đang xảy ra, bằng một dữ kiện có mã M (không phóng đại, không nhãn phán xét).
3. **Điều được mất + câu hỏi trung tâm:** ai chịu ảnh hưởng theo điểm tựa đúng loại A/B/C (`00_core/content_principles.md` §2); kết bằng câu hỏi trung tâm nguyên văn hiến chương và một lộ trình rất ngắn (video sẽ đi qua đâu), không lộ đáp án.
Phần còn lại của Chương 1 (30 giây → ~3:30):
- **Ngữ cảnh tối thiểu** (Orientation Frame 45–60 giây): chỉ những gì cần để hiểu bước kế.
- **Mở, đóng, mở:** mở một câu hỏi nhỏ → trả lời nó (phần thưởng nhỏ) → mở câu kế. Không lồng câu hỏi trong câu hỏi ("muốn hiểu A phải biết B, trước B phải biết C"). Câu hỏi lớn của tập giữ mở tới cuối (Anti-Completion vẫn đúng: vòng nhỏ đóng, vòng lớn không).
- **Báo trước phần thưởng kế tiếp** trước khi trả xong phần thưởng hiện tại; **re-hook quanh 3:30** hứa giá trị đúng loại đề tài.
- Đổi nhịp (số liệu mới, câu hỏi phản biện, phép loại suy) mỗi 60–90 giây.
Ba phép thử trước khi chốt Master Hook: (a) **tắt tiếng**: nhìn thumbnail + đọc 2 câu đầu, có đoán được video nói về gì không; (b) **đặt cạnh thumbnail**: cùng một câu chuyện không; (c) **tắt sau hook**: người xem tắt ngay sau hook có thấy "đủ hiểu" không — có thì hook hỏng.

### Chặng 3: Thẩm Định Thẩm Mỹ & Ký Duyệt Master Hook (Critical Aesthetic Audit)""")
R('.agents/workflows/hook_lab.md',"   - Tạo 7 góc tiếp cận → 10 câu mở → chọn top 3 → chốt 1 câu mở chính + 5 câu móc giữa\n   - Chấm điểm từng câu mở: tò mò / gắn nỗi đau / tín hiệu chiều sâu / giữ chân / đúng kênh",
"   - Viết 3 biến thể Master Hook theo 3 Engine của `hook_engine/SKILL.md` (Chặng 2), mỗi biến thể đủ cấu trúc 30 giây đầu (Chặng 2b: xác nhận cú bấm 0–3 giây, đối nghịch có mã M, điều được mất + câu hỏi trung tâm nguyên văn hiến chương). Chốt 1 Master Hook, 1 câu re-hook ~3:30, và các câu móc chuyển chương theo đúng số chương của `07_outline.md`.\n   - Chấm từng biến thể bằng bảng ở `04_hook_pack_template.md` mục 3 và ba phép thử (tắt tiếng, đặt cạnh thumbnail, tắt sau hook).")
R('.agents/workflows/hook_lab.md',"   ✅ Kiểm tra TRÁNH AI-ISM:",
"   ✅ Kiểm tra CẤU TRÚC 30 GIÂY ĐẦU (hook_engine Chặng 2b):\n   [ ] Câu 1–2 cùng chủ thể và điểm căng với tiêu đề/thumbnail trong hiến chương; không chào hỏi, không niên biểu\n   [ ] Có đối nghịch bằng dữ kiện có mã M; có điều được mất đúng loại A/B/C; kết bằng câu hỏi trung tâm nguyên văn + lộ trình ngắn\n   [ ] Qua phép thử tắt tiếng và đặt cạnh thumbnail\n\n   ✅ Kiểm tra TRÁNH AI-ISM:")
f='02_templates/masterpiece_pipeline/04_hook_pack_template.md'
R(f,"### OPTION 2: ENGINE 2 — THE HIDDEN ARITHMETIC OF RUIN (TOÁN HỌC NGẦM CỦA SỰ ĐỔ VỠ)\n- **Góc tiếp cận:** Đặt khán giả trước phép tính số học trần trụi: Doanh thu hào nhoáng hoặc định giá tỷ đô đối đầu trực diện với dòng tiền âm, chi phí chìm hay điểm hòa vốn bất khả thi.",
"### OPTION 2: ENGINE 2 — THE TWO-MODEL COLLISION (VA CHẠM HAI MÔ HÌNH)\n- **Góc tiếp cận:** Đặt hai cách làm đối lập cạnh nhau (hai chiến lược, hai mô hình vận hành, hai luật chơi) và để dữ kiện có mã M lộ ra sự đánh đổi của mỗi bên: ai trả giá, điều gì quyết định bên nào đứng vững. Số tài chính chỉ dùng khi đề tài là tài chính (WO-00 Q10).")
R(f,"  > *`\"[Đoạn văn thoại sạch đối sánh dữ liệu thực chứng A vs con số nghiệt ngã B từ Vault...]\"`*\n- **Đánh giá ưu điểm:** Kích thích tò mò trí tuệ đỉnh cao, bóc trần ảo tưởng tài chính bằng logic số học không thể chối cãi.",
"  > *`\"[Đoạn văn thoại sạch đặt mô hình A cạnh mô hình B bằng dữ kiện có mã M...]\"`*\n- **Đánh giá ưu điểm:** Kích thích tò mò của người thích nhìn hệ thống; không cần số tài chính vẫn tạo được đối nghịch.")
R(f,"## 3. BẢNG ĐỐI CHIẾU & LỰA CHỌN MASTER HOOK",
"""## 2b. CẤU TRÚC 30 GIÂY ĐẦU CỦA MASTER HOOK (bắt buộc điền cho biến thể được chọn — `hook_engine` Chặng 2b)
| Nhịp | Nội dung | Mã nguồn |
|---|---|---|
| 0–3 giây: xác nhận cú bấm | `[câu 1–2: cùng chủ thể và điểm căng với tiêu đề/thumbnail trong 00_hien_chuong.md; không chào hỏi, không niên biểu]` | — |
| Đối nghịch | `[điều người ta tưởng ≠ điều đang xảy ra]` | `M-xx` |
| Điều được mất | `[theo loại A/B/C: ai chịu ảnh hưởng, vì sao bây giờ]` | `M-xx` |
| Kết hook | `[câu hỏi trung tâm nguyên văn hiến chương + lộ trình ngắn, không lộ đáp án]` | — |
| Re-hook ~3:30 | `[một câu hứa giá trị chặng kế, đúng loại đề tài]` | — |
- Phép thử: tắt tiếng `[đạt/không]` · đặt cạnh thumbnail `[đạt/không]` · tắt sau hook `[chưa đủ hiểu → đạt]`

## 3. BẢNG ĐỐI CHIẾU & LỰA CHỌN MASTER HOOK""")
R(f,"| **Sức hút 3 giây đầu (Thumb-Stop)** | [Điểm 1-10] | [Điểm 1-10] | [Điểm 1-10] |",
"| **Xác nhận cú bấm 0–3 giây (khớp thumbnail)** | [Điểm 1-10] | [Điểm 1-10] | [Điểm 1-10] |")
R(f,"- [ ] Hook nói lại đúng \"Lời hứa đóng gói\" ở `01_global_vision_synthesis.md`; người vừa bấm vào nhận ra mình đến đúng chỗ trong 10–15 giây đầu.",
"- [ ] Hook nói lại đúng \"Lời hứa đóng gói\" ở `01_global_vision_synthesis.md`; người vừa bấm vào nhận ra mình đến đúng chỗ trong 3 giây đầu (câu 1–2 khớp tiêu đề/thumbnail hiến chương).\n- [ ] Không mở bằng niên biểu, không chào hỏi; hook đặt câu hỏi, chưa kết luận (`stance_and_judgment` §8); câu hỏi trung tâm nguyên văn hiến chương.\n- [ ] Mục 2b điền đủ; qua ba phép thử (tắt tiếng, đặt cạnh thumbnail, tắt sau hook); có câu re-hook ~3:30.\n- [ ] Mọi số trong hook có mã `M-xx` (`00_so_du_kien.md`).")
f='00_core/golden_samples/golden_hook.md'
R(f,"15 giây đầu phải có ít nhất 1 trong 2: con số cụ thể có context, HOẶC một nhận định chuyên gia có lập trường. Nếu 15 giây đầu chỉ setup drama mà không có substance → viết lại.",
"15 giây đầu phải có ít nhất 1 trong 2: con số cụ thể có context (mã M), HOẶC một câu diễn giải cho thấy cách đọc riêng mà chưa kết luận. Nếu 15 giây đầu chỉ setup drama mà không có substance → viết lại. Câu 1–2 phải khớp tiêu đề và thumbnail (xác nhận cú bấm trong 3 giây).")
R(f,"### 7. Không tự đóng loop\nNếu người xem tắt video ngay sau hook mà cảm thấy đã đủ hiểu → hook thất bại. Hook phải kết bằng khoảng trống nhận thức mà PHẢI nghe tiếp mới lấp được.",
"### 7. Không tự đóng loop\nNếu người xem tắt video ngay sau hook mà cảm thấy đã đủ hiểu → hook thất bại. Hook phải kết bằng khoảng trống nhận thức mà PHẢI nghe tiếp mới lấp được.\n\n### 8. Mở, đóng, mở (phần còn lại của Chương 1)\nSau hook: mở câu hỏi nhỏ → trả lời (phần thưởng nhỏ) → mở câu kế; không lồng câu hỏi trong câu hỏi; báo trước phần thưởng kế trước khi trả xong phần thưởng hiện tại; re-hook ~3:30. Vòng nhỏ đóng, câu hỏi lớn giữ mở. Chi tiết: `.agents/skills/hook_engine/SKILL.md` Chặng 2b.")
R('00_core/longform_blueprint.md',"Nội dung nên có:\n- một dữ liệu hoặc contrast đủ mạnh,",
"Cấu trúc 30 giây đầu và phần còn lại của Ch.1 (xác nhận cú bấm 0–3 giây, đối nghịch, điều được mất, câu hỏi trung tâm; mở-đóng-mở; re-hook 3:30): `.agents/skills/hook_engine/SKILL.md` Chặng 2b (bản gốc duy nhất).\n\nNội dung nên có:\n- một dữ liệu hoặc contrast đủ mạnh,")
# ===== WO-14 template outline / briefs =====
f='02_templates/masterpiece_pipeline/07_outline_template.md'
R(f,"> 4. Tuyệt đối CẤM cắt xén số liệu hoặc cơ chế thực chứng để ép ngắn dưới Floor; nếu chương vượt trần 1.050 từ bắt buộc kích hoạt Quy tắc Phân hạch (Narrative Fission).",
"> 4. Tuyệt đối CẤM cắt xén số liệu hoặc cơ chế thực chứng để ép ngắn dưới Floor; nếu chương vượt trần 1.050 từ bắt buộc kích hoạt Quy tắc Phân hạch (Narrative Fission).\n> 5. **Trỏ mã, không chép câu:** Key Insight, Causal Exit, Mỏ neo, Data Checklist trỏ mã `M-xx` (`00_so_du_kien.md`), `E-xx`/`H-x` (`00_bang_gia_thuyet.md`); không khẳng định vượt nhãn của mã được trỏ. Chi tiết không có mã và không ghi \"minh họa\" là lỗi (`scripts/kiem_pha.py --pha 4`).")
X(f,r"^- \*\*Key Insight:\*\* .*$","- **Key Insight (trỏ mã):** `M-xx` / `E-xx` / `H-x` — một dòng theo đúng nhãn của mã; không viết lại thành khẳng định mới.",6)
X(f,r"^- \*\*Mỏ neo vật lý \(Physical Anchor\):\*\* \[.*\]\.$","- **Mỏ neo vật lý (Physical Anchor):** [vật thể có thật, có mã M hoặc OBS; không có nguồn thì ghi \"minh họa\" và không nêu số, địa danh, so sánh nhất].",5)
R(f,"- **Thách thức Phản đề Thép (Steelman Challenge):** [Tấn công đồng thời bằng mọi lăng kính đã chọn trong hiến chương tập].",
"- **Thách thức Phản đề Thép (Steelman Challenge):** [Tấn công đồng thời bằng mọi lăng kính đã chọn trong hiến chương tập].\n- **Bằng chứng BÁC và luận điểm đổi gì (bắt buộc, V26):** [mỗi mã E ngược với giả thuyết dẫn đầu trong `00_bang_gia_thuyet.md`: đặt ở đoạn nào của chương này, luận điểm chính giữ / thu hẹp / đổi thế nào, lý do]")
f='02_templates/masterpiece_pipeline/08_chapter_briefs_template.md'
R(f,"| **2** | `chapter_thesis` | Luận điểm cốt lõi — Chương này ta chứng minh điều gì? Tại sao? | Macro Strategist |",
"| **2** | `chapter_thesis` | Luận điểm cốt lõi — Chương này ta chứng minh điều gì? Tại sao? Trỏ giả thuyết `H-x` và các mã `M-xx` chịu lực; nhãn theo sổ dữ kiện. | Macro Strategist |")
R(f,"| **7** | `key_insight` | Insight bản chất đắt giá nhất chỉ chuyên gia chuyên sâu mới thấy. | Macro Strategist |",
"| **7** | `key_insight` | Insight bản chất đắt giá nhất — một dòng, trỏ mã `M-xx`/`E-xx`, viết đúng nhãn của mã (suy luận thì nói là suy luận). | Macro Strategist |")
R(f,"| **9** | `personal_or_relevance_angle` | Góc chiếu thực chứng đời thường (vật thể mỏ neo, tiếng nói hiện trường). | Macro Strategist |",
"| **9** | `personal_or_relevance_angle` | Góc chiếu thực chứng đời thường (vật thể mỏ neo có mã M/OBS, tiếng nói hiện trường có nguồn; không bịa chi tiết cảnh). | Macro Strategist |")
R(f,"| # | Data Point Cụ Thể | Con Số Thực Chứng | Tên File Trong `research_vault/` | Mã Footnote ID | Trích Dẫn Gốc (≤ 15 từ) | Trạng Thái |\n|---|---|---|---|---|---|---|",
"| # | Mã M (`00_so_du_kien.md`) | Data Point Cụ Thể | Con Số Thực Chứng | `OBS-…` hoặc Tên File Trong `research_vault/` | Mã Footnote ID | Trích Dẫn Gốc (≤ 15 từ) | Trạng Thái |\n|---|---|---|---|---|---|---|---|")
X(f,r"^\| (\d) \| \[Data Point Cốt Lõi \d\] \| \[Con số/Tỷ lệ % thực chứng \d\] \| `\[ten_file_nguon_\d\.md\]` \| `\[Footnote \d\]` \| \"\[trích dẫn nguyên văn ≤ 15 từ\]\" \| BẮT BUỘC \|$",
  r"| \1 | `M-xx` | [Data Point] | [Con số] | `OBS-…` / `[file.md]` | `[Footnote]` | \"[trích dẫn nguyên văn ≤ 15 từ]\" | BẮT BUỘC |",5)
errs=0
for op,*a in E:
    if op=='R':
        f,old,new=a; p=os.path.join(ROOT,f); s=open(p).read(); n=s.count(old)
        if n!=1: print(f"LỖI {f}: {n} lần :: {old[:50]!r}"); errs+=1; continue
        open(p,'w').write(s.replace(old,new)); print("OK",f)
    else:
        f,pat,new,minc=a; p=os.path.join(ROOT,f); s=open(p).read()
        s2,n=re.subn(pat,new,s,flags=re.M)
        if n<minc: print(f"LỖI {f}: regex {n} lần < {minc} :: {pat[:40]}"); errs+=1; continue
        open(p,'w').write(s2); print(f"OK {f} x{n}")
print("số sửa:",len(E)-errs,"lỗi:",errs); sys.exit(1 if errs else 0)
