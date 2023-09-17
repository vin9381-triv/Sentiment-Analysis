import pymongo
import time
from newspaper import Article, Config
from newspaper.article import ArticleException

class Summarizing:
    def __init__(self, mongo_uri):
        self.client = pymongo.MongoClient(mongo_uri)

    def summarize_article(self, url):
        article = Article(url,  language='en')
        time.sleep(2)
        try:
            article.download()
            article.parse()
            article.nlp()
            return article.summary
        except ArticleException as e:
            print(f"Failed to process article")
            return None
        
    def process_collection(self, db_name, batch_size=50, break_interval=30):
        db = self.client[db_name]
        collections = db.list_collection_names()
        for collection_name in collections:
            collection = db[collection_name]
            print(f"Processing collection: {collection_name}")
            query = {"$or": [{"summary": {"$exists": False}}, {"summary": ""}]}
            articles = list(collection.find(query))
            num_articles = len(articles)
            summary_count = 0  # Initialize the count of articles with summaries
            for batch_start in range(0, num_articles, batch_size):
                batch_end = min(batch_start + batch_size, num_articles)
                batch = articles[batch_start:batch_end]
                for article in batch:
                    article_id = article["_id"]
                    article_url = article["link"]
                    new_summary = self.summarize_article(article_url)
                    if new_summary:
                        collection.update_one({"_id": article_id}, {"$set": {"summary": new_summary}})
                        summary_count += 1  # Increment the count of articles with summaries
                        print(f"Summary added to article with id: {article_id}")
                if batch_end < num_articles:
                    print(f"Waiting for {break_interval} seconds before processing the next batch...")
                    time.sleep(break_interval)  # Break between batches
            # Print the count of articles with summaries for the current collection
            print(f"Collection '{collection_name}' - Summaries added for {summary_count}/{num_articles} articles.")

if __name__ == "__main__":
    mongo_uri = "mongodb://localhost:27017/"
    summarizer = Summarizing(mongo_uri)
    # Specify your database name
    db_name = "final1"
    summarizer.process_collection(db_name)
