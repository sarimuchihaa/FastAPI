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


# GET endpoint to retrieve all items.
@app.get("/items/")
async def get_items():
    return items_db


# Post endpoint to create new item.
# Request body parameter is item.
@app.post("/items/")
async def create_item(item: Item):
    # Convert Pydantic model Item to dictionary.
    item_dict = item.dict()
    # If tax is provided, calculate price with tax and add it to dictionary.
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
        # Add the item to the in-memory database
        items_db.append(item_dict)
    # Return dictionary containing item data, possibly with price_with_tax included.
    return item_dict
