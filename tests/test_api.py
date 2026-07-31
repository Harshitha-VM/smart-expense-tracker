import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_get_expenses():
    response = client.get("/expenses")
    assert response.status_code == 200

def test_total_expenses():
    response = client.get("/expenses/total")
    assert response.status_code == 200

def test_food_category():
    response = client.get("/expenses/category/Food")
    assert response.status_code == 200

def test_total_food():
    response = client.get("/expenses/total/Food")
    assert response.status_code == 200