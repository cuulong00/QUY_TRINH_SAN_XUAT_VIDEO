import React, { useState, useEffect, useRef } from 'react';
import { 
  LayoutDashboard, 
  Calendar as CalendarIcon, 
  BookOpen, 
  Settings, 
  Flame, 
  Trophy, 
  HelpCircle, 
  ArrowRight, 
  Check, 
  ChevronRight, 
  Info,
  RefreshCw,
  Award,
  Layers,
  BookMarked,
  BrainCircuit,
  Lock,
  ChevronLeft,
  X,
  Play,
  CheckCircle2,
  Trash2,
  Bookmark,
  Clock,
  Sparkles,
  TrendingUp,
  FileText,
  AlertCircle,
  CalendarDays,
  ExternalLink,
  Plus,
  Target
} from 'lucide-react';

const API_BASE = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
  ? 'http://localhost:5002/api'
  : `${window.location.origin}/api`;

// Timeline June to April
const MONTHS_MAP = [
  { id: 1, name: 'Tháng 6', label: 'Tháng 6', phase: 'theory', desc: 'Lý thuyết Cơ bản' },
  { id: 2, name: 'Tháng 7', label: 'Tháng 7', phase: 'theory', desc: 'Lý thuyết Trung cấp' },
  { id: 3, name: 'Tháng 8', label: 'Tháng 8', phase: 'theory', desc: 'Lý thuyết Nâng cao' },
  { id: 4, name: 'Tháng 9', label: 'Tháng 9', phase: 'theory', desc: 'Lý thuyết Bứt phá' },
  { id: 5, name: 'Tháng 10', label: 'Tháng 10', phase: 'theory', desc: 'Tổng ôn Chuyên đề' },
  { id: 6, name: 'Tháng 11', label: 'Tháng 11', phase: 'theory', desc: 'Hệ thống hóa & Review' },
  { id: 7, name: 'Tháng 12', label: 'Tháng 12', phase: 'exam', desc: 'Luyện đề cơ bản' },
  { id: 8, name: 'Tháng 1', label: 'Tháng 1 năm sau', phase: 'exam', desc: 'Luyện đề chất lượng cao' },
  { id: 9, name: 'Tháng 2', label: 'Tháng 2 năm sau', phase: 'exam', desc: 'Thử sức đề trường chuyên' },
  { id: 10, name: 'Tháng 3', label: 'Tháng 3 năm sau', phase: 'exam', desc: 'Tổng duyệt & Quét lỗi sai' },
  { id: 11, name: 'Tháng 4', label: 'Tháng 4 năm sau', phase: 'final', desc: 'KỲ THI TUYỂN SINH CHÍNH THỨC' }
];

const CURRICULUM_DISTRIBUTION = {
  1: { // Tháng 6
    1: { id: 1, name: 'Số học & Các phép tính', subject: 'Toán' },
    2: { id: 7, name: 'Luyện từ và câu - Từ vựng', subject: 'Tiếng Việt' },
    3: { id: 12, name: 'Phát âm & Trọng âm', subject: 'Tiếng Anh' }
  },
  2: { // Tháng 7
    1: { id: 2, name: 'Toán tỉ số & Tỉ số phần trăm', subject: 'Toán' },
    2: { id: 8, name: 'Luyện từ và câu - Ngữ pháp', subject: 'Tiếng Việt' },
    3: { id: 13, name: 'Từ vựng theo chủ điểm', subject: 'Tiếng Anh' }
  },
  3: { // Tháng 8
    1: { id: 3, name: 'Toán có lời văn cơ bản', subject: 'Toán' },
    2: { id: 9, name: 'Biện pháp tu từ', subject: 'Tiếng Việt' },
    3: { id: 14, name: 'Ngữ pháp - Thì của động từ', subject: 'Tiếng Anh' }
  },
  4: { // Tháng 9
    1: { id: 4, name: 'Toán chuyển động đều', subject: 'Toán' },
    2: { id: 10, name: 'Đọc hiểu & Cảm thụ văn học', subject: 'Tiếng Việt' },
    3: { id: 15, name: 'Ngữ pháp - Cấu trúc câu', subject: 'Tiếng Anh' }
  },
  5: { // Tháng 10
    1: { id: 5, name: 'Hình học phẳng & Hình khối', subject: 'Toán' },
    2: { id: 11, name: 'Tập làm văn', subject: 'Tiếng Việt' },
    3: { id: 16, name: 'Đọc điền từ & Đọc hiểu', subject: 'Tiếng Anh' }
  },
  6: { // Tháng 11
    1: { id: 6, name: 'Toán tư duy & Logic', subject: 'Toán' },
    2: { id: 11, name: 'Tập làm văn (Tổng ôn)', subject: 'Tiếng Việt' },
    3: { id: 17, name: 'Viết & Biến đổi câu', subject: 'Tiếng Anh' }
  }
};

const WEEKDAYS = [
  { key: 't2', label: 'Thứ 2', desc: 'Toán' },
  { key: 't3', label: 'Thứ 3', desc: 'Anh' },
  { key: 't4', label: 'Thứ 4', desc: 'Văn' },
  { key: 't5', label: 'Thứ 5', desc: 'Toán' },
  { key: 't6', label: 'Thứ 6', desc: 'Anh' },
  { key: 't7', label: 'Thứ 7', desc: 'Văn' },
  { key: 'cn', label: 'Chủ Nhật', desc: 'Tổng ôn' }
];

const formatTime = (seconds) => {
  const m = Math.floor(seconds / 60);
  const s = seconds % 60;
  return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
};

const getFormattedTime = (date) => {
  const hours = date.getHours().toString().padStart(2, '0');
  const minutes = date.getMinutes().toString().padStart(2, '0');
  const seconds = date.getSeconds().toString().padStart(2, '0');
  const dayNames = ['Chủ Nhật', 'Thứ Hai', 'Thứ Ba', 'Thứ Tư', 'Thứ Năm', 'Thứ Sáu', 'Thứ Bảy'];
  const dayName = dayNames[date.getDay()];
  const dd = date.getDate().toString().padStart(2, '0');
  const mm = (date.getMonth() + 1).toString().padStart(2, '0');
  const yyyy = date.getFullYear();
  return `${hours}:${minutes}:${seconds} - ${dayName}, ngày ${dd}/${mm}/${yyyy}`;
};

const LiveClock = () => {
  const [time, setTime] = React.useState(new Date());
  React.useEffect(() => {
    const clockTimer = setInterval(() => {
      setTime(new Date());
    }, 1000);
    return () => clearInterval(clockTimer);
  }, []);

  return (
    <span style={{ fontWeight: 600, fontFamily: 'monospace' }}>
      {getFormattedTime(time)}
    </span>
  );
};

const SUB_TOPICS_MAP = {
  1: [
    { id: 101, name: 'Phân số và các phép tính' },
    { id: 102, name: 'Số thập phân và các phép tính' },
    { id: 103, name: 'Dãy số có quy luật' },
    { id: 104, name: 'Phép tính nhanh, tính thuận tiện' }
  ],
  2: [
    { id: 201, name: 'Toán Tổng - Tỉ, Hiệu - Tỉ' },
    { id: 202, name: 'Tỉ số phần trăm cơ bản' },
    { id: 203, name: 'Bài toán mua bán, lỗ lãi' },
    { id: 204, name: 'Bài toán hạt tươi - hạt khô & dung dịch' }
  ],
  3: [
    { id: 301, name: 'Bài toán tính tuổi' },
    { id: 302, name: 'Bài toán trồng cây' },
    { id: 303, name: 'Bài toán công việc chung (Vòi nước)' },
    { id: 304, name: 'Phương pháp giả thiết tạm & thế' }
  ],
  4: [
    { id: 401, name: 'Đại lượng chuyển động cơ bản (s, v, t)' },
    { id: 402, name: 'Chuyển động cùng chiều & ngược chiều' },
    { id: 403, name: 'Chuyển động trên dòng nước (Xuôi/Ngược)' },
    { id: 404, name: 'Vật chuyển động có chiều dài đáng kể' }
  ],
  5: [
    { id: 501, name: 'Chu vi & Diện tích (Tam giác, hình thang, hình tròn)' },
    { id: 502, name: 'Diện tích & Thể tích hình hộp chữ nhật / hình lập phương' }
  ],
  6: [
    { id: 601, name: 'Toán logic & suy luận' },
    { id: 602, name: 'Nguyên lý Dirichlet' },
    { id: 603, name: 'Toán đếm & tổ hợp đơn giản' }
  ],
  7: [
    { id: 701, name: 'Cấu tạo từ: Từ đơn, từ phức (ghép, láy)' },
    { id: 702, name: 'Nghĩa của từ: Từ đồng nghĩa, trái nghĩa, đồng âm, nhiều nghĩa' },
    { id: 703, name: 'Thành ngữ và tục ngữ Việt Nam' }
  ],
  8: [
    { id: 801, name: 'Từ loại: Danh, động, tính, đại, quan hệ từ' },
    { id: 802, name: 'Thành phần câu: Chủ, vị, trạng ngữ' },
    { id: 803, name: 'Câu ghép & Các cách nối câu ghép' }
  ],
  9: [
    { id: 901, name: 'So sánh & Nhân hóa' },
    { id: 902, name: 'Điệp từ điệp ngữ' },
    { id: 903, name: 'Ẩn dụ & Hoán dụ' }
  ],
  10: [
    { id: 1001, name: 'Đọc hiểu văn bản & Tìm nội dung chính' },
    { id: 1002, name: 'Đoạn văn cảm thụ văn học ngắn' }
  ],
  11: [
    { id: 1101, name: 'Dàn ý & Viết văn tả cảnh' },
    { id: 1102, name: 'Dàn ý & Viết văn tả người' }
  ],
  12: [
    { id: 1201, name: 'Phát âm đuôi -ed và -s/-es' },
    { id: 1202, name: 'Trọng âm từ có 2 & 3 âm tiết' }
  ],
  13: [
    { id: 1301, name: 'Từ vựng: School, Family, Friends' },
    { id: 1302, name: 'Từ vựng: Jobs, Hobbies, Sports' },
    { id: 1303, name: 'Từ vựng: Food, Animals, Health' }
  ],
  14: [
    { id: 1401, name: 'Hiện tại đơn & Hiện tại tiếp diễn' },
    { id: 1402, name: 'Quá khứ đơn & Quá khứ tiếp diễn' },
    { id: 1403, name: 'Hiện tại hoàn thành' },
    { id: 1404, name: 'Tương lai đơn & Tương lai gần' }
  ],
  15: [
    { id: 1501, name: 'So sánh hơn & So sánh nhất' },
    { id: 1502, name: 'Câu điều kiện loại 0 & Loại 1' },
    { id: 1503, name: 'Câu bị động cơ bản' },
    { id: 1504, name: 'Động từ khuyết thiếu' }
  ],
  16: [
    { id: 1601, name: 'Đọc điền từ (Cloze test)' },
    { id: 1602, name: 'Đọc hiểu trả lời câu hỏi ngắn' }
  ],
  17: [
    { id: 1701, name: 'Viết lại câu (Sentence transformation)' },
    { id: 1702, name: 'Sắp xếp từ xáo trộn thành câu (Reordering)' }
  ]
};

const DEFAULT_RECALL_CARDS = [
  // Toán Chương 1
  { id: 1001, chapter_id: 1, sub_topic_id: 101, front_content: 'Tính nhanh: 3/4 + 1/5 + 1/4 + 4/5', back_content: 'Gộp các phân số cùng mẫu:\n(3/4 + 1/4) + (1/5 + 4/5) = 1 + 1 = 2.', hint: 'Nhóm các phân số có mẫu số giống nhau.', subject_id: 1, box_number: 1 },
  { id: 1002, chapter_id: 1, sub_topic_id: 102, front_content: 'Tìm X: X x 1.2 + X x 1.8 = 15', back_content: 'Áp dụng tính chất phân phối:\nX x (1.2 + 1.8) = 15\nX x 3 = 15\nX = 15 / 3 = 5.', hint: 'Đặt X ra làm nhân tử chung.', subject_id: 1, box_number: 1 },
  { id: 1003, chapter_id: 1, sub_topic_id: 103, front_content: 'Tính tổng dãy số: 1 + 3 + 5 + ... + 19', back_content: 'Số số hạng: (19 - 1) / 2 + 1 = 10 số.\nTổng = (19 + 1) x 10 / 2 = 100.', hint: 'Áp dụng công thức tính tổng dãy số cách đều.', subject_id: 1, box_number: 1 },
  { id: 1004, chapter_id: 1, sub_topic_id: 104, front_content: 'Tính nhanh: 12.5 x 8.8', back_content: 'Tách 8.8 = 8 x 1.1\n12.5 x 8 x 1.1 = 100 x 1.1 = 110.', hint: 'Số 12.5 nhân với 8 sẽ ra số tròn trăm.', subject_id: 1, box_number: 1 },

  // Toán Chương 2
  { id: 1005, chapter_id: 2, sub_topic_id: 201, front_content: 'Tổng của hai số là 80, tỉ số của chúng là 3/5. Tìm hai số đó.', back_content: 'Tổng số phần bằng nhau: 3 + 5 = 8 phần.\nSố bé: 80 / 8 x 3 = 30.\nSố lớn: 80 - 30 = 50.', hint: 'Tìm tổng số phần bằng nhau trước.', subject_id: 1, box_number: 1 },
  { id: 1006, chapter_id: 2, sub_topic_id: 202, front_content: 'Một chiếc áo giá 200.000đ được giảm giá 15%. Hỏi giá sau giảm là bao nhiêu?', back_content: 'Số tiền được giảm: 200.000 x 15% = 30.000đ.\nGiá sau giảm: 200.000 - 30.000 = 170.000đ.', hint: 'Tính số tiền giảm trước hoặc tính phần trăm còn lại.', subject_id: 1, box_number: 1 },
  { id: 1007, chapter_id: 2, sub_topic_id: 203, front_content: 'Mua 100.000đ bán 125.000đ. Hỏi lãi bao nhiêu phần trăm so với vốn?', back_content: 'Số tiền lãi: 125.000 - 100.000 = 25.000đ.\nTỉ lệ lãi so với vốn: 25.000 / 100.000 x 100% = 25%.', hint: 'Lấy tiền lãi chia cho tiền vốn.', subject_id: 1, box_number: 1 },
  { id: 1008, chapter_id: 2, sub_topic_id: 204, front_content: 'Tỉ lệ nước trong hạt tươi là 20%, hạt khô là 10%. Hỏi 180kg hạt tươi thu được bao nhiêu kg hạt khô?', back_content: 'Lượng chất khô trong hạt tươi là: 180 x (100% - 20%) = 144kg.\nKhối lượng hạt khô thu được: 144 / (100% - 10%) = 160kg.', hint: 'Khối lượng chất khô không thay đổi trước và sau khi phơi.', subject_id: 1, box_number: 1 },

  // Toán Chương 3
  { id: 1009, chapter_id: 3, sub_topic_id: 301, front_content: 'Hiện nay mẹ 30 tuổi, con 6 tuổi. Hỏi sau bao nhiêu năm nữa tuổi mẹ gấp 3 lần tuổi con?', back_content: 'Hiệu số tuổi luôn không đổi: 30 - 6 = 24 tuổi.\nKhi tuổi mẹ gấp 3 lần tuổi con, hiệu số phần là: 3 - 1 = 2 phần.\nTuổi con lúc đó: 24 / 2 = 12 tuổi.\nSố năm cần tìm: 12 - 6 = 6 năm.', hint: 'Nhớ rằng hiệu số tuổi của hai mẹ con không thay đổi theo thời gian.', subject_id: 1, box_number: 1 },
  { id: 1010, chapter_id: 3, sub_topic_id: 302, front_content: 'Một đường thẳng dài 100m, trồng cây hai đầu đường, khoảng cách giữa 2 cây là 5m. Tính số cây trồng được.', back_content: 'Số cây = (Chiều dài / Khoảng cách) + 1\nSố cây = (100 / 5) + 1 = 21 cây.', hint: 'Trồng ở hai đầu đường thì số cây nhiều hơn số khoảng cách là 1.', subject_id: 1, box_number: 1 },
  { id: 1011, chapter_id: 3, sub_topic_id: 303, front_content: 'Vòi A chảy đầy bể mất 4 giờ, vòi B mất 6 giờ. Hỏi cả hai vòi cùng chảy mất bao lâu?', back_content: '1 giờ vòi A chảy: 1/4 bể. 1 giờ vòi B chảy: 1/6 bể.\n1 giờ cả hai chảy: 1/4 + 1/6 = 5/12 bể.\nThời gian đầy bể: 1 / (5/12) = 2.4 giờ (2 giờ 24 phút).', hint: 'Tính lượng nước mỗi vòi chảy được trong 1 giờ.', subject_id: 1, box_number: 1 },
  { id: 1033, chapter_id: 3, sub_topic_id: 304, front_content: 'Vừa gà vừa chó có 36 con, 100 chân. Hỏi có bao nhiêu con gà, bao nhiêu con chó?', back_content: 'Giả sử tất cả 36 con đều là gà. Số chân là: 36 x 2 = 72 chân. Số chân thiếu so với thực tế: 100 - 72 = 28 chân. Số con chó: 28 / (4 - 2) = 14 con. Số con gà: 36 - 14 = 22 con.', hint: 'Áp dụng phương pháp giả thiết tạm: giả sử tất cả đều là gà.', subject_id: 1, box_number: 1 },

  // Toán Chương 4
  { id: 1012, chapter_id: 4, sub_topic_id: 401, front_content: 'Xe máy đi từ A lúc 7 giờ và đến B lúc 9h30 với vận tốc 40km/h. Tính quãng đường AB.', back_content: 'Thời gian đi: 9h30 - 7h = 2.5 giờ.\nQuãng đường AB: 40 x 2.5 = 100 km.', hint: 's = v x t. Đổi 2 giờ 30 phút thành 2.5 giờ.', subject_id: 1, box_number: 1 },
  { id: 1034, chapter_id: 4, sub_topic_id: 402, front_content: 'Hai xe cùng xuất phát lúc 7 giờ từ A và B cách nhau 120km, đi ngược chiều nhau. Xe 1 đi từ A với v = 35km/h, xe 2 đi từ B với v = 25km/h. Hỏi hai xe gặp nhau lúc mấy giờ?', back_content: 'Tổng vận tốc hai xe: 35 + 25 = 60 km/h. Thời gian đi để gặp nhau: 120 / 60 = 2 giờ. Thời điểm gặp nhau: 7 + 2 = 9 giờ.', hint: 'Thời gian gặp nhau = Khoảng cách / Tổng vận tốc.', subject_id: 1, box_number: 1 },
  { id: 1013, chapter_id: 4, sub_topic_id: 403, front_content: 'Cano đi xuôi dòng nước có vận tốc 25km/h, vận tốc dòng nước là 3km/h. Tính vận tốc thực của cano.', back_content: 'Vận tốc thực = Vận tốc xuôi dòng - Vận tốc dòng nước\nVận tốc thực = 25 - 3 = 22 km/h.', hint: 'Vận tốc xuôi dòng bằng vận tốc thực cộng vận tốc dòng nước.', subject_id: 1, box_number: 1 },
  { id: 1035, chapter_id: 4, sub_topic_id: 404, front_content: 'Một tàu hỏa dài 150m đi qua một cây cầu dài 450m với vận tốc 36 km/h. Hỏi tàu hỏa đi qua cầu mất bao nhiêu giây?', back_content: 'Đổi 36 km/h = 10 m/s. Quãng đường tàu hỏa đi được để qua hết cầu: 150 + 450 = 600m. Thời gian tàu hỏa đi qua cầu: 600 / 10 = 60 giây (1 phút).', hint: 'Quãng đường đi được bằng chiều dài tàu cộng với chiều dài cầu.', subject_id: 1, box_number: 1 },

  // Toán Chương 5
  { id: 1015, chapter_id: 5, sub_topic_id: 501, front_content: 'Tính diện tích hình thang có đáy lớn 12cm, đáy bé 8cm và chiều cao 6cm.', back_content: 'S = (12 + 8) x 6 / 2 = 60 cm².', hint: 'S = (đáy lớn + đáy bé) x chiều cao / 2', subject_id: 1, box_number: 1 },
  { id: 1016, chapter_id: 5, sub_topic_id: 502, front_content: 'Thể tích của hình lập phương có cạnh 4cm là bao nhiêu?', back_content: 'V = 4 x 4 x 4 = 64 cm³.', hint: 'V = cạnh x cạnh x cạnh', subject_id: 1, box_number: 1 },

  // Toán Chương 6
  { id: 1017, chapter_id: 6, sub_topic_id: 601, front_content: 'Có 5 quả bóng đỏ và 4 quả bóng xanh. Cần bốc ít nhất bao nhiêu quả để chắc chắn có 2 quả cùng màu?', back_content: 'Có 2 màu (đỏ và xanh).\nTheo Dirichlet, bốc 3 quả sẽ chắc chắn có ít nhất 2 quả cùng màu.', hint: 'Áp dụng nguyên lý Dirichlet.', subject_id: 1, box_number: 1 },
  { id: 1036, chapter_id: 6, sub_topic_id: 602, front_content: 'Trong một lớp học có 37 học sinh. Chứng minh rằng có ít nhất 4 học sinh có cùng tháng sinh.', back_content: 'Một năm có 12 tháng sinh. Ta chia 37 học sinh cho 12 tháng: 37 = 3 x 12 + 1. Theo nguyên lý Dirichlet, phải có ít nhất 4 học sinh có cùng tháng sinh.', hint: 'Áp dụng nguyên lý Dirichlet: Lấy số học sinh chia cho số tháng sinh.', subject_id: 1, box_number: 1 },
  { id: 1037, chapter_id: 6, sub_topic_id: 603, front_content: 'Từ các chữ số 1, 2, 3 có thể lập được bao nhiêu số tự nhiên có 3 chữ số khác nhau?', back_content: 'Chữ số hàng trăm có 3 cách chọn, chữ số hàng chục có 2 cách chọn (khác chữ số hàng trăm), chữ số hàng đơn vị có 1 cách chọn. Số các số lập được: 3 x 2 x 1 = 6 số.', hint: 'Dùng quy tắc nhân chọn số từng hàng từ trăm đến đơn vị.', subject_id: 1, box_number: 1 },

  // Tiếng Việt Chương 7
  { id: 1018, chapter_id: 7, sub_topic_id: 701, front_content: 'Từ "xinh xắn" là từ ghép hay từ láy?', back_content: 'Là từ láy bộ phận vần (lặp lại âm đầu "x" và vần gần giống nhau).', hint: 'Xem hai tiếng có quan hệ âm thanh hay không.', subject_id: 2, box_number: 1 },
  { id: 1019, chapter_id: 7, sub_topic_id: 702, front_content: 'Xác định nghĩa của từ "chạy" trong câu: "Nhà này chạy ăn từng bữa."', back_content: 'Nghĩa chuyển: Hoạt động lo toan, xoay xở khẩn trương để có được thứ cần thiết.', hint: 'Từ "chạy" ở đây không chỉ hoạt động của chân.', subject_id: 2, box_number: 1 },
  { id: 1038, chapter_id: 7, sub_topic_id: 703, front_content: 'Giải thích ý nghĩa câu tục ngữ: "Ăn quả nhớ kẻ trồng cây".', back_content: 'Khuyên răn chúng ta phải có lòng biết ơn đối với những người đã có công lao tạo dựng nên thành quả mà chúng ta đang được hưởng thụ ngày hôm nay.', hint: 'Qủa là thành quả được hưởng, kẻ trồng cây là người tạo ra nó.', subject_id: 2, box_number: 1 },

  // Tiếng Việt Chương 8
  { id: 1020, chapter_id: 8, sub_topic_id: 801, front_content: 'Trong câu: "Em rất thích học Tiếng Việt.", từ "thích" thuộc từ loại nào?', back_content: 'Thuộc từ loại: Động từ (chỉ trạng thái tâm lý).', hint: 'Từ chỉ cảm xúc, mong muốn là động từ chỉ trạng thái.', subject_id: 2, box_number: 1 },
  { id: 1021, chapter_id: 8, sub_topic_id: 802, front_content: 'Tìm chủ ngữ trong câu: "Dưới bóng tre xanh, ta gìn giữ một nền văn hóa lâu đời."', back_content: 'Chủ ngữ là "ta".\n"Dưới bóng tre xanh" là trạng ngữ chỉ nơi chốn.', hint: 'Chủ ngữ thực hiện hành động "gìn giữ".', subject_id: 2, box_number: 1 },
  { id: 1039, chapter_id: 8, sub_topic_id: 803, front_content: 'Xác định cặp quan hệ từ và quan hệ ý nghĩa trong câu ghép: "Mặc dù trời mưa to nhưng các em vẫn đến trường đúng giờ."', back_content: 'Cặp quan hệ từ: "Mặc dù ... nhưng ...". Quan hệ ý nghĩa: Quan hệ tương phản.', hint: 'Chú ý từ "Mặc dù" ở vế 1 và "nhưng" ở vế 2.', subject_id: 2, box_number: 1 },

  // Tiếng Việt Chương 9
  { id: 1022, chapter_id: 9, sub_topic_id: 901, front_content: 'Xác định biện pháp tu từ trong câu: "Trẻ em như búp trên cành."', back_content: 'Biện pháp: So sánh (so sánh trẻ em với búp trên cành qua từ "như").', hint: 'Có từ so sánh "như".', subject_id: 2, box_number: 1 },
  { id: 1040, chapter_id: 9, sub_topic_id: 902, front_content: 'Chỉ ra và nêu tác dụng của biện pháp điệp ngữ trong câu thơ: "Tre giữ làng, giữ nước, giữ mái nhà tranh, giữ đồng lúa chín."', back_content: 'Điệp từ: "giữ". Tác dụng: Nhấn mạnh vai trò bảo vệ, chở che kiên cường, bền bỉ của cây tre đối với cuộc sống của người dân Việt Nam.', hint: 'Từ nào được lặp lại nhiều lần liên tiếp?', subject_id: 2, box_number: 1 },
  { id: 1041, chapter_id: 9, sub_topic_id: 903, front_content: 'Xác định biện pháp tu từ trong câu: "Thuyền về có nhớ bến chăng / Bến thì một dạ khăng khăng đợi thuyền."', back_content: 'Biện pháp tu từ: Nhân hóa ("bến" biết mong nhớ, đợi chờ) và ẩn dụ ("thuyền" chỉ người đi xa, "bến" chỉ người ở lại chung thủy).', hint: 'Thuyền và bến được gán cho những cảm xúc nào của con người?', subject_id: 2, box_number: 1 },

  // Tiếng Việt Chương 10
  { id: 1023, chapter_id: 10, sub_topic_id: 1001, front_content: 'Đọc câu thơ: "Quê hương là chùm khế ngọt / Cho con trèo hái mỗi ngày". Tác giả so sánh Quê hương với gì và có ý nghĩa gì?', back_content: 'Tác giả so sánh Quê hương với "chùm khế ngọt", gợi tả sự gần gũi, ngọt ngào, giản dị của gia đình và đất nước gắn liền với tuổi thơ.', hint: 'Gợi tả cảm giác thân thuộc của tuổi thơ.', subject_id: 2, box_number: 1 },
  { id: 1042, chapter_id: 10, sub_topic_id: 1002, front_content: 'Trong câu: "Ôi Tổ quốc, ta yêu như xương thịt / Như mẹ cha ta, như vợ như chồng", tác giả dùng biện pháp so sánh nhằm mục đích gì?', back_content: 'Tác giả dùng phép so sánh liên tiếp để biểu lộ tình yêu Tổ quốc thiêng liêng, gắn bó sâu sắc, máu thịt như những tình cảm ruột thịt, gần gũi nhất.', hint: 'So sánh Tổ quốc với xương thịt, mẹ cha, vợ chồng.', subject_id: 2, box_number: 1 },

  // Tiếng Việt Chương 11
  { id: 1024, chapter_id: 11, sub_topic_id: 1101, front_content: 'Nêu các phần chính của dàn ý bài văn tả cảnh.', back_content: '1. Mở bài: Giới thiệu cảnh định tả.\n2. Thân bài: Tả bao quát rồi tả chi tiết theo trình tự thời gian/không gian.\n3. Kết bài: Nêu cảm nghĩ về cảnh vật.', hint: 'Văn miêu tả luôn có bố cục 3 phần.', subject_id: 2, box_number: 1 },
  { id: 1043, chapter_id: 11, sub_topic_id: 1102, front_content: 'Khi tả ngoại hình một người, em nên lựa chọn những chi tiết như thế nào?', back_content: 'Nên chọn lọc những chi tiết tiêu biểu, đặc sắc nhất của người đó (như ánh mắt, nụ cười, mái tóc, bàn tay...) để vừa gợi tả ngoại hình vừa làm nổi bật tính cách.', hint: 'Tránh tả tràn lan mà hãy chọn những nét riêng biệt.', subject_id: 2, box_number: 1 },

  // Tiếng Anh Chương 12
  { id: 1025, chapter_id: 12, sub_topic_id: 1201, front_content: 'Từ "watched" có phát âm đuôi -ed là gì?', back_content: '/t/ vì kết thúc bằng âm vô thanh /tʃ/.', hint: 'Phát âm là /t/ sau các âm vô thanh như ch, sh, p, k, f, s.', subject_id: 3, box_number: 1 },
  { id: 1026, chapter_id: 12, sub_topic_id: 1202, front_content: 'Trọng âm chính của từ "beautiful" rơi vào âm tiết thứ mấy?', back_content: 'Âm tiết thứ nhất (BEAU-ti-ful).', hint: 'Từ 3 âm tiết có hậu tố -ful thường nhấn âm 1.', subject_id: 3, box_number: 1 },

  // Tiếng Anh Chương 13
  { id: 1027, chapter_id: 13, sub_topic_id: 1301, front_content: 'Dịch sang tiếng Anh: "môn Lịch sử", "môn Địa lý", "môn Khoa học".', back_content: 'History, Geography, Science.', hint: 'Subject names.', subject_id: 3, box_number: 1 },
  { id: 1044, chapter_id: 13, sub_topic_id: 1302, front_content: 'Dịch sang tiếng Anh các từ chỉ nghề nghiệp sau: "bác sĩ thú y", "kiến trúc sư", "kế toán".', back_content: '- Bác sĩ thú y: veterinarian (hoặc vet)\n- Kiến trúc sư: architect\n- Kế toán: accountant', hint: 'Kiến trúc sư bắt đầu bằng chữ "a".', subject_id: 3, box_number: 1 },
  { id: 1045, chapter_id: 13, sub_topic_id: 1303, front_content: 'Dịch sang tiếng Anh các từ sau: "sốt", "đau họng", "chế độ ăn uống cân đối".', back_content: '- Sốt: fever\n- Đau họng: sore throat\n- Chế độ ăn uống cân đối: balanced diet', hint: 'Sore throat là đau họng.', subject_id: 3, box_number: 1 },

  // Tiếng Anh Chương 14
  { id: 1028, chapter_id: 14, sub_topic_id: 1401, front_content: 'Chia động từ: "He (write) a book since 2024."', back_content: 'has been writing (hoặc has written) - Hiện tại hoàn thành.', hint: 'Có từ "since".', subject_id: 3, box_number: 1 },
  { id: 1046, chapter_id: 14, sub_topic_id: 1402, front_content: 'Chia động từ trong ngoặc: "When I arrived home, my family (have) dinner."', back_content: 'was having (hoặc were having)\nGiải thích: Diễn tả một hành động đang diễn ra tại thời điểm đó trong quá khứ.', hint: 'Hành động đang diễn ra tại một thời điểm xác định.', subject_id: 3, box_number: 1 },
  { id: 1047, chapter_id: 14, sub_topic_id: 1403, front_content: 'Chọn giới từ đúng: "I have lived in Hanoi ... 5 years." (for / since)', back_content: 'for\nGiải thích: Dùng "for" trước một khoảng thời gian (5 years). Dùng "since" trước mốc thời gian.', hint: '"5 years" là một khoảng thời gian.', subject_id: 3, box_number: 1 },
  { id: 1048, chapter_id: 14, sub_topic_id: 1404, front_content: 'Chia động từ trong ngoặc: "We (visit) our grandparents this weekend. We already bought the bus tickets."', back_content: 'are going to visit (hoặc are visiting)\nGiải thích: Hành động có kế hoạch, dự định rõ ràng từ trước và có bằng chứng (bought tickets).', hint: 'Sử dụng cấu trúc tương lai gần (be going to).', subject_id: 3, box_number: 1 },

  // Tiếng Anh Chương 15
  { id: 1029, chapter_id: 15, sub_topic_id: 1501, front_content: 'Viết dạng so sánh hơn của "bad" và "good".', back_content: 'bad -> worse\ngood -> better.', hint: 'Dạng so sánh bất quy tắc.', subject_id: 3, box_number: 1 },
  { id: 1030, chapter_id: 15, sub_topic_id: 1502, front_content: 'Chuyển sang bị động: "She cleans the room every day."', back_content: 'The room is cleaned by her every day.', hint: 'Hiện tại đơn chuyển sang bị động dùng am/is/are + V3.', subject_id: 3, box_number: 1 },
  { id: 1049, chapter_id: 15, sub_topic_id: 1503, front_content: 'Chuyển sang câu bị động: "The fire destroyed the building yesterday."', back_content: 'The building was destroyed by the fire yesterday.', hint: 'Quá khứ đơn bị động dùng was/were + V3.', subject_id: 3, box_number: 1 },
  { id: 1050, chapter_id: 15, sub_topic_id: 1504, front_content: 'Điền từ khuyết: "You ... touch that wire. It is very dangerous." (mustn\'t / needn\'t / don\'t have to)', back_content: 'mustn\'t\nGiải thích: Chỉ sự cấm đoán, không được phép làm vì có nguy hiểm.', hint: 'Mang tính chất cấm vì nguy hiểm đến tính mạng.', subject_id: 3, box_number: 1 },

  // Tiếng Anh Chương 16
  { id: 1031, chapter_id: 16, sub_topic_id: 1601, front_content: 'Chọn từ điền vào chỗ trống: "She is interested ... reading books." (on/in/at)', back_content: 'Đáp án: "in" (cấu trúc be interested in).', hint: 'Giới từ đi với interested.', subject_id: 3, box_number: 1 },
  { id: 1051, chapter_id: 16, sub_topic_id: 1602, front_content: 'Đọc câu sau và điền từ thích hợp vào câu trả lời: "Although English is widely spoken, Chinese has the most native speakers." -> Question: Which language has more native speakers, English or Chinese? -> Answer: ...', back_content: 'Chinese (Tiếng Trung Quốc).', hint: 'Xem thông tin vế sau của câu.', subject_id: 3, box_number: 1 },

  // Tiếng Anh Chương 17
  { id: 1032, chapter_id: 17, sub_topic_id: 1701, front_content: 'Viết lại câu: "Although it rained heavily, they went to school." -> "In spite of..."', back_content: 'In spite of the heavy rain, they went to school.', hint: 'In spite of + danh từ/cụm danh từ.', subject_id: 3, box_number: 1 },
  { id: 1052, chapter_id: 17, sub_topic_id: 1702, front_content: 'Sắp xếp các từ sau thành câu đúng: "she / because / tired / went / bed / early / was / to / she"', back_content: 'She went to bed early because she was tired.', hint: 'Mệnh đề kết quả trước, "because" nối mệnh đề nguyên nhân.', subject_id: 3, box_number: 1 }
];

