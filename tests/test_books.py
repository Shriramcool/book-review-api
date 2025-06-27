import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal

# Setup test client
client = TestClient(app)

# Create all tables before running tests
Base.metadata.create_all(bind=engine)

# Helper to get a clean DB session for each test
def override_get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# Test: Create a new book
def test_create_book():
    response = client.post("/books/", json={"title": "Test Book", "author": "Author X"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Book"
    assert data["author"] == "Author X"
    assert "id" in data

# Test: Get all books (includes cached version if present)
def test_get_books():
    response = client.get("/books/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert "title" in data[0]
    assert "author" in data[0]

# Test: Add review to a book
def test_add_review():
    # First, create a book to add review to
    book_resp = client.post("/books/", json={"title": "Review Book", "author": "Review Author"})
    book_id = book_resp.json()["id"]

    review_payload = {
        "reviewer": "John",
        "text": "Excellent book!",
        "rating": 5
    }

    response = client.post(f"/books/{book_id}/reviews", json=review_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["reviewer"] == "John"
    assert data["text"] == "Excellent book!"
    assert data["rating"] == 5

# Test: Get reviews for a book
def test_get_reviews():
    # Create a book
    book_resp = client.post("/books/", json={"title": "Review Get Book", "author": "Author Y"})
    book_id = book_resp.json()["id"]

    # Add a review
    client.post(f"/books/{book_id}/reviews", json={
        "reviewer": "Alice",
        "text": "Not bad",
        "rating": 3
    })

    # Now test the GET reviews endpoint
    response = client.get(f"/books/{book_id}/reviews")
    assert response.status_code == 200
    reviews = response.json()
    assert isinstance(reviews, list)
    assert any(r["reviewer"] == "Alice" for r in reviews)
