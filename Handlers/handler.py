from Services.CoinRate import CoinRate


class MainHandlers:
    @staticmethod
    def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id,
                         text="I'm bot, and I'm not ready yet, but I deployed with docker-compose =_=")

    @staticmethod
    def btc(bot, update):
        current_price = CoinRate.getRate("btc")
        bot.send_message(chat_id=update.message.chat_id,
                         text="1 BTC = " + current_price)
