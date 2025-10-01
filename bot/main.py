from fetch_telegram_video import fetch_video
from upload_to_youtube import upload_to_youtube
from update_embed import update_embed

file_path = fetch_video()
if file_path:
    video_id = upload_to_youtube(file_path, "Auto Video", "Uploaded via bot")
    print("✅ Uploaded:", f"https://youtu.be/{video_id}")

    update_embed(video_id)
    print("🌐 Website updated with embedded video.")
else:
    print("❌ No video found to upload.")
