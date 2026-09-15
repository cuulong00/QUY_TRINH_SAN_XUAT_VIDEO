import yt_dlp
import sys

def main(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    ydl_opts = {
        'getcomments': True,
        'skip_download': True,
        'extract_flat': True,
    }

    print(f"⏳ Đang trích xuất bình luận từ video {video_id} bằng yt-dlp...")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            comments = info.get('comments', [])
            print(f"✅ Tìm thấy {len(comments)} bình luận.")
            
            # Print top 30 comments
            for c in comments[:35]:
                author = c.get('author', 'Anonymous')
                text = c.get('text', '').replace('\n', ' ')
                likes = c.get('like_count', 0)
                print(f"LIKES={likes} | AUTHOR={author} | TEXT={text}")
    except Exception as e:
        print("Error extracting comments:", e)

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '6ga9gg8Ei2A')
