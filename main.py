# Import necessary modules.
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Import Todo model.
from model import Todo

# App object
app = FastAPI()

# Import database functions for CRUD operations.
from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo,
)

# Define allowed origins for CORS.
origins = ['https://localhost:3000']


# Configure CORS middleware.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


# Define route for root endpoint.
# Each route is decorated with HTTP method decorator to specify HTTP method it responds to.
@app.get("/")
def read_root():
    return {"Ping": "Pong"}


# Define route to get all TODO items.
# GET
@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response


# Define route to get TODO item by its title.
# GET BY TITLE
@app.get("/api/todo{title}", response_model=Todo)
async def get_todo_by_title(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no TODO item with this title {title}")


# Define route to create new TODO item.
# POST
@app.post("/api/todo")
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad request")


# Define route to update TODO item by its title.
# PUT
@app.put("/api/todo/{title}/", response_model=Todo)
async def put_todo(title: str, desc: str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"There is no TODO item with this title {title}")


# Define route to delete TODO item by its title.
# DELETE
@app.delete("/api/todo/{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        print(f"Successfully deleted todo item with title: {title}")  # Log success message
        return "Successfully deleted todo item!"
    print(f"Failed to delete todo item with title: {title}")  # Log failure message
    raise HTTPException(404, f"There is no TODO item with this title {title}")