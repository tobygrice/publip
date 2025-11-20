# app.py
import os
import requests
from flask import Flask, Response

app = Flask(__name__)

def get_public_ip():
    try:
        resp = requests.get(
            "https://api.ipify.org",
            params={"format": "text"},
            timeout=5
        )
        resp.raise_for_status()
        return resp.text.strip()
    except Exception as e:
        return f"Error: {e}"

@app.route("/")
def index():
    ip = get_public_ip()

    # Read env vars with sensible defaults
    background = os.getenv("BACKGROUND_COLOR", "#111827")  # slate-900-ish
    text_color = os.getenv("TEXT_COLOR", "#e5e7eb")        # gray-200-ish
    font_size = os.getenv("FONT_SIZE", "2rem")

    html = f"""
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Public IP</title>
        <style>
          :root {{
            color-scheme: dark light;
          }}
          * {{
            box-sizing: border-box;
          }}
          body {{
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: {background};
            color: {text_color};
            font-family: system-ui, -apple-system, BlinkMacSystemFont,
                         "Segoe UI", sans-serif;
          }}
          .wrapper {{
            text-align: center;
          }}
          .label {{
            font-size: 0.9rem;
            opacity: 0.7;
            margin-bottom: 0.2rem;
          }}
          .ip {{
            font-weight: 600;
            font-size: {font_size};
            word-break: break-all;
          }}
        </style>
      </head>
      <body>
        <div class="wrapper">
          <div class="label">Public IP</div>
          <div class="ip">{ip}</div>
        </div>
      </body>
    </html>
    """

    return Response(html, mimetype="text/html")

if __name__ == "__main__":
    # For local dev; in Docker we’ll still use this entrypoint.
    app.run(host="0.0.0.0", port=5001)