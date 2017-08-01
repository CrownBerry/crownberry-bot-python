from Services.CoinRate import CoinRate
from Services.MyOwnCNN import MyOwnCNN
import config


class MainHandlers:
    @staticmethod
    def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id,
                         text="I'm bot, and I'm not ready yet =_=")

    @staticmethod
    def btc(bot, update):
        btc_price = CoinRate.get_rate("btc")
        bcc_prrice = CoinRate.get_rate("bcc")
        eth_price = CoinRate.get_rate("eth")
        bot.send_message(chat_id=update.message.chat_id,
                         text="1 BTC = " + btc_price + "$\n" +
                         "1 BCC = " + bcc_prrice + "$\n" +
                         "1 ETH = " + eth_price + "$")

    @staticmethod
    def cat_or_dog(bot, update):
        pic_id = update.message.photo[-1].file_id
        new_file = bot.get_file(pic_id)
        str_pic = 'pic.jpg'
        new_file.download(str_pic)
        animal_name = MyOwnCNN.who_is_it(str_pic)
        bot.send_message(chat_id=update.message.chat_id,
                         text=animal_name)