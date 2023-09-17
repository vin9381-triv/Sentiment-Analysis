import pymongo
from pymongo import MongoClient
import re
import contractions
from textblob import TextBlob
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

class DataProcessor:
    def __init__(self, source_uri, target_uri):
        self.source_client = MongoClient(source_uri)
        self.target_client = MongoClient(target_uri)

    def preprocess_text(self, text):
        # Lowercasing
        text = text.lower()

        # Expand contractions
        text = contractions.fix(text)

        # Tokenization
        tokens = word_tokenize(text)

        # Stopword Removal
        stop_words = set(stopwords.words("english"))
        tokens = [word for word in tokens if word not in stop_words]

        # Remove Special Characters and Numbers
        tokens = [re.sub(r'[^a-zA-Z]', '', word) for word in tokens if word.isalpha()]

        # Lemmatization
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(word) for word in tokens]

        # Join tokens back to text
        preprocessed_text = ' '.join(tokens)

        return preprocessed_text

    def process_and_store_data(self, source_db_name, target_db_name):
        source_db = self.source_client[source_db_name]
        target_db = self.target_client[target_db_name]

        # Iterate through collections in the source database
        for collection_name in source_db.list_collection_names():
            source_collection = source_db[collection_name]
            target_collection = target_db[collection_name]

        # Process and store data
            for entry in source_collection.find():
                title = entry.get('title', '')
                summary = entry.get('summary', '')  # Retrieve the "summary" field

            # Preprocess the summary field (you can replace 'self.preprocess_text' with your actual preprocessing function)
                preprocessed_summary = self.preprocess_text(summary)

            # Store the preprocessed data in the target collection
                target_collection.insert_one({
                    'title': title,
                    'summary': preprocessed_summary,  # Store the preprocessed summary
                    'published_date': entry.get('published_date', '')
                })

    def close_connections(self):
        self.source_client.close()
        self.target_client.close()

# Usage
if __name__ == "__main__":
    source_uri = "mongodb://localhost:27017/"
    target_uri = "mongodb://localhost:27017/"
    processor = DataProcessor(source_uri, target_uri)

    source_db_name = "final1"
    target_db_name = "summarized_clean"

    processor.process_and_store_data(source_db_name, target_db_name)
    processor.close_connections()