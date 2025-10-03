from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Send /download <TeraBox link> to download.")

async def download_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    link = context.args[0] if context.args else None
    if not link:
        await update.message.reply_text("Please provide a TeraBox link!")
        return
    await update.message.reply_text(f"Downloading from: {link} (Demo)")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("download", download_cmd))
    app.run_polling()
