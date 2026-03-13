#!/usr/bin/env python3
"""
Parse public-apis/public-apis README.md and generate category JSON seed files.
Maps ~45 public-apis categories → our 25 categories.
Deduplicates against existing 190 APIs.
Output: 15 new seed JSON files in categories/ with tier 3 metadata.
"""

import json
import os
import re
import urllib.request

REPO_URL = "https://raw.githubusercontent.com/public-apis/public-apis/master/README.md"
CATEGORIES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "categories")

# Map public-apis categories → our category slugs
CATEGORY_MAP = {
    # New categories (15)
    "Animals": "animals-nature",
    "Environment": "animals-nature",
    "Anime": "entertainment",
    "Entertainment": "entertainment",
    "Games & Comics": "entertainment",
    "Video": "entertainment",
    "Music": "music",
    "Food & Drink": "food-drink",
    "Books": "books-literature",
    "Dictionaries": "books-literature",
    "Sports & Fitness": "sports-fitness",
    "Transportation": "transportation",
    "Vehicle": "transportation",
    "Science & Math": "science",
    "Open Data": "science",
    "Health": "health",
    "Art & Design": "photography-media",
    "Photography": "photography-media",
    "Cryptocurrency": "crypto-web3",
    "Security": "security",
    "Anti-Malware": "security",
    "Shopping": "shopping",
    "URL Shorteners": "utilities",
    "Data Validation": "utilities",
    "Calendar": "utilities",
    "Cloud Storage & File Sharing": "utilities",
    "Documents & Productivity": "utilities",
    "Email": "utilities",
    "Phone": "utilities",
    "Text Analysis": "utilities",
    "Continuous Integration": "utilities",
    "Machine Learning": "utilities",
    "Test Data": "utilities",
    "Tracking": "utilities",
    "Geocoding": "utilities",
    "Currency Exchange": "utilities",
    "Patent": "utilities",
    # Existing categories (map to skip or merge)
    "Weather": "weather",
    "News": "news",
    "Jobs": "jobs",
    "Social": "social",
    "Finance": "finance",
    "Business": "business",
    "Development": "dev-tools",
    "Government": "government",
    "Personality": "entertainment",
    "Authentication & Authorization": "security",
}

# Categories we want to CREATE (new ones only)
NEW_CATEGORIES = {
    "entertainment": "Games, anime, movies, TV, comics, and fun APIs",
    "music": "Music metadata, streaming, lyrics, and audio APIs",
    "food-drink": "Recipes, restaurants, nutrition, and beverage APIs",
    "books-literature": "Book search, dictionaries, quotes, and literary APIs",
    "animals-nature": "Animal facts, images, species data, and nature APIs",
    "sports-fitness": "Sports scores, stats, fitness tracking, and athletic APIs",
    "transportation": "Flights, transit, vehicles, and shipping APIs",
    "science": "Research papers, space, physics, math, and open data APIs",
    "health": "Medical data, nutrition, fitness, and wellness APIs",
    "photography-media": "Stock photos, image processing, art, and design APIs",
    "crypto-web3": "Cryptocurrency beyond basic prices, blockchain, DeFi, and NFT APIs",
    "security": "Vulnerability scanning, malware detection, breach checking, and security APIs",
    "shopping": "Product search, price comparison, e-commerce, and retail APIs",
    "utilities": "URL shorteners, validators, converters, generators, and misc tools",
    "education": "Quiz, trivia, learning resources, and educational APIs",
}

# Also allow adding to existing categories
EXISTING_CATEGORIES = {"weather", "news", "jobs", "social", "finance", "business", "dev-tools", "government"}


def fetch_readme():
    """Fetch the public-apis README.md."""
    print("Fetching public-apis README.md...")
    req = urllib.request.Request(REPO_URL, headers={"User-Agent": "api-catalog-parser/1.0"})
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode("utf-8")


