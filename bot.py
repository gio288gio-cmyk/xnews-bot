import os
import requests

TELEGRAM_TOKEN = "9212972793:AAFZQdJFuPl7KJzUL4zNaQ2UCla_CdqPDnU"
WP_URL = "https://xnews.ge/wp-json/wp/v2/posts"
WP_MEDIA_URL = "https://xnews.ge/wp-json/wp/v2/media"
WP_USER = "giorgi.jgarkava"
WP_PASS = "6zmJ CW4G XnFe pEFe 9144 Ydyk"

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "XNews Bot is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
