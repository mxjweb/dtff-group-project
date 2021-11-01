# %%
import requests

# %%
url = 'https://api.binance.com/api/v3/klines'
params = {
  'symbol': 'BTCUSDT',
  'interval': '1h',
  'startTime': '1623708000',
  'limit': 75
}
response = requests.get(url, params=params)
print(response.json())