#!/usr/bin/env python3
"""Cổng máy kiểm đầu ra từng pha của một tập (WO-09).

Dùng:  KB_GRAPH=kb_v2 scripts/kiem_pha.py <slug|đường dẫn tập> [--pha 1|2|3|4|7|8|all] [--khong-kho]
Mỗi lỗi một dòng: [MÃ] file:dòng — mô tả. Thoát 1 nếu có lỗi. Chạy TRƯỚC mọi lần người chấm đọc.

Kiểm (mã lỗi ↔ sổ vấn đề):
  OBS-THIEU      mã OBS không có trong kho, hoặc không còn `current`                      (V16)
  OBS-GOM        >2 mã OBS trong một dòng có số: tách mỗi mắt xích một mã                   (V32)
  OBS-LECH       số trong câu dẫn không có trong statement của OBS được dẫn               (V24, V27)
  SO-KHONG-NGUON số có đơn vị mà dòng không có mã OBS / M / E / vault / DATA               (V16, V23)
  SOSANH-NHAT    so sánh nhất hoặc chi tiết minh họa (trang, dấu mộc…) không có nguồn       (V23)
  NHAN-MANH      câu tóm khẳng định mạnh (xác nhận/chứng minh) dựa trên nguồn: kiểm nguyên văn  (V22)
  NHAN-ROI       câu tóm (Key Insight, Causal Exit, câu chốt) không trỏ mã M/E/H/OBS và không
                 mang nhãn suy luận                                                       (V12, V22)
  TU-TINH        phép tính kênh tự làm (mỗi ngày, chia ra, tương đương) không ghi "tự tính" (V16)
  HC-THIEU       thiếu `00_hien_chuong.md`; HC-TIEUDE / HC-CAUHOI: tiêu đề hoặc câu hỏi trung tâm
                 không xuất hiện nguyên văn; HC-TUKHOA: từ khóa đã loại xuất hiện           (V15)
  GT-THIEU       thiếu `00_bang_gia_thuyet.md`; GT-SO: số giả thuyết < mức N2;
                 GT-BAC: bằng chứng ngược (−) với giả thuyết dẫn đầu không xuất hiện ở outline (V26)
  SO-CHANDO      chân đỡ (sổ dữ kiện, mục cuối) vắng ở brief/outline mà không có lý do       (V11)
  N5-DONGTIEN    lăng kính dòng tiền xuất hiện trong khi hiến chương không bật               (Q10)
  N3-CHEDO       chế độ kết trong brief khác N3 của hiến chương
  PLAN-O         prompt/câu trích xuất Pha 2 không ghi mã ô [H?↔H?] hoặc GAP                (V08)
"""
import os, re, sys, glob

# ---------- tiện ích ----------
NUM = re.compile(r'(?<![\w.,])(\d{1,3}(?:[.,]\d{3})+|\d+(?:[.,]\d+)?)(?![\w])')
UNIT = r'(xe|tỷ|triệu|nghìn|ngàn|USD|EUR|DKK|VND|đồng|giấy phép|tài xế|trang|km|tấn|ha|cửa hàng|chiếc|ô tô)'
NUM_UNIT = re.compile(r'(\d{1,3}(?:[.,]\d{3})+|\d+(?:[.,]\d+)?)\s*' + UNIT, re.I)
REF = re.compile(r'OBS-[0-9a-f]{6,16}|\b[ME]\d{2,3}\b|\bH\d\b|\bDATA-\d{2}\b|GAP-[A-Z0-9-]+|research_vault/|vault/|R0\d_|\bR0\d\b|§|punkt|Punkt|20-F|424B3|F-1|RDW|KvK|SEC', re.I)
OBS = re.compile(r'OBS-([0-9a-f]{4,16})')
SUYLUAN = re.compile(r'suy luận|giả thuyết|market_analysis|opinion_commentary|chúng tôi cho rằng|cách đọc của tập|minh họa', re.I)
SOSANH = re.compile(r'lớn nhất|nhỏ nhất|đầu tiên|duy nhất|khổng lồ|chưa từng có|hàng ngàn|hàng nghìn|hàng chục nghìn|dày \d+ trang|trang \d+|dấu mộc|in đậm|bờ biển|hoàng hôn|rạng đông', re.I)
TUTINH = re.compile(r'mỗi ngày|/ngày|một ngày|chia ra|tương đương|quy đổi|nhân với|gấp \d', re.I)
TOM = re.compile(r'\*\*(Key Insight|Cú chuyển nhân quả|Causal Exit|Câu chốt|Golden Line|Lập trường)', re.I)
SKIP_LINE = re.compile(r'wpm|từ/phút|từ\)|Floor|Ceiling|Target|ngân sách|Tỷ Trọng|%\s*\||\|\s*\d+,\d+%|CH\d\d|Cấp độ|phút phát sóng|~\d+m', re.I)

