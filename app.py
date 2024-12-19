from flask import Flask, request, jsonify
from models import books_db, Book  # Import models and database

app = Flask(__name__)

# Define the root endpoint or a simple test route (optional)
@app.route('/')
def home():
    return "Welcome to the Library Management System!"

# POST endpoint to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()  # Get data from the request
    new_id = len(books_db) + 1  # Simple ID generation
    book = Book(new_id, data['title'], data['author'], data['year'])  # Create a new Book object
    books_db[new_id] = book  # Add the new book to the "database"
    return jsonify({'message': 'Book Added Successfully'}), 201  # Return a success message

# GET endpoint to retrieve all books
@app.route('/books', methods=['GET'])
def get_books():
    books = []  # Initialize a list to store books
    for book in books_db.values():
        books.append({
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'year': book.year
        })  # Append book data to the list
    return jsonify(books)  # Return the list of books as a JSON response

if __name__ == '__main__':
    app.run(debug=True)
