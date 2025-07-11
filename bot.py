from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# توکن رباتت (مستقیم داخل کد)
BOT_TOKEN = "7289610239:AAEN-hMd_vD_q_ES6soa1HlcX0186bJo-CA"

# آیدی کانال
CHANNEL_ID = "@cinema_zone_channel"

# وقتی کاربر /start رو می‌فرسته
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    member = await context.bot.get_chat_member(CHANNEL_ID, user_id)

    if member.status in ["member", "administrator", "creator"]:
        await update.message.reply_text("✅ شما عضو کانال هستید. لینک دانلود:\nhttps://example.com/your-movie-link")
    else:
        await send_join_message(update)

# اگر عضو نبود
async def send_join_message(update: Update):
    keyboard = [[InlineKeyboardButton("📢 عضویت در کانال", url="https://t.me/cinema_zone_channel")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("❌ لطفاً ابتدا در کانال عضو شوید:", reply_markup=reply_markup)

# اجرای اصلی
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
