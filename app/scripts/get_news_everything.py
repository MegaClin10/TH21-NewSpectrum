from pymongo import MongoClient
from newsapi import NewsApiClient
import json

def get_news_everything(query):
    newsapi = NewsApiClient(api_key=grab_credentials('news-api-key'))

    data = check_database_existing(query)
    in_database = data["in_database"]
    db = data["database"]

    if in_database:
        # return database
        return list(data["documents"])
    else:
        # perform search
        all_articles = newsapi.get_everything(q=query, sort_by="relevancy", language='en')

        # add to database
        for article in all_articles["articles"]:
            article["query"] = query.lower()
            db['cached-news'].insert_one(article)

def check_database_existing(query):
    # check the database
    db = connect_to_mongo_db()
    
    collection=db['cached-news']
    cursor = collection.find({'query': query})

    data = {
        "in_database": cursor.count() > 0,
        "database" : db,
        "documents" : cursor
    }

    return data

def connect_to_mongo_db():
    client = MongoClient("mongodb+srv://worker:" + grab_credentials("mongo-service-key") + "@development.zukcn.mongodb.net/TAMUhack?retryWrites=true&w=majority")
    db = client.TAMUhack
    return db

def grab_credentials(key):
    secrets = json.load(open("../../secrets.json"))
    return secrets[key]