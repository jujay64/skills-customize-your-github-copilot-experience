# 📘 Assignment: Automated Testing with pytest

## 🎯 Objective

Learn to use pytest to check Python functions and FastAPI endpoints, including expected results, edge cases, and error responses.

## 📦 Setup

Download `starter_code.py` and `requirements.txt` into the same folder. Install the dependencies with `python -m pip install -r requirements.txt`. Create your tests in a file named `test_starter_code.py` and run them with `python -m pytest -v`.

## 📝 Tasks

### 🛠️ Test Individual Functions

#### Description
Write tests for `format_name` and `calculate_average` in the starter code. Check ordinary inputs and the documented behavior for an empty list.

#### Requirements
Completed tests should:

- Import the functions from `starter_code.py`.
- Check that `format_name` trims extra whitespace and capitalizes each word.
- Check that `calculate_average` returns the correct average for multiple numbers.
- Check that `calculate_average` raises `ValueError` for an empty list.

### 🛠️ Cover More Inputs with pytest

#### Description
Use pytest's parameterization to check several inputs for `format_name` and `calculate_average` without duplicating test functions.

#### Requirements
Completed tests should:

- Use `pytest.mark.parametrize` with at least three input-and-expected-result cases.
- Include a single-word name and a name with extra spaces.
- Include average calculations with different list lengths and values.
- Keep each test's expected result clear and specific.

### 🛠️ Test FastAPI Endpoints

#### Description
Use FastAPI's `TestClient` to exercise the API directly, without starting a server. Verify both successful responses and the not-found response.

#### Requirements
Completed tests should:

- Create a `TestClient` for the starter code's `app`.
- Check that `GET /health` returns status code `200` and `{"status": "ok"}`.
- Check that `GET /items` returns the available items.
- Check that `GET /items/1` returns the matching item and `GET /items/999` returns status code `404`.
