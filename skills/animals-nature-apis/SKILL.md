---
name: animals-nature-apis
description: Query free animal and nature APIs via curl. Reads catalog for endpoints and auth.
---

# Animals & Nature APIs Skill

## How to use
When the user invokes `/animals-nature-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/animals-nature.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| Dog images by breed | Dogs (dog.ceo) | No auth, random/breed-specific images |
| Cat facts | Cat Facts / MeowFacts | No auth, random cat facts |
| Random dog pictures | RandomDog | No auth, simple random image |
| Bird observations | eBird | Rich birding data by region |
| Air quality data | IQAir or OpenAQ | Real-time air quality readings |
| Carbon footprint | Carbon Interface or UK Carbon Intensity | CO2 emissions calculations |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- If no key needed (Dogs, Cat Facts, RandomDog, RandomFox, RandomDuck), proceed directly
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**Dogs - dog.ceo (dog images, no auth):**
```bash
# Random dog image
curl -s "https://dog.ceo/api/breeds/image/random" | jq '.'

# Random image by breed
curl -s "https://dog.ceo/api/breed/husky/images/random" | jq '.'

# List all breeds
curl -s "https://dog.ceo/api/breeds/list/all" | jq '.message | keys[:20]'
```

**Cat Facts (no auth):**
```bash
# Random cat fact
curl -s "https://catfact.ninja/fact" | jq '.'

# Multiple cat facts
curl -s "https://catfact.ninja/facts?limit=5" | jq '.data[] | .fact'
```

**RandomFox (fox images, no auth):**
```bash
# Random fox image
curl -s "https://randomfox.ca/floof/" | jq '.'
```

**RandomDuck (duck images, no auth):**
```bash
# Random duck image
curl -s "https://random-d.uk/api/random" | jq '.'
```

**UK Carbon Intensity (CO2, no auth):**
```bash
# Current carbon intensity for GB
curl -s "https://api.carbonintensity.org.uk/intensity" | jq '.data[0] | {from, to, intensity: .intensity}'

# Carbon intensity by date
curl -s "https://api.carbonintensity.org.uk/intensity/date/2026-03-12" | jq '.data[:5] | .[] | {from, intensity: .intensity}'
```

**FishWatch (fish species, no auth):**
```bash
# Get fish species info
curl -s "https://www.fishwatch.gov/api/species" | jq '.[:5] | .[] | {"Species Name", "Scientific Name", "Availability", "Calories"}'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- The specific value(s) requested
- Relevant context (breed, species, location)
- Source attribution (which API provided the data)

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **Dogs (dog.ceo)** | None | Dog images by breed, breed lists |
| **Cat Facts** | None | Random cat facts |
| **RandomDog** | None | Random dog pictures |
| **RandomFox** | None | Random fox pictures |
| **RandomDuck** | None | Random duck pictures |
| **FishWatch** | None | Fish species information |
| **UK Carbon Intensity** | None | GB carbon intensity data |
| **eBird** | API key (query param) | Bird observations by region |
| **IUCN** | API key (query param) | Endangered species data |
| **IQAir** | API key (query param) | Air quality data |
| **OpenAQ** | API key (query param) | Open air quality data |
| **xeno-canto** | None | Bird sound recordings |
| **Zoo Animals** | None | Zoo animal facts and pictures |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| Dogs (dog.ceo) | No limit |
| Cat Facts | No limit |
| RandomDog | No limit |
| RandomFox | No limit |
| UK Carbon Intensity | No limit |
| FishWatch | No limit |
| eBird | See docs |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `EBIRD_API_KEY` | eBird | https://ebird.org/api/keygen |
| `IUCN_API_KEY` | IUCN | http://apiv3.iucnredlist.org/api/v3/token |
| `IQAIR_API_KEY` | IQAir | https://www.iqair.com/air-pollution-data-api |
| `OPENAQ_API_KEY` | OpenAQ | https://docs.openaq.org/ |
| `CARBON_INTERFACE_API_KEY` | Carbon Interface | https://docs.carboninterface.com/ |
