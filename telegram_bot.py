import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler

API_TOKEN = os.environ['TELEGRAM_TOKEN']     # ваш токен
WEBAPP_URL = os.environ['WEBAPP_URL']       # URL вашего Bubble-chart

async def start(update: Update, context):
    # Создаём кнопку, которая откроет Web App
    button = InlineKeyboardButton(
        text="Gift Bubbles 💠",
        web_app=WebAppInfo(url=WEBAPP_URL)
    )
    keyboard = InlineKeyboardMarkup([[button]])
    
    # Отправляем сообщение с inline-клавиатурой
    await update.message.reply_text(
        "Обновления бота - @giftsBubbles (Подпишись)
        
        Нажми кнопку, чтобы посмотреть изменения цен telegram gifts:",
        reply_markup=keyboard
    )

if __name__ == "__main__":
    app = Application.builder().token(API_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()
