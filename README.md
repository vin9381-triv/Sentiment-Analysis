# Socio-Economic News Sentiment Analysis

## Overview
This project aims to perform sentiment analysis on news articles related to socio-economic issues in India. The goal is to understand the sentiment and popularity of specific socio-economic topics mentioned in the articles. The project involves fetching articles, extracting keywords, searching for related articles, and finally performing sentiment analysis.

## Libraries Used
- GoogleNews: A Python library to fetch news articles from Google News.
- BeautifulSoup: A library for web scraping and parsing HTML content.
- TextBlob (NLTK): A library for performing sentiment analysis on text data.
- Newspaper3k: A library to extract news articles based on URLs.

## Installing Libraries
To get started with the project, you'll need to install the necessary libraries. Here are the installation steps for each library:

1. **GoogleNews**:
   The `pygooglenews` library can be installed using pip:
   
   ```bash
   pip install pygooglenews
   ```

2. **BeautifulSoup**:
   You can install the `beautifulsoup4` library using pip:
   
   ```bash
   pip install beautifulsoup4
   ```

3. **TextBlob (NLTK)**:
   To install the `textblob` library along with the necessary NLTK corpora, run the following commands:
   
   ```bash
   pip install textblob
   python -m textblob.download_corpora
   ```

4. **Newspaper3k**:
   Install the `newspaper3k` library using pip:
   
   ```bash
   pip install newspaper3k
   ```

5. **Manually Installing pygooglenews**:
   
   If pip command does not work and you have t0 install the `pygooglenews` package and its dependencies, you can follow these steps:
   
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
   - Utilize the GoogleNews library to search for news articles related to socio-economic keywords in India.
   - Fetch article information including titles, URLs, and snippets.

2. **Extracting Keywords**:
   - For each article URL, use BeautifulSoup to scrape the article's content.
   - Utilize Natural Language Processing (NLP) techniques from the NLTK library to extract keywords or significant terms from the article.

3. **Searching for Related Articles**:
   - Use the extracted keywords to search Google News again, targeting articles specifically related to the socio-economic issue mentioned in the original article.
   - Fetch additional articles for analysis.

4. **Sentiment Analysis**:
   - Apply sentiment analysis using the TextBlob library on the fetched articles.
   - Analyze sentiment scores and patterns for each specific socio-economic issue.
   - Gain insights into how these issues are portrayed and perceived in the news.

This project aims to provide valuable insights into the sentiment surrounding socio-economic topics in Indian news articles. By analyzing the sentiment and popularity of these topics, it can contribute to a better understanding of public perception and media coverage.

## Additional Resources
- For more information about the `pygooglenews` library, visit the [pygooglenews GitHub repository](https://github.com/kotartemiy/pygooglenews).
- To learn about the `newspaper` library for article extraction, refer to the [newspaper GitHub repository](https://github.com/codelucas/newspaper).
