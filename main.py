from fastapi import FastAPI, HTTPException

import os

app = FastAPI()


@app.get("/api/{name_dir}")
async def get_dir_data(name_dir):
    if name_dir in os.listdir():
        all_dir = os.listdir(name_dir)
        options_of_dir = {}
        for i in range(len(all_dir)):
            options_of_dir[i] = f'name:{all_dir[i]}, ' \
                                f'type:{("file" if os.path.isfile(name_dir + "/" + all_dir[i]) else "folder")}, ' \
                                f'time:{os.stat(name_dir + "/" + all_dir[i]).st_ctime} '
        return options_of_dir
    else:
        raise HTTPException(status_code=404, detail='Wrong Data')
