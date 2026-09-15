#!/usr/bin/env python3
"""
NotebookLM Direct RPC Deep Research & Batch Extraction Pipeline for Dong_Chay.
Enforces `--mode deep` (Comprehensive Deep Research) and outputs structured data to research_vault.
"""

import os
import sys
import json
import time
import argparse
import subprocess
from pathlib import Path

# Workspace configurations
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
NOTEBOOKLM_HOME = WORKSPACE_ROOT / ".notebooklm_home"
CLI_PATH = WORKSPACE_ROOT / ".venv" / "bin" / "notebooklm"

os.environ["NOTEBOOKLM_HOME"] = str(NOTEBOOKLM_HOME)
os.environ["PYTHONUNBUFFERED"] = "1"


def run_cmd(args, capture=True):
    """Execute notebooklm CLI command with configured environment."""
    env = os.environ.copy()
    env["NOTEBOOKLM_HOME"] = str(NOTEBOOKLM_HOME)
    cmd = [str(CLI_PATH)] + args
    res = subprocess.run(cmd, env=env, capture_output=capture, text=True)
    if res.returncode != 0:
        err_msg = res.stderr or res.stdout
        raise RuntimeError(f"CLI error (code {res.returncode}): {err_msg}")
    return res.stdout


def check_auth():
    """Verify persistent session authentication."""
    try:
        out = run_cmd(["auth", "check", "--json"])
        data = json.loads(out)
        return data.get("checks", {}).get("storage_exists", False)
    except Exception:
        return False


def get_or_create_notebook(episode_dir: Path, topic_title: str) -> str:
    """Read existing notebook ID or create a new Master Notebook."""
    id_file = episode_dir / ".notebook_id"
    if id_file.exists():
        nb_id = id_file.read_text().strip()
        if nb_id:
            print(f"📖 Sử dụng Master Notebook đã lưu: {nb_id}")
            return nb_id

    print(f"🆕 Đang tạo Master Notebook mới: '{topic_title}'...")
    out = run_cmd(["create", topic_title, "--json"])
    data = json.loads(out)
    nb_id = data["notebook"]["id"]
    
    # Persist ID and URL
    id_file.write_text(nb_id)
    url_file = episode_dir / ".notebook_url"
    url_file.write_text(f"https://notebooklm.google.com/notebook/{nb_id}")
    print(f"✓ Đã tạo và lưu Master Notebook ID: {nb_id}")
    return nb_id


def execute_deep_research(nb_id: str, prompt_text: str, timeout: int = 1800):
    """Run mandatory Deep Research (--mode deep) and import all sources."""
    print("\n🔍 Đang kích hoạt DEEP RESEARCH (Chế độ nghiên cứu sâu bắt buộc: --mode deep)...")
    print("⏳ Quá trình này quét đa tầng qua hàng chục nguồn học thuật & báo cáo chính phủ (khoảng 2-10 phút)...")
    
    temp_prompt = WORKSPACE_ROOT / "scratch" / "deep_research_prompt.txt"
    temp_prompt.parent.mkdir(parents=True, exist_ok=True)
    temp_prompt.write_text(prompt_text, encoding="utf-8")

    start_time = time.time()
    out = run_cmd([
        "source", "add-research",
        "--prompt-file", str(temp_prompt),
        "-n", nb_id,
        "--mode", "deep",          # MANDATORY DEEP RESEARCH
        "--import-all",
        "--timeout", str(timeout),
        "--json"
    ])
    elapsed = time.time() - start_time
    
    try:
        data = json.loads(out)
        imported_count = data.get("imported", 0)
        print(f"✓ Hoàn tất Deep Research trong {elapsed:.1f}s. Đã tự động nạp {imported_count} nguồn tài liệu uy tín.")
    except Exception:
        print(f"✓ Hoàn tất Deep Research trong {elapsed:.1f}s.")
    return out


def batch_extract_to_vault(nb_id: str, queries: list, vault_dir: Path):
    """Execute sequential RAG extractions with citations and save to research_vault."""
    vault_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n📦 BẮT ĐẦU BATCH EXTRACTION ({len(queries)} câu hỏi) RA THƯ MỤC: {vault_dir.name}/")

    for idx, item in enumerate(queries, 1):
        filename = item["filename"]
        title = item["title"]
        question = item["question"]

        target_file = vault_dir / filename
        print(f"\n[{idx}/{len(queries)}] Đang trích xuất: {title} -> {filename}...")

        temp_q = WORKSPACE_ROOT / "scratch" / f"q_{idx}.txt"
        temp_q.write_text(question, encoding="utf-8")

        try:
            out = run_cmd([
                "ask",
                "--prompt-file", str(temp_q),
                "-n", nb_id,
                "--save-as-note",
                "-t", title,
                "--json"
            ])
            data = json.loads(out)
            answer = data.get("answer", "")
            references = data.get("references", [])

            # Format markdown file with references
            md_content = f"# {title}\n\n"
            md_content += f"> **Câu hỏi trích xuất:** {question}\n\n"
            md_content += f"## Nội dung Phân tích & Dữ liệu Thực chứng\n\n{answer}\n\n"
            
            if references:
                md_content += "## Mỏ neo Trích dẫn Nguồn (Citations / Footnotes)\n\n"
                for ref in references:
                    cit_no = ref.get("citation_number")
                    cited_text = ref.get("cited_text", "").strip()
                    md_content += f"- **[{cit_no}]**: *\"{cited_text}\"*\n"

            target_file.write_text(md_content, encoding="utf-8")
            print(f"✓ Đã lưu thành công {len(md_content.splitlines())} dòng vào {filename}")

        except Exception as e:
            print(f"✗ Lỗi khi trích xuất câu {idx}: {e}")


def main():
    parser = argparse.ArgumentParser(description="NotebookLM Deep Research Pipeline")
    parser.add_argument("--slug", required=True, help="Episode slug under episodes/")
    parser.add_argument("--title", required=True, help="Notebook title")
    parser.add_argument("--plan-file", help="Path to 02_research_plan.md or JSON query file")
    args = parser.parse_args()

    episode_dir = WORKSPACE_ROOT / "episodes" / args.slug
    episode_dir.mkdir(parents=True, exist_ok=True)
    vault_dir = episode_dir / "research_vault"

    if not check_auth():
        print("❌ Lỗi: Chưa xác thực NotebookLM. Vui lòng chạy lệnh 'notebooklm login' trước!")
        sys.exit(1)

    nb_id = get_or_create_notebook(episode_dir, args.title)
    print(f"🚀 Master Notebook sẵn sàng: {nb_id}")


if __name__ == "__main__":
    main()
