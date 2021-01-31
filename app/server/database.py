from pymongo import MongoClient
import json
import os
from bson.objectid import ObjectId

secrets_dir = os.path.dirname(__file__)
rel_path = "../../secrets.json"
abs_file_path = os.path.join(secrets_dir, rel_path)

secrets = json.load(open(abs_file_path))
MONGO_SERVICE_KEY = secrets["mongo-service-key"]
MONGO_DETAILS = "mongodb+srv://worker:" + MONGO_SERVICE_KEY + "@development.zukcn.mongodb.net/TAMUhack?retryWrites=true&w=majority"

client = MongoClient(MONGO_DETAILS)
db = client.TAMUhack

author_collection = db.get_collection("authors")
source_collection = db.get_collection("sources")

# helper methods

def author_helper(author) -> dict:
    return {
        "id": str(author["_id"]),
        "fullname": author["fullname"],
        "rating": author["rating"]
    }

def source_helper(source) -> dict:
    return {
        "id": str(source["_id"]),
        "source": source["source"],
        "rating": source["rating"]
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

# Retrieve an author with a matching ID
async def retrieve_author(id: str) -> dict:
    author = author_collection.find_one({"_id": ObjectId(id)})
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