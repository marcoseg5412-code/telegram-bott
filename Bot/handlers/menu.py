from telegram import Update
from telegram.ext import ContextTypes

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        "📚 *Menu principale*\n"
        "- /info → informazioni\n"
        "- /help → aiuto\n",
        parse_mode="Markdown"
    )
