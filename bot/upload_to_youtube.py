from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

def upload_to_youtube(file_path, title, description):
    SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
    creds = Credentials.from_authorized_user_file("youtube_auth/token.json", SCOPES)
    youtube = build("youtube", "v3", credentials=creds)

    media = MediaFileUpload(file_path, chunksize=-1, resumable=True)
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description
            },
            "status": {
                "privacyStatus": "unlisted"
            }
        },
        media_body=media
    )
    response = request.execute()
    return response["id"]
