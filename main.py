import logging

from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

import config
import Handlers.handler

if __name__ == '__main__':
    updater = Updater(token=config.tg_token)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    start_handler = CommandHandler('start', Handlers.handler.start)
    btc_handler = CommandHandler('btc', Handlers.handler.btc)
    cod_handler = MessageHandler(Filters.photo, Handlers.handler.cat_or_dog)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(btc_handler)
    dispatcher.add_handler(cod_handler)

    updater.start_polling()
