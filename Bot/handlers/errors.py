import logging
from telegram import Update
from telegram.ext import ContextTypes

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.error(f"Errore: {context.error}")
    if update:
        await update.message.reply_text("⚠️ Si è verificato un errore.")
