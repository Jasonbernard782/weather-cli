# Weather CLI

A colorful, command-line weather app.

# Features

- Current weather by city
- 5-day forecast
- Colorful terminal UI
- Fast & lightweight
- Works on macOS and Linux

# Installation

# macOS/ Linux:

git clone https://github.com/Jasonbernard782/weather-cli.git &&
cd weather-cli &&
python3 -m venv .venv &&
source .venv/bin/activate &&
python -m pip install --upgrade pip setuptools wheel &&
pip install . &&
export OPENWEATHER_API_KEY="ba8195ae3fff71980febe1b3fb527f80" &&
weather
