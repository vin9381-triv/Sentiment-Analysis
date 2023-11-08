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
    

# Connection to the MongoDB databases
source_mongo_uri = "mongodb://localhost:27017"
destination_mongo_uri = "mongodb://localhost:27017"

source_client = MongoClient(source_mongo_uri)
destination_client = MongoClient(destination_mongo_uri)

source_db = source_client['summarized_clean']
destination_db = destination_client['sentiment_analyzed_2']

# Get a list of collection names in the source database
source_collections = source_db.list_collection_names()

for source_collection_name in source_collections:
    # Select the source collection from where you want to retrieve articles
    source_collection = source_db[source_collection_name]

    # Create a new collection in the destination database with the same name
    destination_collection = destination_db[source_collection_name]

    articles = source_collection.find({})

    for article in articles:
        text = article.get("summary")
        if text:
            analyzer = SentimentIntensityAnalyzer()
            sentiment = analyzer.polarity_scores(text)

            sentiment_label = get_sentiment_label(sentiment['compound'])

            new_document = {
                "title": article.get("title"),
                "summary": text,
                "sentiment_label": sentiment_label,
                "sentiment_scores": sentiment["compound"]
                
            }
            destination_collection.insert_one(new_document)

    print(f"Sentiment analysis results for collection '{source_collection_name}' have been stored in the '{source_collection_name}' collection in the destination database.")
