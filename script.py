import yt_dlp
from concurrent.futures import ThreadPoolExecutor
import pyfiglet

def download_video(url, output_format):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': output_format,
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main(urls, output_format):
    with ThreadPoolExecutor(max_workers=5) as executor:
        tasks = [(url, output_format) for url in urls]
        executor.map(lambda x: download_video(*x), tasks)

if __name__ == "__main__":
    header = pyfiglet.figlet_format("yt2clip")
    print(header)

    while True:
        try:
            urls_input = input("Enter YouTube URLs separated by a comma (or 'exit' to quit): ")
            if urls_input.lower() == 'exit':
                break

            youtube_urls = [url.strip() for url in urls_input.split(',')]

            print("Choose an output format (e.g., mp4, mp3, avi, flv):")
            output_format = input("Enter the format: ").lower()

            main(youtube_urls, output_format)

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

