import os
import json
from datetime import datetime, timezone
from flask import Flask, Response

app = Flask(__name__)

VERSION = "1.0.0"
ENV = os.environ.get("FLASK_ENV", "development")
PORT = int(os.environ.get("PORT", 3000))


@app.route("/")
def index():
    now = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S UTC")
    html = f"""<!DOCTYPE html>
<html>
  <head>
    <title>My App</title>
    <style>
      body {{ font-family: sans-serif; display: flex; align-items: center;
              justify-content: center; min-height: 100vh; margin: 0;
              background: #f0f4f8; }}
      .card {{ background: #fff; padding: 2rem 3rem; border-radius: 12px;
               box-shadow: 0 4px 24px rgba(0,0,0,.08); text-align: center; }}
      h1   {{ color: #4f46e5; margin: 0 0 1rem; }}
      p    {{ color: #555; margin: .4rem 0; }}
      .tag {{ display: inline-block; background: #e0e7ff; color: #4f46e5;
              border-radius: 6px; padding: 2px 10px; font-size: .85rem; }}
    </style>
  </head>
  <body>
    <div class="card">
      <h1>🚀 Hello from CI/CD!</h1>
      <p>Version: <span class="tag">v{VERSION}</span></p>
      <p>Environment: <span class="tag">{ENV}</span></p>
      <p>Server time: {now}</p>
    </div>
  </body>
</html>"""
    return Response(html, mimetype="text/html")


@app.route("/health")
def health():
    return Response(
        json.dumps({"status": "ok"}),
        mimetype="application/json"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
