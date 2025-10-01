from google_auth_oauthlib.flow import InstalledAppFlow

# Scope for uploading videos to YouTube
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

# Create OAuth flow using your client_secret.json
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)

# Run local server to authenticate via browser
creds = flow.run_local_server(port=0)

# Save the access + refresh token to token.json
with open("token.json", "w") as token:
    token.write(creds.to_json())

print("✅ token.json generated successfully!")
