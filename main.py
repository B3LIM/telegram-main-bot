from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ.get("TOKEN")  # Bot token from environment variable

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("📥 Get Book (₹10)", callback_data='get_book')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo="https://i.imgur.com/9UtTnWc.jpg",  # Atomic Habits cover
        caption=(
            "📚 *Atomic Habits*\n"
            "💰 *Price:* ₹10\n\n"
            "✅ An Easy & Proven Way to Build Good Habits & Break Bad Ones\n"
            "[💳 Pay Now](https://razorpay.me/@mrmukhi)"
        ),
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'get_book':
        await query.message.reply_document(
            document=open("Atomic_Habits_by_James_Clear-1.pdf", "rb"),
            filename="Atomic_Habits_by_James_Clear.pdf",
            caption="📘 Here's your book. Thanks for supporting!"
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("get", button))
app.run_polling()
