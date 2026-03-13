#!/usr/bin/env python3
"""
Enrich well-known APIs in new categories with real endpoints.
Sets tier 1 (2+ endpoints) or tier 2 (1 endpoint).
"""

import json
import os

CATEGORIES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "categories")

# Enrichment data: category → {api_name: {fields_to_update}}
ENRICHMENTS = {
    "animals-nature": {
        "Dog CEO": {
            "base_url": "https://dog.ceo/api",
            "docs_url": "https://dog.ceo/dog-api/",
            "tier": 1,
            "endpoints": [
                {"path": "/breeds/image/random", "method": "GET", "desc": "Get a random dog image", "example": "curl 'https://dog.ceo/api/breeds/image/random'"},
                {"path": "/breed/{breed}/images/random/3", "method": "GET", "desc": "Get 3 random images of a specific breed", "example": "curl 'https://dog.ceo/api/breed/husky/images/random/3'"}
            ]
        },
        "Cat Facts": {
            "base_url": "https://catfact.ninja",
            "docs_url": "https://catfact.ninja/",
            "tier": 2,
            "endpoints": [
                {"path": "/fact", "method": "GET", "desc": "Get a random cat fact", "example": "curl 'https://catfact.ninja/fact'"}
            ]
        },
        "HTTP Cat": {
            "base_url": "https://http.cat",
            "docs_url": "https://http.cat/",
            "tier": 2,
            "endpoints": [
                {"path": "/{status_code}", "method": "GET", "desc": "Get a cat image for an HTTP status code", "example": "curl -o cat404.jpg 'https://http.cat/404'"}
            ]
        },
        "RandomFox": {
            "base_url": "https://randomfox.ca",
            "docs_url": "https://randomfox.ca/",
            "tier": 2,
            "endpoints": [
                {"path": "/floof/", "method": "GET", "desc": "Get a random fox image URL", "example": "curl 'https://randomfox.ca/floof/'"}
            ]
        },
        "Petfinder": {
            "base_url": "https://api.petfinder.com/v2",
            "docs_url": "https://www.petfinder.com/developers/v2/docs/",
            "tier": 2,
            "endpoints": [
                {"path": "/animals?type=dog&location=85001&distance=25", "method": "GET", "desc": "Search adoptable pets near a location", "example": "curl -H 'Authorization: Bearer $PETFINDER_TOKEN' 'https://api.petfinder.com/v2/animals?type=dog&location=85001&distance=25'"}
            ]
        },
        "IUCN": {
            "base_url": "https://apiv3.iucnredlist.org/api/v3",
            "docs_url": "https://apiv3.iucnredlist.org/api/v3/docs",
            "tier": 2,
            "endpoints": [
                {"path": "/species/page/0?token={key}", "method": "GET", "desc": "List threatened species (paginated)", "example": "curl 'https://apiv3.iucnredlist.org/api/v3/species/page/0?token=$IUCN_API_KEY'"}
            ]
        },
        "FishWatch": {
            "base_url": "https://www.fishwatch.gov/api",
            "docs_url": "https://www.fishwatch.gov/developers",
            "tier": 2,
            "endpoints": [
                {"path": "/species", "method": "GET", "desc": "Get all species with sustainability info", "example": "curl 'https://www.fishwatch.gov/api/species'"}
            ]
        }
    },
    "books-literature": {
        "Google Books": {
            "name": "Google Books",
            "base_url": "https://www.googleapis.com/books/v1",
            "docs_url": "https://developers.google.com/books/docs/v1/using",
            "auth": "none",
            "tier": 1,
            "endpoints": [
                {"path": "/volumes?q={query}&maxResults=5", "method": "GET", "desc": "Search books by title, author, or ISBN", "example": "curl 'https://www.googleapis.com/books/v1/volumes?q=python+programming&maxResults=5'"},
                {"path": "/volumes/{volumeId}", "method": "GET", "desc": "Get detailed book info by volume ID", "example": "curl 'https://www.googleapis.com/books/v1/volumes/s1gVAAAAYAAJ'"}
            ]
        },
        "Open Library": {
            "base_url": "https://openlibrary.org",
            "docs_url": "https://openlibrary.org/developers/api",
            "tier": 1,
            "endpoints": [
                {"path": "/search.json?q={query}&limit=5", "method": "GET", "desc": "Search books by title or author", "example": "curl 'https://openlibrary.org/search.json?q=lord+of+the+rings&limit=5'"},
                {"path": "/isbn/{isbn}.json", "method": "GET", "desc": "Get book by ISBN", "example": "curl 'https://openlibrary.org/isbn/9780140328721.json'"}
            ]
        },
        "PoetryDB": {
            "base_url": "https://poetrydb.org",
            "docs_url": "https://github.com/thundercomb/poetrydb",
            "tier": 1,
            "endpoints": [
                {"path": "/author/{author}", "method": "GET", "desc": "Get poems by author", "example": "curl 'https://poetrydb.org/author/Emily%20Dickinson'"},
                {"path": "/random/1", "method": "GET", "desc": "Get a random poem", "example": "curl 'https://poetrydb.org/random/1'"}
            ]
        }
    },
    "food-drink": {
        "TheMealDB": {
            "name": "TheMealDB",
            "base_url": "https://www.themealdb.com/api/json/v1/1",
            "docs_url": "https://www.themealdb.com/api.php",
            "auth": "none",
            "tier": 1,
            "endpoints": [
                {"path": "/search.php?s={meal}", "method": "GET", "desc": "Search meals by name", "example": "curl 'https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata'"},
                {"path": "/random.php", "method": "GET", "desc": "Get a random meal recipe", "example": "curl 'https://www.themealdb.com/api/json/v1/1/random.php'"}
            ]
        },
        "TheCocktailDB": {
            "name": "TheCocktailDB",
            "base_url": "https://www.thecocktaildb.com/api/json/v1/1",
            "docs_url": "https://www.thecocktaildb.com/api.php",
            "auth": "none",
            "tier": 1,
            "endpoints": [
                {"path": "/search.php?s={cocktail}", "method": "GET", "desc": "Search cocktails by name", "example": "curl 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita'"},
                {"path": "/random.php", "method": "GET", "desc": "Get a random cocktail recipe", "example": "curl 'https://www.thecocktaildb.com/api/json/v1/1/random.php'"}
            ]
        },
        "Open Food Facts": {
            "base_url": "https://world.openfoodfacts.org/api/v2",
            "docs_url": "https://wiki.openfoodfacts.org/API",
            "tier": 1,
            "endpoints": [
                {"path": "/product/{barcode}.json", "method": "GET", "desc": "Get product nutrition by barcode", "example": "curl 'https://world.openfoodfacts.org/api/v2/product/3017620422003.json'"},
                {"path": "/search?categories_tags=pizza&page_size=5", "method": "GET", "desc": "Search products by category", "example": "curl 'https://world.openfoodfacts.org/api/v2/search?categories_tags=pizza&page_size=5'"}
            ]
        },
        "Edamam": {
            "base_url": "https://api.edamam.com",
            "docs_url": "https://developer.edamam.com/edamam-docs-recipe-api",
            "tier": 2,
            "endpoints": [
                {"path": "/api/recipes/v2?type=public&q={query}&app_id={id}&app_key={key}", "method": "GET", "desc": "Search recipes by ingredient or dish name", "example": "curl 'https://api.edamam.com/api/recipes/v2?type=public&q=chicken&app_id=$EDAMAM_APP_ID&app_key=$EDAMAM_API_KEY'"}
            ]
        }
    },
    "sports-fitness": {
        "TheSportsDB": {
            "name": "TheSportsDB",
            "base_url": "https://www.thesportsdb.com/api/v1/json/3",
            "docs_url": "https://www.thesportsdb.com/api.php",
            "auth": "none",
            "tier": 1,
            "endpoints": [
                {"path": "/searchteams.php?t={team}", "method": "GET", "desc": "Search teams by name", "example": "curl 'https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t=Arsenal'"},
                {"path": "/eventslast.php?id={teamId}", "method": "GET", "desc": "Get last 5 events for a team", "example": "curl 'https://www.thesportsdb.com/api/v1/json/3/eventslast.php?id=133604'"}
            ]
        },
        "NBA API": {
            "name": "balldontlie",
            "base_url": "https://api.balldontlie.io/v1",
            "docs_url": "https://www.balldontlie.io/",
            "auth": "none",
            "tier": 1,
            "endpoints": [
                {"path": "/players?search={name}", "method": "GET", "desc": "Search NBA players by name", "example": "curl 'https://api.balldontlie.io/v1/players?search=lebron'"},
                {"path": "/teams", "method": "GET", "desc": "Get all NBA teams", "example": "curl 'https://api.balldontlie.io/v1/teams'"}
            ]
        },
        "Football-Data.org": {
            "name": "Football-Data.org",
            "base_url": "https://api.football-data.org/v4",
            "docs_url": "https://www.football-data.org/documentation/quickstart",
            "auth": "apiKey",
            "auth_param": "X-Auth-Token",
            "auth_location": "header",
            "key_env_var": "FOOTBALL_DATA_API_KEY",
            "tier": 1,
            "endpoints": [
                {"path": "/competitions/PL/standings", "method": "GET", "desc": "Get Premier League standings", "example": "curl -H 'X-Auth-Token: $FOOTBALL_DATA_API_KEY' 'https://api.football-data.org/v4/competitions/PL/standings'"},
                {"path": "/matches?dateFrom={date}&dateTo={date}", "method": "GET", "desc": "Get matches in a date range", "example": "curl -H 'X-Auth-Token: $FOOTBALL_DATA_API_KEY' 'https://api.football-data.org/v4/matches?dateFrom=2026-03-10&dateTo=2026-03-13'"}
            ]
        }
    },
    "transportation": {
        "OpenSky Network": {
            "base_url": "https://opensky-network.org/api",
            "docs_url": "https://openskynetwork.github.io/opensky-api/",
            "tier": 1,
            "endpoints": [
                {"path": "/states/all", "method": "GET", "desc": "Get all current aircraft states (global)", "example": "curl 'https://opensky-network.org/api/states/all?lamin=33.0&lomin=-112.5&lamax=34.0&lomax=-111.5'"},
                {"path": "/flights/all?begin={unix}&end={unix}", "method": "GET", "desc": "Get flights in a time interval", "example": "curl 'https://opensky-network.org/api/flights/all?begin=1710288000&end=1710374400'"}
            ]
        },
        "OpenChargeMap": {
            "base_url": "https://api.openchargemap.io/v3",
            "docs_url": "https://openchargemap.org/site/develop/api",
            "tier": 1,
            "endpoints": [
                {"path": "/poi?latitude={lat}&longitude={lon}&distance=5&maxresults=10&key={key}", "method": "GET", "desc": "Find EV charging stations near a location", "example": "curl 'https://api.openchargemap.io/v3/poi?latitude=33.4484&longitude=-112.074&distance=5&maxresults=10&key=$OPENCHARGEMAP_API_KEY'"},
                {"path": "/referencedata", "method": "GET", "desc": "Get reference data (connector types, networks, etc.)", "example": "curl 'https://api.openchargemap.io/v3/referencedata'"}
            ]
        },
        "ADS-B Exchange": {
            "base_url": "https://adsbexchange.com/api",
            "docs_url": "https://www.adsbexchange.com/data/",
            "tier": 2,
            "endpoints": [
                {"path": "/aircraft/json/lat/{lat}/lon/{lon}/dist/{nm}/", "method": "GET", "desc": "Aircraft near a location", "example": "curl 'https://adsbexchange.com/api/aircraft/json/lat/33.45/lon/-112.07/dist/25/'"}
            ]
        }
    },
    "science": {
        "NASA APOD": {
            "name": "NASA APOD",
            "base_url": "https://api.nasa.gov",
            "docs_url": "https://api.nasa.gov/",
            "auth": "apiKey",
            "auth_param": "api_key",
            "auth_location": "query",
            "key_env_var": "NASA_API_KEY",
            "tier": 1,
            "endpoints": [
                {"path": "/planetary/apod?api_key={key}", "method": "GET", "desc": "Astronomy Picture of the Day", "example": "curl 'https://api.nasa.gov/planetary/apod?api_key=$NASA_API_KEY'"},
                {"path": "/neo/rest/v1/feed?start_date={date}&api_key={key}", "method": "GET", "desc": "Near Earth Objects for a date range", "example": "curl 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2026-03-13&api_key=$NASA_API_KEY'"}
            ]
        },
        "SpaceX API": {
            "name": "SpaceX API",
            "base_url": "https://api.spacexdata.com/v4",
            "docs_url": "https://github.com/r-spacex/SpaceX-API",
            "auth": "none",
            "tier": 1,
            "endpoints": [
                {"path": "/launches/latest", "method": "GET", "desc": "Get latest SpaceX launch details", "example": "curl 'https://api.spacexdata.com/v4/launches/latest'"},
                {"path": "/rockets", "method": "GET", "desc": "Get all SpaceX rockets", "example": "curl 'https://api.spacexdata.com/v4/rockets'"}
            ]
        },
        "USGS Earthquake": {
            "name": "USGS Earthquake",
            "base_url": "https://earthquake.usgs.gov/fdsnws/event/1",
            "docs_url": "https://earthquake.usgs.gov/fdsnws/event/1/",
            "auth": "none",
            "tier": 1,
            "endpoints": [
                {"path": "/query?format=geojson&minmagnitude=4&limit=10&orderby=time", "method": "GET", "desc": "Recent significant earthquakes worldwide", "example": "curl 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minmagnitude=4&limit=10&orderby=time'"},
                {"path": "/query?format=geojson&latitude={lat}&longitude={lon}&maxradiuskm=100", "method": "GET", "desc": "Earthquakes near a location", "example": "curl 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&latitude=33.45&longitude=-112.07&maxradiuskm=100'"}
            ]
        },
        "Launch Library 2": {
            "name": "Launch Library 2",
            "base_url": "https://ll.thespacedevs.com/2.2.0",
            "docs_url": "https://thespacedevs.com/llapi",
            "auth": "none",
            "tier": 1,
            "endpoints": [
                {"path": "/launch/upcoming/?limit=5", "method": "GET", "desc": "Get upcoming space launches", "example": "curl 'https://ll.thespacedevs.com/2.2.0/launch/upcoming/?limit=5'"},
                {"path": "/astronaut/?search={name}", "method": "GET", "desc": "Search astronauts by name", "example": "curl 'https://ll.thespacedevs.com/2.2.0/astronaut/?search=chris'"}
            ]
        },
        "arXiv": {
            "base_url": "http://export.arxiv.org/api",
            "docs_url": "https://info.arxiv.org/help/api/index.html",
            "tier": 2,
            "endpoints": [
                {"path": "/query?search_query=all:{query}&start=0&max_results=5", "method": "GET", "desc": "Search research papers by keyword", "example": "curl 'http://export.arxiv.org/api/query?search_query=all:transformer+attention&max_results=5'"}
            ]
        },
        "PubChem": {
            "name": "PubChem",
            "base_url": "https://pubchem.ncbi.nlm.nih.gov/rest/pug",
            "docs_url": "https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest",
            "auth": "none",
            "tier": 2,
            "endpoints": [
                {"path": "/compound/name/{name}/JSON", "method": "GET", "desc": "Get chemical compound info by name", "example": "curl 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/aspirin/JSON'"}
            ]
        }
    },
    "health": {
        "OpenFDA": {
            "base_url": "https://api.fda.gov",
            "docs_url": "https://open.fda.gov/apis/",
            "tier": 1,
            "endpoints": [
                {"path": "/drug/event.json?search=patient.drug.openfda.brand_name:{drug}&limit=5", "method": "GET", "desc": "Drug adverse event reports", "example": "curl 'https://api.fda.gov/drug/event.json?search=patient.drug.openfda.brand_name:aspirin&limit=5'"},
                {"path": "/food/enforcement.json?limit=5", "method": "GET", "desc": "Recent food recall enforcement reports", "example": "curl 'https://api.fda.gov/food/enforcement.json?limit=5'"}
            ]
        },
        "USDA FoodData Central": {
            "name": "USDA FoodData Central",
            "base_url": "https://api.nal.usda.gov/fdc/v1",
            "docs_url": "https://fdc.nal.usda.gov/api-guide.html",
            "auth": "apiKey",
            "auth_param": "api_key",
            "auth_location": "query",
            "key_env_var": "USDA_API_KEY",
            "tier": 1,
            "endpoints": [
                {"path": "/foods/search?query={food}&api_key={key}&pageSize=5", "method": "GET", "desc": "Search foods with nutrition data", "example": "curl 'https://api.nal.usda.gov/fdc/v1/foods/search?query=banana&api_key=$USDA_API_KEY&pageSize=5'"},
                {"path": "/food/{fdcId}?api_key={key}", "method": "GET", "desc": "Get detailed nutrition for a specific food", "example": "curl 'https://api.nal.usda.gov/fdc/v1/food/534358?api_key=$USDA_API_KEY'"}
            ]
        },
        "Disease.sh": {
            "name": "Disease.sh",
            "base_url": "https://disease.sh/v3",
            "docs_url": "https://disease.sh/docs/",
            "auth": "none",
            "tier": 1,
            "endpoints": [
                {"path": "/covid-19/all", "method": "GET", "desc": "Global COVID-19 statistics", "example": "curl 'https://disease.sh/v3/covid-19/all'"},
                {"path": "/covid-19/countries/{country}", "method": "GET", "desc": "COVID-19 data for a specific country", "example": "curl 'https://disease.sh/v3/covid-19/countries/USA'"}
            ]
        }
    },
    "crypto-web3": {
        "CoinCap": {
            "base_url": "https://api.coincap.io/v2",
            "docs_url": "https://docs.coincap.io/",
            "tier": 1,
            "endpoints": [
                {"path": "/assets?limit=10", "method": "GET", "desc": "Top cryptocurrencies by market cap", "example": "curl 'https://api.coincap.io/v2/assets?limit=10'"},
                {"path": "/assets/{id}/history?interval=d1", "method": "GET", "desc": "Price history for a cryptocurrency", "example": "curl 'https://api.coincap.io/v2/assets/bitcoin/history?interval=d1'"}
            ]
        },
        "Etherscan": {
            "base_url": "https://api.etherscan.io/api",
            "docs_url": "https://docs.etherscan.io/",
            "tier": 1,
            "endpoints": [
                {"path": "?module=account&action=balance&address={addr}&apikey={key}", "method": "GET", "desc": "Get ETH balance for an address", "example": "curl 'https://api.etherscan.io/api?module=account&action=balance&address=0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae&apikey=$ETHERSCAN_API_KEY'"},
                {"path": "?module=stats&action=ethprice&apikey={key}", "method": "GET", "desc": "Get current ETH price", "example": "curl 'https://api.etherscan.io/api?module=stats&action=ethprice&apikey=$ETHERSCAN_API_KEY'"}
            ]
        },
        "DeFi Llama": {
            "base_url": "https://api.llama.fi",
            "docs_url": "https://defillama.com/docs/api",
            "tier": 1,
            "endpoints": [
                {"path": "/protocols", "method": "GET", "desc": "Get all DeFi protocols with TVL data", "example": "curl 'https://api.llama.fi/protocols' | jq '.[0:5] | .[] | {name, tvl}'"},
                {"path": "/tvl/{protocol}", "method": "GET", "desc": "Get current TVL for a protocol", "example": "curl 'https://api.llama.fi/tvl/aave'"}
            ]
        },
        "Blockchain.com": {
            "base_url": "https://blockchain.info",
            "docs_url": "https://www.blockchain.com/explorer/api",
            "tier": 1,
            "endpoints": [
                {"path": "/ticker", "method": "GET", "desc": "Bitcoin price in multiple currencies", "example": "curl 'https://blockchain.info/ticker'"},
                {"path": "/rawaddr/{address}", "method": "GET", "desc": "Get Bitcoin address balance and transactions", "example": "curl 'https://blockchain.info/rawaddr/1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa?limit=3'"}
            ]
        }
    },
    "security": {
        "AbuseIPDB": {
            "base_url": "https://api.abuseipdb.com/api/v2",
            "docs_url": "https://docs.abuseipdb.com/",
            "tier": 1,
            "endpoints": [
                {"path": "/check?ipAddress={ip}&maxAgeInDays=90", "method": "GET", "desc": "Check if an IP has been reported as abusive", "example": "curl -H 'Key: $ABUSEIPDB_API_KEY' -H 'Accept: application/json' 'https://api.abuseipdb.com/api/v2/check?ipAddress=118.25.6.39&maxAgeInDays=90'"},
                {"path": "/blacklist?limit=10", "method": "GET", "desc": "Get most reported IP addresses", "example": "curl -H 'Key: $ABUSEIPDB_API_KEY' -H 'Accept: application/json' 'https://api.abuseipdb.com/api/v2/blacklist?limit=10'"}
            ]
        },
        "VirusTotal": {
            "base_url": "https://www.virustotal.com/api/v3",
            "docs_url": "https://developers.virustotal.com/reference/overview",
            "tier": 1,
            "endpoints": [
                {"path": "/urls/{id}", "method": "GET", "desc": "Get URL scan report", "example": "curl -H 'x-apikey: $VIRUSTOTAL_API_KEY' 'https://www.virustotal.com/api/v3/urls/{url_id}'"},
                {"path": "/domains/{domain}", "method": "GET", "desc": "Get domain reputation report", "example": "curl -H 'x-apikey: $VIRUSTOTAL_API_KEY' 'https://www.virustotal.com/api/v3/domains/google.com'"}
            ]
        },
        "Shodan": {
            "base_url": "https://api.shodan.io",
            "docs_url": "https://developer.shodan.io/api",
            "tier": 1,
            "endpoints": [
                {"path": "/shodan/host/{ip}?key={key}", "method": "GET", "desc": "Get all available information on a host", "example": "curl 'https://api.shodan.io/shodan/host/8.8.8.8?key=$SHODAN_API_KEY'"},
                {"path": "/dns/resolve?hostnames={domain}&key={key}", "method": "GET", "desc": "DNS lookup for a domain", "example": "curl 'https://api.shodan.io/dns/resolve?hostnames=google.com&key=$SHODAN_API_KEY'"}
            ]
        },
        "Have I Been Pwned": {
            "base_url": "https://haveibeenpwned.com/api/v3",
            "docs_url": "https://haveibeenpwned.com/API/v3",
            "tier": 2,
            "endpoints": [
                {"path": "/breachedaccount/{account}", "method": "GET", "desc": "Check if an email has been in a breach", "example": "curl -H 'hibp-api-key: $HIBP_API_KEY' -H 'user-agent: api-catalog' 'https://haveibeenpwned.com/api/v3/breachedaccount/test@example.com'"}
            ]
        }
    },
    "shopping": {
        "Fake Store API": {
            "base_url": "https://fakestoreapi.com",
            "docs_url": "https://fakestoreapi.com/docs",
            "tier": 1,
            "endpoints": [
                {"path": "/products?limit=5", "method": "GET", "desc": "Get product listings", "example": "curl 'https://fakestoreapi.com/products?limit=5'"},
                {"path": "/products/categories", "method": "GET", "desc": "Get all product categories", "example": "curl 'https://fakestoreapi.com/products/categories'"}
            ]
        },
        "DummyJSON": {
            "name": "DummyJSON",
            "base_url": "https://dummyjson.com",
            "docs_url": "https://dummyjson.com/docs/products",
            "auth": "none",
            "tier": 1,
            "endpoints": [
                {"path": "/products/search?q={query}", "method": "GET", "desc": "Search products by name", "example": "curl 'https://dummyjson.com/products/search?q=phone'"},
                {"path": "/products/categories", "method": "GET", "desc": "Get all product categories", "example": "curl 'https://dummyjson.com/products/categories'"}
            ]
        }
    },
    "photography-media": {
        "Unsplash": {
            "base_url": "https://api.unsplash.com",
            "docs_url": "https://unsplash.com/documentation",
            "tier": 1,
            "endpoints": [
                {"path": "/photos/random?query={query}", "method": "GET", "desc": "Get a random photo matching a query", "example": "curl -H 'Authorization: Client-ID $UNSPLASH_ACCESS_KEY' 'https://api.unsplash.com/photos/random?query=nature'"},
                {"path": "/search/photos?query={query}&per_page=5", "method": "GET", "desc": "Search photos by keyword", "example": "curl -H 'Authorization: Client-ID $UNSPLASH_ACCESS_KEY' 'https://api.unsplash.com/search/photos?query=mountain&per_page=5'"}
            ]
        },
        "Pexels": {
            "base_url": "https://api.pexels.com/v1",
            "docs_url": "https://www.pexels.com/api/documentation/",
            "tier": 1,
            "endpoints": [
                {"path": "/search?query={query}&per_page=5", "method": "GET", "desc": "Search photos by keyword", "example": "curl -H 'Authorization: $PEXELS_API_KEY' 'https://api.pexels.com/v1/search?query=sunset&per_page=5'"},
                {"path": "/curated?per_page=5", "method": "GET", "desc": "Get curated photos", "example": "curl -H 'Authorization: $PEXELS_API_KEY' 'https://api.pexels.com/v1/curated?per_page=5'"}
            ]
        },
        "Lorem Picsum": {
            "base_url": "https://picsum.photos",
            "docs_url": "https://picsum.photos/",
            "tier": 1,
            "endpoints": [
                {"path": "/v2/list?limit=10", "method": "GET", "desc": "List available images", "example": "curl 'https://picsum.photos/v2/list?limit=10'"},
                {"path": "/{width}/{height}", "method": "GET", "desc": "Get a random image at specified dimensions", "example": "curl -o image.jpg 'https://picsum.photos/800/600'"}
            ]
        },
        "Pixabay": {
            "base_url": "https://pixabay.com/api",
            "docs_url": "https://pixabay.com/api/docs/",
            "tier": 2,
            "endpoints": [
                {"path": "/?key={key}&q={query}&per_page=5", "method": "GET", "desc": "Search free stock images", "example": "curl 'https://pixabay.com/api/?key=$PIXABAY_API_KEY&q=coding&per_page=5'"}
            ]
        }
    },
    "utilities": {
        "RandomUser": {
            "base_url": "https://randomuser.me",
            "docs_url": "https://randomuser.me/documentation",
            "tier": 1,
            "endpoints": [
                {"path": "/api/?results=5", "method": "GET", "desc": "Generate random user profiles", "example": "curl 'https://randomuser.me/api/?results=5'"},
                {"path": "/api/?results=3&nat=us&gender=female", "method": "GET", "desc": "Generate filtered random users", "example": "curl 'https://randomuser.me/api/?results=3&nat=us&gender=female'"}
            ]
        },
        "UUID Generator": {
            "name": "httpbin UUID",
            "base_url": "https://httpbin.org",
            "docs_url": "https://httpbin.org/",
            "auth": "none",
            "tier": 2,
            "endpoints": [
                {"path": "/uuid", "method": "GET", "desc": "Generate a UUID v4", "example": "curl 'https://httpbin.org/uuid'"}
            ]
        },
        "QR Code Generator": {
            "base_url": "https://api.qrserver.com/v1",
            "docs_url": "https://goqr.me/api/",
            "tier": 2,
            "endpoints": [
                {"path": "/create-qr-code/?size=200x200&data={url}", "method": "GET", "desc": "Generate a QR code image", "example": "curl -o qr.png 'https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://example.com'"}
            ]
        },
        "ip-api": {
            "name": "ip-api",
            "base_url": "http://ip-api.com",
            "docs_url": "https://ip-api.com/docs/",
            "auth": "none",
            "tier": 1,
            "endpoints": [
                {"path": "/json/{ip}", "method": "GET", "desc": "Geolocate an IP address", "example": "curl 'http://ip-api.com/json/24.48.0.1'"},
                {"path": "/json/", "method": "GET", "desc": "Geolocate your own IP", "example": "curl 'http://ip-api.com/json/'"}
            ]
        },
        "Lorem Ipsum": {
            "name": "Bacon Ipsum",
            "base_url": "https://baconipsum.com/api",
            "docs_url": "https://baconipsum.com/json-api/",
            "auth": "none",
            "tier": 2,
            "endpoints": [
                {"path": "/?type=meat-and-filler&paras=3&format=text", "method": "GET", "desc": "Generate placeholder text", "example": "curl 'https://baconipsum.com/api/?type=meat-and-filler&paras=3&format=text'"}
            ]
        }
    }
}


