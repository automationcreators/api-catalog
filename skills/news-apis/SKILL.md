---
name: news-apis
description: Query free news APIs via curl. Reads catalog for endpoints and auth.
---

# News APIs Skill

## How to use
When the user invokes `/news-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/news.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| Top headlines by country/category | NewsAPI | Category filtering, country support |
| Search articles by keyword | NewsAPI or GNews | Full-text search |
| Tech/startup news | Hacker News (Algolia) | Tech-focused, no auth needed |
| Current events summary | GNews | Clean, simple responses |
| Historical article search | NewsAPI or Currents API | Date range filtering |
| Trending tech topics | Hacker News (Algolia) | Real-time tech community pulse |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- If no key needed (Hacker News), proceed directly
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**NewsAPI (headlines, article search):**
```bash
# Top headlines for US
curl -s "https://newsapi.org/v2/top-headlines?country=us&apiKey=$NEWSAPI_KEY" | jq '.articles[:5] | .[] | {title, source: .source.name, url}'

# Top headlines by category (business, technology, science, health, sports, entertainment)
curl -s "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=$NEWSAPI_KEY" | jq '.articles[:5] | .[] | {title, source: .source.name}'

# Search articles by keyword
curl -s "https://newsapi.org/v2/everything?q=artificial+intelligence&sortBy=publishedAt&pageSize=5&apiKey=$NEWSAPI_KEY" | jq '.articles[:5] | .[] | {title, source: .source.name, publishedAt, url}'

# Search with date range
curl -s "https://newsapi.org/v2/everything?q=openai&from=2026-03-01&to=2026-03-12&sortBy=relevancy&apiKey=$NEWSAPI_KEY" | jq '.totalResults, .articles[:3] | .[] | {title, publishedAt}'
```

**GNews (global news):**
```bash
# Top headlines
curl -s "https://gnews.io/api/v4/top-headlines?lang=en&token=$GNEWS_API_KEY" | jq '.articles[:5] | .[] | {title, description, source: .source.name}'

# Search articles
curl -s "https://gnews.io/api/v4/search?q=climate+change&lang=en&token=$GNEWS_API_KEY" | jq '.articles[:5] | .[] | {title, source: .source.name, publishedAt}'

# Headlines by topic (breaking-news, world, nation, business, technology, entertainment, sports, science, health)
curl -s "https://gnews.io/api/v4/top-headlines?topic=technology&lang=en&token=$GNEWS_API_KEY" | jq '.articles[:5] | .[] | {title, description}'
```

**Hacker News via Algolia (no auth):**
```bash
# Search HN stories
curl -s "https://hn.algolia.com/api/v1/search?query=rust+programming&tags=story" | jq '.hits[:5] | .[] | {title, points, url, num_comments}'

# Front page stories (sorted by points)
curl -s "https://hn.algolia.com/api/v1/search?tags=front_page" | jq '.hits[:10] | .[] | {title, points, num_comments, url}'

# Recent stories by date
curl -s "https://hn.algolia.com/api/v1/search_by_date?tags=story&query=AI" | jq '.hits[:5] | .[] | {title, points, created_at, url}'

# Search comments
curl -s "https://hn.algolia.com/api/v1/search?query=claude+code&tags=comment" | jq '.hits[:5] | .[] | {comment_text: .comment_text[:200], points, story_title}'
```

**Currents API (global news):**
```bash
# Latest news
curl -s "https://api.currentsapi.services/v1/latest-news?apiKey=$CURRENTS_API_KEY&language=en" | jq '.news[:5] | .[] | {title, description, published}'

# Search news
curl -s "https://api.currentsapi.services/v1/search?apiKey=$CURRENTS_API_KEY&keywords=bitcoin&language=en" | jq '.news[:5] | .[] | {title, published, url}'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- Article title and source
- Publication date
- Brief description or summary
- URL for full article

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **NewsAPI** | API key (query param) | Headlines by country/category, article search |
| **GNews** | API key (query param) | Global news, topic-based headlines |
| **Hacker News (Algolia)** | None | Tech news, startup news, developer discussions |
| **Currents API** | API key (query param) | Global latest news, keyword search |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| NewsAPI | 100 requests/day (dev plan), no commercial use |
| GNews | 100 requests/day |
| Hacker News (Algolia) | No published limit, be reasonable (10k+/day) |
| Currents API | 600 requests/day |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `NEWSAPI_KEY` | NewsAPI | https://newsapi.org/register |
| `GNEWS_API_KEY` | GNews | https://gnews.io/register |
| `CURRENTS_API_KEY` | Currents API | https://currentsapi.services/en/register |
