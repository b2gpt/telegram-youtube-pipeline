from telethon.sync import TelegramClient
from dotenv import load_dotenv
import os

# ✅ Force load .env from current folder
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# 🔍 Debug print
print("DEBUG: API_ID =", os.getenv("TELEGRAM_API_ID"))

# ✅ Now safely parse
api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")

client = TelegramClient("session", api_id, api_hash)
client.start()  # ✅ OTP maangega

print("✅ Session file created: session.session")
