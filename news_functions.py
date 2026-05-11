import requests
import os
from dotenv import load_dotenv

import textwrap
from datetime import datetime

load_dotenv()
news_key = os.getenv("NEWS_API_KEY")

if not news_key:
    print("No key found!!")
    exit()


def fetch_news(city, num_articles=5):
    """Fetches the news based on city."""

    url = "https://newsapi.org/v2/everything"

    params = {
        "q": city,
        "apiKey": news_key,
        "pageSize": num_articles,
        "language": "en",
        "sortBy": "publishedAt"
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        articles = data.get('articles', [])

        if not articles:
            print(f"No news found for {city}!")
            return []
        
        return articles
        
    except requests.exceptions.HTTPError:
        if response.status_code == 401:
            print("Invalid API key!")
        
        else:
            print(f"News API error: {response.status_code}")
        return []

    except requests.exceptions.Timeout:
        print("News request timed out!")
        return []
    
    except requests.exceptions.ConnectionError:
        print("No internet connection!")
        return []



def fetch_category_news():
    """Fetches news based on category."""

    print("\nCategories: business, entertainment, health, science, sports, technology")
    your_category = input("Enter the category name you want: ").strip().lower()

    url = "https://newsapi.org/v2/top-headlines"
    
    params = {
        "category": your_category,
        "apiKey": news_key,
        "pageSize": 5,
        "language": "en",
        }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        articles = data.get('articles', [])

        if not articles:
            print(f"No headlines for the category {your_category}!")

        return articles
    
    except Exception as e:
        print(f"Error fetching category news: {e}")
        return []


def display_news(articles):
    """This displays the news when other two news functions' data is passed here."""

    if not articles:
        print("\nNo articles to display!")
        return
    
    for article in articles:
        source = article.get("source", {}).get("name", "Unknown")
        title = article.get("title", "N/A")
        news_url = article.get("url", "N/A")

        publishedDate = article.get("publishedAt", "N/A")
        if publishedDate != "N/A":
            dt = datetime.fromisoformat(publishedDate.replace('Z', '+00:00'))
            publishedDate = dt.strftime("%b %d, %Y at %I:%M %p")
        
        # If .get('description') returns None, 'or' will catch it and use "N/A".
        description = article.get("description") or "N/A"
        wrapped_description = textwrap.fill(description, width=52)

        print("=" * 52)
        print(f"\n -> {title}")
        print(" - ", source)
        print(" - ",publishedDate)
        print("-" * 52)
        print(wrapped_description)
        print("\nLink for full news -> ", news_url)