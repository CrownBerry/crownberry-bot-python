from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging

updater = Updater(token="420905549:AAHb1OstzqlLiwGQegNGP27UO1uoS4Jpw5g")
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm bot, and I'm not ready yet, but I deployed with docker-compose")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

if __name__ == '__main__':
    updater.start_polling()
