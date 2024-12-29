from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database URI (SQLite example)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'  # You can use any other database like PostgreSQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable unnecessary tracking of object changes

# Initialize the database
db = SQLAlchemy(app)

# Define Book and Member models
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<Book {self.title}>'

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=True)
    
    def __repr__(self):
        return f'<Member {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# CRUD for Books
@app.route('/books', methods=['GET', 'POST'])
def manage_books():
    if request.method == 'POST':
        book_data = request.json
        new_book = Book(title=book_data['title'], author=book_data['author'])
        db.session.add(new_book)
        db.session.commit()
        return jsonify({'message': 'Book added successfully!', 'book': book_data}), 201
    
    books = Book.query.all()
    return jsonify([{'id': book.id, 'title': book.title, 'author': book.author} for book in books])

@app.route('/books/<int:book_id>', methods=['GET', 'PUT', 'DELETE'])
def book_details(book_id):
    book = Book.query.get(book_id)
    
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    
    if request.method == 'GET':
        return jsonify({'id': book.id, 'title': book.title, 'author': book.author})
    
    if request.method == 'PUT':
        book_data = request.json
        book.title = book_data['title']
        book.author = book_data['author']
        db.session.commit()
        return jsonify({'message': 'Book updated successfully!', 'book': {'id': book.id, 'title': book.title, 'author': book.author}})
    
    if request.method == 'DELETE':
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted successfully!'})

# CRUD for Members
@app.route('/members', methods=['GET', 'POST'])
def manage_members():
    if request.method == 'POST':
        member_data = request.json
        new_member = Member(name=member_data['name'], email=member_data['email'], phone=member_data.get('phone'))
        db.session.add(new_member)
        db.session.commit()
        return jsonify({'message': 'Member added successfully!', 'member': member_data}), 201
    
    members = Member.query.all()
    return jsonify([{'id': member.id, 'name': member.name, 'email': member.email, 'phone': member.phone} for member in members])

@app.route('/members/<int:member_id>', methods=['GET', 'PUT', 'DELETE'])
def member_details(member_id):
    member = Member.query.get(member_id)
    
    if not member:
        return jsonify({'error': 'Member not found'}), 404
    
    if request.method == 'GET':
        return jsonify({'id': member.id, 'name': member.name, 'email': member.email, 'phone': member.phone})
    
    if request.method == 'PUT':
        member_data = request.json
        member.name = member_data['name']
        member.email = member_data['email']
        member.phone = member_data.get('phone')
        db.session.commit()
        return jsonify({'message': 'Member updated successfully!', 'member': {'id': member.id, 'name': member.name, 'email': member.email, 'phone': member.phone}})
    
    if request.method == 'DELETE':
        db.session.delete(member)
        db.session.commit()
        return jsonify({'message': 'Member deleted successfully!'})

# Search Books by Title or Author
@app.route('/books/search', methods=['GET'])
def search_books():
    query = request.args.get('q', '').lower()
    books = Book.query.filter((Book.title.ilike(f'%{query}%')) | (Book.author.ilike(f'%{query}%'))).all()
    return jsonify([{'id': book.id, 'title': book.title, 'author': book.author} for book in books])

if __name__ == '__main__':
    app.run(debug=True)

