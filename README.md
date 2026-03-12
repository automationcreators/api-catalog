# API Catalog

A structured catalog of 1,400+ free public APIs usable from Claude Code via lightweight skills. Each skill loads on-demand, giving Claude the ability to call real-world APIs through simple `curl` commands in Bash -- no server infrastructure required.

## Why Skills Instead of MCP?

This project already connects to 8 MCP servers (Supabase, Vercel, Gmail, Google Calendar, n8n, Perplexity, Cloudinary, and more). Each MCP server consumes context window space just by being connected, whether you use it or not.

Skills solve this differently:

| | MCP Server | Skill (this approach) |
|---|---|---|
| **Context cost** | Always loaded -- consumes tokens even when idle | Zero cost until invoked |
| **Infrastructure** | Requires running server process | None -- just a markdown file + curl |
| **Setup** | Install, configure, keep running | Drop a SKILL.md file in a directory |
| **Scalability** | Each new server adds baseline context | Add 1,000 APIs with no context increase |

The tradeoff: MCP servers provide richer tool integration (typed parameters, streaming, etc.). Skills are better for the long tail of simple REST API calls where you just need to hit an endpoint and parse JSON.

## Architecture

```
catalog.json                    # Master index of all APIs
  |
  +-- categories/
  |     +-- finance.json        # APIs grouped by domain
  |     +-- weather.json
  |     +-- news.json
  |     +-- ...
  |
  +-- skills/
        +-- finance-apis/
        |     +-- SKILL.md      # Claude reads this, learns the endpoints
        +-- weather-apis/
        |     +-- SKILL.md
        +-- ...
```

**How it works:**

1. `catalog.json` is the master index listing every API across all categories
2. Each `categories/*.json` file contains detailed API metadata (base URLs, endpoints, auth method, rate limits)
3. Each `skills/*/SKILL.md` file is a Claude-readable instruction set that teaches Claude how to call the APIs in that category
4. When you invoke a skill (e.g., `/finance-apis`), Claude reads the SKILL.md and uses `curl` in Bash to call the API

## Directory Structure

```
api-catalog/
  README.md              # This file
  BACKLOG.md             # Project roadmap and task tracking
  catalog.json           # Master index of all 60+ APIs across 10 categories
  .env                   # API keys (gitignored, never committed)
  .gitignore             # Protects secrets
  categories/            # Detailed API definitions per category
    finance.json
    weather.json
    news.json
    geo.json
    government.json
    dev-tools.json
    ai-ml.json
    social.json
    business.json
    jobs.json
  skills/                # One skill directory per category
    finance-apis/
      SKILL.md
    weather-apis/
      SKILL.md
    news-apis/
      SKILL.md
    geo-apis/
      SKILL.md
    government-apis/
      SKILL.md
    dev-tools-apis/
      SKILL.md
    ai-ml-apis/
      SKILL.md
    social-apis/
      SKILL.md
    business-apis/
      SKILL.md
    jobs-apis/
      SKILL.md
```

## Usage

Invoke a skill by its slash command name, followed by what you want to do:

```
/finance-apis "get AAPL stock price"
/weather-apis "5-day forecast for Phoenix, AZ"
/news-apis "top tech headlines today"
/geo-apis "reverse geocode 33.4484, -112.0740"
/dev-tools-apis "check if github.com is up"
/ai-ml-apis "detect language of 'Bonjour le monde'"
/social-apis "trending topics on Reddit r/technology"
/business-apis "lookup company by domain anthropic.com"
/government-apis "FDA recalls this week"
/jobs-apis "remote Python developer jobs"
```

Claude reads the relevant SKILL.md, picks the right API and endpoint, constructs the curl command, and returns the parsed result.

## How to Add New APIs

### Adding an API to an existing category

1. Open the relevant `categories/<category>.json` file
2. Add a new entry with the required fields:
   ```json
   {
     "name": "New API Name",
     "base_url": "https://api.example.com/v1",
     "auth": {
       "type": "api_key",
       "header": "X-Api-Key",
       "env_var": "EXAMPLE_API_KEY"
     },
     "rate_limit": "100 requests/day",
     "endpoints": [
       {
         "path": "/data",
         "method": "GET",
         "description": "Fetch data",
         "params": ["query", "limit"]
       }
     ],
     "docs_url": "https://docs.example.com",
     "requires_key": true
   }
   ```
