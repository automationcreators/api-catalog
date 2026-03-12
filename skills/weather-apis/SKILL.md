---
name: weather-apis
description: Query free weather APIs via curl. Reads catalog for endpoints and auth.
---

# Weather APIs Skill

## How to use
When the user invokes `/weather-apis "{query}"`, follow these steps:

### Step 1: Read the catalog
Read the API catalog file at:
`/Users/elizabethknopf/Documents/claudec/active/api-catalog/categories/weather.json`

### Step 2: Select the best API
Based on the user's query, pick the most appropriate API and endpoint:

| Query Type | Best API | Why |
|------------|----------|-----|
| Current weather for a city | Open-Meteo or OpenWeatherMap | Real-time conditions |
| Weather forecast (7-day) | Open-Meteo | 7-day hourly/daily, no auth |
| Historical weather data | Open-Meteo | Free historical archive |
| Weather by coordinates | Open-Meteo or OpenWeatherMap | Direct lat/lon support |
| Air quality | OpenWeatherMap | AQI and pollutant data |
| Sunrise/sunset times | Open-Meteo | Included in daily forecast |
| Weather alerts | NWS (US only) | Official US weather alerts |

### Step 3: Check authentication
- If the API requires a key, check if the env var exists: `echo $ENV_VAR_NAME`
- If no key needed (Open-Meteo, NWS), proceed directly
- If key is missing, tell the user which env var to set

### Step 4: Make the API call
Use Bash with curl to call the API. Patterns by API:

**Open-Meteo (comprehensive, no auth):**
```bash
# Current weather for a location (Phoenix, AZ)
curl -s "https://api.open-meteo.com/v1/forecast?latitude=33.45&longitude=-112.07&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code&temperature_unit=fahrenheit&wind_speed_unit=mph" | jq '.current'

# 7-day forecast
curl -s "https://api.open-meteo.com/v1/forecast?latitude=33.45&longitude=-112.07&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,weather_code&temperature_unit=fahrenheit&timezone=America/Phoenix" | jq '.daily | {time, temperature_2m_max, temperature_2m_min, precipitation_sum}'

# Hourly forecast (next 24h)
curl -s "https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&hourly=temperature_2m,precipitation_probability,weather_code&temperature_unit=fahrenheit&timezone=America/New_York&forecast_hours=24" | jq '.hourly | {time: .time[:6], temperature_2m: .temperature_2m[:6], precipitation_probability: .precipitation_probability[:6]}'

# Historical weather (past dates)
curl -s "https://archive-api.open-meteo.com/v1/archive?latitude=33.45&longitude=-112.07&start_date=2026-03-01&end_date=2026-03-10&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&temperature_unit=fahrenheit&timezone=America/Phoenix" | jq '.daily'

# Geocoding (find coordinates for a city name)
curl -s "https://geocoding-api.open-meteo.com/v1/search?name=Phoenix&count=1" | jq '.results[0] | {name, latitude, longitude, country, timezone}'
```

**OpenWeatherMap (current + forecast):**
```bash
# Current weather by city name
curl -s "https://api.openweathermap.org/data/2.5/weather?q=Phoenix,AZ,US&units=imperial&appid=$OPENWEATHER_API_KEY" | jq '{city: .name, temp: .main.temp, feels_like: .main.feels_like, humidity: .main.humidity, description: .weather[0].description, wind_mph: .wind.speed}'

# Current weather by coordinates
curl -s "https://api.openweathermap.org/data/2.5/weather?lat=33.45&lon=-112.07&units=imperial&appid=$OPENWEATHER_API_KEY" | jq '{temp: .main.temp, description: .weather[0].description, humidity: .main.humidity}'

# 5-day / 3-hour forecast
curl -s "https://api.openweathermap.org/data/2.5/forecast?q=New+York,US&units=imperial&appid=$OPENWEATHER_API_KEY" | jq '.list[:8] | .[] | {dt_txt, temp: .main.temp, description: .weather[0].description}'

# Air quality
curl -s "https://api.openweathermap.org/data/2.5/air_pollution?lat=33.45&lon=-112.07&appid=$OPENWEATHER_API_KEY" | jq '.list[0] | {aqi: .main.aqi, components: {pm2_5: .components.pm2_5, pm10: .components.pm10, co: .components.co}}'
```

