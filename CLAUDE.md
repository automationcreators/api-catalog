# API Catalog Project

## Overview
Structured catalog of 60+ free public APIs usable from Claude Code via lightweight skills — zero MCP bloat.

## Architecture
- `catalog.json` — Master index of all APIs
- `categories/*.json` — Per-category API details (endpoints, auth, rate limits)
- `skills/*/SKILL.md` — Category skills that read catalog + call APIs via curl
- Skills are also installed at `~/.claude/skills/` for slash command access

## Key Rules
1. **NEVER put actual API keys in any file** — use `$ENV_VAR_NAME` references only
2. **All keys live in central `.env`** at `/Users/elizabethknopf/Documents/claudec/.env`
3. **Security scan before every commit** — check for key patterns (sk-proj-, apify_api_, AIza, etc.)
4. **No new MCP servers** — this project exists specifically to avoid MCP context bloat

## Adding a New API
1. Add entry to appropriate `categories/{category}.json`
2. Update `catalog.json` master index (api count, api list)
3. If new category, create new category JSON + SKILL.md

## Slash Commands
- `/finance-apis "query"` — Stock, crypto, forex, economic data
- `/news-apis "query"` — Headlines, article search
- `/geo-apis "query"` — Geocoding, IP geolocation
- `/government-apis "query"` — Federal data, spending, stats
- `/business-apis "query"` — Email finder, company lookup
- `/weather-apis "query"` — Forecasts, conditions
- `/social-apis "query"` — Reddit, HN, dev communities
- `/jobs-apis "query"` — Job listings, remote work
- `/ai-ml-apis "query"` — Inference, translation
- `/dev-tools-apis "query"` — GitHub, npm, packages
