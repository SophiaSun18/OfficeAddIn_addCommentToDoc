import os
import sys
import json
import uvicorn
import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# The start up message
@app.get("/")
async def root():
    return {"Hello! Welcome to dev6!"}

# Get access to files on the server. Only for development use.
@app.get("/directory/{path:path}", response_class=FileResponse)
async def access_contents(path: str):
    return path

# Send data to the server and store data in a new .json file.
# .json named by the time that the data is uploaded.
@app.post("/data")
async def store_data(data: list):
    os.chdir("/home/zs35/storeData")
    file_name = f"data_{time.time()}.json"
    json_data = json.dumps(data)
    with open(file_name, "w") as file:
        file.write(json_data)
    return {"message": "Data stored successfully"}

# Get the response (AI-generated comments) from the server.
# For now, loading an existing file as response.
@app.get("/response")
async def get_response():
    os.chdir("/home/zs35/OfficeAddIn_addCommentToDoc")
    return json.loads(open("testInfo.json").read())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(sys.argv[1]))