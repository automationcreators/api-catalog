---
name: crypto-web3-apis
description: Query free crypto and Web3 APIs via curl. Reads catalog for endpoints and auth.
---

# Crypto & Web3 APIs Skill

## How to use
When the user invokes `/crypto-web3-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/crypto-web3.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| Crypto prices / market data | CoinCap or Coinpaprika | No auth, real-time data |
| Bitcoin price index | CoinDesk | No auth, BPI in multiple currencies |
| Exchange rates (crypto) | CryptoCompare or Cryptonator | No auth, multi-exchange |
| Bitcoin mempool / fees | Mempool | No auth, fee estimation |
| Ethereum blockchain | Gemini or ZMOK | No auth for public endpoints |
| DeFi / DEX aggregation | 1inch or 0x | No auth for public queries |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- If no key needed (CoinCap, Coinpaprika, CoinDesk, Mempool, CryptoCompare), proceed directly
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**CoinCap (crypto market data, no auth):**
```bash
# Top assets by market cap
curl -s "https://api.coincap.io/v2/assets?limit=10" | jq '.data[] | {rank, name, symbol, priceUsd, changePercent24Hr, marketCapUsd}'

# Get specific asset
curl -s "https://api.coincap.io/v2/assets/bitcoin" | jq '.data | {name, priceUsd, changePercent24Hr, marketCapUsd, volumeUsd24Hr}'

# Price history (24h)
curl -s "https://api.coincap.io/v2/assets/bitcoin/history?interval=h1" | jq '.data[-5:] | .[] | {time, priceUsd}'
```

**CoinDesk (Bitcoin Price Index, no auth):**
```bash
# Current BPI
curl -s "https://api.coindesk.com/v1/bpi/currentprice.json" | jq '{time: .time.updated, USD: .bpi.USD.rate, EUR: .bpi.EUR.rate, GBP: .bpi.GBP.rate}'

# Historical BPI
curl -s "https://api.coindesk.com/v1/bpi/historical/close.json?start=2026-03-01&end=2026-03-12" | jq '.bpi'
```

**Coinpaprika (crypto data, no auth):**
```bash
# Top coins
curl -s "https://api.coinpaprika.com/v1/tickers?limit=10" | jq '.[] | {name, symbol, rank, quotes: .quotes.USD | {price, volume_24h, market_cap, percent_change_24h}}'

# Coin details
curl -s "https://api.coinpaprika.com/v1/coins/btc-bitcoin" | jq '{name, symbol, rank, description, started_at}'
```

**Mempool (Bitcoin mempool, no auth):**
```bash
# Recommended fees
curl -s "https://mempool.space/api/v1/fees/recommended" | jq '.'

# Mempool stats
curl -s "https://mempool.space/api/mempool" | jq '{count, vsize, total_fee}'

# Latest block
curl -s "https://mempool.space/api/blocks/tip/hash"
```

**CryptoCompare (comparison data, no auth):**
```bash
# Multi-coin price
curl -s "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,GBP,JPY" | jq '.'

# Top exchanges by volume
curl -s "https://min-api.cryptocompare.com/data/top/exchanges?fsym=BTC&tsym=USD&limit=5" | jq '.Data[] | {exchange, volume24h}'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- The specific value(s) requested
- Relevant context (price changes, volume, market cap)
- Source attribution (which API provided the data)

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **CoinCap** | None | Real-time crypto prices, market cap rankings |
| **CoinDesk** | None | Bitcoin Price Index in multiple currencies |
| **Coinpaprika** | None | Crypto prices, volume, coin details |
| **Mempool** | None | Bitcoin mempool, fee estimation, blocks |
| **CryptoCompare** | None | Multi-exchange price comparison |
| **Cryptonator** | None | Crypto exchange rates |
| **Coinlore** | None | Crypto prices and volume |
| **Gemini** | None (public) | Gemini exchange public data |
| **CoinMarketCap** | API key (query param) | Comprehensive crypto market data |
| **Etherscan** | API key (query param) | Ethereum blockchain explorer |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| CoinCap | 200 requests/minute |
| CoinDesk | No stated limit |
| Coinpaprika | 10 requests/second |
| Mempool | No stated limit |
| CryptoCompare | 100,000 calls/month |
| CoinMarketCap | 333 calls/day |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `COINMARKETCAP_API_KEY` | CoinMarketCap | https://coinmarketcap.com/api/ |
| `ETHERSCAN_API_KEY` | Etherscan | https://etherscan.io/apis |
| `ALCHEMY_ETHEREUM_API_KEY` | Alchemy | https://docs.alchemy.com/ |
| `COINAPI_API_KEY` | CoinAPI | https://docs.coinapi.io/ |
| `COINRANKING_API_KEY` | CoinRanking | https://developers.coinranking.com/ |
