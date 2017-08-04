from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import logging
from Handlers.handler import MainHandlers
from Services.MyOwnCNN import MyOwnCNN
import config


if __name__ == '__main__':
    config.init()
    MyOwnCNN.init_model()

    updater = Updater(token=config.tg_token)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    start_handler = CommandHandler('start', MainHandlers.start)
    btc_handler = CommandHandler('btc', MainHandlers.btc)
    top_word_handler = CommandHandler('topword', MainHandlers.get_top_word)
    cod_handler = MessageHandler(Filters.photo, MainHandlers.cat_or_dog)
    memory_handler = MessageHandler(Filters.text, MainHandlers.save_in_memory)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(btc_handler)
    dispatcher.add_handler(cod_handler)
    dispatcher.add_handler(memory_handler)
    dispatcher.add_handler(top_word_handler)


    updater.start_polling()
