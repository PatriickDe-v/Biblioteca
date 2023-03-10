from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.urls import url_parse

from app import app, db, login
from app.forms import LoginForm, RegistrationForm
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Patrick'}
    books = [{
        'author': {'name': 'Amor de Redenção'},
        'description': 'Califórnia, 1850. Uma época em que os homens vendiam a própria alma \
             por um punhado de ouro e as mulheres vendiam o próprio corpo por um lugar para dormir.'
    }]
    return render_template("index.html", title='Home', books=books)

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
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Entrar', form=form)

#deslogando 
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/cadastro', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit(): 
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Cadastro efetuado com sucesso!')
        return redirect(url_for('login'))
    return render_template('register.html', title='cadastro', form=form)





