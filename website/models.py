from . import db
from flask_login import UserMixin

class Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    imagem = db.Column(db.String(100))
    temporada_id = db.Column(db.Integer)
    jogador_id_1 = db.Column(db.Integer, db.ForeignKey('jogador.id'))
    jogador_id_2 = db.Column(db.Integer, db.ForeignKey('jogador.id'))
    jogador_id_3 = db.Column(db.Integer, db.ForeignKey('jogador.id'))
    jogador_id_4 = db.Column(db.Integer, db.ForeignKey('jogador.id'))
    jogador_id_5 = db.Column(db.Integer, db.ForeignKey('jogador.id'))

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40))
    vulgo = db.Column(db.String(20), unique=True)
    numero = db.Column(db.Integer)
    insta = db.Column(db.String(30))
    imagem = db.Column(db.String(100))

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True)
    senha = db.Column(db.Integer)
    jogador_id = db.Column(db.String(20))
