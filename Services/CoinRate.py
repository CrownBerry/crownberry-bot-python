import requests


class CoinRate:
    URL_STRING = "https://api.cryptonator.com/api/ticker/"

    @classmethod
    def getRate(cls, cur):
        request = requests.get(cls.URL_STRING + cur + "-usd")
        response = request.json()
        return response['ticker']['price']

