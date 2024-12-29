# Flask Library Management (CRUD Application)

## Overview
This project demonstrates a CRUD (Create, Read, Update, Delete) application using Flask and SQLAlchemy. It implements a simple library management system with `Book` and `Member` entities, backed by a SQLite database. The application provides RESTful APIs for managing books and members, as well as searching for books by title or author.

---

## Features
- **Database Integration**: Uses SQLite as the database backend with SQLAlchemy for ORM (Object-Relational Mapping).
- **CRUD Operations**:
  - Add, retrieve, update, and delete books.
  - Add, retrieve, update, and delete members.
- **Search Functionality**:
  - Search for books by title or author.
- **RESTful API Endpoints**: Provides a clean API interface for interaction.

---

## Technologies Used
- **Python**
- **Flask**: A lightweight web framework for Python.
- **Flask-SQLAlchemy**: Extension for SQLAlchemy integration with Flask.
- **SQLite**: Relational database for data persistence.

---

## Setup and Installation

### Prerequisites
- Python (3.8 or later recommended)
- pip (Python package manager)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install dependencies:
   ```bash
   pip install flask flask-sqlalchemy
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Access the application in your browser or API client:
   - URL: `http://127.0.0.1:5000`

---

## API Endpoints

### Books

#### Add a Book
- **Endpoint**: `POST /books`
- **Request Body**:
  ```json
  {
    "title": "Book Title",
    "author": "Author Name"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Book added successfully!",
    "book": { "title": "Book Title", "author": "Author Name" }
  }
  ```

#### Get All Books
- **Endpoint**: `GET /books`
- **Response**:
  ```json
  [
    { "id": 1, "title": "Book Title", "author": "Author Name" }
  ]
  ```

#### Get, Update, or Delete a Book
- **Endpoint**: `GET /books/<book_id>`
- **Endpoint**: `PUT /books/<book_id>`
- **Endpoint**: `DELETE /books/<book_id>`

### Members

#### Add a Member
- **Endpoint**: `POST /members`
- **Request Body**:
  ```json
  {
    "name": "Member Name",
    "email": "member@example.com",
    "phone": "1234567890"
  }
  ```

#### Get All Members
- **Endpoint**: `GET /members`

#### Get, Update, or Delete a Member
- **Endpoint**: `GET /members/<member_id>`
- **Endpoint**: `PUT /members/<member_id>`
- **Endpoint**: `DELETE /members/<member_id>`

### Search Books

#### Search for Books by Title or Author
- **Endpoint**: `GET /books/search`
- **Query Parameters**:
  - `q`: The search term (e.g., `?q=title`)
- **Response**:
  ```json
  [
    { "id": 1, "title": "Book Title", "author": "Author Name" }
  ]
  ```

---

## Code Structure

### Models
- **Book**: Represents a book entity with fields `id`, `title`, and `author`.
- **Member**: Represents a member entity with fields `id`, `name`, `email`, and `phone`.

### Routes
- **`/books`**: CRUD operations for books.
- **`/members`**: CRUD operations for members.
- **`/books/search`**: Search for books by title or author.

---

## Example Usage
### Adding a Book
```bash
curl -X POST http://127.0.0.1:5000/books -H "Content-Type: application/json" -d '{"title": "Example Book", "author": "John Doe"}'
```

### Searching for a Book
```bash
curl -X GET "http://127.0.0.1:5000/books/search?q=example"
```

---

## Notes
- **Database Configuration**: The default database is SQLite, but it can be replaced with any supported database like PostgreSQL or MySQL by updating the `SQLALCHEMY_DATABASE_URI` configuration.
- **Error Handling**: Proper error handling is implemented for invalid operations, such as accessing a non-existent book or member.


