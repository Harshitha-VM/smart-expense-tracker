# Smart Expense Tracker API

## Features

* Add an expense
* View all expenses
* Filter expenses by category
* Calculate total expenses
* Calculate total expenses by category
* Delete an expense
* Interactive Swagger/OpenAPI documentation

## Installation

```bash
pip install -r requirements.txt
```

## Run the Server

```bash
uvicorn src.main:app --reload
```

Server URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

## Run Tests

```bash
pytest -v
```

## Project Structure

```text
smart-expense-tracker/
│
├── README.md
├── AI_NOTES.md
├── requirements.txt
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── storage.py
│   └── expenses.json
│
└── tests/
    ├── __init__.py
    └── test_api.py
```
