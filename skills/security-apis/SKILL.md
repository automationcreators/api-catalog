---
name: security-apis
description: Query free security APIs via curl. Reads catalog for endpoints and auth.
---

# Security APIs Skill

## How to use
When the user invokes `/security-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/security.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| URL/domain reputation | URLhaus or URLScan.io | No auth (URLhaus) or free tier |
| Breach / password check | HaveIBeenPwned | Pwned Passwords API is free, no auth |
| Malware samples | MalwareBazaar | No auth for queries |
| Email reputation | EmailRep | No auth for basic lookups |
| Vulnerability lookup | National Vulnerability Database | No auth, official NIST data |
| Phishing detection | PhishStats | No auth, phishing database |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- If no key needed (URLhaus, MalwareBazaar, EmailRep, NVD, PhishStats), proceed directly
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**URLhaus (malicious URL database, no auth):**
```bash
# Check a URL
curl -s -X POST "https://urlhaus-api.abuse.ch/v1/url/" -d "url=http://example.com" | jq '{query_status, urlhaus_reference, threat}'

# Get recent URLs
curl -s -X POST "https://urlhaus-api.abuse.ch/v1/urls/recent/limit/5/" | jq '.urls[:3] | .[] | {url, url_status, threat, date_added}'

# Search by host
curl -s -X POST "https://urlhaus-api.abuse.ch/v1/host/" -d "host=example.com" | jq '{urlhaus_reference, url_count, urls: [.urls[:3][] | {url, url_status}]}'
```

**HaveIBeenPwned - Pwned Passwords (no auth for passwords):**
```bash
# Check if a password hash prefix has been breached (k-anonymity)
# First 5 chars of SHA1 hash of "password" = 5BAA6
curl -s "https://api.pwnedpasswords.com/range/5BAA6" | head -5
```

**MalwareBazaar (malware samples, no auth):**
```bash
# Get recent malware samples
curl -s -X POST "https://mb-api.abuse.ch/api/v1/" -d "query=get_recent&selector=100" | jq '.data[:3] | .[] | {sha256_hash, file_type, signature, reporter}'

# Search by file hash
curl -s -X POST "https://mb-api.abuse.ch/api/v1/" -d "query=get_info&hash=<SHA256_HASH>" | jq '.'
```

**EmailRep (email reputation, no auth):**
```bash
# Check email reputation
curl -s "https://emailrep.io/test@example.com" | jq '{email, reputation, suspicious, details: {blacklisted, credentials_leaked, data_breach}}'
```

**National Vulnerability Database (CVE data, no auth):**
```bash
# Search vulnerabilities by keyword
curl -s "https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=log4j&resultsPerPage=3" | jq '.vulnerabilities[:3] | .[] | {id: .cve.id, description: .cve.descriptions[0].value}'

# Get specific CVE
curl -s "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2021-44228" | jq '.vulnerabilities[0].cve | {id, descriptions: [.descriptions[0].value]}'
```

**Mozilla HTTP Observatory (website security scan, no auth):**
```bash
# Scan a website
curl -s -X POST "https://http-observatory.security.mozilla.org/api/v1/analyze?host=github.com" | jq '{grade, score, tests_passed, tests_failed}'

# Get scan results
curl -s "https://http-observatory.security.mozilla.org/api/v1/getScanResults?scan=12345" | jq '.'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- The specific value(s) requested
- Relevant context (severity, dates, threat type)
- Source attribution (which API provided the data)
- Security advisory if relevant

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **URLhaus** | None | Malicious URL database queries |
| **HaveIBeenPwned** | None (passwords) / API key (breaches) | Password breach checking |
| **MalwareBazaar** | None | Malware sample search |
| **EmailRep** | None | Email reputation checking |
| **National Vulnerability Database** | None | CVE and vulnerability lookup |
| **PhishStats** | None | Phishing URL database |
| **Mozilla HTTP Observatory** | None | Website security scanning |
| **Shodan** | API key (query param) | Internet-connected device search |
| **VirusTotal** | API key (query param) | File/URL malware analysis |
| **AbuseIPDB** | API key (query param) | IP reputation checking |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| URLhaus | No stated limit |
| HaveIBeenPwned (passwords) | No limit |
| MalwareBazaar | No stated limit |
| EmailRep | No stated limit |
| NVD | 5 requests/30 seconds |
| Mozilla Observatory | No stated limit |
| Shodan | 1 request/second |
| VirusTotal | 4 requests/minute |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `HAVEIBEENPWNED_API_KEY` | HaveIBeenPwned | https://haveibeenpwned.com/API/Key |
| `SHODAN_API_KEY` | Shodan | https://developer.shodan.io/ |
| `VIRUSTOTAL_API_KEY` | VirusTotal | https://www.virustotal.com/gui/join-us |
| `ABUSEIPDB_API_KEY` | AbuseIPDB | https://docs.abuseipdb.com/ |
| `URLSCANIO_API_KEY` | URLScan.io | https://urlscan.io/about-api/ |
| `SECURITYTRAILS_API_KEY` | SecurityTrails | https://securitytrails.com/corp/apidocs |
