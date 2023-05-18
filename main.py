from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import cloudinary
import cloudinary.api

app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cloudinary.config(secure=True)

@app.get("/")
async def root():
    return {"message": "API for cloudinary"}
def get_resources(expression, sort_by, max_results, fields, next_cursor):

    all_resources = []
    result = cloudinary.api.resources(expression=expression, max_results=max_results, sort_by=sort_by, fields=fields, type = 'upload')
    all_resources.extend(result["resources"])
    while "next_cursor" in result and result["next_cursor"] is not None:
        print(result["next_cursor"])
        result = cloudinary.api.resources(expression=expression, max_results=max_results, sort_by=sort_by, fields=fields, type = 'upload', next_cursor = result["next_cursor"])
        all_resources.extend(result["resources"])

    return all_resources

@app.get("/resources/")
async def read_resources(expression=None, sort_by=None, max_results=50, with_field=None, next_cursor=None):
    return get_resources(expression, sort_by, int(max_results), with_field, next_cursor)
