import json
from fastapi.testclient import TestClient
from app.main import app
from app.cache import r

client = TestClient(app)

def test_cache_hit(monkeypatch):
    # Arrange: Fake cached response data
    fake_books = [
        {"id": 1, "title": "Cached Book 1", "author": "Author A"},
        {"id": 2, "title": "Cached Book 2", "author": "Author B"},
    ]

    # Store JSON version of that in Redis
    r.set("books", json.dumps(fake_books))

    # Act: call GET /books
    response = client.get("/books/")

    # Assert
    assert response.status_code == 200
    assert response.json() == fake_books
