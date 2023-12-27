from fastapi.testclient import TestClient
from main import app
from config import settings

def test_answer():
    client = TestClient(app)
    response = client.get(settings.MAIN_URL)
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"} 
