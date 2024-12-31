from telegram import Update # type: ignore
from telegram.ext import Updater, CommandHandler, CallbackContext # type: ignore
from dotenv import load_dotenv # type: ignore
import os

load_dotenv()

TOKEN = os.getenv('BOT_API_TOKEN')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! The Man Who is Wearing a Leaf Bot Active!')

# /help komutuna cevap verecek fonksiyon
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Size nasıl yardımcı olabilirim?')

# Botu başlatan fonksiyon
def main():
    # Updater'ı başlatın
    updater = Updater(TOKEN)

    # Dispatcher oluşturun ve komutları kaydedin
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help_command))

    # Botu çalıştırmaya başla
    updater.start_polling()

    # Botu kapatmak için durmasını sağla
    updater.idle()

if __name__ == '__main__':
    main()

