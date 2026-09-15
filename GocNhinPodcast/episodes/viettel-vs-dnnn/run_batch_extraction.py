import asyncio
import json
import os
import sys
from pathlib import Path
from notebooklm import NotebookLMClient

NOTEBOOK_ID = "664c441e-65c0-49bb-9bfe-0b3148cace2c"
STORAGE_PATH = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.notebooklm_home/profiles/default/storage_state.json"
BASE_DIR = Path("/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/viettel-vs-dnnn")
VAULT_DIR = BASE_DIR / "research_vault"
QUERIES_DIR = BASE_DIR / "queries"

QUERY_MAP = [
    {
        "file": "01_toan_canh_phan_hoa_doanh_nghiep_quan_doi.md",
        "title": "Báo Cáo 01: Toàn Cảnh & Sự Phân Hóa Hệ Sinh Thái Doanh Nghiệp Quân Đội Việt Nam (NQ 425 & KL 16)",
        "query_file": "query_01.txt"
    },
    {
        "file": "02_giai_phau_8_gia_tri_cot_loi_triet_ly_viettel.md",
        "title": "Báo Cáo 02: Giải Phẫu 8 Giá Trị Văn Hóa Cốt Lõi & Hệ Thống Triết Lý Hành Động Viettel",
        "query_file": "query_02.txt"
    },
    {
        "file": "03_dot_pha_the_che_tien_luong_nghi_dinh_79_2024.md",
        "title": "Báo Cáo 03: Đột Phá Thể Chế Tiền Lương & Năng Suất Lao Động Theo Nghị Định 79/2024/NĐ-CP",
        "query_file": "query_03.txt"
    },
    {
        "file": "04_ban_linh_khuoc_tu_bay_dia_to_bat_dong_san.md",
        "title": "Báo Cáo 04: Bản Lĩnh Khước Từ Bẫy Địa Tô Bất Động Sản — Viettel vs Các Bài Học Sai Phạm Đất Quốc Phòng",
        "query_file": "query_04.txt"
    },
    {
        "file": "05_chien_luoc_bat_doi_xung_nong_thon_vay_thanh_thi.md",
        "title": "Báo Cáo 05: Chiến Lược Bất Đối Xứng 'Lấy Nông Thôn Vây Thành Thị' & Cuộc Cách Mạng Bình Dân Hóa Viễn Thông",
        "query_file": "query_05.txt"
    },
    {
        "file": "06_ho_so_vien_chinh_toan_cau_viettel_global.md",
        "title": "Báo Cáo 06: Hồ Sơ Viễn Chinh Toàn Cầu Viettel Global — 10 Thị Trường, 7 Ngôi Đầu & Dòng Kiều Hối Tỷ USD",
        "query_file": "query_06.txt"
    },
    {
        "file": "07_nang_luc_tu_chu_cong_nghe_viettel_high_tech.md",
        "title": "Báo Cáo 07: Năng Lực Tự Chủ Công Nghệ Cao Viettel High Tech — Từ vOCS, 5G Đến Radar 3D AESA & Chip Bán Dẫn",
        "query_file": "query_07.txt"
    },
    {
        "file": "08_hoa_giai_bai_toan_nguoi_dai_dien_ky_tri.md",
        "title": "Báo Cáo 08: Hóa Giải 'Bài Toán Người Đại Diện' (Jensen & Meckling) & 'Ràng Buộc Ngân Sách Mềm' (Janos Kornai)",
        "query_file": "query_08.txt"
    },
    {
        "file": "09_doi_chieu_that_bai_cac_dnnn_truyen_thong.md",
        "title": "Báo Cáo 09: Đối Chiếu Bài Học Thất Bại Của Khối DNNN Truyền Thống — Lời Cảnh Báo Từ Vinashin, Vinalines & BOT",
        "query_file": "query_09.txt"
    },
    {
        "file": "10_ma_tran_rui_ro_con_dau_dau_viettel.md",
        "title": "Báo Cáo 10: Ma Trận Rủi Ro & Những Cơn Đau Đầu Chiến Lược Của Viettel Giai Đoạn 2026–2030 (Red Team Audit)",
        "query_file": "query_10.txt"
    },
    {
        "file": "11_bai_hoc_the_che_nghi_quyet_79_nq_tw.md",
        "title": "Báo Cáo 11: Bài Học Thể Chế Từ 'Ngoại Lệ Viettel' Cho Đề Án Cải Cách DNNN Theo Nghị Quyết 79-NQ/TW",
        "query_file": "query_11.txt"
    }
]

async def main():
    VAULT_DIR.mkdir(parents=True, exist_ok=True)
    print("=== BẮT ĐẦU BATCH EXTRACTION 11 BÁO CÁO NGHIÊN CỨU SÂU VIETTEL VS DNNN ===", flush=True)
    
    async with NotebookLMClient.from_storage(STORAGE_PATH) as client:
        email = await client.get_account_email()
        print(f"Đã kết nối NotebookLM thành công qua tài khoản: {email}", flush=True)
        print(f"Master Notebook ID: {NOTEBOOK_ID}\n", flush=True)
        
        for idx, item in enumerate(QUERY_MAP, start=1):
            out_file = VAULT_DIR / item["file"]
            title = item["title"]
            query_path = QUERIES_DIR / item["query_file"]
            
            if not query_path.exists():
                print(f"  [!] Không tìm thấy file truy vấn: {query_path}", flush=True)
                continue
                
            prompt = query_path.read_text(encoding="utf-8").strip()
            print(f"[{idx:02d}/{len(QUERY_MAP)}] Đang truy vấn: {title}...", flush=True)
            
            try:
                # Ask question to extract data
                res = await client.chat.ask(
                    NOTEBOOK_ID,
                    prompt
                )
                
                answer = res.answer if hasattr(res, "answer") else str(res)
                
                md_content = f"<!--\n"
                md_content += f"DOCUMENT PROVENANCE & EXECUTION LINEAGE:\n"
                md_content += f"- Output Document: episodes/viettel-vs-dnnn/research_vault/{item['file']}\n"
                md_content += f"- Master Notebook ID: {NOTEBOOK_ID}\n"
                md_content += f"- Method: Direct RPC Extraction (notebooklm-py)\n"
                md_content += f"- Topic Code: VAULT_VIETTEL_{idx:02d}\n"
                md_content += f"-->\n\n"
                md_content += f"# {title}\n\n"
                md_content += f"> **Mã chủ đề:** `VAULT_VIETTEL_{idx:02d}`  \n"
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
                
            # Respect rate limits between queries
            await asyncio.sleep(2)
            
    print("\n=== HOÀN TẤT BATCH EXTRACTION 11 BÁO CÁO CHUYÊN SÂU VIETTEL VS DNNN ===", flush=True)

if __name__ == "__main__":
    asyncio.run(main())

