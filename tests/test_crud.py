import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import models, crud, schemas
from app.database import Base

# Use in-memory SQLite for isolated tests
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

def test_create_book_and_get_books(db):
    book_data = schemas.BookCreate(title="Unit Test Book", author="Unit Tester")
    book = crud.create_book(db, book_data)
    assert book.title == "Unit Test Book"

    books = crud.get_books(db)
    assert len(books) == 1
    assert books[0].author == "Unit Tester"

def test_create_and_get_reviews(db):
    book_data = schemas.BookCreate(title="Review Book", author="Reviewer")
    book = crud.create_book(db, book_data)

    review_data = schemas.ReviewCreate(rating=4, comment="Great!", reviewer="Alice")
    review = crud.create_review(db, book.id, review_data)
    assert review.comment == "Great!"

    reviews = crud.get_reviews_for_book(db, book.id)
    assert len(reviews) == 1
    assert reviews[0].rating == 4
