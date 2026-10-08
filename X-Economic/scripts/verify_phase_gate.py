#!/usr/bin/env python3
"""
Phase Gatekeeper Verification Script for X-Economic Production Pipeline.
Enforces hard barriers between phases to prevent LLM agents from skipping
NotebookLM Deep Research, faking vaults, or bypassing data verification.

Usage:
    python3 scripts/verify_phase_gate.py --phase 2 --episode <slug>
    python3 scripts/verify_phase_gate.py --phase 3 --episode <slug>
"""

import os
import sys
import json
import argparse
import subprocess
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
NOTEBOOKLM_HOME = WORKSPACE_ROOT / ".notebooklm_home"
CLI_PATH = WORKSPACE_ROOT / ".venv" / "bin" / "notebooklm"

def run_notebooklm_cmd(args):
    """Run notebooklm CLI and return parsed JSON or raw output."""
    # First try default active environment
    res = subprocess.run(["notebooklm"] + args, capture_output=True, text=True)
    if res.returncode == 0:
        return res.stdout, None
    # Fallback with explicit env if needed
    env = os.environ.copy()
    if NOTEBOOKLM_HOME.exists():
        env["NOTEBOOKLM_HOME"] = str(NOTEBOOKLM_HOME)
    cmd = [str(CLI_PATH if CLI_PATH.exists() else "notebooklm")] + args
    res = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if res.returncode != 0:
        return None, res.stderr or res.stdout
    return res.stdout, None

