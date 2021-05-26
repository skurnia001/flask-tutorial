from flask import Blueprint, jsonify, request

from app.manager import book_manager

book_blueprint = Blueprint('book', __name__)


# GET /api/book
@book_blueprint.route('/api/book', methods=['GET'])
def api_get_book():
    # Get parameters/payload
    query = dict(request.args)

    # Call manager to process data
    books = book_manager.get_books()

    # Return result to client
    return jsonify({
        "books": books
    })


# GET /api/book
@book_blueprint.route('/api/book/even', methods=['GET'])
def api_get_book_even():
    # Get parameters/payload
    query = dict(request.args)

    # Call manager to process data
    books = book_manager.get_books_even()

    # Return result to client
    return jsonify({
        "books": books
    })


# POST /api/book
@book_blueprint.route('/api/book', methods=['POST'])
def api_post_book():
    # Get parameters/payload
    payload = dict(request.json)

    # Call manager to process data
    books = book_manager.create_book(
        payload['name'],
        payload['author']
    )

    # Return result to client
    return jsonify({
        "books": books
    })
