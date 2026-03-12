---
name: business-apis
description: Query free business/lead APIs via curl. Reads catalog for endpoints and auth.
---

# Business APIs Skill

## How to use
When the user invokes `/business-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/business.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| Find email for a person/domain | Hunter.io | Email finder and verifier |
| Verify if an email is valid | Hunter.io or Abstract API | Deliverability check |
| Company info/lookup | Clearbit Logo + Open Corporates | Basic company data |
| Domain/website info | WhoisXML or BuiltWith | Tech stack, registration |
| Business name/entity search | Open Corporates | Official corporate registrations |
| Logo for a company | Clearbit Logo API | No auth, instant logos |
| Enrich a lead | Hunter.io + Clearbit | Combined data |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- If no key needed (Clearbit Logo), proceed directly
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**Hunter.io (email finding/verification):**
```bash
# Find email addresses for a domain
curl -s "https://api.hunter.io/v2/domain-search?domain=stripe.com&api_key=$HUNTER_API_KEY" | jq '{domain, emails: [.data.emails[:5][] | {email: .value, type, confidence}], total: .data.total}'

# Find specific person's email
curl -s "https://api.hunter.io/v2/email-finder?domain=stripe.com&first_name=Patrick&last_name=Collison&api_key=$HUNTER_API_KEY" | jq '.data | {email, confidence, sources}'

# Verify an email address
curl -s "https://api.hunter.io/v2/email-verifier?email=test@stripe.com&api_key=$HUNTER_API_KEY" | jq '.data | {email, result, score, status}'

# Check account usage
curl -s "https://api.hunter.io/v2/account?api_key=$HUNTER_API_KEY" | jq '.data | {email, plan_name, calls: .calls}'
```

**Clearbit Logo API (no auth):**
```bash
# Get company logo (returns image URL, 128px default)
echo "https://logo.clearbit.com/stripe.com"
echo "https://logo.clearbit.com/google.com"

# Different sizes
echo "https://logo.clearbit.com/stripe.com?size=256"
```

**Open Corporates (company search, no auth for basic):**
```bash
# Search companies by name
curl -s "https://api.opencorporates.com/v0.4/companies/search?q=Tesla" | jq '.results.companies[:5] | .[] | .company | {name, jurisdiction_code, company_number, incorporation_date, current_status}'

# Get specific company details
curl -s "https://api.opencorporates.com/v0.4/companies/us_de/0001318605" | jq '.results.company | {name, incorporation_date, current_status, registered_address}'

# Search officers
curl -s "https://api.opencorporates.com/v0.4/officers/search?q=Elon+Musk" | jq '.results.officers[:3] | .[] | .officer | {name, position, company: .company.name}'
```

**Abstract API (email validation):**
```bash
# Validate email
curl -s "https://emailvalidation.abstractapi.com/v1/?api_key=$ABSTRACT_EMAIL_KEY&email=test@google.com" | jq '{email, deliverability, is_valid_format, is_disposable_email, is_free_email}'
```

**WhoisXML API (domain info):**
```bash
# WHOIS lookup
curl -s "https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=$WHOISXML_API_KEY&domainName=stripe.com&outputFormat=JSON" | jq '.WhoisRecord | {domainName, registrarName, createdDate, expiresDate, registrant: .registrant}'

# DNS lookup
curl -s "https://www.whoisxmlapi.com/whoisserver/DNSService?apiKey=$WHOISXML_API_KEY&domainName=stripe.com&type=A&outputFormat=JSON" | jq '.'
```

**BuiltWith (technology lookup, limited free):**
```bash
# Check what tech a site uses (free tier)
curl -s "https://api.builtwith.com/free1/api.json?KEY=$BUILTWITH_API_KEY&LOOKUP=stripe.com" | jq '.groups[] | {name, categories: [.categories[].name]}'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- The specific business data requested
- Confidence scores where available (email finding)
- Source attribution

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **Hunter.io** | API key (query param) | Email finding, domain search, email verification |
| **Clearbit Logo** | None | Company logos by domain |
| **Open Corporates** | None (basic) | Company registration data, officer search |
| **Abstract API** | API key (query param) | Email validation and deliverability |
| **WhoisXML** | API key (query param) | Domain WHOIS, DNS lookup |
| **BuiltWith** | API key (query param) | Website technology stack detection |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| Hunter.io | 25 searches/month, 50 verifications/month |
| Clearbit Logo | Unlimited (just image URLs) |
| Open Corporates | 200 requests/day (no key) |
| Abstract Email | 100 requests/month |
| WhoisXML | 500 credits on signup |
| BuiltWith | 1 free lookup/domain |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `HUNTER_API_KEY` | Hunter.io | https://hunter.io/api_keys |
| `ABSTRACT_EMAIL_KEY` | Abstract API | https://app.abstractapi.com/api/email-validation |
| `WHOISXML_API_KEY` | WhoisXML | https://whoisxmlapi.com/ |
| `BUILTWITH_API_KEY` | BuiltWith | https://api.builtwith.com/ |
