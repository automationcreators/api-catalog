# API-Powered Project Ideas

> 110+ project ideas leveraging 190 free APIs + AI (Claude, local LLMs, HuggingFace) to build differentiated SaaS tools, utilities, and dashboards. Every idea is buildable by a solo dev in 1-4 weeks with Claude Code + Supabase + Vercel + n8n.

**Last updated:** 2026-03-12

---

## Original Wrapper Tools (from backlog)

These 6 ideas were the original starting point. They remain strong candidates.

1. **Local Business Intel Dashboard** — Enter a zip code, get a complete business intelligence report: nearby competitors (Google Places), demographic breakdown (Census), local employment data (BLS), and neighborhood walkability (Nominatim). AI summarizes opportunities and risks.
   - APIs: Google Places, Census Bureau, BLS, Nominatim

2. **Content Trend Engine** — Aggregates trending topics across NewsAPI, Reddit, HackerNews, YouTube, and RSS feeds. AI identifies cross-platform trend convergence and predicts which topics will peak in 24-48 hours.
   - APIs: NewsAPI, Reddit JSON, HN Algolia, RSS2JSON

3. **Job Market Analyzer** — Combines BLS labor statistics, FRED economic indicators, and live job board data to show which roles are growing, which are shrinking, and where salary leverage exists. AI generates career pivot recommendations.
   - APIs: BLS, FRED, Adzuna, RemoteOK

4. **Government Grant Finder** — Searches USASpending, Grants.gov, and SAM.gov simultaneously. AI matches your business profile to eligible grants and generates application summaries.
   - APIs: USASpending, Data.gov, SAM.gov

5. **Lead Enrichment Pipeline** — Takes a list of email addresses or domains, enriches them with company data, social profiles, and validation scores. AI scores lead quality and writes personalized outreach drafts.
   - APIs: Hunter.io, Clearbit Logo, Apollo.io

6. **AI-Powered Market Research** — Pulls economic indicators from FRED, development data from World Bank, and country profiles from REST Countries. AI generates investor-ready market briefs comparing countries or regions.
   - APIs: FRED, World Bank, REST Countries

---

## 110 AI-Differentiated Project Ideas

---

### SaaS Tools (subscription revenue potential)

**7. PriceScope — Competitive Price Intelligence**
- **What it does:** Monitors product/service pricing across industries by combining financial data with company intelligence. Alerts users when competitors change pricing or market conditions shift.
- **APIs used:** Alpha Vantage, SEC EDGAR, Crunchbase, FRED
- **AI angle:** Claude analyzes 10-K filings and economic indicators to predict pricing pressure before competitors announce changes. Generates strategic pricing recommendations.
- **Revenue model:** $29/mo for 5 competitors, $99/mo for 25 competitors with daily alerts.
- **Competition:** Prisync, Competera charge $200+/mo. AI prediction layer and free API data undercut them massively.

**8. DueDiligenceBot — Instant Company Research Reports**
- **What it does:** Enter a company name, get a comprehensive due diligence report in 60 seconds: financials, legal filings, leadership, news sentiment, tech stack.
- **APIs used:** SEC EDGAR, Open Corporates, Companies House UK, BuiltWith, NewsAPI, Hunter.io
- **AI angle:** Claude synthesizes data from 6+ sources into a structured report with risk flags, opportunity signals, and a confidence score. Manual research takes 4-8 hours.
- **Revenue model:** Free for 3 reports/month, $49/mo unlimited, $199/mo with PDF export and team sharing.
- **Competition:** Crunchbase Pro ($49/mo), PitchBook ($thousands). This combines more sources at lower cost with AI synthesis.

**9. ChurnGuard — Customer Health Scoring**
- **What it does:** Connects to a user's Supabase database and enriches customer records with company data, news sentiment, and economic indicators to predict churn.
- **APIs used:** Clearbit Logo, Hunter.io, NewsAPI, FRED, Open Corporates
- **AI angle:** Claude builds a churn risk model by correlating external signals (company layoffs in news, declining industry metrics) with usage patterns.
- **Revenue model:** $79/mo per 1,000 customers tracked.
- **Competition:** ChurnZero, Gainsight charge $500+/mo. This is the budget alternative with AI-powered external signal detection.

**10. InvoiceIQ — Smart Invoice Processing**
- **What it does:** Upload invoices (PDF/image), get them OCR'd, categorized, matched to vendors, and analyzed for spending patterns.
- **APIs used:** OCR.space, ExchangeRate-API, Clearbit Logo, Abstract Email Validation
- **AI angle:** Claude categorizes expenses, detects duplicate charges, identifies cost-saving opportunities, and generates spending reports with natural language insights.
- **Revenue model:** Free for 20 invoices/month, $19/mo for 200, $49/mo unlimited.
- **Competition:** Dext, Hubdoc charge $30+/mo but lack AI-powered spending insights and pattern detection.

**11. ContractLens — AI Contract Analyzer**
- **What it does:** Upload contracts, get instant AI analysis: key dates, obligations, unusual clauses, risk flags, and plain-English summaries.
- **APIs used:** OCR.space, LanguageTool, HuggingFace Inference (NER), Datamuse
- **AI angle:** Claude reads entire contracts and flags non-standard clauses, missing protections, and unfavorable terms compared to industry norms.
- **Revenue model:** $39/mo for freelancers (10 contracts), $149/mo for businesses (unlimited).
- **Competition:** Ironclad, Juro focus on enterprise. No good AI contract review tool exists under $100/mo for freelancers and small businesses.

**12. BrandPulse — Real-Time Brand Monitoring**
- **What it does:** Track any brand across Reddit, HackerNews, news outlets, and Product Hunt. Get AI-generated sentiment summaries and alert on reputation shifts.
- **APIs used:** Reddit JSON, HN Algolia, NewsAPI, GNews, Product Hunt, DEV.to
- **AI angle:** Claude performs nuanced sentiment analysis, distinguishes between complaints vs. feature requests vs. praise, and drafts suggested response templates.
- **Revenue model:** Free for 1 brand, $29/mo for 5 brands, $99/mo for 20 brands with Slack alerts.
- **Competition:** Mention, Brand24 charge $50+/mo. This uses free APIs instead of paid social listening feeds.

**13. MeetingBrief — Pre-Meeting Intelligence**
- **What it does:** Before a sales call or investor meeting, paste a company name and get a one-page brief: recent news, financial health, leadership changes, tech stack, and talking points.
- **APIs used:** NewsAPI, SEC EDGAR, BuiltWith, Crunchbase, Hunter.io, Open Corporates, Clearbit Logo
- **AI angle:** Claude generates custom talking points based on the company's recent activity, identifies mutual connections and interests, and suggests conversation openers.
- **Revenue model:** $19/mo for 20 briefs, $49/mo unlimited.
- **Competition:** Owler (free but shallow), LinkedIn Sales Navigator ($79/mo). This combines more data sources with AI-generated talking points.

---

### Content & Media Tools

**14. NewsDigest AI — Personalized News Briefings**
- **What it does:** Users set topics and preferences. Each morning, AI curates and summarizes the top 10 stories relevant to them from 5+ news sources.
- **APIs used:** NewsAPI, GNews, TheNewsAPI, Currents, Reddit JSON, HN Algolia
- **AI angle:** Claude deduplicates stories across sources, writes concise summaries at the user's preferred reading level, and identifies how stories connect to their interests.
- **Revenue model:** Free for daily email, $9/mo for real-time alerts and custom feeds.
- **Competition:** Feedly ($6/mo), Google News (free). AI summarization and cross-source deduplication is the differentiator.

**15. ThreadCraft — AI Twitter/X Thread Generator**
- **What it does:** Paste a URL, upload a PDF, or describe a topic. Get a ready-to-post thread with hooks, data points, and a CTA. Pulls real statistics to back up claims.
- **APIs used:** FRED, BLS, World Bank, Wikipedia API, Datamuse
- **AI angle:** Claude researches the topic, finds real statistics from government data, writes in the user's voice (learned from their past threads), and optimizes hook patterns.
- **Revenue model:** Free for 5 threads/month, $19/mo unlimited.
- **Competition:** Typefully, Hypefury focus on scheduling. This focuses on AI-generated content backed by real data.

**16. PodScript — Podcast Show Notes Generator**
- **What it does:** Upload a podcast audio file, get a full transcript, AI-generated show notes, chapter markers, key quotes, and social media clips.
- **APIs used:** Deepgram or AssemblyAI (transcription), Datamuse, LanguageTool
- **AI angle:** Claude generates structured show notes with timestamps, identifies the most quotable moments, and writes platform-specific promotional copy.
- **Revenue model:** $29/mo for 4 episodes, $79/mo for 20 episodes.
- **Competition:** Descript ($24/mo for editing), Podium ($19/mo). This focuses specifically on automated show notes and marketing assets.

**17. ViralScope — Content Virality Predictor**
- **What it does:** Analyze any piece of content before publishing and get a virality score based on historical patterns from Reddit, HN, and Product Hunt launches.
- **APIs used:** Reddit JSON, HN Algolia, Product Hunt, DEV.to, StackExchange
- **AI angle:** Claude compares your headline, topic, and format against thousands of viral posts to score engagement potential and suggest improvements.
- **Revenue model:** $15/mo for bloggers, $49/mo for teams.
- **Competition:** CoSchedule Headline Analyzer (free, basic). This uses real viral post data, not just word scoring.

