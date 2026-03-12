---
name: api-reference
description: Master reference for 190+ free APIs across 10 categories. Use when any task could benefit from external data — stocks, weather, news, government data, geocoding, jobs, AI/ML, dev tools, business intel, social media.
---

# API Reference — Master Catalog

## When to Use This
Whenever a task could benefit from live external data, check this reference first. You have 190+ free APIs available via curl — no MCP needed, no context cost until invoked.

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
| Severe weather alerts | NWS Alerts | None |

### "I need location/geography data"
→ `/geo-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/geo.json`

| Need | Best API | Auth |
|------|----------|------|
| Address → lat/lon | Nominatim | None |
| Lat/lon → address | Nominatim or BigDataCloud | None |
| IP → location | ip-api | None |
| Country info | REST Countries | None |
| ZIP code lookup | Zippopotam.us | None |
| Timezone by location | TimeZoneDB | Key |
| Directions/routing | Mapbox | Key |

### "I need government/public data"
→ `/government-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/government.json`

| Need | Best API | Auth |
|------|----------|------|
| Drug/food recalls | OpenFDA | None |
| Company SEC filings | SEC EDGAR | None |
| NASA imagery | NASA APOD | Key |
| Earthquake data | USGS | None |
| Crime statistics | FBI Crime Data | None |
| Federal spending | USASpending.gov | None |
| Congressional bills | Congress.gov | Key |
| Employment/labor data | BLS | None |
| Global health stats | WHO GHO | None |
| World economic data | World Bank | None |
| Air quality | EPA AQS | None |
| Federal regulations | Federal Register | None |
| Sanctions lists | Open Sanctions | None |

### "I need business/company data"
→ `/business-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/business.json`

| Need | Best API | Auth |
|------|----------|------|
| Find email addresses | Hunter.io | Key |
| Company logo by domain | Clearbit Logo | None |
| UK company data | Companies House | None |
| Company search | Open Corporates | None |
| Tech stack detection | BuiltWith | Key |
| Domain/WHOIS info | WhoisXML | Key |
| EU VAT validation | VIES | None |
| Brand assets/logos | Brandfetch | Key |
| Lead enrichment | Apollo.io or FullContact | Key |

### "I need job listings"
→ `/jobs-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/jobs.json`

| Need | Best API | Auth |
|------|----------|------|
| Remote jobs | Remotive or Himalayas.app | None |
| Job search (broad) | Adzuna or JSearch | Key |
| 4-day work week jobs | 4DayWeek.io | None |
| Startup jobs | Wellfound or Startup.jobs | None |
| Freelance/design jobs | Dribbble Jobs | None |
| European tech jobs | Arbeitnow | None |
| Digital nomad jobs | Working Nomads or Jobicy | None |

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
| Text-to-speech | VoiceRSS or ElevenLabs | Key |
| Speech-to-text | AssemblyAI or Deepgram | Key |
| Sentiment analysis | Text-Processing.com | None |
| Word associations | Datamuse | None |
| Math/computation | Wolfram Alpha | Key |

### "I need developer tools"
→ `/dev-tools-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/dev-tools.json`

| Need | Best API | Auth |
|------|----------|------|
| GitHub repo/user info | GitHub Public API | None (60/hr) |
| Vulnerability check | OSV.dev or Snyk | None/Key |
| HTTP testing | HTTPBin or Postman Echo | None |
| Fake REST data | JSONPlaceholder or ReqRes | None |
| Dynamic badges | Shields.io | None |
| Package info (npm) | npm Registry | None |
| Package info (Python) | PyPI | None |
| Package info (Rust) | crates.io | None |
| SSL/TLS testing | SSL Labs | None |
| URL shortening | CleanURI | None |
| Archived web pages | Wayback Machine | None |
| HTML validation | W3C Validator | None |

### "I need social/community data"
→ `/social-apis` — Read `/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/social.json`

