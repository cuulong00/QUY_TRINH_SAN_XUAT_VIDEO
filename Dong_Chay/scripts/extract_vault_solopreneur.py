import subprocess
import json
import os
import sys
from pathlib import Path

env = os.environ.copy()
env["NOTEBOOKLM_HOME"] = "/Users/pro16/Documents/VideoProject/Dong_Chay/.notebooklm_home"
cli = "/Users/pro16/Documents/VideoProject/Dong_Chay/.venv/bin/notebooklm"
notebook_id = "8ba8082d-ddba-4714-a051-2319bdcf83a8"

prompts_dir = Path("episodes/cong-ty-1-nguoi-ai-viet-nam/prompts_extraction")
vault_dir = Path("episodes/cong-ty-1-nguoi-ai-viet-nam/research_vault")
vault_dir.mkdir(parents=True, exist_ok=True)

files = sorted(prompts_dir.glob("*.txt"))
print(f"Found {len(files)} prompts to extract.", flush=True)

for pfile in files:
    out_file = vault_dir / (pfile.stem + ".md")
    if out_file.exists() and out_file.stat().st_size > 1000:
        print(f"[SKIP] Already exists: {out_file.name}", flush=True)
        continue
    
    print(f"[EXTRACTING] {pfile.name} ...", flush=True)
    cmd = [
        cli, "ask",
        "--prompt-file", str(pfile),
        "-n", notebook_id,
        "--json"
    ]
    try:
        res = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=120)
        if res.returncode == 0:
            data = json.loads(res.stdout)
            answer = data.get("answer", "")
            citations = data.get("citations", [])
            
            doc = f"# {pfile.stem.upper()}\n\n{answer}\n\n## Trích dẫn nguồn (Citations)\n\n"
            for c in citations:
                num = c.get("citation_number")
                sid = c.get("source_id")
                txt = c.get("cited_text", "")[:300].replace("\n", " ")
                doc += f"- [{num}] ({sid}): {txt}...\n"
                
            out_file.write_text(doc, encoding="utf-8")
            print(f"[SUCCESS] Saved {out_file.name} ({len(answer)} chars, {len(citations)} citations)", flush=True)
        else:
            print(f"[FAIL] {pfile.name}: {res.stderr[:250]}", flush=True)
    except Exception as e:
        print(f"[ERROR] {pfile.name}: {e}", flush=True)

print("ALL DONE!", flush=True)
