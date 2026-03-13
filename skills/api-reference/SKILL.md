---
name: api-reference
description: Master reference for 1,586 free APIs across 25 categories. Use when any task could benefit from external data — stocks, weather, news, government data, geocoding, jobs, AI/ML, dev tools, business intel, social media, entertainment, music, food, books, animals, sports, transportation, science, health, education, photography, crypto, security, shopping, utilities.
---

# API Reference — Master Catalog (v3.0)

## When to Use This
Whenever a task could benefit from live external data, check this reference first. You have 1,586 free APIs available via curl — no MCP needed, no context cost until invoked.

## Quick Lookup: What API Should I Use?

### "I need stock/crypto/financial data"
→ `/finance-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/finance.json`

| Need | Best API | Auth |
|------|----------|------|
| Stock quote | Finnhub or Alpha Vantage | Key |
| Crypto price | CoinGecko or Binance | None |
| Forex rates | ExchangeRate-API | None |
| Economic indicators (GDP, CPI) | FRED | Key |
| Historical stock data | Twelve Data or Polygon.io | Key |
| Company financials | SEC EDGAR | None |

### "I need news/headlines"
→ `/news-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/news.json`

| Need | Best API | Auth |
|------|----------|------|
| Top headlines | NewsAPI | Key |
| Tech/startup news | HackerNews Algolia | None |
| Global events | GDELT Project | None |
| Space news | Spaceflight News API | None |
| Convert RSS to JSON | RSS2JSON | None |
| Search articles | GNews or Newscatcher | Key |

### "I need weather/climate data"
→ `/weather-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/weather.json`

| Need | Best API | Auth |
|------|----------|------|
| Current weather + forecast | Open-Meteo | None |
| US official forecast | NWS (weather.gov) | None |
| Air quality index | WAQI | Key |
| UV index | Open-Meteo UV | None |
| Historical weather | Oikolab | Key |

### "I need location/geography data"
→ `/geo-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/geo.json`

| Need | Best API | Auth |
|------|----------|------|
| Address → lat/lon | Nominatim | None |
| IP → location | ip-api | None |
| Country info | REST Countries | None |
| ZIP code lookup | Zippopotam.us | None |
| Timezone by location | TimeZoneDB | Key |

### "I need government/public data"
→ `/government-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/government.json`

| Need | Best API | Auth |
|------|----------|------|
| Drug/food recalls | OpenFDA | None |
| Company SEC filings | SEC EDGAR | None |
| NASA imagery | NASA APOD | Key |
| Earthquake data | USGS | None |
| Federal spending | USASpending.gov | None |
| Employment/labor data | BLS | None |
| Global health stats | WHO GHO | None |

### "I need business/company data"
→ `/business-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/business.json`

| Need | Best API | Auth |
|------|----------|------|
| Find email addresses | Hunter.io | Key |
| Company logo by domain | Clearbit Logo | None |
| Company search | Open Corporates | None |
| Tech stack detection | BuiltWith | Key |
| EU VAT validation | VIES | None |

### "I need job listings"
→ `/jobs-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/jobs.json`

| Need | Best API | Auth |
|------|----------|------|
| Remote jobs | Remotive or Himalayas.app | None |
| Job search (broad) | Adzuna or JSearch | Key |
| Startup jobs | Wellfound or Startup.jobs | None |
| European tech jobs | Arbeitnow | None |

### "I need AI/ML capabilities"
→ `/ai-ml-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/ai-ml.json`

| Need | Best API | Auth |
|------|----------|------|
| Run ML models | HuggingFace Inference | Key |
| Fast LLM inference | Groq | Key |
| Local LLM | Ollama | None |
| Translation | LibreTranslate or MyMemory | None |
| Grammar checking | LanguageTool | None |
| OCR (image → text) | OCR.space | Key |
| Math/computation | Wolfram Alpha | Key |

### "I need developer tools"
→ `/dev-tools-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/dev-tools.json`

| Need | Best API | Auth |
|------|----------|------|
| GitHub repo/user info | GitHub Public API | None (60/hr) |
| Vulnerability check | OSV.dev or Snyk | None/Key |
| HTTP testing | HTTPBin or Postman Echo | None |
| Package info (npm/PyPI/crates) | npm, PyPI, crates.io | None |
| Dynamic badges | Shields.io | None |
| URL shortening | CleanURI | None |

### "I need social/community data"
→ `/social-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/social.json`

