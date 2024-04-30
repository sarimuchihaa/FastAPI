from fastapi import FastAPI
from pydantic import BaseModel


# Define Pydantic model called Item.
class Item (BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


# Create instance of FastAPI.
app = FastAPI()


# In-memory database to store items (for demonstration purposes).
items_db = []


# Get endpoint to retrieve all items.
@app.get("/items/")
async def get_items():
    return items_db


# GET endpoint to retrieve single item by name.
# Path parameters are used to extract data from URL path.
# Path parameter is name.
@app.get("/items/{name}")
async def get_item_by_name(name: str):
    for item in items_db:
        if item.name == name:
            return item
    return {"message": "Item not found"}


# Post endpoint to create new item.
# Request body parameter is item.
@app.post("/items/")
async def create_item(item: Item):
    items_db.append(item)
    return item


# PUT endpoint to update existing item by name.
# Request body parameter are used to receive data in body of HTTP request.
# Request body parameter is updated_item.
@app.put("/items/{name}")
async def update_item(name: str, updated_item: Item):
    for item in items_db:
        if item.name == name:
            # Update item attributes with new values.
            item.name = updated_item.name
            item.description = updated_item.description
            item.price = updated_item.price
            item.tax = updated_item.tax
            return item
    return {"message": "Item not found"}


# DELETE endpoint to delete existing item by name.
# Path parameter is name.
@app.delete("/items/{name}")
async def delete_item(name: str):
    global items_db
    # Filter out item with specified name from items_db list.
    items_db = [item for item in items_db if item.name != name]
    return {"message": "Item deleted successfully"}
