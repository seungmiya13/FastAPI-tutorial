"""
쿼리 매개변수
"""
from typing import Union

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

'''
@app.get("/items/")
async def read_item(skip: int=0, limit: int=10):
    return fake_items_db[skip : skip + limit]

# http://127.0.0.1:8000/items/?skip=0&limit=10
'''

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None]= None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/users/{item_id}")
async def read_user_item(
    item_id: str, needy:str, skip: int=0, limit: Union[int, None] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
