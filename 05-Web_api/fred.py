# %%
import requests
import os

# API_KEY = os.getenv("FRED_KEY") # uncomment this line if you have the real api key.

API_KEY = "abc123" 
# %%
url = 'https://api.stlouisfed.org/fred/series/observations'
params = {
    'api_key': API_KEY,
    'series_id': 'UNRATE',
    'file_type': 'json',
    'observation_start': '2020-01-01'
}
response = requests.get(url, params=params)
print(response.json())

# %%