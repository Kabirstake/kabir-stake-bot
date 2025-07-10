import os
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = os.getenv("BOT_TOKEN")

def extract_code(update, context):
    text = update.message.text.lower()
    if "code:" in text:
        start = text.find("code:") + len("code:")
        code = text[start:].strip().split()[0]
        reply = f"✅ Code found: {code}"
        update.message.reply_text(reply)

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, extract_code))
updater.start_polling()
updater.idle()
