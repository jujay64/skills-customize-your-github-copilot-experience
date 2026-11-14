# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a small REST API with FastAPI by creating routes, handling JSON data, and validating requests with Pydantic models.

## 📝 Tasks

### 🛠️ Create the API App

#### Description
Set up a minimal FastAPI application and define a simple route that returns JSON data.

#### Requirements
Completed program should:

- Create a FastAPI app instance.
- Define at least one `GET` route.
- Return a JSON response such as a welcome message or status object.
- Run the app locally with Uvicorn for testing.

### 🛠️ Build a Resource Endpoint

#### Description
Create an in-memory list of items and expose endpoints to view and add them.

#### Requirements
Completed program should:

- Define an item structure with fields such as `id` and `name`.
- Add a `GET /items` route that returns all items.
- Add a `POST /items` route that accepts a new item and returns the created object.
- Store data in memory while the server is running.

### 🛠️ Validate Inputs and Retrieve by ID

#### Description
Add input validation and a detail endpoint for a specific item.

#### Requirements
Completed program should:

- Use a Pydantic model to validate incoming item data.
- Add a `GET /items/{item_id}` route that returns one item.
- Return an appropriate error response if the item does not exist.
- Demonstrate how FastAPI automatically handles request validation.
