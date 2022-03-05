from utils import FREE_CURRENCY_URI
import requests


def get_currency_rate(currency):
    response = requests.get(FREE_CURRENCY_URI)
    if response.status_code != 200:
        print(f"unexpected status code {response.status_code}. stopping...")
        raise
    body = response.json()
    data = body['data'][str.upper(currency)]
    return data