def parse_readme(content):
    """Parse markdown tables into structured API data."""
    apis_by_category = {}
    current_category = None
    in_table = False

    for line in content.split("\n"):
        # Detect category headers (## or ###)
        header_match = re.match(r'^#{2,3}\s+(.+)', line.strip())
        if header_match:
            cat_name = header_match.group(1).strip()
            # Skip non-category headers
            if cat_name in ("Index", "License", "Contributing", "API", "List"):
                continue
            if cat_name in CATEGORY_MAP or any(cat_name.startswith(k) for k in CATEGORY_MAP):
                current_category = cat_name
                if current_category not in apis_by_category:
                    apis_by_category[current_category] = []
                in_table = False
            continue

        # Detect table rows
        if current_category and "|" in line and "---" not in line:
            cols = [c.strip() for c in line.split("|")]
            cols = [c for c in cols if c]  # Remove empty from leading/trailing |

            if len(cols) >= 4:
                # Skip header rows
                if cols[0] == "API" or cols[0] == "Name":
                    in_table = True
                    continue

                if in_table:
                    # Extract link from markdown [name](url)
                    name = cols[0]
                    link_match = re.match(r'\[([^\]]+)\]\(([^)]+)\)', name)

                    api_name = link_match.group(1) if link_match else name
                    api_url = link_match.group(2) if link_match else ""
                    description = cols[1] if len(cols) > 1 else ""
                    auth = cols[2] if len(cols) > 2 else "No"
                    https = cols[3] if len(cols) > 3 else "Yes"
                    cors = cols[4] if len(cols) > 4 else "Unknown"

                    # Normalize auth
                    auth_normalized = "none"
                    if auth.lower() in ("apikey", "api key", "`apikey`", "`apiKey`"):
                        auth_normalized = "apiKey"
                    elif auth.lower() in ("oauth", "`oauth`"):
                        auth_normalized = "OAuth"
                    elif auth.lower() in ("x-mashape-key", "`x-mashape-key`"):
                        auth_normalized = "apiKey"

                    apis_by_category[current_category].append({
                        "name": api_name,
                        "description": description,
                        "url": api_url,
                        "auth": auth_normalized,
                        "https": https.lower() == "yes",
                        "cors": cors,
                    })
        elif not line.strip().startswith("|"):
            in_table = False

    return apis_by_category


def load_existing_apis():
    """Load all existing API names from current category files."""
    existing = set()
    for fname in os.listdir(CATEGORIES_DIR):
        if fname.endswith(".json"):
            filepath = os.path.join(CATEGORIES_DIR, fname)
            with open(filepath) as f:
                data = json.load(f)
                for api in data.get("apis", []):
                    existing.add(api["name"].lower().strip())
    return existing


def map_and_deduplicate(apis_by_category, existing_names):
    """Map public-apis categories to our categories and deduplicate."""
    our_categories = {}

    for source_cat, apis in apis_by_category.items():
        # Find our target category
        target = CATEGORY_MAP.get(source_cat)
        if not target:
            # Try partial match
            for key, val in CATEGORY_MAP.items():
                if key.lower() in source_cat.lower() or source_cat.lower() in key.lower():
                    target = val
                    break

        if not target:
            print(f"  SKIP: No mapping for '{source_cat}' ({len(apis)} APIs)")
            continue

        if target not in our_categories:
            our_categories[target] = []

        for api in apis:
            # Deduplicate by name
            if api["name"].lower().strip() in existing_names:
                continue
            # Also check within our new additions
            already_added = any(
                a["name"].lower() == api["name"].lower()
                for a in our_categories[target]
            )
            if not already_added:
                our_categories[target].append(api)

    return our_categories


def generate_category_json(slug, description, apis):
    """Generate a category JSON file with tier 3 metadata."""
    api_entries = []
    for api in apis:
        # Build base_url from the URL
        base_url = api.get("url", "")
        if not base_url:
            base_url = f"https://{api['name'].lower().replace(' ', '')}.com"

        entry = {
            "name": api["name"],
            "description": api.get("description", ""),
            "base_url": base_url,
            "auth": api.get("auth", "none"),
            "auth_param": None,
            "auth_location": None,
            "free_tier": "See docs",
            "key_env_var": None,
            "docs_url": base_url,
            "tier": 3,
            "endpoints": []
        }

        # Set auth details for apiKey APIs
        if entry["auth"] == "apiKey":
            env_name = re.sub(r'[^A-Z0-9]', '_', api["name"].upper().replace(".", "").replace(" ", "_"))
            env_name = re.sub(r'_+', '_', env_name).strip('_')
            entry["key_env_var"] = f"{env_name}_API_KEY"
            entry["auth_param"] = "key"
            entry["auth_location"] = "query"

        api_entries.append(entry)

    return {
        "category": slug,
        "description": description,
        "apis": api_entries
    }


