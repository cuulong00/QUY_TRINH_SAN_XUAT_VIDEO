#!/usr/bin/env python3
"""
Deep Research Ingestion Script for X-Economic
Episode: cuoc-chien-phan-cuc-ai
Master Notebook: 5dd7498c-d258-4d37-b626-eb5c0f70b917
Runs 6 modular deep research queries sequentially on Google NotebookLM,
waits for Deep Crawler completion, and imports all primary web sources.
"""

import asyncio
import os
import sys
import time
import click
from notebooklm.cli.helpers import get_auth_tokens
from notebooklm.client import NotebookLMClient

NOTEBOOK_ID = "5dd7498c-d258-4d37-b626-eb5c0f70b917"

PROMPTS = [
    (
        "Pillar 1: Scientific Foundations, Nobel 2024 & Superintelligence",
        "Geoffrey Hinton Nobel Physics 2024 Demis Hassabis AlphaFold AGI roadmap 2029 2030 Ray Kurzweil Nick Bostrom orthogonality thesis AI existential risk"
    ),
    (
        "Pillar 2: AI Lab Political Economy, Aschenbrenner, Amodei & SSI 2026",
        "Leopold Aschenbrenner Situational Awareness memo AGI 2027 Dario Amodei Machines of Loving Grace bioweapon risks Ilya Sutskever Safe Superintelligence SSI 32 billion valuation Nvidia Vera Rubin Test Time Training"
    ),
    (
        "Pillar 3: Macroeconomic Audit Nobel Acemoglu & Historical Ontology Harari",
        "Daron Acemoglu Nobel Economics 2024 The Simple Macroeconomics of AI NBER 32487 TFP growth so-so automation Yuval Noah Harari Nexus alien intelligence epistemic collapse Yanis Varoufakis technofeudalism"
    ),
    (
        "Pillar 4: Stargate Infrastructure Crisis 2026 & Energy Chokepoints",
        "Stargate Project 500 billion OpenAI SoftBank Oracle suspension Stargate UK grid constraints ASML EUV TSMC wafer capacity IEA data center 1000 TWh Three Mile Island nuclear Kairos Power SMR Colossus 2GW"
    ),
    (
        "Pillar 5: DeepSeek Algorithmic Breakthrough, Engram Memory & Arms Race 2026",
        "DeepSeek R1 reasoning 6 million training cost DeepSeek Engram Memory architecture memory wall Anthropic distillation claims brutal arms race declaration CAC socialist values regulation Huawei Ascend 910C"
    ),
    (
        "Pillar 6: Global Institutional Clash (US Trump Czar, EU AI Act, Paris Summit & Vietnam)",
        "Donald Trump David Sacks White House AI Crypto Czar National AI Policy Framework federal preemption state laws EU AI Act Article 50 GPAI enforcement Digital Omnibus delay Paris AI Action Summit 150 billion Euro Vietnam Decision 127 QD TTg 50000 semiconductor engineers"
    )
]

def get_client_auth():
    ctx = click.Context(click.Command('ingest'))
    ctx.obj = {}
    return get_auth_tokens(ctx)

async def run_ingestion(auth):
    print(f"=== KÍCH HOẠT DEEP RESEARCH NẠP NGUỒN SƠ CẤP VÀO MASTER NOTEBOOK {NOTEBOOK_ID} ===")
    
    async with NotebookLMClient(auth) as client:
        # Check active tasks first
        existing_task = "5a3b94b0-c227-43f4-8af4-d44b922ebcd7"
        try:
            print(f"\n[Task Hiện Hữu] Kiểm tra trạng thái Task 1: {existing_task}...")
            poll_res = await client.research.poll(NOTEBOOK_ID, existing_task)
            print(f" -> Trạng thái: {poll_res.status} | Số nguồn tìm thấy: {len(poll_res.sources)}")
            
            if poll_res.status in ("completed", "done"):
                print(" -> Đang import các nguồn từ Task 1...")
                imported = await client.research.import_sources(NOTEBOOK_ID, existing_task, poll_res.sources)
                print(f" -> Đã import thành công {len(imported)} nguồn từ Task 1!")
            elif poll_res.status in ("in_progress", "running"):
                print(" -> Đang chờ Task 1 hoàn tất trên Google Deep Crawler...")
                completed_task = await client.research.wait_for_completion(NOTEBOOK_ID, existing_task, timeout=1200)
                print(f" -> Task 1 hoàn tất với {len(completed_task.sources)} nguồn! Đang import...")
                imported = await client.research.import_sources(NOTEBOOK_ID, existing_task, completed_task.sources)
                print(f" -> Đã import thành công {len(imported)} nguồn sơ cấp từ Task 1!")
        except Exception as e:
            print(f" -> Lỗi khi xử lý Task hiện hữu: {e}")

        # Now run the remaining prompts
        for idx, (title, query) in enumerate(PROMPTS[1:], start=2):
            print(f"\n[{idx}/6] Bắt đầu Deep Research: {title}")
            print(f" -> Query: {query}")
            try:
                start_res = await client.research.start(NOTEBOOK_ID, query, source="web", mode="deep")
                task_id = start_res.task_id
                print(f" -> Khởi tạo Deep Research thành công! Task ID: {task_id}")
                print(f" -> Đang quét mạng và cơ sở dữ liệu học thuật quốc tế...")
                completed_task = await client.research.wait_for_completion(NOTEBOOK_ID, task_id, timeout=1800)
                print(f" -> Deep Research hoàn tất! Tìm thấy {len(completed_task.sources)} nguồn sơ cấp.")
                print(f" -> Đang tự động import toàn bộ nguồn vào Master Notebook...")
                imported = await client.research.import_sources(NOTEBOOK_ID, task_id, completed_task.sources)
                print(f" -> [THÀNH CÔNG] Đã nạp thêm {len(imported)} nguồn sơ cấp cho {title}!")
            except Exception as e:
                print(f" -> [CẢNH BÁO] Lỗi khi xử lý query {idx}: {e}")

        print("\n=== HOÀN TẤT TOÀN BỘ CHUỖI NẠP NGUỒN SƠ CẤP! KIỂM TRA TỔNG SỐ NGUỒN TRÊN NOTEBOOKLM ===")

if __name__ == "__main__":
    auth = get_client_auth()
    asyncio.run(run_ingestion(auth))
