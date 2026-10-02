import sys,os
ROOT=sys.argv[1]; E=[]
def R(f,old,new,tag): E.append(('R',f,old,new,tag))
def P(f,header,tag): E.append(('P',f,header,None,tag))   # chèn đầu file nếu chưa có
f='00_core/stance_and_judgment.md'
R(f,'| "Đó là một ảo ảnh thương mại." | "Khoảng 1.500 chiếc đã sang châu Âu. Gần như không chiếc nào đến tay một người mua cá nhân. Người mua là GSM, cùng nằm trong nhà Vingroup." |',
    '| "Đó là một ảo ảnh thương mại." | "Lô tàu Sea Patris tháng 7/2026 chở khoảng 1.500 xe VF 6 sản xuất riêng cho GSM (`OBS-0a1f03ba501ff9f2`; GSM công bố hơn 1.300 xe, `OBS-a93e5b03ae44a7b6`). Trong hai năm 2024–2025, VinFast bán lẻ ở Hà Lan 28 xe (`OBS-edd9166742f77150`). Người mua lô này là GSM, cùng nằm trong Vingroup." |',"Q12")
R(f,'| "Gánh nặng tài chính tự sát." | "Mỗi ngày, lãi vay của tập đoàn là 113 tỷ đồng." |',
    '| "Gánh nặng tài chính tự sát." | "Chi phí lãi vay hợp nhất của Vingroup năm 2025 là 29.160 tỷ đồng (`OBS-0a95967c83f5df86`)." |\n\nSố trong ví dụ phải có mã OBS hiện hành. Không tự chia ra số "mỗi ngày" (phép tính kênh tự làm) và không đặt số toàn tập đoàn cạnh doanh thu một mảng hay một thị trường (lệch phạm vi, sổ vấn đề V16).',"Q12")
R(f,'| Dữ kiện | `verified_data` | Nói thẳng, không rào đón | "VinFast xác nhận với SEC rằng đội taxi là phòng lái thử di động." |',
    '| Dữ kiện | `verified_data` | Nói thẳng, không rào đón | "Hồ sơ VinFast nộp SEC (424B3, F-1) nói hợp tác với GSM mang lại cơ hội cho khách quốc tế lái thử và trải nghiệm xe (`OBS-70086fcb436a21a8`)." |',"Q12")
R(f,'> Ví dụ: "Nếu Vingroup còn đủ sức bù chi phí này thêm ba năm, GSM có thể thành cửa vào châu Âu thật. Nếu dòng tiền Vinhomes chững lại trước đó, châu Âu sẽ là chi phí đầu tiên bị cắt. Chỉ số đáng theo dõi là số xe đăng ký cá nhân ở Hà Lan qua từng quý. Bạn đặt cược vào kịch bản nào?"',
    '> Ví dụ (minh họa cấu trúc, không phải dữ kiện): "Nếu GSM giữ nhịp mở rộng ở châu Âu thêm ba năm và số xe đăng ký cá nhân tăng theo, GSM có thể thành cửa vào châu Âu thật. Nếu tập đoàn thu hẹp mở rộng nước ngoài trước đó, châu Âu là mảng đầu tiên bị cắt. Chỉ số đáng theo dõi là số xe VinFast đăng ký cá nhân ở Hà Lan qua từng quý. Bạn đặt cược vào kịch bản nào?"',"Q12")
R(f,'> ✅ "Hồ sơ gửi SEC gọi đội taxi GSM là phòng lái thử di động. Nhưng một phòng lái thử chỉ có ý nghĩa khi có người bước ra mua xe. Tới giờ, gần như toàn bộ xe VinFast sang châu Âu vẫn do chính GSM đứng tên. Nên câu hỏi đáng đặt ra không còn là GSM có chạy được ở Amsterdam hay không, vì chấp nhận bù lỗ thì chạy được. Câu hỏi là bảng cân đối của Vingroup sẽ trả tiền cho phòng lái thử này trong bao lâu. Chúng tôi đặt cược rằng đó mới là phép thử thật. Và nếu năm tới số xe đăng ký cá nhân ở Hà Lan tăng rõ rệt, chúng tôi sẵn sàng nhận mình đã đọc sai."',
    '> ✅ "Hồ sơ VinFast nộp SEC nói hợp tác với GSM cho khách quốc tế cơ hội lái thử xe (`OBS-70086fcb436a21a8`). Nhưng một chuyến lái thử chỉ có ý nghĩa khi có người bước ra mua xe. Lô 1.500 xe VF 6 sang châu Âu tháng 7/2026 được sản xuất riêng cho GSM (`OBS-0a1f03ba501ff9f2`); hai năm trước đó VinFast bán lẻ ở Hà Lan 28 xe (`OBS-edd9166742f77150`). Nên câu hỏi đáng đặt ra không còn là GSM có chạy được ở Amsterdam hay không. Câu hỏi là đội taxi có biến khách đi xe thành người mua xe không, và luật chơi ở Đan Mạch, Hà Lan có cho GSM lợi thế nào mà Uber, Bolt không có. Chúng tôi đặt cược rằng đó mới là phép thử thật. Và nếu năm tới số xe đăng ký cá nhân ở Hà Lan tăng rõ rệt, chúng tôi sẵn sàng nhận mình đã đọc sai."',"Q12")
H="> ⚠️ Số liệu trong file này lấy từ tập `gdp-quy-1-2026` (đã xuất bản, quý I/2026) và chỉ để minh họa cấu trúc câu, nhịp và giọng. KHÔNG chép số sang tập khác; mọi số trong kịch bản phải có mã OBS hoặc nguồn vault riêng (WO-03).\n\n"
for g in ['.agents/examples/chapter_writer_examples.md','.agents/examples/content_strategy_examples.md','.agents/examples/editorial_qa_examples.md','.agents/examples/editorial_quality_examples.md','.agents/examples/hook_engine_examples.md','.agents/examples/oral_polisher_examples.md','00_core/golden_samples/golden_analysis.md','00_core/golden_samples/golden_transition.md']:
    P(g,H,"R3")
errs=0
for op,f,a,b,tag in E:
    p=os.path.join(ROOT,f); s=open(p).read()
    if op=='R':
        n=s.count(a)
        if n!=1: print(f"LỖI {tag} {f}: chuỗi cũ xuất hiện {n} lần"); errs+=1; continue
        s=s.replace(a,b)
    else:
        if a.strip() in s: print(f"BỎ QUA {tag} {f}: đã có header"); continue
        lines=s.split('\n',1)
        s = lines[0]+'\n\n'+a+(lines[1] if len(lines)>1 else '') if lines[0].startswith('#') else a+s
    open(p,'w').write(s); print(f"OK {tag} {f}")
print("lỗi:",errs); sys.exit(1 if errs else 0)
