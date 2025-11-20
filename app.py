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
    background = os.getenv("BACKGROUND_COLOR", "#2E2E2E")
    text_color = os.getenv("TEXT_COLOR", "#C8C8C8")

    # Treat FONT_SIZE as a max size; allow px/rem/em/vw etc.
    max_font_size = os.getenv("MAX_FONT_SIZE", "3.0rem")

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
            height: 100vh;
            width: 100vw;
            background: {background};
            color: {text_color};
            font-family: system-ui, -apple-system, BlinkMacSystemFont,
                        "Segoe UI", sans-serif;
          }}

          .frame {{
            height: 100%;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: clamp(16px, 4vw, 48px);
            text-align: center;
          }}

          .label {{
            font-size: clamp(0.7rem, 0.2vw, 0.95rem);
            opacity: 0.7;
            font-weight: 500;
            margin-bottom: clamp(6px, 0.2rem, 12px);
          }}

          .ip {{
            width: 100%;
            font-weight: 700;
            line-height: 1.05;
            font-size: clamp(1.5rem, 12vw, {max_font_size});
            word-break: break-word;
            overflow-wrap: anywhere;
          }}
        </style>
      </head>
      <body>
        <div class="frame">
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