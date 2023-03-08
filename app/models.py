from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app import db


# Criando a modelo no banco de dados. 
class User(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(64), index=True, unique=True)
    address = db.Column(db.String(125), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password) #Cria o hash de senha

    def check_password(self, password):
        return check_password_hash(self.password_hash, password) #verifica se o hash está igual o da senha

    def __repr__(self): 
        return f'<User {self.username}>' 

# Criando o modelo de tabela dos livros
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(54), index=True, unique=True)
    description = db.Column(db.String(140))

    def __repr__(self): 
        return f'<Book {self.name}>'