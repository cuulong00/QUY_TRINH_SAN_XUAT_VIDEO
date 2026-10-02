T=$1; cd $T
chk(){ echo "== $1"; shift; grep -rnE "$@" .agents 00_core 02_templates 2>/dev/null | grep -v "_archive" | cut -c1-170 | head -12; }
chk "Q1 case study 1 cho B" -i "(đúng|tối đa) 1 case"
chk "Q2 Ch.2 B ép đời sống" "Chapter 2 Contract|Ch(ương|apter) 2.{0,40}BẮT BUỘC nối vĩ mô"
chk "Q3 đóng toàn bộ loop / CTA chương kết" -i "đóng toàn bộ open loop|CTA dẫn (sang )?video|High Energy CTA|CTA ở chương kết"
chk "Q4 2.5 phút" "2[.,]5 phút"
chk "Q5 8-15 từ bắt buộc" "8[-–]15 từ"
chk "Q6 gợi hình / chiaroscuro văn" -i "gợi hình|Mind's Eye|Chiaroscuro|tả cảnh"
chk "Q7 không đọc lại toàn bộ" -i "không mặc định đọc lại|3 câu cuối của chapter|1 triệu token"
chk "Q8 hook lập trường" -i "hook.{0,30}lập trường rõ|có lập trường rõ"
