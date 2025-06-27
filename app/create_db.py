from .database import Base, engine
from .models import Book, Review

print("Creating database...")
Base.metadata.create_all(bind=engine)
print("Done.")
