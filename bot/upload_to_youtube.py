from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
import json
import os

def upload_to_youtube(file_path, title, description):
    SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
    
    creds_json = os.getenv("CLIENT_SECRET_JSON")
    creds_dict = json.loads(creds_json)
    creds = Credentials.from_authorized_user_info(creds_dict, SCOPES)

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
