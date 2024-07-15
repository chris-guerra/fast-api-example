""" Main file"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Handle requests to the root URL"""
    return {"message": "Hello World"}
