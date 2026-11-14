from fastapi import FastAPI

app = FastAPI(title="Items API")

items = [
    {"id": 1, "name": "Sample Item"},
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


# TODO: Add GET /items, POST /items, and GET /items/{item_id}
