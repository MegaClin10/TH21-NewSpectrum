from pymongo import MongoClient
import json
import os
from bson.objectid import ObjectId
from decouple import config
from app.scripts.get_news_everything import get_news_everything

MONGO_DETAILS = config('MONGO_DETAILS')

client = MongoClient(MONGO_DETAILS)
db = client.TAMUhack

author_collection = db.get_collection("authors")
source_collection = db.get_collection("sources")
article_collection = db.get_collection("cached-news")

# helper methods

def author_helper(author) -> dict:
    return {
        "id": str(author["_id"]),
        "fullname": author["fullname"],
        "rating": author["rating"],
        "consr_votes": author["consr_votes"],
        "libr_votes": author["libr_votes"],
        "neutr_votes": author["neutr_votes"]
    }

def source_helper(source) -> dict:
    return {
        "id": str(source["_id"]),
        "source": source["source"],
        "rating": source["rating"]
    }

def article_helper(article) -> dict: 
    return {
        "id": str(article["_id"]),
        "source": article["source"],
        "author": article["author"],
        "title": article["title"],
        "description": article["description"],
        "url": article["url"],
        "urlToImage": article["urlToImage"],
        "publishedAt": article["publishedAt"],
        "content": article["content"]
    }

# CRUD operations

# Retrieve all authors in the database
async def retrieve_authors():
    authors = []
    for author in author_collection.find():
        authors.append(author_helper(author))
    return authors

# Add a new author into the database
async def add_author(author_data: dict) -> dict:
    author = author_collection.insert_one(author_data)
    new_author = author_collection.find_one({"_id": author.inserted_id})
    return author_helper(new_author)

# Retrieve an author with a matching name
async def retrieve_author(name: str) -> dict:
    author = author_collection.find_one({"fullname": name})
    if author:
        return author_helper(author)

# Update an author with a matching ID
async def update_author(id: str, data: dict):
    # Return false if an empty request body is sent
    if len(data) < 1:
        return False
    author = author_collection.find_one({"_id": ObjectId(id)})
    if author:
        updated_author = author_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )

        if updated_author:
            return True
        return False

# Delete a author from the database
async def delete_author(id: str):
    author = author_collection.find_one({"_id": ObjectId(id)})
    if author:
        author_collection.delete_one({"_id": ObjectId(id)})
        return True

# Retrieve all sources in the database
async def retrieve_sources():
    sources = []
    for source in source_collection.find():
        sources.append(source_helper(source))
    return sources

# Add a new source into the database
async def add_source(source_data: dict) -> dict:
    source = source_collection.insert_one(source_data)
    new_source = source_collection.find_one({"_id": source.inserted_id})
    return source_helper(new_source)

# Retrieve an source with a matching ID
async def retrieve_source(id: str) -> dict:
    source = source_collection.find_one({"_id": ObjectId(id)})
    if source:
        return source_helper(source)

# Update an source with a matching ID
async def update_source(id:str, data: dict):
    # Return false if an empty request body is sent
    if len(data) < 1:
        return False
    source = source_collection.find_one({"_id": ObjectId(id)})
    if source:
        updated_source = source_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )

        if updated_source:
            return True
        return False

# Delete a source from the database
async def delete_source(id: str):
    source = author_collection.find_one({"_id": ObjectId(id)})
    if source:
        source_collection.delete_one({"_id": ObjectId(id)})
        return True

# Retrieves all articles in the database
async def retrieve_articles(q: str):
    articles = []
    get_news_everything(q)
    for article in article_collection.find({'query': q}):
        articles.append(article_helper(article))
    return articles

# Retrieves an article with a matching ID
async def retrieve_article(id: str) -> dict:
    article = article_collection.find_one({"_id": ObjectId(id)})
    if article:
        return article_helper(article)