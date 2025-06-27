from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database, models
from ..cache import get_cached_books, set_cached_books

router = APIRouter(prefix="/books", tags=["Books"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Book])
def list_books(db: Session = Depends(get_db)):
    cached_books = get_cached_books()
    if cached_books:
        return cached_books

    books = crud.get_books(db)
    books_data = [schemas.Book.model_validate(book).model_dump() for book in books]
    set_cached_books(books_data)
    return books_data

@router.post("/", response_model=schemas.Book)
def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@router.get("/{book_id}/reviews", response_model=list[schemas.Review])
def get_reviews(book_id: int, db: Session = Depends(get_db)):
    return crud.get_reviews_for_book(db, book_id)

@router.post("/{book_id}/reviews", response_model=schemas.Review)
def add_review(book_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.create_review(db, book_id, review)
