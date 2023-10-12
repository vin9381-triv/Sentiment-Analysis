from pymongo import MongoClient
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_sentiment_label(compound_score):
    if compound_score >= 0.9:
        return "Highly Positive"
    elif compound_score >= 0.7:
        return "Very Positive"
    elif compound_score >= 0.5:
        return "Positive"
    elif compound_score >= 0.2:
        return "Slightly Positive"
    elif compound_score >= -0.2:
        return "Neutral"
    elif compound_score >= -0.5:
        return "Slightly Negative"
    elif compound_score >= -0.7:
        return "Negative"
    elif compound_score >= -0.9:
        return "Very Negative"
    else:
        return "Highly Negative"

mongoPath = "mongodb://localhost:27017"
client = MongoClient(mongoPath)
db = client['summarized_clean']
collections = db.list_collection_names()

while True:
    print("Available collections:")
    for idx, collection_name in enumerate(collections, start=1):
        print(f"{idx}. {collection_name}")

    collection_index = int(input("Select a collection (1 - {}): ".format(len(collections))) or 1) - 1

    if collection_index < 0 or collection_index >= len(collections):
        print("Invalid collection selection. Please try again.")
        continue

    selected_collection = db[collections[collection_index]]

    print(f"\nSelected Collection: {collections[collection_index]}")

    articles = selected_collection.find({})

    total_polarity = 0
    total_subjectivity = 0
    article_count = 0

    for article in articles:
        text = article.get("summary")
        if text:
            analyzer = SentimentIntensityAnalyzer()
            sentiment = analyzer.polarity_scores(text)
            
            sentiment_label = get_sentiment_label(sentiment['compound'])

            print(f"Article Title: {article.get('title')}")
            print(f"Article Sentiment: {sentiment_label}")
            print("\n")

            total_polarity += sentiment['compound']
            article_count += 1

    if article_count > 0:
        average_polarity = total_polarity / article_count
        average_label = get_sentiment_label(average_polarity)

        print("Overall Collection Sentiment:")
        print(f"Average Polarity of Articles: {average_label}")
    else:
        print("No articles with sentiment found in the selected collection.")

    choice = input("Do you want to select another collection? (yes/no): ")
    if choice.lower() != "yes":
        break
