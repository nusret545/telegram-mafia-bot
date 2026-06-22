from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

app = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salam! Bot işləyir ✅")

app.add_handler(CommandHandler("start", start))

def main():
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
