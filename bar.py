from fastapi import FastAPI
from pydantic import BaseModel

# a POST method that takes one path parameter, one query parameter, and a request body containing a single field. Have this function return all three in a dict.
class Value(BaseModel):
    value: int

app = FastAPI()

@app.post("/{path}")
async def exercise_function(path: str, query: int, body: Value):
    return {"path": path, "query": query, "body": body}