def verify_phase_2(slug: str) -> bool:
    print(f"\n==================================================")
    print(f"🛡️  KIỂM TOÁN CỨNG PHA 2 (DEEP RESEARCH PROOF-OF-EXECUTION)")
    print(f"🎬 Episode: {slug}")
    print(f"==================================================")
    
    episode_dir = WORKSPACE_ROOT / "episodes" / slug
    if not episode_dir.exists():
        print(f"❌ [FAIL] Thư mục episode không tồn tại: {episode_dir}")
        return False

    errors = []
    warnings = []

    # 1. Kiểm tra file .notebook_id
    id_file = episode_dir / ".notebook_id"
    if not id_file.exists():
        errors.append("Thiếu tệp .notebook_id (Chưa khởi tạo Master Notebook)")
        nb_id = None
    else:
        nb_id = id_file.read_text().strip()
        if not nb_id:
            errors.append("Tệp .notebook_id rỗng")
            nb_id = None
        else:
            print(f"✓ Master Notebook ID: {nb_id}")

    # 2. Kiểm tra file .notebook_url
    url_file = episode_dir / ".notebook_url"
    if not url_file.exists():
        warnings.append("Thiếu tệp .notebook_url")
    else:
        print(f"✓ Master Notebook URL: {url_file.read_text().strip()}")

    # 3. Kiểm tra số lượng nguồn thực tế trong NotebookLM qua Direct RPC CLI
    if nb_id:
        print(f"⏳ Đang kết nối NotebookLM Direct RPC để kiểm tra số lượng nguồn nạp thực tế...")
        out, err = run_notebooklm_cmd(["source", "list", "-n", nb_id, "--json"])
        if err or not out:
            errors.append(f"Không thể truy vấn danh sách nguồn từ NotebookLM: {err}")
        else:
            try:
                data = json.loads(out)
                sources = data.get("sources", [])
                ready_sources = [s for s in sources if s.get("status") == "ready"]
                print(f"📊 Tổng số nguồn: {len(sources)} | Nguồn khả dụng (ready): {len(ready_sources)}")

                if len(ready_sources) < 10:
                    errors.append(
                        f"Số lượng nguồn 'ready' trong NotebookLM chỉ đạt {len(ready_sources)}/10 nguồn tối thiểu. "
                        f"BẮT BUỘC phải hoàn tất Deep Research (--mode deep --import-all) nạp đủ ≥ 10 nguồn."
                    )
                else:
                    print(f"✓ Đạt chuẩn số lượng nguồn NotebookLM (≥ 10 sources ready)")
            except Exception as e:
                errors.append(f"Lỗi phân tích JSON kết quả sources: {e}")

    # 4. Kiểm tra thư mục research_vault/
    vault_dir = episode_dir / "research_vault"
    if not vault_dir.exists() or not vault_dir.is_dir():
        errors.append("Thư mục research_vault/ không tồn tại hoặc chưa được tạo.")
    else:
        vault_files = list(vault_dir.glob("*.md"))
        print(f"📁 Số lượng hồ sơ bóc tách trong research_vault/: {len(vault_files)}")
        if len(vault_files) < 5:
            errors.append(
                f"Số lượng hồ sơ trong research_vault/ quá ít ({len(vault_files)} files). "
                f"BẮT BUỘC tối thiểu ≥ 5 file bóc tách chuyên sâu từ NotebookLM."
            )
        else:
            # Kiểm tra kích thước và nội dung hồ sơ
            small_files = [f.name for f in vault_files if f.stat().st_size < 500]
            if small_files:
                errors.append(f"Phát hiện file trong research_vault/ có kích thước quá nhỏ (<500B): {small_files}")
            else:
                print(f"✓ Các file trong research_vault/ đều có dữ liệu thực chứng đầy đủ.")

    # 5. Kiểm tra 02_research_map.md
    map_file = episode_dir / "02_research_map.md"
    if not map_file.exists():
        errors.append("Thiếu tệp 02_research_map.md")
    else:
        size = map_file.stat().st_size
        if size < 2000:
            errors.append(f"Tệp 02_research_map.md quá sơ sài ({size} bytes < 2000 bytes)")
        else:
            content = map_file.read_text(encoding="utf-8", errors="ignore")
            if "counter-thesis" not in content.lower() and "phản biện" not in content.lower():
                errors.append("Tệp 02_research_map.md thiếu phần Counter-Thesis (Phản biện bắt buộc)")
            else:
                print(f"✓ 02_research_map.md đạt chuẩn ({size} bytes, có Counter-Thesis)")

    # 6. Kiểm tra 02_research_synthesis.md
    synth_file = episode_dir / "02_research_synthesis.md"
    if not synth_file.exists():
        errors.append("Thiếu tệp 02_research_synthesis.md")
    else:
        size = synth_file.stat().st_size
        if size < 3000:
            errors.append(f"Tệp 02_research_synthesis.md quá ngắn ({size} bytes < 3000 bytes, tối thiểu 1.000 từ)")
        else:
            print(f"✓ 02_research_synthesis.md đạt chuẩn ({size} bytes)")

    # TỔNG KẾT
    print("\n--------------------------------------------------")
    if warnings:
        print("⚠️ CẢNH BÁO (WARNINGS):")
        for w in warnings:
            print(f"  - {w}")

    if errors:
        print("❌ KẾT QUẢ: KHÔNG VƯỢT QUA KIỂM TOÁN (FAILED GATE 2)!")
        print("CÁC LỖI BẮT BUỘC PHẢI KHẮC PHỤC TRƯỚC KHI CHUYỂN SANG PHA 3 / PHA 4:")
        for idx, err in enumerate(errors, 1):
            print(f"  [{idx}] {err}")
        print("--------------------------------------------------")
        print("🛑 AGENT PHẢI DỪNG LẠI, CHẠY LỆNH NOTEBOOKLM THỰC TẾ VÀ TRÍCH XUẤT ĐẦY ĐỦ!\n")
        return False
    else:
        print("✅ KẾT QUẢ: VƯỢT QUA KIỂM TOÁN PHA 2 (PASSED GATE 2)!")
        print("Đủ điều kiện dữ liệu thực chứng để tiếp tục sang Pha 2.5 (Global Vision) & Pha 3 (Brief).")
        print("--------------------------------------------------\n")
        return True


def main():
    parser = argparse.ArgumentParser(description="Phase Gatekeeper Verification")
    parser.add_argument("--phase", required=True, type=int, help="Phase number to verify (e.g. 2)")
    parser.add_argument("--episode", required=True, help="Episode slug under episodes/")
    args = parser.parse_args()

    if args.phase == 2:
        success = verify_phase_2(args.episode)
    else:
        print(f"Chưa có validator cho phase {args.phase}")
        sys.exit(0)

    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
