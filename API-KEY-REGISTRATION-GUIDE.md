# API Key Registration Guide

## Priority Order & Reference Table

Register these free API keys in order of value. All are free tier — no credit card required unless noted.

---

## Tier 1: Register First (Highest Value, Immediate Use)

These unlock the most useful capabilities across your daily workflow.

| # | API | Free Tier | Time to Register | Env Var | Register URL |
|---|-----|-----------|-----------------|---------|-------------|
| 1 | **FRED** (Federal Reserve) | Unlimited requests | 2 min | `FRED_API_KEY` | https://fred.stlouisfed.org/docs/api/api_key.html |
| 2 | **Finnhub** | 60 calls/min | 1 min | `FINNHUB_API_KEY` | https://finnhub.io/register |
| 3 | **Alpha Vantage** | 25 req/day | 1 min (instant key) | `ALPHA_VANTAGE_API_KEY` | https://www.alphavantage.co/support/#api-key |
| 4 | **NewsAPI** | 100 req/day | 2 min | `NEWS_API_KEY` | https://newsapi.org/register |
| 5 | **OpenWeatherMap** | 1,000 calls/day | 2 min | `OPENWEATHER_KEY` | https://openweathermap.org/appid |
| 6 | **NASA** | 1,000 req/hr | 1 min | `NASA_API_KEY` | https://api.nasa.gov/ |

**Why these first:** FRED gives you unlimited economic data (GDP, CPI, unemployment, interest rates). Finnhub + Alpha Vantage cover all stock/market data. NewsAPI powers headline search. OpenWeatherMap is the most reliable weather API. NASA is just cool and free.

---

## Tier 2: Register Next (High Value, Broader Coverage)

These add depth to categories you'll use regularly.

| # | API | Free Tier | Env Var | Register URL |
|---|-----|-----------|---------|-------------|
| 7 | **HuggingFace** | Free inference API | `HUGGINGFACE_TOKEN` | https://huggingface.co/settings/tokens |
| 8 | **Twelve Data** | 800 credits/day | `TWELVE_DATA_API_KEY` | https://twelvedata.com/account/api-keys |
| 9 | **WeatherAPI.com** | 1M calls/month | `WEATHERAPI_KEY` | https://www.weatherapi.com/signup.aspx |
| 10 | **Groq** | Free fast inference | `GROQ_API_KEY` | https://console.groq.com/keys |
| 11 | **OpenCage** | 2,500 req/day | `OPENCAGE_API_KEY` | https://opencagedata.com/users/sign_up |
| 12 | **Congress.gov** | Unlimited | `CONGRESS_API_KEY` | https://api.congress.gov/sign-up/ |
| 13 | **US Census** | Unlimited | `CENSUS_API_KEY` | https://api.census.gov/data/key_signup.html |
| 14 | **Polygon.io** | 5 calls/min | `POLYGON_API_KEY` | https://polygon.io/dashboard/signup |

**Why these next:** HuggingFace lets you run ML models for free. Twelve Data adds forex/crypto depth. Groq gives blazing fast LLM inference. OpenCage is the best geocoding API. Congress + Census unlock deep government data.

---

## Tier 3: Register When Needed (Specialized Use Cases)

These serve specific workflows — register when you actually need them.

| # | API | Free Tier | Env Var | Register URL | Use Case |
|---|-----|-----------|---------|-------------|----------|
| 15 | **Hunter.io** | 25 searches/mo | `HUNTER_API_KEY` | https://hunter.io/users/sign_up | Email finding for leads |
| 16 | **Adzuna** | 250 req/day | `ADZUNA_APP_ID` + `ADZUNA_APP_KEY` | https://developer.adzuna.com/ | Job market data |
| 17 | **Abstract API** | 20k req/mo | `ABSTRACT_API_KEY` | https://www.abstractapi.com/ | Email validation, IP geo |
| 18 | **GeoNames** | 20k credits/day | `GEONAMES_USERNAME` | https://www.geonames.org/login | Advanced geocoding |
| 19 | **Mapbox** | 100k req/mo | `MAPBOX_TOKEN` | https://account.mapbox.com/auth/signup/ | Maps, directions, geocoding |
| 20 | **Event Registry** | 500 req/day | `EVENT_REGISTRY_KEY` | https://eventregistry.org/register | Global event monitoring |
| 21 | **WhoisXML** | 500 req/mo | `WHOISXML_API_KEY` | https://whois.whoisxmlapi.com/ | Domain/company intel |
| 22 | **OCR.space** | 25k req/mo | `OCR_SPACE_KEY` | https://ocr.space/ocrapi/freekey | Image-to-text extraction |
| 23 | **AssemblyAI** | Free tier | `ASSEMBLYAI_API_KEY` | https://www.assemblyai.com/dashboard/signup | Audio transcription |
| 24 | **ElevenLabs** | 10k chars/mo | `ELEVENLABS_API_KEY` | https://elevenlabs.io/ | Text-to-speech |
| 25 | **Wolfram Alpha** | 2k req/mo | `WOLFRAM_APP_ID` | https://developer.wolframalpha.com/ | Computational answers |
| 26 | **BuiltWith** | Limited free | `BUILTWITH_API_KEY` | https://builtwith.com/api | Tech stack detection |
| 27 | **Brandfetch** | 100 req/mo | `BRANDFETCH_API_KEY` | https://brandfetch.com/developers | Logo + brand data |
| 28 | **Together AI** | Free credits | `TOGETHER_API_KEY` | https://api.together.xyz/ | Open-source LLM inference |
| 29 | **Deepgram** | $200 credit | `DEEPGRAM_API_KEY` | https://console.deepgram.com/signup | Speech-to-text |
| 30 | **Replicate** | Free credits | `REPLICATE_API_TOKEN` | https://replicate.com/ | Run ML models |

