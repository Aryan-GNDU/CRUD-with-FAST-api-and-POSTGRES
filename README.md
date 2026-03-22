# 📚 FastAPI Bookstore CRUD API

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-CRUD%20API-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/Pydantic-Validation-E92063?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic">
</p>

<p align="center">
  A clean and simple <b>Book Management REST API</b> built with <b>FastAPI</b>, <b>PostgreSQL</b>, and <b>SQLAlchemy</b>.
</p>

## ✨ Overview

This project is a beginner-friendly CRUD API for managing books. It lets you:

- ➕ Create a new book
- 📖 View all books
- 🔎 Fetch a book by ID
- ✏️ Update book details
- ❌ Delete a book

The API uses:

- `FastAPI` for building the REST endpoints
- `PostgreSQL` as the database
- `SQLAlchemy` for ORM/database operations
- `Pydantic` for request and response validation

## 🧰 Tech Stack

- `Python`
- `FastAPI`
- `Uvicorn`
- `SQLAlchemy`
- `PostgreSQL`
- `psycopg2-binary`
- `Pydantic`
- `python-dotenv`

## 📁 Project Structure

```text
CRUD  with Fast API and PostGres/
├── main.py
├── config.py
├── db.py
├── models.py
├── schemas.py
├── requirements.txt
├── .env
└── Services/
    └── services.py
```

## ⚙️ Features

- RESTful book CRUD endpoints
- PostgreSQL database integration
- SQLAlchemy model-based data handling
- Pydantic schema validation
- Dependency-based database session management
- Auto-generated API docs with Swagger UI

## 🗃️ Database Model

The project currently stores books with these fields:

| Field | Type |
|------|------|
| `id` | Integer |
| `title` | String |
| `author` | String |
| `description` | String |
| `year` | Integer |

## 🚀 API Endpoints

| Method | Endpoint | Description |
|------|------|------|
| `GET` | `/books/` | Get all books |
| `POST` | `/books/` | Create a new book |
| `GET` | `/books/{id}` | Get a book by ID |
| `PUT` | `/books/{id}` | Update a book by ID |
| `DELETE` | `/books/{id}` | Delete a book by ID |

## 🧪 Example Request Body

Use this JSON for `POST /books/` and `PUT /books/{id}`:

```json
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "description": "A practical book on building good habits and breaking bad ones.",
  "year": 2018
}
```

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd "CRUD  with Fast API and PostGres"
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the root directory:

```env
URI=postgresql+psycopg2://YOUR_USERNAME:YOUR_PASSWORD@localhost:5432/YOUR_DATABASE
```

Important:

- Do not commit real database credentials to GitHub
- If your current `.env` contains real credentials, rotate them before publishing the repository

### 6. Create database tables

Before running the API, make sure the `books` table exists.

You can create it from Python:

```python
from db import create_table
create_table()
```

### 7. Run the FastAPI server

```bash
uvicorn main:app --reload
```

The API will be available at:

- `http://127.0.0.1:8000`

## 📘 Interactive API Docs

FastAPI provides built-in documentation:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## 🔄 How It Works

- `main.py` defines the API routes
- `schemas.py` contains Pydantic schemas for validation
- `models.py` defines the SQLAlchemy `Book` model
- `db.py` manages database connection and sessions
- `config.py` loads the database URL from `.env`
- `Services/services.py` contains CRUD database logic

## 🌟 Future Improvements

- Add input validation for book fields
- Add pagination and search
- Add authentication and authorization
- Add Docker support
- Add automated tests with `pytest`
- Add Alembic for database migrations

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a pull request

