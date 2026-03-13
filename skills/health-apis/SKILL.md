---
name: health-apis
description: Query free health and medical APIs via curl. Reads catalog for endpoints and auth.
---

# Health APIs Skill

## How to use
When the user invokes `/health-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/health.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| Nutrition / food data | FoodData Central | USDA official nutrient database |
| COVID-19 stats | Open Disease | No auth, global COVID/influenza data |
| US healthcare providers | NPPES | No auth, NPI registry lookup |
| Disease data worldwide | Open Disease (disease.sh) | No auth, comprehensive disease stats |
| Healthcare marketplace info | Healthcare.gov | No auth, US health insurance info |
| NHS Scotland data | Open Data NHS Scotland | No auth, public health statistics |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- If no key needed (Open Disease, NPPES, Healthcare.gov), proceed directly
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**Open Disease - disease.sh (disease data, no auth):**
```bash
# Global COVID-19 stats
curl -s "https://disease.sh/v3/covid-19/all" | jq '{cases, deaths, recovered, active, tests, todayCases, todayDeaths}'

# COVID stats by country
curl -s "https://disease.sh/v3/covid-19/countries/USA" | jq '{country, cases, deaths, recovered, active, todayCases, casesPerOneMillion}'

# Influenza data
curl -s "https://disease.sh/v3/influenza/NREVSS/clinical_labs" | jq '.[:3]'
```

**NPPES (US healthcare provider lookup, no auth):**
```bash
# Search provider by name
curl -s "https://npiregistry.cms.hhs.gov/api/?version=2.1&first_name=john&last_name=smith&limit=5" | jq '.results[:3] | .[] | {number, basic: {first_name: .basic.first_name, last_name: .basic.last_name, credential: .basic.credential}}'

# Search by NPI number
curl -s "https://npiregistry.cms.hhs.gov/api/?version=2.1&number=1234567890" | jq '.results[0] | {number, basic}'

# Search by specialty/taxonomy
curl -s "https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=cardiology&limit=5" | jq '.results[:3] | .[] | {number, basic: {first_name: .basic.first_name, last_name: .basic.last_name}}'
```

**FoodData Central (USDA nutrition, API key required):**
```bash
# Search foods
curl -s "https://api.nal.usda.gov/fdc/v1/foods/search?query=chicken+breast&pageSize=3&api_key=$FOODDATA_CENTRAL_API_KEY" | jq '.foods[:3] | .[] | {description, brandName, foodNutrients: [.foodNutrients[:5][] | {nutrientName, value, unitName}]}'

# Get food by FDC ID
curl -s "https://api.nal.usda.gov/fdc/v1/food/534358?api_key=$FOODDATA_CENTRAL_API_KEY" | jq '{description, foodNutrients: [.foodNutrients[:10][] | {nutrient: .nutrient.name, amount, unitName: .nutrient.unitName}]}'
```

**Healthcare.gov (US health insurance, no auth):**
```bash
# Get articles/content
curl -s "https://www.healthcare.gov/api/articles.json" | jq '.articles[:5] | .[] | {title, url, date}'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- The specific value(s) requested
- Relevant context (dates, locations, statistics)
- Source attribution (which API provided the data)
- Disclaimer: This data is for informational purposes only, not medical advice

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **Open Disease (disease.sh)** | None | COVID-19 and influenza statistics globally |
| **NPPES** | None | US healthcare provider NPI lookup |
| **Healthcare.gov** | None | US health insurance marketplace info |
| **FoodData Central** | API key (query param) | USDA nutrition database |
| **Open Data NHS Scotland** | None | Scottish public health data |
| **Nutritionix** | API key (query param) | Nutrition tracking database |
| **Infermedica** | API key (query param) | Symptom checker and triage |
| **CMS.gov** | API key (query param) | Medicare provider data |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| Open Disease | No limit |
| NPPES | 200 requests/day |
| Healthcare.gov | No limit |
| FoodData Central | 1000 requests/hour |
| Nutritionix | See docs |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `FOODDATA_CENTRAL_API_KEY` | FoodData Central | https://fdc.nal.usda.gov/api-key-signup.html |
| `NUTRITIONIX_API_KEY` | Nutritionix | https://developer.nutritionix.com/ |
| `INFERMEDICA_API_KEY` | Infermedica | https://developer.infermedica.com/ |
| `CMSGOV_API_KEY` | CMS.gov | https://data.cms.gov/ |