**18. WikiBrief — Instant Research Summaries**
- **What it does:** Enter any topic and get a structured research brief pulling from Wikipedia, academic papers, news, and community discussions.
- **APIs used:** Wikipedia API, Wikidata SPARQL, Open Library, StackExchange, DEV.to, Archive.org
- **AI angle:** Claude synthesizes information across sources, identifies contradictions, provides confidence levels, and presents information in a structured brief format.
- **Revenue model:** Free for 10/month, $12/mo unlimited, $39/mo with export and citation formatting.
- **Competition:** Perplexity (similar concept). Differentiate with deeper Wikipedia/Wikidata integration and academic source emphasis.

**19. TechBlogForge — AI Technical Blog Writer**
- **What it does:** Describe a technical topic. AI researches it across dev communities, pulls code examples from GitHub, and drafts a complete blog post with real data points.
- **APIs used:** GitHub API, StackExchange, DEV.to, npm Registry, PyPI, HN Algolia
- **AI angle:** Claude writes posts that reference actual package download counts, GitHub star trends, and community sentiment, making content data-driven rather than generic.
- **Revenue model:** $29/mo for dev advocates and technical marketers.
- **Competition:** Jasper, Copy.ai write generic content. This produces technically accurate, data-backed posts.

**20. SubtitleGenius — AI Video Subtitle Generator**
- **What it does:** Upload video, get transcription with speaker diarization, auto-translation to 10+ languages, and SRT/VTT export.
- **APIs used:** Deepgram, DeepL, LibreTranslate, MyMemory Translation
- **AI angle:** Claude improves raw transcription accuracy, identifies speakers, adds punctuation, and handles technical jargon that standard ASR misses.
- **Revenue model:** Free for 30 min/month, $15/mo for 5 hours, $49/mo for 20 hours.
- **Competition:** Rev ($1.50/min), Otter.ai ($17/mo). Multi-language support with free translation APIs keeps costs near zero.

---

### Business Intelligence & Analytics

**21. MarketPulse — Real-Time Economic Dashboard**
- **What it does:** Live dashboard combining FRED economic indicators, BLS employment data, stock indices, and news sentiment into a single "state of the economy" view.
- **APIs used:** FRED, BLS, Alpha Vantage, CoinGecko, NewsAPI, World Bank
- **AI angle:** Claude generates a daily "Economic Weather Report" — a plain-English summary of what the numbers mean for specific industries.
- **Revenue model:** Free dashboard, $29/mo for AI industry-specific reports.
- **Competition:** TradingView (charts only), FRED website (raw data). AI narrative layer and cross-source correlation is the moat.

**22. SupplyChainRadar — Disruption Early Warning**
- **What it does:** Monitors news, shipping data, weather events, and economic indicators to flag supply chain disruptions before they hit.
- **APIs used:** NewsAPI, GDELT, OpenWeatherMap, USGS Earthquake, FRED, ExchangeRate-API
- **AI angle:** Claude correlates weather events, geopolitical news, and economic shifts to predict supply chain impacts for specific industries and generates mitigation recommendations.
- **Revenue model:** $99/mo per supply chain tracked.
- **Competition:** Everstream, Resilinc charge $10K+/year for enterprise. This is the SMB version.

**23. CompetitorWatch — Automated Competitive Intelligence**
- **What it does:** Track competitors' tech stack changes, hiring patterns, news mentions, product launches, and financial filings in one dashboard.
- **APIs used:** BuiltWith, GitHub API, Adzuna, NewsAPI, SEC EDGAR, Product Hunt, Crunchbase
- **AI angle:** Claude identifies strategic patterns (e.g., "Competitor X added 5 ML engineers and changed their stack to include TensorFlow — likely building AI features").
- **Revenue model:** $49/mo for 3 competitors, $149/mo for 15.
- **Competition:** Crayon, Klue charge $10K+/year. This automates 80% of their value for 1% of the price.

**24. FundingTracker — Startup Funding Intelligence**
- **What it does:** Aggregates funding rounds from Crunchbase, SEC filings, and tech news. AI analyzes trends by sector, stage, and geography.
- **APIs used:** Crunchbase, SEC EDGAR, NewsAPI, Product Hunt, HN Algolia
- **AI angle:** Claude identifies emerging investment themes, predicts which sectors are heating up, and generates weekly funding landscape reports.
- **Revenue model:** Free weekly digest, $39/mo for real-time alerts and sector deep dives.
- **Competition:** Crunchbase Pro ($49/mo) has the data but no AI analysis layer.

**25. ReviewRadar — Multi-Platform Review Aggregator**
- **What it does:** Aggregates reviews/mentions from Google Places, Reddit, HN, and news sources for any product or business. AI categorizes feedback themes.
- **APIs used:** Google Places, Reddit JSON, HN Algolia, NewsAPI, StackExchange
- **AI angle:** Claude categorizes every mention into themes (pricing, UX, support, reliability), tracks sentiment over time, and generates a "Voice of the Customer" report.
- **Revenue model:** $29/mo for 1 product, $79/mo for 5 products.
- **Competition:** ReviewTrackers, Birdeye charge $200+/mo and focus on review management, not AI-powered analysis.

**26. IPORadar — Pre-IPO Company Intelligence**
- **What it does:** Tracks companies likely to IPO by monitoring SEC EDGAR filings, news patterns, hiring surges, and funding rounds.
- **APIs used:** SEC EDGAR, Crunchbase, NewsAPI, Adzuna, BLS, Open Corporates
- **AI angle:** Claude scores IPO likelihood based on filing patterns, identifies comparable companies' pre-IPO trajectories, and generates investment thesis briefs.
- **Revenue model:** $49/mo for retail investors.
- **Competition:** IPO-focused newsletters ($20-50/mo) are human-curated. This is automated and data-driven.

**27. RegWatch — Regulatory Change Monitor**
- **What it does:** Monitors the Federal Register, Congress.gov, and EU Open Data Portal for regulatory changes relevant to specific industries. AI explains impact.
- **APIs used:** Federal Register API, Congress.gov, EU Open Data Portal, NewsAPI
- **AI angle:** Claude translates legal/regulatory language into business impact summaries, identifies which regulations affect which business functions, and suggests compliance actions.
- **Revenue model:** $79/mo per industry vertical.
- **Competition:** Thomson Reuters, LexisNexis charge $thousands. This covers 70% of the use case for 1% of the price.

---

### Developer Tools & Utilities

**28. DepShield — Dependency Risk Scanner**
- **What it does:** Paste a package.json, requirements.txt, or Cargo.toml. Get a risk report on every dependency: vulnerability status, maintenance health, license issues, and alternatives.
- **APIs used:** npm Registry, PyPI, crates.io, Libraries.io, Snyk, OSV.dev, GitHub API
- **AI angle:** Claude goes beyond CVE lists to assess overall dependency health (commit frequency, bus factor, issue response time) and recommends safer alternatives.
- **Revenue model:** Free for 1 project, $19/mo for unlimited, $49/mo with CI/CD integration.
- **Competition:** Snyk (free tier limited), Dependabot (GitHub only). This combines multiple package ecosystems with AI risk narrative.

**29. GitPulse — Open Source Project Health Dashboard**
- **What it does:** Enter a GitHub repo URL, get a comprehensive health report: contributor trends, issue resolution time, PR velocity, dependency freshness, and community sentiment.
- **APIs used:** GitHub API, npm Registry, PyPI, Libraries.io, StackExchange, Reddit JSON
- **AI angle:** Claude generates a "Should you depend on this?" recommendation with reasoning, compares against similar projects, and predicts maintenance trajectory.
- **Revenue model:** Free for public repos, $29/mo for private repo scanning and team dashboards.
- **Competition:** GitHub Insights (basic), Cauldron (complex). This provides an AI-narrated, opinionated health check.

**30. APIStatus — Unified API Health Monitor**
- **What it does:** Monitor the health and response times of any set of APIs. Get alerts when endpoints degrade, change schemas, or go down.
- **APIs used:** Postman Echo, HTTPBin (for validation), SSL Labs API, W3C Validator
- **AI angle:** Claude analyzes response pattern changes to predict outages before they happen, identifies schema drift, and generates incident reports.
- **Revenue model:** Free for 5 endpoints, $15/mo for 50, $49/mo for 200 with Slack/Discord alerts.
- **Competition:** UptimeRobot (free, basic), Pingdom ($15/mo). AI-powered prediction and schema drift detection are unique.

**31. DocForge — API Documentation Generator**
- **What it does:** Point it at any REST API endpoint. It auto-discovers the schema, tests edge cases, and generates complete documentation with examples.
- **APIs used:** HTTPBin, Postman Echo (testing), GitHub API (hosting docs), Shields.io (badges)
- **AI angle:** Claude generates human-readable descriptions, infers field meanings, creates practical code examples in multiple languages, and identifies undocumented behaviors.
- **Revenue model:** $19/mo for individual developers, $79/mo for teams.
- **Competition:** Swagger/OpenAPI (requires manual spec). This auto-generates docs from live endpoints.

**32. CodeReviewBot — Automated PR Review Assistant**
- **What it does:** Connect to GitHub repos, get AI-powered code reviews on every PR. Checks for security issues, performance problems, style consistency, and best practices.
- **APIs used:** GitHub API, Snyk, OSV.dev, LanguageTool, StackExchange
- **AI angle:** Claude reviews code with context awareness, explains why changes are risky, suggests specific fixes, and learns team coding patterns over time.
- **Revenue model:** Free for public repos, $29/mo per private repo.
- **Competition:** CodeRabbit, Sourcery ($19+/mo). Differentiate with deeper security scanning via Snyk/OSV integration.

