import yt_dlp
from datetime import timedelta

playlist_url = 'https://www.youtube.com/watch?v=IUCEFBmYIog&list=PLlVtbbG169nED0_vMEniWBQjSoxTsBYS3'

def format_seconds(seconds: int) -> str:
    return str(timedelta(seconds=seconds))

def main():
    ydl_opts = {
        'quiet': True,
        'extract_flat': False,
        'skip_download': True,
        'ignoreerrors': True,
    }

    total_seconds = 0
    video_count = 0

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist_url, download=False)
        entries = info.get('entries', [])

        for i, entry in enumerate(entries, 1):
            if entry is None:
                continue
            duration = entry.get('duration', 0)
            total_seconds += duration
            formatted = format_seconds(duration)
            print(f"video {i}: {formatted}")
            video_count += 1

    print("\n--- Summary ---")
    print(f"Total videos processed: {video_count}")
    total_minutes = total_seconds // 60
    total_time = format_seconds(total_seconds)
    print(f"Total duration: {total_time}")
    print(f"Total minutes: {total_minutes}")
    print(f"Total hours: {total_minutes // 60}h {total_minutes % 60}m")

if __name__ == "__main__":
    main()