const MOTIVATIONAL_QUOTES = [
  "\"Học từ ngày hôm qua, sống cho ngày hôm nay, hy vọng cho ngày mai. Điều quan trọng nhất là không ngừng học hỏi.\" — Albert Einstein 🌸",
  "\"Cuộc sống không phải để sợ hãi, mà là để hiểu. Đây là lúc chúng ta cần hiểu nhiều hơn để bớt sợ hãi đi.\" — Marie Curie 🦄",
  "\"Thiên tài chỉ có 1% là cảm hứng bẩm sinh, còn 99% là sự kiên trì nỗ lực mỗi ngày.\" — Thomas Edison 💡",
  "\"Mọi ước mơ đều có thể trở thành hiện thực nếu con có đủ can đảm để kiên trì theo đuổi.\" — Walt Disney 🎀",
  "\"Tương lai thuộc về những ai tin tưởng vào vẻ đẹp của những ước mơ.\" — Eleanor Roosevelt ✨",
  "\"Chúng ta có thể đạt được mọi mục tiêu của cuộc sống nếu chúng ta kiên trì theo đuổi đủ lâu.\" — Helen Keller 🌟",
  "\"Hành trình vạn dặm để chinh phục ước mơ luôn khởi đầu từ những bước học tập nhỏ bé mỗi ngày.\" — Khổng Tử 📚"
];

const getDailyQuote = () => {
  const day = new Date().getDay(); // 0 (CN), 1 (T2), ..., 6 (T7)
  const idx = day === 0 ? 6 : day - 1;
  return MOTIVATIONAL_QUOTES[idx];
};
const isCoreTopic = (item) => {
  if (!item) return false;
  const name = (item.name || '').toLowerCase();
  const sub = (item.sub_chapter || '').toLowerCase();
  const parent = (item.parent_chapter || '').toLowerCase();
  const title = (item.title_vn || '').toLowerCase();

  // English core topics (subject_id 3)
  if (item.subject_id === 3) {
    return (
      // 1. Tenses (Các thì)
      name.includes('tenses') || title.includes('thì') ||
      // 2. Passive (Bị động)
      name.includes('passive') || title.includes('bị động') ||
      // 3. Comparisons (So sánh)
      name.includes('comparison') || title.includes('so sánh') ||
      // 4. Conditionals & Wish (Điều kiện & Ước)
      name.includes('conditional') || title.includes('điều kiện') || title.includes('câu ước') ||
      // 5. Relative Clauses & Noun/Adverbial Clauses (Mệnh đề quan hệ, danh ngữ, trạng ngữ)
      name.includes('relative') || name.includes('clauses') || title.includes('quan hệ') || title.includes('mệnh đề') ||
      // 6. Prepositions (Giới từ)
      name.includes('preposition') || title.includes('giới từ') ||
      // 7. Reported Speech (Tường thuật)
      name.includes('reported') || title.includes('tường thuật') || title.includes('gián tiếp') ||
      // 8. Tag Questions (Câu hỏi đuôi)
      name.includes('tag') || title.includes('câu hỏi đuôi') ||
      // 9. Gerund & Infinitive (Danh động từ & Động từ nguyên mẫu)
      name.includes('infinitive') || name.includes('-ing form') || title.includes('danh động từ') || title.includes('nguyên thể') ||
      // 10. Conjunctions & Linking words (Liên từ)
      name.includes('linking') || name.includes('conjunction') || title.includes('liên từ') ||
      // 11. Word formation & Word forms (Cấu trúc từ / Loại từ)
      name.includes('formation') || title.includes('loại từ') || name.includes('word form') ||
      // 12. Writing (Viết & Biến đổi câu)
      parent.includes('writing') || name.includes('writing') || name.includes('transformation') || title.includes('viết lại câu') ||
      // 13. Reading Comprehension (Đọc hiểu)
      parent.includes('reading') || title.includes('đọc hiểu')
    );
  }

  // Math core topics (subject_id 1)
  if (item.subject_id === 1) {
    return (
      name.includes('chuyển động') ||
      name.includes('tỉ số') ||
      name.includes('phần trăm') ||
      name.includes('tuổi') ||
      name.includes('công việc') ||
      name.includes('diện tích') ||
      name.includes('chia hết') ||
      name.includes('dãy số') ||
      name.includes('tổng hiệu') ||
      title.includes('chuyển động') ||
      title.includes('tỉ số') ||
      title.includes('phần trăm') ||
      title.includes('tuổi') ||
      title.includes('diện tích') ||
      title.includes('chia hết') ||
      title.includes('dãy số') ||
      title.includes('tính nhanh')
    );
  }

  // Vietnamese core topics (subject_id 2)
  if (item.subject_id === 2) {
    return (
      name.includes('từ ghép') ||
      name.includes('từ láy') ||
      name.includes('từ loại') ||
      name.includes('biện pháp tu từ') ||
      name.includes('câu ghép') ||
      name.includes('đọc hiểu') ||
      name.includes('cảm thụ') ||
      name.includes('miêu tả') ||
      title.includes('từ ghép') ||
      title.includes('từ láy') ||
      title.includes('từ loại') ||
      title.includes('tu từ') ||
      title.includes('câu ghép') ||
      title.includes('đọc hiểu') ||
      title.includes('cảm thụ') ||
      title.includes('miêu tả')
    );
  }

  return false;
};