**33. StackSolver — AI-Powered Error Resolution**
- **What it does:** Paste an error message or stack trace. AI searches StackOverflow, GitHub Issues, and dev forums to find the most relevant solution and adapts it to your context.
- **APIs used:** StackExchange API, GitHub API, DEV.to, Reddit JSON (r/programming)
- **AI angle:** Claude doesn't just find matching answers — it synthesizes multiple solutions, ranks them by recency and upvotes, and tailors the fix to your specific stack.
- **Revenue model:** Free for 10/month, $12/mo unlimited (VS Code extension).
- **Competition:** StackOverflow search (manual), Phind (general). This is specifically optimized for error resolution.

**34. MigrationPilot — Framework Migration Planner**
- **What it does:** Analyze a codebase and generate a migration plan (e.g., React class to hooks, Python 2 to 3, Express to Fastify) with effort estimates and risk flags.
- **APIs used:** GitHub API, npm Registry, PyPI, Libraries.io, StackExchange
- **AI angle:** Claude analyzes the actual codebase, identifies breaking changes, estimates effort per file, and generates a prioritized migration checklist with automated codemods where possible.
- **Revenue model:** $49/mo for individual devs, $199/mo for teams.
- **Competition:** Migration tools are typically framework-specific. This is framework-agnostic with AI-powered effort estimation.

**35. LicenseGuard — Open Source License Compliance**
- **What it does:** Scan a project's full dependency tree and generate a license compliance report. Flag conflicts, missing attributions, and copyleft contamination.
- **APIs used:** npm Registry, PyPI, crates.io, Libraries.io, GitHub API
- **AI angle:** Claude explains license implications in plain English, identifies transitive dependency license conflicts, and generates NOTICE files and attribution documents.
- **Revenue model:** Free for 1 scan/month, $29/mo unlimited.
- **Competition:** FOSSA, WhiteSource charge $hundreds/mo. This covers the core use case at hobby-tier pricing.

---

### Local & Community Tools

**36. NeighborhoodIQ — Relocation Research Tool**
- **What it does:** Enter any US address and get a complete neighborhood report: demographics, crime rates, air quality, weather patterns, school ratings, and cost of living.
- **APIs used:** Census Bureau, FBI Crime Data, EPA AirNow, OpenWeatherMap, Nominatim, Zippopotam.us, BLS
- **AI angle:** Claude generates a narrative "livability report" comparing the neighborhood to similar areas, highlights trade-offs, and scores it against user-stated priorities (schools vs. cost vs. safety).
- **Revenue model:** Free for 3 reports, $9.99 per detailed report, $19/mo unlimited.
- **Competition:** Niche.com (basic grades), AreaVibes (scores only). AI narrative and personalized priority weighting are unique.

**37. EventScout — Hyperlocal Event Discovery**
- **What it does:** Aggregates events from Reddit community posts, Discourse forums, Meetup-style RSS feeds, and local news for any area. AI categorizes and recommends.
- **APIs used:** Reddit JSON, Discourse API, RSS2JSON, Nominatim, NewsAPI, Google Places
- **AI angle:** Claude learns user preferences, filters out low-quality events, and generates personalized weekly event digests with "why you'd like this" explanations.
- **Revenue model:** Free for users, sponsored event placement for organizers ($5-20/event).
- **Competition:** Eventbrite, Meetup miss hyperlocal events. This scrapes community sources they don't.

**38. LocalEats — Restaurant Discovery Beyond Yelp**
- **What it does:** Combines Google Places data with Reddit discussions, local news reviews, and health inspection scores for restaurant recommendations.
- **APIs used:** Google Places, Reddit JSON, NewsAPI, Nominatim, OpenWeatherMap
- **AI angle:** Claude analyzes Reddit discussions for authentic reviews (vs. fake Yelp reviews), identifies trending new spots before they're popular, and factors in weather for outdoor dining suggestions.
- **Revenue model:** Free for users, $49/mo for restaurant owners (reputation monitoring).
- **Competition:** Yelp (fake review problem), Google Maps (no community analysis). Reddit-sourced authenticity is the hook.

**39. CommuteCast — AI Commute Optimizer**
- **What it does:** Analyzes weather forecasts, air quality, and traffic patterns to recommend the best commute method and timing each day.
- **APIs used:** OpenWeatherMap, EPA AirNow, Nominatim, Open-Meteo, UV Index API
- **AI angle:** Claude learns your schedule and preferences, correlates weather/air quality with historical commute patterns, and sends morning recommendations ("Bike today — 72F, AQI 25, low UV").
- **Revenue model:** Free for basic, $4.99/mo for multi-modal optimization and calendar integration.
- **Competition:** Google Maps (no weather/AQ integration), Apple Weather (no commute advice). The combination is unique.

**40. DisasterReady — Local Emergency Preparedness**
- **What it does:** Monitors USGS earthquakes, NWS severe weather, EPA air quality, and news for your area. AI generates personalized emergency preparedness alerts.
- **APIs used:** USGS Earthquake, National Weather Service, EPA AirNow, NewsAPI, Nominatim
- **AI angle:** Claude contextualizes alerts (not just "earthquake magnitude 4.2" but "This is unlikely to cause damage at your location, but check water heater strapping") and maintains a personalized preparedness checklist.
- **Revenue model:** Free for basic alerts, $4.99/mo for family plans with check-in features.
- **Competition:** FEMA app (basic), Citizen (crime-focused). AI contextualization and preparedness coaching are unique.

**41. ParkFinder — Outdoor Recreation Planner**
- **What it does:** Find the best outdoor activities for any location based on current weather, air quality, UV index, and seasonal conditions.
- **APIs used:** OpenWeatherMap, EPA AirNow, UV Index API, Google Pollen API, Nominatim, Open-Meteo
- **AI angle:** Claude considers all environmental factors to recommend specific activities ("Good for trail running — clear skies, low pollen, moderate UV. Apply SPF 30. Avoid 12-2pm peak UV.").
- **Revenue model:** Free for basic, $6.99/mo for premium with weekly adventure planning.
- **Competition:** AllTrails (trails only), Weather apps (no activity recommendations). This is an activity-first weather tool.

---

### Personal Finance & Investing

**42. PortfolioNarrative — AI Investment Reporter**
- **What it does:** Connect your brokerage account or enter holdings. Get daily AI-generated reports explaining what happened to your portfolio and why, in plain English.
- **APIs used:** Alpha Vantage, Finnhub, FRED, CoinGecko, NewsAPI, ExchangeRate-API
- **AI angle:** Claude correlates your portfolio moves with specific news events, economic data releases, and sector trends. Not just "AAPL -2%" but "AAPL fell after new EU AI regulation news, impacting your tech allocation."
- **Revenue model:** Free for 1 portfolio, $14.99/mo for multiple portfolios and weekly deep-dive reports.
- **Competition:** Robinhood Snacks (generic), Yahoo Finance (raw data). Personalized narrative tied to YOUR holdings is the moat.

**43. DividendMap — Dividend Income Optimizer**
- **What it does:** Analyze dividend stocks using financial data and economic indicators. AI builds optimized dividend portfolios based on yield, safety, and growth.
- **APIs used:** Alpha Vantage, Finnhub, Twelve Data, FRED, SEC EDGAR
- **AI angle:** Claude analyzes payout ratios, free cash flow trends, and economic cycle positioning to score dividend sustainability. Generates "dividend calendar" showing expected monthly income.
- **Revenue model:** $19/mo for portfolio tracking and recommendations.
- **Competition:** Simply Safe Dividends ($199/yr), Seeking Alpha ($240/yr). This is cheaper with AI-powered safety scoring.

**44. CryptoSentinel — Crypto Market Intelligence**
- **What it does:** Tracks crypto prices, on-chain data, social sentiment, and news. AI generates risk assessments and identifies unusual activity patterns.
- **APIs used:** CoinGecko, Binance, Kraken, Coinbase, Reddit JSON, HN Algolia, NewsAPI
- **AI angle:** Claude correlates price movements with social sentiment shifts and news events to identify FUD vs. real risk. Generates "Fear/Greed" narratives explaining market psychology.
- **Revenue model:** Free for top 10 coins, $24.99/mo for full portfolio with alerts.
- **Competition:** CoinMarketCap (data only), Santiment ($49/mo). AI narrative and multi-source sentiment analysis differentiate.

**45. ForexFlow — Currency Movement Explainer**
- **What it does:** Tracks exchange rates and explains WHY currencies are moving by correlating with economic data, news events, and policy changes.
- **APIs used:** ExchangeRate-API, Fixer.io, FRED, World Bank, NewsAPI, Federal Register
- **AI angle:** Claude generates daily currency movement narratives: "USD strengthened against EUR because of better-than-expected jobs data from BLS, while ECB signals rate hold."
- **Revenue model:** $19/mo for 5 currency pairs, $49/mo for unlimited with alerts.
- **Competition:** XE.com (rates only), Bloomberg (expensive). AI explanation of movements is unique at this price point.

**46. TaxHarvest — Tax Loss Harvesting Assistant**
- **What it does:** Monitor your portfolio for tax loss harvesting opportunities. AI identifies similar replacement securities and calculates tax savings.
- **APIs used:** Alpha Vantage, Twelve Data, Finnhub, IEX Cloud
- **AI angle:** Claude identifies wash sale risks, suggests correlated-but-not-identical replacement funds, and estimates actual tax savings based on your bracket.
- **Revenue model:** $29/mo or 0.1% of harvested losses.
- **Competition:** Wealthfront (requires full AUM), TurboTax (manual). This is a standalone tool for DIY investors.

