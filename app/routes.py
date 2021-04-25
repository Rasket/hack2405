# -*- coding: utf-8 -*-
from app import app, db
from app.models import User
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm, ResponsibilityWaste, EditProfileForm
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
	return render_template('indeax.html', title='Index')
# главная страница, скорее всего удалится в будущем


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
# разлогиниться

@app.route('/company/<companyname>/', methods=['GET', 'POST'])
@login_required
def company(companyname):
    user = User.query.filter_by(username=companyname).first_or_404()
    return render_template('user.html', user=user)
# страница компании отедльной


@app.route('/explore', methods=['GET', 'POST'])
def explore():
    return render_template('placeholder.html')
    '''
    form = ResponsibilityWaste()
    if form.validate_on_submit():
        print(form.example.data)
    return render_template('ecotestone.html', form = form)
    '''
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
        flash('Congratulations, you are now part of a ECO-profile!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
# секретная регистрация для компании


@app.route('/edit_profile', methods = ['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data      
        if form.image.data:
            current_user.avatar = image_db.data(form.image.data)        
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit.html', title = 'Edit Profile', form = form)    


@app.route('/ecoquiz', methods=['GET', 'POST'])
def quiz():
    form = ResponsibilityWaste()
    if form.validate_on_submit():
        flash(form.first.data)     
        return redirect(url_for('quiz'))
    return render_template('quiz.html', form = form, text='test')
# возможность узнать свою экооценку