def lines_of(path):
    with open(path, encoding='utf-8') as f:
        return f.read().split('\n')

def norm_nums(text):
    out = set()
    for m in NUM.finditer(text):
        t = m.group(1).replace('.', '').replace(',', '.')
        try:
            v = float(t); out.add(round(v, 2))
        except ValueError:
            pass
    return out

class Kiem:
    def __init__(self, ep, use_kb=True):
        self.ep = ep; self.err = []; self.kb = None
        if use_kb:
            try:
                sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'kg_common'))
                import kb_write; self.kb = kb_write.graph()
            except Exception as e:
                print(f"[CẢNH BÁO] không nối được kho ({e}); bỏ kiểm OBS", file=sys.stderr)
        self.obs_cache = {}

    def e(self, code, path, ln, msg):
        self.err.append(f"[{code}] {os.path.relpath(path, self.ep)}:{ln} — {msg}")

    def obs(self, oid):
        if oid in self.obs_cache: return self.obs_cache[oid]
        r = None
        if self.kb:
            q = self.kb.ro_query("MATCH (o:Observation) WHERE o.obs_id STARTS WITH $i RETURN o.status, o.statement LIMIT 2", {"i": oid}).result_set
            r = q[0] if len(q) == 1 else (None if not q else ('NHIEU', ''))
        self.obs_cache[oid] = r; return r

    # ----- kiểm chung cho mọi file nội dung -----
    def kiem_noidung(self, path, pha):
        if not os.path.exists(path): return
        L = lines_of(path)
        for i, line in enumerate(L, 1):
            if line.startswith('<!--') or line.startswith('|---') or SKIP_LINE.search(line) and not OBS.search(line):
                pass
            # nhiều OBS trong một dòng làm mờ quy trách số → nguồn (V32)
            if len(OBS.findall(line)) > 2 and NUM_UNIT.search(line):
                self.e('OBS-GOM', path, i, f"{len(OBS.findall(line))} mã OBS trong một dòng có số: tách mỗi mắt xích một mã, hoặc ghi rõ số nào thuộc mã nào")
            # OBS tồn tại + khớp số
            for m in OBS.finditer(line):
                oid = 'OBS-' + m.group(1)
                if len(m.group(1)) < 16:
                    self.e('OBS-THIEU', path, i, f"{oid} bị cắt cụt"); continue
                r = self.obs(oid)
                if self.kb:
                    if r is None: self.e('OBS-THIEU', path, i, f"{oid} không có trong kho")
                    elif r[0] == 'NHIEU': pass
                    elif r[0] != 'current': self.e('OBS-THIEU', path, i, f"{oid} status={r[0]}")
                    else:
                        pre = line[:m.start()]
                        cut = max(pre.rfind('OBS-'), pre.rfind(';'), pre.rfind('. '), pre.rfind(' ('), pre.rfind('→'), pre.rfind('|'))
                        seg = pre[cut+1:] if cut >= 0 else pre
                        if seg.strip().startswith('OBS') or len(seg.strip()) < 4:  # mã nối tiếp mã: dùng mệnh đề trước đó
                            prev = pre[:cut]; c2 = max(prev.rfind(';'), prev.rfind('. '), prev.rfind(' ('), prev.rfind('|')); seg = prev[c2+1:]
                        nums = {n for n in norm_nums(seg) if n >= 10 and not (1900 <= n <= 2100)}
                        st = {n for n in norm_nums(r[1] or '') if n >= 10 and not (1900 <= n <= 2100)}
                        def khop(a, b):
                            for x in a:
                                for y in b:
                                    for k in (1, 1e3, 1e6, 1e9):
                                        if y and abs(x*k - y) / y < 0.002 or x and abs(y*k - x) / x < 0.002: return True
                            return False
                        if nums and st and not khop(nums, st):
                            self.e('OBS-LECH', path, i, f"số {sorted(nums)[:3]} trước {oid} không có trong statement ({sorted(st)[:3]})")
            if line.startswith('|---') or line.startswith('<!--') or line.lstrip().startswith('>') or 'BẮT BUỘC' in line or 'Checklist' in line: continue
            if pha not in ('3', '4', '7', '8'): continue
            has_ref = bool(REF.search(line))
            # số có đơn vị mà không nguồn
            if NUM_UNIT.search(line) and not has_ref and not SKIP_LINE.search(line):
                self.e('SO-KHONG-NGUON', path, i, f"số có đơn vị, không mã OBS/M/E/vault: «{line.strip()[:90]}»")
            # so sánh nhất / chi tiết minh họa
            if SOSANH.search(line) and not has_ref and not SUYLUAN.search(line):
                self.e('SOSANH-NHAT', path, i, f"«{SOSANH.search(line).group(0)}» không có nguồn hay nhãn minh họa")
            # câu tóm không trỏ mã, không nhãn
            if TOM.search(line) and not has_ref and not SUYLUAN.search(line):
                self.e('NHAN-ROI', path, i, "câu tóm không trỏ mã M/E/H/OBS và không mang nhãn suy luận")
            # câu tóm khẳng định mạnh dựa trên nguồn: kiểm nguyên văn
            if TOM.search(line) and re.search(r'chính thức xác nhận|xác nhận|chứng minh|khẳng định|cô độc|tử huyệt', line, re.I) and not SUYLUAN.search(line):
                self.e('NHAN-MANH', path, i, "câu tóm khẳng định mạnh («xác nhận/chứng minh») — kiểm nguyên văn nguồn, hoặc hạ xuống nhãn suy luận")
            # tự tính
            if TUTINH.search(line) and NUM.search(line) and 'tự tính' not in line.lower() and not SUYLUAN.search(line) and 'tỷ giá' not in line.lower():
                self.e('TU-TINH', path, i, f"phép tính kênh tự làm chưa ghi «tự tính»: «{line.strip()[:80]}»")

    # ----- hiến chương -----
    def hien_chuong(self):
        p = os.path.join(self.ep, '00_hien_chuong.md')
        if not os.path.exists(p):
            self.e('HC-THIEU', p, 0, "chưa có hiến chương tập (Pha 0)"); return {}
        t = open(p, encoding='utf-8').read()
        def grab(label):
            m = re.search(r'\*\*' + label + r'[^*]*\*\*\s*(.+)', t);
            return m.group(1).strip().strip('[]') if m else ''
        hc = {'tieude': grab('Tiêu đề chính'), 'cauhoi': grab('Câu hỏi trung tâm')}
        hc['tukhoa'] = [c.split('|')[1].strip().strip('[]') for c in re.findall(r'\n\|([^\n]+)', t.split('## 3.')[1].split('## 4.')[0])][1:] if '## 3.' in t else []
        hc['tukhoa'] = [t.strip().strip('"') for k in hc['tukhoa'] if k and not k.startswith('-') and 'ví dụ' not in k.lower() for t in re.split(r',| làm | hay ', k) if len(t.strip()) > 2 and t.strip().lower() not in ('xương sống', 'khung đề')]
        hc['dongtien'] = 'dòng tiền' in (t.split('## 4.')[1].split('## 5.')[0].lower() if '## 4.' in t else '') and 'không bật' not in t.lower()
        m = re.search(r'N2 Số lời giải hợp lý \| ([^|]+)\|', t); hc['n2'] = (m.group(1).strip() if m else '')
        m = re.search(r'## 5\..*?\n- (A|B)\b', t, re.S); hc['n3'] = m.group(1) if m else ''
        return hc

    def kiem_hc(self, hc, files):
        if not hc: return
        for f in files:
            if not os.path.exists(f) or os.path.basename(f).startswith(('01b_', '01c_')): continue  # file do kbaudit sinh, không áp hiến chương
            t = open(f, encoding='utf-8').read()
            so = os.path.basename(f).startswith('00_')  # sổ xuyên tập: chỉ kiểm từ khóa và lăng kính
            if not so and hc['tieude'] and not hc['tieude'].startswith('[') and hc['tieude'].upper() not in t.upper():
                self.e('HC-TIEUDE', f, 0, f"tiêu đề «{hc['tieude'][:50]}» không xuất hiện nguyên văn")
            if not so and hc['cauhoi'] and not hc['cauhoi'].startswith('[') and hc['cauhoi'][:60].lower() not in t.lower():
                self.e('HC-CAUHOI', f, 0, "câu hỏi trung tâm không xuất hiện nguyên văn")
            for k in hc['tukhoa']:
                for i, line in enumerate(t.split('\n'), 1):
                    if k.lower() in line.lower() and 'đã loại' not in line.lower() and 'không' not in line.lower()[:40]:
                        self.e('HC-TUKHOA', f, i, f"từ khóa đã loại «{k}» xuất hiện")
            if not hc['dongtien'] and re.search(r'Forensic Cash|dòng tiền tự do|FCF|điểm hòa vốn|bảng cân đối', t, re.I):
                i = next(i for i, l in enumerate(t.split('\n'), 1) if re.search(r'Forensic Cash|dòng tiền tự do|FCF|điểm hòa vốn|bảng cân đối', l, re.I))
                self.e('N5-DONGTIEN', f, i, "khung dòng tiền xuất hiện nhưng hiến chương không bật lăng kính này")

    # ----- bảng giả thuyết -----
    def gia_thuyet(self, hc, outline):
        p = os.path.join(self.ep, '00_bang_gia_thuyet.md')
        if not os.path.exists(p):
            self.e('GT-THIEU', p, 0, "chưa có bảng giả thuyết (Pha 1)"); return
        t = open(p, encoding='utf-8').read()
        hs = re.findall(r'^\| (H\d) \| (.+?) \|', t, re.M)
        hs = [h for h in hs if h[1].strip()]
        minh = 3 if (hc.get('n2', '') or '').startswith('1') or not hs else 3
        if len(hs) < minh: self.e('GT-SO', p, 0, f"chỉ có {len(hs)} giả thuyết có nội dung, cần ≥ {minh}")
        m = re.search(r'Giả thuyết còn đứng:\s*(H\d)', t); lead = m.group(1) if m else None
        if lead and os.path.exists(outline):
            hdr = re.search(r'^\| Mã E \|.*$', t, re.M)
            if hdr:
                cols = [c.strip() for c in hdr.group(0).strip('|').split('|')]
                if lead in cols:
                    ci = cols.index(lead); ot = open(outline, encoding='utf-8').read()
                    for row in re.findall(r'^\| (E\d{2,3}) \|.*$', t, re.M):
                        cells = [c.strip() for c in re.search(r'^\| ' + row + r' \|.*$', t, re.M).group(0).strip('|').split('|')]
                        if len(cells) > ci and cells[ci] in ('−', '-') and row not in ot:
                            self.e('GT-BAC', outline, 0, f"bằng chứng {row} ngược với {lead} không xuất hiện trong outline")

    # ----- sổ dữ kiện: chân đỡ -----
    def chan_do(self, files):
        p = os.path.join(self.ep, '00_so_du_kien.md')
        if not os.path.exists(p): return
        t = open(p, encoding='utf-8').read()
        sec = t.split('## Chân đỡ')[1] if '## Chân đỡ' in t else ''
        for m in re.finditer(r'^\| (M\d{2,3}) \|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|', sec, re.M):
            code, _, b3, b4, lydo = m.groups()
            for f in files:
                if os.path.exists(f) and code not in open(f, encoding='utf-8').read() and not lydo.strip():
                    self.e('SO-CHANDO', f, 0, f"chân đỡ {code} vắng, không có lý do bỏ")

    # ----- Pha 2 plan -----
    def plan(self, hc):
        p = os.path.join(self.ep, '02_research_plan.md')
        if not os.path.exists(p): return
        for i, line in enumerate(lines_of(p), 1):
            if re.match(r'\s*(-|\d+\.)\s*\*\*?(Prompt|Query|Q\d|P\d)', line) and not re.search(r'\[H\d\s*[↔<>-]+\s*H\d|GAP-', line):
                self.e('PLAN-O', p, i, "prompt/câu trích xuất không ghi mã ô ma trận [H?↔H?] hoặc GAP")

    def chedo(self, hc):
        p = os.path.join(self.ep, '03_brief.md')
        if not hc.get('n3') or not os.path.exists(p): return
        t = open(p, encoding='utf-8').read()
        m = re.search(r'CHẾ ĐỘ (A|B)|Chế độ kết[^A-Z]{0,40}\b(A|B)\b', t)
        got = (m.group(1) or m.group(2)) if m else None
        if got and got != hc['n3']: self.e('N3-CHEDO', p, 0, f"brief chọn chế độ {got}, hiến chương N3 = {hc['n3']}")

