import requests

btc = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin/').json()
print(f"Price for 1 BTC is {str(btc[0]['price_usd'])}$")