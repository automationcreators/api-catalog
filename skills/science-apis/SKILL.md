---
name: science-apis
description: Query free science APIs via curl. Reads catalog for endpoints and auth.
---

# Science APIs Skill

## How to use
When the user invokes `/science-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/science.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| NASA images / APOD | NASA | No auth required (DEMO_KEY), official NASA data |
| Space launches | SpaceX or Launch Library 2 | No auth, launch data and schedules |
| Research papers | arXiv | No auth, physics/math/CS preprints |
| ISS location / astronauts | Open Notify | No auth, real-time ISS data |
| Earthquake data | USGS Earthquake | No auth, real-time seismic data |
| Math calculations | Newton | No auth, symbolic math via URL |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- NASA has free DEMO_KEY; most science APIs need no auth
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**NASA (space data, DEMO_KEY or free key):**
```bash
# Astronomy Picture of the Day
curl -s "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY" | jq '{title, date, explanation, url}'

# Mars Rover photos
curl -s "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&page=1&api_key=DEMO_KEY" | jq '.photos[:3] | .[] | {id, earth_date, camera: .camera.full_name, img_src}'

# Near Earth Objects (asteroids)
curl -s "https://api.nasa.gov/neo/rest/v1/feed?start_date=2026-03-12&end_date=2026-03-12&api_key=DEMO_KEY" | jq '.element_count'
```

**SpaceX (launch data, no auth):**
```bash
# Latest launch
curl -s "https://api.spacexdata.com/v4/launches/latest" | jq '{name, date_utc, success, details}'

# Upcoming launches
curl -s "https://api.spacexdata.com/v4/launches/upcoming" | jq '.[:5] | .[] | {name, date_utc}'

# All rockets
curl -s "https://api.spacexdata.com/v4/rockets" | jq '.[] | {name, type, active, cost_per_launch, success_rate_pct}'
```

**Open Notify (ISS data, no auth):**
```bash
# Current ISS position
curl -s "http://api.open-notify.org/iss-now.json" | jq '.'

# People currently in space
curl -s "http://api.open-notify.org/astros.json" | jq '{number, people: [.people[] | {name, craft}]}'
```

**USGS Earthquake (seismic data, no auth):**
```bash
# Significant earthquakes in the last day
curl -s "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_day.geojson" | jq '.features[] | {place: .properties.place, mag: .properties.mag, time: .properties.time}'

# All 4.5+ earthquakes in the last week
curl -s "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson" | jq '.features[:5] | .[] | {place: .properties.place, mag: .properties.mag, type: .properties.type}'
```

**Newton (math calculator, no auth):**
```bash
# Simplify an expression
curl -s "https://newton.vercel.app/api/v2/simplify/2^2+2(2)" | jq '.'

# Derive a function
curl -s "https://newton.vercel.app/api/v2/derive/x^3+2x" | jq '.'

# Integrate
curl -s "https://newton.vercel.app/api/v2/integrate/x^2" | jq '.'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- The specific value(s) requested
- Relevant context (dates, magnitudes, coordinates)
- Source attribution (which API provided the data)

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **NASA** | API key (DEMO_KEY works) | APOD, Mars rovers, asteroids, Earth imagery |
| **SpaceX** | None | Launch data, rockets, capsules, Starlink |
| **Open Notify** | None | ISS position, astronauts in space |
| **USGS Earthquake** | None | Real-time earthquake data worldwide |
| **Newton** | None | Symbolic math calculations |
| **arXiv** | None | Research paper search (physics, math, CS) |
| **USGS Water Services** | None | River/lake water quality and levels |
| **Sunrise and Sunset** | None | Sunrise/sunset times by coordinates |
| **Nobel Prize** | None | Nobel Prize laureate data |
| **World Bank** | None | Global development indicators |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| NASA (DEMO_KEY) | 30 requests/hour, 50/day |
| NASA (registered) | 1000 requests/hour |
| SpaceX | No stated limit |
| Open Notify | No limit |
| USGS Earthquake | No limit |
| Newton | No limit |
| arXiv | 3 second wait between requests |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `NASA_API_KEY` | NASA | https://api.nasa.gov/ (free, instant) |
| `CORE_API_KEY` | CORE | https://core.ac.uk/services#api |
