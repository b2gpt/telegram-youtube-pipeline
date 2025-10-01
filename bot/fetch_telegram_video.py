import os
from telethon.sync import TelegramClient
from dotenv import load_dotenv

# 🔐 Load environment variables
load_dotenv()

# ✅ Credentials from .env
api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")
channel_url = os.getenv("TELEGRAM_CHANNEL")  # e.g. "https://t.me/testingnowdone"

# 🧠 Extract username from full URL
channel_username = channel_url.replace("https://t.me/", "").replace("t.me/", "").strip()

# 📁 Output path
output_folder = "video"
output_file = os.path.join(output_folder, "video.mp4")

def fetch_video():
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with TelegramClient("session", api_id, api_hash) as client:
        messages = client.get_messages(channel_username, limit=10)
        for msg in messages:
            if msg.video:
                print("🎥 Found video:", msg.id)
                msg.download_media(file=output_file)
                print("✅ Saved to:", output_file)
                return output_file

    print("❌ No video found.")
    return None
