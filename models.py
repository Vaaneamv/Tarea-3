import email
from unicodedata import name
from app.db import db, BaseModelMixin
class Film(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    lastname = db.Column(db.Integer)
    rut = db.Column(db.Integer)
    email = db.Column(db.String)
    birthday = db.Column(db.Integer)
    def __init__(self, name, lastname, rut, email, birthday=[]):
        self.name = name
        self.lastname = lastname
        self.rut = rut
        self.email = email
        self.birthday = birthday
    def __repr__(self):
        return f'Film({self.name})'
    def __str__(self):
        return f'{self.name}'
class Actor(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'), nullable=False)
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'Actor({self.name})'
    def __str__(self):
        return f'{self.name}'