def main():
    # Fetch and parse
    content = fetch_readme()
    apis_by_category = parse_readme(content)

    total_parsed = sum(len(v) for v in apis_by_category.values())
    print(f"Parsed {total_parsed} APIs across {len(apis_by_category)} categories")
    for cat, apis in sorted(apis_by_category.items()):
        target = CATEGORY_MAP.get(cat, "UNMAPPED")
        print(f"  {cat}: {len(apis)} APIs → {target}")

    # Load existing
    existing_names = load_existing_apis()
    print(f"\nExisting catalog: {len(existing_names)} unique API names")

    # Map and deduplicate
    our_categories = map_and_deduplicate(apis_by_category, existing_names)

    new_total = sum(len(v) for v in our_categories.items() if v[0] in NEW_CATEGORIES)
    print(f"\nNew APIs to add: {sum(len(v) for v in our_categories.values())} across {len(our_categories)} categories")

    # Generate files for NEW categories only
    files_created = 0
    apis_added = 0

    for slug, description in NEW_CATEGORIES.items():
        apis = our_categories.get(slug, [])
        if not apis:
            print(f"  EMPTY: {slug} — no new APIs found")
            # Still create with empty list for completeness
            apis = []

        category_data = generate_category_json(slug, description, apis)

        filepath = os.path.join(CATEGORIES_DIR, f"{slug}.json")

        # If file already exists, merge
        if os.path.exists(filepath):
            with open(filepath) as f:
                existing = json.load(f)
            existing_api_names = {a["name"].lower() for a in existing.get("apis", [])}
            new_apis = [a for a in category_data["apis"] if a["name"].lower() not in existing_api_names]
            existing["apis"].extend(new_apis)
            category_data = existing
            print(f"  MERGE: {slug} — added {len(new_apis)} new APIs to existing {len(existing_api_names)}")
        else:
            print(f"  CREATE: {slug} — {len(category_data['apis'])} APIs")

        with open(filepath, "w") as f:
            json.dump(category_data, f, indent=2)

        files_created += 1
        apis_added += len(category_data["apis"])

    # Also handle APIs that map to existing categories (add to existing files)
    existing_additions = 0
    for slug in EXISTING_CATEGORIES:
        apis = our_categories.get(slug, [])
        if not apis:
            continue

        filepath = os.path.join(CATEGORIES_DIR, f"{slug}.json")
        if not os.path.exists(filepath):
            continue

        with open(filepath) as f:
            existing = json.load(f)

        existing_api_names = {a["name"].lower() for a in existing.get("apis", [])}
        new_entries = []
        for api in apis:
            if api["name"].lower() not in existing_api_names:
                entry = {
                    "name": api["name"],
                    "description": api.get("description", ""),
                    "base_url": api.get("url", ""),
                    "auth": api.get("auth", "none"),
                    "auth_param": None,
                    "auth_location": None,
                    "free_tier": "See docs",
                    "key_env_var": None,
                    "docs_url": api.get("url", ""),
                    "tier": 3,
                    "endpoints": []
                }
                if entry["auth"] == "apiKey":
                    env_name = re.sub(r'[^A-Z0-9]', '_', api["name"].upper().replace(".", "").replace(" ", "_"))
                    env_name = re.sub(r'_+', '_', env_name).strip('_')
                    entry["key_env_var"] = f"{env_name}_API_KEY"
                    entry["auth_param"] = "key"
                    entry["auth_location"] = "query"
                new_entries.append(entry)

        if new_entries:
            existing["apis"].extend(new_entries)
            with open(filepath, "w") as f:
                json.dump(existing, f, indent=2)
            existing_additions += len(new_entries)
            print(f"  AUGMENT: {slug} — added {len(new_entries)} new APIs")

    print(f"\n{'='*50}")
    print(f"Files created/updated: {files_created}")
    print(f"New category APIs: {apis_added}")
    print(f"Existing category additions: {existing_additions}")
    print(f"Total new APIs: {apis_added + existing_additions}")


if __name__ == "__main__":
    main()