export default function App() {

  const [activeTab, setActiveTab] = useState('overview');
  const [subjects, setSubjects] = useState([]);
  const [chapters, setChapters] = useState([]);
  const [dueCards, setDueCards] = useState([]);
  const [dueChapters, setDueChapters] = useState([]);
  const [selectedSubjectId, setSelectedSubjectId] = useState(1);
  const [selectedParentChapter, setSelectedParentChapter] = useState('');
  const [topicSearchQuery, setTopicSearchQuery] = useState('');
  const [showCoreOnly, setShowCoreOnly] = useState(false);
  const [activePracticeTopic, setActivePracticeTopic] = useState(null);
  const [practiceTimer, setPracticeTimer] = useState(0);
  const [allCards, setAllCards] = useState([]);
  const [expandedChapters, setExpandedChapters] = useState({});
  const [viewingSubTopic, setViewingSubTopic] = useState(null);
  const [viewingTheoryTopic, setViewingTheoryTopic] = useState(null);

  const [stats, setStats] = useState({
    streak_days: 0,
    total_score: 0,
    total_cards: 0,
    due_cards: 0,
    total_reviews: 0
  });

  const [isOnline, setIsOnline] = useState(true);

  // Active Recall Study Session State
  const [studySession, setStudySession] = useState(null); // { cards: [], currentIndex: 0, showAnswer: false, startTime: null }
  const [sessionCompleted, setSessionCompleted] = useState(false);
  const [xpGained, setXpGained] = useState(0);

  // Focus Mode Pomodoro States
  const [pomodoroTime, setPomodoroTime] = useState(1500); // 25 minutes
  const [pomodoroActive, setPomodoroActive] = useState(false);
  const pomodoroInterval = useRef(null);

  // AI Generation States
  const [aiText, setAiText] = useState('');
  const [aiSubjectId, setAiSubjectId] = useState(1);
  const [aiChapterId, setAiChapterId] = useState(1);
  const [aiCount, setAiCount] = useState(5);
  const [aiLoading, setAiLoading] = useState(false);
  const [aiGeneratedCards, setAiGeneratedCards] = useState([]);

  // Manual Card Creation States
  const [newCard, setNewCard] = useState({
    subject_id: 1,
    chapter_id: 1,
    sub_topic_id: 101,
    front_content: '',
    back_content: '',
    hint: ''
  });

  // Practice Exam Logs States
  const [exams, setExams] = useState(() => {
    const cached = localStorage.getItem('recallkid_exams');
    return cached ? JSON.parse(cached) : [
      { id: 1, name: 'Đề thi thử Lương Thế Vinh lần 1', subject_id: 1, score: 8.5, date: '2026-06-01' },
      { id: 2, name: 'Đề thi thử Nguyễn Tất Thành lần 1', subject_id: 3, score: 9.0, date: '2026-06-10' }
    ];
  });
  const [newExam, setNewExam] = useState({
    name: '',
    subject_id: 1,
    score: '',
    date: new Date().toISOString().split('T')[0]
  });

  // Mistake logger states
  const [mistakeCard, setMistakeCard] = useState({
    exam_name: '',
    subject_id: 1,
    chapter_id: 1,
    sub_topic_id: 101,
    front_content: '',
    back_content: '',
    hint: ''
  });

  // Timeline June to April State
  const [currentMonthIndex, setCurrentMonthIndex] = useState(1); // 1 to 11 (June = 1, April = 11)
  const [currentWeekIndex, setCurrentWeekIndex] = useState(1); // 1 to 4
  const [selectedDayKey, setSelectedDayKey] = useState('t2'); // t2, t3...

  // Track completed study items on TAK12
  const [completedLessons, setCompletedLessons] = useState(() => {
    const cached = localStorage.getItem('recallkid_completed_lessons');
    return cached ? JSON.parse(cached) : {};
  });

  useEffect(() => {
    localStorage.setItem('recallkid_completed_lessons', JSON.stringify(completedLessons));
  }, [completedLessons]);

  useEffect(() => {
    localStorage.setItem('recallkid_exams', JSON.stringify(exams));
  }, [exams]);

  // Auto-detect & activate correct current Month, Week, and Day on startup
  useEffect(() => {
    const today = new Date();
    const currentMonth = today.getMonth(); // 0-11
    const currentYear = today.getFullYear();

    let monthIdx = 1;
    if (currentYear === 2026) {
      if (currentMonth >= 5) { // June is 5
        monthIdx = currentMonth - 5 + 1;
      } else {
        monthIdx = 1; // Default to June 2026
      }
    } else if (currentYear === 2027) {
      monthIdx = currentMonth + 7 + 1; // January 2027 is Month 8
    } else {
      monthIdx = 1;
    }
    if (monthIdx > 11) monthIdx = 11;
    setCurrentMonthIndex(monthIdx);

    const dayOfMonth = today.getDate();
    const weekIdx = Math.min(Math.floor((dayOfMonth - 1) / 7) + 1, 4);
    setCurrentWeekIndex(weekIdx);

    const dayOfWeek = today.getDay(); // 0-6
    const dayKeys = ['cn', 't2', 't3', 't4', 't5', 't6', 't7'];
    setSelectedDayKey(dayKeys[dayOfWeek]);
  }, []);

  // Load baseline data on startup
  useEffect(() => {
    fetchData();
  }, []);


  // Pomodoro countdown timer logic
  useEffect(() => {
    if (pomodoroActive) {
      pomodoroInterval.current = setInterval(() => {
        setPomodoroTime((prev) => {
          if (prev <= 1) {
            clearInterval(pomodoroInterval.current);
            setPomodoroActive(false);
            alert('⏱️ Hết 25 phút tập trung! Bé hãy đứng dậy giải lao 5 phút, uống nước và nhắm mắt nghỉ ngơi để bảo vệ thị lực.');
            return 1500;
          }
          return prev - 1;
        });
      }, 1000);
    } else {
      if (pomodoroInterval.current) clearInterval(pomodoroInterval.current);
    }
    return () => {
      if (pomodoroInterval.current) clearInterval(pomodoroInterval.current);
    };
  }, [pomodoroActive]);

  // Auto-select first parent chapter when selectedSubjectId, chapters, or showCoreOnly change
  useEffect(() => {
    if (chapters && chapters.length > 0 && selectedSubjectId) {
      let subjectChapters = chapters.filter(c => c.subject_id === selectedSubjectId && c.parent_chapter);
      if (showCoreOnly) {
        subjectChapters = subjectChapters.filter(isCoreTopic);
      }
      if (subjectChapters.length > 0) {
        const parentChapters = Array.from(new Set(subjectChapters.map(c => c.parent_chapter)));
        if (!parentChapters.includes(selectedParentChapter)) {
          setSelectedParentChapter(parentChapters[0]);
        }
      } else {
        setSelectedParentChapter('');
      }
    }
  }, [selectedSubjectId, chapters, showCoreOnly]);

  const fetchData = async () => {
    try {
      const resSubj = await fetch(`${API_BASE}/subjects`);
      if (!resSubj.ok) throw new Error('Backend unreached');
      const dataSubj = await resSubj.json();
      setSubjects(dataSubj);

      const resCh = await fetch(`${API_BASE}/chapters`);
      const dataCh = await resCh.json();
      setChapters(dataCh);

      const resStats = await fetch(`${API_BASE}/study/stats`);
      const dataStats = await resStats.json();
      setStats(dataStats);

      const resDue = await fetch(`${API_BASE}/study/due`);
      const dataDue = await resDue.json();
      setDueCards(dataDue);

      const resAll = await fetch(`${API_BASE}/flashcards`);
      const dataAll = await resAll.json();
      setAllCards(dataAll);

      const resDueCh = await fetch(`${API_BASE}/chapters/due`);
      const dataDueCh = await resDueCh.json();
      setDueChapters(dataDueCh);

      setIsOnline(true);
    } catch (error) {
      console.warn('Backend server offline. Running in offline fallback mode with mock data.', error);
      setIsOnline(false);
      setupMockFallback();
    }
  };

  const setupMockFallback = () => {
    const mockSubjects = [
      { id: 1, name: 'Toán', color_code: 'hsl(200, 100%, 55%)' },
      { id: 2, name: 'Tiếng Việt', color_code: 'hsl(20, 95%, 60%)' },
      { id: 3, name: 'Tiếng Anh', color_code: 'hsl(150, 80%, 50%)' }
    ];
    setSubjects(mockSubjects);

    const mockChapters = [
      { id: 1, subject_id: 1, name: 'Số học & Các phép tính', sort_order: 1 },
      { id: 2, subject_id: 1, name: 'Toán tỉ số & Tỉ số phần trăm', sort_order: 2 },
      { id: 3, subject_id: 1, name: 'Toán có lời văn cơ bản', sort_order: 3 },
      { id: 4, subject_id: 1, name: 'Toán chuyển động đều', sort_order: 4 },
      { id: 5, subject_id: 1, name: 'Hình học phẳng & Hình khối', sort_order: 5 },
      { id: 6, subject_id: 1, name: 'Toán tư duy & Logic', sort_order: 6 },
      { id: 7, subject_id: 2, name: 'Luyện từ và câu - Từ vựng', sort_order: 1 },
      { id: 8, subject_id: 2, name: 'Luyện từ và câu - Ngữ pháp', sort_order: 2 },
      { id: 9, subject_id: 2, name: 'Biện pháp tu từ', sort_order: 3 },
      { id: 10, subject_id: 2, name: 'Đọc hiểu & Cảm thụ văn học', sort_order: 4 },
      { id: 11, subject_id: 2, name: 'Tập làm văn', sort_order: 5 },
      { id: 12, subject_id: 3, name: 'Phát âm & Trọng âm', sort_order: 1 },
      { id: 13, subject_id: 3, name: 'Từ vựng theo chủ điểm', sort_order: 2 },
      { id: 14, subject_id: 3, name: 'Ngữ pháp - Thì của động từ', sort_order: 3 },
      { id: 15, subject_id: 3, name: 'Ngữ pháp - Cấu trúc câu', sort_order: 4 },
      { id: 16, subject_id: 3, name: 'Đọc điền từ & Đọc hiểu', sort_order: 5 },
      { id: 17, subject_id: 3, name: 'Viết & Biến đổi câu', sort_order: 6 }
    ];
    setChapters(mockChapters);

    // Initial seed mock flashcards using detailed DEFAULT_RECALL_CARDS
    setAllCards(DEFAULT_RECALL_CARDS);
    setDueCards(DEFAULT_RECALL_CARDS);
    setDueChapters([]);

    setStats({
      streak_days: 6,
      total_score: 180,
      total_cards: DEFAULT_RECALL_CARDS.length,
      due_cards: DEFAULT_RECALL_CARDS.length,
      total_reviews: 42
    });
  };

  // Start study session
  const startStudySession = (filterSubjectId = null) => {
    let filteredDue = [...dueCards];
    if (filterSubjectId) {
      filteredDue = filteredDue.filter(card => {
        const ch = chapters.find(c => c.id === card.chapter_id);
        return ch && ch.subject_id === filterSubjectId;
      });
    }

    if (filteredDue.length === 0) {
      alert('Hôm nay bé không có thẻ ôn tập nào thuộc môn học này. Hãy ôn tập chung hoặc học lý thuyết trên TAK12!');
      return;
    }

    setStudySession({
      cards: filteredDue,
      currentIndex: 0,
      showAnswer: false,
      startTime: new Date()
    });
    setSessionCompleted(false);
    setXpGained(0);
    setPomodoroActive(true);
  };

  // Submit Spaced Repetition card review
  const submitReview = async (score) => {
    if (!studySession) return;
    const currentCard = studySession.cards[studySession.currentIndex];
    const localXp = score >= 3 ? 10 : 5;
    setXpGained(prev => prev + localXp);

    if (isOnline) {
      try {
        await fetch(`${API_BASE}/study/review`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ card_id: currentCard.id, score })
        });
      } catch (err) {
        console.error('Failed to submit review online', err);
      }
    } else {
      const updatedCards = dueCards.map(c => {
        if (c.id === currentCard.id) {
          return { ...c, box_number: score >= 3 ? Math.min((c.box_number || 1) + 1, 5) : 1 };
        }
        return c;
      });
      setDueCards(updatedCards);
      setStats(prev => ({
        ...prev,
        total_score: prev.total_score + localXp,
        total_reviews: prev.total_reviews + 1
      }));
    }

    if (studySession.currentIndex + 1 < studySession.cards.length) {
      setStudySession(prev => ({
        ...prev,
        currentIndex: prev.currentIndex + 1,
        showAnswer: false
      }));
    } else {
      setSessionCompleted(true);
      setPomodoroActive(false);
      fetchData();
    }
  };

  // Topic Practice Helper Functions
  const startTopicPractice = async (chapter) => {
    setPracticeTimer(0);
    setActivePracticeTopic({
      chapter,
      questions: [],
      currentIndex: 0,
      showAnswer: false,
      answers: [],
      selectedAnswer: null,
      score: null,
      xp_awarded: 0,
      loading: true,
      error: null
    });

    try {
      const res = await fetch(`${API_BASE}/chapters/${chapter.id}/questions`);
      if (!res.ok) {
        throw new Error('Không thể tải câu hỏi từ máy chủ.');
      }
      const data = await res.json();
      if (!data.questions || data.questions.length === 0) {
        throw new Error('Chủ đề này chưa có câu hỏi hoặc không thể tự động biên soạn.');
      }
      setActivePracticeTopic(prev => ({
        ...prev,
        questions: data.questions,
        loading: false
      }));
    } catch (err) {
      console.error('Error fetching questions:', err);
      setActivePracticeTopic(prev => ({
        ...prev,
        loading: false,
        error: err.message || 'Lỗi tải câu hỏi'
      }));
    }
  };

  const handleSelectOption = (option) => {
    if (!activePracticeTopic || activePracticeTopic.showAnswer) return;

    const currentQuestion = activePracticeTopic.questions[activePracticeTopic.currentIndex];
    const isCorrect = option === currentQuestion.correct_answer;

    setActivePracticeTopic(prev => {
      const newAnswers = [...prev.answers];
      newAnswers[prev.currentIndex] = {
        questionId: currentQuestion.id,
        selected: option,
        isCorrect: isCorrect
      };

      return {
        ...prev,
        selectedAnswer: option,
        showAnswer: true,
        answers: newAnswers
      };
    });
  };

  const handleNextQuestion = async () => {
    if (!activePracticeTopic) return;

    const nextIndex = activePracticeTopic.currentIndex + 1;
    if (nextIndex < activePracticeTopic.questions.length) {
      setActivePracticeTopic(prev => ({
        ...prev,
        currentIndex: nextIndex,
        selectedAnswer: null,
        showAnswer: false
      }));
    } else {
      // Calculate score
      const correctCount = activePracticeTopic.answers.filter(a => a.isCorrect).length;
      const totalCount = activePracticeTopic.questions.length;
      const scorePercent = Math.round((correctCount / totalCount) * 100);

      // Call practice submit API
      try {
        const res = await fetch(`${API_BASE}/chapters/${activePracticeTopic.chapter.id}/practice`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            score: scorePercent,
            total_questions: totalCount,
            correct_answers: correctCount
          })
        });
        const data = await res.json();
        
        setActivePracticeTopic(prev => ({
          ...prev,
          score: scorePercent,
          xp_awarded: data.xp_awarded || (correctCount * 10),
          next_review_in: data.next_review_in || 1,
          box_number: data.box_number || 1
        }));

        // Refresh stats/data
        fetchData();
      } catch (err) {
        console.error('Error submitting practice results:', err);
        // Fallback for offline mode
        setActivePracticeTopic(prev => ({
          ...prev,
          score: scorePercent,
          xp_awarded: correctCount * 10,
          next_review_in: 1,
          box_number: 1
        }));
      }
    }
  };

  const handleSaveQuestionAsFlashcard = async (q) => {
    // Front content: Question text + options
    const front = `Chủ đề: ${activePracticeTopic.chapter.name}\n\nCâu hỏi: ${q.question_text}\n\n${q.options.join('\n')}`;
    const back = `Đáp án đúng: ${q.correct_answer}\n\nGiải thích: ${q.explanation}`;
    const hint = q.hint || '';

    try {
      const res = await fetch(`${API_BASE}/flashcards`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          chapter_id: activePracticeTopic.chapter.id,
          front_content: front,
          back_content: back,
          hint: hint
        })
      });
      if (res.ok) {
        alert('🎉 Đã lưu câu hỏi thành flashcard vào kho thẻ để ôn tập!');
      } else {
        throw new Error('Lỗi từ server');
      }
    } catch (err) {
      console.error('Error saving flashcard:', err);
      alert('❌ Không thể lưu câu hỏi thành flashcard. Hãy kiểm tra kết nối mạng.');
    }
  };

  const handleCompletePractice = () => {
    setActivePracticeTopic(null);
    setPracticeTimer(0);
    fetchData();
  };

  // Practice timer interval
  useEffect(() => {
    let interval = null;
    if (activePracticeTopic && !activePracticeTopic.loading && activePracticeTopic.score === null) {
      interval = setInterval(() => {
        setPracticeTimer((prev) => prev + 1);
      }, 1000);
    } else {
      if (interval) clearInterval(interval);
    }
    return () => {
      if (interval) clearInterval(interval);
    };
  }, [activePracticeTopic]);

  // Keydown event listener for Focus Arena practice options
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (!activePracticeTopic || activePracticeTopic.loading || activePracticeTopic.score !== null) return;
      
      const key = e.key.toLowerCase();
      
      // If showing the answer, space or enter goes to next
      if (activePracticeTopic.showAnswer) {
        if (key === ' ' || key === 'enter') {
          e.preventDefault();
          handleNextQuestion();
        }
        return;
      }
      
      const options = activePracticeTopic.questions[activePracticeTopic.currentIndex]?.options || [];
      if (options.length === 0) return;
      
      let selectedIdx = -1;
      if (key === '1' || key === 'a') selectedIdx = 0;
      else if (key === '2' || key === 'b') selectedIdx = 1;
      else if (key === '3' || key === 'c') selectedIdx = 2;
      else if (key === '4' || key === 'd') selectedIdx = 3;
      
      if (selectedIdx >= 0 && selectedIdx < options.length) {
        e.preventDefault();
        handleSelectOption(options[selectedIdx]);
      }
    };
    
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [activePracticeTopic]);

  // Toggle lesson complete state
  const toggleLessonComplete = (lessonKey, chapterId) => {
    const isCompleted = !completedLessons[lessonKey];
    setCompletedLessons(prev => ({
      ...prev,
      [lessonKey]: isCompleted
    }));

    if (isCompleted) {
      // Trigger XP gain for completing study session
      setStats(prev => ({ ...prev, total_score: prev.total_score + 20 }));
      alert('🎉 Đã ghi nhận học lý thuyết trên TAK12! Hệ thống sẽ xếp lịch ôn tập Active Recall cho chuyên đề này từ ngày mai.');
      
      // Auto pre-populate 3 standard study check cards for this chapter if none exist
      const existingCards = allCards.filter(c => c.chapter_id === chapterId);
      if (existingCards.length === 0) {
        addTemplateCardsForChapter(chapterId);
      }
    }
  };

  // Insert base recall cards for a newly completed chapter
  const addTemplateCardsForChapter = async (chapterId) => {
    const chapterName = chapters.find(c => c.id === chapterId)?.name || 'Chuyên đề';
    const templates = [
      {
        front_content: `[Recall Lý thuyết] Nêu khái niệm cốt lõi hoặc công thức quan trọng của chuyên đề: "${chapterName}".`,
        back_content: `Bé hãy tự đối chiếu kiến thức lý thuyết đã học trên chuyên đề "${chapterName}" của TAK12 để kiểm tra xem mình đã hiểu rõ bản chất chưa.`,
        hint: 'Tóm tắt lý thuyết trọng tâm của chương.'
      },
      {
        front_content: `[Recall Dạng bài] Chuyên đề "${chapterName}" thường có những dạng câu hỏi hoặc bài tập điển hình nào trên đề thi?`,
        back_content: 'Liệt kê các dạng bài tập chính của chuyên đề và cách thức giải quyết cơ bản.',
        hint: 'Xem cấu trúc đề luyện thi trên TAK12.'
      }
    ];

    for (const temp of templates) {
      const payload = { chapter_id: chapterId, ...temp };
      if (isOnline) {
        try {
          await fetch(`${API_BASE}/flashcards`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
          });
        } catch (e) {
          console.error(e);
        }
      } else {
        const mockNew = {
          id: Date.now() + Math.random(),
          chapter_id: chapterId,
          ...temp,
          box_number: 1
        };
        setAllCards(prev => [...prev, mockNew]);
        setDueCards(prev => [...prev, mockNew]);
      }
    }
    fetchData();
  };

  // Create Manual Flashcard
  const handleCreateCard = async (e) => {
    e.preventDefault();
    if (!newCard.front_content || !newCard.back_content) {
      alert('Vui lòng nhập đầy đủ nội dung.');
      return;
    }

    const payload = {
      chapter_id: parseInt(newCard.chapter_id),
      sub_topic_id: parseInt(newCard.sub_topic_id),
      front_content: newCard.front_content,
      back_content: newCard.back_content,
      hint: newCard.hint
    };

    if (isOnline) {
      try {
        const res = await fetch(`${API_BASE}/flashcards`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
        if (res.ok) {
          alert('Đã tạo thẻ recall mới thành công!');
          setNewCard({ ...newCard, front_content: '', back_content: '', hint: '' });
          fetchData();
        }
      } catch (err) {
        alert('Lỗi kết nối server.');
      }
    } else {
      const mockNewCard = {
        id: Date.now(),
        ...payload,
        box_number: 1
      };
      setAllCards([...allCards, mockNewCard]);
      setDueCards([...dueCards, mockNewCard]);
      setNewCard({ ...newCard, front_content: '', back_content: '', hint: '' });
      alert('Đã thêm thẻ mới vào cơ sở dữ liệu tạm thời (Offline).');
    }
  };

  // AI Flashcard Generation via Gemini API
  const handleAIGenerate = async () => {
    if (!aiText) {
      alert('Vui lòng dán nội dung lý thuyết.');
      return;
    }
    setAiLoading(true);
    setAiGeneratedCards([]);

    try {
      const subjectName = subjects.find(s => s.id === parseInt(aiSubjectId))?.name || 'Học tập';
      const res = await fetch(`${API_BASE}/ai/generate-flashcards`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          text: aiText,
          subject_name: subjectName,
          count: aiCount
        })
      });
      if (res.ok) {
        const data = await res.json();
        if (data.flashcards && data.flashcards.length > 0) {
          setAiGeneratedCards(data.flashcards);
        } else {
          alert('Không sinh được câu hỏi nào. Hãy kiểm tra lại đoạn văn bản đầu vào.');
        }
      } else {
        alert('Server báo lỗi khi gọi API AI.');
      }
    } catch (err) {
      alert('Lỗi kết nối AI server.');
    } finally {
      setAiLoading(false);
    }
  };

  const saveAICards = async () => {
    if (aiGeneratedCards.length === 0) return;
    let countSaved = 0;
    for (const card of aiGeneratedCards) {
      try {
        const payload = {
          chapter_id: parseInt(aiChapterId),
          front_content: card.front,
          back_content: card.back,
          hint: card.hint
        };
        if (isOnline) {
          await fetch(`${API_BASE}/flashcards`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
          });
        }
        countSaved++;
      } catch (err) {
        console.error(err);
      }
    }
    alert(`Đã lưu thành công ${countSaved} câu hỏi recall vào database!`);
    setAiGeneratedCards([]);
    setAiText('');
    fetchData();
  };

  // Add practice exam log
  const handleAddExam = (e) => {
    e.preventDefault();
    if (!newExam.name || !newExam.score) {
      alert('Vui lòng nhập tên đề thi và điểm số.');
      return;
    }
    const scoreVal = parseFloat(newExam.score);
    if (isNaN(scoreVal) || scoreVal < 0 || scoreVal > 10) {
      alert('Điểm số phải hợp lệ từ 0 đến 10.');
      return;
    }

    const newExamObj = {
      id: Date.now(),
      name: newExam.name,
      subject_id: parseInt(newExam.subject_id),
      score: scoreVal,
      date: newExam.date
    };

    setExams([newExamObj, ...exams]);
    setMistakeCard(prev => ({
      ...prev,
      exam_name: newExam.name,
      subject_id: parseInt(newExam.subject_id)
    }));
    setNewExam({
      name: '',
      subject_id: 1,
      score: '',
      date: new Date().toISOString().split('T')[0]
    });
    alert('Đã ghi nhận bài thi thử!');
  };

  // Add mistake card log
  const handleAddMistake = async (e) => {
    e.preventDefault();
    if (!mistakeCard.front_content || !mistakeCard.back_content) {
      alert('Vui lòng nhập câu sai và đáp án.');
      return;
    }

    const payload = {
      chapter_id: parseInt(mistakeCard.chapter_id),
      sub_topic_id: parseInt(mistakeCard.sub_topic_id),
      front_content: `[SAI TỪ ĐỀ: ${mistakeCard.exam_name || 'Luyện đề TAK12'}]\n${mistakeCard.front_content}`,
      back_content: mistakeCard.back_content,
      hint: mistakeCard.hint || 'Câu hỏi sửa sai đề thi'
    };

    if (isOnline) {
      try {
        const res = await fetch(`${API_BASE}/flashcards`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
        if (res.ok) {
          alert('Đã lưu lỗi sai vào danh mục ôn tập recall!');
          setMistakeCard({ ...mistakeCard, front_content: '', back_content: '', hint: '' });
          fetchData();
        }
      } catch (err) {
        alert('Lỗi kết nối server.');
      }
    } else {
      const mockCard = {
        id: Date.now(),
        ...payload,
        box_number: 1
      };
      setAllCards([...allCards, mockCard]);
      setDueCards([mockCard, ...dueCards]);
      setMistakeCard({ ...mistakeCard, front_content: '', back_content: '', hint: '' });
      alert('Đã lưu lỗi sai vào bộ nhớ tạm thời!');
    }
  };

  // Determine what is scheduled for a specific day based on the calendar plan
  const getDayPlanDetails = (monthIdx, weekIdx, dayKey) => {
    const monthObj = MONTHS_MAP[monthIdx - 1];
    
    // Final exam month (April) has no lessons, just final exams
    if (monthObj.phase === 'final') {
      return {
        type: 'final_exam',
        title: 'KỲ THI CHÍNH THỨC VÀO LỚP 6',
        desc: 'Bé giữ vững tinh thần thoải mái, làm bài thi tự tin!'
      };
    }

    // Practice phase (Dec - Mar)
    if (monthObj.phase === 'exam') {
      if (dayKey === 'cn') {
        return {
          type: 'exam_practice',
          title: `Luyện đề thi thử (${monthObj.desc})`,
          desc: 'Làm 1 bộ đề thi tổng hợp trên TAK12, nhập điểm và ghi câu sai.'
        };
      }
      return {
        type: 'exam_recall',
        title: 'Ôn tập lỗi sai đề thi thử',
        desc: 'Recall lại các câu hỏi sai đã tích lũy trong kho lỗi sai.'
      };
    }

    // Theory Phase (June - Nov)
    const monthSyllabus = CURRICULUM_DISTRIBUTION[monthIdx];
    if (!monthSyllabus) return null;

    if (dayKey === 't2' || dayKey === 't5') { // Math theory
      const chInfo = monthSyllabus[1];
      return {
        type: 'study_theory',
        subject_id: 1,
        subject_name: 'Toán',
        chapter_id: chInfo.id,
        chapter_name: chInfo.name,
        desc: `Học lý thuyết và làm bài tập chuyên đề "${chInfo.name}" trên TAK12.`
      };
    }
    if (dayKey === 't3' || dayKey === 't6') { // English theory
      const chInfo = monthSyllabus[3];
      return {
        type: 'study_theory',
        subject_id: 3,
        subject_name: 'Tiếng Anh',
        chapter_id: chInfo.id,
        chapter_name: chInfo.name,
        desc: `Học từ vựng/ngữ pháp chuyên đề "${chInfo.name}" trên TAK12.`
      };
    }
    if (dayKey === 't4' || dayKey === 't7') { // TV theory
      const chInfo = monthSyllabus[2];
      return {
        type: 'study_theory',
        subject_id: 2,
        subject_name: 'Tiếng Việt',
        chapter_id: chInfo.id,
        chapter_name: chInfo.name,
        desc: `Học lý thuyết và ôn luyện chuyên đề "${chInfo.name}" trên TAK12.`
      };
    }

    // Active Recall / Comprehensive Review Day (Sunday)
    return {
      type: 'recall_only',
      title: 'Tổng ôn tập Spaced Repetition',
      desc: 'Hôm nay không học lý thuyết mới. Bé hãy tập trung ôn tập toàn bộ các thẻ đến hạn và câu hỏi tích lũy.'
    };
  };

  const selectedDayPlan = getDayPlanDetails(currentMonthIndex, currentWeekIndex, selectedDayKey);
  const currentMonthObj = MONTHS_MAP[currentMonthIndex - 1];

  return (
    <div className="app-container">
      
      {/* Offline Alert Bar */}
      {!isOnline && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          background: 'rgba(245, 158, 11, 0.95)',
          color: '#000000',
          padding: '8px 16px',
          textAlign: 'center',
          fontSize: '0.85rem',
          fontWeight: 700,
          zIndex: 100,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          gap: '8px',
          boxShadow: '0 2px 10px rgba(0,0,0,0.3)'
        }}>
          <AlertCircle size={16} />
          <span>Ứng dụng đang chạy ở Chế Độ Ngoại Tuyến. Lịch trình và câu hỏi học tập sử dụng cơ sở dữ liệu dự phòng.</span>
        </div>
      )}

      {/* Sidebar navigation */}
      <div className="sidebar" style={{ paddingTop: !isOnline ? '36px' : '0' }}>
        <div style={{ padding: '1.5rem', borderBottom: '1px solid var(--glass-border)', display: 'flex', alignItems: 'center', gap: '10px' }}>
          <div style={{ background: 'var(--color-primary-bg)', padding: '6px', borderRadius: '10px', border: '1px solid var(--color-primary-border)' }}>
            <BrainCircuit style={{ color: 'var(--color-primary)' }} size={24} />
          </div>
          <div>
            <div className="logo-text" style={{ fontWeight: 800, fontSize: '1.15rem', tracking: '-0.02em' }}>RecallKid Pro</div>
            <div className="logo-text" style={{ fontSize: '0.7rem', color: 'var(--color-text-subtle)', fontWeight: 600 }}>Bộ não Lập Lịch Học Ôn Thi</div>
          </div>
        </div>

        <div style={{ flex: 1, padding: '1rem 0.5rem', display: 'flex', flexDirection: 'column', gap: '4px' }}>
          <button 
            className={`tab-btn ${activeTab === 'overview' ? 'active' : ''}`}
            onClick={() => { setActiveTab('overview'); setStudySession(null); }}
            style={{ 
              display: 'flex', 
              alignItems: 'center', 
              gap: '12px', 
              width: '100%', 
              textAlign: 'left', 
              borderRadius: '10px', 
              border: 'none', 
              borderBottom: 'none',
              background: activeTab === 'overview' ? 'var(--color-girl-bg)' : 'transparent',
              borderColor: activeTab === 'overview' ? 'var(--color-girl-border)' : 'transparent',
              color: activeTab === 'overview' ? 'var(--color-girl)' : 'var(--color-text-muted)',
              boxShadow: activeTab === 'overview' ? '0 0 10px rgba(244, 63, 94, 0.15)' : 'none'
            }}
          >
            <Sparkles size={18} style={{ color: activeTab === 'overview' ? 'var(--color-girl)' : 'inherit' }} />
            <span className="nav-label" style={{ fontWeight: activeTab === 'overview' ? 700 : 'normal' }}>Lịch & Lộ Trình 🌸</span>
          </button>

          <button 
            className={`tab-btn ${activeTab === 'dashboard' ? 'active' : ''}`}
            onClick={() => { setActiveTab('dashboard'); setStudySession(null); }}
            style={{ display: 'flex', alignItems: 'center', gap: '12px', width: '100%', textAlign: 'left', borderRadius: '10px', border: 'none', borderBottom: 'none' }}
          >
            <LayoutDashboard size={18} />
            <span className="nav-label">Lịch Học & Recall</span>
          </button>

          <button 
            className={`tab-btn ${activeTab === 'timeline' ? 'active' : ''}`}
            onClick={() => { setActiveTab('timeline'); setStudySession(null); }}
            style={{ display: 'flex', alignItems: 'center', gap: '12px', width: '100%', textAlign: 'left', borderRadius: '10px', border: 'none', borderBottom: 'none' }}
          >
            <CalendarDays size={18} />
            <span className="nav-label">Roadmap 10 Tháng</span>
          </button>

          <button 
            className={`tab-btn ${activeTab === 'topics' ? 'active' : ''}`}
            onClick={() => { setActiveTab('topics'); setStudySession(null); }}
            style={{ display: 'flex', alignItems: 'center', gap: '12px', width: '100%', textAlign: 'left', borderRadius: '10px', border: 'none', borderBottom: 'none' }}
          >
            <Target size={18} />
            <span className="nav-label">Luyện Chuyên Đề 🎯</span>
          </button>

          <button 
            className={`tab-btn ${activeTab === 'library' ? 'active' : ''}`}
            onClick={() => { setActiveTab('library'); setStudySession(null); }}
            style={{ display: 'flex', alignItems: 'center', gap: '12px', width: '100%', textAlign: 'left', borderRadius: '10px', border: 'none', borderBottom: 'none' }}
          >
            <BookOpen size={18} />
            <span className="nav-label">Xem Thẻ Ôn Tập</span>
          </button>

          <button 
            className={`tab-btn ${activeTab === 'parent' ? 'active' : ''}`}
            onClick={() => { setActiveTab('parent'); setStudySession(null); }}
            style={{ display: 'flex', alignItems: 'center', gap: '12px', width: '100%', textAlign: 'left', borderRadius: '10px', border: 'none', borderBottom: 'none' }}
          >
            <Settings size={18} />
            <span className="nav-label">Cổng Phụ Huynh</span>
          </button>
        </div>

        <div style={{ padding: '1rem', borderTop: '1px solid var(--glass-border)', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }} className="user-info">
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <div style={{ width: '36px', height: '36px', borderRadius: '50%', background: 'linear-gradient(135deg, var(--color-girl) 0%, var(--color-primary) 100%)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 'bold', fontSize: '0.85rem', boxShadow: '0 0 10px rgba(244, 63, 94, 0.4)' }}>
              🌸
            </div>
            <div>
              <div style={{ fontSize: '0.85rem', fontWeight: 'bold', color: '#ffffff' }}>Hoàng My 🎀</div>
              <div style={{ fontSize: '0.75rem', color: 'var(--color-text-muted)' }}>XP: {stats.total_score}</div>
            </div>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '4px', background: 'rgba(255, 120, 50, 0.1)', border: '1px solid rgba(255, 120, 50, 0.2)', padding: '2px 8px', borderRadius: '99px' }}>
            <Flame size={14} style={{ color: 'var(--color-viet)' }} />
            <span style={{ fontSize: '0.8rem', fontWeight: 'bold', color: 'var(--color-viet)' }}>{stats.streak_days} 🔥</span>
          </div>
        </div>
      </div>

      {/* Main viewport */}
      <div className="main-content" style={{ marginTop: !isOnline ? '36px' : '0' }}>
        
        {/* Active Study Session Overlay */}
        {studySession && (
          <div style={{
            background: 'var(--bg-deep)',
            position: 'fixed',
            inset: 0,
            zIndex: 50,
            padding: '2rem',
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'space-between',
            boxSizing: 'border-box'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', width: '100%', borderBottom: '1px solid var(--glass-border)', paddingBottom: '1rem' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                <button 
                  onClick={() => {
                    if (confirm('Bé có muốn tạm dừng phiên ôn tập?')) {
                      setStudySession(null);
                      setPomodoroActive(false);
                    }
                  }} 
                  style={{ background: 'transparent', border: 'none', cursor: 'pointer', color: '#ffffff' }}
                >
                  <ChevronLeft size={24} />
                </button>
                <span style={{ fontWeight: 'bold', fontSize: '1.2rem' }}>Phiên Ôn Tập Active Recall</span>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '6px', background: 'rgba(255,255,255,0.05)', padding: '4px 10px', borderRadius: '8px' }}>
                  <Clock size={16} style={{ color: 'var(--color-primary)' }} />
                  <span style={{ fontSize: '0.9rem', fontWeight: 600, fontFamily: 'monospace' }}>{formatTime(pomodoroTime)}</span>
                </div>
                <span style={{ fontSize: '0.9rem', color: 'var(--color-text-muted)' }}>
                  Thẻ {studySession.currentIndex + 1} / {studySession.cards.length}
                </span>
              </div>
            </div>

            <div style={{ flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', padding: '1rem 0' }}>
              {!sessionCompleted ? (
                <>
                  <div 
                    className={`recall-card-wrapper ${studySession.showAnswer ? 'flipped' : ''}`}
                    onClick={() => setStudySession(prev => ({ ...prev, showAnswer: !prev.showAnswer }))}
                  >
                    <div className="recall-card-inner">
                      {/* Front */}
                      <div className="recall-card-face recall-card-front">
                        <span style={{ 
                          fontSize: '0.75rem', 
                          fontWeight: 700, 
                          color: 'var(--color-primary)', 
                          background: 'var(--color-primary-bg)', 
                          border: '1px solid var(--color-primary-border)',
                          padding: '2px 8px',
                          borderRadius: '99px',
                          textTransform: 'uppercase'
                        }}>
                          Câu hỏi ôn tập (Mặt Trước)
                        </span>
                        
                        <div className="card-content">
                          {studySession.cards[studySession.currentIndex].front_content}
                        </div>

                        <div style={{ fontSize: '0.85rem', color: 'var(--color-text-subtle)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                          <Info size={14} />
                          <span>Tự suy nghĩ đáp án, viết ra nháp rồi click thẻ để lật kiểm tra</span>
                        </div>
                      </div>

                      {/* Back */}
                      <div className="recall-card-face recall-card-back">
                        <span style={{ 
                          fontSize: '0.75rem', 
                          fontWeight: 700, 
                          color: 'var(--color-eng)', 
                          background: 'rgba(16, 185, 129, 0.15)', 
                          border: '1px solid rgba(16, 185, 129, 0.3)',
                          padding: '2px 8px',
                          borderRadius: '99px',
                          textTransform: 'uppercase'
                        }}>
                          Đáp án chính xác (Mặt Sau)
                        </span>

                        <div className="card-content" style={{ fontSize: '1.25rem' }}>
                          {studySession.cards[studySession.currentIndex].back_content}
                        </div>

                        {studySession.cards[studySession.currentIndex].hint && (
                          <div style={{ 
                            background: 'rgba(255, 255, 255, 0.03)', 
                            border: '1px solid var(--glass-border)', 
                            borderRadius: '8px', 
                            padding: '6px 12px', 
                            fontSize: '0.8rem', 
                            color: 'var(--color-accent-amber)',
                            maxWidth: '90%'
                          }}>
                            <strong>Gợi ý: </strong>{studySession.cards[studySession.currentIndex].hint}
                          </div>
                        )}
                      </div>
                    </div>
                  </div>

                  {studySession.showAnswer ? (
                    <div style={{ textAlign: 'center', width: '100%' }}>
                      <p style={{ margin: '0 0 10px 0', fontSize: '0.9rem', color: 'var(--color-text-muted)' }}>
                        Bé tự đánh giá độ ghi nhớ của câu này để hệ thống lên lịch lặp:
                      </p>
                      <div className="score-button-group">
                        <button className="score-btn score-btn-hardest" onClick={() => submitReview(1)}>
                          <span>Rất Khó</span>
                          <span className="btn-desc">Ôn lại ngày mai</span>
                        </button>
                        <button className="score-btn score-btn-hard" onClick={() => submitReview(2)}>
                          <span>Khó</span>
                          <span className="btn-desc">Ôn sau 3 ngày</span>
                        </button>
                        <button className="score-btn score-btn-good" onClick={() => submitReview(3)}>
                          <span>Nhớ Bài</span>
                          <span className="btn-desc">Ôn sau 7 ngày</span>
                        </button>
                        <button className="score-btn score-btn-easy" onClick={() => submitReview(4)}>
                          <span>Rất Dễ</span>
                          <span className="btn-desc">Ôn sau 14 ngày</span>
                        </button>
                      </div>
                    </div>
                  ) : (
                    <button 
                      className="btn-primary glow-active"
                      onClick={() => setStudySession(prev => ({ ...prev, showAnswer: true }))}
                      style={{ padding: '1rem 2.5rem', borderRadius: '14px', fontSize: '1.1rem' }}
                    >
                      Lật Thẻ Xem Đáp Án
                    </button>
                  )}
                </>
              ) : (
                <div style={{ textAlign: 'center', maxWidth: '480px', animation: 'slide-in 0.4s ease' }}>
                  <div style={{ 
                    background: 'var(--color-primary-bg)', 
                    border: '1px solid var(--color-primary-border)', 
                    width: '80px', 
                    height: '80px', 
                    borderRadius: '50%', 
                    display: 'flex', 
                    alignItems: 'center', 
                    justifyContent: 'center', 
                    margin: '0 auto 1.5rem auto',
                    boxShadow: '0 0 30px rgba(120, 100, 255, 0.4)'
                  }}>
                    <Award size={48} style={{ color: 'var(--color-primary)' }} />
                  </div>
                  <h2 style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>Hoàn Thành Phiên Ôn Tập!</h2>
                  <p style={{ color: 'var(--color-text-muted)', marginBottom: '2rem' }}>
                    Bé đã hoàn tất kiểm tra chủ động {studySession.cards.length} thẻ đến hạn ngày hôm nay.
                  </p>
                  
                  <div style={{ 
                    display: 'grid', 
                    gridTemplateColumns: '1fr 1fr', 
                    gap: '16px', 
                    marginBottom: '2rem' 
                  }}>
                    <div style={{ background: 'rgba(255,255,255,0.02)', border: '1px solid var(--glass-border)', padding: '1rem', borderRadius: '12px' }}>
                      <div style={{ fontSize: '0.8rem', color: 'var(--color-text-muted)' }}>Điểm Thưởng Tích Lũy</div>
                      <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: 'var(--color-accent-amber)' }}>+{xpGained} XP</div>
                    </div>
                    <div style={{ background: 'rgba(255,255,255,0.02)', border: '1px solid var(--glass-border)', padding: '1rem', borderRadius: '12px' }}>
                      <div style={{ fontSize: '0.8rem', color: 'var(--color-text-muted)' }}>Streak Ôn Tập</div>
                      <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: 'var(--color-viet)' }}>{stats.streak_days} 🔥</div>
                    </div>
                  </div>

                  <button 
                    className="btn-primary" 
                    onClick={() => { setStudySession(null); setSessionCompleted(false); }}
                    style={{ width: '100%', padding: '0.9rem', borderRadius: '12px' }}
                  >
                    Quay Lại Lịch Trình
                  </button>
                </div>
              )}
            </div>
          </div>
        )}

        {/* Lịch & Lộ Trình Tab: Combined Schedule & Roadmap in Feminine Aesthetic */}
        {activeTab === 'overview' && (
          <div style={{ animation: 'slide-in 0.4s ease', display: 'flex', flexDirection: 'column', gap: '2rem' }}>
            
            {/* Top Greeting & Motivational Quote (Pink Styled Card) */}
            <div className="girl-card" style={{ display: 'flex', alignItems: 'center', gap: '1.5rem', flexWrap: 'wrap' }}>
              <div style={{ 
                width: '64px', 
                height: '64px', 
                borderRadius: '50%', 
                background: 'linear-gradient(135deg, var(--color-girl) 0%, hsl(280, 85%, 65%) 100%)', 
                display: 'flex', 
                alignItems: 'center', 
                justifyContent: 'center', 
                fontSize: '2rem', 
                boxShadow: '0 0 20px rgba(244, 63, 94, 0.4)' 
              }}>
                🌸
              </div>
              <div style={{ flex: 1, minWidth: '250px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <h1 style={{ margin: 0, fontSize: '1.6rem', fontWeight: 800, color: '#ffffff' }}>Góc Học Tập Của Hoàng My 🎀</h1>
                  <span className="girl-badge">Bé Ngoan 🍭</span>
                </div>
                <div style={{ fontSize: '0.85rem', color: 'var(--color-girl)', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.05em', marginTop: '8px' }}>
                  🌸 Câu nói truyền cảm hứng hôm nay:
                </div>
                <div style={{ fontSize: '1rem', fontWeight: 600, color: '#ffffff', marginTop: '4px', fontStyle: 'italic', lineHeight: '1.4' }}>
                  "{getDailyQuote()}"
                </div>
              </div>
            </div>

            {/* Main Combined Area: 2 Columns */}
            <div style={{ display: 'grid', gridTemplateColumns: '1.2fr 0.8fr', gap: '2rem' }} className="overview-grid">
              
              {/* Left Column: Weekly Schedule & Actions */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
                
                <div className="girl-card" style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
                  
                  {/* Title & Month/Week Dropdowns */}
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
                    <h3 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '8px', fontSize: '1.2rem', color: '#ffffff' }}>
                      <CalendarIcon size={20} style={{ color: 'var(--color-girl)' }} />
                      Lịch Học Tuần Này
                    </h3>
                    
                    {/* Month/Week selectors */}
                    <div style={{ display: 'flex', gap: '8px' }}>
                      <select 
                        className="input-field" 
                        value={currentMonthIndex} 
                        onChange={(e) => setCurrentMonthIndex(parseInt(e.target.value))}
                        style={{ width: '130px', padding: '4px 10px', fontSize: '0.85rem', border: '1px solid var(--color-girl-border)', background: 'rgba(0,0,0,0.3)' }}
                      >
                        {MONTHS_MAP.map(m => <option key={m.id} value={m.id}>{m.name}</option>)}
                      </select>

                      {currentMonthObj.phase !== 'final' && (
                        <select 
                          className="input-field" 
                          value={currentWeekIndex} 
                          onChange={(e) => setCurrentWeekIndex(parseInt(e.target.value))}
                          style={{ width: '90px', padding: '4px 10px', fontSize: '0.85rem', border: '1px solid var(--color-girl-border)', background: 'rgba(0,0,0,0.3)' }}
                        >
                          {[1, 2, 3, 4].map(w => <option key={w} value={w}>Tuần {w}</option>)}
                        </select>
                      )}
                    </div>
                  </div>

                  {/* Horizontal Weekly Days Grid */}
                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(7, 1fr)', gap: '8px' }}>
                    {WEEKDAYS.map(day => {
                      const isActive = selectedDayKey === day.key;
                      const plan = getDayPlanDetails(currentMonthIndex, currentWeekIndex, day.key);
                      const hasStudy = plan && plan.type === 'study_theory';
                      const hasExam = plan && plan.type === 'exam_practice';

                      // Find out if day.key corresponds to today
                      const todayIndex = new Date().getDay(); // 0 is Sunday, 1 is Monday...
                      const daysMap = { 't2': 1, 't3': 2, 't4': 3, 't5': 4, 't6': 5, 't7': 6, 'cn': 0 };
                      const isRealToday = daysMap[day.key] === todayIndex;

                      const dayChObj = (plan && plan.chapter_id) ? chapters.find(c => c.id === plan.chapter_id) : null;
                      const isDayCore = dayChObj ? isCoreTopic(dayChObj) : false;

                      return (
                        <div 
                          key={day.key}
                          onClick={() => setSelectedDayKey(day.key)}
                          style={{
                            background: isActive ? 'var(--color-girl-bg)' : 'rgba(255, 255, 255, 0.02)',
                            border: isActive 
                              ? '2px solid var(--color-girl)' 
                              : (isRealToday ? '1.5px solid var(--color-accent-amber)' : '1px solid var(--bg-card-border)'),
                            borderRadius: '12px',
                            padding: '10px 4px',
                            textAlign: 'center',
                            cursor: 'pointer',
                            transition: 'all 0.2s ease',
                            display: 'flex',
                            flexDirection: 'column',
                            alignItems: 'center',
                            gap: '4px',
                            boxShadow: isActive ? '0 0 10px rgba(244, 63, 94, 0.2)' : 'none'
                          }}
                        >
                          <span style={{ fontSize: '0.75rem', fontWeight: 700, color: isActive ? 'var(--color-girl)' : 'var(--color-text-muted)' }}>
                            {day.label}
                          </span>
                          <span style={{ fontSize: '1.1rem', fontWeight: 800, color: '#ffffff', display: 'flex', alignItems: 'center', gap: '2px' }}>
                            {day.key === 'cn' ? '🎯' : day.desc}
                            {isDayCore && <span style={{ fontSize: '0.9rem', color: '#ef4444' }} title="Trọng tâm ôn thi">🔥</span>}
                          </span>
                          
                          <div className="day-badges" style={{ height: '6px' }}>
                            {hasStudy && (
                              <div className={`badge-dot ${plan.subject_id === 1 ? 'math' : (plan.subject_id === 2 ? 'viet' : 'eng')}`} />
                            )}
                            {hasExam && <div className="badge-dot recall" />}
                            {day.key !== 'cn' && stats.due_cards > 0 && isRealToday && (
                              <div className="badge-dot recall" />
                            )}
                          </div>
                        </div>
                      );
                    })}
                  </div>

                  {/* Selected Day Details Panel */}
                  <div style={{ 
                    background: 'rgba(0, 0, 0, 0.2)', 
                    border: '1px solid var(--color-girl-border)', 
                    borderRadius: '16px', 
                    padding: '1.25rem', 
                    marginTop: '0.5rem',
                    position: 'relative'
                  }}>
                    <span className="girl-badge" style={{ position: 'absolute', top: '12px', right: '12px' }}>
                      Chi Tiết Nhiệm Vụ 🧁
                    </span>
                    
                    <h4 style={{ margin: '0 0 8px 0', fontSize: '1.1rem', color: '#ffffff', display: 'flex', alignItems: 'center', gap: '6px' }}>
                      <span>{WEEKDAYS.find(d => d.key === selectedDayKey)?.label}</span>
                      <span style={{ color: 'var(--color-text-muted)', fontSize: '0.85rem' }}>({WEEKDAYS.find(d => d.key === selectedDayKey)?.desc})</span>
                    </h4>

                    {selectedDayPlan ? (
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                        <div style={{ fontWeight: 700, fontSize: '0.95rem', color: selectedDayPlan.subject_id === 1 ? 'var(--color-math)' : (selectedDayPlan.subject_id === 2 ? 'var(--color-viet)' : (selectedDayPlan.subject_id === 3 ? 'var(--color-eng)' : 'var(--color-girl)')) }}>
                          {selectedDayPlan.title || `${selectedDayPlan.subject_name || ''} - ${selectedDayPlan.chapter_name || ''}`}
                        </div>
                        <p style={{ margin: 0, fontSize: '0.85rem', color: 'var(--color-text-muted)', lineHeight: '1.4' }}>
                          {selectedDayPlan.desc}
                        </p>
                      </div>
                    ) : (
                      <span style={{ fontSize: '0.85rem', color: 'var(--color-text-muted)' }}>Hôm nay không có kế hoạch cụ thể. Bé tự ôn tập nhé!</span>
                    )}

                    {/* Active Recall Call To Action inside Selected Day */}
                    <div style={{ marginTop: '1.25rem', paddingTop: '1rem', borderTop: '1px solid rgba(255,255,255,0.05)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
                      <div>
                        <div style={{ fontSize: '0.85rem', fontWeight: 600, color: '#ffffff' }}>Thẻ ôn tập đến hạn hôm nay:</div>
                        <div style={{ fontSize: '0.75rem', color: 'var(--color-text-muted)' }}>
                          Hệ thống lưu trữ lặp lại ngắt quãng để ghi nhớ sâu.
                        </div>
                      </div>
                      
                      {stats.due_cards > 0 ? (
                        <button 
                          className="girl-btn-primary" 
                          onClick={() => startStudySession()}
                          style={{ fontSize: '0.85rem', padding: '8px 16px' }}
                        >
                          <BrainCircuit size={16} />
                          Ôn Tập {stats.due_cards} Thẻ 🧠
                        </button>
                      ) : (
                        <span style={{ fontSize: '0.85rem', color: 'var(--color-eng)', fontWeight: 600, display: 'flex', alignItems: 'center', gap: '4px' }}>
                          ✨ Đã hoàn thành tất cả thẻ!
                        </span>
                      )}
                    </div>
                  </div>

                </div>

                {/* Pomodoro Timer Widget inside Left Column */}
                <div className="girl-card" style={{ display: 'grid', gridTemplateColumns: '1fr 1.2fr', gap: '1.5rem', alignItems: 'center' }}>
                  <div style={{ textAlign: 'center' }}>
                    <div className="pomodoro-ring-container" style={{ 
                      width: '110px', 
                      height: '110px', 
                      border: '4px solid var(--color-girl-border)', 
                      borderRadius: '50%',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      boxShadow: pomodoroActive ? '0 0 20px rgba(244, 63, 94, 0.3)' : 'none',
                      animation: pomodoroActive ? 'pulse-glow 2s infinite' : 'none'
                    }}>
                      <div className="pomodoro-time" style={{ fontSize: '1.4rem', fontWeight: 800, color: pomodoroActive ? 'var(--color-girl)' : '#ffffff' }}>
                        {formatTime(pomodoroTime)}
                      </div>
                    </div>
                  </div>

                  <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                    <h4 style={{ margin: 0, fontSize: '1.05rem', color: '#ffffff', display: 'flex', alignItems: 'center', gap: '6px' }}>
                      <Clock size={16} style={{ color: 'var(--color-girl)' }} />
                      Đồng Hồ Tập Trung Pomodoro
                    </h4>
                    <p style={{ margin: 0, fontSize: '0.75rem', color: 'var(--color-text-muted)', lineHeight: '1.4' }}>
                      Học tập trung 25 phút để làm bài tập trên TAK12, sau đó nghỉ ngơi 5 phút con nhé.
                    </p>
                    
                    <div style={{ display: 'flex', gap: '8px', marginTop: '4px' }}>
                      <button 
                        className="girl-btn-primary" 
                        onClick={() => setPomodoroActive(!pomodoroActive)}
                        style={{ flex: 1, fontSize: '0.8rem', padding: '6px 12px', borderRadius: '8px' }}
                      >
                        {pomodoroActive ? 'Tạm Dừng ⏸️' : 'Bắt Đầu ▶️'}
                      </button>
                      <button 
                        onClick={() => { setPomodoroActive(false); setPomodoroTime(1500); }}
                        style={{ 
                          background: 'rgba(255,255,255,0.05)', 
                          border: '1px solid var(--color-girl-border)', 
                          color: '#ffffff', 
                          borderRadius: '8px', 
                          padding: '6px 12px', 
                          cursor: 'pointer' 
                        }}
                      >
                        <RefreshCw size={14} />
                      </button>
                    </div>
                  </div>
                </div>

              </div>

              {/* Right Column: Statistics & 10-Month Roadmap */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
                
                {/* Stats Widget (Streak & Score) */}
                <div className="girl-card" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', padding: '1.25rem' }}>
                  <div style={{ 
                    background: 'rgba(255, 120, 50, 0.08)', 
                    border: '1px solid rgba(255, 120, 50, 0.25)', 
                    borderRadius: '16px', 
                    padding: '12px', 
                    textAlign: 'center' 
                  }}>
                    <Flame size={24} style={{ color: 'var(--color-viet)', margin: '0 auto 6px auto' }} />
                    <div style={{ fontSize: '0.75rem', color: 'var(--color-text-muted)', fontWeight: 600 }}>Học Liên Tục</div>
                    <div style={{ fontSize: '1.4rem', fontWeight: 800, color: 'var(--color-viet)', marginTop: '2px' }}>
                      {stats.streak_days} Ngày 🔥
                    </div>
                  </div>

                  <div style={{ 
                    background: 'rgba(244, 63, 94, 0.08)', 
                    border: '1px solid var(--color-girl-border)', 
                    borderRadius: '16px', 
                    padding: '12px', 
                    textAlign: 'center' 
                  }}>
                    <Trophy size={24} style={{ color: 'var(--color-girl)', margin: '0 auto 6px auto' }} />
                    <div style={{ fontSize: '0.75rem', color: 'var(--color-text-muted)', fontWeight: 600 }}>Điểm Học Tập</div>
                    <div style={{ fontSize: '1.4rem', fontWeight: 800, color: 'var(--color-girl)', marginTop: '2px' }}>
                      {stats.total_score} XP 🏆
                    </div>
                  </div>
                </div>

                {/* Daily Due Topics Spaced Repetition Widget */}
                <div className="girl-card" style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                  <h3 style={{ margin: 0, fontSize: '1.15rem', color: '#ffffff', display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <Target size={18} style={{ color: 'var(--color-girl)' }} />
                    Chủ Điểm Cần Ôn Hôm Nay
                  </h3>
                  
                  {dueChapters.length === 0 ? (
                    <div style={{ textAlign: 'center', padding: '1rem', background: 'rgba(16, 185, 129, 0.05)', border: '1px solid rgba(16, 185, 129, 0.15)', borderRadius: '12px' }}>
                      <span style={{ fontSize: '1.8rem' }}>🎉</span>
                      <p style={{ margin: '8px 0 0 0', fontSize: '0.85rem', color: '#10b981', fontWeight: 600, lineHeight: 1.4 }}>
                        Tuyệt vời! Con đã hoàn thành tất cả chuyên đề cần ôn tập. Hãy tiếp tục giữ vững phong độ nhé!
                      </p>
                    </div>
                  ) : (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                      <p style={{ margin: 0, fontSize: '0.8rem', color: 'var(--color-text-muted)', lineHeight: 1.4 }}>
                        Lặp lại ngắt quãng (Leitner) nhắc con ôn tập các chủ điểm này để tránh bị quên kiến thức:
                      </p>
                      
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                        {dueChapters.slice(0, 3).map(ch => {
                          const subj = subjects.find(s => s.id === ch.subject_id);
                          const subjectEmoji = ch.subject_id === 1 ? '📐' : ch.subject_id === 2 ? '✍️' : '🇬🇧';
                          return (
                            <div 
                              key={ch.id} 
                              style={{ 
                                display: 'flex', 
                                justifyItems: 'center', 
                                justifyContent: 'space-between', 
                                alignItems: 'center',
                                padding: '8px 12px', 
                                background: 'rgba(255,255,255,0.02)', 
                                border: '1px solid var(--glass-border)', 
                                borderRadius: '10px' 
                              }}
                            >
                              <div style={{ flex: 1, paddingRight: '8px' }}>
                                <div style={{ fontSize: '0.7rem', color: subj?.id === 1 ? 'var(--color-math)' : subj?.id === 2 ? 'var(--color-viet)' : 'var(--color-eng)', fontWeight: 'bold' }}>
                                  {subjectEmoji} {subj?.name || 'Môn học'}
                                </div>
                                <div style={{ fontSize: '0.8rem', fontWeight: 600, color: '#ffffff', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', maxWidth: '180px' }} title={ch.title_vn || ch.name}>
                                  {ch.title_vn || ch.name}
                                </div>
                              </div>
                              <button
                                onClick={() => startTopicPractice(ch)}
                                className="action-btn"
                                style={{
                                  padding: '4px 10px',
                                  fontSize: '0.75rem',
                                  borderRadius: '6px',
                                  background: 'linear-gradient(135deg, var(--color-girl) 0%, var(--color-primary) 100%)',
                                  color: '#fff',
                                  border: 'none',
                                  fontWeight: 'bold',
                                  cursor: 'pointer'
                                }}
                              >
                                Ôn Ngay
                              </button>
                            </div>
                          );
                        })}
                      </div>

                      {dueChapters.length > 3 && (
                        <button
                          onClick={() => setActiveTab('topics')}
                          style={{
                            background: 'none',
                            border: 'none',
                            color: 'var(--color-girl)',
                            fontSize: '0.75rem',
                            fontWeight: 'bold',
                            cursor: 'pointer',
                            textAlign: 'left',
                            padding: '4px 0',
                            display: 'flex',
                            alignItems: 'center',
                            gap: '4px'
                          }}
                        >
                          Xem thêm {dueChapters.length - 3} chủ điểm ôn tập khác <ArrowRight size={12} />
                        </button>
                      )}
                    </div>
                  )}
                </div>

                {/* 10-Month Roadmap Widget */}
                <div className="girl-card" style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                  <h3 style={{ margin: 0, fontSize: '1.15rem', color: '#ffffff', display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <TrendingUp size={18} style={{ color: 'var(--color-girl)' }} />
                    Lộ Trình Tổng Thể 10 Tháng
                  </h3>
                  
                  <p style={{ margin: 0, fontSize: '0.75rem', color: 'var(--color-text-muted)', lineHeight: '1.4' }}>
                    Click vào bông hoa các tháng để xem chi tiết mục tiêu và chuyên đề tương ứng của tháng đó:
                  </p>

                  {/* Horizontal 花 (flower) timeline track */}
                  <div style={{ position: 'relative', display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '1rem 0.5rem', margin: '0.5rem 0' }}>
                    <div className="flower-path-line" />
                    {MONTHS_MAP.map(m => {
                      let statusClass = '';
                      if (m.id === currentMonthIndex) {
                        statusClass = 'active';
                      } else if (m.id < currentMonthIndex) {
                        statusClass = 'completed';
                      }
                      
                      return (
                        <div 
                          key={m.id} 
                          className={`flower-timeline-node ${statusClass}`}
                          onClick={() => setCurrentMonthIndex(m.id)}
                          style={{ cursor: 'pointer', zIndex: 5, position: 'relative' }}
                          title={`${m.name}: ${m.desc}`}
                        >
                          {m.id === currentMonthIndex ? '🌸' : m.id}
                        </div>
                      );
                    })}
                  </div>

                  {/* Month target details details display */}
                  <div style={{ 
                    background: 'rgba(0, 0, 0, 0.25)', 
                    border: '1px solid rgba(244, 63, 94, 0.15)', 
                    borderRadius: '12px', 
                    padding: '12px',
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '8px'
                  }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <span style={{ fontSize: '0.9rem', fontWeight: 800, color: 'var(--color-girl)' }}>
                        {currentMonthObj.name}
                      </span>
                      <span style={{ 
                        fontSize: '0.7rem', 
                        fontWeight: 700, 
                        color: currentMonthObj.phase === 'theory' ? 'var(--color-primary)' : 'var(--color-eng)',
                        background: currentMonthObj.phase === 'theory' ? 'var(--color-primary-bg)' : 'rgba(16, 185, 129, 0.12)',
                        padding: '2px 6px',
                        borderRadius: '4px'
                      }}>
                        {currentMonthObj.phase === 'theory' ? 'Học Lý Thuyết' : (currentMonthObj.phase === 'exam' ? 'Luyện Đề Thi' : 'Thi Tuyển Sinh')}
                      </span>
                    </div>

                    <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#ffffff' }}>
                      Mục tiêu: {currentMonthObj.desc}
                    </div>

                    {/* Subjects syllabus details */}
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', fontSize: '0.75rem', marginTop: '4px', borderTop: '1px solid rgba(255,255,255,0.05)', paddingTop: '8px' }}>
                      {CURRICULUM_DISTRIBUTION[currentMonthIndex] ? (
                        <>
                          <div>
                            <strong style={{ color: 'var(--color-math)' }}>Toán: </strong> 
                            {CURRICULUM_DISTRIBUTION[currentMonthIndex][1].name}
                            <span style={{ color: 'var(--color-text-subtle)', display: 'block', fontSize: '0.7rem', marginTop: '2px' }}>
                              (Đầu mục con: {(SUB_TOPICS_MAP[CURRICULUM_DISTRIBUTION[currentMonthIndex][1].id] || []).map(s => s.name).join(', ')})
                            </span>
                          </div>
                          <div>
                            <strong style={{ color: 'var(--color-viet)' }}>Tiếng Việt: </strong> 
                            {CURRICULUM_DISTRIBUTION[currentMonthIndex][2].name}
                            <span style={{ color: 'var(--color-text-subtle)', display: 'block', fontSize: '0.7rem', marginTop: '2px' }}>
                              (Đầu mục con: {(SUB_TOPICS_MAP[CURRICULUM_DISTRIBUTION[currentMonthIndex][2].id] || []).map(s => s.name).join(', ')})
                            </span>
                          </div>
                          <div>
                            <strong style={{ color: 'var(--color-eng)' }}>Tiếng Anh: </strong> 
                            {CURRICULUM_DISTRIBUTION[currentMonthIndex][3].name}
                            <span style={{ color: 'var(--color-text-subtle)', display: 'block', fontSize: '0.7rem', marginTop: '2px' }}>
                              (Đầu mục con: {(SUB_TOPICS_MAP[CURRICULUM_DISTRIBUTION[currentMonthIndex][3].id] || []).map(s => s.name).join(', ')})
                            </span>
                          </div>
                        </>
                      ) : (
                        <div style={{ fontStyle: 'italic', color: 'var(--color-text-muted)' }}>
                          Giai đoạn luyện đề và kỳ thi chính thức. Tập trung luyện toàn bộ đề thi tổng hợp trên TAK12.
                        </div>
                      )}
                    </div>
                  </div>

                </div>

              </div>

            </div>

          </div>
        )}

        {/* Dashboard Tab: Calendar Schedule & Due Recall */}
        {activeTab === 'dashboard' && (
          <div style={{ animation: 'slide-in 0.4s ease' }}>
            
            {/* Header / Month-Week Selector */}
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem', flexWrap: 'wrap', gap: '10px' }}>
              <div>
                <h1 style={{ margin: 0, fontSize: '1.8rem', fontWeight: 800 }}>Kế Hoạch & Lịch Trình Học Hôm Nay</h1>
                <div style={{ fontSize: '0.9rem', color: 'var(--color-text-muted)', display: 'flex', alignItems: 'center', gap: '6px', marginTop: '4px', flexWrap: 'wrap' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                    <CalendarIcon size={16} />
                    <span>Con đang ở: <strong>{currentMonthObj.name} ({currentMonthObj.desc})</strong> - Tuần {currentWeekIndex}</span>
                  </div>
                  <span style={{ color: 'var(--color-text-subtle)' }}>•</span>
                  <div style={{ 
                    display: 'flex', 
                    alignItems: 'center', 
                    gap: '6px', 
                    background: 'rgba(255, 255, 255, 0.03)',
                    border: '1px solid var(--glass-border)',
                    padding: '2px 8px',
                    borderRadius: '6px',
                    color: 'var(--color-accent-amber)'
                  }}>
                    <Clock size={14} />
                    <LiveClock />
                  </div>
                </div>
              </div>


              {/* Selector dropdowns for month/week */}
              <div style={{ display: 'flex', gap: '8px' }}>
                <select 
                  className="input-field" 
                  value={currentMonthIndex} 
                  onChange={(e) => setCurrentMonthIndex(parseInt(e.target.value))}
                  style={{ width: '150px', padding: '6px 12px' }}
                >
                  {MONTHS_MAP.map(m => <option key={m.id} value={m.id}>{m.name}</option>)}
                </select>

                {currentMonthObj.phase !== 'final' && (
                  <select 
                    className="input-field" 
                    value={currentWeekIndex} 
                    onChange={(e) => setCurrentWeekIndex(parseInt(e.target.value))}
                    style={{ width: '100px', padding: '6px 12px' }}
                  >
                    {[1, 2, 3, 4].map(w => <option key={w} value={w}>Tuần {w}</option>)}
                  </select>
                )}
              </div>
            </div>

            {/* Daily Motivational Quote for Hoàng My */}
            <div style={{ 
              background: 'linear-gradient(135deg, rgba(244, 63, 94, 0.15) 0%, rgba(120, 100, 255, 0.1) 100%)',
              border: '1px solid rgba(244, 63, 94, 0.25)',
              borderRadius: '12px',
              padding: '12px 18px',
              marginBottom: '1.5rem',
              display: 'flex',
              alignItems: 'center',
              gap: '12px',
              boxShadow: '0 4px 15px rgba(244, 63, 94, 0.1)'
            }}>
              <span style={{ fontSize: '1.5rem' }}>🌸</span>
              <div>
                <div style={{ fontSize: '0.75rem', color: 'var(--color-girl)', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.05em' }}>Lời động viên hôm nay cho con gái Hoàng My:</div>
                <div style={{ fontSize: '0.95rem', fontWeight: 600, color: '#ffffff', marginTop: '2px', fontStyle: 'italic' }}>
                  "{getDailyQuote()}"
                </div>
              </div>
            </div>

            {/* Weekly Calendar Grid (Horizontal Days) */}
            <div className="week-grid">
              {WEEKDAYS.map(day => {
                const isActive = selectedDayKey === day.key;
                
                // Check if this day has a lesson scheduled
                const plan = getDayPlanDetails(currentMonthIndex, currentWeekIndex, day.key);
                const hasStudy = plan && plan.type === 'study_theory';
                const hasExam = plan && plan.type === 'exam_practice';

                const dayChObj = (plan && plan.chapter_id) ? chapters.find(c => c.id === plan.chapter_id) : null;
                const isDayCore = dayChObj ? isCoreTopic(dayChObj) : false;

                return (
                  <div 
                    key={day.key}
                    className={`day-card ${isActive ? 'active' : ''}`}
                    onClick={() => setSelectedDayKey(day.key)}
                  >
                    <span className="day-name">{day.label}</span>
                    <span className="day-num" style={{ color: isActive ? 'var(--color-primary)' : '#ffffff', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '2px' }}>
                      {day.key === 'cn' ? '🎯' : day.desc}
                      {isDayCore && <span style={{ fontSize: '0.9rem', color: '#ef4444' }} title="Trọng tâm ôn thi">🔥</span>}
                    </span>
                    <div className="day-badges">
                      {hasStudy && (
                        <div className={`badge-dot ${plan.subject_id === 1 ? 'math' : (plan.subject_id === 2 ? 'viet' : 'eng')}`} title="Có bài học lý thuyết mới" />
                      )}
                      {hasExam && <div className="badge-dot recall" title="Có lịch luyện đề thi" />}
                      {/* Red dot if there are cards due to review today (only for today indicator) */}
                      {day.key !== 'cn' && stats.due_cards > 0 && day.key === 't3' && (
                        <div className="badge-dot recall" title="Có thẻ cần ôn tập" />
                      )}
                    </div>
                  </div>
                );
              })}
            </div>

            {/* Selected Day Details Panel */}
            <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '1.5rem' }}>
              
              {/* Daily tasks details */}
              <div className="premium-card" style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
                <h3 style={{ margin: 0, borderBottom: '1px solid var(--glass-border)', paddingBottom: '0.75rem', display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <BookMarked size={20} style={{ color: 'var(--color-primary)' }} />
                  Nhiệm vụ học {WEEKDAYS.find(d => d.key === selectedDayKey)?.label}:
                </h3>

                {selectedDayPlan ? (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
                    
                    {/* Render according to day task type */}
                    {selectedDayPlan.type === 'study_theory' && (
                      <div style={{ 
                        background: 'rgba(255,255,255,0.02)', 
                        border: '1px solid var(--glass-border)', 
                        padding: '1.5rem', 
                        borderRadius: '12px',
                        display: 'flex',
                        flexDirection: 'column',
                        gap: '12px'
                      }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                          <span style={{ 
                            fontSize: '0.75rem', 
                            fontWeight: 'bold', 
                            background: selectedDayPlan.subject_id === 1 ? 'var(--color-math-bg)' : (selectedDayPlan.subject_id === 2 ? 'var(--color-viet-bg)' : 'var(--color-eng-bg)'), 
                            color: selectedDayPlan.subject_id === 1 ? 'var(--color-math)' : (selectedDayPlan.subject_id === 2 ? 'var(--color-viet)' : 'var(--color-eng)'),
                            padding: '4px 10px',
                            borderRadius: '99px',
                            border: `1px solid ${selectedDayPlan.subject_id === 1 ? 'var(--color-math-border)' : (selectedDayPlan.subject_id === 2 ? 'var(--color-viet-border)' : 'var(--color-eng-border)')}`
                          }}>
                            Môn học: {selectedDayPlan.subject_name}
                          </span>
                          <a 
                            href={(() => {
                              const ch = chapters.find(c => c.id === selectedDayPlan.chapter_id);
                              return ch && ch.url ? (ch.url.startsWith('http') ? ch.url : `https://tak12.com${ch.url}`) : 'https://tak12.com';
                            })()} 
                            target="_blank" 
                            rel="noreferrer"
                            style={{ display: 'flex', alignItems: 'center', gap: '4px', fontSize: '0.8rem', color: 'var(--color-primary)', textDecoration: 'none' }}
                          >
                            Học trên TAK12 <ExternalLink size={14} />
                          </a>
                        </div>

                        <div>
                          <h4 style={{ margin: '0 0 6px 0', fontSize: '1.3rem', fontWeight: 800, display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
                            {(() => {
                              const chObj = chapters.find(c => c.id === selectedDayPlan.chapter_id);
                              return chObj && isCoreTopic(chObj) ? (
                                <span style={{
                                  fontSize: '0.75rem',
                                  padding: '4px 10px',
                                  borderRadius: '6px',
                                  background: 'rgba(239, 68, 68, 0.15)',
                                  color: '#ef4444',
                                  fontWeight: 'bold',
                                  border: '1px solid rgba(239, 68, 68, 0.3)'
                                }}>
                                  🔥 Trọng tâm ôn thi
                                </span>
                              ) : null;
                            })()}
                            <span>{selectedDayPlan.chapter_name}</span>
                          </h4>
                          <p style={{ margin: 0, color: 'var(--color-text-muted)', fontSize: '0.9rem', lineHeight: '1.5' }}>
                            {selectedDayPlan.desc}
                          </p>
                          {(() => {
                            const chObj = chapters.find(c => c.id === selectedDayPlan.chapter_id);
                            if (chObj && chObj.theory) {
                              return (
                                <button
                                  onClick={() => setViewingTheoryTopic(chObj)}
                                  className="btn-primary"
                                  style={{
                                    marginTop: '12px',
                                    padding: '8px 16px',
                                    borderRadius: '8px',
                                    background: 'rgba(255, 255, 255, 0.05)',
                                    border: '1px solid var(--glass-border)',
                                    color: '#fff',
                                    fontSize: '0.85rem',
                                    fontWeight: 'bold',
                                    cursor: 'pointer',
                                    display: 'flex',
                                    alignItems: 'center',
                                    gap: '6px',
                                    width: 'fit-content'
                                  }}
                                >
                                  📖 Xem Tóm Tắt Lý Thuyết (Local)
                                </button>
                              );
                            }
                            return null;
                          })()}
                        </div>

                        {/* Completed Checkbox */}
                        <div style={{ 
                          marginTop: '0.5rem',
                          borderTop: '1px solid rgba(255,255,255,0.05)', 
                          paddingTop: '1rem',
                          display: 'flex',
                          justifyContent: 'space-between',
                          alignItems: 'center'
                        }}>
                          <span style={{ fontSize: '0.85rem', color: 'var(--color-text-subtle)' }}>
                            Sau khi học xong trên TAK12, bé click nút bên cạnh để hoàn thành:
                          </span>
                          
                          {/* Unique key for this specific month, week, day, chapter */}
                          {(() => {
                            const lessonKey = `${currentMonthIndex}_${currentWeekIndex}_${selectedDayKey}_${selectedDayPlan.chapter_id}`;
                            const isDone = completedLessons[lessonKey];
                            return (
                              <button
                                onClick={() => toggleLessonComplete(lessonKey, selectedDayPlan.chapter_id)}
                                className="btn-primary"
                                style={{ 
                                  background: isDone ? 'rgba(16, 185, 129, 0.15)' : 'var(--color-primary)',
                                  border: isDone ? '1px solid rgba(16, 185, 129, 0.3)' : 'none',
                                  color: isDone ? 'var(--color-eng)' : '#ffffff',
                                  padding: '0.5rem 1rem',
                                  fontSize: '0.85rem',
                                  display: 'flex',
                                  alignItems: 'center',
                                  gap: '6px'
                                }}
                              >
                                {isDone ? (
                                  <>
                                    <CheckCircle2 size={16} /> <span>Đã học xong lý thuyết</span>
                                  </>
                                ) : (
                                  <>
                                    <span>Đánh dấu Đã học xong</span>
                                  </>
                                )}
                              </button>
                            );
                          })()}
                        </div>
                      </div>
                    )}

                    {selectedDayPlan.type === 'exam_practice' && (
                      <div style={{ 
                        background: 'rgba(255, 255, 255, 0.02)', 
                        border: '1px solid var(--glass-border)', 
                        padding: '1.5rem', 
                        borderRadius: '12px',
                        display: 'flex',
                        flexDirection: 'column',
                        gap: '12px'
                      }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                          <span style={{ fontSize: '0.75rem', fontWeight: 'bold', background: 'rgba(120, 100, 255, 0.15)', color: 'var(--color-primary)', padding: '4px 10px', borderRadius: '99px' }}>
                            Giai đoạn: LUYỆN ĐỀ
                          </span>
                          <a href="https://tak12.com" target="_blank" rel="noreferrer" style={{ display: 'flex', alignItems: 'center', gap: '4px', fontSize: '0.8rem', color: 'var(--color-primary)', textDecoration: 'none' }}>
                            Mở TAK12 <ExternalLink size={14} />
                          </a>
                        </div>
                        <h4 style={{ margin: '0 0 6px 0', fontSize: '1.3rem', fontWeight: 800 }}>{selectedDayPlan.title}</h4>
                        <p style={{ margin: 0, color: 'var(--color-text-muted)', fontSize: '0.9rem' }}>{selectedDayPlan.desc}</p>
                        <div style={{ marginTop: '0.5rem', borderTop: '1px solid rgba(255,255,255,0.05)', paddingTop: '1rem', display: 'flex', gap: '10px' }}>
                          <button className="btn-primary" onClick={() => setActiveTab('parent')} style={{ fontSize: '0.85rem' }}>
                            Nhập kết quả điểm & Câu sai đề thi
                          </button>
                        </div>
                      </div>
                    )}

                    {selectedDayPlan.type === 'exam_recall' && (
                      <div style={{ background: 'rgba(255, 255, 255, 0.02)', border: '1px solid var(--glass-border)', padding: '1.5rem', borderRadius: '12px' }}>
                        <h4 style={{ margin: '0 0 6px 0', fontSize: '1.2rem', fontWeight: 800 }}>{selectedDayPlan.title}</h4>
                        <p style={{ margin: 0, color: 'var(--color-text-muted)', fontSize: '0.9rem', marginBottom: '1rem' }}>{selectedDayPlan.desc}</p>
                        <button className="btn-primary" onClick={() => startStudySession()} style={{ fontSize: '0.85rem' }}>
                          Bắt đầu Recall kho lỗi sai ({stats.due_cards} câu đến hạn)
                        </button>
                      </div>
                    )}

                    {selectedDayPlan.type === 'recall_only' && (
                      <div style={{ background: 'rgba(255, 255, 255, 0.02)', border: '1px solid var(--glass-border)', padding: '1.5rem', borderRadius: '12px' }}>
                        <h4 style={{ margin: '0 0 6px 0', fontSize: '1.2rem', fontWeight: 800 }}>{selectedDayPlan.title}</h4>
                        <p style={{ margin: 0, color: 'var(--color-text-muted)', fontSize: '0.9rem', marginBottom: '1rem' }}>{selectedDayPlan.desc}</p>
                        <div style={{ display: 'flex', gap: '10px' }}>
                          <button className="btn-primary" onClick={() => startStudySession()} style={{ fontSize: '0.85rem' }}>
                            Ôn Tập Hàng Đợi ({stats.due_cards} thẻ)
                          </button>
                        </div>
                      </div>
                    )}

                    {selectedDayPlan.type === 'final_exam' && (
                      <div style={{ background: 'rgba(239, 68, 68, 0.08)', border: '1px solid rgba(239, 68, 68, 0.25)', padding: '1.5rem', borderRadius: '12px', textAlign: 'center' }}>
                        <Trophy size={48} style={{ color: 'var(--color-accent-amber)', margin: '0 auto 10px auto' }} />
                        <h4 style={{ margin: '0 0 6px 0', fontSize: '1.3rem', fontWeight: 800, color: '#ffffff' }}>{selectedDayPlan.title}</h4>
                        <p style={{ margin: 0, color: 'var(--color-text-muted)', fontSize: '0.95rem' }}>{selectedDayPlan.desc}</p>
                      </div>
                    )}

                  </div>
                ) : (
                  <p style={{ color: 'var(--color-text-muted)' }}>Chưa cấu hình lịch trình cho ngày này.</p>
                )}

                {/* Spaced Repetition Due queue status */}
                <div style={{ borderTop: '1px solid var(--glass-border)', paddingTop: '1.5rem' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
                    <h4 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <Layers size={18} style={{ color: 'var(--color-primary)' }} />
                      Hàng Đợi Ôn Tập (Active Recall Queue)
                    </h4>
                    <span style={{ fontSize: '0.8rem', background: 'rgba(255,255,255,0.05)', padding: '2px 8px', borderRadius: '8px' }}>
                      {stats.due_cards} thẻ cần lặp lại hôm nay
                    </span>
                  </div>

                  {stats.due_cards > 0 ? (
                    <div style={{ background: 'rgba(120, 100, 255, 0.05)', border: '1px solid var(--color-primary-border)', padding: '1.25rem', borderRadius: '12px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <div>
                        <div style={{ fontSize: '1rem', fontWeight: 'bold' }}>Bé có thẻ đến hạn ôn tập!</div>
                        <div style={{ fontSize: '0.85rem', color: 'var(--color-text-muted)' }}>Luyện tập Active Recall giúp ghi nhớ sâu hơn 80% so với đọc lại.</div>
                      </div>
                      <button className="btn-primary" onClick={() => startStudySession()}>
                        Bắt Đầu Ôn Tập
                      </button>
                    </div>
                  ) : (
                    <div style={{ background: 'rgba(255,255,255,0.02)', border: '1px solid var(--glass-border)', padding: '1.25rem', borderRadius: '12px', textAlign: 'center', color: 'var(--color-text-muted)', fontSize: '0.9rem' }}>
                      ✨ Tuyệt vời! Bé không còn thẻ học nào đến hạn cần ôn lại hôm nay.
                    </div>
                  )}
                </div>

              </div>

              {/* Sidebar stats/Pomodoro details */}
              <div className="premium-card" style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem', height: 'fit-content' }}>
                <h3 style={{ margin: 0, fontSize: '1.1rem', display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <Clock size={18} style={{ color: 'var(--color-primary)' }} />
                  Đồng Hồ Tập Trung (Pomodoro)
                </h3>
                <p style={{ margin: 0, fontSize: '0.8rem', color: 'var(--color-text-muted)', lineHeight: '1.4' }}>
                  Học 25 phút, nghỉ 5 phút. Hỗ trợ bé tập trung cao độ và không bị mỏi mắt khi tự học trên TAK12.
                </p>

                <div className="pomodoro-ring-container">
                  <div className="pomodoro-time">{formatTime(pomodoroTime)}</div>
                </div>

                <div style={{ display: 'flex', gap: '8px', width: '100%' }}>
                  <button 
                    className="btn-primary" 
                    onClick={() => setPomodoroActive(!pomodoroActive)}
                    style={{ flex: 1, fontSize: '0.85rem', padding: '0.5rem 0' }}
                  >
                    {pomodoroActive ? 'Tạm Dừng' : 'Bắt Đầu'}
                  </button>
                  <button 
                    onClick={() => { setPomodoroActive(false); setPomodoroTime(1500); }}
                    style={{ background: 'rgba(255,255,255,0.05)', border: '1px solid var(--glass-border)', color: '#ffffff', borderRadius: '10px', padding: '0.5rem 1rem', cursor: 'pointer' }}
                  >
                    <RefreshCw size={16} />
                  </button>
                </div>
              </div>

            </div>

          </div>
        )}

        {/* 10-Month Roadmap Timeline Tab */}
        {activeTab === 'timeline' && (
          <div style={{ animation: 'slide-in 0.4s ease' }}>
            {/* 10 Month Roadmap Track */}
            <div className="premium-card" style={{ marginBottom: '2rem' }}>
              <h3 style={{ marginTop: 0, display: 'flex', alignItems: 'center', gap: '8px' }}>
                <CalendarIcon size={20} className="text-primary" style={{ color: 'var(--color-primary)' }} />
                Lộ Trình Tổng Thể 10 Tháng Ôn Thi Lớp 6
              </h3>
              <p style={{ fontSize: '0.9rem', color: 'var(--color-text-muted)', marginBottom: '1.5rem' }}>
                Từ Tháng 6 đến Tháng 4 năm sau. Click vào từng tháng để xem chi tiết mục tiêu học lý thuyết và luyện đề của con.
              </p>

              <div className="timeline-track">
                {MONTHS_MAP.map(m => {
                  let statusClass = '';
                  if (m.id === currentMonthIndex) {
                    statusClass = 'active';
                  } else if (m.id < currentMonthIndex) {
                    statusClass = 'completed';
                  }
                  return (
                    <div 
                      key={m.id} 
                      className={`timeline-step ${statusClass}`}
                      onClick={() => setCurrentMonthIndex(m.id)}
                      style={{ cursor: 'pointer' }}
                    >
                      <div className="timeline-node">{m.id}</div>
                      <span className="timeline-label">{m.name}</span>
                    </div>
                  );
                })}
              </div>

              {/* Month Detail View */}
              <div style={{ 
                background: 'rgba(0, 0, 0, 0.2)', 
                borderRadius: '12px', 
                padding: '1.25rem', 
                border: '1px solid var(--glass-border)',
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
                flexWrap: 'wrap',
                gap: '12px'
              }}>
                <div>
                  <span style={{ 
                    background: currentMonthObj.phase === 'theory' ? 'var(--color-primary-bg)' : 'rgba(16, 185, 129, 0.15)',
                    border: `1px solid ${currentMonthObj.phase === 'theory' ? 'var(--color-primary-border)' : 'rgba(16, 185, 129, 0.3)'}`,
                    color: currentMonthObj.phase === 'theory' ? 'var(--color-primary)' : 'var(--color-eng)',
                    padding: '2px 8px',
                    borderRadius: '99px',
                    fontSize: '0.75rem',
                    fontWeight: 700,
                    textTransform: 'uppercase'
                  }}>
                    {currentMonthObj.phase === 'theory' ? 'Giai Đoạn Lý Thuyết' : (currentMonthObj.phase === 'exam' ? 'Giai Đoạn Luyện Đề' : 'Kỳ Thi')}
                  </span>
                  <h4 style={{ margin: '8px 0 4px 0', fontSize: '1.15rem' }}>
                    Mục tiêu {currentMonthObj.name}: {currentMonthObj.desc}
                  </h4>
                  <p style={{ margin: 0, fontSize: '0.85rem', color: 'var(--color-text-muted)' }}>
                    {currentMonthObj.phase === 'theory' 
                      ? 'Học lý thuyết và nắm bắt cốt lõi 3 chuyên đề tương ứng của tháng trên TAK12, sau đó lặp lại qua flashcards.'
                      : (currentMonthObj.phase === 'exam' 
                        ? 'Luyện các bộ đề tổng hợp trên TAK12. Tập trung phân tích các câu làm sai và nạp lỗi sai để ôn lặp khoảng cách.'
                        : 'Tham gia kỳ thi tuyển sinh chính thức. Hãy bình tĩnh, tự tin và làm bài hết mình nhé bé!')}
                  </p>
                </div>
                <button 
                  className="btn-primary" 
                  onClick={() => setActiveTab('dashboard')}
                  style={{ fontSize: '0.85rem', padding: '0.5rem 1rem' }}
                >
                  Xem Lịch Tháng Này
                </button>
              </div>
            </div>

            {/* Monthly Chapter List Grid */}
            <div className="premium-card">
              <h3 style={{ marginTop: 0 }}>Danh mục các chuyên đề phân chia trong 6 tháng lý thuyết:</h3>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '1.5rem', marginTop: '1rem' }}>
                {Object.keys(CURRICULUM_DISTRIBUTION).map(monthKey => {
                  const mSyllabus = CURRICULUM_DISTRIBUTION[monthKey];
                  const mName = MONTHS_MAP[monthKey - 1].name;
                  return (
                    <div key={monthKey} style={{ background: 'rgba(255,255,255,0.02)', border: '1px solid var(--glass-border)', padding: '1rem', borderRadius: '12px' }}>
                      <h4 style={{ color: 'var(--color-primary)', marginTop: 0, marginBottom: '8px', borderBottom: '1px solid rgba(255,255,255,0.05)', paddingBottom: '4px' }}>
                        {mName}
                      </h4>
                      <ul style={{ paddingLeft: '1.25rem', fontSize: '0.85rem', color: 'var(--color-text-muted)', display: 'flex', flexDirection: 'column', gap: '10px', margin: 0 }}>
                        <li>
                          <strong style={{ color: 'var(--color-math)' }}>Toán:</strong> {mSyllabus[1].name}
                          <div style={{ fontSize: '0.75rem', color: 'var(--color-text-subtle)', marginLeft: '10px', marginTop: '2px', lineHeight: '1.3' }}>
                            • Đầu mục con: {(SUB_TOPICS_MAP[mSyllabus[1].id] || []).map(s => s.name).join(', ')}
                          </div>
                        </li>
                        <li>
                          <strong style={{ color: 'var(--color-viet)' }}>Tiếng Việt:</strong> {mSyllabus[2].name}
                          <div style={{ fontSize: '0.75rem', color: 'var(--color-text-subtle)', marginLeft: '10px', marginTop: '2px', lineHeight: '1.3' }}>
                            • Đầu mục con: {(SUB_TOPICS_MAP[mSyllabus[2].id] || []).map(s => s.name).join(', ')}
                          </div>
                        </li>
                        <li>
                          <strong style={{ color: 'var(--color-eng)' }}>Tiếng Anh:</strong> {mSyllabus[3].name}
                          <div style={{ fontSize: '0.75rem', color: 'var(--color-text-subtle)', marginLeft: '10px', marginTop: '2px', lineHeight: '1.3' }}>
                            • Đầu mục con: {(SUB_TOPICS_MAP[mSyllabus[3].id] || []).map(s => s.name).join(', ')}
                          </div>
                        </li>
                      </ul>
                    </div>
                  );
                })}
              </div>
            </div>
          </div>
        )}

        {/* Luyện Chuyên Đề Tab */}
        {activeTab === 'topics' && (
          <div style={{ animation: 'slide-in 0.4s ease' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
              <h2 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '10px' }}>
                <span>🎯</span> Luyện Tập Theo Chuyên Đề Học Tập
              </h2>
              <span style={{ fontSize: '0.9rem', color: 'var(--color-text-muted)' }}>
                Tổng số chủ điểm: <strong>{chapters.length} chuyên đề</strong>
              </span>
            </div>

            {/* Subject Selection Tabs */}
            <div style={{ display: 'flex', gap: '10px', marginBottom: '1.5rem', borderBottom: '1px solid var(--glass-border)', paddingBottom: '0.75rem' }}>
              {subjects.map(subj => (
                <button
                  key={subj.id}
                  onClick={() => {
                    setSelectedSubjectId(subj.id);
                    setTopicSearchQuery('');
                  }}
                  style={{
                    padding: '10px 20px',
                    borderRadius: '10px',
                    border: 'none',
                    background: selectedSubjectId === subj.id ? 'var(--color-primary-bg)' : 'transparent',
                    color: selectedSubjectId === subj.id ? 'var(--color-primary)' : 'var(--color-text-muted)',
                    fontWeight: 'bold',
                    cursor: 'pointer',
                    transition: 'all 0.2s',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '8px'
                  }}
                >
                  {subj.id === 1 ? '📐' : subj.id === 2 ? '✍️' : '🇬🇧'} {subj.name} vào 6
                </button>
              ))}
            </div>

            {/* Search & Stats Dashboard */}
            <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'space-between', alignItems: 'center', gap: '1rem', marginBottom: '1.5rem' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '12px', flexWrap: 'wrap' }}>
                <div style={{ position: 'relative', width: '300px' }}>
                  <input
                    type="text"
                    placeholder="🔍 Nhập tên chuyên đề để tìm kiếm..."
                    value={topicSearchQuery}
                    onChange={(e) => setTopicSearchQuery(e.target.value)}
                    style={{
                      width: '100%',
                      padding: '12px 16px',
                      borderRadius: '12px',
                      border: '1px solid var(--glass-border)',
                      background: 'var(--glass-bg)',
                      color: '#fff',
                      fontSize: '0.9rem'
                    }}
                  />
                  {topicSearchQuery && (
                    <button
                      onClick={() => setTopicSearchQuery('')}
                      style={{
                        position: 'absolute',
                        right: '12px',
                        top: '50%',
                        transform: 'translateY(-50%)',
                        background: 'none',
                        border: 'none',
                        color: 'var(--color-text-muted)',
                        cursor: 'pointer'
                      }}
                    >
                      ✕
                    </button>
                  )}
                </div>

                <button
                  onClick={() => setShowCoreOnly(!showCoreOnly)}
                  style={{
                    padding: '10px 16px',
                    borderRadius: '12px',
                    border: '1px solid rgba(255, 255, 255, 0.08)',
                    background: showCoreOnly ? 'rgba(239, 68, 68, 0.15)' : 'rgba(255, 255, 255, 0.03)',
                    borderColor: showCoreOnly ? 'rgba(239, 68, 68, 0.3)' : 'var(--glass-border)',
                    color: showCoreOnly ? '#ef4444' : 'var(--color-text-muted)',
                    fontSize: '0.85rem',
                    fontWeight: 'bold',
                    cursor: 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '6px',
                    transition: 'all 0.2s',
                    boxShadow: showCoreOnly ? '0 0 10px rgba(239, 68, 68, 0.15)' : 'none'
                  }}
                >
                  <span>🔥</span> Chỉ xem trọng tâm ôn thi
                </button>
              </div>

              <div style={{ display: 'flex', gap: '15px' }}>
                <div className="premium-card" style={{ padding: '8px 16px', display: 'flex', alignItems: 'center', gap: '8px', background: 'rgba(255,255,255,0.02)' }}>
                  <span style={{ fontSize: '1.2rem' }}>⏰</span>
                  <div>
                    <div style={{ fontSize: '0.75rem', color: 'var(--color-text-muted)' }}>Cần Ôn Luyện</div>
                    <div style={{ fontSize: '1rem', fontWeight: 'bold', color: 'var(--color-girl)' }}>
                      {dueChapters.filter(c => c.subject_id === selectedSubjectId).length} chuyên đề
                    </div>
                  </div>
                </div>
                <div className="premium-card" style={{ padding: '8px 16px', display: 'flex', alignItems: 'center', gap: '8px', background: 'rgba(255,255,255,0.02)' }}>
                  <span style={{ fontSize: '1.2rem' }}>📈</span>
                  <div>
                    <div style={{ fontSize: '0.75rem', color: 'var(--color-text-muted)' }}>Độ Vững Trung Bình</div>
                    <div style={{ fontSize: '1rem', fontWeight: 'bold', color: 'var(--color-primary)' }}>
                      {(() => {
                        const subjCh = chapters.filter(c => c.subject_id === selectedSubjectId);
                        if (subjCh.length === 0) return '0%';
                        const totalScore = subjCh.reduce((sum, c) => sum + (c.current_score || c.original_score || 0), 0);
                        return `${Math.round(totalScore / subjCh.length)}%`;
                      })()}
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* Parent Chapters (Horizontal Pill Bar) */}
            {!topicSearchQuery && (
              <div 
                className="custom-scrollbar"
                style={{ 
                  display: 'flex', 
                  gap: '8px', 
                  overflowX: 'auto', 
                  paddingBottom: '12px', 
                  marginBottom: '1.5rem',
                  maxWidth: '100%'
                }}
              >
                {(() => {
                  const parentChapters = Array.from(new Set(
                    chapters
                      .filter(c => c.subject_id === selectedSubjectId && c.parent_chapter && (!showCoreOnly || isCoreTopic(c)))
                      .map(c => c.parent_chapter)
                  ));

                  return parentChapters.map(pCh => {
                    const isActive = selectedParentChapter === pCh;
                    return (
                      <button
                        key={pCh}
                        onClick={() => setSelectedParentChapter(pCh)}
                        className={`tag-pill ${isActive ? 'active' : ''}`}
                        style={{
                          whiteSpace: 'nowrap',
                          padding: '8px 16px',
                          borderRadius: '20px',
                          border: 'none',
                          fontSize: '0.85rem',
                          fontWeight: 600,
                          cursor: 'pointer',
                          background: isActive ? 'var(--color-girl-bg)' : 'rgba(255,255,255,0.05)',
                          color: isActive ? 'var(--color-girl)' : 'var(--color-text-muted)',
                          border: isActive ? '1px solid var(--color-girl-border)' : '1px solid transparent',
                          transition: 'all 0.2s'
                        }}
                      >
                        {pCh}
                      </button>
                    );
                  });
                })()}
              </div>
            )}

            {/* Topics Grouped by sub_chapter */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
              {(() => {
                let filteredChapters = chapters.filter(c => c.subject_id === selectedSubjectId);
                
                if (showCoreOnly) {
                  filteredChapters = filteredChapters.filter(isCoreTopic);
                }

                if (topicSearchQuery) {
                  const queryLower = topicSearchQuery.toLowerCase();
                  filteredChapters = filteredChapters.filter(c => 
                    (c.title_vn && c.title_vn.toLowerCase().includes(queryLower)) ||
                    (c.parent_chapter && c.parent_chapter.toLowerCase().includes(queryLower)) ||
                    (c.sub_chapter && c.sub_chapter.toLowerCase().includes(queryLower)) ||
                    (c.name && c.name.toLowerCase().includes(queryLower))
                  );
                } else {
                  filteredChapters = filteredChapters.filter(c => c.parent_chapter === selectedParentChapter);
                }

                if (filteredChapters.length === 0) {
                  return (
                    <div style={{ textAlign: 'center', padding: '3rem', color: 'var(--color-text-muted)' }}>
                      Không tìm thấy chuyên đề nào phù hợp.
                    </div>
                  );
                }

                // Group by sub_chapter
                const grouped = {};
                filteredChapters.forEach(c => {
                  const sub = c.sub_chapter || 'Chuyên đề chung';
                  if (!grouped[sub]) grouped[sub] = [];
                  grouped[sub].push(c);
                });

                return Object.entries(grouped).map(([subTitle, items]) => (
                  <div key={subTitle} style={{ background: 'rgba(255, 255, 255, 0.01)', borderRadius: '16px', padding: '1.5rem', border: '1px solid var(--glass-border)' }}>
                    <h3 style={{ margin: '0 0 1.25rem 0', fontSize: '1.1rem', color: 'var(--color-primary)', display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <span>📂</span> {subTitle}
                    </h3>
                    
                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(340px, 1fr))', gap: '1.25rem' }}>
                      {items.map(item => {
                        const mastery = item.current_score || item.original_score || 0;
                        
                        // Spaced Repetition status badge
                        const isDue = dueChapters.some(dc => dc.id === item.id);
                        let badgeText = '';
                        let badgeBg = '';
                        let badgeColor = '';
                        
                        if (isDue) {
                          badgeText = 'Cần ôn tập ⏰';
                          badgeBg = 'rgba(239, 68, 68, 0.15)';
                          badgeColor = '#ef4444';
                        } else if (item.current_score >= 80) {
                          badgeText = `Hộp ${item.box_number} 🌟`;
                          badgeBg = 'rgba(16, 185, 129, 0.15)';
                          badgeColor = '#10b981';
                        } else if (item.current_score > 0) {
                          badgeText = `Hộp ${item.box_number} ⏳`;
                          badgeBg = 'rgba(245, 158, 11, 0.15)';
                          badgeColor = '#f59e0b';
                        }

                        // Progress color based on score
                        let progressColor = '#ef4444'; // Red
                        if (mastery >= 80) progressColor = '#10b981'; // Green
                        else if (mastery >= 40) progressColor = '#f59e0b'; // Orange/Yellow

                        return (
                          <div 
                            key={item.id} 
                            className="premium-card topic-card"
                            style={{ 
                              display: 'flex', 
                              flexDirection: 'column', 
                              justifyContent: 'space-between', 
                              padding: '1.25rem', 
                              background: 'rgba(0,0,0,0.15)',
                              border: '1px solid var(--glass-border)',
                              borderRadius: '12px',
                              position: 'relative'
                            }}
                          >
                            {badgeText && (
                              <span style={{
                                position: 'absolute',
                                top: '12px',
                                right: '12px',
                                fontSize: '0.7rem',
                                padding: '3px 8px',
                                borderRadius: '6px',
                                background: badgeBg,
                                color: badgeColor,
                                fontWeight: 'bold'
                              }}>
                                {badgeText}
                              </span>
                            )}

                            <div style={{ paddingRight: badgeText ? '85px' : '0' }}>
                              <h4 style={{ margin: '0 0 8px 0', fontSize: '0.95rem', fontWeight: 600, color: '#fff', lineHeight: '1.4', display: 'flex', alignItems: 'center', gap: '6px', flexWrap: 'wrap' }}>
                                {isCoreTopic(item) && (
                                  <span style={{
                                    fontSize: '0.65rem',
                                    padding: '2px 6px',
                                    borderRadius: '4px',
                                    background: 'rgba(239, 68, 68, 0.15)',
                                    color: '#ef4444',
                                    fontWeight: 'bold',
                                    border: '1px solid rgba(239, 68, 68, 0.3)',
                                    whiteSpace: 'nowrap'
                                  }}>
                                    🔥 Trọng tâm
                                  </span>
                                )}
                                <span>{item.title_vn || item.name}</span>
                              </h4>
                              {item.title_en && (
                                <div style={{ fontSize: '0.75rem', color: 'var(--color-text-muted)', marginBottom: '8px', fontStyle: 'italic' }}>
                                  {item.title_en}
                                </div>
                              )}
                            </div>

                            <div style={{ marginTop: '1.25rem' }}>
                              {/* Progress bar */}
                              <div style={{ display: 'flex', alignItems: 'center', justifyItems: 'space-between', gap: '10px', marginBottom: '10px' }}>
                                <div style={{ flex: 1, height: '8px', background: 'rgba(255,255,255,0.05)', borderRadius: '4px', overflow: 'hidden' }}>
                                  <div 
                                    style={{ 
                                      width: `${mastery}%`, 
                                      height: '100%', 
                                      background: `linear-gradient(90deg, ${progressColor} 0%, ${progressColor} 80%, #fff 100%)`,
                                      borderRadius: '4px',
                                      transition: 'width 0.5s ease-out'
                                    }} 
                                  />
                                </div>
                                <span style={{ fontSize: '0.85rem', fontWeight: 'bold', color: progressColor }}>
                                  {mastery}
                                </span>
                              </div>

                              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                <span style={{ fontSize: '0.75rem', color: 'var(--color-text-muted)' }}>
                                  {item.interval_days > 0 ? `Ôn lại sau ${item.interval_days} ngày` : 'Chưa ôn luyện'}
                                </span>
                                
                                <div style={{ display: 'flex', gap: '6px' }}>
                                  {item.theory && (
                                    <button
                                      onClick={() => setViewingTheoryTopic(item)}
                                      className="action-btn"
                                      style={{
                                        padding: '6px 10px',
                                        borderRadius: '8px',
                                        background: 'rgba(255,255,255,0.05)',
                                        border: '1px solid var(--glass-border)',
                                        color: '#fff',
                                        fontSize: '0.75rem',
                                        cursor: 'pointer',
                                        transition: 'all 0.2s'
                                      }}
                                    >
                                      📖 Lý Thuyết
                                    </button>
                                  )}
                                  
                                  <button
                                    onClick={() => startTopicPractice(item)}
                                    className="action-btn"
                                    style={{
                                      padding: '6px 12px',
                                      borderRadius: '8px',
                                      background: isDue ? 'linear-gradient(135deg, var(--color-girl) 0%, var(--color-primary) 100%)' : 'rgba(255,255,255,0.06)',
                                      color: '#fff',
                                      border: 'none',
                                      fontWeight: 'bold',
                                      fontSize: '0.75rem',
                                      cursor: 'pointer',
                                      transition: 'all 0.2s'
                                    }}
                                  >
                                    {isDue ? '⚡ Ôn Ngay' : '🎯 Luyện Tập'}
                                  </button>
                                </div>
                              </div>
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  </div>
                ));
              })()}
            </div>
          </div>
        )}

        {/* Library Tab: View Flashcards */}
        {activeTab === 'library' && (
          <div style={{ animation: 'slide-in 0.4s ease' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
              <h2 style={{ margin: 0 }}>Kho Lưu Trữ Thẻ Ghi Nhớ Active Recall</h2>
              <span style={{ fontSize: '0.9rem', color: 'var(--color-text-muted)' }}>
                Tổng số thẻ ôn tập đã tạo: <strong>{allCards.length} thẻ</strong>
              </span>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '1.5rem', height: 'calc(100vh - 200px)', minHeight: '550px' }}>
              {subjects.map(subj => {
                const subChapters = chapters.filter(c => c.subject_id === subj.id);
                return (
                  <div key={subj.id} className="premium-card" style={{ display: 'flex', flexDirection: 'column', gap: '1rem', height: '100%', maxHeight: '100%', overflow: 'hidden' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--glass-border)', paddingBottom: '0.75rem' }}>
                      <h3 style={{ margin: 0, color: subj.id === 1 ? 'var(--color-math)' : (subj.id === 2 ? 'var(--color-viet)' : 'var(--color-eng)') }}>
                        Môn {subj.name}
                      </h3>
                      <span style={{ fontSize: '0.8rem', background: 'rgba(255,255,255,0.05)', padding: '2px 8px', borderRadius: '8px' }}>
                        {subChapters.length} chương
                      </span>
                    </div>

                    <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', overflowY: 'auto', flex: 1, paddingRight: '4px' }}>
                      {subChapters.map(ch => {
                        const chCards = allCards.filter(card => card.chapter_id === ch.id);
                        const isExpanded = !!expandedChapters[ch.id];
                        const subTopics = SUB_TOPICS_MAP[ch.id] || [];

                        return (
                          <div 
                            key={ch.id} 
                            style={{ 
                              padding: '0.75rem', 
                              background: 'rgba(0,0,0,0.15)', 
                              borderRadius: '10px', 
                              display: 'flex', 
                              flexDirection: 'column',
                              gap: '8px',
                              border: isExpanded ? '1px solid var(--color-primary-border)' : '1px solid transparent'
                            }}
                          >
                            {/* Chapter Header */}
                            <div 
                              style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', cursor: 'pointer' }}
                              onClick={() => setExpandedChapters(prev => ({ ...prev, [ch.id]: !isExpanded }))}
                            >
                              <div style={{ flex: 1, paddingRight: '10px' }}>
                                <div style={{ fontSize: '0.9rem', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '6px' }}>
                                  <ChevronRight size={16} style={{ transform: isExpanded ? 'rotate(90deg)' : 'none', transition: 'transform 0.2s' }} />
                                  {ch.name}
                                </div>
                                <div style={{ fontSize: '0.75rem', color: 'var(--color-text-subtle)', marginLeft: '22px' }}>
                                  Tích lũy: {chCards.length} thẻ recall
                                </div>
                              </div>
                              {chCards.length > 0 && (
                                <button 
                                  className="btn-primary" 
                                  onClick={(e) => {
                                    e.stopPropagation();
                                    setStudySession({ cards: chCards, currentIndex: 0, showAnswer: false, startTime: new Date() });
                                  }}
                                  style={{ padding: '4px 8px', fontSize: '0.75rem' }}
                                >
                                  Luyện cả chương
                                </button>
                              )}
                            </div>

                            {/* Sub-topics list (expanded) */}
                            {isExpanded && (
                              <div style={{ 
                                marginLeft: '22px', 
                                borderLeft: '2px solid var(--glass-border)', 
                                paddingLeft: '10px', 
                                display: 'flex', 
                                flexDirection: 'column', 
                                gap: '8px',
                                marginTop: '4px',
                                paddingBottom: '4px'
                              }}>
                                {subTopics.length > 0 ? (
                                  subTopics.map(sub => {
                                    const subCards = allCards.filter(card => card.chapter_id === ch.id && card.sub_topic_id === sub.id);
                                    return (
                                      <div key={sub.id} style={{ 
                                        display: 'flex', 
                                        justifyContent: 'space-between', 
                                        alignItems: 'center', 
                                        padding: '4px 0', 
                                        borderBottom: '1px solid rgba(255,255,255,0.02)'
                                      }}>
                                        <div style={{ flex: 1, paddingRight: '10px' }}>
                                          <div style={{ fontSize: '0.8rem', color: 'var(--color-text-muted)', fontWeight: 500 }}>{sub.name}</div>
                                          <div style={{ fontSize: '0.7rem', color: 'var(--color-text-subtle)' }}>({subCards.length} thẻ)</div>
                                        </div>
                                        {subCards.length > 0 ? (
                                          <div style={{ display: 'flex', gap: '4px' }}>
                                            <button 
                                              onClick={() => setViewingSubTopic({ name: sub.name, cards: subCards })}
                                              style={{ 
                                                background: 'rgba(255,255,255,0.05)', 
                                                border: '1px solid var(--glass-border)', 
                                                color: '#ffffff', 
                                                padding: '2px 6px', 
                                                borderRadius: '4px', 
                                                fontSize: '0.7rem',
                                                cursor: 'pointer'
                                              }}
                                            >
                                              Xem
                                            </button>
                                            <button 
                                              className="btn-primary" 
                                              onClick={() => setStudySession({ cards: subCards, currentIndex: 0, showAnswer: false, startTime: new Date() })}
                                              style={{ padding: '2px 6px', fontSize: '0.7rem', background: 'var(--color-primary)' }}
                                            >
                                              Luyện
                                            </button>
                                          </div>
                                        ) : (
                                          <span style={{ fontSize: '0.7rem', color: 'var(--color-text-subtle)', fontStyle: 'italic' }}>Chưa có thẻ</span>
                                        )}
                                      </div>
                                    );
                                  })
                                ) : (
                                  <div style={{ fontSize: '0.75rem', color: 'var(--color-text-subtle)', fontStyle: 'italic' }}>Không có mục nhỏ nào.</div>
                                )}
                              </div>
                            )}
                          </div>
                        );
                      })}
                    </div>

                  </div>
                );
              })}
            </div>
          </div>
        )}

        {/* Parent Control Tab */}
        {activeTab === 'parent' && (
          <div style={{ animation: 'slide-in 0.4s ease', display: 'flex', flexDirection: 'column', gap: '2rem' }}>
            
            <div>
              <h2 style={{ margin: 0 }}>Cổng Điều Khiển Của Phụ Huynh (Parent Console)</h2>
              <p style={{ color: 'var(--color-text-muted)', margin: '4px 0 0 0', fontSize: '0.9rem' }}>
                Thiết lập lịch thi thử, tự động sinh thẻ recall từ đoạn văn bản lý thuyết bằng AI (Gemini 1.5 Flash) hoặc ghi nhận câu sai để nhắc con ôn.
              </p>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem' }}>
              
              {/* Manual & AI Flashcard Maker */}
              <div className="premium-card" style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
                <h3 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <Sparkles size={20} style={{ color: 'var(--color-accent-amber)' }} />
                  Tự động sinh thẻ Recall lý thuyết
                </h3>

                <div style={{ display: 'flex', background: 'rgba(0,0,0,0.2)', padding: '4px', borderRadius: '8px', border: '1px solid var(--glass-border)' }}>
                  <button 
                    onClick={() => setAiGeneratedCards([])} 
                    style={{ 
                      flex: 1, 
                      background: aiGeneratedCards.length === 0 ? 'var(--color-primary)' : 'transparent', 
                      border: 'none', 
                      color: '#ffffff', 
                      padding: '6px', 
                      borderRadius: '6px', 
                      fontWeight: 600, 
                      fontSize: '0.85rem',
                      cursor: 'pointer' 
                    }}
                  >
                    Thủ Công
                  </button>
                  <button 
                    onClick={() => setAiGeneratedCards([{ front: 'Đoán từ khuyết...', back: 'Khái niệm chuẩn', hint: 'Gợi ý nhỏ' }])}
                    style={{ 
                      flex: 1, 
                      background: aiGeneratedCards.length > 0 ? 'var(--color-primary)' : 'transparent', 
                      border: 'none', 
                      color: '#ffffff', 
                      padding: '6px', 
                      borderRadius: '6px', 
                      fontWeight: 600, 
                      fontSize: '0.85rem',
                      cursor: 'pointer' 
                    }}
                  >
                    Sinh Thẻ Bằng AI ✨
                  </button>
                </div>

                {aiGeneratedCards.length === 0 ? (
                  /* Manual Form */
                  <form onSubmit={handleCreateCard} style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1.2fr 1.2fr', gap: '12px' }}>
                      <div>
                        <label style={{ fontSize: '0.8rem', color: 'var(--color-text-muted)', display: 'block', marginBottom: '4px' }}>Môn Học</label>
                        <select 
                          className="input-field"
                          value={newCard.subject_id}
                          onChange={(e) => {
                            const val = parseInt(e.target.value);
                            const related = chapters.filter(c => c.subject_id === val);
                            const nextChId = related[0]?.id || 1;
                            const nextSub = SUB_TOPICS_MAP[nextChId] || [];
                            setNewCard({
                              ...newCard,
                              subject_id: val,
                              chapter_id: nextChId,
                              sub_topic_id: nextSub[0]?.id || ''
                            });
                          }}
                        >
                          {subjects.map(s => <option key={s.id} value={s.id}>{s.name}</option>)}
                        </select>
                      </div>
                      <div>
                        <label style={{ fontSize: '0.8rem', color: 'var(--color-text-muted)', display: 'block', marginBottom: '4px' }}>Chuyên đề</label>
                        <select 
                          className="input-field"
                          value={newCard.chapter_id}
                          onChange={(e) => {
                            const chId = parseInt(e.target.value);
                            const nextSub = SUB_TOPICS_MAP[chId] || [];
                            setNewCard({ 
                              ...newCard, 
                              chapter_id: chId,
                              sub_topic_id: nextSub[0]?.id || ''
                            });
                          }}
                        >
                          {chapters.filter(c => c.subject_id === parseInt(newCard.subject_id)).map(ch => (
                            <option key={ch.id} value={ch.id}>{ch.name}</option>
                          ))}
                        </select>
                      </div>
                      <div>
                        <label style={{ fontSize: '0.8rem', color: 'var(--color-text-muted)', display: 'block', marginBottom: '4px' }}>Đầu mục con</label>
                        <select 
                          className="input-field"
                          value={newCard.sub_topic_id}
                          onChange={(e) => setNewCard({ ...newCard, sub_topic_id: parseInt(e.target.value) })}
                        >
                          {(SUB_TOPICS_MAP[newCard.chapter_id] || []).map(sub => (
                            <option key={sub.id} value={sub.id}>{sub.name}</option>
                          ))}
                        </select>
                      </div>
                    </div>

                    <div>
                      <label style={{ fontSize: '0.8rem', color: 'var(--color-text-muted)', display: 'block', marginBottom: '4px' }}>Mặt trước (Câu hỏi)</label>
                      <textarea 
                        className="input-field" 
                        rows="2" 
                        value={newCard.front_content}
                        onChange={(e) => setNewCard({ ...newCard, front_content: e.target.value })}
                        placeholder="Ví dụ: Công thức tính diện tích hình thang là gì?"
                      />
                    </div>

                    <div>
                      <label style={{ fontSize: '0.8rem', color: 'var(--color-text-muted)', display: 'block', marginBottom: '4px' }}>Mặt sau (Đáp án & Giải thích)</label>
                      <textarea 
                        className="input-field" 
                        rows="2" 
                        value={newCard.back_content}
                        onChange={(e) => setNewCard({ ...newCard, back_content: e.target.value })}
                        placeholder="Ví dụ: S = (a + b) x h / 2 (Tổng độ dài 2 đáy nhân chiều cao rồi chia đôi)."
                      />
                    </div>

                    <div>
                      <label style={{ fontSize: '0.8rem', color: 'var(--color-text-muted)', display: 'block', marginBottom: '4px' }}>Gợi ý (Không bắt buộc)</label>
                      <input 
                        type="text" 
                        className="input-field" 
                        value={newCard.hint}
                        onChange={(e) => setNewCard({ ...newCard, hint: e.target.value })}
                        placeholder="Gợi ý: a, b là 2 đáy, h là chiều cao"
                      />
                    </div>

                    <button type="submit" className="btn-primary" style={{ marginTop: '0.5rem' }}>
                      Tạo Thẻ Thủ Công
                    </button>
                  </form>
                ) : (
                  /* AI Generation */
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px' }}>
                      <div>
                        <label style={{ fontSize: '0.8rem', color: 'var(--color-text-muted)', display: 'block', marginBottom: '4px' }}>Chọn Môn</label>
                        <select className="input-field" value={aiSubjectId} onChange={(e) => setAiSubjectId(e.target.value)}>
                          {subjects.map(s => <option key={s.id} value={s.id}>{s.name}</option>)}
                        </select>
                      </div>
                      <div>
                        <label style={{ fontSize: '0.8rem', color: 'var(--color-text-muted)', display: 'block', marginBottom: '4px' }}>Chọn Chương</label>
                        <select className="input-field" value={aiChapterId} onChange={(e) => setAiChapterId(e.target.value)}>
                          {chapters.filter(c => c.subject_id === parseInt(aiSubjectId)).map(ch => (
                            <option key={ch.id} value={ch.id}>{ch.name}</option>
                          ))}
                        </select>
                      </div>
                    </div>

                    <div>
                      <label style={{ fontSize: '0.8rem', color: 'var(--color-text-muted)', display: 'block', marginBottom: '4px' }}>Đoạn văn lý thuyết cốt lõi</label>
                      <textarea 
                        className="input-field" 
                        rows="4" 
                        value={aiText}
                        onChange={(e) => setAiText(e.target.value)}
                        placeholder="Hãy copy dán đoạn lý thuyết hoặc ngữ pháp quan trọng từ TAK12 để AI sinh thẻ..."
                      />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: '10px' }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                        <span style={{ fontSize: '0.85rem' }}>Số thẻ:</span>
                        <input type="number" min="1" max="10" className="input-field" style={{ width: '60px', padding: '4px 8px' }} value={aiCount} onChange={(e) => setAiCount(e.target.value)} />
                      </div>
                      <button 
                        onClick={handleAIGenerate} 
                        className="btn-primary" 
                        disabled={aiLoading}
                        style={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px' }}
                      >
                        {aiLoading ? <RefreshCw className="animate-spin" size={16} /> : <Sparkles size={16} />}
                        <span>{aiLoading ? 'Đang sinh thẻ...' : 'Sinh thẻ bằng AI'}</span>
                      </button>
                    </div>

                    {aiGeneratedCards.length > 1 && (
                      <div style={{ marginTop: '1rem', background: 'rgba(0,0,0,0.3)', padding: '1rem', borderRadius: '10px', border: '1px solid var(--color-primary-border)' }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                          <span style={{ fontSize: '0.85rem', fontWeight: 'bold' }}>Kết quả đề xuất ({aiGeneratedCards.length} câu)</span>
                          <button className="btn-primary" onClick={saveAICards} style={{ padding: '2px 8px', fontSize: '0.75rem' }}>Lưu Tất Cả</button>
                        </div>
                        <div style={{ maxHeight: '180px', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '6px' }}>
                          {aiGeneratedCards.map((c, i) => (
                            <div key={i} style={{ background: 'rgba(255,255,255,0.02)', padding: '6px', borderRadius: '6px', fontSize: '0.75rem', borderLeft: '3px solid var(--color-primary)' }}>
                              <div><strong>Hỏi:</strong> {c.front}</div>
                              <div style={{ color: 'var(--color-eng)', marginTop: '2px' }}><strong>Đáp:</strong> {c.back}</div>
                            </div>
                          ))}
                        </div>
                      </div>
                    )}
                  </div>
                )}
              </div>

              {/* Practice Mock Test & Mistake Card Generator (Tháng 7-10) */}
              <div className="premium-card" style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
                <h3 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <TrendingUp size={20} style={{ color: 'var(--color-math)' }} />
                  Quản lý lỗi sai & Điểm thi thử TAK12
                </h3>
                
                {/* 1. Add exam log */}
                <form onSubmit={handleAddExam} style={{ display: 'flex', flexDirection: 'column', gap: '10px', background: 'rgba(0,0,0,0.15)', padding: '1rem', borderRadius: '12px' }}>
                  <div style={{ fontSize: '0.85rem', fontWeight: 'bold', borderBottom: '1px solid var(--glass-border)', paddingBottom: '4px' }}>
                    1. Nhật ký điểm thi thử mới trên TAK12
                  </div>
                  <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '10px' }}>
                    <input 
                      type="text" 
                      className="input-field" 
                      placeholder="Tên đề: ví dụ Đề Lương Thế Vinh lần 2" 
                      value={newExam.name}
                      onChange={(e) => setNewExam({ ...newExam, name: e.target.value })}
                    />
                    <input 
                      type="text" 
                      className="input-field" 
                      placeholder="Điểm (0-10)" 
                      value={newExam.score}
                      onChange={(e) => setNewExam({ ...newExam, score: e.target.value })}
                    />
                  </div>
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
                    <select className="input-field" value={newExam.subject_id} onChange={(e) => setNewExam({ ...newExam, subject_id: e.target.value })}>
                      {subjects.map(s => <option key={s.id} value={s.id}>{s.name}</option>)}
                    </select>
                    <button type="submit" className="btn-primary" style={{ padding: '0.5rem' }}>Lưu kết quả</button>
                  </div>
                </form>

                {/* 2. Mistake creator */}
                <form onSubmit={handleAddMistake} style={{ display: 'flex', flexDirection: 'column', gap: '10px', background: 'rgba(239, 68, 68, 0.05)', border: '1px solid rgba(239, 68, 68, 0.15)', padding: '1rem', borderRadius: '12px' }}>
                  <div style={{ fontSize: '0.85rem', fontWeight: 'bold', color: 'var(--color-accent-red)', borderBottom: '1px solid rgba(239,68,68,0.15)', paddingBottom: '4px' }}>
                    2. Nạp câu bị sai từ đề thi để lặp Active Recall
                  </div>
                  
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
                    <input 
                      type="text" 
                      className="input-field" 
                      placeholder="Từ bài thi nào?" 
                      value={mistakeCard.exam_name}
                      onChange={(e) => setMistakeCard({ ...mistakeCard, exam_name: e.target.value })}
                    />
                    <select 
                      className="input-field" 
                      value={mistakeCard.chapter_id} 
                      onChange={(e) => {
                        const chId = parseInt(e.target.value);
                        const nextSub = SUB_TOPICS_MAP[chId] || [];
                        setMistakeCard({ 
                          ...mistakeCard, 
                          chapter_id: chId,
                          sub_topic_id: nextSub[0]?.id || ''
                        });
                      }}
                    >
                      {chapters.map(ch => <option key={ch.id} value={ch.id}>{ch.name}</option>)}
                    </select>
                  </div>

                  <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                    <select 
                      className="input-field"
                      value={mistakeCard.sub_topic_id}
                      onChange={(e) => setMistakeCard({ ...mistakeCard, sub_topic_id: parseInt(e.target.value) })}
                    >
                      {(SUB_TOPICS_MAP[mistakeCard.chapter_id] || []).map(sub => (
                        <option key={sub.id} value={sub.id}>{sub.name}</option>
                      ))}
                    </select>
                  </div>

                  <textarea 
                    className="input-field" 
                    rows="2" 
                    placeholder="Câu hỏi bị sai (Ví dụ: Tìm chủ ngữ câu: Hôm nay tôi đi học.)" 
                    value={mistakeCard.front_content}
                    onChange={(e) => setMistakeCard({ ...mistakeCard, front_content: e.target.value })}
                  />

                  <textarea 
                    className="input-field" 
                    rows="2" 
                    placeholder="Đáp án đúng & cách giải thích chuẩn để bé sửa đổi" 
                    value={mistakeCard.back_content}
                    onChange={(e) => setMistakeCard({ ...mistakeCard, back_content: e.target.value })}
                  />

                  <button type="submit" className="btn-primary" style={{ background: 'var(--color-accent-red)', padding: '0.5rem' }}>
                    Nạp thẻ câu sai
                  </button>
                </form>

              </div>
            </div>

            {/* List of logged exams */}
            <div className="premium-card">
              <h3 style={{ marginTop: 0, display: 'flex', alignItems: 'center', gap: '8px' }}>
                <FileText size={20} style={{ color: 'var(--color-primary)' }} />
                Nhật ký điểm số làm đề thi thử
              </h3>
              <div style={{ overflowX: 'auto', marginTop: '1rem' }}>
                <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '0.9rem' }}>
                  <thead>
                    <tr style={{ borderBottom: '1px solid var(--glass-border)', color: 'var(--color-text-muted)' }}>
                      <th style={{ padding: '8px' }}>Đề thi thử</th>
                      <th style={{ padding: '8px' }}>Môn</th>
                      <th style={{ padding: '8px' }}>Điểm đạt được</th>
                      <th style={{ padding: '8px' }}>Ngày nhập</th>
                    </tr>
                  </thead>
                  <tbody>
                    {exams.map(ex => (
                      <tr key={ex.id} style={{ borderBottom: '1px solid rgba(255,255,255,0.03)' }}>
                        <td style={{ padding: '8px', fontWeight: 600 }}>{ex.name}</td>
                        <td style={{ padding: '8px' }}>
                          <span style={{ 
                            fontSize: '0.75rem', 
                            background: ex.subject_id === 1 ? 'var(--color-math-bg)' : (ex.subject_id === 2 ? 'var(--color-viet-bg)' : 'var(--color-eng-bg)'), 
                            color: ex.subject_id === 1 ? 'var(--color-math)' : (ex.subject_id === 2 ? 'var(--color-viet)' : 'var(--color-eng)'),
                            padding: '2px 6px',
                            borderRadius: '4px',
                            fontWeight: 600
                          }}>
                            {subjects.find(s => s.id === ex.subject_id)?.name || 'Môn'}
                          </span>
                        </td>
                        <td style={{ padding: '8px', fontWeight: 'bold', color: ex.score >= 8 ? 'var(--color-eng)' : 'var(--color-accent-amber)' }}>
                          {ex.score} / 10
                        </td>
                        <td style={{ padding: '8px', color: 'var(--color-text-subtle)' }}>{ex.date}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>

          </div>
        )}

      </div>

      {/* Modal viewing sub-topic cards */}
      {viewingSubTopic && (
        <div style={{
          position: 'fixed',
          inset: 0,
          background: 'rgba(0, 0, 0, 0.8)',
          backdropFilter: 'blur(8px)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 100,
          padding: '1.5rem'
        }}>
          <div style={{
            background: 'var(--bg-card)',
            border: '1px solid var(--glass-border)',
            borderRadius: '16px',
            width: '100%',
            maxWidth: '600px',
            maxHeight: '80vh',
            display: 'flex',
            flexDirection: 'column',
            boxShadow: '0 20px 50px rgba(0,0,0,0.5)',
            overflow: 'hidden',
            animation: 'scale-up 0.3s ease'
          }}>
            {/* Modal Header */}
            <div style={{
              padding: '1.25rem 1.5rem',
              borderBottom: '1px solid var(--glass-border)',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center'
            }}>
              <div>
                <div style={{ fontSize: '0.8rem', color: 'var(--color-primary)', fontWeight: 700, textTransform: 'uppercase' }}>Danh sách thẻ Active Recall</div>
                <h3 style={{ margin: '4px 0 0 0', fontSize: '1.15rem' }}>{viewingSubTopic.name}</h3>
              </div>
              <button 
                onClick={() => setViewingSubTopic(null)}
                style={{
                  background: 'rgba(255,255,255,0.05)',
                  border: '1px solid var(--glass-border)',
                  color: '#ffffff',
                  padding: '8px',
                  borderRadius: '50%',
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center'
                }}
              >
                <X size={16} />
              </button>
            </div>

            {/* Modal Body */}
            <div style={{ padding: '1.5rem', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '1rem', flex: 1 }}>
              {viewingSubTopic.cards.length > 0 ? (
                viewingSubTopic.cards.map((card, idx) => (
                  <div 
                    key={card.id || idx} 
                    style={{
                      background: 'rgba(255,255,255,0.02)',
                      border: '1px solid var(--glass-border)',
                      borderRadius: '12px',
                      padding: '1rem',
                      display: 'flex',
                      flexDirection: 'column',
                      gap: '8px'
                    }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <span style={{ fontSize: '0.75rem', color: 'var(--color-text-subtle)', fontWeight: 600 }}>Thẻ #{idx + 1}</span>
                      {card.box_number && (
                        <span style={{ fontSize: '0.75rem', background: 'var(--color-primary-bg)', color: 'var(--color-primary)', border: '1px solid var(--color-primary-border)', padding: '2px 8px', borderRadius: '99px' }}>
                          Hộp {card.box_number}
                        </span>
                      )}
                    </div>
                    <div style={{ fontSize: '0.95rem', fontWeight: 600, color: '#ffffff', lineHeight: 1.4 }}>
                      <strong>Hỏi:</strong> {card.front_content}
                    </div>
                    <div style={{ fontSize: '0.9rem', color: 'var(--color-eng)', lineHeight: 1.4, borderTop: '1px solid rgba(255,255,255,0.05)', paddingTop: '8px', marginTop: '4px' }}>
                      <strong>Đáp:</strong> {card.back_content}
                    </div>
                    {card.hint && (
                      <div style={{ fontSize: '0.8rem', color: 'var(--color-accent-amber)', fontStyle: 'italic' }}>
                        <strong>Gợi ý:</strong> {card.hint}
                      </div>
                    )}
                  </div>
                ))
              ) : (
                <div style={{ textAlign: 'center', color: 'var(--color-text-muted)', padding: '2rem 0' }}>
                  Chưa có thẻ ôn tập nào cho đầu mục này.
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      {/* Modal viewing theory */}
      {viewingTheoryTopic && (
        <div style={{
          position: 'fixed',
          inset: 0,
          background: 'rgba(0, 0, 0, 0.85)',
          backdropFilter: 'blur(10px)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 110,
          padding: '1.5rem'
        }}>
          <div style={{
            background: '#12121e',
            border: '1px solid var(--glass-border)',
            borderRadius: '16px',
            width: '100%',
            maxWidth: '1000px',
            maxHeight: '90vh',
            display: 'flex',
            flexDirection: 'column',
            boxShadow: '0 20px 50px rgba(0,0,0,0.6)',
            overflow: 'hidden',
            animation: 'scale-up 0.3s ease'
          }}>
            {/* Modal Header */}
            <div style={{
              padding: '1.25rem 1.5rem',
              borderBottom: '1px solid var(--glass-border)',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              background: 'rgba(255,255,255,0.02)'
            }}>
              <div>
                <div style={{ fontSize: '0.8rem', color: 'var(--color-primary)', fontWeight: 700, textTransform: 'uppercase' }}>Tóm tắt lý thuyết kiến thức</div>
                <h3 style={{ margin: '4px 0 0 0', fontSize: '1.15rem', color: '#fff' }}>{viewingTheoryTopic.title_vn || viewingTheoryTopic.name}</h3>
              </div>
              <button 
                onClick={() => setViewingTheoryTopic(null)}
                style={{
                  background: 'rgba(255,255,255,0.05)',
                  border: '1px solid var(--glass-border)',
                  color: '#ffffff',
                  padding: '8px',
                  borderRadius: '50%',
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center'
                }}
              >
                <X size={16} />
              </button>
            </div>

            {/* Modal Body */}
            <div 
              className="theory-modal-body custom-scrollbar" 
              style={{ 
                padding: '2rem', 
                overflowY: 'auto', 
                flex: 1, 
                color: '#e5e7eb',
                lineHeight: '1.6',
                fontSize: '1rem'
              }}
            >
              <div 
                className="scraped-theory-html"
                dangerouslySetInnerHTML={{ __html: viewingTheoryTopic.theory }} 
                style={{
                  width: '100%'
                }}
              />
            </div>
            
            {/* Modal Footer */}
            <div style={{
              padding: '1rem 1.5rem',
              borderTop: '1px solid var(--glass-border)',
              display: 'flex',
              justifyContent: 'flex-end',
              gap: '12px',
              background: 'rgba(255,255,255,0.02)'
            }}>
              <button
                onClick={() => setViewingTheoryTopic(null)}
                className="btn-secondary"
                style={{
                  padding: '8px 16px',
                  borderRadius: '8px',
                  background: 'rgba(255,255,255,0.05)',
                  color: '#fff',
                  border: '1px solid var(--glass-border)',
                  cursor: 'pointer'
                }}
              >
                Đóng lại
              </button>
              <button
                onClick={() => {
                  const topic = viewingTheoryTopic;
                  setViewingTheoryTopic(null);
                  startTopicPractice(topic);
                }}
                className="btn-primary"
                style={{
                  padding: '8px 20px',
                  borderRadius: '8px',
                  background: 'linear-gradient(135deg, var(--color-girl) 0%, var(--color-primary) 100%)',
                  color: '#fff',
                  border: 'none',
                  fontWeight: 'bold',
                  cursor: 'pointer'
                }}
              >
                ⚡ Luyện Tập Ngay
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Focus Practice Arena (Fullscreen Overlay) */}
      {activePracticeTopic && (
        <div className="focus-arena-overlay">
          <div className="focus-arena-container">
            {/* If loading */}
            {activePracticeTopic.loading && (
              <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', flex: 1, padding: '3rem', textAlign: 'center', gap: '1.5rem' }}>
                <div style={{ width: '50px', height: '50px', border: '4px solid rgba(255,255,255,0.1)', borderTopColor: 'var(--color-girl)', borderRadius: '50%', animation: 'spin 1s linear infinite' }} />
                <div>
                  {activePracticeTopic.chapter.question_count > 0 ? (
                    <>
                      <h3 style={{ margin: '0 0 8px 0', color: '#ffffff' }}>📥 Đang tải câu hỏi trắc nghiệm...</h3>
                      <p style={{ margin: 0, color: 'var(--color-text-muted)', fontSize: '0.9rem', maxWidth: '400px' }}>
                        Hệ thống đang tải các câu hỏi học tập đã được chuẩn bị sẵn từ TAK12 cho chuyên đề "{activePracticeTopic.chapter.title_vn || activePracticeTopic.chapter.name}".
                      </p>
                    </>
                  ) : (
                    <>
                      <h3 style={{ margin: '0 0 8px 0', color: '#ffffff' }}>🤖 Đang biên soạn câu hỏi học tập...</h3>
                      <p style={{ margin: 0, color: 'var(--color-text-muted)', fontSize: '0.9rem', maxWidth: '400px' }}>
                        Gemini AI đang thiết kế 5 câu hỏi thông minh, bám sát chuyên đề "{activePracticeTopic.chapter.title_vn || activePracticeTopic.chapter.name}" dành riêng cho con.
                      </p>
                    </>
                  )}
                </div>
              </div>
            )}

            {/* If error */}
            {activePracticeTopic.error && (
              <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', flex: 1, padding: '3rem', textAlign: 'center', gap: '1rem' }}>
                <span style={{ fontSize: '3rem' }}>❌</span>
                <div>
                  <h3 style={{ margin: '0 0 8px 0', color: '#ffffff' }}>Không Thể Tải Câu Hỏi</h3>
                  <p style={{ margin: 0, color: 'var(--color-text-muted)', fontSize: '0.9rem', marginBottom: '1.5rem' }}>
                    {activePracticeTopic.error}
                  </p>
                  <button 
                    onClick={handleCompletePractice}
                    className="girl-btn-primary"
                    style={{ padding: '8px 20px', borderRadius: '10px' }}
                  >
                    Quay Lại Danh Sách
                  </button>
                </div>
              </div>
            )}

            {/* If quiz session is active & not loading/error */}
            {!activePracticeTopic.loading && !activePracticeTopic.error && (
              <>
                {/* Header */}
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '1.25rem 1.5rem', borderBottom: '1px solid rgba(255,255,255,0.06)' }}>
                  <div>
                    <span style={{ fontSize: '0.75rem', color: 'var(--color-girl)', fontWeight: 'bold', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                      ⚡ Phòng Luyện Tập Tập Trung
                    </span>
                    <h3 style={{ margin: '4px 0 0 0', fontSize: '1rem', color: '#ffffff', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', maxWidth: '450px' }}>
                      {activePracticeTopic.chapter.title_vn || activePracticeTopic.chapter.name}
                    </h3>
                  </div>

                  <div style={{ display: 'flex', alignItems: 'center', gap: '15px' }}>
                    {activePracticeTopic.score === null && (
                      <div style={{ fontSize: '0.9rem', color: 'var(--color-accent-amber)', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '6px' }}>
                        ⏱️ {(() => {
                          const m = Math.floor(practiceTimer / 60);
                          const s = practiceTimer % 60;
                          return `${m}:${s < 10 ? '0' : ''}${s}`;
                        })()}
                      </div>
                    )}
                    
                    <button 
                      onClick={() => {
                        if (activePracticeTopic.score !== null || confirm('Con có chắc chắn muốn thoát khỏi phiên luyện tập này không? Kết quả hiện tại sẽ không được lưu.')) {
                          handleCompletePractice();
                        }
                      }}
                      style={{ background: 'rgba(255,255,255,0.05)', border: 'none', color: '#fff', width: '32px', height: '32px', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', cursor: 'pointer' }}
                    >
                      <X size={16} />
                    </button>
                  </div>
                </div>

                {/* Score Summary View (Completed) */}
                {activePracticeTopic.score !== null ? (
                  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', flex: 1, padding: '2.5rem', textAlign: 'center', overflowY: 'auto' }}>
                    {/* Confetti particles */}
                    {activePracticeTopic.score >= 80 && (
                      <div style={{ position: 'absolute', top: 0, left: 0, right: 0, bottom: 0, overflow: 'hidden', pointerEvents: 'none' }}>
                        {[...Array(30)].map((_, i) => {
                          const delay = Math.random() * 3;
                          const left = Math.random() * 100;
                          const color = `hsl(${Math.random() * 360}, 100%, 60%)`;
                          return (
                            <div 
                              key={i} 
                              className="confetti-particle" 
                              style={{ 
                                left: `${left}%`, 
                                background: color, 
                                animationDelay: `${delay}s`,
                                width: `${Math.random() * 6 + 6}px`,
                                height: `${Math.random() * 12 + 6}px`
                              }} 
                            />
                          );
                        })}
                      </div>
                    )}

                    <div style={{ fontSize: '4.5rem', marginBottom: '1rem', animation: 'bounce 1s infinite' }}>
                      {activePracticeTopic.score >= 80 ? '🏆' : activePracticeTopic.score >= 50 ? '🥈' : '💪'}
                    </div>

                    <h2 style={{ margin: '0 0 8px 0', fontSize: '1.75rem', color: '#ffffff' }}>
                      {activePracticeTopic.score >= 80 ? 'Hoàn Thành Xuất Sắc!' : activePracticeTopic.score >= 50 ? 'Luyện Tập Thành Công!' : 'Hãy Cố Gắng Hơn Nhé!'}
                    </h2>
                    
                    <p style={{ margin: '0 0 1.5rem 0', color: 'var(--color-text-muted)', fontSize: '0.95rem' }}>
                      Con đã trả lời đúng <strong>{activePracticeTopic.answers.filter(a => a.isCorrect).length} / {activePracticeTopic.questions.length}</strong> câu hỏi.
                    </p>

                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', width: '100%', maxWidth: '400px', marginBottom: '2rem' }}>
                      <div className="premium-card" style={{ padding: '12px', background: 'rgba(255, 120, 50, 0.05)', textAlign: 'center' }}>
                        <div style={{ fontSize: '0.75rem', color: 'var(--color-text-muted)', fontWeight: 600 }}>Điểm Đạt Được</div>
                        <div style={{ fontSize: '1.5rem', fontWeight: 800, color: 'var(--color-viet)', marginTop: '4px' }}>
                          {activePracticeTopic.score}%
                        </div>
                      </div>
                      <div className="premium-card" style={{ padding: '12px', background: 'rgba(16, 185, 129, 0.05)', textAlign: 'center' }}>
                        <div style={{ fontSize: '0.75rem', color: 'var(--color-text-muted)', fontWeight: 600 }}>Thành Tích Thưởng</div>
                        <div style={{ fontSize: '1.5rem', fontWeight: 800, color: '#10b981', marginTop: '4px' }}>
                          +{activePracticeTopic.xp_awarded} XP 🌟
                        </div>
                      </div>
                    </div>

                    <div className="premium-card" style={{ width: '100%', maxWidth: '400px', padding: '15px', background: 'rgba(255,255,255,0.02)', border: '1px solid var(--glass-border)', borderRadius: '12px', marginBottom: '2rem', textAlign: 'left' }}>
                      <h4 style={{ margin: '0 0 8px 0', fontSize: '0.9rem', color: 'var(--color-primary)' }}>📅 Cập nhật Lặp lại ngắt quãng (Leitner)</h4>
                      <p style={{ margin: 0, fontSize: '0.8rem', color: 'var(--color-text-muted)', lineHeight: '1.4' }}>
                        Chuyên đề này được chuyển vào <strong>Hộp {activePracticeTopic.box_number} / 5</strong>.
                        Lịch ôn tập tiếp theo sẽ tự động nhắc nhở con sau <strong>{activePracticeTopic.next_review_in} ngày</strong>.
                      </p>
                    </div>

                    <button
                      onClick={handleCompletePractice}
                      className="girl-btn-primary"
                      style={{ padding: '10px 30px', borderRadius: '12px', fontSize: '0.95rem', fontWeight: 'bold' }}
                    >
                      Xác Nhận & Đóng
                    </button>
                  </div>
                ) : (
                  /* Question View (Practicing) */
                  (() => {
                    const currentIndex = activePracticeTopic.currentIndex;
                    const q = activePracticeTopic.questions[currentIndex];
                    const selected = activePracticeTopic.selectedAnswer;
                    const showAnswer = activePracticeTopic.showAnswer;
                    const totalQuestions = activePracticeTopic.questions.length;
                    
                    const progressPercent = Math.round((currentIndex / totalQuestions) * 100);

                    const cleanOptionText = (text, index) => {
                      if (!text) return '';
                      const label = ['A', 'B', 'C', 'D'][index];
                      const prefixPattern = new RegExp(`^[${label}]\\b[\\s\\.\\,\\:\\-\\)]*`, 'i');
                      return text.replace(prefixPattern, '').trim();
                    };

                    return (
                      <div style={{ display: 'flex', flexDirection: 'column', flex: 1, overflow: 'hidden' }}>
                        {/* Progress Bar */}
                        <div style={{ padding: '0.75rem 1.5rem 0.25rem 1.5rem', background: 'rgba(0,0,0,0.1)' }}>
                          <div style={{ height: '8px', background: 'rgba(255, 255, 255, 0.05)', width: '100%', borderRadius: '4px', overflow: 'hidden' }}>
                            <div style={{ 
                              height: '100%', 
                              width: `${progressPercent}%`, 
                              background: 'linear-gradient(90deg, var(--color-primary) 0%, var(--color-girl) 100%)', 
                              borderRadius: '4px',
                              transition: 'width 0.4s cubic-bezier(0.4, 0, 0.2, 1)' 
                            }} />
                          </div>
                        </div>

                        {/* Split Panels Body */}
                        <div className="focus-practice-body">
                          {/* Left Panel: Question context and metadata */}
                          <div className="practice-left-panel">
                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                <span style={{ fontSize: '0.8rem', color: 'var(--color-text-muted)', fontWeight: 'bold', background: 'rgba(255,255,255,0.04)', padding: '4px 10px', borderRadius: '8px' }}>
                                  Câu hỏi {currentIndex + 1} / {totalQuestions}
                                </span>
                                {q.difficulty === 'easy' && (
                                  <span style={{ fontSize: '0.75rem', background: 'rgba(16, 185, 129, 0.1)', color: '#10b981', padding: '4px 10px', borderRadius: '8px', fontWeight: 'bold' }}>
                                    🟢 Dễ
                                  </span>
                                )}
                                {q.difficulty === 'medium' && (
                                  <span style={{ fontSize: '0.75rem', background: 'rgba(245, 158, 11, 0.1)', color: '#f59e0b', padding: '4px 10px', borderRadius: '8px', fontWeight: 'bold' }}>
                                    🟡 Trung bình
                                  </span>
                                )}
                                {q.difficulty === 'hard' && (
                                  <span style={{ fontSize: '0.75rem', background: 'rgba(239, 68, 68, 0.1)', color: '#ef4444', padding: '4px 10px', borderRadius: '8px', fontWeight: 'bold' }}>
                                    🔴 Khó
                                  </span>
                                )}
                              </div>
                              
                              {q.hint && (
                                <button
                                  onClick={() => alert(`💡 Gợi ý làm bài: ${q.hint}`)}
                                  style={{ background: 'rgba(245, 158, 11, 0.1)', color: '#f59e0b', border: '1px solid rgba(245, 158, 11, 0.2)', padding: '4px 10px', borderRadius: '8px', fontSize: '0.75rem', fontWeight: 'bold', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '4px' }}
                                >
                                  💡 Gợi Ý
                                </button>
                              )}
                            </div>

                            {/* Question text card with whiteSpace: 'pre-wrap' */}
                            <div style={{ 
                              fontSize: '1.15rem', 
                              fontWeight: 600, 
                              color: '#ffffff', 
                              lineHeight: '1.6', 
                              background: 'rgba(255,255,255,0.015)', 
                              padding: '1.5rem', 
                              borderRadius: '16px', 
                              border: '1px solid rgba(255,255,255,0.04)',
                              whiteSpace: 'pre-wrap',
                              boxShadow: 'inset 0 1px 1px rgba(255,255,255,0.05)'
                            }}>
                              {q.question_text}
                            </div>
                          </div>

                          {/* Right Panel: Options & Explanation Drawer */}
                          <div className="practice-right-panel">
                            {/* Options grid */}
                            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                              {q.options.map((opt, idx) => {
                                const optionLabel = ['A', 'B', 'C', 'D'][idx] || '';
                                const cleanedOpt = cleanOptionText(opt, idx);
                                
                                let optClass = 'option-card-btn';
                                if (showAnswer) {
                                  if (opt === q.correct_answer) {
                                    optClass += ' correct';
                                  } else if (opt === selected) {
                                    optClass += ' incorrect';
                                  } else {
                                    optClass += ' neutral-fade';
                                  }
                                }

                                return (
                                  <button
                                    key={idx}
                                    disabled={showAnswer}
                                    onClick={() => handleSelectOption(opt)}
                                    className={optClass}
                                    style={{ display: 'flex', alignItems: 'center', width: '100%' }}
                                  >
                                    <span style={{ 
                                      width: '32px', 
                                      height: '32px', 
                                      borderRadius: '50%', 
                                      background: showAnswer && opt === q.correct_answer ? '#10b981' : (showAnswer && opt === selected ? '#ef4444' : 'rgba(255,255,255,0.06)'),
                                      color: showAnswer && (opt === q.correct_answer || opt === selected) ? '#fff' : 'var(--color-text-muted)',
                                      display: 'flex', 
                                      alignItems: 'center', 
                                      justifyContent: 'center',
                                      fontSize: '0.85rem',
                                      fontWeight: 'bold',
                                      flexShrink: 0
                                    }}>
                                      {optionLabel}
                                    </span>
                                    <span style={{ flex: 1, paddingRight: '8px' }}>{cleanedOpt}</span>
                                    
                                    {/* Visual keyboard shortcut keycap */}
                                    <span className="option-keycap">
                                      {['1', '2', '3', '4'][idx]}
                                    </span>
                                  </button>
                                );
                              })}
                            </div>

                            {/* Instant Feedback and Explanation Box */}
                            {showAnswer && (
                              <div style={{ 
                                background: selected === q.correct_answer ? 'rgba(16, 185, 129, 0.05)' : 'rgba(239, 68, 68, 0.04)',
                                border: selected === q.correct_answer ? '1px solid rgba(16, 185, 129, 0.2)' : '1px solid rgba(239, 68, 68, 0.2)',
                                borderRadius: '16px',
                                padding: '1.25rem',
                                display: 'flex',
                                flexDirection: 'column',
                                gap: '1rem',
                                animation: 'slide-in 0.3s ease'
                              }}>
                                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                  <span style={{ fontSize: '1.1rem', fontWeight: 'bold', color: selected === q.correct_answer ? '#34d399' : '#f87171' }}>
                                    {selected === q.correct_answer ? '🎉 Chính xác! Con giỏi quá!' : '💡 Chưa chính xác rồi con.'}
                                  </span>
                                </div>
                                
                                <p style={{ margin: 0, fontSize: '0.9rem', color: 'var(--color-text-muted)', lineHeight: '1.6' }}>
                                  <strong style={{ color: '#ffffff' }}>Giải thích:</strong> {q.explanation}
                                </p>

                                <div style={{ display: 'flex', justifyContent: 'space-between', gap: '12px', marginTop: '4px' }}>
                                  <button
                                    onClick={() => handleSaveQuestionAsFlashcard(q)}
                                    style={{
                                      background: 'rgba(255, 255, 255, 0.05)',
                                      border: '1px solid rgba(255, 255, 255, 0.1)',
                                      color: '#e5e7eb',
                                      padding: '10px 16px',
                                      borderRadius: '12px',
                                      fontSize: '0.8rem',
                                      fontWeight: 'bold',
                                      cursor: 'pointer',
                                      display: 'flex',
                                      alignItems: 'center',
                                      gap: '6px',
                                      transition: 'all 0.2s'
                                    }}
                                  >
                                    💾 Lưu Flashcard
                                  </button>

                                  <button
                                    onClick={handleNextQuestion}
                                    className="girl-btn-primary"
                                    style={{
                                      padding: '10px 24px',
                                      borderRadius: '12px',
                                      fontSize: '0.8rem',
                                      fontWeight: 'bold',
                                      cursor: 'pointer',
                                      background: selected === q.correct_answer 
                                        ? 'linear-gradient(135deg, #10b981 0%, #059669 100%)'
                                        : 'linear-gradient(135deg, var(--color-primary) 0%, var(--color-girl) 100%)',
                                      border: 'none',
                                      color: '#ffffff',
                                      boxShadow: '0 4px 12px rgba(0,0,0,0.2)'
                                    }}
                                  >
                                    {currentIndex + 1 === totalQuestions ? 'Xem kết quả 🏁' : 'Câu tiếp theo ➡️'}
                                  </button>
                                </div>
                              </div>
                            )}
                          </div>
                        </div>

                        {/* Footer keys reminder */}
                        {activePracticeTopic.score === null && (
                          <div style={{ padding: '0.85rem 1.5rem', background: 'rgba(0,0,0,0.3)', borderTop: '1px solid rgba(255,255,255,0.05)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '0.75rem', color: 'var(--color-text-subtle)' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                              <span>⌨️ Nhấn</span>
                              <kbd style={{ background: 'rgba(255,255,255,0.1)', border: '1px solid rgba(255,255,255,0.2)', padding: '1px 5px', borderRadius: '3px', fontFamily: 'monospace' }}>1</kbd>
                              <kbd style={{ background: 'rgba(255,255,255,0.1)', border: '1px solid rgba(255,255,255,0.2)', padding: '1px 5px', borderRadius: '3px', fontFamily: 'monospace' }}>2</kbd>
                              <kbd style={{ background: 'rgba(255,255,255,0.1)', border: '1px solid rgba(255,255,255,0.2)', padding: '1px 5px', borderRadius: '3px', fontFamily: 'monospace' }}>3</kbd>
                              <kbd style={{ background: 'rgba(255,255,255,0.1)', border: '1px solid rgba(255,255,255,0.2)', padding: '1px 5px', borderRadius: '3px', fontFamily: 'monospace' }}>4</kbd>
                              <span>hoặc</span>
                              <kbd style={{ background: 'rgba(255,255,255,0.1)', border: '1px solid rgba(255,255,255,0.2)', padding: '1px 5px', borderRadius: '3px', fontFamily: 'monospace' }}>A</kbd>
                              <kbd style={{ background: 'rgba(255,255,255,0.1)', border: '1px solid rgba(255,255,255,0.2)', padding: '1px 5px', borderRadius: '3px', fontFamily: 'monospace' }}>B</kbd>
                              <kbd style={{ background: 'rgba(255,255,255,0.1)', border: '1px solid rgba(255,255,255,0.2)', padding: '1px 5px', borderRadius: '3px', fontFamily: 'monospace' }}>C</kbd>
                              <kbd style={{ background: 'rgba(255,255,255,0.1)', border: '1px solid rgba(255,255,255,0.2)', padding: '1px 5px', borderRadius: '3px', fontFamily: 'monospace' }}>D</kbd>
                              <span>để chọn</span>
                            </div>
                            {showAnswer && (
                              <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                                <span>Nhấn</span>
                                <kbd style={{ background: 'rgba(255,255,255,0.1)', border: '1px solid rgba(255,255,255,0.2)', padding: '1px 5px', borderRadius: '3px', fontFamily: 'monospace' }}>Space</kbd>
                                <span>hoặc</span>
                                <kbd style={{ background: 'rgba(255,255,255,0.1)', border: '1px solid rgba(255,255,255,0.2)', padding: '1px 5px', borderRadius: '3px', fontFamily: 'monospace' }}>Enter</kbd>
                                <span>để tiếp tục</span>
                              </div>
                            )}
                          </div>
                        )}
                      </div>
                    );
                  })()
                )}
              </>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
