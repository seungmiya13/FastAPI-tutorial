"""
Query Parameters and String Validations
"""
from typing import List, Union

from fastapi import FastAPI, Query
from pydantic import Required

app = FastAPI()


@app.get("/items/")
async def read_items(
    # q: Union[str, None]= Query(
    # default=None, min_length=3, max_length=50, regex="^fixedquery$"
    # )
    
    # q: str = Query(default=..., min_length=3) # value is required
    # q: str = Query(default=Required, min_length=3)

    #q: Union[List[str], None] = Query(default=["foo", "bar"])
    q : Union[str, None] = Query(
        default=None, 
        alias="item-query",
        title="Query string", 
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
        )
):
    '''
    query_items = {"q": q}
    return query_items
    '''
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
    #'''
'''
@app.get("/items/")
async def read_items(
    hidden_query: Union[str, None] = Query(default=None, include_in_schema=False)
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}
'''