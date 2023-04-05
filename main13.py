"""Header Parameters"""
from typing import List, Union

from fastapi import FastAPI, Header 

app = FastAPI()


# 중복 헤더 
@app.get("/items/")
async def read_items(x_token: Union[List[str], None] = Header(default=None)):
    return {"X-Token values": x_token}


"""# _ -> - 으로 자동변환을 비활성화
@app.get("/items/")
async def read_items(strange_header: Union[str, None] = Header(default=None, convert_underscores=False)):
    return {"strange_header": strange_header} 
"""