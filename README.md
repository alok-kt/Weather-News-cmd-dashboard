# 🌤️ Weather & News Dashboard

A Streamlit web app that shows live weather for any city and the latest news by city or category, all in one clean browser dashboard.

> **Live demo:** _add your Streamlit Cloud link here_

---

## What It Does

- **Your city at a glance:** the Weather tab opens with the current weather for a default city (Thrissur), shown as four metric cards: temperature, feels like, humidity, and wind speed.
- **Weather for any city:** type a city name in the sidebar and get the same four metrics, with the city and country shown as the heading.
- **News by city:** fetch the latest English-language articles mentioning any city, sorted by most recent.
- **News by category:** browse top headlines in six categories: business, entertainment, health, science, sports, and technology.
- **You choose how many:** a sidebar slider sets the number of articles (1 to 20, default 5).
- **Clean article cards:** each story is an expandable card with the source, publish date, description, and a link to the full article.
- **Friendly error messages:** misspelled cities and empty searches show a clear message in the app instead of crashing.

---

## Why I Built This

This started as a command-line project to learn how APIs work in Python: authentication, request parameters, error handling, and parsing JSON responses. Once the logic worked, I turned it into a web app with Streamlit to practice building a real interface on top of it.

Because fetching and displaying were kept separate from the start, the same `weather_functions.py` and `news_functions.py` power both the original CLI and the Streamlit app. Only the display layer changed.

---

## Project Structure

```
Weather-News-cmd-dashboard/
│
├── app.py                  # Streamlit web app (main entry point)
├── weather_functions.py    # Weather fetching logic (OpenWeatherMap)
├── news_functions.py       # News fetching logic (NewsAPI)
├── final_display.py        # Original command-line version
├── requirements.txt        # Dependencies
├── .env.example            # API key template
└── .gitignore
```

**Design decision:** each file has one job. The two function files fetch data, `app.py` handles the web interface, and `final_display.py` handles the terminal menu. Adding a feature means touching one place, not everything.

---

## Tech Stack

- **Python 3**
- **Streamlit:** web interface (tabs, sidebar controls, metric cards, expanders)
- **Requests:** HTTP calls to both APIs
- **python-dotenv:** API key management through a `.env` file
- **OpenWeatherMap API:** real-time weather data
- **NewsAPI:** news articles and top headlines

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

Get free keys here:

- [OpenWeatherMap](https://openweathermap.org/api)
- [NewsAPI](https://newsapi.org/)

**4. (Optional) Change the default city**

In `app.py`, update the city in the Weather tab:

```python
st.subheader("Your City - Thrissur")
default_data = fetch_weather("thrissur")
```

**5. Run the app**

```bash
streamlit run app.py
```

Streamlit will open the dashboard in your browser (usually at `http://localhost:8501`).

---

## How to Use

1. Open the **sidebar** on the left.
2. Enter a city under **Weather**, or leave it empty to keep your default city.
3. Under **News**, choose **City** or **Category**, then pick a city or category.
4. Set the number of articles with the slider.
5. Click **Search**. Results appear in the **Weather** and **News** tabs.

---

## Deploying to Streamlit Community Cloud

1. Push the project to GitHub (never commit your real `.env` file).
2. Create a new app on [Streamlit Community Cloud](https://streamlit.io/cloud) pointing to `app.py`.
3. In the app's **Secrets** settings, add your keys:

```toml
WEATHER_API_KEY = "your_openweathermap_key"
NEWS_API_KEY = "your_newsapi_key"
```

---

## Error Handling

The app handles failures gracefully instead of crashing:

- Invalid or misspelled city names
- Invalid API keys (401)
- Rate limit and server errors
- Network timeouts and connection failures
- Empty API responses and articles with missing fields

---

## Running the Original CLI Version

The terminal version is still included:

```bash
python final_display.py
```

It offers a menu to search weather by city and news by city or category from the command line.

---

## Learnings

- Structuring a Python project across multiple modules
- Managing API keys securely with `.env` and platform secrets
- Defensive programming: handling every failure mode, not just the happy path
- Turning a working script into a web app with Streamlit: layout, tabs, sidebar widgets, and metric cards
- Keeping logic separate from display, so one backend can serve both a terminal and a web interface

---

_Built by [Alok](https://github.com/alok-kt)_