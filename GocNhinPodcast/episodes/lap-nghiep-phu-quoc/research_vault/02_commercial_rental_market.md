# Báo Cáo 02: Thị Trường Thuê Mặt Bằng Kinh Doanh, Kiot & Shophouse Tại Phú Quốc 2025–2026

> **Mã chủ đề:** `VAULT_PQ_CAREER_02`  
> **Nguồn trích xuất:** Google NotebookLM Master Notebook (`b14b9d2f-6f32-491a-b7dd-c5638817dc71`)  
> **Phương pháp:** Direct RPC Ingestion & Batch Extraction (`notebooklm-py`)  
> **Thời điểm trích xuất:** Tháng 09/2026  

## 1. Yêu Cầu Truy Vấn (Research Prompt)

```text
Mổ xẻ thực trạng thị trường cho thuê mặt bằng thương mại tại Phú Quốc hiện nay:
        1. Mặt bằng kinh doanh nhỏ, kiot chợ, quán ăn ven đường: giá thuê trung bình, biến động giá qua các năm.
        2. Shophouse tại các khu đô thị lớn và mặt tiền các trục đường huyết mạch (ĐT.975, Trần Hưng Đạo, 30/4): giá thuê thực tế, tỷ lệ lấp đầy, các căn bỏ hoang.
        3. Rào cản vốn ban đầu: Quy định về tiền đặt cọc (1-6 tháng), chu kỳ thanh toán (3-6 tháng/lần), chi phí cải tạo hoàn thiện thô.
        4. Rủi ro pháp lý hợp đồng thuê: thời hạn cam kết, điều khoản tăng giá thuê hàng năm, rủi ro thu hồi đất hoặc tranh chấp pháp lý mặt bằng.
```

---

## 2. Báo Cáo Phân Tích & Dữ Liệu Thực Chứng (Grounded Insights)

### 1. Thực trạng mặt bằng kinh doanh quy mô nhỏ và biến động thị trường

Tại Đặc khu Phú Quốc, thị trường mặt bằng bán lẻ quy mô nhỏ (kiot chợ truyền thống, quán ăn ven đường, cửa hàng dịch vụ tự phát) chịu sự phân hóa mạnh mẽ và áp lực cơ cấu rất lớn dưới tác động của các chu kỳ du lịch cũng như khung thể chế quản lý mới [1]:

*   **Giá thuê trung bình:** 
    *   Đối với các hộ kinh doanh cá thể nhỏ lẻ tại các khu vực truyền thống như chợ Dương Đông hoặc các tuyến đường ven trung tâm, giá thuê thực tế dao động từ **8.000.000 đến 15.000.000 VND/tháng** tùy thuộc vào diện tích và mật độ dân cư.
    *   Tại các trục đường huyết mạch thương mại tự do sầm uất của Dương Đông như đường **Trần Hưng Đạo**, giá thuê đất trống thương mại diện tích lớn (từ 1.500 đến 2.000 \\(m^2\\)) cận kề các điểm dịch vụ lớn như Kingkong Mart có giá thuê lên tới **120.000.000 VND/tháng** [2].
    *   Trục đường **30 Tháng 4 (Dương Đông)** có giá đất quy định từ 18 triệu đến 25 triệu VND/\\(m^2\\) [3], đẩy chi phí thuê nhà phố kinh doanh mặt tiền tại đây dao động ổn định từ **40.000.000 đến 70.000.000 VND/tháng** [4].
*   **Biến động giá thuê qua các năm:** 
    *   **Giai đoạn bùng nổ (2022):** Khi Phú Quốc đón lượng khách kỷ lục gần 5 triệu lượt [5], làn sóng tranh giành mặt bằng đẩy giá thuê kiot và cửa hàng nhỏ tăng vọt từ 30% - 50%.
    *   **Giai đoạn chững lại (2023 - 2025):** Sự sụt giảm lượng khách nội địa do rào cản giá vé máy bay quá cao (một số đợt nghỉ lễ ghi nhận lượng khách giảm tới 11% và doanh thu giảm 24% [5, 6]) đã ép biên lợi nhuận của các cửa hàng nhỏ xuống mức tối thiểu, dẫn đến làn sóng trả mặt bằng, cắt lỗ hàng loạt [7, 8].
    *   **Giai đoạn chuẩn hóa (2026):** Việc ban hành **Bảng giá đất mới năm 2026** làm tăng khung thuế sử dụng đất phi nông nghiệp và đơn giá thuê đất công, gián tiếp đẩy giá thuê mặt bằng tư nhân tại trung tâm **tăng từ 15% đến 25%** [3, 9]. Đồng thời, chính quyền đặc khu siết chặt quản lý hộ kinh doanh cá thể, yêu cầu địa chỉ kinh doanh phải hợp pháp, đáp ứng tiêu chuẩn PCCC và bảo vệ môi trường, khiến các mặt hàng lấn chiếm vỉa hè, hành lang biển hoàn toàn bị xóa sổ [9].

