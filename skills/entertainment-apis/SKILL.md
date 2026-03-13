---
name: entertainment-apis
description: Query free entertainment APIs via curl. Reads catalog for endpoints and auth.
---

# Entertainment APIs Skill

## How to use
When the user invokes `/entertainment-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/entertainment.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| Anime search / info | Jikan (MyAnimeList) | No auth, comprehensive anime/manga data |
| Movie / TV info | TMDB | Huge movie/TV database, free API key |
| Random jokes | JokeAPI | No auth, multiple categories |
| Trivia questions | Open Trivia DB | No auth, customizable categories |
| Comic book data | Comic Vine | Large comic database |
| Game info / reviews | RAWG | Video game database, free tier |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- If no key needed (Jikan, JokeAPI, Open Trivia DB), proceed directly
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**Jikan - MyAnimeList (anime/manga, no auth):**
```bash
# Search anime by name
curl -s "https://api.jikan.moe/v4/anime?q=naruto&limit=5" | jq '.data[] | {mal_id, title, score, episodes, status}'

# Get top anime
curl -s "https://api.jikan.moe/v4/top/anime?limit=10" | jq '.data[] | {title, score, episodes}'

# Search manga
curl -s "https://api.jikan.moe/v4/manga?q=one+piece&limit=5" | jq '.data[] | {title, score, chapters}'
```

**TMDB (movies/TV, API key required):**
```bash
# Search movies
curl -s "https://api.themoviedb.org/3/search/movie?api_key=$TMDB_API_KEY&query=inception" | jq '.results[:5] | .[] | {title, release_date, vote_average, overview}'

# Get trending movies
curl -s "https://api.themoviedb.org/3/trending/movie/week?api_key=$TMDB_API_KEY" | jq '.results[:5] | .[] | {title, vote_average, release_date}'

# Search TV shows
curl -s "https://api.themoviedb.org/3/search/tv?api_key=$TMDB_API_KEY&query=breaking+bad" | jq '.results[:5] | .[] | {name, first_air_date, vote_average}'
```

**JokeAPI (jokes, no auth):**
```bash
# Random joke
curl -s "https://v2.jokeapi.dev/joke/Any" | jq '.'

# Programming joke
curl -s "https://v2.jokeapi.dev/joke/Programming" | jq '.'
```

**Open Trivia DB (trivia, no auth):**
```bash
# Get trivia questions
curl -s "https://opentdb.com/api.php?amount=5&category=11&type=multiple" | jq '.results[] | {question, correct_answer, incorrect_answers}'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- The specific value(s) requested
- Relevant context (ratings, release dates, episode counts)
- Source attribution (which API provided the data)

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **Jikan** | None | Anime/manga search, top lists, seasonal anime |
| **TMDB** | API key (query param) | Movies, TV shows, trending, search |
| **JokeAPI** | None | Random jokes, programming humor |
| **Open Trivia DB** | None | Trivia questions by category |
| **Comic Vine** | API key (query param) | Comic book characters, issues, series |
| **RAWG** | API key (query param) | Video game database, reviews, screenshots |
| **AnimeChan** | None | Anime quotes |
| **AnimeFacts** | None | Random anime facts |
| **MangaDex** | API key | Manga database and community |
| **Chuck Norris** | None | Chuck Norris jokes |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| Jikan | 60 requests/minute |
| TMDB | 40 requests/10 seconds |
| JokeAPI | 120 requests/minute |
| Open Trivia DB | 1 request/5 seconds |
| RAWG | 20,000 requests/month |
| Comic Vine | See docs |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `TMDB_API_KEY` | TMDB | https://www.themoviedb.org/settings/api |
| `RAWG_API_KEY` | RAWG | https://rawg.io/apidocs |
| `COMIC_VINE_API_KEY` | Comic Vine | https://comicvine.gamespot.com/api/ |
