""" Declare Request Example Data
"""
from typing import Union

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
from typing_extensions import Annotated

app = FastAPI()


class Item(BaseModel):
    name: str # = Field(example="Foo")
    description: Union[str, None] = None # = Field(default=None, example="A very nice item")
    price: float # = Field(example=35.4)
    tax: Union[float, None] = None # = Field(default=None, example=3.2)
    
    """
    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }
    """

@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary" : "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results

"""
async def update_item(item_id: int, item:Item):
    results = {"item_id": item_id, "item": item}
    return results
"""