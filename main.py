from fastapi import FastAPI, status
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
        all = []
        for root, dirs, files in os.walk('src'):
            all.extend(files)
            all.extend(dirs)
    else:
        raise status.HTTP_404_NOT_FOUND


    return dir_data