| Need | Best API | Auth |
|------|----------|------|
| Reddit posts/comments | Reddit JSON (append .json) | None |
| HackerNews stories | HN Algolia or Firebase | None |
| Wikipedia articles | Wikipedia/MediaWiki API | None |
| Dev articles | DEV.to | None |
| Q&A data | Stack Exchange | None |

### "I need entertainment/games/movies"
→ `/entertainment-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/entertainment.json`

| Need | Best API | Auth |
|------|----------|------|
| Movie/TV data | TMDB or OMDB | Key |
| TV show schedules | TVMaze | None |
| Video game data | RAWG | Key |
| Random jokes | JokeAPI | None |
| Pokemon data | PokeAPI | None |
| Anime/manga | Jikan (MAL) | None |

### "I need music data"
→ `/music-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/music.json`

| Need | Best API | Auth |
|------|----------|------|
| Music metadata | MusicBrainz or Last.fm | None/Key |
| Song search | Deezer or iTunes Search | None |
| Audio features | Spotify Web API | OAuth |
| Lyrics | Lyrics.ovh | None |

### "I need food/recipe data"
→ `/food-drink-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/food-drink.json`

| Need | Best API | Auth |
|------|----------|------|
| Meal recipes | TheMealDB | None |
| Cocktail recipes | TheCocktailDB | None |
| Product nutrition | Open Food Facts | None |
| Recipe search | Edamam | Key |

### "I need book/literature data"
→ `/books-literature-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/books-literature.json`

| Need | Best API | Auth |
|------|----------|------|
| Book search | Google Books or Open Library | None |
| Poetry | PoetryDB | None |
| Public domain books | Gutendex | None |

### "I need animal/nature data"
→ `/animals-nature-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/animals-nature.json`

| Need | Best API | Auth |
|------|----------|------|
| Dog images | Dog CEO | None |
| Cat facts | Cat Facts | None |
| Bird observations | eBird | Key |
| Threatened species | IUCN Red List | Key |

### "I need sports data"
→ `/sports-fitness-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/sports-fitness.json`

| Need | Best API | Auth |
|------|----------|------|
| Team/event search | TheSportsDB | None |
| NBA stats | balldontlie | None |
| Football/soccer | Football-Data.org | Key |

### "I need transportation/flight data"
→ `/transportation-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/transportation.json`

| Need | Best API | Auth |
|------|----------|------|
| Live flight tracking | OpenSky Network | None |
| EV charging stations | OpenChargeMap | Key |
| Aircraft tracking | ADS-B Exchange | None |

### "I need science/space data"
→ `/science-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/science.json`

| Need | Best API | Auth |
|------|----------|------|
| Astronomy picture | NASA APOD | Key |
| SpaceX launches | SpaceX API | None |
| Upcoming launches | Launch Library 2 | None |
| Earthquakes | USGS Earthquake | None |
| Research papers | arXiv or Semantic Scholar | None |
| Chemical compounds | PubChem | None |

### "I need health/medical data"
→ `/health-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/health.json`

| Need | Best API | Auth |
|------|----------|------|
| Drug adverse events | OpenFDA | None |
| Food nutrition | USDA FoodData Central | Key |
| Disease stats | Disease.sh | None |

### "I need education/reference data"
→ `/education-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/education.json`

| Need | Best API | Auth |
|------|----------|------|
| Word definitions | Free Dictionary API | None |
| Trivia questions | Open Trivia DB | None |
| Academic papers | Semantic Scholar or CrossRef | None |
| Wikipedia summaries | Wikipedia REST API | None |

### "I need photos/media"
→ `/photography-media-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/photography-media.json`

| Need | Best API | Auth |
|------|----------|------|
| Stock photos | Unsplash or Pexels | Key |
| Placeholder images | Lorem Picsum | None |
| Free images | Pixabay | Key |

### "I need crypto/blockchain data"
→ `/crypto-web3-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/crypto-web3.json`

| Need | Best API | Auth |
|------|----------|------|
| Crypto prices/market cap | CoinCap | None |
| Ethereum data | Etherscan | Key |
| DeFi TVL data | DeFi Llama | None |
| Bitcoin blockchain | Blockchain.com | None |

### "I need security/threat data"
→ `/security-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/security.json`

| Need | Best API | Auth |
|------|----------|------|
| IP reputation | AbuseIPDB | Key |
| Malware scanning | VirusTotal | Key |
| Internet scanning | Shodan | Key |
| Breach checking | Have I Been Pwned | Key |

