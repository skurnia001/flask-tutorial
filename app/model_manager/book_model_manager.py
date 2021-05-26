from app import db
from app.model.book_model import Book


def get_all_books():
    return [book.to_dict() for book in Book.query.all()]


def create_book(name, author):
    book = Book(name, author)
    db.session.add(book)
    db.session.commit()
    return book.to_dict()
