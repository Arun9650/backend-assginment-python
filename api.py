from fastapi import FastAPI
from pymongo import MongoClient
from fastapi import APIRouter
from bson import ObjectId

router = APIRouter()

MONGODB_URL = "mongodb+srv://ArunKumar:ArunKumar@cluster0.giujeng.mongodb.net"  # Replace this with your MongoDB connection string
DATABASE_NAME = "data-base-name"  # Replace this with your database name






def get_database():
    client = MongoClient(MONGODB_URL)
    database = client[DATABASE_NAME]
    return database

@router.get("/{item_id}")
async def read_item(item_id: str):
    db = get_database()
    # print("this is db", db)
    collection = db["collection-name"]
    # print('this is collection', collection)
    item = collection.find_one({"_id": ObjectId(item_id)})  
    print('item', item);
    # item = list(collection.find({}))
    return {"item": item}





@router.get("/")
async def get_all_items():
    db = get_database()
    collection = db['collection-name']
    items = list(collection.find({}))  # Fetch all documents in the collection as a list
    # Convert ObjectId to string for each item in the list
    items = [{**item, '_id': str(item['_id'])} for item in items]
    return {"items": items}





