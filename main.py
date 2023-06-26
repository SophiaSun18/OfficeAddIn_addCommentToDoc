import sys
import json
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()
root_path = "/OfficeAddIn_addCommentToDoc/assets/"

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/")
# async def root():
#     return {"Hello World!"}

@app.get("/info")
async def get_info():
    return json.loads(open("testInfo.json").read())

@app.get("/", response_class=FileResponse)
async def root():
    return root_path

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(sys.argv[1]))