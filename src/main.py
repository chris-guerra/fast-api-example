from fastapi import FastAPI
from typing import Union



app = FastAPI()


# We add an example of a path parameter in this function
@app.get("/items/{item_id}")
async def read_item(item_id: Union[int, str]) -> dict:
    """
    """
    return {"item_id": item_id}


