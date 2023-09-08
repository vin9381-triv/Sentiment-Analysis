from pygooglenews import GoogleNews
import datetime as dt
import time
from pymongo import MongoClient
socio_economic_keywords = [
    {"collection": "Poverty", "keywords": ["Poverty", "Deprivation", "Financial Hardship"]},
    {"collection": "Wealth Gap", "keywords": ["Wealth Gap", "Income Disparity", "Economic Inequality"]},
    {"collection": "Income Inequality", "keywords": ["Income Inequality", "Economic Disparity", "Wage Gap"]},
    {"collection": "Education Access", "keywords": ["Education Access", "Lack of Learning Opportunities", "Educational Inequality"]},
    {"collection": "Rape", "keywords": ["Rape", "Sexual Assault", "Gender-based Violence"]},
    {"collection": "Healthcare Access", "keywords": ["Healthcare Access", "Medical Services Availability", "Health Services Gap"]},
    {"collection": "Housing Crisis", "keywords": ["Housing Crisis", "Homelessness", "Lack of Shelter"]},
    {"collection": "Labor Rights", "keywords": ["Labor Rights", "Workers' Rights", "Employee Protections"]},
    {"collection": "Minimum Wage", "keywords": ["Minimum Wage", "Lowest Pay Rate", "Base Salary"]},
    {"collection": "Economic Empowerment", "keywords": ["Economic Empowerment", "Financial Independence", "Self-Sufficiency"]},
    {"collection": "Gender Pay Gap", "keywords": ["Gender Pay Gap", "Wage Disparity Between Genders", "Salary Inequity"]},
    {"collection": "Racial Discrimination", "keywords": ["Racial Discrimination", "Ethnic Bias", "Race-based Inequality"]},
    {"collection": "Access to Resources", "keywords": ["Access to Resources", "Resource Availability", "Equitable Access"]},
    {"collection": "Food Security", "keywords": ["Food Security", "Hunger", "Nutritional Insecurity"]},
    {"collection": "Social Mobility", "keywords": ["Social Mobility", "Opportunity Advancement", "Class Movement"]},
    {"collection": "Economic Development", "keywords": ["Economic Development", "Growth of Economy", "Progressive Advancement"]},
    {"collection": "Wealth Distribution", "keywords": ["Wealth Distribution", "Allocation of Resources", "Financial Sharing"]},
    # Add more entries in the same format for other issues
]

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['articles_6_months']

start_date = dt.date(2023, 1, 1)
end_date = dt.date(2023, 6, 30)

news = GoogleNews(country = 'in')

for cause in socio_economic_keywords:
    collection_name = cause["collection"]
    keywords = cause["keywords"]

    sdate = start_date
    while sdate <= end_date:
        edate = sdate + dt.timedelta(days=30)
        from_date = sdate.strftime('%Y-%m-%d')
        to_date = edate.strftime('%Y-%m-%d')

        for keyword in keywords:
            result = news.search(keyword, from_=from_date, to_=to_date)
  
            time.sleep(5)

            collection = db[collection_name]

            for entry in result['entries']:
                entry_dict = {
                    "keyword": keyword,
                    "from_date": from_date,
                    "to_date": to_date,
                    "title": entry['title'],
                    "link": entry['link'],
                    "published_date": entry.get('published', ''),
                    # Add more fields as needed
                }
                collection.insert_one(entry_dict)

        sdate = edate + dt.timedelta(days=30)

# Close the MongoDB connection
client.close()

print("Data insertion completed.")
