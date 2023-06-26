import os
import sys
import json
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"Hello! Welcome to dev6!"}

@app.get("/info")
async def get_info():
    return json.loads(open("testInfo.json").read())

# @app.get("/", response_class=FileResponse)
# async def root():
#     return root_path

@app.get("/directory/{path:path}")
async def access_contents(path:str):
    directory_path = os.path.join(os.getcwd(), path)
    if (os.path.isdir(directory_path)):
        contents = os.listdir(directory_path)
    elif (os.path.isfile(directory_path)):
        content = directory_path
    return content

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(sys.argv[1]))