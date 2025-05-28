import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.error import BadRequest

API_TOKEN = os.environ['TELEGRAM_TOKEN']     # ваш токен
WEBAPP_URL = os.environ['WEBAPP_URL']       # URL вашего Bubble-chart
CHANNEL_USERNAME = "@giftsBubbles"           # юзернейм канала

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    try:
        # проверяем статус пользователя в канале
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)
        is_subscribed = member.status in ("member", "administrator", "creator")
    except BadRequest:
        # например, бот не является администратором или канал приватный
        is_subscribed = False

    if not is_subscribed:
        # если не подписан — просим подписаться
        await update.message.reply_text(
            f"Чтобы пользоваться ботом, подпишись на канал {CHANNEL_USERNAME}"
        )
        return

    # пользователь подписан — показываем кнопку WebApp
    button = InlineKeyboardButton(
        text="Gift Bubbles 💠",
        web_app=WebAppInfo(url=WEBAPP_URL)
    )
    keyboard = InlineKeyboardMarkup([[button]])
    
    await update.message.reply_text(
        "Нажми кнопку, чтобы посмотреть изменения цен telegram gifts:",
        reply_markup=keyboard
    )

if __name__ == "__main__":
    app = Application.builder().token(API_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()
