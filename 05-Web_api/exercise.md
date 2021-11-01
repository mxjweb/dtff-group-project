# Web API Exercises

## The first part is about the Binance API

Information can be found here: https://binance-docs.github.io/apidocs/spot/en/#change-log

### What is the root URL?

The root url is: [https://api.binance.com](https://api.binance.com)

### What is the endpoint to retrieve klines (open-high-low-close data) for a specific cryptocurrency?

The endpoint is `/api/v3/klines`.

### Specify a request string to retrieve 75 observations of klines data for BTCUSDT since 2021-06-15.



The request would be `https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&startTime=1623708000&limit=75`

### Write a function (in Python, R or Julia) that retrieves 75 observations of klines data for a generic currency pair since a generic date. The function should take the currency pair and start date as input parameters.



## The rest is about the FRED API:
The root api is `https://api.stlouisfed.org/`.

### Read how authentication with API keys works. Create an account and obtain your own key.

### What is the root URL?

- What is the endpoint to retrieve time series observations?
- Construct a query string to retrieve the series of the monthly unemployment rate (seasonally adjusted) since 2020-01. Use the fake API key abc123 in the query string.