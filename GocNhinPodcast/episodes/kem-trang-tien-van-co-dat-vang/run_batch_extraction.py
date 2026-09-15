import asyncio
import json
import os
import sys
from pathlib import Path
from notebooklm import NotebookLMClient

NOTEBOOK_ID = "e3a67063-85de-410c-af2f-bd7da97b02ae"
STORAGE_PATH = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.notebooklm_home/profiles/default/storage_state.json"
BASE_DIR = Path("/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/kem-trang-tien-van-co-dat-vang")
VAULT_DIR = BASE_DIR / "research_vault"
QUERIES_DIR = BASE_DIR / "queries"

QUERY_MAP = [
    {
        "file": "01_lich_su_co_phan_hoa_2000_dinh_gia_dat_vang.md",
        "title": "Báo Cáo 01: Lịch Sử Cổ Phần Hóa Năm 2000 — Vốn Điều Lệ 3,2 Tỷ & Kẽ Hở Quản Lý Đất Đai 35 Tràng Tiền",
        "query_file": "query_01.txt",
        "code": "VAULT_KTT_01"
    },
    {
        "file": "02_thuong_vu_ma_500_ty_ocean_group_2010.md",
        "title": "Báo Cáo 02: Thương Vụ M&A 500 Tỷ Của Ocean Group (2008–2010) — Khi Kem Là Vỏ Bọc Thâu Tóm Đất Vàng",
        "query_file": "query_02.txt",
        "code": "VAULT_KTT_02"
    },
    {
        "file": "03_dai_an_oceanbank_vung_lay_no_xau_och.md",
        "title": "Báo Cáo 03: Đại Án OceanBank & Vũng Lầy Nợ Xấu OCH — Khoản Tạm Ứng 500 Tỷ Đóng Băng Dự Án",
        "query_file": "query_03.txt",
        "code": "VAULT_KTT_03"
    },
    {
        "file": "04_pvcombank_can_tru_no_trai_phieu_dau_gia.md",
        "title": "Báo Cáo 04: PVcomBank Cấn Trừ Khoản Trái Phiếu 736 Tỷ & Chu Kỳ Đấu Giá Đất Vàng 35 Tràng Tiền",
        "query_file": "query_04.txt",
        "code": "VAULT_KTT_04"
    },
    {
        "file": "05_tat_toan_747_ty_chu_moi_le_xuan_hoc_2026.md",
        "title": "Báo Cáo 05: Tất Toán Nợ 747 Tỷ Tháng 4/2026 & Chủ Mới Lê Xuân Học (Bách Giang DCI) Tiếp Quản",
        "query_file": "query_05.txt",
        "code": "VAULT_KTT_05"
    },
    {
        "file": "06_phan_ly_phap_ly_kem_trang_tien_vs_dat_trang_tien.md",
        "title": "Báo Cáo 06: Bóc Tách Sự Phân Ly Pháp Lý — CTCP Kem Tràng Tiền (Bán Kem) vs CTCP Tràng Tiền (Ôm Đất)",
        "query_file": "query_06.txt",
        "code": "VAULT_KTT_06"
    },
    {
        "file": "07_su_kien_dong_cua_15_9_2026_va_dieu_chuyen.md",
        "title": "Báo Cáo 07: Biến Cố Đóng Cửa Ngày 15/9/2026 — Dư Luận, Hoài Niệm & Cuộc Dịch Chuyển Sang 18 Hàng Bài",
        "query_file": "query_07.txt",
        "code": "VAULT_KTT_07"
    },
    {
        "file": "08_kinh_te_hoc_dat_vang_vs_tuong_lai_thuong_hieu.md",
        "title": "Báo Cáo 08: Kinh Tế Học First Principles — Chi Phí Cơ Hội Đất Vàng Hoàn Kiếm & Tương Lai Thương Hiệu Di Sản",
        "query_file": "query_08.txt",
        "code": "VAULT_KTT_08"
    }
]

