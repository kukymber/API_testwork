from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

import os

app = FastAPI()


class Dir_Data(BaseModel):
    name: str
    type: str
    time: int


@app.get("/api/{name_dir}", response_model=Dir_Data)
async def get_dir_data(name_dir: str):
    dir_data = Dir_Data
    if name_dir in os.listdir():
        all_data = []
        for root, dirs, files in os.walk('src'):
            all_data.extend(files)
            all_data.extend(dirs)
    else:
        raise HTTPException(status_code=404, detail='Wrong Data')


    return dir_data
