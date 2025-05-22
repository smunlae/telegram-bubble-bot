from telegram import Update, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler
import os

API_TOKEN = os.environ['TELEGRAM_TOKEN']       # читаем из env
WEBAPP_URL = os.environ['WEBAPP_URL']         # читаем из env

async def start(update: Update, context):
    keyboard = [[{
        "text": "Показать график 💠",
        "web_app": WebAppInfo(url=WEBAPP_URL)
    }]]
    await update.message.reply_text(
        "Нажми кнопку, чтобы посмотреть пузырьковый график:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

if __name__ == "__main__":
    app = Application.builder().token(API_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()
