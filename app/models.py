from sqlalchemy import Column, Integer, String, ForeignKey, Index
from sqlalchemy.orm import relationship
from .database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)

    reviews = relationship("Review", back_populates="book", cascade="all, delete")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    reviewer = Column(String, nullable=False)  
    comment = Column(String, nullable=False)   
    rating = Column(Integer, nullable=False)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"), index=True)

    book = relationship("Book", back_populates="reviews")

# Add an index on book_id (optimization)
Index("idx_reviews_book_id", Review.book_id)
