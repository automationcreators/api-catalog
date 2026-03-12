---
name: jobs-apis
description: Query free jobs/salary APIs via curl. Reads catalog for endpoints and auth.
---

# Jobs APIs Skill

## How to use
When the user invokes `/jobs-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/jobs.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| Remote job listings | Remotive | Curated remote jobs, no auth |
| Tech job search | Adzuna or JSearch | Broad coverage |
| Job search by keyword/location | Adzuna or JSearch | Filterable search |
| Remote-only developer jobs | Remotive | Remote-first focus |
| Job market trends | Adzuna | Salary histograms, trends |
| Startup jobs | Arbeitnow | Startup-focused listings |
| Freelance/contract work | Remotive or Arbeitnow | Filter by job type |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- If no key needed (Remotive, Arbeitnow), proceed directly
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**Remotive (remote jobs, no auth):**
```bash
# All remote jobs
curl -s "https://remotive.com/api/remote-jobs?limit=5" | jq '.jobs[:5] | .[] | {title: .title, company: .company_name, category: .category, salary, url}'

# Remote jobs by category (software-dev, design, customer-support, marketing, sales, product, data, devops, etc.)
curl -s "https://remotive.com/api/remote-jobs?category=software-dev&limit=5" | jq '.jobs[:5] | .[] | {title, company: .company_name, salary, tags}'

# Search by keyword
curl -s "https://remotive.com/api/remote-jobs?search=python&limit=5" | jq '.jobs[:5] | .[] | {title, company: .company_name, salary, url}'

# Data science remote jobs
curl -s "https://remotive.com/api/remote-jobs?category=data&limit=5" | jq '.jobs[:5] | .[] | {title, company: .company_name, salary}'

# DevOps remote jobs
curl -s "https://remotive.com/api/remote-jobs?category=devops&limit=5" | jq '.jobs[:5] | .[] | {title, company: .company_name, salary, tags}'
```

**Adzuna (job search with salary data):**
```bash
# Search jobs (US)
curl -s "https://api.adzuna.com/v1/api/jobs/us/search/1?app_id=$ADZUNA_APP_ID&app_key=$ADZUNA_API_KEY&what=software+engineer&where=Phoenix+AZ&results_per_page=5" | jq '.results[:5] | .[] | {title, company: .company.display_name, location: .location.display_name, salary_min, salary_max}'

# Remote jobs
curl -s "https://api.adzuna.com/v1/api/jobs/us/search/1?app_id=$ADZUNA_APP_ID&app_key=$ADZUNA_API_KEY&what=remote+developer&results_per_page=5" | jq '.results[:5] | .[] | {title, company: .company.display_name, salary_min, salary_max}'

# Salary histogram for a job title
curl -s "https://api.adzuna.com/v1/api/jobs/us/histogram?app_id=$ADZUNA_APP_ID&app_key=$ADZUNA_API_KEY&what=data+scientist" | jq '.'

# Top companies hiring
curl -s "https://api.adzuna.com/v1/api/jobs/us/top_companies?app_id=$ADZUNA_APP_ID&app_key=$ADZUNA_API_KEY&what=machine+learning" | jq '.leaderboard[:10]'

# Job count by category
curl -s "https://api.adzuna.com/v1/api/jobs/us/categories?app_id=$ADZUNA_APP_ID&app_key=$ADZUNA_API_KEY" | jq '.results[:10] | .[] | {tag, label}'
```

**JSearch (via RapidAPI):**
```bash
# Search jobs
curl -s "https://jsearch.p.rapidapi.com/search?query=Python+developer+in+Austin&page=1&num_pages=1" -H "X-RapidAPI-Key: $RAPIDAPI_KEY" -H "X-RapidAPI-Host: jsearch.p.rapidapi.com" | jq '.data[:5] | .[] | {title: .job_title, company: .employer_name, location: .job_city, type: .job_employment_type, posted: .job_posted_at_datetime_utc}'

# Job details
curl -s "https://jsearch.p.rapidapi.com/job-details?job_id=JOB_ID" -H "X-RapidAPI-Key: $RAPIDAPI_KEY" -H "X-RapidAPI-Host: jsearch.p.rapidapi.com" | jq '.data[0] | {title: .job_title, description: .job_description[:300], salary_min: .job_min_salary, salary_max: .job_max_salary}'

# Salary estimate
curl -s "https://jsearch.p.rapidapi.com/estimated-salary?job_title=Software+Engineer&location=San+Francisco" -H "X-RapidAPI-Key: $RAPIDAPI_KEY" -H "X-RapidAPI-Host: jsearch.p.rapidapi.com" | jq '.data[:3]'
```

**Arbeitnow (startup/tech jobs, no auth):**
```bash
# Latest jobs
curl -s "https://www.arbeitnow.com/api/job-board-api" | jq '.data[:5] | .[] | {title, company_name, location, remote, tags, url}'

# The API returns all jobs - filter client-side for remote
curl -s "https://www.arbeitnow.com/api/job-board-api" | jq '[.data[] | select(.remote == true)][:5] | .[] | {title, company_name, tags}'

# Filter by tags
curl -s "https://www.arbeitnow.com/api/job-board-api" | jq '[.data[] | select(.tags | index("python"))][:5] | .[] | {title, company_name, location}'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- Job title and company
- Location or remote status
- Salary range (if available)
- Link to apply
- Key tags/requirements

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **Remotive** | None | Curated remote jobs, category filtering |
| **Adzuna** | App ID + API key (query params) | Job search with salary data, market trends |
| **JSearch** | RapidAPI key (header) | Aggregated job search, salary estimates |
| **Arbeitnow** | None | Startup/tech jobs, simple API |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| Remotive | No published limit (be reasonable) |
| Adzuna | 250 calls/day on free tier |
| JSearch | 200 requests/month (RapidAPI free) |
| Arbeitnow | No published limit |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `ADZUNA_APP_ID` | Adzuna | https://developer.adzuna.com/ |
| `ADZUNA_API_KEY` | Adzuna | https://developer.adzuna.com/ |
| `RAPIDAPI_KEY` | JSearch (RapidAPI) | https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch |

## Remotive Job Categories
- `software-dev` - Software Development
- `data` - Data Science / Analytics
- `devops` - DevOps / Sysadmin
- `design` - Design
- `product` - Product Management
- `customer-support` - Customer Support
- `marketing` - Marketing
- `sales` - Sales
- `hr` - Human Resources
- `finance` - Finance / Legal
- `writing` - Writing / Content
- `qa` - Quality Assurance
