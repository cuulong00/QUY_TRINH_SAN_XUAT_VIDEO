import asyncio
import json
import os
from pathlib import Path
from notebooklm import NotebookLMClient

NOTEBOOK_ID = "82a612e7-c2d6-4cb7-b38e-2fcd8d223489"
STORAGE_PATH = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.notebooklm_home/profiles/default/storage_state.json"
BASE_DIR = Path("/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/phu-quoc-tinh-hoa-hoi-tu")
QUERIES_DIR = BASE_DIR / "research_queries"
VAULT_DIR = BASE_DIR / "research_vault"

QUERIES_MAP = [
    ("query_01_ippg_bai_vong.txt", "01_ippg_bai_vong_free_trade_zone.md", "Báo Cáo Chuyên Sâu: Khu Phi Thuế Quan IPPG 6.830 Tỷ Tại Bãi Vòng & Thặng Dư Thương Mại Xa Xỉ"),
    ("query_02_sungroup_mice_tod.txt", "02_sungroup_mice_and_tod_infrastructure.md", "Báo Cáo Chuyên Sâu: Hạ Tầng MICE Mũi Đất Đỏ & Tuyến Tàu Điện TOD 9.000 Tỷ Của Sun Group"),
    ("query_03_real_estate_long_term.txt", "03_real_estate_long_term_and_elite_community.md", "Báo Cáo Chuyên Sâu: Sự Dịch Chuyển Sang Bất Động Sản Đô Thị Sở Hữu Lâu Dài & Cộng Đồng Tinh Hoa"),
    ("query_04_sandbox_talent_visa221.txt", "04_sandbox_talent_visa_decree_221.md", "Báo Cáo Chuyên Sâu: Khung Thể Chế Sandbox & Nghị Định 221/2025/NĐ-CP Thu Hút Nhân Tài Toàn Cầu"),
    ("query_05_benchmark_hainan_ftp.txt", "05_international_benchmark_hainan_ftp_friction.md", "Đối Sánh Quốc Tế: Bài Học 'Ma Sát Chính Sách' & Suy Giảm Doanh Số Tại Cảng Tự Do Hải Nam"),
    ("query_06_benchmark_jeju_jdc.txt", "06_international_benchmark_jeju_jdc_private_services.md", "Đối Sánh Quốc Tế: Mô Hình Dịch Vụ Giáo Dục - Y Tế Tư Nhân & BĐS Gắn Visa Tại Jeju JDC"),
    ("query_07_counter_thesis_seed_funding.txt", "07_counter_thesis_seed_funding_and_fdi_wait_and_see.md", "Phản Biện Vĩ Mô 1: Rủi Ro 'Ảo Ảnh Vốn Mồi' & Tâm Lý Wait-And-See Của Dòng Vốn FDI"),
    ("query_08_counter_thesis_ecological_limits.txt", "08_counter_thesis_ecological_limits_and_infrastructure.md", "Phản Biện Vĩ Mô 2: Lằn Ranh Sinh Thái, An Ninh Nguồn Nước & Năng Lực Chịu Tải Hạ Tầng"),
    ("query_09_counter_thesis_social_welfare.txt", "09_counter_thesis_social_welfare_and_livelihood.md", "Phản Biện Vĩ Mô 3: Tác Động Dân Sinh, Chuyển Đổi Sinh Kế & Nguy Cơ Phân Hóa Hai Tầng"),
    ("query_10_institutional_governance_evolution.txt", "10_institutional_governance_systemic_evolution.md", "Quản Trị Thể Chế Dài Hạn: Chuyển Dịch Từ 'Uy Quyền Cá Nhân' Sang 'Hệ Thống Pháp Trị Tự Động'"),
]

async def main():
    VAULT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"=== BẮT ĐẦU QUY TRÌNH BATCH EXTRACTION SANG RESEARCH_VAULT ===")
    print(f"Notebook ID: {NOTEBOOK_ID}")
    
    async with NotebookLMClient.from_storage(STORAGE_PATH) as client:
        email = await client.get_account_email()
        print(f"Đã kết nối NotebookLM thành công với tài khoản: {email}\n")
        
        for idx, (query_file, output_file, title) in enumerate(QUERIES_MAP, start=1):
            query_path = QUERIES_DIR / query_file
            output_path = VAULT_DIR / output_file
            
            if not query_path.exists():
                print(f"[-] Không tìm thấy file query: {query_file}")
                continue
                
            query_text = query_path.read_text(encoding="utf-8").strip()
            print(f"[{idx}/{len(QUERIES_MAP)}] Đang trích xuất: {title}...")
            
            try:
                res = await client.chat.ask(
                    notebook_id=NOTEBOOK_ID,
                    question=query_text
                )
                
                answer = res.answer if hasattr(res, "answer") else str(res)
                
                # Format file Markdown
                md_content = f"# {title}\n\n"
                md_content += f"> **Mã chủ đề:** `VAULT_T3_{idx:02d}`  \n"
                md_content += f"> **Nguồn trích xuất:** Google NotebookLM Master Notebook (`{NOTEBOOK_ID}`)  \n"
                md_content += f"> **Phương pháp:** Direct RPC Ingestion & Batch Extraction (`notebooklm-py`)  \n\n"
                md_content += f"## 1. Yêu Cầu Truy Vấn (Research Prompt)\n\n"
                md_content += f"```text\n{query_text}\n```\n\n"
                md_content += f"---\n\n"
                md_content += f"## 2. Báo Cáo Phân Tích & Dữ Liệu Thực Chứng (Grounded Insights)\n\n"
                md_content += f"{answer}\n\n"
                
                # Ghi citations nếu có
                if hasattr(res, "references") and res.references:
                    md_content += f"---\n\n## 3. Danh Mục Nguồn Trích Dẫn Thực Chứng (Citations & Sources)\n\n"
                    for ref_idx, ref in enumerate(res.references, start=1):
                        source_id = getattr(ref, "source_id", "N/A")
                        quote = getattr(ref, "quote", "") or getattr(ref, "text", "")
                        title_src = getattr(ref, "source_title", "") or getattr(ref, "title", "Tài liệu NotebookLM")
                        md_content += f"- **[{ref_idx}] {title_src}** (Source ID: `{source_id}`)\n"
                        if quote:
                            md_content += f"  > *\"{quote.strip()}\"*\n"
                
                output_path.write_text(md_content, encoding="utf-8")
                print(f"  [+] Đã lưu thành công: {output_file} ({len(md_content.encode('utf-8'))} bytes)")
                
            except Exception as e:
                print(f"  [!] Lỗi khi trích xuất {title}: {e}")
                
            # Nghỉ ngắn giữa các câu hỏi để tránh rate limit
            await asyncio.sleep(2)
            
    print(f"\n=== HOÀN TẤT BATCH EXTRACTION 10/10 TỆP VÀO RESEARCH_VAULT ===")

if __name__ == "__main__":
    asyncio.run(main())