def enrich_category(slug, enrichments):
    filepath = os.path.join(CATEGORIES_DIR, f"{slug}.json")
    with open(filepath) as f:
        data = json.load(f)

    enriched_count = 0
    added_count = 0

    for api in data["apis"]:
        api_name = api["name"]
        if api_name in enrichments:
            enrich = enrichments[api_name]
            for key, val in enrich.items():
                if key != "name":  # don't overwrite name
                    api[key] = val
            enriched_count += 1

    # Check for APIs in enrichments that need to be added (not found by name)
    existing_names = {a["name"].lower() for a in data["apis"]}
    for api_name, enrich in enrichments.items():
        if api_name.lower() not in existing_names and "name" in enrich:
            new_api = {
                "name": enrich.get("name", api_name),
                "description": enrich.get("description", ""),
                "base_url": enrich.get("base_url", ""),
                "auth": enrich.get("auth", "none"),
                "auth_param": enrich.get("auth_param", None),
                "auth_location": enrich.get("auth_location", None),
                "free_tier": enrich.get("free_tier", "See docs"),
                "key_env_var": enrich.get("key_env_var", None),
                "docs_url": enrich.get("docs_url", ""),
                "tier": enrich.get("tier", 2),
                "endpoints": enrich.get("endpoints", [])
            }
            data["apis"].append(new_api)
            added_count += 1

    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

    return enriched_count, added_count


def main():
    total_enriched = 0
    total_added = 0

    for slug, enrichments in ENRICHMENTS.items():
        enriched, added = enrich_category(slug, enrichments)
        total_enriched += enriched
        total_added += added
        print(f"{slug:25s}: {enriched} enriched, {added} added")

    print(f"\nTotal: {total_enriched} enriched, {total_added} added")


if __name__ == "__main__":
    main()
