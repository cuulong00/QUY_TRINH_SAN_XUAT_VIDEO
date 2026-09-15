# 02_research_map.md

episode_slug: cong-ty-1-nguoi-ai-viet-nam

core_question: Làm thế nào một cá nhân tại Việt Nam có thể tận dụng AI Agents và tự động hóa để xây dựng cỗ máy doanh nghiệp 1 người (Solopreneur) đạt doanh thu 50 - 150 triệu VNĐ/tháng với biên lợi nhuận trên 75%, đánh bại các agency cồng kềnh?
research_goal: Tổng hợp toàn bộ cơ sở pháp lý, số liệu kinh tế vĩ mô, cấu trúc chi phí so sánh và các quy trình tự động hóa thực chiến (n8n, Zalo OA, Facebook Messenger, CRM) tại thị trường Việt Nam.

verified_data_candidates:
- claim: Nhân viên văn phòng/agency tại VN lãng phí trung bình 69 giờ mỗi tháng (tương đương 2 ngày làm việc/tuần) cho các tác vụ thủ công lặp đi lặp lại.
  tentative_source: Báo cáo Tự động hóa quy trình kinh doanh (BPA) & VnEconomy TechConnect 2026.
  year: 2026
  why_it_matters: Chứng minh sự thất thoát nguồn lực khổng lồ trong bộ máy truyền thống.
  confidence: high (Vault Ref: 06_so_sanh_kinh_te_1_nguoi_vs_agency_truyen_thong.md)

- claim: Cơ cấu chi phí vận hành cố định của Agency 10-15 người tại VN dao động từ 210 đến 300 triệu VNĐ/tháng (2,5 - 3,6 tỷ/năm) với biên lợi nhuận ròng mỏng 15-25%. Trong khi Solopreneur AI chỉ tốn 5-10 triệu VNĐ/tháng chi phí cố định với biên lợi nhuận ròng 70-85%.
  tentative_source: Mô hình tài chính định lượng tổng hợp từ MISA AMIS, CloudGO, OCD & Case Study Agency VN.
  year: 2026
  why_it_matters: Mỏ neo số liệu tài chính đắt giá nhất để so sánh trực quan hai mô hình.
  confidence: high (Vault Ref: 06_so_sanh_kinh_te_1_nguoi_vs_agency_truyen_thong.md)

- claim: Chính phủ Việt Nam đã có các định hướng chính sách thí điểm mô hình "Doanh nghiệp một người" (One-Person Company - OPC) và Đề án chuyển đổi số SME 2025-2030, hỗ trợ 1 triệu doanh nhân số.
  tentative_source: Báo Chính Phủ, Báo Tuổi Trẻ, Dân Trí (Nghị quyết 86/NQ-CP & Quyết định Bộ KH&ĐT).
  year: 2026
  why_it_matters: Khẳng định tính chính danh và hợp thời của mô hình tại Việt Nam.
  confidence: high (Vault Ref: 01_chinh_sach_va_vi_mo.md)

- claim: Việc triển khai self-hosted n8n trên VPS nội địa (100k - 300k/tháng) kết hợp API LLMs (Google Gemini / OpenRouter 500k - 1tr/tháng) giúp xử lý hàng vạn lượt tương tác không giới hạn tác vụ và bảo mật dữ liệu theo Nghị định 13/2023/NĐ-CP.
  tentative_source: FPT Digital, RedAI, Benocode, Brands Vietnam.
  year: 2026
  why_it_matters: Cung cấp giải pháp kỹ thuật cụ thể, chi phí cực thấp, an toàn pháp lý cho Solopreneur.
  confidence: high (Vault Ref: 03_co_che_ai_agent_va_tu_dong_hoa.md & 05_conversational_commerce_zalo_facebook.md)

market_analysis_candidates:
- claim: Thị trường thương mại hội thoại (Conversational Commerce) tại Việt Nam dịch chuyển từ Chatbot bấm phím 1-2-3 sang AI Agent hiểu ngữ cảnh tự do và bám đuổi lead đa kênh trên Zalo OA và Messenger.
  basis: Người tiêu dùng Việt có thói quen chat trước khi mua, không dùng email.
  caveat: Cần tích hợp đúng API và bảo mật token kết nối Zalo/Facebook.
  why_useful: Giải thích tại sao AI Agent chốt đơn là "mỏ vàng" cho Solopreneur tại VN. (Vault Ref: 05_conversational_commerce_zalo_facebook.md)

case_study_candidates:
- case_name: AI Automation Agency (AAA) cho Chuỗi Nha Khoa / Thẩm Mỹ Viện
  year: 2026
  location: TP.HCM & Hà Nội
  lesson: Biến đánh giá Google Maps & tin nhắn Zalo OA thành lịch hẹn tự động, thu 10-20M/tháng/phòng khám, 1 người quản 10 phòng khám đạt 100-200M doanh thu.
  evidence_strength: high (Vault Ref: 04_mo_hinh_aaa_va_local_business.md)
  chapter_fit: Chapter 4

- case_name: Media Engine 1 Người (Sản xuất 30-50 Shorts/tháng cho Chuyên gia)
  year: 2026
  location: Việt Nam
  lesson: 1 người dùng Opus Clip + Descript + Custom GPT xử lý trọn gói Personal Branding cho 5-7 khách hàng với giá 8-15M/khách, chỉ tốn 2h/khách/tuần.
  evidence_strength: high (Vault Ref: 04_mo_hinh_aaa_va_local_business.md)
  chapter_fit: Chapter 4

framework_candidates:
- framework: Công thức Solopreneur AI (1 Người sáng lập + 1 Hệ thống AI Agents + N Đối tác Outsource)
  simplified_explanation: Thay vì nuôi nhân viên full-time, dùng AI làm lực lượng lao động chính và chỉ thuê ngoài chuyên gia cấp cao theo từng đầu việc cụ thể.
  chapter_fit: Chapter 2 & 3

- framework: 3 Bước Nhạc Trưởng AI (Phân rã -> Ủy quyền tác vụ -> Nắn dòng đầu ra)
  simplified_explanation: Kỹ năng điều phối hệ thống AI thay vì gõ prompt bâng quơ.
  chapter_fit: Chapter 5

- framework: Lộ trình 5 Bước Khởi động Cỗ máy 1 Người tại VN
  simplified_explanation: Chọn bài toán có sẵn nhu cầu chi trả -> Đóng gói cỗ máy AI -> Tạo bằng chứng thực tế -> Xây kênh phân phối -> Giữ vững giá trị con người.
  chapter_fit: Chapter 6

weak_zones:
- Cần tránh các con số phóng đại phi thực tế; mọi con số thu nhập đều phải gắn liền với năng lực giải quyết vấn đề và năng lực đóng gói hệ thống thực tế.

claims_to_avoid:
- Tránh tuyên bố "AI sẽ khiến 100% nhân sự mất việc ngay lập tức" (cần giải thích đúng bản chất là thay thế các tác vụ lặp lại giá trị thấp).
- Tránh khuyên người xem bỏ việc ngay khi chưa xây dựng được hệ thống và chưa có khách hàng đầu tiên.

research_verdict: sufficient
notes: Toàn bộ 7 file dữ liệu nghiên cứu chuyên sâu đã được kiểm chứng và lưu trữ tại research_vault/. Sẵn sàng chuyển sang Pha 3 (Strategy Brief).