from pymongo import MongoClient

source_mongo_uri = "mongodb://localhost:27017"

source_client = MongoClient(source_mongo_uri)
db = source_client['sentiment_analyzed_2']


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


while True:
    collections = db.list_collection_names()

    print("Available collections:")
    for idx, collection_name in enumerate(collections, start=1):
        print(f"{idx}. {collection_name}")

    collection_index = int(input("Select a collection (1 - {}): ".format(len(collections))) or 1) - 1

    if collection_index < 0 or collection_index >= len(collections):
        print("Invalid collection selection. Please try again.")
        continue

    selected_collection = db[collections[collection_index]]
    analysis_type = input("Analyze individually or as a whole? (i/a): ")

    if analysis_type == "i":
        articles = selected_collection.find({})
        for article in articles:
            article_title = article.get('title')
            sentiment_label = article.get('sentiment_label')
            sentiment_score = article.get('sentiment_scores')

            print(f"Article Title: {article_title}")
            print(f"Article Sentiment: {sentiment_label}")
            print(f"Article Sentiment Score: {sentiment_score}")
            print("\n")

    elif analysis_type == "a":
        sentiment_scores_list = []
        for article in selected_collection.find({}):
            sentiment_score = article.get('sentiment_scores')
            sentiment_scores_list.append(sentiment_score)

        if sentiment_scores_list:
            average_sentiment_score = sum(sentiment_scores_list) / len(sentiment_scores_list)
            average_sentiment_label = get_sentiment_label(average_sentiment_score)
            print(f"\nA")
            print(f"\nAggregate Sentiment Score: {average_sentiment_score}")
            print(f"Aggregate Sentiment Label: {average_sentiment_label}")
        else:
            print("No sentiment scores found in this collection.")

    else:
        print("Invalid analysis type. Please enter 'i' for individual analysis or 'a' for aggregate analysis.")

    print("\n")