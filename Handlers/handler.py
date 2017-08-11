import config
from Services.CoinRate import CoinRate


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="I'm bot and I can tell you current exchange rate of BTC, BCC, ETH v0.02")


def btc(bot, update):
    coin_rate = CoinRate()
    btc_price = coin_rate.get_rate(cur="btc")
    bcc_price = coin_rate.get_rate(cur="bcc")
    eth_price = coin_rate.get_rate(cur="eth")
    bot.send_message(chat_id=update.message.chat_id,
                     text="1 BTC = $" + btc_price + "\n" +
                          "1 BCC = $" + bcc_price + "\n" +
                          "1 ETH = $" + eth_price)


def cat_or_dog(bot, update):
    pic_id = update.message.photo[-1].file_id
    new_file = bot.get_file(pic_id)
    str_pic = 'pic.jpg'
    new_file.download(str_pic)
    animal_name = config.myConvolutionalNeuralNetwork.recongnize(str_pic=str_pic)
    bot.send_message(chat_id=update.message.chat_id,
                     text=animal_name)


def topword_saving(bot, update):
    user = update.message.from_user.username
    message = update.message.text
    message = ''.join(c for c in message if c.isalpha())
    for word in message.split():
        if len(word) > 2:
            config.topwords.add_word(word, user)


def get_topword(bot, update, args):
    try:
        user = args[0]
    except:
        user = update.message.from_user.username
    print(user)
    answer = config.topwords.get_topword(user)
    bot.send_message(chat_id=update.message.chat_id,
                     text=answer)
