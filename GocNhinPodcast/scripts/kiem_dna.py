#!/usr/bin/env python3
"""Kiểm DNA (WO-04/WO-05). Dùng: python3 scripts/kiem_dna.py [--persona] [--root <thư mục>]
--persona: với mỗi workflow có HARD GATE, so tập persona ở hard gate với persona khai báo ở Pre-flight và với bảng pha trong rules/content-os-pipeline.md. Thoát 1 nếu lệch."""
import re,sys,os,glob
root=sys.argv[sys.argv.index('--root')+1] if '--root' in sys.argv else '.'
def slug(name):
    n=name.strip().strip('`').lower().replace('the ','').replace('(','').replace(')','')
    n=re.sub(r'[^a-z_ ]','',n).strip().replace(' ','_')
    return n if n.startswith('the_') else 'the_'+n
def personas_in(text):
    return set(re.findall(r'personas/(the_[a-z_]+)\.md',text))
def preflight_personas(text):
    m=re.search(r'Chuyên Gia \(Persona DNA\) Kích Hoạt:\*\*\s*(.+)',text)
    if not m: return None
    line=m.group(1)
    out=set(re.findall(r'`(the_[a-z_]+)`',line))
    for part in re.split(r'\+|,',re.sub(r'\(.*?\)','',line)):
        part=part.strip()
        if part.lower().startswith('the ') : out.add(slug(part))
    return out
pipe=open(os.path.join(root,'.agents/rules/content-os-pipeline.md')).read()
rows={}
for line in pipe.split('\n'):
    if line.startswith('| ') and '`/' in line:
        cells=[c.strip() for c in line.split('|')]
        wf=re.findall(r'`/([a-z_]+)`',line)
        if wf and len(cells)>4: rows.setdefault(wf[0],set(re.findall(r'`(the_[a-z_]+)`',cells[3])))
bad=0
for wf in sorted(glob.glob(os.path.join(root,'.agents/workflows/*.md'))):
    t=open(wf).read(); name=os.path.basename(wf)[:-3]
    if 'HARD GATE' not in t: continue
    i=t.find('HARD GATE'); j=t.find('\n---',i)
    sec=t[i:j if j>0 else None]
    if 'personas/' not in sec and 'skills/' not in sec:
        print('BỎ QUA '+name+' (hard gate không phải cổng persona)'); continue
    gate=personas_in(sec)
    pre=preflight_personas(t)
    row=rows.get(name)
    msgs=[]
    if pre is not None and gate!=pre: msgs.append(f"hard gate {sorted(gate)} ≠ pre-flight {sorted(pre)}")
    if row is not None and row and gate!=row: msgs.append(f"hard gate {sorted(gate)} ≠ bảng pha {sorted(row)}")
    print(("LỆCH " if msgs else "KHỚP ")+name+("; ".join([""]+msgs)))
    bad+=bool(msgs)
sys.exit(1 if bad else 0)
