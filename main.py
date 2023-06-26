import os
import sys
import json
import uvicorn
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

@app.get("/")
async def root():
    return {"Hello! Welcome to dev6!"}

@app.get("/response")
async def get_response():
    return json.loads(open("testInfo.json").read())

@app.get("/directory/{path:path}", response_class=FileResponse)
async def access_contents(path: str):
    return path

@app.post("/data")
async def store_data(data: list):
    file_name = f"data_{time.time()}.json"
    json_data = json.dumps(data)
    with open(file_name, "w") as file:
        file.write(json_data)
    return {"message": "Data stored successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(sys.argv[1]))