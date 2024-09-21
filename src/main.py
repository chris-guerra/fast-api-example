from enum import Enum
from fastapi import FastAPI

#--------------------------------------------------------------------
# Code from part 4 of FastAPI course
#--------------------------------------------------------------------

# We create a class with some model name, in this example ModelName
# The convention is to use caps for the start of each word.
class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

app = FastAPI() # We create our app, this is an instance of the FastAPI class

# We will go into what 'get' is in a bit, "/" is our file path
# for example if we use "/items/foo" we would have to acces the URL
# http://some_url/items/foo to access our method
@app.get("/")
# Define an async function named 'root' to handle the requests.
async def root():
    # Return a JSON response with a message "Hello World".
    return {"message": "Hello World"}

# Between {} we have our dynamic code
@app.get("/items/{item_id}")
# Notice we use the same variable "item_id" and declare a data type
async def read_items(item_id: int):
    # We return a json with the item_id
    return {"item_id": item_id}

# First we declare a fixed path after users
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

# Here we declare a dynamic path  after userswith integers
# to see the user_id
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}

@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]

# In this method we have a custom ModelName that should be
# one of the three options we set up in our ModelName Class
@app.get("/models/{model_name}")
# Our dtype this time is custom as ModelName instead of a traditional
# dtype like str or int
async def get_model(model_name: ModelName):
    # Our method will return a JSON with the model name and a message.
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    elif model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    else:
      return {"model_name": model_name, "message": "Have some residuals"}

# Adding File Paths
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
