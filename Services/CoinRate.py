import requests


class CoinRate:
    URL_STRING = "https://api.cryptonator.com/api/ticker/"

    @classmethod
    def get_rate(cls, cur):
        request = requests.get(cls.URL_STRING + cur + "-usd")
        response = request.json()
        rate = round(float(response['ticker']['price']),2)
        return str(rate)

