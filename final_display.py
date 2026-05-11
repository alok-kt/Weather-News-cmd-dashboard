from weather_functions import weather_display, my_weather
from news_functions import fetch_news, fetch_category_news, display_news
import time

def main():

    my_weather()

    while True:
        print("\n-------------")
        print("MENU OPTIONS")
        print("-------------")
        print("\n1. Search weather by CITY")
        print("2. Search for News by CITY")
        print("3. Search News by CATEGORY")
        print("4. EXIT")

        choose_options = input("\nSelect options (1 - 4): ").strip()

        if choose_options == '1':
            print("\nWeather by CITY Search - Selected")
            time.sleep(2)
            city = input("\nEnter the name of the city: ").strip()
            time.sleep(2)
            weather_display(city)

        elif choose_options == '2':
            print("\nNews by CITY Search - Selected")
            time.sleep(1)
            city = input("\nEnter the name of the CITY: ").strip().lower()
            news_articles = fetch_news(city)
            print("\nFetching your News...")
            time.sleep(2)
            display_news(news_articles)

        elif choose_options == '3':
            print("\nNews by CATEGORY - Seleceted")
            time.sleep(1)
            category_news = fetch_category_news()
            time.sleep(2)
            print("\nFetching your News...")
            time.sleep(2)
            display_news(category_news)

        elif choose_options == '4':
            print("\nGoodbye. Exiting...")
            time.sleep(2)
            break

        else:
            time.sleep(1)
            print("\nInvalid selection! Enter 1, 2, 3 or 4 ONLY!")

if __name__ == "__main__":
    main()