**47. SideHustleTracker — Freelance Income Dashboard**
- **What it does:** Track freelance income, expenses, tax obligations, and market rates. AI estimates quarterly taxes and suggests rate adjustments based on market data.
- **APIs used:** BLS, FRED, ExchangeRate-API, Adzuna (rate benchmarking)
- **AI angle:** Claude analyzes your earning patterns, predicts quarterly tax obligations, identifies your most profitable services, and benchmarks your rates against market data.
- **Revenue model:** Free for basic tracking, $12/mo for AI insights and tax estimates.
- **Competition:** QuickBooks Self-Employed ($15/mo), Hurdlr ($10/mo). AI rate benchmarking and predictive tax estimates are the hook.

---

### Health & Wellness

**48. AllergyShield — Personalized Allergy Forecast**
- **What it does:** Combines pollen forecasts, air quality data, and weather conditions to generate personalized allergy risk scores and medication timing recommendations.
- **APIs used:** Google Pollen API, EPA AirNow, OpenWeatherMap, Open-Meteo
- **AI angle:** Claude learns your specific triggers, correlates your symptom diary with environmental data, and predicts bad days 48 hours in advance with preventive action suggestions.
- **Revenue model:** Free basic forecast, $5.99/mo for personalized predictions and medication reminders.
- **Competition:** Pollen.com (basic counts), Weather apps (generic). Personalized correlation with your symptom patterns is unique.

**49. AirGuard — Indoor/Outdoor Air Quality Advisor**
- **What it does:** Real-time air quality monitoring with AI-generated health recommendations based on your conditions (asthma, COPD, exercise plans).
- **APIs used:** World Air Quality Index (WAQI), EPA AirNow, OpenWeatherMap, Open-Meteo
- **AI angle:** Claude provides context-aware advice: "AQI is 85 — safe for most people but if you have asthma, run indoors today. Window ventilation safe after 6pm when AQI drops."
- **Revenue model:** Free for basic, $4.99/mo for health-condition-specific advice.
- **Competition:** IQAir (data focused), AirVisual (basic alerts). Health-condition-personalized advice is the differentiator.

**50. FitWeather — Weather-Optimized Workout Planner**
- **What it does:** Generates daily workout plans optimized for weather, air quality, UV exposure, and your fitness goals.
- **APIs used:** OpenWeatherMap, UV Index API, EPA AirNow, Google Pollen API, Open-Meteo
- **AI angle:** Claude adjusts workout intensity and location (indoor/outdoor) based on conditions, plans the optimal time of day, and adapts your training plan around weather patterns.
- **Revenue model:** $7.99/mo for personalized plans.
- **Competition:** Generic fitness apps ignore weather. This is the first weather-aware workout planner.

**51. DrugCheck — Medication Interaction Checker**
- **What it does:** Enter your medications, get a comprehensive interaction report with AI-explained risks, food interactions, and timing recommendations.
- **APIs used:** OpenFDA, WHO GHO, Wikipedia API
- **AI angle:** Claude explains interactions in plain English, provides severity context, suggests questions to ask your doctor, and identifies OTC drugs that interact with your prescriptions.
- **Revenue model:** Free for 3 medications, $6.99/mo for unlimited with family profiles.
- **Competition:** Drugs.com (basic checker), WebMD (generic). AI-generated plain-English explanations with actionable doctor questions are unique.

---

### Education & Research

**52. PaperScout — Academic Research Assistant**
- **What it does:** Enter a research topic, get a curated reading list with AI-generated summaries, key findings, methodology assessments, and citation networks.
- **APIs used:** Open Library, Archive.org, Wikipedia API, Wikidata SPARQL, DEV.to, StackExchange
- **AI angle:** Claude summarizes papers at different complexity levels (undergraduate vs. PhD), identifies methodological strengths and weaknesses, and maps how papers connect.
- **Revenue model:** Free for 5 searches/month, $14.99/mo for students, $29/mo for researchers.
- **Competition:** Semantic Scholar (basic), Connected Papers (visualization only). AI-generated summaries at multiple levels are the differentiator.

**53. LanguageLab — AI Language Learning Companion**
- **What it does:** Practice conversations with AI in any language. Get grammar corrections, vocabulary suggestions, and cultural context. AI adapts difficulty to your level.
- **APIs used:** DeepL, LibreTranslate, MyMemory Translation, LanguageTool, Datamuse, VoiceRSS
- **AI angle:** Claude conducts natural conversations, corrects mistakes in context (not just grammar rules), teaches colloquial usage, and generates personalized vocabulary lists.
- **Revenue model:** Free for 10 conversations/month, $12.99/mo unlimited.
- **Competition:** Duolingo (gamified but shallow), iTalki (expensive tutors). AI provides tutor-quality conversation practice at app pricing.

**54. HistoryMap — Interactive Historical Event Explorer**
- **What it does:** Explore historical events on an interactive timeline and map. AI connects events, explains causes and consequences, and answers follow-up questions.
- **APIs used:** Wikipedia API, Wikidata SPARQL, Archive.org, Open Library, Nominatim
- **AI angle:** Claude generates narrative connections between events ("The 1929 crash led to the Smoot-Hawley Tariff, which deepened the Depression and contributed to WWII"), answers counterfactual questions.
- **Revenue model:** Free for education, $9.99/mo for premium features (essay generation, citation support).
- **Competition:** Wikipedia (unstructured), Khan Academy (video only). Interactive AI-narrated exploration is unique.

**55. StudyForge — Exam Prep Generator**
- **What it does:** Enter a subject or textbook chapter. AI generates practice questions, flashcards, and study guides pulling from Wikipedia, Open Library, and educational resources.
- **APIs used:** Wikipedia API, Open Library, Wikidata SPARQL, Datamuse, LanguageTool
- **AI angle:** Claude generates questions at varying difficulty levels, explains wrong answers with references, identifies knowledge gaps, and creates spaced-repetition schedules.
- **Revenue model:** Free for basic, $9.99/mo for students.
- **Competition:** Quizlet (user-generated), Anki (manual creation). AI auto-generates content from any source material.

**56. CodeMentor — Interactive Coding Tutorial Generator**
- **What it does:** Enter a programming concept or project idea. AI generates a step-by-step tutorial with real code examples, exercises, and links to documentation.
- **APIs used:** GitHub API, StackExchange, npm Registry, PyPI, DevDocs.io, DEV.to
- **AI angle:** Claude tailors tutorials to your skill level, uses real-world code patterns from popular repos, and generates progressively harder exercises.
- **Revenue model:** Free for basic, $14.99/mo for personalized learning paths.
- **Competition:** freeCodeCamp (rigid curriculum), Codecademy ($20/mo). AI-personalized, data-backed tutorials are the hook.

**57. GrantWriter — AI Research Grant Assistant**
- **What it does:** Help researchers find relevant grants and draft application sections. Pulls from government grant databases and matches to research profiles.
- **APIs used:** USASpending, Data.gov, Federal Register, Congress.gov, Wikipedia API
- **AI angle:** Claude matches research profiles to grants, drafts specific aims pages, generates budget justifications, and identifies funding trends in your field.
- **Revenue model:** $49/mo for researchers, $199/mo for institutions.
- **Competition:** Pivot-RP ($thousands/year), Grant Forward. This is the affordable alternative with AI drafting.

---

### Real Estate & Property

**58. PropertyPulse — Real Estate Investment Analyzer**
- **What it does:** Enter any US address and get an investment analysis: demographics, economic trends, crime data, environmental risks, and comparable area analysis.
- **APIs used:** Census Bureau, FRED, BLS, FBI Crime Data, EPA AirNow, USGS Earthquake, Zippopotam.us, Nominatim
- **AI angle:** Claude generates a narrative investment thesis: why this area is appreciating or declining, what demographic shifts mean for rental demand, and compares to similar neighborhoods nationwide.
- **Revenue model:** Free for 2 analyses, $29/mo for investors.
- **Competition:** Zillow (price estimates), Mashvisor ($100/mo). This combines more data sources at lower cost with AI narrative.

**59. RentRadar — Rental Market Intelligence**
- **What it does:** Track rental market conditions in any area: economic indicators, population trends, employment data, and seasonal patterns.
- **APIs used:** Census Bureau, BLS, FRED, Nominatim, OpenWeatherMap
- **AI angle:** Claude identifies emerging rental markets before they're obvious, predicts seasonal demand patterns, and generates landlord-focused market reports.
- **Revenue model:** $19/mo for landlords, $49/mo for property managers.
- **Competition:** RentCafe (listings), CoStar ($expensive). This provides market intelligence at consumer prices.

**60. FloodCheck — Property Environmental Risk Report**
- **What it does:** Enter an address, get a comprehensive environmental risk report: earthquake proximity, air quality history, flood risk factors, and weather extremes.
- **APIs used:** USGS Earthquake, EPA AirNow, National Weather Service, Open-Meteo (historical), Nominatim
- **AI angle:** Claude translates raw data into insurance and safety implications. "This property is 12 miles from an active fault. Historical AQI exceeds 100 on 15 days/year. Factor flood insurance at $X/year."
- **Revenue model:** $4.99 per report, $19/mo for real estate agents (unlimited).
- **Competition:** FEMA flood maps (hard to read), ClimateCheck ($10/report). AI-generated plain-English risk narratives are the differentiator.

