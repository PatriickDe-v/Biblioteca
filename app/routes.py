from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user

from app import app, login
from app.forms import LoginForm
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Patrick'}
    books = [{
        'author': {'name': 'Amor de Redenção'},
        'description': 'Califórnia, 1850. Uma época em que os homens vendiam a própria alma \
             por um punhado de ouro e as mulheres vendiam o próprio corpo por um lugar para dormir.'
    }]
    return render_template('index.html', title='Home', user=user, books=books)

#Carregador de usuário
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#Recebendo credenciais de login. 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Nome de usuário ou senha inválidos.')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Entrar', form=form)
#deslogando 
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))