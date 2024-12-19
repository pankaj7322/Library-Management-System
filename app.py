# app.py
from flask import Flask, request, jsonify
from models import books_db, members_db, Book, Member
from config import API_TOKEN

app = Flask(__name__)

# Simple function to verify API token
def verify_token(token):
    return token == API_TOKEN

# Root endpoint
@app.route('/')
def home():
    return "Welcome to the Library Management System!"

# --- Books Routes ---
# POST: Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_id = len(books_db) + 1
    book = Book(new_id, data['title'], data['author'], data['year'])
    books_db[new_id] = book
    return jsonify({'message': 'Book Added Successfully'}), 201

# GET: Get all books with pagination
@app.route('/books', methods=['GET'])
def get_books():
    page = int(request.args.get('page', 1))  # Get page number from query params
    per_page = int(request.args.get('per_page', 5))  # Books per page (default 5)
    start = (page - 1) * per_page
    end = start + per_page
    books = list(books_db.values())[start:end]

    result = [{'id': book.id, 'title': book.title, 'author': book.author, 'year': book.year} for book in books]
    return jsonify(result)

# GET: Search books by title or author
@app.route('/books/search', methods=['GET'])
def search_books():
    query = request.args.get('query', '').lower()
    result = []
    for book in books_db.values():
        if query in book.title.lower() or query in book.author.lower():
            result.append({'id': book.id, 'title': book.title, 'author': book.author, 'year': book.year})
    return jsonify(result)

# PUT: Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    if book_id not in books_db:
        return jsonify({'message': 'Book not found'}), 404
    data = request.get_json()
    book = books_db[book_id]
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.year = data.get('year', book.year)
    return jsonify({'message': 'Book updated successfully'})

# DELETE: Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if book_id not in books_db:
        return jsonify({'message': 'Book not found'}), 404
    del books_db[book_id]
    return jsonify({'message': 'Book deleted successfully'})

# --- Members Routes ---
# POST: Add a new member
@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    new_id = len(members_db) + 1
    member = Member(new_id, data['name'], data['email'])
    members_db[new_id] = member
    return jsonify({'message': 'Member added successfully'}), 201

# GET: Get all members
@app.route('/members', methods=['GET'])
def get_members():
    members = [{'id': member.id, 'name': member.name, 'email': member.email} for member in members_db.values()]
    return jsonify(members)

# --- Authentication ---
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    token = data.get('token')
    if verify_token(token):
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid token'}), 401

if __name__ == '__main__':
    app.run(debug=True)
