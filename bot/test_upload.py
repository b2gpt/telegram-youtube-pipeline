from upload_to_youtube import upload_to_youtube

video_id = upload_to_youtube("video/video.mp4", "Test Video", "Uploaded via bot")
print("✅ Uploaded:", f"https://youtu.be/{video_id}")
