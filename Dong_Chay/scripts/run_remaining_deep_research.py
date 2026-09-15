import asyncio
import time
import subprocess
from notebooklm.client import NotebookLMClient
from notebooklm.exceptions import ResearchTimeoutError, RateLimitError, AuthError

NOTEBOOK_ID = "477ee042-ce17-4ef1-9f53-9cbd97316e78"

REMAINING_QUERIES = [
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

def refresh_browser_cookies():
    print("    🔄 Đang làm mới cookies từ Chrome...")
    subprocess.run([
        ".venv/bin/notebooklm", "login",
        "--browser-cookies", "chrome",
        "--account", "duongtt84@gmail.com"
    ], check=True)

async def run_pipeline():
    print(f"=== TIẾP TỤC CHUỖI DEEP RESEARCH [Q5 -> Q8] TRÊN MASTER NOTEBOOK {NOTEBOOK_ID} ===")
    
    for item in REMAINING_QUERIES:
        qid = item["id"]
        qtitle = item["title"]
        qstr = item["query"]
        
        print(f"\n[{qid}] 🚀 Bắt đầu Deep Research: {qtitle}")
        print(f"    Query: {qstr}")
        
        # Đảm bảo cookies luôn tươi mới trước mỗi query
        try:
            refresh_browser_cookies()
        except Exception as e:
            print(f"    ⚠️ Cảnh báo refresh cookies: {e}")
        
        async with NotebookLMClient.from_storage() as client:
            try:
                task_start = await client.research.start(
                    NOTEBOOK_ID,
                    qstr,
                    mode="deep",
                    source="web"
                )
                
                poll_task_id = task_start.report_id or task_start.task_id
                print(f"    -> Đã khởi tạo task: {poll_task_id}. Đang quét sâu...")
                
                task = await client.research.wait_for_completion(
                    NOTEBOOK_ID,
                    task_id=poll_task_id,
                    timeout=900
                )
                
                print(f"    -> Hoàn tất quét! Trạng thái: {task.status.value}, Tìm thấy: {len(task.sources)} nguồn.")
                
                if task.sources:
                    print(f"    -> Đang nạp toàn bộ {len(task.sources)} nguồn vào Master Notebook...")
                    imported = await client.research.import_sources(
                        NOTEBOOK_ID,
                        task_id=task.task_id,
                        sources=task.sources
                    )
                    print(f"    ✅ [{qid}] Nạp thành công {len(imported)} nguồn mới vào sổ tay!")
                else:
                    print(f"    ⚠️ [{qid}] Không có nguồn mới.")
                    
            except ResearchTimeoutError:
                print(f"    ❌ [{qid}] Timeout 900s.")
            except RateLimitError:
                print(f"    ⚠️ [{qid}] Rate limited, nghỉ 60s...")
                await asyncio.sleep(60)
            except Exception as e:
                print(f"    ❌ [{qid}] Lỗi: {e}")
                
        print(f"    Nghỉ 5 giây trước chuyên đề tiếp theo...")
        await asyncio.sleep(5)

    print("\n🎉 HOÀN TẤT 100% TOÀN BỘ CÁC CHUYÊN ĐỀ DEEP RESEARCH Q1 -> Q8!")

if __name__ == "__main__":
    asyncio.run(run_pipeline())
