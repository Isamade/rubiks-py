from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import rotation

# 1. Create the application instance
app = FastAPI()

# a. Define the origins that are allowed to make requests
origins = [
    "http://localhost:8080",    # React default port
    "http://127.0.0.1:8080",
]

# b. Add the middleware to your app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Allows specific origins
    allow_credentials=True,           # Allows cookies/auth headers
    allow_methods=["*"],              # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],              # Allows all headers
)

# 2. Define a "path operation" (route)
@app.get("/")
def read_root():
    return {"Hello": "World"}

# 3. Add an endpoint with parameters
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

# 4. Add a POST endpoint
# Retrieve data from the request body and perform cube rotation
@app.post("/rotate")
async def rotate_axis(request: Request):
    # Parse the JSON body
    json_data = await request.json()
    # Convert to dictionary
    data = dict(json_data)
    # Extract move and cubeState
    move = data["move"]
    cubeState = data["cubeState"]
    # Validate move and cubeState
    # Perform rotation based on move
    if (move not in ['U', "U'", 'D', "D'", 'L', "L'", 'R', "R'", 'F', "F'", 'B', "B'"]):
        return {"error": "Invalid move"}
    elif (len(cubeState["pieces"]) != 27):
        return {"error": "Invalid cube state"}
    elif (move == 'U'):
        # Perform top clockwise rotation
        new_state = rotation.top_clockwise(list(cubeState["pieces"]))
        return {"pieces": new_state}
    elif (move == "U'"):
        # Perform top counter-clockwise rotation
        new_state = rotation.top_counter_clockwise(list(cubeState["pieces"]))
        return {"pieces": new_state}
    elif (move == 'D'):
        # Perform bottom clockwise rotation
        new_state = rotation.bottom_clockwise(list(cubeState["pieces"]))
        return {"pieces": new_state}