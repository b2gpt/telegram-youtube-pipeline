import os
from telethon.sync import TelegramClient

def fetch_video():
    api_id_raw = os.getenv("TELEGRAM_API_ID")
    api_hash = os.getenv("TELEGRAM_API_HASH")
    bot_token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")  # ✅ added

    if not api_id_raw or not api_hash or not bot_token or not chat_id:
        raise ValueError("Missing TELEGRAM_API_ID, TELEGRAM_API_HASH, BOT_TOKEN, or CHAT_ID in environment variables")

    api_id = int(api_id_raw)

    with TelegramClient("session", api_id, api_hash) as client:
        client.start(bot_token=bot_token)

        messages = client.get_messages(chat_id, limit=1)
        for msg in messages:
            if msg.video or msg.document:
                file_path = client.download_media(msg)
                return file_path

    return None
