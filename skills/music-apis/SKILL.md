---
name: music-apis
description: Query free music APIs via curl. Reads catalog for endpoints and auth.
---

# Music APIs Skill

## How to use
When the user invokes `/music-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/music.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| Song lyrics | Lyrics.ovh | No auth, simple artist/title lookup |
| Artist info / similar artists | TasteDive or LastFm | Recommendations and metadata |
| Music search (iTunes) | iTunes Search | No auth, broad catalog |
| Internet radio stations | Radio Browser | No auth, global station list |
| Song tabs / chords | Songsterr | No auth, guitar/bass/drums tabs |
| Music genre discovery | Genrenator | No auth, random genre generator |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- If no key needed (Lyrics.ovh, iTunes Search, Radio Browser, Songsterr), proceed directly
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**Lyrics.ovh (lyrics, no auth):**
```bash
# Get lyrics for a song
curl -s "https://api.lyrics.ovh/v1/Radiohead/Creep" | jq '.lyrics' | head -20
```

**iTunes Search (music search, no auth):**
```bash
# Search for songs
curl -s "https://itunes.apple.com/search?term=bohemian+rhapsody&media=music&limit=5" | jq '.results[] | {trackName, artistName, collectionName, releaseDate}'

# Search for albums
curl -s "https://itunes.apple.com/search?term=pink+floyd&entity=album&limit=5" | jq '.results[] | {collectionName, artistName, releaseDate, trackCount}'
```

**Radio Browser (internet radio, no auth):**
```bash
# Search radio stations by name
curl -s "https://de1.api.radio-browser.info/json/stations/byname/jazz?limit=5" | jq '.[] | {name, url, country, tags, bitrate}'

# Get top-voted stations
curl -s "https://de1.api.radio-browser.info/json/stations/topvote?limit=10" | jq '.[] | {name, country, tags, votes}'
```

**LastFm (artist info, API key required):**
```bash
# Get artist info
curl -s "https://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=Radiohead&api_key=$LASTFM_API_KEY&format=json" | jq '.artist | {name, stats, tags}'

# Get similar artists
curl -s "https://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist=Radiohead&api_key=$LASTFM_API_KEY&format=json&limit=5" | jq '.similarartists.artist[] | {name, match}'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- The specific value(s) requested
- Relevant context (artist, album, release date)
- Source attribution (which API provided the data)

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **Lyrics.ovh** | None | Song lyrics lookup by artist/title |
| **iTunes Search** | None | Music, album, and artist search |
| **Radio Browser** | None | Internet radio station directory |
| **LastFm** | API key (query param) | Artist info, similar artists, top tracks |
| **TasteDive** | API key (query param) | Similar artist/movie/show recommendations |
| **Songsterr** | None | Guitar, bass, and drums tabs/chords |
| **Genrenator** | None | Random music genre generator |
| **TheAudioDB** | API key (query param) | Music metadata and artwork |
| **Musixmatch** | API key (query param) | Lyrics and music metadata |
| **Freesound** | API key (query param) | Sound samples and effects |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| Lyrics.ovh | See docs |
| iTunes Search | ~20 calls/minute |
| Radio Browser | No limit |
| LastFm | See docs |
| TasteDive | See docs |
| Musixmatch | 2000 calls/day |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `LASTFM_API_KEY` | LastFm | https://www.last.fm/api/account/create |
| `TASTEDIVE_API_KEY` | TasteDive | https://tastedive.com/read/api |
| `MUSIXMATCH_API_KEY` | Musixmatch | https://developer.musixmatch.com/ |
| `THEAUDIODB_API_KEY` | TheAudioDB | https://www.theaudiodb.com/api_guide.php |
| `FREESOUND_API_KEY` | Freesound | https://freesound.org/apiv2/apply |
