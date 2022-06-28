from ast import dump
from marshmallow import fields
from app.ext import ma
class PatientOn(ma.Schema):
    id = fields.Integer(dump_only=True)
    doctor = fields.String()
    lastname = fields.String()
    rut = fields.Integer()
    email = fields.String()
    birthday = fields.String
class PrescriptionOn(ma.Schema):
    id = fields.Integer(dump_only=True)
    id_patient= fields.Integer(dump_only=True)
    comentario= fields.String()
    drug = fields.String()
    doctor= fields.String()