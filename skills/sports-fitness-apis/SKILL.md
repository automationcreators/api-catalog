---
name: sports-fitness-apis
description: Query free sports and fitness APIs via curl. Reads catalog for endpoints and auth.
---

# Sports & Fitness APIs Skill

## How to use
When the user invokes `/sports-fitness-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/sports-fitness.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| NBA stats / players | balldontlie | No auth, comprehensive NBA data |
| F1 racing data | Ergast F1 | No auth, historical F1 data since 1950 |
| Football/soccer data | Football-Data | Free tier with API key, matches and standings |
| NHL hockey stats | NHL Records and Stats | No auth, historical NHL data |
| MLB baseball stats | MLB Records and Stats | No auth, historical MLB data |
| Exercise / workout data | Wger | Exercises, muscles, equipment info |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- If no key needed (balldontlie, Ergast F1, NHL, MLB, City Bikes), proceed directly
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**balldontlie (NBA stats, no auth):**
```bash
# Search NBA players
curl -s "https://www.balldontlie.io/api/v1/players?search=lebron" | jq '.data[] | {first_name, last_name, position, team: .team.full_name}'

# Get NBA teams
curl -s "https://www.balldontlie.io/api/v1/teams" | jq '.data[] | {full_name, abbreviation, conference, division}'
```

**Ergast F1 (Formula 1 data, no auth):**
```bash
# Current season driver standings
curl -s "https://ergast.com/api/f1/current/driverStandings.json" | jq '.MRData.StandingsTable.StandingsLists[0].DriverStandings[:5] | .[] | {position, Driver: .Driver.familyName, Constructors: .Constructors[0].name, points}'

# Last race results
curl -s "https://ergast.com/api/f1/current/last/results.json" | jq '.MRData.RaceTable.Races[0] | {raceName, date, Results: [.Results[:5][] | {position, Driver: .Driver.familyName, Constructor: .Constructor.name}]}'

# List all circuits
curl -s "https://ergast.com/api/f1/circuits.json?limit=10" | jq '.MRData.CircuitTable.Circuits[] | {circuitName, Location: .Location.country}'
```

**TheSportsDB (multi-sport, free test key "1"):**
```bash
# Search team by name
curl -s "https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Arsenal" | jq '.teams[0] | {strTeam, strLeague, strCountry, strStadium, strDescriptionEN}'

# Get league table
curl -s "https://www.thesportsdb.com/api/v1/json/1/lookuptable.php?l=4328&s=2025-2026" | jq '.table[:5] | .[] | {name, played, win, draw, loss, total}'
```

**City Bikes (bike sharing, no auth):**
```bash
# List bike networks worldwide
curl -s "https://api.citybik.es/v2/networks?fields=id,name,location" | jq '.networks[:10] | .[] | {name, location: .location.city}'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- The specific value(s) requested
- Relevant context (standings, scores, stats)
- Source attribution (which API provided the data)

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **balldontlie** | None | NBA players, teams, games, stats |
| **Ergast F1** | None | F1 races, drivers, constructors since 1950 |
| **TheSportsDB** | API key (free test: "1") | Multi-sport team/league search |
| **Football-Data** | API key (query param) | Soccer matches, standings, competitions |
| **NHL Records and Stats** | None | NHL historical data |
| **MLB Records and Stats** | None | MLB historical data |
| **City Bikes** | None | Bike sharing networks worldwide |
| **Wger** | API key (query param) | Exercise database, muscles, equipment |
| **API-FOOTBALL** | API key (query param) | Football leagues and cups |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| balldontlie | 60 requests/minute |
| Ergast F1 | 4 requests/second |
| TheSportsDB | Free test key unlimited |
| Football-Data | 10 calls/minute |
| NHL/MLB | No stated limit |
| City Bikes | No limit |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `FOOTBALL_DATA_API_KEY` | Football-Data | https://www.football-data.org/client/register |
| `API_FOOTBALL_API_KEY` | API-FOOTBALL | https://www.api-football.com/ |
| `THESPORTSDB_API_KEY` | TheSportsDB | https://www.thesportsdb.com/api.php |
| `WGER_API_KEY` | Wger | https://wger.de/en/user/api-key |