**National Weather Service (US only, no auth):**
```bash
# Get forecast for a US location (step 1: get grid point)
curl -s "https://api.weather.gov/points/33.4484,-112.0740" -H "User-Agent: ClaudeCode/1.0" | jq '{forecast: .properties.forecast, forecastHourly: .properties.forecastHourly}'

# Get the actual forecast (use URL from step 1)
curl -s "https://api.weather.gov/gridpoints/PSR/159,57/forecast" -H "User-Agent: ClaudeCode/1.0" | jq '.properties.periods[:3] | .[] | {name, temperature, temperatureUnit, shortForecast, windSpeed}'

# Active alerts for a state
curl -s "https://api.weather.gov/alerts/active?area=AZ" -H "User-Agent: ClaudeCode/1.0" | jq '.features[:3] | .[] | .properties | {headline, severity, description: .description[:200]}'

# Active alerts for coordinates
curl -s "https://api.weather.gov/alerts/active?point=33.45,-112.07" -H "User-Agent: ClaudeCode/1.0" | jq '.features | length'
```

**WeatherAPI.com (current + forecast):**
```bash
# Current weather
curl -s "https://api.weatherapi.com/v1/current.json?key=$WEATHERAPI_KEY&q=Phoenix" | jq '{city: .location.name, temp_f: .current.temp_f, condition: .current.condition.text, humidity: .current.humidity, wind_mph: .current.wind_mph}'

# 3-day forecast
curl -s "https://api.weatherapi.com/v1/forecast.json?key=$WEATHERAPI_KEY&q=Phoenix&days=3" | jq '.forecast.forecastday[] | {date, maxtemp_f: .day.maxtemp_f, mintemp_f: .day.mintemp_f, condition: .day.condition.text}'

# Astronomy (sunrise/sunset)
curl -s "https://api.weatherapi.com/v1/astronomy.json?key=$WEATHERAPI_KEY&q=Phoenix" | jq '.astronomy.astro'
```

### Step 5: Format response
Parse the JSON response and present key data points clearly to the user. Include:
- Temperature with units (F or C as appropriate)
- Conditions description
- Key details (humidity, wind, precipitation)
- Forecast period if applicable

## Geocoding Helper
If the user provides a city name instead of coordinates, first use Open-Meteo's geocoding to get lat/lon:
```bash
curl -s "https://geocoding-api.open-meteo.com/v1/search?name=CityName&count=1" | jq '.results[0] | {latitude, longitude}'
```

## Available APIs

| API | Auth | Best For |
|-----|------|----------|
| **Open-Meteo** | None | Current, forecast, historical weather (global) |
| **OpenWeatherMap** | API key (query param) | Current weather, 5-day forecast, air quality |
| **National Weather Service** | None (US only) | Official US forecasts, severe weather alerts |
| **WeatherAPI.com** | API key (query param) | Current, forecast, astronomy data |

## Rate Limits

| API | Free Tier Limits |
|-----|-----------------|
| Open-Meteo | 10,000 requests/day (non-commercial) |
| OpenWeatherMap | 60 calls/minute, 1,000,000 calls/month |
| NWS | No published limit (be reasonable, use User-Agent) |
| WeatherAPI.com | 1,000,000 calls/month |

## Environment Variables

| Variable | API | How to Get |
|----------|-----|-----------|
| `OPENWEATHER_API_KEY` | OpenWeatherMap | https://openweathermap.org/api |
| `WEATHERAPI_KEY` | WeatherAPI.com | https://www.weatherapi.com/signup.aspx |

## Weather Code Reference (Open-Meteo)
- 0: Clear sky
- 1-3: Mainly clear, partly cloudy, overcast
- 45, 48: Fog
- 51-55: Drizzle
- 61-65: Rain
- 71-75: Snow
- 80-82: Rain showers
- 95: Thunderstorm
