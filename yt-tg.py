import os
import asyncio
import yt_dlp
from pyrogram import Client
from pydantic import BaseModel

api_id="Insert yours api_id here"
api_hash="Insert yours api_hash here"
chat_id="Insert yours chat_id here"
channel_url="Insert yours channel_url here"

class Metadata(BaseModel):
    id: str
    title: str
    description: str


def get_video_links():
    ydl_opts = {
        'ignoreerrors': True,
        'quiet': True,
        'skip_download': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(channel_url, download=False)
        if info and 'entries' in info:
            video_urls = [item['webpage_url'] for item in info['entries']]
            return video_urls
        else:
            return []

def download_video(url):
    ydl_opts = {
        'ignoreerrors': True,
        'quiet': True,
        'outtmpl': '%(title)s.%(ext)s',
        'remux_video': 'mp4',
        'writethumbnail': True,
        'writeinfojson': True,
        'max_filesize': '4G',
        'concurrent_fragment_downloads': 6    
        }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        video_filename = ydl.prepare_filename(info)
        thumbnail_filename = os.path.splitext(video_filename)[0] + ".webp"
        metadata_filename = os.path.splitext(video_filename)[0] + ".info.json"
        return video_filename, thumbnail_filename, metadata_filename

async def send_files_to_channel(video_filename: str, thumbnail_filename: str, metadata_filename: str):
    metadata = Metadata.parse_file(metadata_filename)
    async with Client("Sergo1217", api_id=api_id, api_hash=api_hash) as app:
        print(f"отправляю {video_filename}")
        await app.send_video(chat_id, video=video_filename, caption=metadata.description[:1024], thumb=thumbnail_filename)
        print(f"{video_filename} отправлен")

if __name__ == '__main__':
    video_urls = get_video_links()
    if video_urls:
        video_urls.reverse()
        for video in video_urls:
            print(video)
            video_filename, thumbnail_filename, metadata_filename = download_video(video)
            asyncio.run(send_files_to_channel(video_filename, thumbnail_filename, metadata_filename))

