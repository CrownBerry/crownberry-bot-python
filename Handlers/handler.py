from Services.CoinRate import CoinRate


class MainHandlers:
    @staticmethod
    def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id,
                         text="I'm bot, and I'm not ready yet, but I deployed with docker-compose =_=")

    @staticmethod
    def btc(bot, update):
        btc_price = CoinRate.getRate("btc")
        eth_price = CoinRate.getRate("eth")
        bot.send_message(chat_id=update.message.chat_id,
                         text="1 BTC = " + round(btc_price,2) + "\n" +
                         "1 ETH = " + round(eth_price,2))
