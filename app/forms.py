from flask_wtf import FlaskForm
from wtforms import (BooleanField, PasswordField, RadioField, StringField,
                     SubmitField, TextAreaField)
from wtforms.validators import (DataRequired, Email, EqualTo, Length,
                                ValidationError)

from app.models import User


# Formulário de login
class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar de mim')
    submit = SubmitField('Entrar')

# Formulário de registro.
class RegistrationForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    password2 = PasswordField('Digite novamente sua senha', validators=[DataRequired(), EqualTo('password')])
    admin_or_not = BooleanField('Adminstrador')
    submit = SubmitField('Enviar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Por favor, use um nome de usuário diferente.')
                
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Por favor, use um enedereço de e-mail diferente.')


class RegistrationBookForm(FlaskForm):
    name = StringField('Nome do livro', validators=[DataRequired()])
    author = StringField('Autor', validators=[DataRequired()])
    category = StringField('Categoria', validators=[DataRequired()])
    pages = StringField('Número de páginas', validators=[DataRequired()])
    description = TextAreaField('Descrição', validators=[Length(min=0, max=140)])
    publishCompany = StringField('Editora', validators=[DataRequired()])
    submit = SubmitField('Registrar')