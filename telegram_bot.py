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
        "Нажми кнопку, чтобы посмотреть изменения цен telegram gifts:",
        reply_markup=keyboard
    )

async def _remove_webhook(app: Application) -> None:
    """Ensure polling can be used by removing an active webhook."""

    await app.bot.delete_webhook(drop_pending_updates=True)


if __name__ == "__main__":
    app = Application.builder().token(API_TOKEN).post_init(_remove_webhook).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()
