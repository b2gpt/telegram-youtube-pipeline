import os
from telethon.sync import TelegramClient

def fetch_video():
    api_id_raw = os.getenv("TELEGRAM_API_ID")
    api_hash = os.getenv("TELEGRAM_API_HASH")
    bot_token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    # Debug logs
    print("DEBUG: TELEGRAM_API_ID =", api_id_raw)
    print("DEBUG: TELEGRAM_API_HASH =", api_hash)
    print("DEBUG: BOT_TOKEN =", bot_token)
    print("DEBUG: CHAT_ID =", chat_id)

    if not api_id_raw or not api_hash or not bot_token or not chat_id:
        raise ValueError("Missing TELEGRAM_API_ID, TELEGRAM_API_HASH, BOT_TOKEN, or CHAT_ID in environment variables")

    api_id = int(api_id_raw)

    with TelegramClient("session", api_id, api_hash) as client:
        client.start(bot_token=bot_token)

        print("DEBUG: Logged in as =", client.get_me())

        messages = client.get_messages(chat_id, limit=1)
        print("DEBUG: Messages fetched =", messages)

        for msg in messages:
            if msg.video or msg.document:
                file_path = client.download_media(msg)
                print("DEBUG: Downloaded file path =", file_path)
                return file_path

    print("DEBUG: No video or document found")
    return None
