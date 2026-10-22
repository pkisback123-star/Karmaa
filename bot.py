import os
import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import yt_dlp

TOKEN = os.getenv("8972022752:AAEwFjxYp_0TYRuWtOctA5Ix7OQIzWcgjVQ")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "👋 Hello! Main aapka All-Rounder Bot hoon.\n\n"
        "🔥 **Features:**\n"
        "1. Instagram Video/Reel download karne ke liye link bhejein.\n"
        "2. Voice chat me song search karne ke liye `/play [song name]` use karein."
    )
    await update.message.reply_text(welcome_text)

# --- Feature 1: Instagram Video Downloader ---
async def download_instagram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    if "instagram.com" not in url:
        return

    msg = await update.message.reply_text("📥 Instagram video download ho rahi hai, kripya intezaar karein...")

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'insta_video.mp4',
        'quiet': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        if os.path.exists('insta_video.mp4'):
            await update.message.reply_video(video=open('insta_video.mp4', 'rb'), caption="✨ Here is your Instagram video!")
            os.remove('insta_video.mp4')
            await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=msg.message_id)
        else:
            await update.message.reply_text("❌ Video download nahi ho payi. Link check karein.")
    except Exception as e:
        logger.error(f"Error downloading IG video: {e}")
        await update.message.reply_text("❌ Kuch error aa gaya video download karne me.")

# --- Feature 2: VC Song Search/Player ---
async def play_song(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args)
    if not query:
        await update.message.reply_text("⚠️ Kripya song ka naam likhein. Example: `/play Aashiqui 2 song`")
        return

    await update.message.reply_text(f"🎵 **{query}** ko search kiya ja raha hai...")
    
    ydl_opts = {
        'format': 'bestaudio',
        'default_search': 'ytsearch1',
        'quiet': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            if 'entries' in info:
                info = info['entries'][0]
            title = info.get('title', 'Unknown')
            
            await update.message.reply_text(f"✅ Song found: **{title}**\n🔗 Ready for Voice Chat!")
    except Exception as e:
        logger.error(f"Error finding song: {e}")
        await update.message.reply_text("❌ Song search karne me error aaya.")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("play", play_song))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), download_instagram))
    
    print("All-Rounder Bot is starting...")
    application.run_polling()
