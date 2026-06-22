from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

app = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salam! Bot işləyir ✅")

app.add_handler(CommandHandler("start", start))

# ❌ main() silirik
# ❌ run_polling istifadə etmirik

async def run_bot():
    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    # bot işləsin
    await app.updater.idle()

import asyncio
asyncio.run(run_bot())