**61. RemoterScout — Remote Worker Relocation Advisor**
- **What it does:** For remote workers considering relocation: compare cities on cost of living, taxes, weather, air quality, internet infrastructure, and coworking density.
- **APIs used:** BLS, Census Bureau, OpenWeatherMap, EPA AirNow, Nominatim, REST Countries, Google Places
- **AI angle:** Claude generates personalized "should you move?" reports based on your priorities (climate, taxes, community), current salary, and work requirements.
- **Revenue model:** $9.99 per city comparison, $19/mo unlimited.
- **Competition:** Nomad List ($99/yr for digital nomads). This targets domestic remote worker relocation specifically.

---

### Government & Civic Tech

**62. SpendingStory — Government Spending Narratives**
- **What it does:** Make government spending data accessible. Enter any federal agency or program, get AI-narrated spending breakdowns with trends and context.
- **APIs used:** USASpending, FRED, Congress.gov, Federal Register
- **AI angle:** Claude transforms raw spending data into journalist-quality narratives: "NASA's budget increased 12% YoY, with 40% going to Artemis. Here's how that compares to the Apollo era in inflation-adjusted dollars."
- **Revenue model:** Free for public use, $29/mo for journalists and researchers (export, API access).
- **Competition:** USASpending.gov (raw data), GovTrack (votes only). AI narrative layer makes data accessible.

**63. BillTracker — Legislation Impact Analyzer**
- **What it does:** Track bills in Congress and get AI-generated impact analyses: who benefits, who's harmed, economic implications, and likelihood of passage.
- **APIs used:** Congress.gov, Federal Register, NewsAPI, FRED, BLS
- **AI angle:** Claude explains bills in plain English, estimates economic impact using FRED data, identifies affected industries, and tracks amendment changes.
- **Revenue model:** Free for 5 bills, $14.99/mo for lobbyists, advocacy groups, and policy wonks.
- **Competition:** GovTrack (tracking only), LegiScan (basic). AI impact analysis is the unique layer.

**64. CensusStory — Demographic Trend Explorer**
- **What it does:** Explore Census data through natural language. "Show me population growth in Phoenix metro vs. Austin over the last decade" returns AI-generated analysis with charts.
- **APIs used:** Census Bureau, BLS, FRED, Nominatim, BEA
- **AI angle:** Claude translates Census queries from plain English, generates trend narratives, identifies correlations, and produces report-ready visualizations.
- **Revenue model:** Free for basic queries, $24.99/mo for export, custom reports, and API access.
- **Competition:** Census.gov (terrible UX), Social Explorer ($90/yr). Natural language querying is a massive UX improvement.

**65. SafetyScore — Community Safety Dashboard**
- **What it does:** Real-time community safety dashboard combining crime data, earthquake activity, weather alerts, and air quality for any US location.
- **APIs used:** FBI Crime Data, USGS Earthquake, National Weather Service, EPA AirNow, Nominatim
- **AI angle:** Claude generates contextualized safety briefs: not just crime rates but trends, comparison to similar communities, and seasonal patterns with predictive alerts.
- **Revenue model:** Free for basic, $9.99/mo for real-time alerts and family safety features.
- **Competition:** CrimeMapping (crime only), Ring Neighbors (anecdotal). Multi-factor safety scoring with AI context is unique.

**66. VoteGuide — AI Election Research Tool**
- **What it does:** Enter your address, get a complete voter guide: upcoming elections, candidate profiles, voting record analysis, and policy position comparisons.
- **APIs used:** Congress.gov, Federal Register, NewsAPI, Wikipedia API, Nominatim
- **AI angle:** Claude generates balanced candidate comparisons, explains policy positions in plain English, and identifies discrepancies between stated positions and voting records.
- **Revenue model:** Free (civic tool), optional donations. Premium: $4.99/mo for custom issue tracking.
- **Competition:** Ballotpedia (basic info), Vote Smart (data heavy). AI-generated balanced comparisons are the differentiator.

**67. OpenSanctionsCheck — Compliance Screening Tool**
- **What it does:** Screen individuals and companies against global sanctions lists, PEP databases, and corporate registries for KYC/AML compliance.
- **APIs used:** Open Sanctions, Open Corporates, Companies House UK, VIES VAT, SEC EDGAR
- **AI angle:** Claude resolves name variations, reduces false positives, explains why matches were flagged, and generates compliance reports.
- **Revenue model:** $49/mo for 100 screenings, $199/mo for 1000.
- **Competition:** Dow Jones Risk & Compliance ($thousands), ComplyAdvantage ($$$). This is the affordable SMB version.

---

### E-commerce & Retail

**68. PriceDrop — Smart Price Alert System**
- **What it does:** Track product prices across retailers. AI predicts when prices will drop based on historical patterns, seasonal trends, and economic indicators.
- **APIs used:** FRED (consumer spending indicators), NewsAPI (retail news), Reddit JSON (deal communities), CoinGecko (for crypto purchases)
- **AI angle:** Claude predicts price drops by analyzing seasonal patterns, upcoming sales events, and economic indicators. "TVs drop 23% average in the 2 weeks before Super Bowl."
- **Revenue model:** Free for 10 items, $4.99/mo unlimited with prediction alerts.
- **Competition:** CamelCamelCamel (Amazon only), Honey (no prediction). AI price prediction is the moat.

**69. ReviewSynth — Product Review Summarizer**
- **What it does:** Enter a product name, get an AI-synthesized review summary from Reddit, forums, and community discussions (not just Amazon reviews).
- **APIs used:** Reddit JSON, HN Algolia, StackExchange, DEV.to (for tech products), Google Places (for local businesses)
- **AI angle:** Claude identifies review patterns, separates genuine feedback from marketing, compares products head-to-head, and generates "buy or skip" recommendations with reasoning.
- **Revenue model:** Free for 5/month, $6.99/mo unlimited (browser extension).
- **Competition:** ReviewMeta (Amazon focused), Fakespot (fake detection). Community-sourced synthesis is the differentiator.

**70. DropshipScout — Product Research for E-commerce**
- **What it does:** Identifies trending products by analyzing social media trends, news, and seasonal patterns. AI predicts demand windows.
- **APIs used:** Reddit JSON, HN Algolia, Product Hunt, NewsAPI, Google Places, FRED
- **AI angle:** Claude identifies emerging product trends 2-4 weeks before they peak, analyzes competition density, and estimates profit margins based on seasonal patterns.
- **Revenue model:** $29/mo for product research, $79/mo with supplier database.
- **Competition:** Jungle Scout ($49/mo, Amazon only), Sell The Trend ($40/mo). Multi-platform trend detection is the hook.

**71. StorefrontAudit — E-commerce Site Analyzer**
- **What it does:** Enter any e-commerce URL and get a comprehensive audit: tech stack, performance, SEO basics, SSL security, and competitive positioning.
- **APIs used:** BuiltWith, SSL Labs, W3C Validator, WhoisXML API, SimilarWeb, Clearbit Logo
- **AI angle:** Claude identifies specific opportunities (missing structured data, slow loading, weak SSL config) and generates a prioritized improvement roadmap.
- **Revenue model:** Free for 1 audit/month, $24.99/mo for agencies (unlimited).
- **Competition:** GTmetrix (speed only), Screaming Frog (SEO only). AI-generated multi-factor audit with prioritized recommendations is unique.

---

### HR & Recruiting

**72. HireSignal — Candidate Sourcing Intelligence**
- **What it does:** Find and evaluate potential hires by analyzing GitHub contributions, Stack Overflow activity, DEV.to posts, and community engagement.
- **APIs used:** GitHub API, StackExchange, DEV.to, HN Algolia, npm Registry, PyPI
- **AI angle:** Claude evaluates code quality, contribution patterns, communication skills (from comments/posts), and generates candidate briefs with strengths, concerns, and interview question suggestions.
- **Revenue model:** $49/mo for 10 searches, $149/mo unlimited.
- **Competition:** LinkedIn Recruiter ($150/mo), GitHub search (basic). AI-powered skill assessment from public activity is unique.

