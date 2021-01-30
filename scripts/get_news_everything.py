from pymongo import MongoClient
from newsapi import NewsApiClient
import json

def get_news_everything(query):
    in_database = check_database_existing(query)
    print(in_database)
    #if in_database:
        # return database
    #else:
        # perform search
        # add to database

def check_database_existing(query):
    # check the database
    db = connect_to_mongo_db()
    
    collection=db['cached-news']
    cursor = collection.find({'query': query})

    return cursor.count() > 0

def connect_to_mongo_db():
    client = MongoClient("mongodb+srv://worker:" + grab_credentials() + "@development.zukcn.mongodb.net/TAMUhack?retryWrites=true&w=majority")
    db = client.TAMUhack
    return db

def grab_credentials():
    secrets = json.load(open("../secrets.json"))
    return secrets["mongo-service-key"]

get_news_everything("BITCOIN".lower())