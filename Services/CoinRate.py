import requests


class CoinRate:
    URL_STRING = "https://api.cryptonator.com/api/ticker/"

    def __init__(self):
        pass

    def get_rate(self, cur: str) -> str:
        request = requests.get(self.URL_STRING + cur + "-usd")
        response = request.json()
        rate = round(float(response['ticker']['price']), 2)
        return str(rate)
