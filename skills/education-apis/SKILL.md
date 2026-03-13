---
name: education-apis
description: Query free education APIs via curl. Reads catalog for endpoints and auth.
---

# Education APIs Skill

## How to use
When the user invokes `/education-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/education.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| Word definitions | Free Dictionary API | No auth, definitions + phonetics + examples |
| Wikipedia summaries | Wikipedia REST API | No auth, instant article summaries |
| Trivia / quiz questions | Open Trivia DB | No auth, customizable categories |
| Academic paper search | Semantic Scholar | No auth, citation graphs and author info |
| Research paper lookup | arXiv API or CrossRef | No auth, scholarly metadata |
| Number/date facts | Numbers API | No auth, fun facts about numbers |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- If no key needed (Free Dictionary, Wikipedia, Open Trivia DB, Semantic Scholar), proceed directly
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**Free Dictionary API (definitions, no auth):**
```bash
# Look up a word
curl -s "https://api.dictionaryapi.dev/api/v2/entries/en/serendipity" | jq '.[0] | {word, phonetic, meanings: [.meanings[] | {partOfSpeech, definitions: [.definitions[:2][] | .definition]}]}'
```

**Wikipedia REST API (article summaries, no auth):**
```bash
# Get article summary
curl -s "https://en.wikipedia.org/api/rest_v1/page/summary/Machine_learning" | jq '{title, description, extract}'

# Get featured article of the day
curl -s "https://en.wikipedia.org/api/rest_v1/feed/featured/2026/03/12" | jq '.tfa | {title, description, extract}'
```

**Open Trivia DB (trivia questions, no auth):**
```bash
# Get trivia questions (category 18 = computers)
curl -s "https://opentdb.com/api.php?amount=5&category=18&type=multiple" | jq '.results[] | {category, difficulty, question, correct_answer}'

# Get random trivia
curl -s "https://opentdb.com/api.php?amount=5&type=multiple" | jq '.results[] | {category, question, correct_answer, incorrect_answers}'

# List available categories
curl -s "https://opentdb.com/api_category.php" | jq '.trivia_categories[] | {id, name}'
```

**Semantic Scholar (academic papers, no auth):**
```bash
# Search papers
curl -s "https://api.semanticscholar.org/graph/v1/paper/search?query=large+language+models&limit=5" | jq '.data[] | {title, year, citationCount}'

# Get paper details by ID
curl -s "https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b?fields=title,abstract,year,citationCount" | jq '{title, year, citationCount, abstract}'
```

**Numbers API (number facts, no auth):**
```bash
# Trivia fact about a number
curl -s "http://numbersapi.com/42/trivia?json" | jq '.'

# Math fact
curl -s "http://numbersapi.com/1729/math?json" | jq '.'

# Date fact
curl -s "http://numbersapi.com/3/12/date?json" | jq '.'
```

**CrossRef (scholarly metadata, no auth):**
```bash
# Search works
curl -s "https://api.crossref.org/works?query=deep+learning&rows=5" | jq '.message.items[:3] | .[] | {title: .title[0], DOI, published: .published."date-parts"[0]}'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- The specific value(s) requested
- Relevant context (definitions, citations, sources)
- Source attribution (which API provided the data)

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **Free Dictionary API** | None | Word definitions, phonetics, examples |
| **Wikipedia REST API** | None | Article summaries, featured content |
| **Open Trivia DB** | None | Trivia questions by category/difficulty |
| **Semantic Scholar** | None | Academic paper search, citations |
| **Numbers API** | None | Facts about numbers and dates |
| **arXiv API** | None | Research preprint search |
| **CrossRef** | None | DOI and scholarly metadata lookup |
| **Merriam-Webster** | API key (query param) | Dictionary and thesaurus |
| **Quotable** | None | Random quotes from famous people |
| **PoetryDB** | None | Poetry search by author/title |
| **Gutendex** | None | Project Gutenberg book search |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| Free Dictionary API | Generous limits |
| Wikipedia REST API | 200 requests/second |
| Open Trivia DB | 1 request/5 seconds |
| Semantic Scholar | 100 requests/5 minutes |
| Numbers API | Unlimited |
| arXiv API | 3 second wait between requests |
| CrossRef | Polite pool (include email) |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `MERRIAM_WEBSTER_API_KEY` | Merriam-Webster | https://dictionaryapi.com/register |
