# YT-TG
This is a Python script that downloads YouTube videos and sends them to a Telegram.

# Requirements
* Python 3.7 or higher
* [pyrogram](https://github.com/pyrogram/pyrogram)
* [yt-dlp](https://github.com/yt-dlp/yt-dlp)
* [pydantic](https://github.com/pydantic/pydantic)
* [asyncio](https://docs.python.org/3/library/asyncio.html)
* [tgcrypto](https://github.com/pyrogram/tgcrypto)

You can install the required modules by running the following command:

```bash
pip install pyrogram yt-dlp pydantic asyncio tgcrypto
```
# Usage
Before running the script, you need to fill in the 

* api_id and api_hash (can be obtained by following this link https://my.telegram.org)
* chat_id 
* channel_url 

To run the script, simply execute the following command:

```bash
python yt-tg.py
```
