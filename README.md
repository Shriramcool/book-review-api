# 📚 Book Review API

A FastAPI-powered backend application that allows users to create and manage books and their reviews, with Redis caching and PostgreSQL support.

---

## 🚀 Features

- Add, list books 📖
- Add, list reviews 📝
- Redis caching for performance ⚡
- PostgreSQL database integration 🗄️
- Alembic database migrations
- Automated tests with pytest ✅

---

## 🧰 Tech Stack

- Python 3.12+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Redis
- Alembic
- Pytest

---


## 📁 Project Structure

```plaintext
book-review-api/
├── app/                          # Main application code
│   ├── __init__.py               # Makes 'app' a Python package
│   ├── main.py                   # FastAPI entry point, includes routers, creates DB tables
│   ├── models.py                 # SQLAlchemy models for Book and Review
│   ├── crud.py                   # CRUD logic for books and reviews
│   ├── schemas.py                # Pydantic models for request/response validation
│   ├── database.py               # DB engine setup and session management
│   ├── cache.py                  # Redis cache interaction logic
│   └── routes/                   # Folder for route definitions
│       ├── __init__.py           # Makes 'routes' a Python package
│       └── books.py              # API routes for books and reviews
├── tests/                        # Unit and integration test suite
│   ├── test_books.py             # Tests for book & review APIs
│   └── test_integration_cache.py# Tests to validate Redis caching logic
├── alembic/                      # Alembic migrations folder
│   ├── versions/                 # Auto-generated migration files
│   └── env.py                    # Migration configuration and metadata loading
├── alembic.ini                   # Alembic config file with DB URL and migration settings
├── requirements.txt              # Python dependencies (FastAPI, SQLAlchemy, etc.)
├── pytest.ini                    # Pytest configuration for test discovery and paths
└── README.md                     # Project setup, usage, and API documentation
```


---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Shriramcool/book-review-api
cd book-review-api

2. Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows

3. Install Dependencies

pip install -r requirements.txt

4.Setup .env File

DATABASE_URL=postgresql://user:password@localhost:5432/bookdb
REDIS_URL=redis://localhost:6379

# Replace user, password, bookdb with your actual PostgreSQL credentials.

🗄️ Setup PostgreSQL & Redis
📌 PostgreSQL 

CREATE DATABASE bookdb;

Redis
Install and start Redis server:

redis-server.exe


🔧 Run Database Migrations

# Create initial migration (if not created)
alembic revision --autogenerate -m "Initial migration"

# Apply migrations
alembic upgrade head

🚀 Run the Server

uvicorn app.main:app --reload


🧪 Run Tests
Set PYTHONPATH and run tests:   

set PYTHONPATH=.
pytest


 API Endpoints
Method	Endpoint	Description
GET	/books/	List all books
POST	/books/	Add a new book
GET	/books/{id}/reviews	Get book reviews
POST	/books/{id}/reviews	Add book review



