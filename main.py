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
    btc_handler = CommandHandler('btc', Handlers.handler.btc, pass_args=True)
    cod_handler = MessageHandler(Filters.photo, Handlers.handler.cat_or_dog)
    add_word_handler = MessageHandler(Filters.text, Handlers.handler.topword_saving)
    get_topword_handler = CommandHandler('topword', Handlers.handler.get_topword, pass_args=True)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(btc_handler)
    dispatcher.add_handler(cod_handler)
    dispatcher.add_handler(add_word_handler)
    dispatcher.add_handler(get_topword_handler)

    updater.start_polling()
