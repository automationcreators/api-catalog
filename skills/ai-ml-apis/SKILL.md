---
name: ai-ml-apis
description: Query free AI/ML APIs via curl. Reads catalog for endpoints and auth.
---

# AI/ML APIs Skill

## How to use
When the user invokes `/ai-ml-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/ai-ml.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| Text translation | LibreTranslate or MyMemory | Free, no auth options |
| Language detection | LibreTranslate or DetectLanguage | Identify unknown text |
| Text-to-speech | VoiceRSS | Multiple languages/voices |
| Sentiment analysis | Text-Processing.com | Simple, no auth |
| Image classification/description | Hugging Face Inference | Broad model selection |
| Text generation/summarization | Hugging Face Inference | Free tier available |
| OCR (image to text) | OCR.space | Free tier, no auth needed |
| Spell check | LanguageTool | Grammar + spelling, no auth |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- If no key needed, proceed directly
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**Hugging Face Inference API:**
```bash
# Text generation
curl -s "https://api-inference.huggingface.co/models/gpt2" -H "Authorization: Bearer $HUGGINGFACE_TOKEN" -H "Content-Type: application/json" -d '{"inputs":"The future of AI is"}' | jq '.'

# Summarization
curl -s "https://api-inference.huggingface.co/models/facebook/bart-large-cnn" -H "Authorization: Bearer $HUGGINGFACE_TOKEN" -H "Content-Type: application/json" -d '{"inputs":"Long article text here..."}' | jq '.[0].summary_text'

# Sentiment analysis
curl -s "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english" -H "Authorization: Bearer $HUGGINGFACE_TOKEN" -H "Content-Type: application/json" -d '{"inputs":"I love building with Claude Code!"}' | jq '.'

# Zero-shot classification
curl -s "https://api-inference.huggingface.co/models/facebook/bart-large-mnli" -H "Authorization: Bearer $HUGGINGFACE_TOKEN" -H "Content-Type: application/json" -d '{"inputs":"I want to buy a new laptop","parameters":{"candidate_labels":["technology","sports","politics"]}}' | jq '.'

# Question answering
curl -s "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2" -H "Authorization: Bearer $HUGGINGFACE_TOKEN" -H "Content-Type: application/json" -d '{"inputs":{"question":"What is the capital of France?","context":"France is a country in Europe. Its capital is Paris."}}' | jq '.'

# Text embeddings
curl -s "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2" -H "Authorization: Bearer $HUGGINGFACE_TOKEN" -H "Content-Type: application/json" -d '{"inputs":"This is a test sentence"}' | jq '.[0][:5]'
```

**LibreTranslate (translation, self-hosted or public instances):**
```bash
# Translate text
curl -s "https://libretranslate.com/translate" -H "Content-Type: application/json" -d '{"q":"Hello, how are you?","source":"en","target":"es"}' | jq '.translatedText'

# Detect language
curl -s "https://libretranslate.com/detect" -H "Content-Type: application/json" -d '{"q":"Bonjour le monde"}' | jq '.[0] | {language, confidence}'

# List supported languages
curl -s "https://libretranslate.com/languages" | jq '.[] | {code, name}'
```

**MyMemory Translation (no auth):**
```bash
# Translate text (no auth, 5000 chars/day)
curl -s "https://api.mymemory.translated.net/get?q=Hello+world&langpair=en|es" | jq '{translation: .responseData.translatedText, match: .responseData.match}'

# Translate with email for higher limits
curl -s "https://api.mymemory.translated.net/get?q=Good+morning&langpair=en|fr&de=your@email.com" | jq '.responseData.translatedText'
```

**LanguageTool (grammar/spell check, no auth):**
```bash
# Check text for errors
curl -s "https://api.languagetool.org/v2/check" --data-urlencode "text=This is a sentece with erors." --data "language=en-US" | jq '.matches[:5] | .[] | {message, shortMessage, offset, length, replacements: [.replacements[:3][].value]}'

# Check in another language
curl -s "https://api.languagetool.org/v2/check" --data-urlencode "text=Je suis alle au magasin." --data "language=fr" | jq '.matches[] | {message, replacements: [.replacements[:3][].value]}'

# List supported languages
curl -s "https://api.languagetool.org/v2/languages" | jq '.[:10] | .[] | {name, code}'
```

**OCR.space (image to text):**
```bash
# OCR from URL
curl -s "https://api.ocr.space/parse/imageurl?apikey=$OCR_SPACE_KEY&url=https://example.com/image.png" | jq '.ParsedResults[0].ParsedText'

# OCR from file
curl -s "https://api.ocr.space/parse/image" -F "apikey=$OCR_SPACE_KEY" -F "file=@/path/to/image.png" | jq '.ParsedResults[0].ParsedText'

# OCR with language hint
curl -s "https://api.ocr.space/parse/imageurl?apikey=$OCR_SPACE_KEY&url=https://example.com/image.png&language=eng&isOverlayRequired=false" | jq '.ParsedResults[0].ParsedText'
```

**Text-Processing.com (NLP, no auth):**
```bash
# Sentiment analysis
curl -s "http://text-processing.com/api/sentiment/" -d "text=I love this product, it is amazing!" | jq '.'

# Stemming
curl -s "http://text-processing.com/api/stem/" -d "text=running walked flying" | jq '.'

# Part-of-speech tagging
curl -s "http://text-processing.com/api/tag/" -d "text=The quick brown fox jumps" | jq '.'
```

**VoiceRSS (text-to-speech):**
```bash
# Generate speech (returns audio data)
curl -s "https://api.voicerss.org/?key=$VOICERSS_KEY&hl=en-us&src=Hello+world&c=MP3" -o /tmp/speech.mp3
echo "Audio saved to /tmp/speech.mp3"

# List supported languages
echo "Common codes: en-us, en-gb, es-es, fr-fr, de-de, ja-jp, zh-cn"
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- The AI/ML result (translation, sentiment, classification, etc.)
- Confidence scores where available
- Model name used
- Any relevant metadata

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **Hugging Face Inference** | Bearer token (header) | Text generation, summarization, sentiment, embeddings |
| **LibreTranslate** | None or API key | Translation, language detection |
| **MyMemory** | None | Quick translation (no auth) |
| **LanguageTool** | None | Grammar and spell checking |
| **OCR.space** | API key (query/form) | Image to text (OCR) |
| **Text-Processing.com** | None | Sentiment analysis, NLP |
| **VoiceRSS** | API key (query param) | Text-to-speech audio generation |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| Hugging Face | Rate-limited, queue-based (free tier) |
| LibreTranslate | Varies by instance (public: ~20/min) |
| MyMemory | 5,000 characters/day (no auth), 50k with email |
| LanguageTool | 20 requests/minute (public API) |
| OCR.space | 25,000 requests/month |
| Text-Processing.com | 1,000 calls/day per IP |
| VoiceRSS | 350 requests/day |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `HUGGINGFACE_TOKEN` | Hugging Face | https://huggingface.co/settings/tokens |
| `OCR_SPACE_KEY` | OCR.space | https://ocr.space/ocrapi/freekey |
| `VOICERSS_KEY` | VoiceRSS | https://www.voicerss.org/registration.aspx |

## Popular Hugging Face Models
- `gpt2` - Text generation
- `facebook/bart-large-cnn` - Summarization
- `distilbert-base-uncased-finetuned-sst-2-english` - Sentiment
- `facebook/bart-large-mnli` - Zero-shot classification
- `deepset/roberta-base-squad2` - Question answering
- `sentence-transformers/all-MiniLM-L6-v2` - Text embeddings
- `openai/whisper-large-v3` - Speech-to-text