**73. SalaryBenchmark — AI Compensation Analyzer**
- **What it does:** Get accurate salary benchmarks by combining BLS data, job board listings, and economic indicators for any role in any US metro.
- **APIs used:** BLS, FRED, Adzuna, RemoteOK, Census Bureau, Nominatim
- **AI angle:** Claude adjusts for cost of living, analyzes trends (is this role's pay growing or shrinking?), and generates compensation reports with percentile breakdowns.
- **Revenue model:** Free for 3 lookups, $19/mo for HR teams.
- **Competition:** Glassdoor (user-reported, biased), Salary.com ($100+/mo). Government data + AI analysis is more accurate and cheaper.

**74. TalentTrend — Tech Hiring Market Dashboard**
- **What it does:** Real-time dashboard showing which technologies, roles, and skills are trending in job listings. Identify what to learn or hire for.
- **APIs used:** Adzuna, RemoteOK, We Work Remotely, GitHub API (trending repos), npm Registry, PyPI
- **AI angle:** Claude identifies emerging skill demands before they become obvious ("Rust jobs increased 40% QoQ, mostly in crypto and systems companies — expect mainstream adoption in 12 months").
- **Revenue model:** Free dashboard, $24.99/mo for alerts and custom skill tracking.
- **Competition:** LinkedIn talent insights (enterprise), Indeed hiring trends (basic). AI-powered predictive skill demand forecasting is the differentiator.

**75. InterviewPrep — AI Interview Coach**
- **What it does:** Enter a company name and role. AI generates likely interview questions based on the company's tech stack, recent news, and Glassdoor reviews.
- **APIs used:** BuiltWith, GitHub API, Glassdoor (Unofficial), NewsAPI, Adzuna, StackExchange
- **AI angle:** Claude generates company-specific questions (not generic), provides model answers, and conducts mock interviews adapting to your responses.
- **Revenue model:** Free for 1 prep session, $19/mo for unlimited.
- **Competition:** Pramp (peer practice), InterviewBit (algorithm only). Company-specific AI-generated prep is unique.

**76. RetentionRadar — Employee Attrition Predictor**
- **What it does:** For HR teams: combines industry turnover data, local job market conditions, and economic indicators to predict attrition risk.
- **APIs used:** BLS, FRED, Adzuna, RemoteOK, Census Bureau
- **AI angle:** Claude identifies external risk factors ("Tech job postings in Austin up 30%, your engineers are being recruited") and suggests retention strategies based on market conditions.
- **Revenue model:** $79/mo per company.
- **Competition:** Visier, Lattice ($thousands). This provides external-signal-based prediction at SMB pricing.

---

### Marketing & SEO

**77. SEOPilot — AI Content Strategy Planner**
- **What it does:** Analyze any website's content strategy and generate a competitive content plan. Identifies content gaps, keyword opportunities, and topic clusters.
- **APIs used:** BuiltWith, SimilarWeb, Reddit JSON, HN Algolia, StackExchange, Google Places, Wayback Machine
- **AI angle:** Claude analyzes competitor content, identifies questions being asked on Reddit/HN that nobody's answering, and generates a 90-day content calendar with specific article briefs.
- **Revenue model:** $39/mo for bloggers, $99/mo for agencies.
- **Competition:** Ahrefs ($99/mo), SEMrush ($130/mo). This uses free APIs + AI for content strategy (not backlink analysis, which needs paid data).

**78. EmailCraft — AI Cold Email Generator**
- **What it does:** Enter a prospect's email or domain. AI researches the company and person, then generates a personalized cold email based on their tech stack, recent news, and hiring patterns.
- **APIs used:** Hunter.io, BuiltWith, NewsAPI, GitHub API, Crunchbase, Clearbit Logo
- **AI angle:** Claude writes emails that reference specific, recent, relevant things about the prospect ("Noticed you migrated to Next.js last month — here's how we help teams optimize...").
- **Revenue model:** $29/mo for 100 emails, $79/mo for 500.
- **Competition:** Instantly ($30/mo), Lemlist ($59/mo) are sending tools. This focuses on research-backed personalization.

**79. AdSpy — Competitor Ad Research Tool**
- **What it does:** Track competitors' online presence changes: tech stack updates, new pages, content changes, and hiring patterns that signal marketing strategy shifts.
- **APIs used:** BuiltWith, Wayback Machine, SimilarWeb, Adzuna, NewsAPI, WhoisXML API
- **AI angle:** Claude identifies strategic patterns from observable data ("Competitor added HubSpot tracking, posted 3 marketing roles, and registered 2 new domains — likely launching a new product line").
- **Revenue model:** $49/mo for 5 competitors.
- **Competition:** SpyFu, SimilarWeb Pro ($100+/mo). AI-powered strategic inference from free signals is unique.

**80. SocialProof — Testimonial & Case Study Generator**
- **What it does:** Pull customer mentions from Reddit, Product Hunt, HN, and social media. AI identifies the best testimonials and drafts case study outlines.
- **APIs used:** Reddit JSON, Product Hunt, HN Algolia, DEV.to, StackExchange, Mastodon
- **AI angle:** Claude finds and ranks unsolicited positive mentions, extracts quotable passages, identifies customers for case study outreach, and drafts case study frameworks.
- **Revenue model:** $24.99/mo for startups.
- **Competition:** Testimonial.to (collection tool), Senja ($29/mo). This finds organic mentions you didn't know existed.

**81. LocalSEO — Small Business Local Search Optimizer**
- **What it does:** Analyze a local business's online presence: Google Places profile, competitor analysis, local search optimization, and reputation monitoring.
- **APIs used:** Google Places, Nominatim, Reddit JSON, BuiltWith, WhoisXML API
- **AI angle:** Claude audits the business listing, identifies optimization opportunities, benchmarks against local competitors, and generates a monthly improvement plan.
- **Revenue model:** $29/mo for small businesses.
- **Competition:** BrightLocal ($39/mo), Yext ($199/mo). AI-generated action plans at lower price point.

---

### Legal & Compliance

**82. ComplianceBot — Regulatory Compliance Checker**
- **What it does:** Enter your business type and location. AI identifies relevant federal, state, and industry regulations and generates a compliance checklist.
- **APIs used:** Federal Register, Congress.gov, EU Open Data Portal, Data.gov, Open Sanctions
- **AI angle:** Claude maps regulations to specific business functions, explains requirements in plain English, tracks regulatory changes, and alerts when new rules affect your business.
- **Revenue model:** $49/mo for small businesses, $199/mo for multi-state operations.
- **Competition:** ComplyAdvantage (enterprise), manual legal research. AI-automated compliance mapping for SMBs is underserved.

**83. PatentScout — Patent Landscape Analyzer**
- **What it does:** Research patent landscapes for any technology. AI identifies key patents, potential conflicts, and white space opportunities.
- **APIs used:** Data.gov, Wikipedia API, Wikidata SPARQL, NewsAPI, SEC EDGAR
- **AI angle:** Claude maps patent clusters, identifies potential infringement risks, highlights expiring patents that create opportunities, and generates freedom-to-operate summaries.
- **Revenue model:** $79/mo for startups, $249/mo for patent attorneys.
- **Competition:** Google Patents (search only), PatSnap ($thousands). AI-powered landscape analysis at startup pricing.

**84. ContractCompare — Side-by-Side Contract Analysis**
- **What it does:** Upload two contracts (e.g., a vendor's proposed terms vs. your standard terms). AI highlights differences, flags risks, and suggests negotiation points.
- **APIs used:** OCR.space, LanguageTool, HuggingFace Inference (NER)
- **AI angle:** Claude identifies materially different clauses, explains implications, generates redline suggestions, and provides negotiation talking points.
- **Revenue model:** Free for 2 comparisons/month, $39/mo unlimited.
- **Competition:** LegalSifter (enterprise), manual review. AI contract comparison for SMBs doesn't really exist.

**85. PrivacyAudit — Website Privacy Compliance Scanner**
- **What it does:** Scan any website for privacy compliance issues: cookies, tracking scripts, data collection practices, and policy gaps.
- **APIs used:** BuiltWith, SSL Labs, W3C Validator, WhoisXML API
- **AI angle:** Claude identifies specific GDPR/CCPA violations, explains the risk level, and generates remediation steps with sample policy language.
- **Revenue model:** Free for 1 scan, $29/mo for agencies (unlimited), $99/mo with monitoring.
- **Competition:** Cookiebot ($12/mo, cookies only), OneTrust (enterprise). Full-scope AI privacy audit is unique at this price.

---

### Sustainability & Climate

**86. CarbonCalc — Business Carbon Footprint Estimator**
- **What it does:** Estimate business carbon footprint using economic data, energy consumption benchmarks, and industry averages. AI generates reduction roadmaps.
- **APIs used:** EPA AirNow, World Bank (climate indicators), FRED, BLS, Open-Meteo (historical climate)
- **AI angle:** Claude estimates emissions from business activity data, benchmarks against industry peers, identifies highest-impact reduction opportunities, and generates sustainability reports.
- **Revenue model:** Free for basic estimate, $39/mo for detailed tracking and reporting.
- **Competition:** Watershed ($expensive), manual calculations. AI-estimated footprints from economic data is novel for SMBs.

**87. ClimateRisk — Location Climate Risk Assessment**
- **What it does:** Enter any address and get a 30-year climate risk projection: heat waves, flooding, air quality degradation, and extreme weather probability.
- **APIs used:** Open-Meteo (historical), USGS Earthquake, EPA AirNow, National Weather Service, Oikolab
- **AI angle:** Claude analyzes 20+ years of historical weather data to project trends, contextualizes risks for property decisions, and generates insurance-relevant risk summaries.
- **Revenue model:** $9.99 per report, $49/mo for real estate professionals.
- **Competition:** ClimateCheck ($10/report), First Street (flood only). Multi-hazard AI-projected risk is more comprehensive.

**88. GreenScore — Product Sustainability Scorer**
- **What it does:** Enter a product or brand name. AI researches sustainability practices from public data, news, and corporate filings to generate a sustainability score.
- **APIs used:** SEC EDGAR, NewsAPI, Reddit JSON, Wikipedia API, Open Corporates
- **AI angle:** Claude aggregates sustainability data from filings, news sentiment, and community reports to generate evidence-based sustainability scores with source citations.
- **Revenue model:** Free for consumers, $29/mo for brands (track your own score).
- **Competition:** Good On You (fashion only), B Corp (certification). AI-aggregated scoring across all industries is new.

**89. EnergyOptimizer — Home Energy Usage Analyzer**
- **What it does:** Enter your location and home details. AI analyzes weather patterns, energy rate trends, and seasonal usage to optimize heating/cooling schedules and predict bills.
- **APIs used:** OpenWeatherMap, Open-Meteo (historical), FRED (energy prices), Nominatim
- **AI angle:** Claude correlates weather forecasts with your usage patterns to recommend specific thermostat settings and predict monthly bills within 10% accuracy.
- **Revenue model:** Free for basic tips, $7.99/mo for smart thermostat integration and bill prediction.
- **Competition:** Sense (hardware required), EnergyStar (generic tips). Software-only AI prediction from weather data is unique.

---

### Automation & Productivity

**90. InboxZero — AI Email Triage Assistant**
- **What it does:** Analyzes incoming emails and auto-categorizes them: urgent, actionable, FYI, promotional, follow-up needed. Generates draft responses for common patterns.
- **APIs used:** Abstract Email Validation, Hunter.io, Clearbit Logo, NewsAPI
- **AI angle:** Claude understands email context, prioritizes by sender importance (enriched via Hunter/Clearbit), drafts contextual responses, and identifies emails that need follow-up.
- **Revenue model:** $12.99/mo for individuals, $29/mo for teams.
- **Competition:** SaneBox ($7/mo, rule-based), Superhuman ($30/mo). AI-drafted responses with sender enrichment is the differentiator.

**91. ReportForge — Automated Business Report Generator**
- **What it does:** Connect data sources (Supabase, APIs) and generate polished weekly/monthly business reports with AI-written narratives, charts, and recommendations.
- **APIs used:** FRED, BLS, Alpha Vantage, ExchangeRate-API, Plausible Analytics
- **AI angle:** Claude transforms raw metrics into executive-ready narratives: not just "revenue up 12%" but "revenue increased 12% driven by new enterprise tier, outpacing the 3% industry average (BLS data)."
- **Revenue model:** $39/mo for automated weekly reports, $99/mo with custom KPIs.
- **Competition:** Databox ($72/mo), Geckoboard ($39/mo) — dashboards without AI narrative. This writes the report for you.

**92. MeetingRecap — AI Meeting Notes & Action Items**
- **What it does:** Upload meeting audio or paste a transcript. AI generates structured notes, action items, decisions made, and follow-up tasks.
- **APIs used:** Deepgram or AssemblyAI (transcription), LanguageTool, Datamuse
- **AI angle:** Claude identifies decisions vs. discussions vs. action items, assigns owners, generates follow-up emails, and tracks action item completion across meetings.
- **Revenue model:** Free for 2 meetings/month, $19/mo unlimited.
- **Competition:** Otter.ai ($17/mo), Fireflies ($19/mo). Action item tracking and follow-up email generation differentiate.

**93. DataPipe — No-Code API Integration Builder**
- **What it does:** Visual builder to connect any APIs from the catalog, transform data with AI, and output to Supabase, webhooks, or dashboards.
- **APIs used:** Any combination from the 190-API catalog
- **AI angle:** Claude generates the integration code, handles authentication, manages rate limits, and transforms data between incompatible API schemas automatically.
- **Revenue model:** Free for 3 integrations, $19/mo for 20, $49/mo unlimited.
- **Competition:** Zapier ($20/mo), Make ($9/mo). AI-powered data transformation and free API focus differentiate.

**94. ChangelogAI — Automated Release Notes Generator**
- **What it does:** Connect to a GitHub repo. AI generates user-facing release notes from commits, PRs, and issues. Publishes to a hosted changelog page.
- **APIs used:** GitHub API, GitLab API, Shields.io
- **AI angle:** Claude transforms developer-facing commit messages into user-friendly release notes, categorizes changes (features, fixes, improvements), and generates email-ready announcements.
- **Revenue model:** Free for public repos, $14.99/mo per private repo.
- **Competition:** Release Please (templates only), Changelogfy ($29/mo). AI-written user-facing notes from developer commits is the key differentiator.

**95. FormGenius — AI Form Builder**
- **What it does:** Describe what information you need to collect. AI generates an optimized form with validation, conditional logic, and submission handling (stored in Supabase).
- **APIs used:** Abstract Email Validation, ZeroBounce, Zippopotam.us, Nominatim
- **AI angle:** Claude designs forms that minimize abandonment, adds smart validation (real-time email/address verification), and generates analysis reports on submissions.
- **Revenue model:** Free for 3 forms, $14.99/mo unlimited.
- **Competition:** Typeform ($25/mo), Tally (free, basic). AI-optimized form design with built-in data validation is unique.

---

### Cross-Category Power Combinations

**96. StartupRadar — New Startup Discovery Engine**
- **What it does:** Identifies newly launched startups by monitoring Product Hunt, HN launches, new domain registrations, GitHub trending, and funding news.
- **APIs used:** Product Hunt, HN Algolia, WhoisXML API, GitHub API, Crunchbase, NewsAPI
- **AI angle:** Claude scores startup potential based on team backgrounds, market timing, tech stack choices, and community reception. Generates weekly "startups to watch" briefings.
- **Revenue model:** Free weekly digest, $29/mo for real-time alerts and deep dives.
- **Competition:** Product Hunt (launches only), Crunchbase (funding only). Multi-signal AI scoring across launch, technical, and market indicators is unique.

**97. FreelanceHQ — Complete Freelancer Business Tool**
- **What it does:** All-in-one freelancer tool: find leads (job boards), validate clients (email/company checks), track income, benchmark rates, and estimate taxes.
- **APIs used:** Adzuna, RemoteOK, Hunter.io, Open Corporates, BLS, FRED, ExchangeRate-API
- **AI angle:** Claude identifies high-value opportunities, validates client legitimacy, suggests optimal pricing, and generates proposals with market-rate justification.
- **Revenue model:** $19/mo for freelancers.
- **Competition:** AND.CO (invoicing), Upwork (marketplace). This combines sourcing + validation + business management.

**98. CityCompare — Relocation Decision Engine**
- **What it does:** Compare any two cities across 50+ factors: cost of living, weather, air quality, crime, employment, demographics, and more.
- **APIs used:** Census Bureau, BLS, FRED, OpenWeatherMap, EPA AirNow, FBI Crime Data, Nominatim, BEA
- **AI angle:** Claude generates a personalized comparison weighted by your priorities, identifies hidden advantages (e.g., "Austin has no state income tax, saving you $X on your salary"), and produces a recommendation with confidence score.
- **Revenue model:** Free for 1 comparison, $9.99/mo unlimited.
- **Competition:** NomadList (digital nomads), BestPlaces (basic). AI-personalized weighted comparison is the differentiator.

**99. NicheValidator — Business Idea Validation Tool**
- **What it does:** Enter a business idea. AI researches market size (BLS/Census), competition (company databases), demand signals (Reddit/HN), and regulatory requirements.
- **APIs used:** BLS, Census Bureau, FRED, Reddit JSON, HN Algolia, Crunchbase, Federal Register, Google Places
- **AI angle:** Claude generates a validation report with market sizing, competitor landscape, demand evidence, and a "viability score." Identifies specific risks and opportunities.
- **Revenue model:** Free for 1 validation, $24.99/mo for entrepreneurs.
- **Competition:** Exploding Topics ($47/mo, trends only), manual research. Comprehensive AI-powered validation from free data sources is unique.

**100. TechDueDiligence — Technical Assessment for M&A**
- **What it does:** Evaluate a target company's technical health: tech stack, open source usage, dependency risks, security posture, and engineering team quality.
- **APIs used:** BuiltWith, GitHub API, Snyk, OSV.dev, npm Registry, StackExchange, Adzuna
- **AI angle:** Claude generates an investor-ready technical assessment: architecture quality signals, technical debt indicators, security risks, and team capability evidence.
- **Revenue model:** $199 per assessment.
- **Competition:** Manual technical due diligence ($10K+). Automated AI assessment covers 60% of the scope at 2% of the cost.

**101. NewsTrader — News-to-Market Signal Converter**
- **What it does:** Monitors breaking news and correlates with market movements in real time. Identifies which stocks are most likely affected by current events.
- **APIs used:** NewsAPI, GNews, GDELT, Alpha Vantage, Finnhub, FRED
- **AI angle:** Claude maps news events to specific tickers and sectors, estimates impact magnitude and direction, and tracks historical accuracy of its predictions.
- **Revenue model:** $39/mo for retail traders.
- **Competition:** Bloomberg Terminal ($thousands), generic news. AI-powered news-to-ticker mapping at consumer price point.

**102. OpenDataExplorer — Government Data Natural Language Interface**
- **What it does:** Ask questions about government data in plain English. AI translates to API queries, fetches data, and generates visual reports.
- **APIs used:** Census Bureau, BLS, FRED, BEA, USASpending, Data.gov, FBI Crime Data, EPA AirNow
- **AI angle:** Claude acts as a "data analyst for hire" — understands natural language questions, queries the right APIs, and presents findings in a narrative format with charts.
- **Revenue model:** Free for 10 queries/month, $19/mo for analysts and journalists.
- **Competition:** Data.gov (raw), FRED (technical). Natural language data querying is a massive accessibility improvement.

**103. InvestorBrief — LP/Investor Update Generator**
- **What it does:** For startup founders: paste your metrics, and AI generates an investor update email with market context, competitive landscape, and forward-looking narrative.
- **APIs used:** FRED, Alpha Vantage, Crunchbase, NewsAPI, BLS
- **AI angle:** Claude contextualizes your metrics against market benchmarks, adds relevant economic indicators, and writes in a confident-but-honest investor communication style.
- **Revenue model:** $29/mo for founders.
- **Competition:** Visible ($79/mo), manual writing. AI-drafted updates with market context save founders hours monthly.

**104. APIMarketplace — API Discovery and Comparison Platform**
- **What it does:** Search and compare APIs for any use case. AI evaluates reliability, pricing, documentation quality, and recommends the best option for your needs.
- **APIs used:** GitHub API (for API repos), npm Registry, PyPI, StackExchange, Reddit JSON, DevDocs.io
- **AI angle:** Claude evaluates API quality beyond marketing pages — checks community sentiment, issue resolution speed, documentation completeness, and generates comparison reports.
- **Revenue model:** Free for developers, affiliate revenue from paid API signups.
- **Competition:** RapidAPI (marketplace), ProgrammableWeb (directory). AI-powered quality assessment and comparison recommendations are new.

**105. SpaceWatch — Space & Astronomy Dashboard**
- **What it does:** Live dashboard with NASA data: near-Earth objects, Mars rover photos, astronomy picture of the day, SpaceX launches, and ISS tracking.
- **APIs used:** NASA APOD, NASA NEO, NASA Mars Rover, Spaceflight News API, Open-Meteo
- **AI angle:** Claude generates educational narratives for each data point, explains asteroid risks in context, and creates weekly "space weather" reports.
- **Revenue model:** Free (ad-supported), $4.99/mo for educators (lesson plan generation).
- **Competition:** NASA website (fragmented), SpaceX tracker (launches only). Unified AI-narrated space dashboard is unique.

**106. GameDiscover — Indie Game Discovery Engine**
- **What it does:** Find new games based on your preferences by analyzing RAWG database, Reddit gaming communities, and HN discussions about game development.
- **APIs used:** RAWG, Reddit JSON, HN Algolia, Board Game Geek, Jikan (anime games)
- **AI angle:** Claude learns your taste profile, identifies hidden gems with high community praise but low visibility, and generates personalized discovery feeds.
- **Revenue model:** Free for users, affiliate links to stores.
- **Competition:** Steam Discovery Queue (platform-locked), Metacritic (score only). Cross-platform AI curation with community signal analysis.

**107. MusicResearch — Sample & Influence Finder**
- **What it does:** Enter an artist or song. AI traces musical influences, identifies similar artists, and maps the creative lineage using MusicBrainz and community data.
- **APIs used:** MusicBrainz, Reddit JSON, Wikipedia API, Wikidata SPARQL, DEV.to
- **AI angle:** Claude generates "creative lineage maps" showing how artists influenced each other, identifies overlooked similar artists, and creates curated listening guides.
- **Revenue model:** Free for music fans, $9.99/mo for music journalists and curators.
- **Competition:** Spotify recommendations (algorithm, no explanation). AI-generated influence narratives and lineage maps are unique.

**108. QuakeAlert — Seismic Activity Monitor**
- **What it does:** Real-time earthquake monitoring with AI-generated impact assessments for specific locations. Explains what each event means for your area.
- **APIs used:** USGS Earthquake, Nominatim, OpenWeatherMap, NewsAPI
- **AI angle:** Claude contextualizes every seismic event: distance from populated areas, historical comparison, aftershock probability, and what you should actually do (or not do).
- **Revenue model:** Free for basic alerts, $4.99/mo for personalized risk assessment.
- **Competition:** USGS (raw data), QuakeFeed (basic). AI-contextualized impact assessment for your specific location is the moat.

**109. BookBrief — AI Book Research Assistant**
- **What it does:** Enter a topic. AI searches Open Library and Archive.org to find relevant books, generates summaries of key texts, and creates a curated reading list.
- **APIs used:** Open Library, Archive.org, Wikipedia API, Wikidata SPARQL, Datamuse
- **AI angle:** Claude generates executive summaries of available books, identifies the "must-read" list for any topic, and creates structured reading plans with time estimates.
- **Revenue model:** Free for 5 searches/month, $9.99/mo for book clubs and researchers.
- **Competition:** Goodreads (social reviews), Blinkist ($15/mo for summaries). This searches across open libraries with AI curation.

**110. InfluenceMap — Social Network Analysis Tool**
- **What it does:** Map influence networks within any niche by analyzing who's mentioned, quoted, and linked across Reddit, HN, DEV.to, and tech news.
- **APIs used:** Reddit JSON, HN Algolia, DEV.to, Product Hunt, Mastodon, Lemmy
- **AI angle:** Claude identifies thought leaders, rising voices, and influence patterns within any topic. Generates "who to follow" lists with reasoning.
- **Revenue model:** $29/mo for marketers and PR teams.
- **Competition:** SparkToro ($50/mo for audience research). Multi-platform influence mapping from free APIs is unique.

**111. FactCheck — AI Claim Verification Tool**
- **What it does:** Paste any claim or statement. AI cross-references Wikipedia, government data, news sources, and academic resources to verify it.
- **APIs used:** Wikipedia API, Wikidata SPARQL, FRED, BLS, Census Bureau, NewsAPI, Open Library
- **AI angle:** Claude traces claims to primary sources, identifies missing context, rates confidence levels, and explains where the claim is accurate vs. misleading.
- **Revenue model:** Free for 10/month, $9.99/mo for journalists and researchers.
- **Competition:** Snopes (manual, slow), PolitiFact (politics only). AI-automated multi-source verification across all topics is new.

**112. TechStackDB — Technology Adoption Tracker**
- **What it does:** Track which technologies companies are adopting or abandoning. Identify trends in tech stack choices across industries.
- **APIs used:** BuiltWith, GitHub API, npm Registry, PyPI, StackExchange, Adzuna (tech in job postings)
- **AI angle:** Claude identifies emerging technology adoption curves, predicts which frameworks will grow or decline, and generates "State of [Technology]" reports.
- **Revenue model:** Free dashboard, $39/mo for custom tracking and reports.
- **Competition:** BuiltWith (raw data), StackOverflow Survey (annual). Real-time AI-analyzed adoption tracking is unique.

**113. WhistleWatch — Corporate Accountability Tracker**
- **What it does:** Monitor companies for accountability signals: SEC violations, environmental complaints, labor disputes, and news sentiment shifts.
- **APIs used:** SEC EDGAR, EPA AirNow, Open Sanctions, NewsAPI, Reddit JSON, Open Corporates
- **AI angle:** Claude identifies patterns that precede corporate scandals, tracks ESG risk indicators, and generates accountability reports for investors and journalists.
- **Revenue model:** $29/mo for investors, $79/mo for journalists.
- **Competition:** MSCI ESG (enterprise), manual research. AI-aggregated multi-source accountability monitoring at consumer pricing.

**114. ConsulateQ — Immigration & Visa Wait Time Tracker**
- **What it does:** Track visa processing times, policy changes, and application requirements across countries using government data and community reports.
- **APIs used:** Federal Register, REST Countries, Reddit JSON, NewsAPI, Data.gov
- **AI angle:** Claude predicts processing times based on historical patterns, explains policy changes in plain English, and identifies the fastest processing paths.
- **Revenue model:** Free for basic info, $14.99/mo for personalized tracking and alerts.
- **Competition:** VisaJourney (forum-based), government websites (hard to navigate). AI-powered prediction and plain-English policy explanation are unique.

**115. CountryRisk — International Business Risk Assessment**
- **What it does:** Assess the risk of doing business in any country: economic stability, regulatory environment, sanctions, currency risk, and political stability.
- **APIs used:** REST Countries, World Bank, FRED, ExchangeRate-API, Open Sanctions, WHO GHO, UN Data
- **AI angle:** Claude generates country risk reports with specific recommendations, compares alternative markets, and tracks risk trend changes with alerts.
- **Revenue model:** $49/mo for SMBs expanding internationally.
- **Competition:** Control Risks ($thousands), Euler Hermes (enterprise). AI-powered country risk at SMB pricing.

**116. DevRelDash — Developer Relations Analytics**
- **What it does:** Track your developer community health: GitHub stars/forks/issues, StackOverflow questions, Reddit mentions, npm downloads, and DEV.to engagement.
- **APIs used:** GitHub API, StackExchange, Reddit JSON, DEV.to, npm Registry, PyPI, HN Algolia
- **AI angle:** Claude identifies community sentiment trends, flags emerging issues before they become crises, and generates weekly DevRel reports with action items.
- **Revenue model:** $49/mo per project tracked.
- **Competition:** Orbit (community management), Common Room ($expensive). AI-powered multi-platform community analytics at indie pricing.

---

## Summary

| Category | Count |
|----------|-------|
| Original Wrapper Tools | 6 |
| SaaS Tools | 7 |
| Content & Media | 7 |
| Business Intelligence & Analytics | 7 |
| Developer Tools & Utilities | 8 |
| Local & Community Tools | 6 |
| Personal Finance & Investing | 6 |
| Health & Wellness | 4 |
| Education & Research | 6 |
| Real Estate & Property | 4 |
| Government & Civic Tech | 6 |
| E-commerce & Retail | 4 |
| HR & Recruiting | 5 |
| Marketing & SEO | 5 |
| Legal & Compliance | 4 |
| Sustainability & Climate | 4 |
| Automation & Productivity | 6 |
| Cross-Category Power Combinations | 21 |
| **Total** | **116** |

## Build Stack

Every idea above is buildable with:
- **Claude Code** — development and AI logic
- **Supabase** — database, auth, edge functions
- **Vercel** — frontend hosting, serverless functions
- **n8n** — workflow automation, API orchestration, scheduled jobs
- **API Catalog** — 190 free APIs across 10 categories
- **HuggingFace** — specialized ML models (NER, sentiment, classification)

## Prioritization Framework

When picking which to build first, score each idea on:

1. **Data moat (1-5):** How hard is this data to get without these free APIs?
2. **AI differentiation (1-5):** How much better is the AI version vs. manual?
3. **Demand signal (1-5):** Are people already searching for this? (Check Google Trends, Reddit)
4. **Build speed (1-5):** Can a solo dev ship an MVP in under 2 weeks?
5. **Revenue clarity (1-5):** Is the monetization obvious and proven?

**Score = sum of all 5.** Anything above 20 is a strong candidate. Build the highest-scoring idea first.