---

## No Registration Needed (Just Works)

These APIs require zero setup — use them immediately via skills.

### Finance
| API | What it does | Rate Limit |
|-----|-------------|-----------|
| CoinGecko | Crypto prices, market cap, charts | 10-30/min |
| ExchangeRate-API | Currency conversion | Unlimited (daily updates) |
| Binance | Crypto prices, orderbook, trades | 1200/min |
| Kraken | Crypto prices, OHLC, pairs | 15/min |
| Coinbase | Exchange rates | Reasonable |
| World Bank | Economic indicators by country | Unlimited |
| OpenFIGI | Financial instrument lookup | 20/min |

### News & Media
| API | What it does | Rate Limit |
|-----|-------------|-----------|
| HackerNews Algolia | HN stories, comments, search | Generous |
| Spaceflight News | Space launches, articles | Unlimited |
| GDELT Project | Global events, tone analysis | Unlimited |
| Wikipedia Current Events | Daily news summaries | Reasonable |
| RSS2JSON | Convert any RSS to JSON | 10k/day |

### Geography & Location
| API | What it does | Rate Limit |
|-----|-------------|-----------|
| Nominatim (OSM) | Geocoding, reverse geocoding | 1/sec |
| ip-api | IP geolocation | 45/min |
| REST Countries | Country data, flags, currencies | Unlimited |
| Zippopotam.us | ZIP/postal code lookup | Unlimited |
| BigDataCloud | Reverse geocoding | 10k/day |
| CountryIS | Country by IP | Unlimited |

### Government & Public Data
| API | What it does | Rate Limit |
|-----|-------------|-----------|
| OpenFDA | Drug recalls, adverse events | 240/min |
| BLS (Bureau of Labor Stats) | Employment, CPI, wages | Unlimited |
| USASpending.gov | Federal spending data | Unlimited |
| Federal Register | Federal rules, regulations | Unlimited |
| SEC EDGAR | Company filings, full-text search | 10/sec |
| FBI Crime Data | Crime statistics by state | Unlimited |
| USGS Earthquakes | Real-time earthquake data | Unlimited |
| NWS (weather.gov) | Official US forecasts, alerts | Unlimited |
| EPA Air Quality | Air quality index data | Unlimited |
| Data.gov CKAN | 300k+ government datasets | Unlimited |
| UK Parliament | Bills, votes, members | Unlimited |
| EU Open Data | European datasets | Unlimited |
| WHO GHO | Global health statistics | Unlimited |
| World Bank | Development indicators | Unlimited |
| Open Sanctions | Sanctions/PEP lists | Basic free |

### Weather
| API | What it does | Rate Limit |
|-----|-------------|-----------|
| Open-Meteo | Forecasts, historical, marine | Unlimited |
| NWS | Official US weather | Unlimited |
| Bright Sky (DWD) | German weather data | Unlimited |
| UV Index | UV radiation forecasts | Unlimited |

### Social & Community
| API | What it does | Rate Limit |
|-----|-------------|-----------|
| Reddit JSON | Subreddit posts, comments | 60/min |
| HackerNews Firebase | Stories, comments, users | Unlimited |
| DEV.to | Developer articles, tags | Unlimited |
| Stack Exchange | Q&A across all SE sites | 300/day (no key) |
| Lobsters | Tech link aggregator | Reasonable |
| Mastodon | Public toots, timelines | Instance-dependent |
| Lemmy | Fediverse communities | Instance-dependent |
| Wikipedia | Articles, search, summaries | Unlimited |
| Wikidata SPARQL | Structured knowledge queries | Unlimited |
| Open Library | Book data, covers, search | Unlimited |
| Archive.org | Wayback Machine, media | Unlimited |
| MusicBrainz | Music metadata | 1/sec |
| Board Game Geek | Board game data | Reasonable |
| Jikan (MAL) | Anime/manga data | 60/min |
| RAWG | Video game database | 20k/mo |