3. Update `catalog.json`: increment the category's `api_count` and add the API name to its `apis` array. Increment `total_apis`.
4. Update the category's SKILL.md to include usage examples for the new API.

### Adding a new category

1. Create `categories/<new-category>.json` with the API definitions
2. Create `skills/<new-category>-apis/SKILL.md` with usage instructions
3. Add the category entry and skill entry to `catalog.json`

## Security

**API keys must never be committed to the repository.**

- All API keys are stored in `.env` at the project root (gitignored)
- SKILL.md files reference keys via `$ENV_VAR` syntax (e.g., `$ALPHA_VANTAGE_KEY`)
- The `.gitignore` excludes `.env`, `.env.*`, `*.key`, `*.pem`, and `secrets.*`
- Category JSON files use `env_var` fields to name the variable, never the actual key value
- Before committing, run a security scan to verify no keys are present

## Setup

### Free API Keys to Register

Most APIs in this catalog are completely free with no key required. For those that need a key, register at the following (all free tier):

| API | Registration URL | Env Variable | Free Tier |
|-----|-----------------|--------------|-----------|
| Alpha Vantage | https://www.alphavantage.co/support/#api-key | `ALPHA_VANTAGE_KEY` | 25 requests/day |
| Finnhub | https://finnhub.io/register | `FINNHUB_KEY` | 60 calls/minute |
| Twelve Data | https://twelvedata.com/register | `TWELVE_DATA_KEY` | 800 calls/day |
| NewsAPI | https://newsapi.org/register | `NEWS_API_KEY` | 100 requests/day |
| OpenWeatherMap | https://openweathermap.org/api | `OPENWEATHER_KEY` | 1,000 calls/day |
| Weatherapi.com | https://www.weatherapi.com/signup.aspx | `WEATHERAPI_KEY` | 1M calls/month |
| Abstract API (Geolocation) | https://www.abstractapi.com/api/ip-geolocation-api | `ABSTRACT_GEO_KEY` | 20,000 calls/month |
| Clearbit (Logo) | https://clearbit.com/logo | `CLEARBIT_KEY` | Free for logos |
| Adzuna | https://developer.adzuna.com/ | `ADZUNA_APP_ID` / `ADZUNA_APP_KEY` | 250 calls/day |
| The Muse | https://www.themuse.com/developers/api/v2 | `MUSE_API_KEY` | Free |
| Hugging Face | https://huggingface.co/settings/tokens | `HUGGINGFACE_TOKEN` | Free inference API |

### Setting Up .env

Create a `.env` file in the project root:

```bash
# Finance
ALPHA_VANTAGE_KEY=your_key_here
FINNHUB_KEY=your_key_here
TWELVE_DATA_KEY=your_key_here

# News
NEWS_API_KEY=your_key_here

# Weather
OPENWEATHER_KEY=your_key_here
WEATHERAPI_KEY=your_key_here

# Geo
ABSTRACT_GEO_KEY=your_key_here

# Business
CLEARBIT_KEY=your_key_here

# Jobs
ADZUNA_APP_ID=your_id_here
ADZUNA_APP_KEY=your_key_here
MUSE_API_KEY=your_key_here

# AI/ML
HUGGINGFACE_TOKEN=your_token_here
```

Then source it before use or let Claude read it at runtime:

```bash
source .env
```

## No-Key APIs

The majority of APIs in this catalog require no authentication at all. These include:

- **Finance:** CoinGecko, FRED, ExchangeRate-API
- **Weather:** Open-Meteo, NWS (weather.gov)
- **News:** Hacker News, Wikipedia Current Events
- **Geo:** Nominatim, GeoJS, ip-api, Zippopotam
- **Government:** All (FDA, SEC, FEC, Congress, Federal Register, USAspending, Census, NOAA, NASA, EPA)
- **Dev Tools:** All (GitHub public API, HTTPBin, Public APIs list, ip-api, Supported Browsers, DevDocs, cdnjs, shields.io, License API)
- **AI/ML:** LibreTranslate, Datamuse, Perspective API
- **Social:** Reddit JSON, Hacker News, Wikipedia, Wikidata, Open Library, MusicBrainz, Jikan (MyAnimeList)
- **Business:** Open Food Facts, REST Countries, Universities API
- **Jobs:** Arbeitnow, Remotive

These work immediately with no setup.
