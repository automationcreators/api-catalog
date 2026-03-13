---
name: shopping-apis
description: Query free shopping and e-commerce APIs via curl. Reads catalog for endpoints and auth.
---

# Shopping APIs Skill

## How to use
When the user invokes `/shopping-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/shopping.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| Product search / reviews | Best Buy | Free API key, products and recommendations |
| Dummy product data | Dummy Products | Test data for development |
| Electronic components | Octopart | Electronic part search and pricing |
| Fake Store (testing) | Fake Store API | No auth, mock e-commerce data |
| WooCommerce integration | WooCommerce | REST API for WordPress stores |
| Barcode lookup | UPC Database | Product data by barcode |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- Fake Store API needs no auth and is great for testing
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**Fake Store API (mock e-commerce, no auth):**
```bash
# Get all products
curl -s "https://fakestoreapi.com/products?limit=5" | jq '.[] | {id, title, price, category, rating: .rating.rate}'

# Get product by ID
curl -s "https://fakestoreapi.com/products/1" | jq '{title, price, description, category, image}'

# Get product categories
curl -s "https://fakestoreapi.com/products/categories" | jq '.'

# Get products in a category
curl -s "https://fakestoreapi.com/products/category/electronics" | jq '.[] | {title, price, rating: .rating.rate}'
```

**Best Buy (product data, API key required):**
```bash
# Search products
curl -s "https://api.bestbuy.com/v1/products(search=laptop)?apiKey=$BEST_BUY_API_KEY&format=json&show=sku,name,salePrice,customerReviewAverage&pageSize=5" | jq '.products[] | {name, salePrice, customerReviewAverage}'

# Get product categories
curl -s "https://api.bestbuy.com/v1/categories?apiKey=$BEST_BUY_API_KEY&format=json&pageSize=10" | jq '.categories[] | {id, name}'
```

**DummyJSON (mock products, no auth):**
```bash
# Get products
curl -s "https://dummyjson.com/products?limit=5" | jq '.products[] | {title, price, brand, category, rating}'

# Search products
curl -s "https://dummyjson.com/products/search?q=phone" | jq '.products[] | {title, price, brand, rating}'

# Get product categories
curl -s "https://dummyjson.com/products/categories" | jq '.'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- The specific value(s) requested
- Relevant context (prices, ratings, availability)
- Source attribution (which API provided the data)

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **Fake Store API** | None | Mock e-commerce data for testing |
| **DummyJSON** | None | Mock products, carts, users for testing |
| **Best Buy** | API key (query param) | Real product search, prices, reviews |
| **Octopart** | API key (query param) | Electronic component search |
| **WooCommerce** | API key | WordPress e-commerce integration |
| **Shopee** | API key (query param) | Shopee marketplace integration |
| **Mercadolibre** | API key (query param) | Latin American marketplace |
| **Lazada** | API key (query param) | Southeast Asian marketplace |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| Fake Store API | No limit |
| DummyJSON | No limit |
| Best Buy | 5 calls/second |
| Octopart | See docs |
| WooCommerce | Depends on hosting |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `BEST_BUY_API_KEY` | Best Buy | https://developer.bestbuy.com/ |
| `OCTOPART_API_KEY` | Octopart | https://octopart.com/api/v4/reference |
| `WOOCOMMERCE_API_KEY` | WooCommerce | Generated in WordPress admin |
