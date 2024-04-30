# Import BaseModel class from Pydantic.
from pydantic import BaseModel


# Define class named Todo that inherits from BaseModel.
class Todo(BaseModel):
    # Define attributes of Todo class: title and description.
    title: str
    description: str