---

### 2. Phân tích giá thuê Shophouse tại các trục đường huyết mạch và khu đô thị lớn

Thị trường shophouse Phú Quốc giai đoạn 2025 - 2026 ghi nhận **sự phân cực giá thuê vô cùng khốc liệt** giữa các dự án đô thị mở và các siêu tổ hợp nghỉ dưỡng khép kín (Integrated Resorts) [10, 11]:

| Khu vực / Tuyến đường | Dự án tiêu biểu | Diện tích (\\(m^2\\)) | Giá thuê thực tế (VND/tháng) | Đặc điểm khai thác & Tỷ lệ lấp đầy |
| :--- | :--- | :--- | :--- | :--- |
| **Đường ĐT.975 (An Thới)** | Đại lộ AT (Sun Grand City New An Thới) | 100 - 120 | **15.000.000** [2] | Mức giá khởi điểm dễ thở, chủ yếu khai thác các dịch vụ đô thị mở [10]. Tỷ lệ lấp đầy ở mức trung bình. |
| **Khu đô thị mới An Thới** | Sun Grand City New An Thới | 100 - 150 | **60.000.000** [2] | Shophouse hoàn thiện thông thường. Phục vụ dân cư và tệp khách liên kết khu vực Nam đảo [10]. |
| **The Center (Sunset Town)** | Phân khu Shophouse cao cấp Nam đảo | 120 - 180 | **108.600.000** [2] | Giá thuê kỷ lục nhờ vị trí đắc địa cạnh ga đi cáp treo Hòn Thơm, Cầu Hôn, tháp đồng hồ [12, 13]. Thích hợp làm nhà hàng, spa cao cấp, bar/pub [14, 15]. Tỷ lệ lấp đầy kịch trần. |
| **Grand World (Bắc Đảo)** | Shophouse khu phức hợp không ngủ | 80 - 120 | **30.000.000 - 50.000.000** | Nằm trong quần thể phức hợp khép kín của Vingroup [11]. Thừa hưởng dòng khách all-inclusive đổ về đều đặn [16]. Tỷ lệ lấp đầy tốt ở các trục chính. |

*   **Tỷ lệ lấp đầy và thực trạng phân cực:** Các tổ hợp Integrated Resorts khép kín như Grand World hay Sunset Town kiểm soát chặt chẽ dòng khách bằng hệ sinh thái đưa đón chuyên dụng từ sân bay về nội khu [16]. Toàn bộ dòng tiền chi tiêu của khách được giữ lại bên trong dự án, giúp các dãy shophouse tại đây duy trì tỷ lệ lấp đầy cao [11, 16]. 
*   **Thực trạng "bỏ hoang":** Ngược lại, các shophouse nằm ngoài ranh giới dự án hoặc tại các trục đô thị mới chưa lấp đầy cư dân phải đối mặt với **tỷ lệ lấp đầy thấp, nhiều dãy căn hộ bỏ hoang**. Các chủ mặt bằng tại đây bị cô lập khỏi dòng khách quốc tế chất lượng cao, buộc phải cạnh tranh trong phân khúc khách du lịch bụi có mức chi tiêu thấp, dẫn đến tình trạng suy thoái doanh thu kéo dài [16].

---

### 3. Rào cản vốn ban đầu và áp lực hoàn thiện thô

Việc thiết lập một cơ sở kinh doanh thương mại chính quy tại Phú Quốc đòi hỏi một lượng vốn lưu động ban đầu cực kỳ lớn, tạo thành rào cản gia nhập thị trường đối với các doanh nghiệp vừa và nhỏ:

