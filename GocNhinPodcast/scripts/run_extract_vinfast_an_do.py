#!/usr/bin/env python3
import os
import sys
import json
import time
import subprocess
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
NOTEBOOKLM_HOME = WORKSPACE_ROOT / ".notebooklm_home"
CLI_PATH = WORKSPACE_ROOT / ".venv_notebooklm" / "bin" / "notebooklm"

EPISODE_SLUG = "vinfast-an-do-thay-doi-chien-luoc"
EPISODE_DIR = WORKSPACE_ROOT / "episodes" / EPISODE_SLUG
VAULT_DIR = EPISODE_DIR / "research_vault"
QUERIES_FILE = WORKSPACE_ROOT / "scratch" / "extraction_queries.json"

os.environ["NOTEBOOKLM_HOME"] = str(NOTEBOOKLM_HOME)
os.environ["PYTHONUNBUFFERED"] = "1"

def run_cmd(args):
    env = os.environ.copy()
    env["NOTEBOOKLM_HOME"] = str(NOTEBOOKLM_HOME)
    cmd = [str(CLI_PATH)] + args
    res = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"CLI error (code {res.returncode}): {res.stderr or res.stdout}")
    return res.stdout

def main():
    VAULT_DIR.mkdir(parents=True, exist_ok=True)
    nb_id = (EPISODE_DIR / ".notebook_id").read_text().strip()
    print(f"📖 Master Notebook ID: {nb_id}")
    
    with open(QUERIES_FILE, "r", encoding="utf-8") as f:
        queries = json.load(f)
        
    print(f"\n🚀 BẮT ĐẦU BATCH EXTRACTION ({len(queries)} chuyên đề) RA {VAULT_DIR.name}/")
    
    for idx, item in enumerate(queries, 1):
        filename = item["filename"]
        title = item["title"]
        question = item["question"]
        target_file = VAULT_DIR / filename
        
        print(f"\n[{idx}/{len(queries)}] Đang trích xuất: {title} -> {filename}...")
        
        temp_q = WORKSPACE_ROOT / "scratch" / f"q_{idx}.txt"
        temp_q.write_text(question, encoding="utf-8")
        
        try:
            start_t = time.time()
            out = run_cmd([
                "ask",
                "--prompt-file", str(temp_q),
                "-n", nb_id,
                "--save-as-note",
                "-t", title,
                "--json"
            ])
            elapsed = time.time() - start_t
            data = json.loads(out)
            answer = data.get("answer", "")
            references = data.get("references", [])
            
            md_content = f"# {title}\n\n"
            md_content += f"> **Câu hỏi trích xuất chuyên sâu:** {question}\n\n"
            md_content += f"## Nội dung Phân tích & Dữ liệu Thực chứng\n\n{answer}\n\n"
            
            if references:
                md_content += "## Mỏ neo Trích dẫn Nguồn (Citations / Footnotes)\n\n"
                for ref in references:
                    cit_no = ref.get("citation_number")
                    cited_text = ref.get("cited_text", "").strip()
                    md_content += f"- **[{cit_no}]**: *\"{cited_text}\"*\n"
                    
            target_file.write_text(md_content, encoding="utf-8")
            print(f"✓ Hoàn tất sau {elapsed:.1f}s. Đã lưu {len(md_content.splitlines())} dòng vào {filename}")
            
        except Exception as e:
            print(f"✗ Lỗi khi trích xuất câu {idx}: {e}")
            
    print("\n🎉 Hoàn thành toàn bộ Batch Extraction vào research_vault/!")

if __name__ == "__main__":
    main()
