---
name: dev-tools-apis
description: Query free developer tool APIs via curl. Reads catalog for endpoints and auth.
---

# Dev Tools APIs Skill

## How to use
When the user invokes `/dev-tools-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/dev-tools.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| GitHub repo info/stars | GitHub API | Official, comprehensive |
| GitHub trending repos | GitHub Search API | Sort by stars/recent |
| npm package info | npm Registry | No auth, full metadata |
| npm download stats | npm API | Download counts over time |
| Package vulnerabilities | OSV.dev | Google's vulnerability DB |
| Crates.io (Rust packages) | Crates.io API | No auth needed |
| PyPI (Python packages) | PyPI JSON API | No auth needed |
| Public APIs list | Public APIs project | Discover new APIs |
| URL shortening | CleanURI | No auth, simple |
| Code execution | Judge0 | Run code in 60+ languages |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- Many dev tool APIs work without auth (npm, PyPI, Crates.io)
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**GitHub API (public endpoints, optional auth):**
```bash
# Repo info
curl -s "https://api.github.com/repos/anthropics/claude-code" -H "Accept: application/vnd.github.v3+json" | jq '{name, full_name, description, stargazers_count, forks_count, language, updated_at, open_issues_count}'

# Search repos by topic/keyword
curl -s "https://api.github.com/search/repositories?q=AI+agents&sort=stars&per_page=5" -H "Accept: application/vnd.github.v3+json" | jq '.items[:5] | .[] | {full_name, description, stars: .stargazers_count, language, url: .html_url}'

# Trending repos (created recently, most stars)
curl -s "https://api.github.com/search/repositories?q=created:>2026-03-01&sort=stars&per_page=10" -H "Accept: application/vnd.github.v3+json" | jq '.items[:10] | .[] | {full_name, description, stars: .stargazers_count, language}'

# User/org info
curl -s "https://api.github.com/users/anthropics" -H "Accept: application/vnd.github.v3+json" | jq '{login, name, bio, public_repos, followers}'

# Repo releases
curl -s "https://api.github.com/repos/denoland/deno/releases?per_page=3" -H "Accept: application/vnd.github.v3+json" | jq '.[:3] | .[] | {tag_name, name, published_at, body: .body[:200]}'

# Repo languages
curl -s "https://api.github.com/repos/anthropics/claude-code/languages" -H "Accept: application/vnd.github.v3+json" | jq '.'

# With auth (higher rate limits)
curl -s "https://api.github.com/repos/owner/repo" -H "Authorization: Bearer $GITHUB_TOKEN" -H "Accept: application/vnd.github.v3+json" | jq '.'
```

**npm Registry (package info, no auth):**
```bash
# Package info
curl -s "https://registry.npmjs.org/express/latest" | jq '{name, version, description, homepage, license, dependencies: (.dependencies | keys)}'

# All versions
curl -s "https://registry.npmjs.org/react" | jq '{name, description, latest: .["dist-tags"].latest, versions: (.versions | keys | .[-5:])}'

# Search packages
curl -s "https://registry.npmjs.org/-/v1/search?text=state+management+react&size=5" | jq '.objects[:5] | .[] | .package | {name, version, description, links: .links.npm}'
```

**npm Download Stats (no auth):**
```bash
# Weekly downloads for a package
curl -s "https://api.npmjs.org/downloads/point/last-week/express" | jq '{package, downloads, start, end}'

# Daily downloads over a range
curl -s "https://api.npmjs.org/downloads/range/2026-03-01:2026-03-12/react" | jq '{package, downloads: [.downloads[] | {day, downloads}]}'

# Compare packages
curl -s "https://api.npmjs.org/downloads/point/last-month/express,fastify,koa" | jq '.'
```

**PyPI (Python packages, no auth):**
```bash
# Package info
curl -s "https://pypi.org/pypi/requests/json" | jq '{name: .info.name, version: .info.version, summary: .info.summary, author: .info.author, license: .info.license, home_page: .info.home_page}'

# Specific version
curl -s "https://pypi.org/pypi/flask/3.0.0/json" | jq '{name: .info.name, version: .info.version, requires_python: .info.requires_python}'

# Check latest version
curl -s "https://pypi.org/pypi/django/json" | jq '{name: .info.name, version: .info.version, summary: .info.summary}'
```

**Crates.io (Rust packages, no auth):**
```bash
# Crate info
curl -s "https://crates.io/api/v1/crates/serde" -H "User-Agent: ClaudeCode/1.0" | jq '.crate | {name, description, downloads, max_version, repository}'

# Search crates
curl -s "https://crates.io/api/v1/crates?q=async+runtime&per_page=5" -H "User-Agent: ClaudeCode/1.0" | jq '.crates[:5] | .[] | {name, description, downloads, max_version}'

# Most downloaded crates
curl -s "https://crates.io/api/v1/crates?sort=downloads&per_page=10" -H "User-Agent: ClaudeCode/1.0" | jq '.crates[:10] | .[] | {name, downloads, max_version}'
```

**OSV.dev (vulnerability database, no auth):**
```bash
# Query vulnerabilities for a package
curl -s -X POST "https://api.osv.dev/v1/query" -H "Content-Type: application/json" -d '{"package":{"name":"lodash","ecosystem":"npm"}}' | jq '.vulns[:3] | .[] | {id, summary, modified}'

# Get specific vulnerability
curl -s "https://api.osv.dev/v1/vulns/GHSA-xxxx-xxxx-xxxx" | jq '{id, summary, details: .details[:300], affected: [.affected[].package.name]}'

# Batch query
curl -s -X POST "https://api.osv.dev/v1/querybatch" -H "Content-Type: application/json" -d '{"queries":[{"package":{"name":"express","ecosystem":"npm"}},{"package":{"name":"django","ecosystem":"PyPI"}}]}' | jq '.results[] | {vulns: (.vulns // [] | length)}'
```

**CleanURI (URL shortener, no auth):**
```bash
# Shorten a URL
curl -s "https://cleanuri.com/api/v1/shorten" -d "url=https://github.com/anthropics/claude-code" | jq '.result_url'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- Package/repo name and version
- Key metrics (stars, downloads, dependencies)
- Relevant links
- Vulnerability count if queried

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **GitHub API** | Optional token (header) | Repos, users, search, releases |
| **npm Registry** | None | Package info, search, versions |
| **npm Downloads** | None | Download statistics |
| **PyPI** | None | Python package info |
| **Crates.io** | None (User-Agent required) | Rust crate info and search |
| **OSV.dev** | None | Vulnerability database queries |
| **CleanURI** | None | URL shortening |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| GitHub (no auth) | 60 requests/hour |
| GitHub (with token) | 5,000 requests/hour |
| npm Registry | No published limit |
| npm Downloads | No published limit |
| PyPI | No published limit |
| Crates.io | 1 request/second (User-Agent required) |
| OSV.dev | No published limit |
| CleanURI | No published limit |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `GITHUB_TOKEN` | GitHub (optional, higher limits) | https://github.com/settings/tokens |

Most dev tool APIs require no authentication for read access.
