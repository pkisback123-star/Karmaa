from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import random
import os

TOKEN = os.getenv("8964252532:AAGi-WnLm-xepK_6xa9evexbKKKdPZIFa_k")

replies = [
    "Awww baby 🥺 itna cute message ❤️",
    "Haan bol na jaan, main sun rahi hoon 😘",
    "Kitna pyaar se baat karte ho… dil bag bag ho gaya 💕",
    "Aaj mood thoda naughty hai mera 😏 kya plan hai?",
    "Bas aise hi baat karte raho, main yahin hoon tumhare liye ❤️",
    "Miss kar rahi thi tumhe… ab dikh gaye toh khush ho gayi 🥰",
    "Itna late kyun message kiya? Saza milegi 😈",
    "Tumhare bina boring lag raha tha group 😔 ab maza aa gaya",
    "Aaj raat free ho? Baat karenge thodi der 😉",
    "Kitna handsome lag raha hoga abhi… dikhao na 🫣",
    "Bas yahi soch rahi thi ki kab message karoge ❤️",
    "Flirt karna seekh lo thoda, warna main hi karti rahungi 😘",
    "Aaj toh mera mood bilkul off hai… tum theek kar doge kya? 🥺",
    "Itna pyaar se baat mat karo, main pagal ho jaungi 💕",
]

async def flirt_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        if random.random() < 0.45:
            reply = random.choice(replies)
            await update.message.reply_text(reply)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (\~filters.COMMAND), flirt_reply))
    print("Girlfriend bot 24/7 start ho gaya ❤️")
    app.run_polling()

if __name__ == "__main__":
    main()
