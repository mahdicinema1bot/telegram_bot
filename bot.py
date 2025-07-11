from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio

BOT_TOKEN = "7289610239:AAEN-hMd_vD_q_ES6soa1HlcX0186bJo-CA"
CHANNEL_ID = "@cinema_zone_channel"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    try:
        member = await context.bot.get_chat_member(CHANNEL_ID, user_id)
        if member.status in ["member", "administrator", "creator"]:
            await update.message.reply_text("✅ شما عضو کانال هستید.\n🎬 لینک فیلم:\nhttps://example.com/movie")
        else:
            await send_join_message(update)
    except:
        await send_join_message(update)

async def send_join_message(update: Update):
    keyboard = [[InlineKeyboardButton("📢 عضویت در کانال", url="https://t.me/cinema_zone_channel")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("❌ لطفاً ابتدا در کانال عضو شوید:", reply_markup=reply_markup)

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
