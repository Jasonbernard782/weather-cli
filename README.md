# Weather CLI:

A colorful, command-line weather app.

# Features:

- Current weather by city
- 5-day forecast
- Colorful terminal UI
- Fast & lightweight
- Works on macOS and Linux

# Installation:

# macOS/ Linux:

command -v pipx >/dev/null || (python3 -m pip install --user pipx && python3 -m pipx ensurepath) && pipx install git+https://github.com/Jasonbernard782/weather-cli.git

(This will install Weather-CLI in an isolated environment. You only need to do this once per machine.)

(Install pipx if not already installed.)


# Get an OpenWeather API Key:

Weather-CLI requires an API key from https://openweathermap.org/api
to fetch live weather data.

- Sign up for a free account

- Copy your API key

# Set your API key (One-time setup):

# macOS / Linux:

export OPENWEATHER_API_KEY="your_api_key_here"

# To make it permanent:

echo 'export OPENWEATHER_API_KEY="your_api_key_here"' >> ~/.zshrc

source ~/.zshrc

# Run Weather-CLI:

weather

weather city

weather --forecast city or -f

weather --units metric | imperial

weather --help

<img width="844" height="1016" alt="Screenshot 2025-12-29 at 04 10 46" src="https://github.com/user-attachments/assets/b0f1a7e5-332c-4e6e-b042-0d5ec30cba17" />
