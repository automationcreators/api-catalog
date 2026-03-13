---
name: photography-media-apis
description: Query free photography and media APIs via curl. Reads catalog for endpoints and auth.
---

# Photography & Media APIs Skill

## How to use
When the user invokes `/photography-media-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/photography-media.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| Art museum collections | Art Institute of Chicago or Met Museum | No auth, rich art metadata |
| Placeholder images | Lorem Picsum | No auth, Unsplash-quality placeholders |
| Color palettes | Colormind or ColourLovers | No auth, color scheme generation |
| GIF search | Giphy | API key, massive GIF library |
| Stock photos | Pexels or Pixabay | Free API key, high-quality photos |
| Website favicons | Icon Horse | No auth, instant favicons |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- If no key needed (Art Institute of Chicago, Met Museum, Lorem Picsum, Colormind), proceed directly
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**Art Institute of Chicago (art data, no auth):**
```bash
# Search artworks
curl -s "https://api.artic.edu/api/v1/artworks/search?q=monet&limit=5" | jq '.data[] | {id, title, artist_display, date_display}'

# Get artwork details
curl -s "https://api.artic.edu/api/v1/artworks/27992" | jq '.data | {title, artist_display, date_display, medium_display, dimensions}'

# Browse artworks
curl -s "https://api.artic.edu/api/v1/artworks?limit=5&fields=id,title,artist_display,image_id" | jq '.data[] | {title, artist_display, image_url: ("https://www.artic.edu/iiif/2/" + .image_id + "/full/843,/0/default.jpg")}'
```

**Metropolitan Museum of Art (art data, no auth):**
```bash
# Search objects
curl -s "https://collectionapi.metmuseum.org/public/collection/v1/search?q=sunflowers" | jq '{total, objectIDs: .objectIDs[:5]}'

# Get object details
curl -s "https://collectionapi.metmuseum.org/public/collection/v1/objects/436535" | jq '{title, artistDisplayName, objectDate, medium, department, primaryImage}'
```

**Colormind (color palette, no auth):**
```bash
# Generate a random color palette
curl -s -X POST "http://colormind.io/api/" -d '{"model":"default"}' | jq '.'

# Generate palette with a seed color
curl -s -X POST "http://colormind.io/api/" -d '{"input":[[44,43,44],"N","N","N","N"],"model":"default"}' | jq '.'
```

**Lorem Picsum (placeholder images, no auth):**
```bash
# Get random image info
curl -s "https://picsum.photos/v2/list?page=1&limit=5" | jq '.[] | {id, author, width, height, download_url}'

# Get specific image info
curl -s "https://picsum.photos/id/237/info" | jq '.'
```

**Icon Horse (favicons, no auth):**
```bash
# Get favicon URL (direct image URL)
echo "https://icon.horse/icon/github.com"
echo "https://icon.horse/icon/google.com"
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- The specific value(s) requested
- Relevant context (artist, dimensions, colors)
- Source attribution (which API provided the data)

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **Art Institute of Chicago** | None | Artwork search, museum collection data |
| **Metropolitan Museum of Art** | None | Met collection search, object details |
| **Lorem Picsum** | None | Placeholder images from Unsplash |
| **Colormind** | None | AI color palette generation |
| **ColourLovers** | None | Community color palettes and patterns |
| **Icon Horse** | None | Website favicons |
| **Giphy** | API key (query param) | GIF search and trending |
| **Pexels** | API key (query param) | Free stock photos and videos |
| **Pixabay** | API key (query param) | Free stock photography |
| **Rijksmuseum** | API key (query param) | Rijksmuseum collection data |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| Art Institute of Chicago | 60 requests/minute |
| Metropolitan Museum of Art | 80 requests/second |
| Lorem Picsum | No stated limit |
| Colormind | No stated limit |
| Giphy | See docs |
| Pexels | 200 requests/hour |
| Pixabay | 100 requests/minute |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `GIPHY_API_KEY` | Giphy | https://developers.giphy.com/dashboard/ |
| `PEXELS_API_KEY` | Pexels | https://www.pexels.com/api/ |
| `PIXABAY_API_KEY` | Pixabay | https://pixabay.com/api/docs/ |
| `RIJKSMUSEUM_API_KEY` | Rijksmuseum | https://data.rijksmuseum.nl/object-metadata/api/ |
| `HARVARD_ART_MUSEUMS_API_KEY` | Harvard Art Museums | https://github.com/harvardartmuseums/api-docs |
