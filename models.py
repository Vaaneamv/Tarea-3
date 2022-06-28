import email
from unicodedata import doctor
from urllib.parse import DefragResult
from xml.etree.ElementTree import Comment
from app.db import db, BaseModelMixin
class Patient(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    doctor = db.Column(db.String)
    lastname = db.Column(db.String)
    rut = db.Column(db.Integer)
    email = db.Column(db.String)
    birthday = db.Column(db.Integer)
    def __init__(self, doctor, lastname, rut, email, birthday):
        self.doctor = doctor
        self.lastname = lastname
        self.rut = rut
        self.email = email
        self.birthday = birthday
    def __repr__(self):
        return f'Patient({self.doctor})'
    def __str__(self):
        return f'{self.doctor}'
class Prescription(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    id_patient= db.Column(db.Integer, primary_key=True)
    comentario= db.Column(db.String)
    drug= db.Column(db.String)
    doctor = db.Column(db.String)
    Patient_id = db.Column(db.Integer, db.ForeignKey('Patient.id'), nullable=False)
    def __init__(self, doctor):
        self.doctor = doctor
        self.comentario= comentario
        self.drug= drug 
    def __repr__(self):
        return f'Prescription({self.doctor})'
    def __str__(self):
        return f'{self.doctor}'