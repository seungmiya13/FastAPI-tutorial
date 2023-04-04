"""Body - Nested Models
"""
from typing import Dict, Set, List, Union

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str
    
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    #tags: List[str] = []
    tags: Set[str] = set()
    image: Union[List[Image], None] = None
    
class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    items: List[Item]


@app.post("/index-weights/")
async def create_index_weight(weights: Dict[int, float]):
    return weights

@app.post("images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images

@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer
    
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
