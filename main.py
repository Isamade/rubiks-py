from fastapi import FastAPI
from typing import Iterable
from rotation import top_clockwise

# 1. Create the application instance
app = FastAPI()

# 2. Define a "path operation" (route)
@app.get("/")
def read_root():
    return {"Hello": "World"}

# 3. Add an endpoint with parameters
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

# 4. Add a POST endpoint
# Retrieve data from the request body
# Here, we expect a JSON body with 'move' and 'cube_state' fields
# move is a string, cube_state is an iterable (like a list)
@app.post("/rotate")
def rotate_axis(move: str, cube_state: Iterable[object]):
    if (move not in ['U', "U'", 'D', "D'", 'L', "L'", 'R', "R'", 'F', "F'", 'B', "B'"]):
        return {"error": "Invalid move"}
    elif (len(cube_state) != 54):
        return {"error": "Invalid cube state"}
    elif (move == 'U'):
        new_state = top_clockwise(list(cube_state))
        return {"new_state": new_state}