| Need | Best API | Auth |
|------|----------|------|
| Reddit posts/comments | Reddit JSON (append .json) | None |
| HackerNews stories | HN Algolia or Firebase | None |
| Wikipedia articles | Wikipedia/MediaWiki API | None |
| Structured knowledge | Wikidata SPARQL | None |
| Book data | Open Library | None |
| Archived websites | Archive.org Wayback | None |
| Music metadata | MusicBrainz | None |
| Video game data | RAWG | Key |
| Anime/manga | Jikan (MAL) | None |
| Dev articles | DEV.to | None |
| Q&A data | Stack Exchange | None |

---

## How to Call Any API

### Step 1: Read the category file
```
Read /Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/{category}.json
```

### Step 2: Check if key is needed
```bash
# If API needs a key, check env
echo $ENV_VAR_NAME
# If empty, tell user to register (see registration guide)
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
| `/finance-apis` | finance | 16 |
| `/news-apis` | news | 16 |
| `/weather-apis` | weather | 16 |
| `/geo-apis` | geo | 15 |
| `/government-apis` | government | 22 |
| `/business-apis` | business | 19 |
| `/social-apis` | social | 18 |
| `/jobs-apis` | jobs | 20 |
| `/ai-ml-apis` | ai-ml | 22 |
| `/dev-tools-apis` | dev-tools | 26 |
| **Total** | | **190** |

---

## API Key Registration Reference

Full guide with signup URLs: `/Users/elizabethknopf/Documents/claudec/active/api-catalog/API-KEY-REGISTRATION-GUIDE.md`

### Tier 1 — Register First (highest value)
| API | Env Var | Free Tier | URL |
|-----|---------|-----------|-----|
| FRED | `FRED_API_KEY` | Unlimited | fred.stlouisfed.org/docs/api/api_key.html |
| Finnhub | `FINNHUB_API_KEY` | 60/min | finnhub.io/register |
| Alpha Vantage | `ALPHA_VANTAGE_API_KEY` | 25/day | alphavantage.co/support/#api-key |
| NewsAPI | `NEWS_API_KEY` | 100/day | newsapi.org/register |
| OpenWeatherMap | `OPENWEATHER_KEY` | 1000/day | openweathermap.org/appid |
| NASA | `NASA_API_KEY` | 1000/hr | api.nasa.gov |

### Tier 2 — Register Next
| API | Env Var | Free Tier | URL |
|-----|---------|-----------|-----|
| HuggingFace | `HUGGINGFACE_TOKEN` | Free inference | huggingface.co/settings/tokens |
| Twelve Data | `TWELVE_DATA_API_KEY` | 800/day | twelvedata.com/account/api-keys |
| WeatherAPI | `WEATHERAPI_KEY` | 1M/month | weatherapi.com/signup.aspx |
| Groq | `GROQ_API_KEY` | Free fast inference | console.groq.com/keys |
| OpenCage | `OPENCAGE_API_KEY` | 2500/day | opencagedata.com/users/sign_up |
| Congress.gov | `CONGRESS_API_KEY` | Unlimited | api.congress.gov/sign-up |
| Census | `CENSUS_API_KEY` | Unlimited | api.census.gov/data/key_signup.html |
| Polygon.io | `POLYGON_API_KEY` | 5/min | polygon.io/dashboard/signup |

### Tier 3 — Register When Needed
Hunter.io, Adzuna, Abstract API, GeoNames, Mapbox, Event Registry, WhoisXML, OCR.space, AssemblyAI, ElevenLabs, Wolfram Alpha, BuiltWith, Brandfetch, Together AI, Deepgram, Replicate

---

## Future Categories (Not Yet Cataloged)

These categories have known free APIs but haven't been added to the catalog yet. When needed, research and add them:

### Entertainment & Media
| API | What it does | Auth |
|-----|-------------|------|
| TMDB | Movies, TV shows, actors | Key (free) |
| OMDB | Movie data (like IMDB) | Key (1k/day) |
| Spotify Web API | Playlists, tracks, artists | OAuth |
| Last.fm | Music stats, scrobbles | Key (free) |
| TVMaze | TV show schedules, episodes | None |
| IGDB | Video game database | Key |
| Podcast Index | Podcast search, episodes | Key (free) |
| Deezer | Music catalog | None (public) |
| iTunes Search | Apple media search | None |
| Open Movie Database | Film data | Key (free) |

### Transportation & Travel
| API | What it does | Auth |
|-----|-------------|------|
| OpenSky Network | Live flight tracking | None |
| AviationStack | Flight status, airports | Key (free) |
| ADS-B Exchange | Aircraft tracking | None |
| Transitland | Public transit routes | None |
| OpenChargeMap | EV charging stations | None |
| Google Flights (SerpAPI) | Flight prices | Key |
| Skyscanner (RapidAPI) | Flight search | Key |
| Rome2Rio | Multi-modal travel routes | Key |
| OpenTripMap | Points of interest | Key (free) |
| Navitia | Public transport routing | Key (free) |

### Science & Research
| API | What it does | Auth |
|-----|-------------|------|
| PubMed/NCBI | Medical research papers | None |
| arXiv | Preprint papers | None |
| Semantic Scholar | Paper search, citations | None |
| CrossRef | DOI lookup, citations | None |
| OpenAlex | Academic papers, authors | None |
| CERN Open Data | Particle physics data | None |
| NASA Exoplanet Archive | Exoplanet data | None |
| GBIF | Biodiversity data | None |
| iNaturalist | Species observations | None |
| Launch Library 2 | Space launches | None |

### Health & Wellness
| API | What it does | Auth |
|-----|-------------|------|
| OpenFDA Drugs | Drug info, interactions | None |
| CDC WONDER | Public health data | None |
| Nutritionix | Food nutrition data | Key |
| USDA FoodData | Nutrient database | Key (free) |
| Open Disease | Disease statistics | None |
| HealthData.gov | Health datasets | None |
| DrugBank (limited) | Drug interactions | Key |
| MyFitnessPal (unofficial) | Calorie data | None |

### Education
| API | What it does | Auth |
|-----|-------------|------|
| Wikipedia | Knowledge articles | None |
| Wikibooks | Free textbook content | None |
| Open Trivia DB | Quiz questions | None |
| Numbers API | Number/date facts | None |
| Dictionary API | Word definitions | None |
| Merriam-Webster | Dictionary/thesaurus | Key (free) |
| LibreTexts | Open textbooks | None |
| OpenStax | Free textbook catalog | None |

### Utilities & Misc
| API | What it does | Auth |
|-----|-------------|------|
| QR Code Generator | Generate QR codes | None |
| Lorem Ipsum | Placeholder text | None |
| RandomUser | Fake user data | None |
| UUID Generator | Generate UUIDs | None |
| Color API | Color info, palettes | None |
| Unsplash | Stock photos | Key (free) |
| Pexels | Stock photos/video | Key (free) |
| AbstractAPI (all) | 10+ utility APIs | Key (free) |
| IPinfo | IP intelligence | Key (free) |
| Have I Been Pwned | Breach checking | Key |

### Real Estate & Property
| API | What it does | Auth |
|-----|-------------|------|
| Zillow (RapidAPI) | Home values, listings | Key |
| Realty Mole | Property data | Key (free tier) |
| Rentcast | Rental estimates | Key (free tier) |
| ATTOM | Property records | Key |
| Walk Score | Walkability ratings | Key (free) |
| Google Places | Nearby amenities | Key (free tier) |

### Crypto & Web3
| API | What it does | Auth |
|-----|-------------|------|
| CoinGecko | Already in finance | None |
| CoinCap | Real-time crypto | None |
| Etherscan | Ethereum explorer | Key (free) |
| Blockchain.com | Bitcoin data | None |
| DeFi Llama | DeFi protocol TVL | None |
| CryptoCompare | Crypto social/market | Key (free) |
| Alchemy | Web3/NFT data | Key (free tier) |
