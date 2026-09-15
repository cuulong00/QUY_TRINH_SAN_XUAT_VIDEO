import asyncio
import time
from notebooklm.client import NotebookLMClient
from notebooklm.exceptions import ResearchTimeoutError, RateLimitError, AuthError

NOTEBOOK_ID = "477ee042-ce17-4ef1-9f53-9cbd97316e78"

QUERIES = [
    {
        "id": "Q3",
        "title": "Tử huyệt Giá điện & Đạo luật EPIRA 2001",
        "query": "Philippines electricity prices tariffs Meralco EPIRA 2001 power generation cartels kWh rates industrial manufacturing competitiveness DOE 2025 2026"
    },
    {
        "id": "Q4",
        "title": "Khủng hoảng Lúa gạo & Nghịch lý IRRI vs Việt Nam",
        "query": "Philippines rice imports world largest importer USDA IRRI Los Banos CARP agrarian reform Vietnam rice trade DA BPI food inflation 2025 2026"
    },
    {
        "id": "Q5",
        "title": "Kiều hối OFW & Ngành BPO trước Cơn bão AI",
        "query": "Philippines BPO IT-BPM industry IBPAP generative AI voice agents impact customer service OFW personal cash remittances BSP 2025 2026 roadmap refresh"
    },
    {
        "id": "Q6",
        "title": "Quả bom Nợ công & Quỹ Maharlika",
        "query": "Philippines national debt 19 trillion peso debt-to-GDP ratio Bureau of Treasury Maharlika Investment Fund LandBank DBP fiscal strain 2025 2026"
    },
    {
        "id": "Q7",
        "title": "Nội chiến Vương triều Marcos Jr. vs Duterte",
        "query": "Marcos Duterte feud UniTeam split Sara Duterte impeachment Senate trial Rodrigo Duterte ICC The Hague confidential funds 2025 2026"
    },
    {
        "id": "Q8",
        "title": "Bàn cờ Biển Đông & 9 Căn cứ Quân sự EDCA",
        "query": "Philippines EDCA US military bases Cagayan Isabela Palawan South China Sea West Philippine Sea Ayungin Scarborough shoal tensions China MDT 1951 2025 2026"
    }
]

async def run_pipeline():
    print(f"=== BẮT ĐẦU CHUỖI DEEP RESEARCH TUẦN TỰ TRÊN MASTER NOTEBOOK {NOTEBOOK_ID} ===")
    
    async with NotebookLMClient.from_storage() as client:
        for item in QUERIES:
            qid = item["id"]
            qtitle = item["title"]
            qstr = item["query"]
            
            print(f"\n[{qid}] 🚀 Bắt đầu Deep Research: {qtitle}")
            print(f"    Query: {qstr}")
            
            try:
                task_start = await client.research.start(
                    NOTEBOOK_ID,
                    qstr,
                    mode="deep",
                    source="web"
                )
                
                # Xác định task_id hoặc report_id để chờ
                poll_task_id = task_start.report_id or task_start.task_id
                print(f"    -> Đã khởi tạo thành công task: {poll_task_id}. Đang tiến hành quét sâu web và đợi hoàn tất...")
                
                task = await client.research.wait_for_completion(
                    NOTEBOOK_ID,
                    task_id=poll_task_id,
                    timeout=900
                )
                
                print(f"    -> Deep Research hoàn tất! Trạng thái: {task.status.value}, Tìm thấy: {len(task.sources)} nguồn.")
                
                if task.sources:
                    print(f"    -> Đang nạp toàn bộ {len(task.sources)} nguồn vào Master Notebook...")
                    imported = await client.research.import_sources(
                        NOTEBOOK_ID,
                        task_id=task.task_id,
                        sources=task.sources
                    )
                    print(f"    ✅ [{qid}] Nạp thành công {len(imported)} nguồn mới vào sổ tay!")
                else:
                    print(f"    ⚠️ [{qid}] Không có nguồn mới để nạp.")
                    
            except ResearchTimeoutError:
                print(f"    ❌ [{qid}] Quá thời gian chờ (Timeout 900s).")
            except RateLimitError:
                print(f"    ⚠️ [{qid}] Bị giới hạn tần suất (Rate limit), tạm dừng 60s trước khi thử lại...")
                await asyncio.sleep(60)
            except Exception as e:
                print(f"    ❌ [{qid}] Lỗi không mong muốn: {e}")
                
            print(f"    Nghỉ 5 giây trước khi thực hiện chuyên đề tiếp theo...")
            await asyncio.sleep(5)

    print("\n🎉 HOÀN TẤT TOÀN BỘ CHUỖI DEEP RESEARCH Q3 -> Q8!")

if __name__ == "__main__":
    asyncio.run(run_pipeline())
