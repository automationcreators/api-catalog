---
name: finance-apis
description: Query free finance APIs via curl. Reads catalog for endpoints and auth.
---

# Finance APIs Skill

## How to use
When the user invokes `/finance-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/finance.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| Stock quote / price | Alpha Vantage or Finnhub | Real-time quotes |
| Crypto price | CoinGecko | No auth required, comprehensive |
| Forex / currency exchange | ExchangeRate-API (no auth) or Twelve Data | Live rates |
| Economic indicators (GDP, CPI, unemployment) | FRED | Official Federal Reserve data |
| Historical stock data | Alpha Vantage or Twelve Data | OHLCV time series |
| Company news | Finnhub | News with date range filtering |
| Crypto market overview | CoinGecko | Market cap rankings |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- If no key needed (CoinGecko, ExchangeRate-API), proceed directly
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**Alpha Vantage (stock quotes, time series):**
```bash
# Real-time stock quote
curl -s "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=AAPL&apikey=$ALPHA_VANTAGE_API_KEY" | jq '.'

# Daily time series (last 100 days)
curl -s "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=$ALPHA_VANTAGE_API_KEY" | jq '."Time Series (Daily)" | to_entries[:5]'

# Intraday prices
curl -s "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=5min&apikey=$ALPHA_VANTAGE_API_KEY" | jq '.'
```

**CoinGecko (crypto, no auth):**
```bash
# Current price for one or more coins
curl -s "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd" | jq '.'

# Top coins by market cap
curl -s "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1" | jq '.[] | {name, current_price, market_cap, price_change_percentage_24h}'

# Historical chart data (30 days)
curl -s "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30" | jq '.prices | length'
```

**Finnhub (quotes, company news):**
```bash
# Real-time quote
curl -s "https://finnhub.io/api/v1/quote?symbol=AAPL&token=$FINNHUB_API_KEY" | jq '.'

# Company news
curl -s "https://finnhub.io/api/v1/company-news?symbol=AAPL&from=2026-03-01&to=2026-03-12&token=$FINNHUB_API_KEY" | jq '.[:5] | .[] | {headline, summary, url}'
```

**FRED (economic data):**
```bash
# GDP data
curl -s "https://api.stlouisfed.org/fred/series/observations?series_id=GDP&api_key=$FRED_API_KEY&file_type=json&sort_order=desc&limit=5" | jq '.observations[:5]'

# Search for economic series
curl -s "https://api.stlouisfed.org/fred/series/search?search_text=unemployment+rate&api_key=$FRED_API_KEY&file_type=json&limit=5" | jq '.seriess[:5] | .[] | {id, title, frequency}'

# CPI (inflation)
curl -s "https://api.stlouisfed.org/fred/series/observations?series_id=CPIAUCSL&api_key=$FRED_API_KEY&file_type=json&sort_order=desc&limit=12" | jq '.observations'
```

**ExchangeRate-API (forex, no auth):**
```bash
# Latest exchange rates from USD
curl -s "https://open.er-api.com/v6/latest/USD" | jq '{base: .base_code, rates: {EUR: .rates.EUR, GBP: .rates.GBP, JPY: .rates.JPY, CAD: .rates.CAD}}'
```

**Twelve Data (stocks, forex, crypto):**
```bash
# Real-time price
curl -s "https://api.twelvedata.com/price?symbol=EUR/USD&apikey=$TWELVE_DATA_API_KEY" | jq '.'

# Detailed quote
curl -s "https://api.twelvedata.com/quote?symbol=GOOGL&apikey=$TWELVE_DATA_API_KEY" | jq '.'

# Time series
curl -s "https://api.twelvedata.com/time_series?symbol=AAPL&interval=1day&outputsize=30&apikey=$TWELVE_DATA_API_KEY" | jq '.values[:5]'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- The specific value(s) requested
- Relevant context (change %, volume, date range)
- Source attribution (which API provided the data)

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **Alpha Vantage** | API key (query param) | Stock quotes, daily/intraday time series |
| **CoinGecko** | None | Crypto prices, market cap rankings, historical charts |
| **Finnhub** | API key (query param) | Real-time quotes, company news, stock candles |
| **FRED** | API key (query param) | GDP, CPI, unemployment, interest rates, economic data |
| **ExchangeRate-API** | None | Currency exchange rates, forex conversion |
| **Twelve Data** | API key (query param) | Stocks, forex, crypto time series and quotes |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| Alpha Vantage | 25 requests/day, 5/minute |
| CoinGecko | 10-30 calls/minute |
| Finnhub | 60 calls/minute |
| FRED | 120 requests/minute, unlimited daily |
| ExchangeRate-API | No limit (updates daily) |
| Twelve Data | 800 credits/day, 8 credits/minute |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `ALPHA_VANTAGE_API_KEY` | Alpha Vantage | https://www.alphavantage.co/support/#api-key |
| `FINNHUB_API_KEY` | Finnhub | https://finnhub.io/register |
| `FRED_API_KEY` | FRED | https://fred.stlouisfed.org/docs/api/api_key.html |
| `TWELVE_DATA_API_KEY` | Twelve Data | https://twelvedata.com/account |

## Common Series IDs (FRED)
- `GDP` - Gross Domestic Product
- `CPIAUCSL` - Consumer Price Index (inflation)
- `UNRATE` - Unemployment Rate
- `FEDFUNDS` - Federal Funds Rate
- `DGS10` - 10-Year Treasury Rate
- `SP500` - S&P 500 Index
