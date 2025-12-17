"""
Demonstrates common HTTP methods in FastAPI
using basic request bodies (no Pydantic models).

This example focuses on HTTP semantics rather than data validation.
"""

from fastapi import FastAPI, Body                                   # Body contains the information that will be used to create new/ update existing record

app = FastAPI()
    
@app.get("/items")
async def get_items():
    """
    Retrieve a list of items.
    """
    return {"message": "GET request received"}


@app.post("/items")
async def create_item(item: dict = Body(...)):
    """
    Create a new item using a basic request body.
    """
    return {
        "message": "POST request received",
        "item": item
    }


@app.put("/items/{item_id}")                                        #{item_id} is the path paramter
async def update_item(item_id: int, item: dict = Body(...)):        # item is used to assign the value that is provided. 
    """
    Replace an existing item completely.
    """
    return {
        "message": "PUT request received",
        "item_id": item_id,
        "item": item
    }


@app.patch("/items/{item_id}")                                      #{item_id} is the path paramter
async def partially_update_item(item_id: int, item: dict = Body(...)):
    """
    Partially update an existing item.
    """
    return {
        "message": "PATCH request received",
        "item_id": item_id,
        "item": item
    }


@app.delete("/items/{item_id}")                                     #{item_id} is the path paramter
async def delete_item(item_id: int):
    """
    Delete an item.
    """
    return {
        "message": "DELETE request received",
        "item_id": item_id
    }
