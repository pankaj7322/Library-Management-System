# Library Management System API

## Description
This is a simple REST API built using Flask for a Library Management System. The API allows managing books and members with CRUD operations. Additionally, it provides search functionality, pagination, and basic token-based authentication.

## How to Run
1. Clone this repository.
2. Install the required dependencies: `pip install flask`.
3. Run the application: `python app.py`.
4. Access the API at `http://127.0.0.1:5000`.

## Endpoints

- **Books**:
  - `POST /books`: Add a new book.
  - `GET /books`: Get all books (supports pagination with `page` and `per_page`).
  - `GET /books/search`: Search books by title or author.
  - `PUT /books/<id>`: Update book details.
  - `DELETE /books/<id>`: Delete a book by ID.

- **Members**:
  - `POST /members`: Add a new member.
  - `GET /members`: Get all members.


## Design Choices
- **In-memory storage**: The data is stored in memory (`books_db` and `members_db`) for simplicity. In a production system, a database like SQLite or PostgreSQL would be used.
- **Token Authentication**: A simple hardcoded token is used to authenticate API requests.

## Assumptions & Limitations
- No third-party libraries are used (e.g., JWT).
- Data is not persistent and will be lost when the app is restarted.