*   **Áp lực từ quy định đặt cọc và chu kỳ thanh toán:** 
    *   Yêu cầu đặt cọc đối với các mặt bằng shophouse thương mại phổ biến từ **3 đến 6 tháng tiền thuê** [10].
    *   Chu kỳ thanh toán định kỳ thường từ **3 đến 6 tháng một lần** (trả trước) [10].
    *   *Ví dụ thực tế:* Để vận hành một căn shophouse tại phân khu The Center với mức giá thuê trung bình 108,6 triệu VND/tháng [2], doanh nghiệp phải chuẩn bị ít nhất **651.600.000 VND** tiền đặt cọc (6 tháng) và **651.600.000 VND** tiền thanh toán kỳ đầu tiên (6 tháng). Tổng chi phí cố định ban đầu cho mặt bằng đã vượt ngưỡng **1,3 tỷ VND** [10], chưa tính chi phí vận hành.
*   **Chi phí cải tạo hoàn thiện thô chịu ảnh hưởng của "Thuế hải đảo" (Island Tax):** 
    *   Hầu hết shophouse dự án bàn giao cho khách thuê dưới dạng hoàn thiện mặt ngoài và thô hoàn toàn bên trong [17].
    *   Chi phí xây dựng, ngăn vách, lắp đặt hệ thống cơ điện tại Phú Quốc bị đội lên cao do toàn bộ vật tư xây dựng (nhôm xingfa, kính cường lực, thiết bị điện tử) đều phải gánh mức cước vận tải biển từ 1.300 đến 2.100 VND/kg, hoặc chi phí bao xe tải nặng từ Sài Gòn lên tới 19 triệu VND/chuyến [18, 19]. 
    *   Hệ số cộng thêm này đẩy **giá thành hoàn thiện phần thô tại đảo cao hơn đất liền tối thiểu 15% - 20%** [19].

---

### 4. Hệ thống rủi ro pháp lý hợp đồng và tính chất mùa vụ

Bên cạnh áp lực tài chính, các đơn vị vận hành kinh doanh tại Đặc khu Phú Quốc phải đối mặt với hệ rủi ro kép về pháp lý hợp đồng và tính chu kỳ thiên nhiên khắc nghiệt:

*   **Rủi ro từ điều khoản lũy tiến và tăng giá thuê:** Các hợp đồng dài hạn (thường từ 3 - 5 năm) luôn đính kèm điều khoản tăng giá thuê lũy tiến từ **5% - 10% mỗi năm**. Khi bảng giá đất mới năm 2026 đi vào hiệu lực, giá thuê mặt bằng tư nhân có xu hướng bị đẩy vọt theo thị trường tự do [9], đẩy doanh nghiệp vào thế tiến thoái lưỡng nan nếu doanh thu du lịch không tăng trưởng tương xứng.
*   **Rủi ro từ tính chu kỳ thời tiết (Gió mùa Tây Nam):** 
    *   Mùa mưa kéo dài từ tháng 5 đến tháng 10 hàng năm với sóng lớn và mưa bão liên tục thường xuyên làm gián đoạn các đường tàu vượt biển và suy giảm từ **50% đến 70% lượng khách du lịch** [8].
    *   Các cơ sở kinh doanh F&B, cà phê tự phát ven biển rơi vào trạng thái "đóng băng" dòng thu trong khi chi phí cố định (mặt bằng, lương nhân sự cốt cán, bảo trì thiết bị hao mòn do muối biển) vẫn phải chi trả đều đặn [20, 21]. Việc thiếu quỹ dự phòng tài chính tối thiểu 6 tháng đến 1 năm là nguyên nhân cốt lõi khiến các mô hình này **"chết yểu" chỉ sau chưa đầy một năm hoạt động** [9, 21].
*   **Rủi ro thu hồi đất và tranh chấp quy hoạch:** 
    *   Phú Quốc đang đẩy nhanh tiến độ điều chỉnh cục bộ quy hoạch chung đến năm 2040 tại 23 vị trí để sẵn sàng hạ tầng đón sự kiện APEC 2027 [1, 22].
    *   Chính quyền đặc khu đang đồng loạt triển khai lực lượng thực hiện **cưỡng chế thu hồi đất và cưỡng chế khắc phục hậu quả** đối với các trường hợp lấn chiếm hành lang bảo vệ hoặc xây dựng không phép trên đất nông nghiệp, đất rừng (tiêu biểu như các vụ cưỡng chế tại khu phố Bãi Thơm) [23, 24]. 
    *   Nếu doanh nghiệp thuê phải các mặt bằng tự phát, không có giấy phép xây dựng hợp pháp hoặc nằm trong ranh giới đất công lộ giới mở lộ, họ đứng trước nguy cơ **mất trắng toàn bộ chi phí đầu tư cải tạo ban đầu** khi mặt bằng bị thu hồi cưỡng chế [9, 23, 24].

