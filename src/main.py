from fastapi import FastAPI, HTTPException
from src.models import Expense
from src.storage import load_expenses, save_expenses

app = FastAPI(
    title="Smart Expense Tracker API",
    description="API to manage personal expenses",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Expense Tracker API Running"}

@app.post("/expenses")
def add_expense(expense: Expense):

    expenses = load_expenses()

    for e in expenses:
        if e["id"] == expense.id:
            raise HTTPException(
                status_code=400,
                detail="Expense ID already exists"
            )

    expenses.append(
        expense.model_dump(mode="json")
    )

    save_expenses(expenses)

    return {
        "message": "Expense added successfully",
        "expense": expense
    }

@app.get("/expenses")
def get_all_expenses():
    return load_expenses()

@app.get("/expenses/category/{category}")
def get_expenses_by_category(category: str):

    expenses = load_expenses()

    filtered_expenses = [
        expense
        for expense in expenses
        if expense["category"].lower() == category.lower()
    ]

    return filtered_expenses

@app.get("/expenses/total")
def get_total_expenses():

    expenses = load_expenses()

    total = sum(
        expense["amount"]
        for expense in expenses
    )

    return {
        "total_expenses": total
    }

@app.get("/expenses/total/{category}")
def get_total_by_category(category: str):

    expenses = load_expenses()

    total = sum(
        expense["amount"]
        for expense in expenses
        if expense["category"].lower() == category.lower()
    )

    return {
        "category": category,
        "total": total
    }

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):

    expenses = load_expenses()

    updated_expenses = [
        expense
        for expense in expenses
        if expense["id"] != expense_id
    ]

    if len(updated_expenses) == len(expenses):
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    save_expenses(updated_expenses)

    return {
        "message": f"Expense {expense_id} deleted successfully"
    }