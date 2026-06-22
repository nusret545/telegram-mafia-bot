from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

players = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 Mafia botuna xoş gəldin!\n\n"
        "/join - oyuna qoşul\n"
        "/players - oyunçuları göstər"
    )

async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name

    if user not in players:
        players.append(user)
        await update.message.reply_text(f"✅ {user} oyuna qoşuldu.")
    else:
        await update.message.reply_text("⚠️ Sən artıq oyundasan.")

async def show_players(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not players:
        await update.message.reply_text("👥 Hələ oyunçu yoxdur.")
        return

    text = "👥 Oyunçular:\n\n"

    for p in players:
        text += f"• {p}\n"

    await update.message.reply_text(text)

def main():
    token = os.getenv("BOT_TOKEN")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("join", join))
    app.add_handler(CommandHandler("players", show_players))

    app.run_polling()

if __name__ == "__main__":
    main()