---

Tôi đã cập nhật toàn bộ hệ thống số liệu thực chứng và bảng so sánh giá thuê shophouse này vào bản báo cáo trực quan trong Studio của bạn để tiện theo dõi. 

**📈 Để hỗ trợ bạn xây dựng một kế hoạch kinh doanh an toàn, bạn có muốn tôi thiết kế một mô hình dự toán dòng tiền chạy thử (Financial Run-rate) trong vòng 1 năm cho một shophouse điển hình tại Phú Quốc nhằm tính toán điểm hòa vốn giữa mùa khô và mùa mưa không?**

---

## 3. Danh Mục Nguồn Trích Dẫn Thực Chứng (Citations & Sources)

- **[1] Tài liệu NotebookLM** (Source ID: `dae2b5bb-e931-4fff-9042-e9c078dc31f7`)
- **[2] Tài liệu NotebookLM** (Source ID: `dae2b5bb-e931-4fff-9042-e9c078dc31f7`)
- **[3] Tài liệu NotebookLM** (Source ID: `dae2b5bb-e931-4fff-9042-e9c078dc31f7`)
- **[4] Tài liệu NotebookLM** (Source ID: `dae2b5bb-e931-4fff-9042-e9c078dc31f7`)
- **[5] Tài liệu NotebookLM** (Source ID: `07e268c3-7582-4af7-993e-36df52d747b3`)
- **[6] Tài liệu NotebookLM** (Source ID: `07e268c3-7582-4af7-993e-36df52d747b3`)
- **[7] Tài liệu NotebookLM** (Source ID: `dae2b5bb-e931-4fff-9042-e9c078dc31f7`)
- **[8] Tài liệu NotebookLM** (Source ID: `dae2b5bb-e931-4fff-9042-e9c078dc31f7`)
- **[9] Tài liệu NotebookLM** (Source ID: `dae2b5bb-e931-4fff-9042-e9c078dc31f7`)
- **[10] Tài liệu NotebookLM** (Source ID: `dae2b5bb-e931-4fff-9042-e9c078dc31f7`)
- **[11] Tài liệu NotebookLM** (Source ID: `dae2b5bb-e931-4fff-9042-e9c078dc31f7`)
- **[12] Tài liệu NotebookLM** (Source ID: `5952f22e-36f6-4c8a-b938-9f168931ce32`)
- **[13] Tài liệu NotebookLM** (Source ID: `5952f22e-36f6-4c8a-b938-9f168931ce32`)
- **[14] Tài liệu NotebookLM** (Source ID: `5952f22e-36f6-4c8a-b938-9f168931ce32`)
- **[15] Tài liệu NotebookLM** (Source ID: `5952f22e-36f6-4c8a-b938-9f168931ce32`)
- **[16] Tài liệu NotebookLM** (Source ID: `dae2b5bb-e931-4fff-9042-e9c078dc31f7`)
- **[17] Tài liệu NotebookLM** (Source ID: `5952f22e-36f6-4c8a-b938-9f168931ce32`)
- **[18] Tài liệu NotebookLM** (Source ID: `e3294859-889c-4e18-90bc-9d59b0d6d3c3`)
- **[19] Tài liệu NotebookLM** (Source ID: `dae2b5bb-e931-4fff-9042-e9c078dc31f7`)
- **[20] Tài liệu NotebookLM** (Source ID: `dae2b5bb-e931-4fff-9042-e9c078dc31f7`)
- **[21] Tài liệu NotebookLM** (Source ID: `dae2b5bb-e931-4fff-9042-e9c078dc31f7`)
- **[22] Tài liệu NotebookLM** (Source ID: `6b527c08-891c-4222-ba17-429371cdb29c`)
- **[23] Tài liệu NotebookLM** (Source ID: `71fcd927-71d0-43d5-a7e8-19b92f831ce7`)
- **[24] Tài liệu NotebookLM** (Source ID: `71fcd927-71d0-43d5-a7e8-19b92f831ce7`)
