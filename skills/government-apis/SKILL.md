---
name: government-apis
description: Query free government/public data APIs via curl. Reads catalog for endpoints and auth.
---

# Government APIs Skill

## How to use
When the user invokes `/government-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/government.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| Economic data (GDP, CPI, trade) | FRED or BLS | Official government sources |
| Federal spending/contracts | USASpending.gov | Comprehensive federal spending data |
| Census / demographic data | Census Bureau API | Official population and demographic stats |
| Regulations / federal register | Federal Register API | Full text of proposed/final rules |
| Labor statistics (employment, wages) | BLS | Bureau of Labor Statistics |
| Congressional data | Congress.gov API | Bills, members, votes |
| SEC filings | SEC EDGAR | Company filings, financial reports |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- Many government APIs are free with no key required
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**USASpending.gov (federal spending, no auth):**
```bash
# Search federal awards/contracts by keyword
curl -s -X POST "https://api.usaspending.gov/api/v2/search/spending_by_award/" -H "Content-Type: application/json" -d '{"filters":{"keywords":["artificial intelligence"]},"limit":5}' | jq '.results[:5] | .[] | {award: .Award_ID, recipient: .Recipient_Name, amount: .Award_Amount}'

# Federal spending by agency
curl -s "https://api.usaspending.gov/api/v2/agency/012/budgetary_resources/" | jq '.'

# Total spending by year
curl -s -X POST "https://api.usaspending.gov/api/v2/spending/" -H "Content-Type: application/json" -d '{"type":"agency","filters":{"fy":"2025"}}' | jq '.results[:10]'
```

**Bureau of Labor Statistics (BLS, no auth for v1):**
```bash
# Get latest unemployment data (series LNS14000000)
curl -s "https://api.bls.gov/publicAPI/v1/timeseries/data/LNS14000000" | jq '.Results.series[0].data[:6] | .[] | {year, period, value}'

# Consumer Price Index
curl -s "https://api.bls.gov/publicAPI/v1/timeseries/data/CUUR0000SA0" | jq '.Results.series[0].data[:6] | .[] | {year, period, value}'

# Average hourly earnings
curl -s "https://api.bls.gov/publicAPI/v1/timeseries/data/CES0500000003" | jq '.Results.series[0].data[:6]'

# Multiple series with v2 (requires key)
curl -s -X POST "https://api.bls.gov/publicAPI/v2/timeseries/data/" -H "Content-Type: application/json" -d '{"seriesid":["LNS14000000","CUUR0000SA0"],"registrationkey":"'$BLS_API_KEY'"}' | jq '.Results.series[] | {id: .seriesID, latest: .data[0]}'
```

**Census Bureau (demographics):**
```bash
# Population by state (latest ACS 5-year)
curl -s "https://api.census.gov/data/2022/acs/acs5?get=NAME,B01003_001E&for=state:*&key=$CENSUS_API_KEY" | jq '.'

# Specific state population by county
curl -s "https://api.census.gov/data/2022/acs/acs5?get=NAME,B01003_001E&for=county:*&in=state:04&key=$CENSUS_API_KEY" | jq '.'

# Median household income by state
curl -s "https://api.census.gov/data/2022/acs/acs5?get=NAME,B19013_001E&for=state:*&key=$CENSUS_API_KEY" | jq '.'
```

**Federal Register (regulations, no auth):**
```bash
# Search regulations
curl -s "https://www.federalregister.gov/api/v1/documents.json?conditions%5Bterm%5D=artificial+intelligence&per_page=5" | jq '.results[:5] | .[] | {title, type, publication_date, agencies: [.agencies[].name]}'

# Recent executive orders
curl -s "https://www.federalregister.gov/api/v1/documents.json?conditions%5Btype%5D=PRESDOCU&conditions%5Bpresidential_document_type%5D=executive_order&per_page=5" | jq '.results[:5] | .[] | {title, publication_date, executive_order_number}'

# Proposed rules by agency
curl -s "https://www.federalregister.gov/api/v1/documents.json?conditions%5Btype%5D=PRORULE&per_page=5" | jq '.results[:5] | .[] | {title, publication_date, agencies: [.agencies[].name]}'
```

**Congress.gov API:**
```bash
# Recent bills
curl -s "https://api.congress.gov/v3/bill?api_key=$CONGRESS_API_KEY&limit=5&sort=updateDate+desc" | jq '.bills[:5] | .[] | {number, title, type, latestAction: .latestAction.text}'

# Search bills by keyword
curl -s "https://api.congress.gov/v3/bill?api_key=$CONGRESS_API_KEY&limit=5&query=cybersecurity" | jq '.bills[:5] | .[] | {number, title}'

# Members of Congress
curl -s "https://api.congress.gov/v3/member?api_key=$CONGRESS_API_KEY&limit=10" | jq '.members[:5] | .[] | {name, state, party}'
```

**SEC EDGAR (company filings, no auth):**
```bash
# Company filings (requires User-Agent header)
curl -s "https://efts.sec.gov/LATEST/search-index?q=Tesla&dateRange=custom&startdt=2026-01-01&enddt=2026-03-12&forms=10-K,10-Q" -H "User-Agent: ClaudeCode elizabeth@example.com" | jq '.hits[:5]'

# Company facts by CIK
curl -s "https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json" -H "User-Agent: ClaudeCode elizabeth@example.com" | jq '{entityName, facts: (.facts["us-gaap"] | keys[:10])}'

# Recent filings feed
curl -s "https://efts.sec.gov/LATEST/search-index?forms=10-K&dateRange=custom&startdt=2026-03-01" -H "User-Agent: ClaudeCode elizabeth@example.com" | jq '.hits[:5]'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- The specific data values requested with units and dates
- Source agency attribution
- Context for the numbers (trends, comparisons)

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **USASpending.gov** | None | Federal contracts, grants, spending data |
| **BLS** | None (v1) / API key (v2) | Employment, wages, CPI, labor statistics |
| **Census Bureau** | API key | Population, demographics, income, housing |
| **Federal Register** | None | Regulations, executive orders, proposed rules |
| **Congress.gov** | API key | Bills, members of Congress, votes |
| **SEC EDGAR** | None (User-Agent required) | Company filings, financial reports |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| USASpending.gov | No published limit, be reasonable |
| BLS v1 | 25 requests per 10 seconds (no key) |
| BLS v2 | 500 requests/day (with key) |
| Census Bureau | 500 requests/day per key |
| Federal Register | No published limit |
| Congress.gov | 5,000 requests/hour |
| SEC EDGAR | 10 requests/second (User-Agent required) |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `BLS_API_KEY` | BLS v2 | https://data.bls.gov/registrationEngine/ |
| `CENSUS_API_KEY` | Census Bureau | https://api.census.gov/data/key_signup.html |
| `CONGRESS_API_KEY` | Congress.gov | https://api.congress.gov/sign-up/ |

## Common BLS Series IDs
- `LNS14000000` - Unemployment Rate
- `CUUR0000SA0` - CPI-U (All Urban Consumers)
- `CES0500000003` - Average Hourly Earnings
- `CES0000000001` - Total Nonfarm Payrolls
- `LNS12000000` - Employment Level
