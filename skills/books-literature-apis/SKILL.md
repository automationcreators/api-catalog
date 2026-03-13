---
name: books-literature-apis
description: Query free book, dictionary, and literature APIs via curl. Reads catalog for endpoints and auth.
---

# Books & Literature APIs Skill

## How to use
When the user invokes `/books-literature-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/books-literature.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| Word definition / meaning | Free Dictionary | No auth, definitions + phonetics + examples |
| Public domain books | Gutendex | No auth, Project Gutenberg catalog |
| Poetry lookup | PoetryDB | No auth, search by author/title/lines |
| Bible verses | Bible-api | No auth, multiple translations |
| Synonyms / thesaurus | Wiktionary | No auth, collaborative dictionary |
| Book metadata search | Crossref Metadata Search | No auth, scholarly metadata |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- If no key needed (Free Dictionary, Gutendex, PoetryDB, Bible-api), proceed directly
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**Free Dictionary (word definitions, no auth):**
```bash
# Look up a word
curl -s "https://api.dictionaryapi.dev/api/v2/entries/en/serendipity" | jq '.[0] | {word, phonetic, meanings: [.meanings[] | {partOfSpeech, definitions: [.definitions[:2][] | .definition]}]}'

# Look up another word
curl -s "https://api.dictionaryapi.dev/api/v2/entries/en/ephemeral" | jq '.[0].meanings[] | {partOfSpeech, definitions: [.definitions[:2][] | .definition]}'
```

**Gutendex (Project Gutenberg books, no auth):**
```bash
# Search books by title
curl -s "https://gutendex.com/books/?search=pride+and+prejudice" | jq '.results[:5] | .[] | {id, title, authors: [.authors[].name], languages, download_count}'

# Search by author
curl -s "https://gutendex.com/books/?search=shakespeare" | jq '.results[:5] | .[] | {title, authors: [.authors[].name], download_count}'

# Get popular books
curl -s "https://gutendex.com/books/?sort=popular" | jq '.results[:5] | .[] | {title, authors: [.authors[].name], download_count}'
```

**PoetryDB (poetry, no auth):**
```bash
# Search by author
curl -s "https://poetrydb.org/author/Emily Dickinson" | jq '.[:3] | .[] | {title, author, linecount}'

# Search by title
curl -s "https://poetrydb.org/title/Sonnet" | jq '.[:3] | .[] | {title, author, lines: .lines[:4]}'

# Get a specific poem
curl -s "https://poetrydb.org/author,title/Shakespeare;Sonnet 18" | jq '.[0] | {title, author, lines}'
```

**Bible-api (Bible verses, no auth):**
```bash
# Get a verse
curl -s "https://bible-api.com/john+3:16" | jq '{reference, text, translation_name}'

# Get a chapter
curl -s "https://bible-api.com/psalm+23" | jq '{reference, text}'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- The specific value(s) requested
- Relevant context (author, year, source)
- Source attribution (which API provided the data)

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **Free Dictionary** | None | Word definitions, phonetics, examples |
| **Gutendex** | None | Project Gutenberg public domain books |
| **PoetryDB** | None | Poetry search by author, title, lines |
| **Bible-api** | None | Bible verses in multiple languages |
| **Crossref Metadata Search** | None | Scholarly book/article metadata |
| **Wiktionary** | None | Collaborative dictionary data |
| **Merriam-Webster** | API key (query param) | Dictionary and thesaurus |
| **Oxford** | API key (query param) | Oxford dictionary data |
| **Wordnik** | API key (query param) | Dictionary with examples |
| **Wizard World** | None | Harry Potter universe data |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| Free Dictionary | Generous, no stated limit |
| Gutendex | No limit |
| PoetryDB | No limit |
| Bible-api | No limit |
| Crossref | Polite pool (include email) |
| Merriam-Webster | 1000 queries/day |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `MERRIAM_WEBSTER_API_KEY` | Merriam-Webster | https://dictionaryapi.com/ |
| `OXFORD_API_KEY` | Oxford | https://developer.oxforddictionaries.com/ |
| `WORDNIK_API_KEY` | Wordnik | https://developer.wordnik.com |
| `COLLINS_API_KEY` | Collins | https://api.collinsdictionary.com/ |
