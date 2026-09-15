import asyncio
import sys
from notebooklm.client import NotebookLMClient
from notebooklm.exceptions import ResearchTimeoutError

NOTEBOOK_ID = "477ee042-ce17-4ef1-9f53-9cbd97316e78"
TASK_ID = "3bddfe4d-c065-4f7e-ba43-51320729f676"

async def main():
    async with NotebookLMClient.from_storage() as client:
        print(f"Đang kiểm tra tiến trình Query 2 (Task ID: {TASK_ID})...")
        task = await client.research.poll(NOTEBOOK_ID, task_id=TASK_ID)
        print(f"Trạng thái hiện tại: {task.status.value}")
        print(f"Số lượng nguồn tìm được: {len(task.sources)}")
        
        if task.status.value == "completed":
            print(f"Tiến hành nạp toàn bộ {len(task.sources)} nguồn vào Master Notebook...")
            imported = await client.research.import_sources(NOTEBOOK_ID, task_id=task.task_id, sources=task.sources)
            print(f"✅ Đã nạp thành công {len(imported)} nguồn từ Query 2!")
        elif task.status.value == "in_progress":
            print("Vẫn đang nghiên cứu, tiến hành chờ...")
            try:
                task = await client.research.wait_for_completion(NOTEBOOK_ID, task_id=TASK_ID, timeout=600)
                print(f"Nghiên cứu hoàn tất! Trạng thái: {task.status.value}, Nguồn: {len(task.sources)}")
                imported = await client.research.import_sources(NOTEBOOK_ID, task_id=task.task_id, sources=task.sources)
                print(f"✅ Đã nạp thành công {len(imported)} nguồn từ Query 2!")
            except ResearchTimeoutError:
                print("Chờ quá thời gian (timeout), tiếp tục kiểm tra lại sau.")
        else:
            print(f"Trạng thái khác: {task.status.value}")

if __name__ == "__main__":
    asyncio.run(main())
