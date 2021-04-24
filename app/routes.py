# -*- coding: utf-8 -*-
from app import app, db
from app.models import User
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from app.forms import RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required

'''
Функция логина
'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:# проверяет авторизован ли текущий юзер если да то выкидывает его в индекс
        return redirect(url_for('index'))
    form = LoginForm()# форма на логин
    if form.validate_on_submit():# если форма заполнена
        user = User.query.filter_by(username=form.username.data).first()# находим юзера и пароль
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')# проверяем пароль возвращаем в логин
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)# входим с проверкой галки на запомнить меня
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)# сам логин с формой


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	return render_template('index.html', title='Index')
# главная страница, скорее всего удалится в будущем


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
# разлогиниться

@app.route('/company/<companyname>/', methods=['GET', 'POST'])
@login_required
def company(companyname):
	return companyname
# страница компании отедльной


@app.route('/explore')
def explore():
	return 'hello'
# здесь планируется размещать информацию о всех компаниях которые хотят рассказать о своей эко оценке + поиск по компаниям

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
# секретная регистрация для компании


@app.route('/ecoquiz', methods=['GET', 'POST'])
def quiz():
	return redirect(url_for('index'))
# возможность узнать свою экооценку