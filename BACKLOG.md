# API Catalog - Backlog

## NOW (This Session) - 2026-03-12

- [x] Create project directory structure (`categories/`, `skills/` with 10 subdirectories)
- [x] Write `README.md` with architecture, setup, usage, and security docs
- [x] Write `catalog.json` master index with all 10 categories and 60 APIs
- [x] Write `BACKLOG.md` (this file)
- [ ] Create `categories/finance.json` with 6 API definitions
- [ ] Create `categories/weather.json` with 6 API definitions
- [ ] Create `categories/news.json` with 6 API definitions
- [ ] Create `categories/geo.json` with 6 API definitions
- [ ] Create `categories/government.json` with 10 API definitions
- [ ] Create `categories/dev-tools.json` with 6 API definitions
- [ ] Create `categories/ai-ml.json` with 6 API definitions
- [ ] Create `categories/social.json` with 6 API definitions
- [ ] Create `categories/business.json` with 6 API definitions
- [ ] Create `categories/jobs.json` with 6 API definitions
- [ ] Write `skills/finance-apis/SKILL.md`
- [ ] Write `skills/weather-apis/SKILL.md`
- [ ] Write `skills/news-apis/SKILL.md`
- [ ] Write `skills/geo-apis/SKILL.md`
- [ ] Write `skills/government-apis/SKILL.md`
- [ ] Write `skills/dev-tools-apis/SKILL.md`
- [ ] Write `skills/ai-ml-apis/SKILL.md`
- [ ] Write `skills/social-apis/SKILL.md`
- [ ] Write `skills/business-apis/SKILL.md`
- [ ] Write `skills/jobs-apis/SKILL.md`
- [ ] Create `.env.example` with placeholder keys
- [ ] Create `.gitignore` for the project
- [ ] Test at least 1 skill end-to-end (e.g., `/finance-apis "get AAPL price"`)
- [ ] Initial git commit

## NEXT (Near-Term)

### Validation and Testing
- [ ] Test every no-auth API endpoint (should work immediately)
- [ ] Test every key-required API with real keys in `.env`
- [ ] Verify rate limit documentation matches actual limits
- [ ] Add error handling guidance to each SKILL.md (what to do on 429, 401, 500)

### Expand Coverage
- [ ] Add `categories/entertainment.json` (TMDB, OMDB, TVMaze, Jikan, BoardGameGeek, RAWG)
- [ ] Add `skills/entertainment-apis/SKILL.md`
- [ ] Add `categories/science.json` (arXiv, CrossRef, CORE, Semantic Scholar, PubChem, GBIF)
- [ ] Add `skills/science-apis/SKILL.md`
- [ ] Add `categories/transportation.json` (OpenSky, BART, MTA, CTA, Citybikes)
- [ ] Add `skills/transportation-apis/SKILL.md`
- [ ] Add `categories/health.json` (OpenFDA drugs, WHO, Disease.sh, NLM)
- [ ] Add `skills/health-apis/SKILL.md`
- [ ] Update `catalog.json` with new categories

### Quality of Life
- [ ] Write a `CLAUDE.md` for the project so Claude Code loads context automatically
- [ ] Add `jq` parsing examples to each SKILL.md for cleaner output
- [ ] Create a "quick reference" card with one-liner examples for all 10 categories
- [ ] Add pagination guidance for APIs that return large datasets

### Integration with Personal-OS
- [ ] Register api-catalog in `project-registry.json`
- [ ] Add API health check to `deploy-monitor` agent
- [ ] Create a `trend-scanner` integration that uses news-apis skill
- [ ] Wire `content-creator` agent to pull real data via finance/news skills

## LATER (Backlog)

### Wrapper Tools
- [ ] Build `api-test.sh` script that validates all endpoints in a category JSON
- [ ] Build `api-status.sh` that checks which APIs are currently responding
- [ ] Create `add-api.sh` helper that scaffolds a new API entry interactively
- [ ] Build rate-limit tracker that warns before hitting daily/monthly limits

### Advanced Skills
- [ ] Composite skills that chain multiple APIs (e.g., "get weather + news for a city")
- [ ] Caching layer -- save recent API responses to avoid redundant calls
- [ ] Response format templates (table, summary, raw JSON) per skill
- [ ] Auto-retry logic with exponential backoff for SKILL.md instructions

### Scale to 1,400+
- [ ] Audit public-apis GitHub repo for full API list
- [ ] Categorize and add APIs in batches of 50
- [ ] Add sub-categories within large categories (e.g., government: federal, state, local)
- [ ] Build catalog search skill (`/api-search "find APIs about astronomy"`)
- [ ] Generate SKILL.md files programmatically from category JSON definitions

### Documentation and Content
- [ ] Write blog post: "Why I chose Skills over MCP for 1,400 APIs"
- [ ] Create YouTube script: building an API catalog for AI coding assistants
- [ ] Add to Social-Content-Generator as source material
- [ ] Publish catalog as open-source template for others

### Monitoring and Observability
- [ ] Log API call history (which APIs called, when, success/failure)
- [ ] Dashboard showing API usage across categories
- [ ] Alert when an API changes its schema or goes offline
- [ ] Monthly report: most-used APIs, error rates, new APIs added
