import operator

from Services.CoinRate import CoinRate
from Services.DTO import DTO
from Services.MyOwnCNN import MyOwnCNN
import config


class MainHandlers:
    @staticmethod
    def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id,
                         text="I'm bot and I can tell you current exchange rate of BTC, BCC, ETH v0.02")

    @staticmethod
    def btc(bot, update):
        btc_price = CoinRate.get_rate("btc")
        bcc_prrice = CoinRate.get_rate("bcc")
        eth_price = CoinRate.get_rate("eth")
        bot.send_message(chat_id=update.message.chat_id,
                         text="1 BTC = $" + btc_price + "\n" +
                              "1 BCC = $" + bcc_prrice + "\n" +
                              "1 ETH = $" + eth_price)

    @staticmethod
    def cat_or_dog(bot, update):
        pic_id = update.message.photo[-1].file_id
        new_file = bot.get_file(pic_id)
        str_pic = 'pic.jpg'
        new_file.download(str_pic)
        animal_name = MyOwnCNN.who_is_it(str_pic)
        bot.send_message(chat_id=update.message.chat_id,
                         text=animal_name)

    @staticmethod
    def save_in_memory(bot, update):
        word_list = update.message.text.split()
        for w in word_list:
            if config.list_of_word[w] is not None:
                config.list_of_word[w] = config.list_of_word[w] + 1
            else:
                config.list_of_word[w] = 1

    @staticmethod
    def get_top_word(bot, update):
        try:
            max(config.list_of_word, key=lambda k: config.list_of_word[k])
        except Exception as e:
            item_name = str(e)
        bot.send_message(chat_id=update.message.chat_id,
                         text="Most common word in our conversation now is: " + item_name)
