# Socio-Economic News Sentiment Analysis

## Overview
This project aims to perform sentiment analysis on news articles related to socio-economic issues in India. The goal is to understand the sentiment and popularity of specific socio-economic topics mentioned in the articles. The project involves fetching articles, data preprocessing, and finding sentiment.

## Libraries Used
- **GoogleNews**: A Python library to fetch news articles from Google News.
- **Pymongo**: A Python library to connect to Mongo Db Compass.
- **TextBlob (NLTK)**: A library for performing sentiment analysis on text data.

## Installing Libraries
To get started with the project, you'll need to install the necessary libraries. Here are the installation steps for each library:

1. **GoogleNews**:
   The `pygooglenews` library can be installed using pip:
   
   ```bash
   pip install pygooglenews
   ```

2. **Pymongo**:
   You can install the `pymongo` library using pip:
   
   ```bash
   pip install pymongo
   ```

3. **TextBlob (NLTK)**:
   To install the `textblob` library along with the necessary NLTK corpora, run the following commands:
   
   ```bash
   pip install textblob
   python -m textblob.download_corpora
   ```

4. **Manually Installing pygooglenews**:
   
   If the pip command does not work, and you have to install the `pygooglenews` package and its dependencies, you can follow these steps:
   
   ```bash
   curl -O https://files.pythonhosted.org/packages/3f/d5/695ef6cd1da80e090534562ba354bc72876438ae91d3693d6bd2afc947df/pygooglenews-0.1.2.tar.gz
   tar -xvzf pygooglenews-0.1.2.tar.gz
   cd pygooglenews-0.1.2
   pip install feedparser --force
   pip install beautifulsoup4 --force
   pip install dateparser --force
   pip install requests --force
   pip install . --no-deps
   ```

   **Note**: You might need to adjust the installation steps based on your interpreter.

## Approach
1. **Fetching Articles**:
   - Utilize the GoogleNews library in the `collection.py` script to search for news articles related to socio-economic keywords in India.
   - Fetch article information, including titles, URLs, and snippets.
   - Script: [collection.py](Collection.py)

2. **Data Preprocessing**:
   - Utilize the `summarizer.py` script to summarize the collected articles.
   - Perform data preprocessing to clean and prepare the collected articles for analysis. This may involve:
     - Removing HTML tags and irrelevant content.
     - Tokenization: Splitting text into words or phrases.
     - Removing stopwords (common words like "and," "the," "in") to reduce noise.
     - Lemmatization or stemming to reduce words to their base form.
     - Handling missing data, if any.
   - Script: [summarizer.py](summarizing.py)

3. **Finding Sentiment**:
   - Utilize the `data_processor.py` script to preprocess the summarized data.
   - Utilize the `sentiment_analysis.py` script to perform sentiment analysis on the preprocessed articles.
   - Assign sentiment scores (positive, negative, neutral) to each article.
   - Store the sentiment information in a new database for further analysis.
   - Script (Preprocessing): [preprocessing.py](preprocessing.py)
   - Script (Sentiment Analysis): [sentiment_analysis.py](sentiment_analysis.py)

4. **User Interaction**:
   - Allow the user to input a socio-economic topic and choose whether they want to see sentiment analysis on an aggregate level or individual article level.
   - Script: [printing.py](printing.py)

### Implementation
- After data preprocessing, loop through the articles and use TextBlob to analyze the sentiment of each article.
- Store the sentiment scores along with article information (title, URL, etc.) in a new database using Pymongo.

### Additional Consideration
- Implement error handling for cases where sentiment analysis might not be accurate or if there are issues with data retrieval.

This project aims to provide valuable insights into the sentiment surrounding socio-economic topics in Indian news articles. By analyzing the sentiment and popularity of these topics, it can contribute to a better understanding of public perception and media coverage.

## Additional Resources
- For more information about the `pygooglenews` library, visit the [pygooglenews GitHub repository](https://github.com/kotartemiy/pygooglenews).
- To learn about the `newspaper` library for article extraction, refer to the [newspaper GitHub repository](https://github.com/codelucas/newspaper).

- To learn about the `newspaper` library for article extraction, refer to the [newspaper GitHub repository](https://github.com/codelucas/newspaper).
