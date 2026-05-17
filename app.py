import streamlit as st
from weather_functions import fetch_weather
from news_functions import fetch_news, fetch_category_news, display_news

st.set_page_config(
    page_title="Weather & News Dashboard",
    page_icon="🌤️",
    layout="wide"
)

st.markdown("""
    <style>
        body { background-color: #0a0a0a; }
        .block-container { padding-top: 2rem; }
        h1, h2, h3 { font-family: 'Courier New', monospace; }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("⚙️ Controls")
    st.markdown("---")

    st.subheader("🌍 Weather")
    city_input = st.text_input("Enter city name", placeholder="e.g. London, Tokyo...")

    st.markdown("---")

    st.subheader("📰 News")
    news_mode = st.radio("Search by", ["City", "Category"])

    if news_mode == "City":
        news_city = st.text_input("News city", placeholder="e.g. Mumbai...")
    else:
        news_category = st.selectbox("Category", [
            "Business", "Entertainment", "Health",
            "Science", "Sports", "Technology"
        ])

    num_articles = st.slider("number of articles", 1, 20, 5)

    st.markdown("---")
    search_btn = st.button("🔍 Search", use_container_width=True)

st.title("🌤️ Weather & News Dashboard")
st.markdown("---")

tab1, tab2 = st.tabs(["🌡️ Weather", "📰 News"])

with tab1:
    st.subheader("Your City - Thrissur")
    default_data = fetch_weather("thrissur")
    
    if default_data:
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("🌡️ Temperature", f"{default_data['main']['temp']:.1f} °C")
        col2.metric("🤔 Feels Like", f"{default_data['main']['feels_like']:.1f} °C")
        col3.metric("💧 Humidity", f"{default_data['main']['humidity']}%")
        col4.metric("🌬️ Wind Speed", f"{default_data['wind']['speed']} m/s")

    st.markdown("---")
    st.subheader("Search Any City")

    if search_btn and city_input:
        weather_data = fetch_weather(city_input)
        if weather_data:
            st.markdown(f"### {weather_data['name']}, {weather_data['sys']['country']}")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("🌡️ Temperature", f"{weather_data['main']['temp']:.1f} °C")
            col2.metric("🤔 Feels Like", f"{weather_data['main']['feels_like']:.1f} °C")
            col3.metric("💧 Humidity", f"{weather_data['main']['humidity']}%")
            col4.metric("🌬️ Wind Speed", f"{weather_data['wind']['speed']} m/s")
        else:
            st.error("City not found! Check the spelling and try again.")
    elif search_btn and not city_input:
        st.warning("Please enter a city name in the sidebar.")

with tab2:
    st.subheader("Latest News")

    if search_btn:
        if news_mode == "City":
            if news_city:
                articles = fetch_news(news_city, num_articles)
            else:
                st.warning("Please enter a city name for news.")
                articles = []
        else:
            articles = fetch_category_news(news_category, num_articles)

        if articles:
            for article in articles:
                with st.expander(article.get("title", "No title")):
                    source = article.get("source", {}).get("name", "Unknown")
                    published = article.get("publishedAt", "")[:10]
                    description = article.get("description") or "No description available."
                    url = article.get("url", "")

                    st.caption(f"📰 {source} . 🗓️ {published}")
                    st.write(description)
                    if url:
                        st.markdown(f"[Read full article ->]({url})")
        else:
            st.info("Use the sidebar to search news by city or category")