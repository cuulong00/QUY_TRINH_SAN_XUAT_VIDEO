import os, json, subprocess

env = os.environ.copy()
env["NOTEBOOKLM_HOME"] = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.notebooklm_home"
bin_path = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.venv_notebooklm/bin/notebooklm"
notebook_id = "7069c72d-fe15-436c-9c21-57ac114117ec"

queries = [
    ("002_enshittification_and_digital_rent.txt", "002_enshittification_and_digital_rent.md", "Quy luat Enshittification va Ban chat Thu to so"),
    ("003_us_archetype_uber_amazon.txt", "003_us_archetype_uber_amazon.md", "Nguyen mau My: Uber Amazon va Cu siet no Pho Wall"),
    ("004_china_archetype_meituan_algorithms.txt", "004_china_archetype_meituan_algorithms.md", "Nguyen mau Trung Quoc: Chuyen che thuat toan Meituan va SAMR"),
    ("005_f2c_supply_chain_and_logistics.txt", "005_f2c_supply_chain_and_logistics.md", "Chuoi cung ung F2C va Con bao hang xuong bien gioi"),
    ("006_the_precariat_and_asset_asymmetry.txt", "006_the_precariat_and_asset_asymmetry.md", "Giai cap bap benh The Precariat va Bat doi xung tai san"),
    ("007_ecommerce_fees_and_creator_fatigue.txt", "007_ecommerce_fees_and_creator_fatigue.md", "Ma tran phi san TMDT va Su suy thoai cua Creator"),
    ("008_tripartite_structural_conflict.txt", "008_tripartite_structural_conflict.md", "Giai phau xung dot tam giac: Nen tang - Doi tac - Khach hang"),
    ("009_resistance_and_private_domain.txt", "009_resistance_and_private_domain.md", "Chien tranh du kich va Lan song di cu ve Ao rieng"),
    ("010_regulatory_interventions_global_and_vn.txt", "010_regulatory_interventions_global_and_vn.md", "Ban co can thiep the che: Tu Quoc te den Viet Nam")
]

for qfile, outfile, title in queries:
    p_path = os.path.join("episodes/bay-mat-ngot-kinh-te-nen-tang/extraction_prompts", qfile)
    o_path = os.path.join("episodes/bay-mat-ngot-kinh-te-nen-tang/research_vault", outfile)
    print(f"=== Extracting: {title} ===", flush=True)
    cmd = [bin_path, "ask", "--prompt-file", p_path, "-n", notebook_id, "--json", "--save-as-note", "-t", title, "--timeout", "240"]
    res = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if res.returncode == 0:
        try:
            data = json.loads(res.stdout)
            answer = data.get("answer", "")
            refs = data.get("references", [])
            print(f"SUCCESS: {title} -> {len(answer)} chars, {len(refs)} citations.", flush=True)
            with open(o_path, "w", encoding="utf-8") as out_f:
                out_f.write("<!--" + nl)
                out_f.write(f"PROVENANCE: NotebookLM Direct RPC Extraction" + nl)
                out_f.write(f"Master Notebook: {notebook_id}" + nl)
                out_f.write(f"Topic: {title}" + nl)
                out_f.write("-->" + nl + nl)
                out_f.write(f"# {title.upper()}" + nl + nl)
                out_f.write(answer + nl + nl)
                out_f.write("## NGUON TRICH DAN (CITATIONS)" + nl)
                for r in refs:
                    idx = r.get("index", "")
                    t = r.get("title", "")
                    u = r.get("url", "")
                    out_f.write(f"- [{idx}] **{t}**: {u}" + nl)
            print(f"Saved to {o_path}", flush=True)
        except Exception as e:
            print(f"JSON parsing error: {e}", flush=True)
    else:
        print(f"FAILED {title}: {res.stderr}", flush=True)

print("ALL 9 EXTRACTIONS FINISHED!", flush=True)
