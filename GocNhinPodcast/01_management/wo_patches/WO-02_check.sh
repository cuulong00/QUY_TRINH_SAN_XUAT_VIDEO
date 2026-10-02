T=$1; cd $T
echo "== lăng kính dòng tiền liệt kê cứng ngoài AGENTS.md / persona chuyên môn"
grep -rnE "Forensic Cash Auditor" .agents 00_core 02_templates | grep -v _archive | grep -vE "AGENTS.md|the_capital_markets_analyst" | cut -c1-150
echo "== '3 lăng kính' còn"; grep -rnE "3 lăng kính|ba lăng kính|3 đòn công kích" .agents 00_core 02_templates | grep -v _archive | cut -c1-150
echo "== điểm hòa vốn / FCF trong cổng chấm chung"; grep -rnE "điểm hòa vốn|FCF|bảng cân đối" 00_core/masterpiece_quality_standard.md 00_core/chapter_quality_standard.md 00_core/retention_gate_checklist.md 00_core/quality_rubric.md .agents/skills/compliance_council/SKILL.md .agents/skills/hook_engine/SKILL.md | cut -c1-150
echo "== Personal-First / Loại A và B gộp"; grep -rnE "Personal-First|PERSONAL-FIRST|Loại A và B" .agents 00_core 02_templates | grep -v _archive | cut -c1-150
echo "== túi tiền trong luật hook/cổng chung (không tính Loại A, Shorts, persona)"; grep -rn "túi tiền" 00_core/golden_samples/golden_hook.md 00_core/retention_gate_checklist.md 00_core/masterpiece_quality_standard.md .agents/skills/hook_engine/SKILL.md | grep -viE "Loại A|A: " | cut -c1-150
echo "(hết)"
