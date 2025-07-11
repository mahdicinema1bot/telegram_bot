import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
import telegram.error

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@cinema_zone_channel"

def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    try:
        member = context.bot.get_chat_member(CHANNEL_ID, user_id)
        if member.status in ["member", "administrator", "creator"]:
            update.message.reply_text("✅ شما عضو کانال هستید. لینک دانلود:\nhttps://example.com/your-movie-link")
        else:
            send_join_message(update)
    except telegram.error.BadRequest:
        send_join_message(update)

def send_join_message(update: Update):
    keyboard = [[InlineKeyboardButton("📢 عضویت در کانال", url="https://t.me/cinema_zone_channel")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("❌ ابتدا باید در کانال عضو شوید.", reply_markup=reply_markup)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