### Business & Company Data
| API | What it does | Rate Limit |
|-----|-------------|-----------|
| Clearbit Logo | Company logos by domain | Unlimited |
| Open Corporates | Company registry search | Unlimited |
| Companies House UK | UK company data | Unlimited |
| SEC Company Search | US public company data | 10/sec |
| VAT/VIES | EU tax number validation | Unlimited |
| Open Food Facts | Product/barcode data | Unlimited |
| REST Countries | Country economic data | Unlimited |
| Universities API | Global university listing | Unlimited |

### AI & ML
| API | What it does | Rate Limit |
|-----|-------------|-----------|
| LibreTranslate | Open-source translation | Instance-dependent |
| Datamuse | Word associations, rhymes | Unlimited |
| LanguageTool | Grammar/spell checking | 20/min |
| MyMemory Translation | Translation memory | 10k chars/day |
| Text-Processing.com | Sentiment analysis, NER | 1k/day |
| Ollama (local) | Run LLMs locally | Unlimited |

### Developer Tools
| API | What it does | Rate Limit |
|-----|-------------|-----------|
| GitHub Public | Repos, users, search | 60/hr (no auth) |
| GitLab | Public projects, pipelines | 300/min |
| npm Registry | Package info, versions | Unlimited |
| PyPI | Python package metadata | Unlimited |
| crates.io | Rust crate info | Unlimited |
| HTTPBin | HTTP request testing | Unlimited |
| JSONPlaceholder | Fake REST API for testing | Unlimited |
| ReqRes | Fake user API for testing | Unlimited |
| Shields.io | Dynamic badges | Unlimited |
| Postman Echo | Request/response testing | Unlimited |
| OSV.dev | Vulnerability database | Unlimited |
| Wayback Machine | Archived web pages | Unlimited |
| W3C Validator | HTML/CSS validation | Unlimited |
| SSL Labs | SSL/TLS testing | Reasonable |
| CleanURI | URL shortening | Unlimited |
| QR Code APIs | Generate QR codes | Unlimited |
| DevDocs.io | Documentation search | Unlimited |

### Jobs
| API | What it does | Rate Limit |
|-----|-------------|-----------|
| Remotive | Remote jobs | Unlimited |
| Arbeitnow | European tech jobs | Unlimited |
| We Work Remotely | Remote job listings (RSS) | Unlimited |
| JustRemote | Remote jobs | Unlimited |
| Working Nomads | Digital nomad jobs | Unlimited |
| Himalayas.app | Remote company + jobs | Unlimited |
| 4DayWeek.io | 4-day work week jobs | Unlimited |
| Jobicy | Remote jobs worldwide | Unlimited |
| The Muse | Career advice + jobs | Unlimited |

---

## After Registering Keys

Add each key to your central `.env`:

```bash
# Edit the central .env
nano /Users/elizabethknopf/Documents/claudec/.env

# Add each key on its own line:
FRED_API_KEY=your_key_here
FINNHUB_API_KEY=your_key_here
# ... etc
```

The skills automatically read from environment variables — no other configuration needed.

---

## Quick Registration Checklist

### Tier 1 (do now, ~8 minutes)
- [ ] FRED — https://fred.stlouisfed.org/docs/api/api_key.html
- [ ] Finnhub — https://finnhub.io/register
- [ ] Alpha Vantage — https://www.alphavantage.co/support/#api-key
- [ ] NewsAPI — https://newsapi.org/register
- [ ] OpenWeatherMap — https://openweathermap.org/appid
- [ ] NASA — https://api.nasa.gov/

### Tier 2 (do this week, ~10 minutes)
- [ ] HuggingFace — https://huggingface.co/settings/tokens
- [ ] Twelve Data — https://twelvedata.com/account/api-keys
- [ ] WeatherAPI — https://www.weatherapi.com/signup.aspx
- [ ] Groq — https://console.groq.com/keys
- [ ] OpenCage — https://opencagedata.com/users/sign_up
- [ ] Congress.gov — https://api.congress.gov/sign-up/
- [ ] Census — https://api.census.gov/data/key_signup.html
- [ ] Polygon.io — https://polygon.io/dashboard/signup

### Tier 3 (register as needed)
- [ ] Hunter.io, Adzuna, Abstract API, GeoNames, Mapbox, Event Registry
- [ ] WhoisXML, OCR.space, AssemblyAI, ElevenLabs, Wolfram Alpha
- [ ] BuiltWith, Brandfetch, Together AI, Deepgram, Replicate

---

*Last updated: 2026-03-12 | Total APIs cataloged: 200+*