def main():
    a = sys.argv[1:]
    if not a: print(__doc__); return 2
    ep = a[0] if os.path.isdir(a[0]) else os.path.join('episodes', a[0])
    pha = a[a.index('--pha') + 1] if '--pha' in a else 'all'
    k = Kiem(ep, use_kb='--khong-kho' not in a)
    F = {'1': ['01_global_vision_synthesis.md', '01b_knowledge_audit.md'], '2': ['02_research_plan.md', '02_research_map.md', '02_research_synthesis.md'],
         '3': ['03_brief.md'], '4': ['07_outline.md', '08_chapter_briefs.md', '04_hook_pack.md'], '7': sorted(os.path.basename(x) for x in glob.glob(os.path.join(ep, 'chapter_*.md'))), '8': ['voiceover.md']}
    phas = list(F) if pha == 'all' else [pha]
    files = [os.path.join(ep, f) for p in phas for f in F[p]]
    hc = k.hien_chuong()
    for p_ in phas:
        for f in F[p_]: k.kiem_noidung(os.path.join(ep, f), p_)
    k.kiem_hc(hc, files + [os.path.join(ep, '00_bang_gia_thuyet.md'), os.path.join(ep, '00_so_du_kien.md')])  # hai sổ xuyên tập luôn chịu kiểm hiến chương
    if pha in ('all', '2'): k.plan(hc)
    if pha in ('all', '3'): k.chedo(hc)
    if pha in ('all', '3', '4'): k.chan_do([os.path.join(ep, '03_brief.md'), os.path.join(ep, '07_outline.md')])
    if pha in ('all', '4'): k.gia_thuyet(hc, os.path.join(ep, '07_outline.md'))
    for x in k.err: print(x)
    print(f"KẾT QUẢ: {'ĐẠT' if not k.err else f'{len(k.err)} LỖI'} ({ep}, pha {pha})")
    return 1 if k.err else 0

if __name__ == '__main__':
    sys.exit(main())
