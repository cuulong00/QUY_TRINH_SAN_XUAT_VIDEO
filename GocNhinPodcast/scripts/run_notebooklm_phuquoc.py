#!/usr/bin/env python3
"""
Automation script for NotebookLM Deep Research on Phu Quoc 2025-2027 Geopolitics.
Uses teng-lin/notebooklm-py RPC client and CLI commands.
"""

import os
import sys
import subprocess
from pathlib import Path

# Set workspace home directory for persistent NotebookLM profile
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
NOTEBOOKLM_HOME = WORKSPACE_ROOT / ".notebooklm_home"
os.environ["NOTEBOOKLM_HOME"] = str(NOTEBOOKLM_HOME)
os.environ["PYTHONUNBUFFERED"] = "1"

NOTEBOOK_TITLE = "Phú Quốc 2025-2027: Địa chính trị & Bứt phá Vĩ mô"

RESEARCH_QUERY = (
    "Phân tích bối cảnh 'Thiên thời' của Đặc khu Phú Quốc giai đoạn 2025-2027: "
    "1. Lực đẩy từ sự kiện APEC 2027 và mô hình 'Đảo sự kiện' biệt lập cho các nguyên thủ quốc gia. "
    "2. Biến số địa chính trị hàng hải: Kênh đào Funan Techo Campuchia và vị thế án ngữ Vịnh Thái Lan của Phú Quốc, Cảng An Thới. "
    "3. Làn sóng soán ngôi: Dữ liệu Condé Nast Traveler (2025), Travel+Leisure (2024), tỷ lệ lấp đầy phòng và tăng trưởng RevPAR so với Bali, Phuket."
)

STRATEGIC_QUESTIONS = [
    (
        "1_APEC_2027_Event_Island.md",
        "Phân tích chi tiết tại sao Phú Quốc được chọn là địa điểm tổ chức Tuần lễ Cấp cao APEC 2027? "
        "Mô hình 'Đảo sự kiện' (Event Island) biệt lập mang lại lợi thế gì về an ninh 3 tầng, kiểm soát không phận, "
        "vùng nước và lễ tân ngoại giao VVIP so với các đô thị đất liền? Ưu tiên số liệu và sự kiện mới nhất 2024-2027."
    ),
    (
        "2_Funan_Techo_Maritime_Geopolitics.md",
        "Đánh giá tác động địa chính trị của Kênh đào Funan Techo (Campuchia) đối với cục diện an ninh hàng hải Vịnh Thái Lan. "
        "Vị thế tiền tiêu của Phú Quốc và cụm cảng An Thới đóng vai trò thế nào trong việc kiểm soát luồng hàng hải, "
        "cân bằng thế trận an ninh và bảo vệ không gian sinh tồn kinh tế biển phía Tây Nam Việt Nam?"
    ),
    (
        "3_Hospitality_Soan_Ngoi_Bali_Phuket.md",
        "Đối chiếu các chỉ số du lịch và khách sạn: Condé Nast Traveler Readers' Choice 2025, Travel+Leisure 2024, "
        "tỷ lệ lấp đầy phòng (Occupancy >90%) và định giá RevPAR ($160-$170 USD) của Phú Quốc so với Phuket và Bali. "
        "Những động lực cấu trúc nào (chính sách miễn visa 30 ngày, hạ tầng nghỉ dưỡng All-in-One) tạo nên cú bứt phá này?"
    ),
]


def check_auth():
    """Verify if NotebookLM storage state exists."""
    storage_file = NOTEBOOKLM_HOME / "profiles" / "default" / "storage_state.json"
    return storage_file.exists()


def run_cli_cmd(args):
    """Run notebooklm CLI command within virtual environment."""
    cli_path = WORKSPACE_ROOT / ".venv_notebooklm" / "bin" / "notebooklm"
    env = os.environ.copy()
    env["NOTEBOOKLM_HOME"] = str(NOTEBOOKLM_HOME)
    cmd = [str(cli_path)] + args
    return subprocess.run(cmd, env=env, capture_output=True, text=True)


def main():
    print("=" * 70)
    print("🚀 NOTEBOOKLM DEEP RESEARCH PIPELINE: PHÚ QUỐC 2025-2027")
    print("=" * 70)

    if not check_auth():
        print("\n⚠️  CHƯA PHÁT HIỆN SESSION AUTHENTICATION!")
        print("Để kết nối trực tiếp đến Google NotebookLM, vui lòng chạy lệnh 1 lần:")
        print(f"  NOTEBOOKLM_HOME={NOTEBOOKLM_HOME} {WORKSPACE_ROOT}/.venv_notebooklm/bin/notebooklm login")
        print("\nHoặc import cookies bằng lệnh:")
        print(f"  NOTEBOOKLM_HOME={NOTEBOOKLM_HOME} {WORKSPACE_ROOT}/.venv_notebooklm/bin/notebooklm auth import-cookies <file.json>")
        print("=" * 70)
        return

    print("✓ Đã xác thực thành công!")
    print(f"• Tạo/Sử dụng Master Notebook: '{NOTEBOOK_TITLE}'")
    res = run_cli_cmd(["create", NOTEBOOK_TITLE, "--json"])
    print(res.stdout or res.stderr)


if __name__ == "__main__":
    main()
