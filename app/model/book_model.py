from app import db


# Book:
# id: int
# name: str
# author: str

class Book(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))
    author = db.Column(db.String(100))

    def __init__(self, name, author):
        self.name = name
        self.author = author

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author
        }
