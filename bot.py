from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import yt_dlp

TOKEN = "8933832246:AAFCa_hcoFWW6-jmwEr19uUD0k5Hab2nO-I"

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text

    await update.message.reply_text("⏳ جاري التحميل...")

    ydl_opts = {
        "format": "best",
        "outtmpl": "video.%(ext)s",
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        await update.message.reply_video(video=open(filename, "rb"))

    except Exception as e:
        await update.message.reply_text(f"خطأ: {e}")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download))

print("البوت شغال...")
app.run_polling()