### "I need shopping/product data"
→ `/shopping-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/shopping.json`

| Need | Best API | Auth |
|------|----------|------|
| Test product data | Fake Store API or DummyJSON | None |
| Product search | Best Buy (RapidAPI) | Key |

### "I need utility/misc tools"
→ `/utilities-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/utilities.json`

| Need | Best API | Auth |
|------|----------|------|
| Random user profiles | RandomUser | None |
| QR code generation | goqr.me | None |
| IP geolocation | ip-api | None |
| Placeholder text | Bacon Ipsum | None |
| UUID generation | httpbin | None |

---

## How to Call Any API

### Step 1: Read the category file
```
Read /Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/{category}.json
```

### Step 2: Check if key is needed
```bash
echo $ENV_VAR_NAME
```

### Step 3: Call via curl
```bash
# No-auth API
curl -s "https://api.example.com/endpoint?param=value" | jq '.'

# Query param auth
curl -s "https://api.example.com/endpoint?apikey=$ENV_VAR&param=value" | jq '.'

# Header auth
curl -s -H "Authorization: Bearer $ENV_VAR" "https://api.example.com/endpoint" | jq '.'
```

### Step 4: Parse and present
Use jq to extract relevant fields. Present data clearly with source attribution.

---

## Category Skill Slash Commands
| Command | Category | APIs |
|---------|----------|------|
| `/finance-apis` | finance | 56 |
| `/news-apis` | news | 34 |
| `/weather-apis` | weather | 41 |
| `/geo-apis` | geo | 15 |
| `/government-apis` | government | 106 |
| `/business-apis` | business | 42 |
| `/social-apis` | social | 58 |
| `/jobs-apis` | jobs | 34 |
| `/ai-ml-apis` | ai-ml | 22 |
| `/dev-tools-apis` | dev-tools | 142 |
| `/entertainment-apis` | entertainment | 189 |
| `/music-apis` | music | 32 |
| `/food-drink-apis` | food-drink | 24 |
| `/books-literature-apis` | books-literature | 34 |
| `/animals-nature-apis` | animals-nature | 46 |
| `/sports-fitness-apis` | sports-fitness | 35 |
| `/transportation-apis` | transportation | 73 |
| `/science-apis` | science | 78 |
| `/health-apis` | health | 31 |
| `/education-apis` | education | 13 |
| `/photography-media-apis` | photography-media | 54 |
| `/crypto-web3-apis` | crypto-web3 | 60 |
| `/security-apis` | security | 71 |
| `/shopping-apis` | shopping | 15 |
| `/utilities-apis` | utilities | 281 |
| **Total** | **25 categories** | **1,586** |

---

## API Key Registration Reference

Full guide: `/Users/elizabethknopf/Documents/claudec/active/api-catalog/API-KEY-REGISTRATION-GUIDE.md`

### Tier 1 — Register First (highest value)
| API | Env Var | Free Tier |
|-----|---------|-----------|
| FRED | `FRED_API_KEY` | Unlimited |
| Finnhub | `FINNHUB_API_KEY` | 60/min |
| Alpha Vantage | `ALPHA_VANTAGE_API_KEY` | 25/day |
| NewsAPI | `NEWS_API_KEY` | 100/day |
| OpenWeatherMap | `OPENWEATHER_KEY` | 1000/day |
| NASA | `NASA_API_KEY` | 1000/hr |

### Tier 2 — Register Next
HuggingFace, Twelve Data, WeatherAPI, Groq, OpenCage, Congress.gov, Census, Polygon.io, Unsplash, Pexels, Football-Data.org, Etherscan, Shodan, USDA FoodData

### No Auth Required (just use them)
CoinGecko, Binance, Open-Meteo, NWS, ip-api, REST Countries, Reddit JSON, HN Algolia, TheMealDB, Dog CEO, PokeAPI, TVMaze, JokeAPI, Open Library, USGS Earthquake, SpaceX API, DeFi Llama, CoinCap, Fake Store API, RandomUser, Lorem Picsum, Disease.sh, arXiv, PoetryDB, TheSportsDB, OpenSky Network

---

## Tier System
- **Tier 1**: Full detail — 2-3 endpoints, curl examples, rate limits
- **Tier 2**: Basic detail — 1 endpoint, 1 example
- **Tier 3**: Metadata only — searchable, Claude reads docs on-demand when needed
