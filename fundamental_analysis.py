import requests
from textblob import TextBlob

# Function to get economic indicators (dummy function, can be expanded)
def get_economic_indicators():
    indicators = {
        'GDP': 21.43,  # Trillion USD
        'Unemployment Rate': 5.4,  # Percentage
        'Inflation Rate': 2.5  # Percentage
    }
    return indicators

# Function to analyze sentiment from financial news
def analyze_sentiment(news_article):
    analysis = TextBlob(news_article)
    return analysis.sentiment

# Example usage
if __name__ == "__main__":
    indicators = get_economic_indicators()
    print("Economic Indicators:", indicators)

    news_article = "The stock market is seeing great potential for growth this year."
    sentiment = analyze_sentiment(news_article)
    print("Sentiment of Article:", sentiment)