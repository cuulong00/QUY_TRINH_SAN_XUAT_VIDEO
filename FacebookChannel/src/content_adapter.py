"""Content Adapter: Converts YouTube video packages (Dòng Chảy & Góc Nhìn Podcast)
into high-engagement Facebook video post packages following The Meta Strategist directives.
"""

import re
from pathlib import Path
from typing import Dict, Any, List, Optional


class ContentAdapter:
    """Transforms YouTube content assets into Facebook posts."""

    def __init__(self, channel: str = "gocnhin"):
        self.channel = channel.lower().strip()

    def adapt_from_folder(self, episode_dir: str) -> Dict[str, Any]:
        """Tự động tìm kiếm tài liệu trong thư mục tập và tạo gói bài đăng Facebook."""
        dir_path = Path(episode_dir)
        if not dir_path.exists():
            raise FileNotFoundError(f"Thư mục tập không tồn tại: {episode_dir}")

        # Tìm các file tiềm năng: buc_tranh_toan_canh.md, README.md, transcript_vi.md, kịch bản...
        blueprint_files = list(dir_path.glob("buc_tranh_toan_canh.md"))
        readme_files = list(dir_path.glob("README.md")) + list(dir_path.glob("readme.md"))
        transcript_files = list(dir_path.glob("transcript*.md")) + list(dir_path.glob("kich_ban*.md"))

        target_file = None
        if blueprint_files:
            target_file = blueprint_files[0]
        elif readme_files:
            target_file = readme_files[0]
        elif transcript_files:
            target_file = transcript_files[0]

        if not target_file:
            # Lấy bất kỳ file markdown nào đầu tiên
            md_files = list(dir_path.glob("*.md"))
            if md_files:
                target_file = md_files[0]

        content_raw = ""
        if target_file and target_file.exists():
            with open(target_file, "r", encoding="utf-8") as f:
                content_raw = f.read()

        episode_name = dir_path.name
        return self.generate_facebook_package(episode_name=episode_name, raw_text=content_raw)

    def generate_facebook_package(self, episode_name: str, raw_text: str = "") -> Dict[str, Any]:
        """Tạo gói bài viết chuẩn với cấu trúc Hook 3 dòng, Visual Rhythm và MSI question."""
        title_clean = episode_name.replace("-", " ").replace("_", " ").title()

        # Trích xuất các gạch đầu dòng hoặc luận điểm từ tài liệu gốc nếu có
        bullet_points = self._extract_key_bullets(raw_text)

        if "dong_chay" in self.channel:
            tag_primary = "#DongChay"
            category_tags = ["#DiaChinhTri", "#LichSuTheChe", "#KinhTeChinhTri", "#GocNhinDaChieu"]
            perspective_intro = "Lịch sử không vận hành theo các tuyên bố ngoại giao trên bục giảng. Nó vận hành bằng dòng tiền, tài nguyên chiến lược và các bàn cờ thể chế vô hình:"
            msi_question = "Theo góc nhìn của các bạn, trước sự dịch chuyển quyền lực toàn cầu này, cán cân lợi ích giữa các bên sẽ thay đổi theo kịch bản nào? Rất mong nhận được thảo luận đa chiều từ các anh chị."
        else:
            tag_primary = "#GocNhinPodcast"
            category_tags = ["#KinhTeHoc", "#ChinhSachCong", "#XaHoiHoc", "#GocNhinDaChieu"]
            perspective_intro = "Chúng ta thường nhìn các biến chuyển xã hội dưới lăng kính cảm tính. Nhưng dưới góc nhìn kinh tế học hành vi và thể chế, đây là hệ quả tất yếu của cấu trúc động lực:"
            msi_question = "Đứng trước bài toán này, các bạn đánh giá đâu là biến số mang tính quyết định nhất để tạo ra sự chuyển dịch bền vững? Hãy để lại quan điểm phản biện bên dưới."

        # Cấu trúc 3 dòng hook
        hook_line_1 = f"Tại sao điều số đông coi là hiển nhiên lại đang che giấu một nghịch lý kinh tế sâu sắc?"
        hook_line_2 = f"Khi bóc tách các con số thực chứng đằng sau câu chuyện {title_clean}, toàn bộ luật chơi lộ diện hoàn toàn khác."
        hook_line_3 = f"Đâu là cơ chế ngầm đã định hình toàn bộ diễn biến này?"

        # Ghép bài viết hoàn chỉnh
        caption_lines = [
            hook_line_1,
            hook_line_2,
            hook_line_3,
            "",
            "---",
            "",
            perspective_intro,
        ]

        if bullet_points:
            for bp in bullet_points[:4]:
                caption_lines.append(f"• {bp}")
        else:
            caption_lines.append("• Điểm nghẽn mang tính cấu trúc đằng sau hiện tượng.")
            caption_lines.append("• Sự bất cân xứng thông tin và lợi ích giữa các bên liên quan.")
            caption_lines.append("• Bài học định lượng thực tế đối với bức tranh vĩ mô hiện nay.")

        caption_lines.extend([
            "",
            f"💬 {msi_question}",
            "",
            "🎬 Toàn bộ video phân tích chuyên sâu (kèm biểu đồ dữ liệu và tài liệu đối chứng) được ghim tại bình luận đầu tiên.",
            "",
            f"{tag_primary} " + " ".join(category_tags)
        ])

        final_caption = "\n".join(caption_lines)

        return {
            "title": f"Góc Nhìn Chuyên Sâu: {title_clean}",
            "caption": final_caption,
            "hook": [hook_line_1, hook_line_2, hook_line_3],
            "first_comment": f"🎬 Xem video phân tích đầy đủ và chi tiết tại link chính thức: [Kèm link video YouTube gốc ở đây]",
            "hashtags": [tag_primary] + category_tags
        }

    def _extract_key_bullets(self, text: str) -> List[str]:
        """Lọc ra các câu đắt giá hoặc bullet points từ tài liệu gốc."""
        bullets = []
        for line in text.splitlines():
            line_str = line.strip()
            if line_str.startswith("- ") or line_str.startswith("* ") or line_str.startswith("• "):
                clean = re.sub(r"^[-*•]\s*", "", line_str)
                # Loại bỏ các định dạng markdown đậm/nghiêng
                clean = re.sub(r"[*_#]", "", clean).strip()
                if 20 < len(clean) < 150:
                    bullets.append(clean)
        return bullets
