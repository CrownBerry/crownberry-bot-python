import requests


class CoinRate:
    URL_STRING = "https://api.cryptonator.com/api/ticker/"

    def __init__(self):
        pass

    def get_rate(self, cur: str, cash: str) -> str:
        try:
            request = requests.get(self.URL_STRING + cur + "-" + cash)
            response = request.json()
            rate = round(float(response['ticker']['price']), 2)
        except KeyError:
            rate = 'None'
        return str(rate)
