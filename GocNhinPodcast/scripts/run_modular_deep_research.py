#!/usr/bin/env python3
"""
Modular Multi-Query Deep Research Ingestion Engine V2
For Episode: Vinh Thai Lan - Song Ngam & Ngoai Giao VN
Notebook ID: 8cde2086-515e-4de5-99a4-84ecf6a3e8fb
"""

import asyncio
import os
import sys
import time

os.environ["NOTEBOOKLM_HOME"] = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.notebooklm_home"

from notebooklm.client import NotebookLMClient

NOTEBOOK_ID = "8cde2086-515e-4de5-99a4-84ecf6a3e8fb"

# Remaining Prompts to execute sequentially
PROMPTS = [
    {
        "id": 3,
        "label": "Prompt 3: Dia kinh te Nang luong, OCA & Kra Landbridge",
        "query": (
            "Thailand Cambodia Overlapping Claims Area OCA MOU 44 Koh Kood natural gas Erawan field; "
            "Tranh chap vung bien chong lan Thai Lan Campuchia mo khi; "
            "Thailand Land Bridge Chumphon Ranong deep sea port Kra isthmus Malacca bypass Singapore reaction"
        ),
    },
    {
        "id": 4,
        "label": "Prompt 4: Thuy van Mekong, Kenh Phu Nam Techo & DBSCL",
        "query": (
            "Funan Techo Canal Cambodia Mekong River Commission MRC Bassac river impact Mekong Delta salinity intrusion; "
            "Kenh dao Phu Nam Techo Campuchia 180 km Cai Mep Thi Vai logistics sovereignty"
        ),
    },
    {
        "id": 5,
        "label": "Prompt 5: Da phuong ASEAN, Canh tranh Quoc te & Ngu nghiep IUU",
        "query": (
            "Gulf of Thailand maritime security ASEAN SEANWFZ; "
            "IUU fishing Gulf of Thailand European Commission yellow card Thailand Vietnam; "
            "Fisheries disputes Gulf of Thailand overfishing small scale fishermen Kien Giang Ca Mau"
        ),
    },
]

async def poll_until_complete(client, notebook_id: str, task_id: str, label: str, max_wait_sec: int = 1200):
    print(f"\n[*] [{label}] Bat dau theo doi Task {task_id} (Timeout: {max_wait_sec}s)...", flush=True)
    start_time = time.time()
    
    while True:
        elapsed = int(time.time() - start_time)
        if elapsed > max_wait_sec:
            print(f"[!] [{label}] Qua thoi gian cho ({max_wait_sec}s). Huy task de tranh tac nghen...", flush=True)
            await client.research.cancel(notebook_id, run_id=task_id)
            return None

        # Poll using internal model lookup to avoid ambiguous error
        tasks = await client.research._poll_task_models(notebook_id)
        current_task = next((t for t in tasks if t.task_id == task_id), None)
        
        if not current_task:
            print(f"[-] [{label}] Khong tim thay task {task_id}", flush=True)
            return None
            
        status = current_task.status
        print(f"    [{label}] Elapsed: {elapsed}s | Status: {status} | Sources so far: {len(current_task.sources)}", flush=True)
        
        if status == "completed":
            print(f"[+] [{label}] HOAN TAT! So luong nguon: {len(current_task.sources)}", flush=True)
            return current_task
        elif status in ("failed", "cancelled"):
            print(f"[-] [{label}] Task ket thuc voi trang thai: {status}", flush=True)
            return None
            
        await asyncio.sleep(20)

async def import_task_sources(client, notebook_id: str, task, label: str):
    if not task or not task.sources:
        print(f"[-] [{label}] Khong co nguon de import.", flush=True)
        return []
        
    print(f"[*] [{label}] Dang import {len(task.sources)} nguon vao Master Notebook...", flush=True)
    try:
        imported = await client.research.import_sources_with_verification(notebook_id, task.task_id, task.sources)
        print(f"[+] [{label}] Da import thanh cong {len(imported)} nguon!", flush=True)
        return imported
    except Exception as e:
        print(f"[!] [{label}] Loi khi import_sources_with_verification: {e}", flush=True)
        try:
            imported = await client.research.import_sources(notebook_id, task.task_id, task.sources)
            print(f"[+] [{label}] Fallback import_sources thanh cong {len(imported)} nguon!", flush=True)
            return imported
        except Exception as e2:
            print(f"[!] [{label}] Loi fallback import_sources: {e2}", flush=True)
            return []

async def main():
    async with NotebookLMClient.from_storage() as client:
        print(f"=======================================================", flush=True)
        print(f"[*] BAT DAU PIPELINE MODULAR DEEP RESEARCH", flush=True)
        print(f"[*] Master Notebook: {NOTEBOOK_ID}", flush=True)
        print(f"=======================================================", flush=True)
        
        # 1. Wait for active Prompt 2 task
        prompt_2_id = "085c1dce-7241-4676-bdfb-33de619542cf"
        p2_task = await poll_until_complete(client, NOTEBOOK_ID, prompt_2_id, "Prompt 2: An ninh & Ream")
        if p2_task:
            await import_task_sources(client, NOTEBOOK_ID, p2_task, "Prompt 2")
            
        await asyncio.sleep(10)
        
        # 2. Sequentially run Prompts 3, 4, 5
        for p in PROMPTS:
            print(f"\n-------------------------------------------------------", flush=True)
            print(f"[*] KHOI CHAY {p['label']}...", flush=True)
            print(f"[*] Query: {p['query']}", flush=True)
            print(f"-------------------------------------------------------", flush=True)
            
            try:
                start_res = await client.research.start(NOTEBOOK_ID, p["query"], mode="deep")
                task_id = start_res.task_id
                print(f"[+] Started! Task ID: {task_id}", flush=True)
                
                # Resolve UUID from _poll_task_models
                await asyncio.sleep(5)
                tasks = await client.research._poll_task_models(NOTEBOOK_ID)
                # Find task matching query
                active_t = next((t for t in tasks if t.query.startswith(p["query"][:30]) and t.status == "in_progress"), None)
                real_task_id = active_t.task_id if active_t else task_id
                
                completed_task = await poll_until_complete(client, NOTEBOOK_ID, real_task_id, p["label"])
                if completed_task:
                    await import_task_sources(client, NOTEBOOK_ID, completed_task, p["label"])
            except Exception as e:
                print(f"[!] Loi khi thuc thi {p['label']}: {e}", flush=True)
                
            await asyncio.sleep(15)
            
        # 3. Final summary of total sources
        sources = await client.sources.list(NOTEBOOK_ID)
        print(f"\n=======================================================", flush=True)
        print(f"[+] HOAN TAT TOAN BO PIPELINE DEEP RESEARCH!", flush=True)
        print(f"[+] Tong so tai lieu da nap vao Master Notebook: {len(sources)}", flush=True)
        print(f"=======================================================", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