async def main():
    VAULT_DIR.mkdir(parents=True, exist_ok=True)
    print("=== BẮT ĐẦU BATCH EXTRACTION 8 BÁO CÁO NGHIÊN CỨU SÂU KEM TRÀNG TIỀN ===", flush=True)
    
    async with NotebookLMClient.from_storage(STORAGE_PATH) as client:
        email = await client.get_account_email()
        print(f"Đã kết nối NotebookLM thành công qua tài khoản: {email}", flush=True)
        print(f"Master Notebook ID: {NOTEBOOK_ID}\n", flush=True)
        
        for idx, item in enumerate(QUERY_MAP, start=1):
            out_file = VAULT_DIR / item["file"]
            title = item["title"]
            query_path = QUERIES_DIR / item["query_file"]
            code = item["code"]
            
            if not query_path.exists():
                print(f"  [!] Không tìm thấy file truy vấn: {query_path}", flush=True)
                continue
                
            prompt = query_path.read_text(encoding="utf-8").strip()
            print(f"[{idx:02d}/{len(QUERY_MAP)}] Đang truy vấn: {title}...", flush=True)
            
            try:
                res = await client.chat.ask(
                    NOTEBOOK_ID,
                    prompt
                )
                
                answer = res.answer if hasattr(res, "answer") else str(res)
                
                md_content = f"<!--\n"
                md_content += f"DOCUMENT PROVENANCE & EXECUTION LINEAGE:\n"
                md_content += f"- Output Document: episodes/kem-trang-tien-van-co-dat-vang/research_vault/{item['file']}\n"
                md_content += f"- Master Notebook ID: {NOTEBOOK_ID}\n"
                md_content += f"- Method: Direct RPC Extraction (notebooklm-py)\n"
                md_content += f"- Topic Code: {code}\n"
                md_content += f"-->\n\n"
                md_content += f"# {title}\n\n"
                md_content += f"> **Mã chủ đề:** `{code}`  \n"
                md_content += f"> **Nguồn trích xuất:** Google NotebookLM Master Notebook (`{NOTEBOOK_ID}`)  \n"
                md_content += f"> **Phương pháp:** Direct RPC Ingestion & Batch Extraction (`notebooklm-py`)  \n"
                md_content += f"> **Thời điểm trích xuất:** Tháng 09/2026  \n\n"
                md_content += f"## 1. Yêu Cầu Truy Vấn (Research Prompt)\n\n"
                md_content += f"```text\n{prompt}\n```\n\n"
                md_content += f"---\n\n"
                md_content += f"## 2. Báo Cáo Phân Tích & Dữ Liệu Thực Chứng (Grounded Insights)\n\n"
                md_content += f"{answer}\n\n"
                
                if hasattr(res, "references") and res.references:
                    md_content += f"---\n\n## 3. Danh Mục Nguồn Trích Dẫn Thực Chứng (Citations & Sources)\n\n"
                    for ref_idx, ref in enumerate(res.references, start=1):
                        source_id = getattr(ref, "source_id", "N/A")
                        quote = getattr(ref, "quote", "") or getattr(ref, "text", "")
                        title_src = getattr(ref, "source_title", "") or getattr(ref, "title", "Tài liệu NotebookLM")
                        md_content += f"- **[{ref_idx}] {title_src}** (Source ID: `{source_id}`)\n"
                        if quote:
                            md_content += f"  > *\"{quote.strip()}\"*\n"
                
                out_file.write_text(md_content, encoding="utf-8")
                print(f"  [+] Đã lưu thành công: {item['file']} ({len(md_content.encode('utf-8'))} bytes)", flush=True)
                
            except Exception as e:
                print(f"  [!] Lỗi khi truy vấn {title}: {e}", flush=True)
                
            # Rate limit politeness
            await asyncio.sleep(2)
            
    print("\n=== HOÀN TẤT BATCH EXTRACTION 8 BÁO CÁO CHUYÊN SÂU KEM TRÀNG TIỀN ===", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
