from fastapi import FastAPI, HTTPException

app = FastAPI(title="Testing Practice API")

items = [
    {"id": 1, "name": "Notebook"},
    {"id": 2, "name": "Pencil"},
]


def format_name(name: str) -> str:
    """Trim extra whitespace and capitalize each word in a name."""
    return " ".join(name.split()).title()


def calculate_average(numbers: list[float]) -> float:
    """Return the average of the numbers, or raise ValueError if there are none."""
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")
    return sum(numbers) / len(numbers)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/items")
def list_items() -> list[dict[str, int | str]]:
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int) -> dict[str, int | str]:
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
