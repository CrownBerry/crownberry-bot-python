from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging
from Handlers.handler import MainHandlers

updater = Updater(token="420905549:AAHb1OstzqlLiwGQegNGP27UO1uoS4Jpw5g")
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


start_handler = CommandHandler('start', MainHandlers.start)
btc_handler = CommandHandler('btc', MainHandlers.btc)
cod_handler = CommandHandler('catordog', MainHandlers.cat_or_dog)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(btc_handler)
dispatcher.add_handler(cod_handler)

if __name__ == '__main__':
    updater.start_polling()
