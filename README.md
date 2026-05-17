# 🌤️ Weather & News CMD Dashboard

A command-line Python app that gives you a quick, clean snapshot of the world — weather from any city on the planet and top news by location or category, all from your terminal.

---

## What It Does

- **Your city on startup** — Automatically fetches and displays the weather report for your default city every time you run the app, and logs it to a local JSON file for historical reference.
- **Weather by city** — Search real-time weather for any city in the world: temperature, feels like, humidity, and wind speed.
- **News by city** — Fetch the top 5 latest news articles from any city, with source, timestamp, description, and a direct link to read the full article.
- **News by category** — Browse top headlines across six categories: business, entertainment, health, science, sports, and technology.

---

## Why I Built This

This started as a learning project to understand how APIs work in Python — authentication, parameters, error handling, parsing JSON responses. It quickly became something I actually wanted to use daily.

The goal was to build something that *feels* like an app, not just a script — clean output, clear menu, graceful error messages, and a logical separation between fetching data and displaying it.

---

## Project Structure

```
weather-news-dashboard/
│
├── final_display.py        # Entry point — menu and app flow
├── weather_functions.py    # Weather fetching and display logic
├── news_functions.py       # News fetching and display logic
├── requirements.txt        # Dependencies
├── .env.example            # API key template
└── .gitignore
```

**Design decision:** Each file has a single responsibility. `weather_functions.py` and `news_functions.py` handle fetching and displaying their respective data. `final_display.py` only handles the menu flow and calls into those modules. This makes the codebase easy to extend — adding a new feature means touching one file, not everything.

---

## Tech Stack

- **Python 3**
- **Requests** — HTTP calls to both APIs
- **python-dotenv** — Secure API key management via `.env`
- **OpenWeatherMap API** — Real-time weather data
- **NewsAPI** — News articles and top headlines

---

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/alok-kt/Weather-News-cmd-dashboard.git
cd Weather-News-cmd-dashboard
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up your API keys**

Copy `.env.example` to `.env` and add your keys:
```
WEATHER_API_KEY=your_openweathermap_key
NEWS_API_KEY=your_newsapi_key
```

Get your free keys here:
- [OpenWeatherMap](https://openweathermap.org/api)
- [NewsAPI](https://newsapi.org/)

**4. Set your default city**

In `weather_functions.py`, the `my_weather()` function accepts a city parameter. Update the default value to your city:
```python
def my_weather(city="your_city"):
```

**5. Run the app**
```bash
python final_display.py
```

---

## Error Handling

The app handles failures gracefully rather than crashing:
- Invalid or misspelled city names
- Invalid API keys (401)
- Rate limit and server errors with descriptive messages
- Network timeouts and connection failures
- Empty API responses

---

## v2 — Streamlit Web Interface
The CMD version has been upgraded to a full browser-based 
Streamlit app available on the streamlit-v2 branch. 
Features the same core functionality with a visual UI, 
tabbed layout, sidebar controls, and expandable news cards.

---

## Learnings

This was my first fully working multi-API project. Key things I learned building it:
- How to structure a Python project across multiple modules
- Secure API key management with `.env`
- Defensive programming — handling every failure mode, not just the happy path
- The difference between a script that runs and an app that feels intentional

---

*Built by [Alok](https://github.com/alok-kt)*
