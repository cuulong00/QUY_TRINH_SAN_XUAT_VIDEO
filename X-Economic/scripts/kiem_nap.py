#!/usr/bin/env python3
"""Đo xem agent Antigravity THỰC SỰ nhận được gì trong ngữ cảnh (03/10/2026).

Dùng:
  scripts/kiem_nap.py <conversationId|đường dẫn .db>            # khối rule được chèn + file agent đã mở
  scripts/kiem_nap.py <id> --tu <bước> --den <bước>              # chỉ xem file mở trong khoảng bước
  scripts/kiem_nap.py --gan-nhat [N]                             # N hội thoại mới nhất (mặc định 5), chỉ phần rule

Đọc ~/.gemini/antigravity/conversations/<id>.db (chỉ đọc, mở ở chế độ ro):
  - bảng gen_metadata: khối <user_rules> mà Antigravity chèn (file nào, bao nhiêu ký tự, bị <truncated>, bị loại vì vượt ngân sách)
  - bảng steps: các lệnh view_file / write_to_file / replace_file_content và đường dẫn.
Không tin lời agent tự khai "đã đọc"; dùng script này làm bằng chứng.
"""
import glob, os, re, sqlite3, sys
from collections import Counter

BASE = os.path.expanduser('~/.gemini/antigravity/conversations')
ROOT = '/Users/pro16/Documents/VideoProject/'
TOOLS = (b'view_file', b'write_to_file', b'replace_file_content', b'multi_replace_file_content', b'run_command', b'grep_search')
PATH = re.compile(rb'/Users/pro16/Documents/VideoProject/([A-Za-z0-9_./\-]+\.(?:md|txt|json|py|csv))')


def db_of(arg):
    if arg.endswith('.db') and os.path.exists(arg):
        return arg
    hits = glob.glob(os.path.join(BASE, arg + '*.db'))
    if not hits:
        sys.exit(f'không thấy hội thoại {arg}')
    return hits[0]


def connect(path):
    return sqlite3.connect(f'file:{path}?mode=ro', uri=True)


def rules(con):
    for (d,) in con.execute('select data from gen_metadata order by idx desc'):
        if d and b'<user_rules' in d:
            s = d.decode('utf-8', 'ignore')
            i = s.find('<user_rules'); j = s.find('</user_rules>', i)
            return s[i:j]
    return None


def report_rules(block):
    if block is None:
        print('  (không thấy khối <user_rules>)'); return
    print(f'  tổng khối rule: {len(block):,} ký tự')
    parts = re.split(r'(<RULE\[[^\]]+\]>)', block)
    for k in range(1, len(parts), 2):
        name = parts[k][6:-2].replace(ROOT, '')
        body = parts[k + 1]
        cut = re.search(r'<truncated (\d+) bytes>', body)
        print(f'  - {name}: {len(body):,} ký tự' + (f'  ⚠️ BỊ CẮT, mất {int(cut.group(1)):,} bytes' if cut else ''))
    m = re.search(r'excluded from inline injection[^\n]*\n((?:- [^\n]+\n?)+)', block)
    if m:
        for line in m.group(1).strip().splitlines():
            print(f'  ⛔ BỊ LOẠI (vượt ngân sách): {line[2:].replace(ROOT, "")}')


def report_steps(con, lo, hi):
    rows = con.execute('select idx, step_payload from steps where step_type=15 and idx between ? and ? order by idx', (lo, hi)).fetchall()
    seen = Counter(); first = {}
    for idx, p in rows:
        if not p:
            continue
        tool = next((t.decode() for t in TOOLS if t in p), None)
        if tool not in ('view_file', 'write_to_file', 'replace_file_content', 'multi_replace_file_content'):
            continue
        for f in set(PATH.findall(p)):
            key = (tool, f.decode())
            seen[key] += 1; first.setdefault(key, idx)
    for kind in ('view_file', 'write_to_file', 'replace_file_content', 'multi_replace_file_content'):
        items = sorted((first[k], k[1], seen[k]) for k in seen if k[0] == kind)
        if items:
            print(f'  [{kind}] {len(items)} file')
            for i, f, n in items:
                print(f'     bước {i:>5}  ×{n}  {f}')


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); return
    if a[0] == '--gan-nhat':
        n = int(a[1]) if len(a) > 1 else 5
        for f in sorted(glob.glob(os.path.join(BASE, '*.db')), key=os.path.getmtime)[-n:]:
            print(os.path.basename(f)[:8]); report_rules(rules(connect(f)))
        return
    path = db_of(a[0]); con = connect(path)
    lo = int(a[a.index('--tu') + 1]) if '--tu' in a else 0
    hi = int(a[a.index('--den') + 1]) if '--den' in a else 10 ** 9
    print(f'Hội thoại {os.path.basename(path)}')
    print('1. Rule được chèn tự động:'); report_rules(rules(con))
    print('2. File agent đã thao tác:'); report_steps(con, lo, hi)


if __name__ == '__main__':
    main()
