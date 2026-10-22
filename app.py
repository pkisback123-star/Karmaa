from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "All-Rounder Telegram Bot is Running 24/7!"

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    t = threading.Thread(target=run_flask)
    t.start()
    os.system("python bot.py")
