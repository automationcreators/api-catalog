---
name: social-apis
description: Query free social/community APIs via curl. Reads catalog for endpoints and auth.
---

# Social APIs Skill

## How to use
When the user invokes `/social-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/social.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| Reddit posts/discussions | Reddit JSON API | No auth for read-only |
| Hacker News stories/comments | HN Algolia API | Fast search, no auth |
| Product Hunt launches | Product Hunt (unofficial) | New product launches |
| Dev.to articles | Dev.to API | Developer blog posts |
| Lobsters stories | Lobsters API | Curated tech links |
| Stack Overflow questions | Stack Exchange API | Q&A, programming help |
| Trending topics in tech | HN + Reddit combined | Multiple signal sources |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- Most social APIs listed here require no auth for read access
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**Reddit JSON API (no auth for public subreddits):**
```bash
# Top posts from a subreddit
curl -s "https://www.reddit.com/r/programming/top.json?t=day&limit=5" -H "User-Agent: ClaudeCode/1.0" | jq '.data.children[:5] | .[] | .data | {title, score, num_comments, url}'

# Hot posts from a subreddit
curl -s "https://www.reddit.com/r/artificial/hot.json?limit=5" -H "User-Agent: ClaudeCode/1.0" | jq '.data.children[:5] | .[] | .data | {title, score, num_comments, url, selftext: .selftext[:200]}'

# Search Reddit
curl -s "https://www.reddit.com/search.json?q=claude+code&sort=relevance&t=week&limit=5" -H "User-Agent: ClaudeCode/1.0" | jq '.data.children[:5] | .[] | .data | {title, subreddit, score, url}'

# Subreddit info
curl -s "https://www.reddit.com/r/MachineLearning/about.json" -H "User-Agent: ClaudeCode/1.0" | jq '.data | {display_name, subscribers, public_description}'
```

**Hacker News Algolia API (no auth):**
```bash
# Search HN stories
curl -s "https://hn.algolia.com/api/v1/search?query=AI+agents&tags=story" | jq '.hits[:5] | .[] | {title, points, num_comments, url}'

# Front page stories
curl -s "https://hn.algolia.com/api/v1/search?tags=front_page" | jq '.hits[:10] | .[] | {title, points, num_comments, url}'

# Recent stories sorted by date
curl -s "https://hn.algolia.com/api/v1/search_by_date?tags=story&query=rust" | jq '.hits[:5] | .[] | {title, points, created_at}'

# Search Show HN posts
curl -s "https://hn.algolia.com/api/v1/search?tags=show_hn&query=saas" | jq '.hits[:5] | .[] | {title, points, num_comments, url}'

# Search Ask HN posts
curl -s "https://hn.algolia.com/api/v1/search?tags=ask_hn&query=startup" | jq '.hits[:5] | .[] | {title, points, num_comments}'

# Get a specific item with comments
curl -s "https://hn.algolia.com/api/v1/items/12345" | jq '{title, points, children: [.children[:3][] | {text: .text[:200], author}]}'
```

**Hacker News Official API (no auth):**
```bash
# Top story IDs
curl -s "https://hacker-news.firebaseio.com/v0/topstories.json" | jq '.[:10]'

# Get story details by ID
curl -s "https://hacker-news.firebaseio.com/v0/item/12345.json" | jq '{title, score, url, by, descendants}'

# New stories
curl -s "https://hacker-news.firebaseio.com/v0/newstories.json" | jq '.[:5]'

# Best stories
curl -s "https://hacker-news.firebaseio.com/v0/beststories.json" | jq '.[:10]'
```

**Dev.to API (no auth for reading):**
```bash
# Top articles (last 7 days)
curl -s "https://dev.to/api/articles?top=7&per_page=5" | jq '.[:5] | .[] | {title, user: .user.username, positive_reactions_count, comments_count, url, tag_list}'

# Search articles by tag
curl -s "https://dev.to/api/articles?tag=ai&per_page=5" | jq '.[:5] | .[] | {title, user: .user.username, positive_reactions_count, url}'

# Latest articles
curl -s "https://dev.to/api/articles?per_page=5" | jq '.[:5] | .[] | {title, user: .user.username, published_at, tag_list}'

# Articles by username
curl -s "https://dev.to/api/articles?username=ben&per_page=5" | jq '.[:5] | .[] | {title, positive_reactions_count, comments_count}'
```

**Stack Exchange API (no auth for basic):**
```bash
# Search questions on Stack Overflow
curl -s "https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=relevance&q=python+async&site=stackoverflow&pagesize=5" | jq '.items[:5] | .[] | {title, score, answer_count, is_answered, link}'

# Hot questions across all sites
curl -s "https://api.stackexchange.com/2.3/questions?order=desc&sort=hot&site=stackoverflow&pagesize=5" | jq '.items[:5] | .[] | {title, score, answer_count, view_count}'

# Questions by tag
curl -s "https://api.stackexchange.com/2.3/questions?order=desc&sort=votes&tagged=claude&site=stackoverflow&pagesize=5" | jq '.items[:5] | .[] | {title, score, answer_count, link}'

# Trending tags
curl -s "https://api.stackexchange.com/2.3/tags?order=desc&sort=popular&site=stackoverflow&pagesize=10" | jq '.items[:10] | .[] | {name, count}'
```

**Lobsters (no auth):**
```bash
# Hottest stories
curl -s "https://lobste.rs/hottest.json" | jq '.[:5] | .[] | {title, score, comment_count, url, tags}'

# Newest stories
curl -s "https://lobste.rs/newest.json" | jq '.[:5] | .[] | {title, score, url, tags}'

# Stories by tag
curl -s "https://lobste.rs/t/ai.json" | jq '.[:5] | .[] | {title, score, comment_count, url}'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- Post/article title
- Engagement metrics (score, comments, reactions)
- Source community
- URLs for further reading

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **Reddit JSON** | None (User-Agent required) | Subreddit posts, discussions, search |
| **HN Algolia** | None | HN story search, front page, comments |
| **HN Official** | None | Top/new/best story IDs, item details |
| **Dev.to** | None (reading) | Developer blog posts, tag-based browsing |
| **Stack Exchange** | None (basic) | Programming Q&A, hot questions |
| **Lobsters** | None | Curated tech/programming links |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| Reddit JSON | ~60 requests/minute (with User-Agent) |
| HN Algolia | 10,000 requests/hour |
| HN Official | No published limit |
| Dev.to | 30 requests/30 seconds |
| Stack Exchange | 300 requests/day (no key), 10,000/day (with key) |
| Lobsters | No published limit (be reasonable) |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `STACKEXCHANGE_KEY` | Stack Exchange (optional) | https://stackapps.com/apps/oauth/register |

Most social APIs in this catalog require no authentication for read access.
