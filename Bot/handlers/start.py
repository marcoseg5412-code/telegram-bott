from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from database import add_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    add_user(user.id, user.username)

    keyboard = [
        [InlineKeyboardButton("📚 Menu", callback_data="menu")],
        [InlineKeyboardButton("🤖 AI Chat", callback_data="ai")],
    ]

    await update.message.reply_text(
        f"Ciao {user.first_name}! 👋\nBenvenuto nel bot avanzato.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
