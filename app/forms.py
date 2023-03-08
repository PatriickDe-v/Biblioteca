from flask_wtf import FlaskForm
from wtforms import (BooleanField, PasswordField, RadioField, StringField,
                     SubmitField)
from wtforms.validators import DataRequired


#Formulário de login 
class LoginForm(FlaskForm): 
    username = StringField('Nome', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar de mim')
    submit = SubmitField('Entrar')
    admin_or_not = BooleanField('Adminstrador')