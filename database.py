# Import Todo model from model module.
from model import Todo

# Import ObjectId class from bson module.
from bson import ObjectId

# Import MongoDB driver.
import motor.motor_asyncio


# Connect to MongoDB database using AsyncIOMotorClient.
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
# Select TodoList database.
database = client.TodoList
# Select todo collection within TodoList database.
collection = database.todo


# Define asynchronous function to fetch single TODO item by its title.
async def fetch_one_todo(title):
    # Use find_one method to query collection for document with given title.
    document = await collection.find_one({"title": title})  # Correctly formatted query.
    return document


# Define asynchronous function to fetch all TODO items from collection.
async def fetch_all_todos():
    todos = []
    # Use find method to retrieve all documents from collection.
    cursor = collection.find({})
    # Iterate asynchronously through cursor to retrieve each document.
    async for document in cursor:
        # Create Todo object from each document and append it to todo list.
        todos.append(Todo(**document))
    return todos


# Define asynchronous function to create new TODO item.
async def create_todo(todo):
    # Insert todo document into collection.
    # Insert todo document into collection.
    document = todo
    result = await collection.insert_one(document)
    # Convert ObjectId to string and add it to document.
    document["_id"] = str(document["_id"])  # Convert ObjectId to string
    return document


# Define asynchronous function to update TODO item description by its title.
async def update_todo(title, desc):
    # Use update_one method to update description of document with given title.
    await collection.update_one({"title": title}, {"$set": {"description": desc}})
    # Retrieve updated document.
    document = await collection.find_one({"title": title})
    return document


# Define asynchronous function to remove TODO item by its title.
async def remove_todo(title):
    # Use delete_one method to delete document with given title.
    await collection.delete_one({"title": title})
    return True
