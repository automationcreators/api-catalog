---
name: geo-apis
description: Query free geo/location APIs via curl. Reads catalog for endpoints and auth.
---

# Geo APIs Skill

## How to use
When the user invokes `/geo-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/geo.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| Address to lat/lng (geocode) | Nominatim (OSM) | No auth, reliable |
| Lat/lng to address (reverse geocode) | Nominatim (OSM) | No auth, global coverage |
| IP address geolocation | ip-api.com | No auth, detailed response |
| My current IP location | ipinfo.io or ip-api.com | Quick, no auth |
| Country/city info | REST Countries | No auth, comprehensive |
| Zip code lookup | Zippopotam.us | No auth, simple |
| Distance between coordinates | Calculate from geocoded results | Use Nominatim first |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- Most geo APIs here are free with no auth required
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**Nominatim / OpenStreetMap (geocoding, no auth):**
```bash
# Forward geocode: address to coordinates
curl -s "https://nominatim.openstreetmap.org/search?q=1600+Pennsylvania+Ave+Washington+DC&format=json&limit=1" -H "User-Agent: ClaudeCode/1.0" | jq '.[0] | {lat, lon, display_name}'

# Reverse geocode: coordinates to address
curl -s "https://nominatim.openstreetmap.org/reverse?lat=33.4484&lon=-112.0740&format=json" -H "User-Agent: ClaudeCode/1.0" | jq '{display_name, address: {city: .address.city, state: .address.state, country: .address.country}}'

# Search for places
curl -s "https://nominatim.openstreetmap.org/search?q=coffee+shops+near+Phoenix+AZ&format=json&limit=5" -H "User-Agent: ClaudeCode/1.0" | jq '.[] | {name: .display_name, lat, lon}'
```

**ip-api.com (IP geolocation, no auth):**
```bash
# Geolocate a specific IP
curl -s "http://ip-api.com/json/8.8.8.8" | jq '{ip: .query, city, region: .regionName, country, lat, lon, isp, org}'

# Geolocate your current IP
curl -s "http://ip-api.com/json/" | jq '{ip: .query, city, region: .regionName, country, lat, lon, timezone}'

# Batch lookup (POST, up to 100 IPs)
curl -s -X POST "http://ip-api.com/batch" -H "Content-Type: application/json" -d '["8.8.8.8","1.1.1.1"]' | jq '.[] | {query, city, country}'
```

**ipinfo.io (IP info, optional auth):**
```bash
# Basic IP info (no auth, 50k/month)
curl -s "https://ipinfo.io/8.8.8.8/json" | jq '{ip, city, region, country, loc, org}'

# Your own IP
curl -s "https://ipinfo.io/json" | jq '{ip, city, region, country, loc, org}'
```

**REST Countries (country data, no auth):**
```bash
# Search country by name
curl -s "https://restcountries.com/v3.1/name/japan" | jq '.[0] | {name: .name.common, capital: .capital[0], population, region, currencies: (.currencies | keys), languages: (.languages | values)}'

# All countries in a region
curl -s "https://restcountries.com/v3.1/region/europe" | jq '.[] | {name: .name.common, capital: .capital[0], population}' | head -40

# Country by code
curl -s "https://restcountries.com/v3.1/alpha/US" | jq '.[0] | {name: .name.common, capital: .capital[0], population, area, timezones}'

# Search by currency
curl -s "https://restcountries.com/v3.1/currency/eur" | jq '.[] | .name.common'
```

**Zippopotam.us (zip code lookup, no auth):**
```bash
# US zip code lookup
curl -s "https://api.zippopotam.us/us/85001" | jq '{zip: .["post code"], country, state: .places[0].state, city: .places[0]["place name"], lat: .places[0].latitude, lng: .places[0].longitude}'

# Other countries (use country code)
curl -s "https://api.zippopotam.us/gb/EC1A" | jq '.'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- Location coordinates or address as appropriate
- Relevant geographic context (country, region, timezone)
- Source attribution

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **Nominatim (OSM)** | None (User-Agent required) | Geocoding, reverse geocoding, place search |
| **ip-api.com** | None | IP geolocation with ISP/org info |
| **ipinfo.io** | Optional token | IP info, clean responses |
| **REST Countries** | None | Country data, population, currencies, languages |
| **Zippopotam.us** | None | Zip/postal code to city/state/coordinates |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| Nominatim | 1 request/second (must set User-Agent) |
| ip-api.com | 45 requests/minute |
| ipinfo.io | 50,000 requests/month (no token) |
| REST Countries | No published limit |
| Zippopotam.us | No published limit |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `IPINFO_TOKEN` | ipinfo.io (optional) | https://ipinfo.io/signup |

Most geo APIs in this catalog require no authentication.
