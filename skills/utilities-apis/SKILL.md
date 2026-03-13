---
name: utilities-apis
description: Query free utility APIs via curl. Reads catalog for endpoints and auth.
---

# Utilities APIs Skill

## How to use
When the user invokes `/utilities-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/utilities.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| Public holidays by country | Nager.Date | No auth, 90+ countries |
| UK bank holidays | UK Bank Holidays | No auth, official gov.uk data |
| QR code generation | goqr.me | No auth, instant QR codes |
| URL shortening | is.gd or v.gd | No auth, simple URL shortener |
| Email validation | Mailboxlayer | Free tier with API key |
| Hebrew/liturgical calendar | Hebrew Calendar | No auth, Shabbat times |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- If no key needed (Nager.Date, UK Bank Holidays, Hebrew Calendar), proceed directly
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**Nager.Date (public holidays, no auth):**
```bash
# Get public holidays for a country and year
curl -s "https://date.nager.at/api/v3/PublicHolidays/2026/US" | jq '.[:5] | .[] | {date, localName, name, countryCode}'

# Get next public holidays worldwide
curl -s "https://date.nager.at/api/v3/NextPublicHolidays/US" | jq '.[:5] | .[] | {date, name}'

# Check if today is a public holiday
curl -s "https://date.nager.at/api/v3/IsTodayPublicHoliday/US"

# List available countries
curl -s "https://date.nager.at/api/v3/AvailableCountries" | jq '.[:10] | .[] | {countryCode, name}'
```

**UK Bank Holidays (official, no auth):**
```bash
# Get UK bank holidays
curl -s "https://www.gov.uk/bank-holidays.json" | jq '."england-and-wales".events[:5] | .[] | {title, date}'
```

**Hebrew Calendar (no auth):**
```bash
# Get Shabbat times for a location
curl -s "https://www.hebcal.com/shabbat?cfg=json&geonameid=5128581&M=on" | jq '{title, location, items: [.items[:5][] | {title, date}]}'

# Get holidays for a year
curl -s "https://www.hebcal.com/hebcal?v=1&cfg=json&maj=on&min=on&year=2026" | jq '.items[:10] | .[] | {title, date, category}'
```

**QR Code Generation (goqr.me, no auth):**
```bash
# Generate QR code (returns image URL)
echo "https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://example.com"

# Generate QR code with custom size
echo "https://api.qrserver.com/v1/create-qr-code/?size=400x400&data=Hello+World"
```

**Nameday Calendar (no auth):**
```bash
# Get today's nameday
curl -s "https://nameday.abalin.net/api/V1/today?country=us" | jq '.'

# Search for a name
curl -s "https://nameday.abalin.net/api/V1/getdate?name=john&country=us" | jq '.'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- The specific value(s) requested
- Relevant context (dates, countries, formats)
- Source attribution (which API provided the data)

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **Nager.Date** | None | Public holidays for 90+ countries |
| **UK Bank Holidays** | None | Official UK bank holiday dates |
| **Hebrew Calendar** | None | Jewish holidays, Shabbat times |
| **Nameday Calendar** | None | Nameday lookup by country |
| **Church Calendar** | None | Catholic liturgical calendar |
| **Calendarific** | API key (query param) | Worldwide holidays |
| **goqr.me** | None | QR code generation |
| **is.gd** | None | URL shortening |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| Nager.Date | No stated limit |
| UK Bank Holidays | No limit |
| Hebrew Calendar | No stated limit |
| Nameday Calendar | No stated limit |
| Calendarific | 1000 requests/month |
| goqr.me | No stated limit |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `CALENDARIFIC_API_KEY` | Calendarific | https://calendarific.com/signup |
| `PUBLIC_HOLIDAYS_API_KEY` | Abstract Holidays | https://www.abstractapi.com/holidays-api |
| `HOLIDAYS_API_KEY` | Holiday API | https://holidayapi.com/ |
