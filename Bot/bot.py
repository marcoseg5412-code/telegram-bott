import logging
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    CallbackQueryHandler, filters
)
from config import TOKEN
from database import init_db
from handlers.start import start
from handlers.menu import menu
from handlers.ai import ai, ai_message
from handlers.errors import error_handler

logging.basicConfig(level=logging.INFO)

def main():
    init_db()

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu, pattern="menu"))
    app.add_handler(CallbackQueryHandler(ai, pattern="ai"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ai_message))

    app.add_error_handler(error_handler)

    print("Bot avanzato avviato...")
    app.run_polling()

if __name__ == "__main__":
    main()
