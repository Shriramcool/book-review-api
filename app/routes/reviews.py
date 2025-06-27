from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud, deps

router = APIRouter()

@router.get("/books/{book_id}/reviews", response_model=list[schemas.Review])
def get_reviews(book_id: int, db: Session = Depends(deps.get_db)):
    return crud.get_reviews_by_book(db, book_id)

@router.post("/books/{book_id}/reviews", response_model=schemas.Review)
def add_review(book_id: int, review: schemas.ReviewCreate, db: Session = Depends(deps.get_db)):
    return crud.create_review(db, review, book_id)
