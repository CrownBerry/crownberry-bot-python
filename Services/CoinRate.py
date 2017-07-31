import requests


class CoinRate:
    URL_STRING = "https://api.cryptonator.com/api/ticker/"

    @classmethod
    def getRate(cls, cur):
        request = requests.get(cls.URL_STRING + cur + "-usd")
        response = request.json()
        rate = round(response['ticker']['price'],2)
        return rate

