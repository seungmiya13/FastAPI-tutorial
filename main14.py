"""Response Model - Return Type"""
from typing import Any, List, Union

from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel, EmailStr

app = FastAPI()

"""
## 4 Other Return Type Annotations
# Return a Response Directly
@app.get("/portal", response_model=None) # disable response model
async def get_portal(teleport:bool = False) -> Response: # -> Union[Response, dict]: # fail 
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})


# Annotate a Response Subclass
@app.get("/teleport")
async def get_teleport() -> RedirectResponse:
    return RedirectResponse()
"""


"""
## 3 Return Type and Data Filtering
class BaseUser(BaseModel):
    username: str 
    email: EmailStr
    full_name: Union[str, None] = None


class UserIn(BaseUser):
    password: str
    
    
@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user
"""


"""
## 2 response_model Priority
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel): # add output model without password
    username: str
    email: EmailStr
    full_name: Union[str, None] = None
    
    
@app.post("/user/", response_model=UserOut) 
async def create_user(user: UserIn) -> Any:
    return user
    # reseponse_model(UserOut) take priority than return type(UserIn)
"""



## 1 - return type & response_model Parameter
## 4 - Response Model encoding parameters
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5 # Union[float, None] = None
    tags: List[str] = []
    
    
items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bartenders", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz", 
        "description": "There goes my baz", 
        "price": 50.2, 
        "tax": 10.5,
    },
}
    

@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"}, # just include these set
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"}) # exclude these set of all
async def read_item_public_data(item_id: str):
    return items[item_id]

    
@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True) # only the values actually set
async def read_item(item_id: str):
    return items[item_id]


@app.post("/items/", response_model=Item) # use response_model Parameter
async def create_item(item: Item) -> Any: # -> Item:
    return item


@app.get("/items", response_model=List[Item])
async def read_items() -> Any: # -> List[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]
