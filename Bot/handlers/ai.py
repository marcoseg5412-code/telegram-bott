import os
from telegram import Update
from telegram.ext import ContextTypes
import requests

async def ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.edit_message_text("Scrivi un messaggio e ti risponderò con l'AI!")

async def ai_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    api_key = os.getenv("GROQ_API_KEY")

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": "llama3-8b-8192",
            "messages": [{"role": "user", "content": text}]
        }
    ).json()

    reply = response["choices"][0]["message"]["content"]
    await update.message.reply_text(reply)
