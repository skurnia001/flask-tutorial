from app.model_manager import book_model_manager


def get_books():
    books = book_model_manager.get_all_books()
    return books


def create_book(name, author):
    if author == 'Ico':
        return None
    book = book_model_manager.create_book(name, author)
    return book


def get_books_even():
    books = book_model_manager.get_all_books()
    filtered_books = []
    for book in books:
        if book['id'] % 2 == 0:
            filtered_books.append(book)
    return filtered_books
