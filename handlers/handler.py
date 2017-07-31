class MainHandlers:
    @staticmethod
    def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id,
                         text="I'm bot, and I'm not ready yet, but I deployed with docker-compose")

    @staticmethod
    def btc(bot, update):
        bot.send_message(chat_id=update.message.chat_id,
                         text="Soon!")
