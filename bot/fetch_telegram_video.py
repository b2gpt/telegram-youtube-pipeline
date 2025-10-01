import os
from telethon.sync import TelegramClient

def fetch_video():
    api_id_raw = os.getenv("TELEGRAM_API_ID")
    api_hash = os.getenv("TELEGRAM_API_HASH")
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not api_id_raw or not api_hash or not bot_token:
        raise ValueError("Missing TELEGRAM_API_ID, API_HASH, or BOT_TOKEN in Railway Variables")

    api_id = int(api_id_raw)

    with TelegramClient("session", api_id, api_hash) as client:
        client.start(bot_token=bot_token)

        # Example: fetch latest video message
        messages = client.get_messages("your_channel_username", limit=1)
        for msg in messages:
            if msg.video or msg.document:
                file_path = client.download_media(msg)
                return file_path

    return None
