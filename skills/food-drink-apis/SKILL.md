---
name: food-drink-apis
description: Query free food and drink APIs via curl. Reads catalog for endpoints and auth.
---

# Food & Drink APIs Skill

## How to use
When the user invokes `/food-drink-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/food-drink.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| Meal recipes | TheMealDB | Free test key, recipe search by name/ingredient |
| Cocktail recipes | TheCocktailDB | Free test key, cocktail search |
| Food product data | Open Food Facts | No auth, barcode/product lookup |
| Brewery / beer info | Open Brewery DB | No auth, brewery search by city/state |
| Fruit nutrition data | Fruityvice | No auth, detailed fruit info |
| Beer recipes | PunkAPI | No auth, Brewdog beer recipes |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- TheMealDB and TheCocktailDB have free test API key: `1` for testing
- If no key needed (Open Food Facts, Open Brewery DB, Fruityvice, PunkAPI), proceed directly
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**TheMealDB (meal recipes, free test key "1"):**
```bash
# Search meal by name
curl -s "https://www.themealdb.com/api/json/v1/1/search.php?s=chicken" | jq '.meals[:3] | .[] | {strMeal, strCategory, strArea, strInstructions}'

# Random meal
curl -s "https://www.themealdb.com/api/json/v1/1/random.php" | jq '.meals[0] | {strMeal, strCategory, strInstructions}'

# Filter by ingredient
curl -s "https://www.themealdb.com/api/json/v1/1/filter.php?i=salmon" | jq '.meals[:5] | .[] | {strMeal, strMealThumb}'
```

**TheCocktailDB (cocktails, free test key "1"):**
```bash
# Search cocktail by name
curl -s "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita" | jq '.drinks[:3] | .[] | {strDrink, strCategory, strInstructions, strIngredient1, strIngredient2, strIngredient3}'

# Random cocktail
curl -s "https://www.thecocktaildb.com/api/json/v1/1/random.php" | jq '.drinks[0] | {strDrink, strCategory, strInstructions}'
```

**Open Food Facts (product data, no auth):**
```bash
# Lookup product by barcode
curl -s "https://world.openfoodfacts.org/api/v0/product/737628064502.json" | jq '.product | {product_name, brands, nutriments: {energy_kcal: .nutriments."energy-kcal_100g", fat: .nutriments.fat_100g, sugars: .nutriments.sugars_100g}}'

# Search products
curl -s "https://world.openfoodfacts.org/cgi/search.pl?search_terms=chocolate&json=1&page_size=5" | jq '.products[:5] | .[] | {product_name, brands}'
```

**Open Brewery DB (breweries, no auth):**
```bash
# Search breweries by city
curl -s "https://api.openbrewerydb.org/v1/breweries?by_city=portland&per_page=5" | jq '.[] | {name, city, state, brewery_type, website_url}'

# Search by name
curl -s "https://api.openbrewerydb.org/v1/breweries?by_name=sierra+nevada&per_page=5" | jq '.'
```

**Fruityvice (fruit data, no auth):**
```bash
# Get fruit info
curl -s "https://www.fruityvice.com/api/fruit/banana" | jq '{name, family, nutritions}'

# Get all fruits
curl -s "https://www.fruityvice.com/api/fruit/all" | jq '.[:5] | .[] | {name, family, nutritions: {calories, sugar, carbohydrates}}'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- The specific value(s) requested
- Relevant context (ingredients, nutrition, location)
- Source attribution (which API provided the data)

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **TheMealDB** | API key (free test: "1") | Meal recipes, ingredients, categories |
| **TheCocktailDB** | API key (free test: "1") | Cocktail recipes, ingredients |
| **Open Food Facts** | None | Food product data, barcode lookup, nutrition |
| **Open Brewery DB** | None | Brewery search by location/name |
| **Fruityvice** | None | Fruit nutrition data |
| **PunkAPI** | None | Brewdog beer recipes |
| **Spoonacular** | API key (query param) | Recipes, meal planning, nutrition |
| **Edamam** | API key (query param) | Nutrition analysis, recipe search |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| TheMealDB | Free test key unlimited |
| TheCocktailDB | Free test key unlimited |
| Open Food Facts | No limit |
| Open Brewery DB | No limit |
| Fruityvice | No limit |
| PunkAPI | No limit |
| Spoonacular | 150 points/day |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `SPOONACULAR_API_KEY` | Spoonacular | https://spoonacular.com/food-api |
| `EDAMAM_NUTRITION_API_KEY` | Edamam | https://developer.edamam.com/ |
| `EDAMAM_RECIPES_API_KEY` | Edamam Recipes | https://developer.edamam.com/ |
