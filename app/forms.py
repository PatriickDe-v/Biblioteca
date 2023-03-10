from flask_wtf import FlaskForm
from wtforms import (BooleanField, PasswordField, RadioField, StringField,
                     SubmitField)
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app.models import User


#Formulário de login 
class LoginForm(FlaskForm): 
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar de mim')
    submit = SubmitField('Entrar')
    admin_or_not = BooleanField('Adminstrador')

#Formulário de registro.
class RegistrationForm(FlaskForm): 
    username = StringField('Usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    password2 = PasswordField('Digite novamente sua senha', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Enviar')

    def validate_username(self, username): 
        user = User.query.filter_by(username=username.data).first()
        if user is not None: 
            raise ValidationError('Por favor, use um nome de usuário diferente.')    
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None: 
            raise ValidationError('Por favor, use um enedereço de e-mail diferente.')
