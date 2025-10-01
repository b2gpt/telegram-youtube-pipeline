import os

def update_embed(video_id):
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latest Video</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      text-align: center;
      padding: 50px;
      background-color: #f9f9f9;
    }}
    iframe {{
      border: none;
      width: 80%;
      max-width: 720px;
      height: 405px;
    }}
    h1 {{
      color: #333;
    }}
  </style>
</head>
<body>
  <h1>🎬 Latest Auto-Uploaded Video</h1>
  <iframe src="https://www.youtube.com/embed/{video_id}" allowfullscreen></iframe>
</body>
</html>"""

    os.makedirs("site", exist_ok=True)
    with open("site/index.html", "w", encoding="utf-8") as f:
        f.write(html_template)

    print("🌐 site/index.html updated with embedded video.")
