import os
from telethon.sync import TelegramClient

def fetch_video():
    api_id_raw = os.getenv("TELEGRAM_API_ID")
    api_hash = os.getenv("TELEGRAM_API_HASH")
    bot_token = os.getenv("BOT_TOKEN")  # ✅ fixed

    if not api_id_raw or not api_hash or not bot_token:
        raise ValueError("Missing TELEGRAM_API_ID, TELEGRAM_API_HASH, or BOT_TOKEN in environment variables")

    api_id = int(api_id_raw)

    with TelegramClient("session", api_id, api_hash) as client:
        client.start(bot_token=bot_token)

        messages = client.get_messages("your_channel_username", limit=1)
        for msg in messages:
            if msg.video or msg.document:
                file_path = client.download_media(msg)
                return file_path

    return None
