---
name: transportation-apis
description: Query free transportation APIs via curl. Reads catalog for endpoints and auth.
---

# Transportation APIs Skill

## How to use
When the user invokes `/transportation-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/transportation.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| Live flight tracking | OpenSky Network | No auth, real-time ADS-B data |
| Airport info | AviationAPI or airportsapi | No auth, FAA data |
| Vehicle VIN decode | NHTSA | No auth, official US gov data |
| EV charging stations | Open Charge Map | Free API key, global registry |
| Public transit (Europe) | transport.rest | No auth, developer-friendly |
| Routing / directions | GraphHopper | Free tier with API key |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- If no key needed (OpenSky, AviationAPI, NHTSA, transport.rest), proceed directly
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**OpenSky Network (flight tracking, no auth):**
```bash
# Get all flights in the air right now (limited area for performance)
curl -s "https://opensky-network.org/api/states/all?lamin=33.0&lomin=-118.5&lamax=34.5&lomax=-117.0" | jq '.states[:5] | .[] | {icao24: .[0], callsign: .[1], origin_country: .[2], longitude: .[5], latitude: .[6], altitude: .[7]}'

# Get arrivals at an airport (ICAO code) in a time range
curl -s "https://opensky-network.org/api/flights/arrival?airport=KJFK&begin=1710201600&end=1710288000" | jq '.[:5] | .[] | {icao24, callsign, estDepartureAirport, estArrivalAirport}'
```

**AviationAPI (FAA data, no auth):**
```bash
# Get airport info
curl -s "https://aviationapi.com/v1/airports?apt=KJFK" | jq '.'
```

**NHTSA (vehicle data, no auth):**
```bash
# Decode a VIN
curl -s "https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/1HGBH41JXMN109186?format=json" | jq '.Results[0] | {Make, Model, ModelYear, BodyClass, FuelTypePrimary, PlantCountry}'

# Get all makes
curl -s "https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json" | jq '.Results[:10] | .[] | {Make_ID, Make_Name}'

# Get models for a make
curl -s "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/honda?format=json" | jq '.Results[:10] | .[] | {Make_Name, Model_Name}'
```

**transport.rest (European transit, no auth):**
```bash
# Search stations in Germany
curl -s "https://v6.db.transport.rest/stations?query=berlin&limit=5" | jq 'to_entries[:5] | .[] | .value | {name, id}'

# Get departures from a station
curl -s "https://v6.db.transport.rest/stops/8011160/departures?duration=30" | jq '.departures[:5] | .[] | {direction, line: .line.name, when, platform}'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- The specific value(s) requested
- Relevant context (locations, times, routes)
- Source attribution (which API provided the data)

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **OpenSky Network** | None | Real-time flight tracking, ADS-B data |
| **AviationAPI** | None | FAA airport data, charts |
| **NHTSA** | None | VIN decoding, vehicle makes/models |
| **transport.rest** | None | European public transit data |
| **Open Charge Map** | API key (query param) | EV charging station locations |
| **GraphHopper** | API key (query param) | Routing, directions, turn-by-turn |
| **airportsapi** | None | Airport info by ICAO code |
| **TransitLand** | None | Transit aggregation data |
| **BC Ferries** | None | BC Ferries sailing times |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| OpenSky Network | 10 seconds between requests (anonymous) |
| AviationAPI | No stated limit |
| NHTSA | No stated limit |
| transport.rest | 100 requests/minute |
| Open Charge Map | See docs |
| GraphHopper | 500 requests/day |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `OPEN_CHARGE_MAP_API_KEY` | Open Charge Map | https://openchargemap.org/site/develop/api |
| `GRAPHHOPPER_API_KEY` | GraphHopper | https://www.graphhopper.com/dashboard/#/apikeys |
| `TRIPADVISOR_API_KEY` | Tripadvisor | https://developer-tripadvisor.com/home/ |
