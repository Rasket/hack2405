# -*- coding: utf-8 -*-
from app import app, db
from app.models import User
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm, ResponsibilityWaste, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from test1 import test1

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
    company = User.query.filter_by(public=1).all()
    return render_template('explore.html', company = company)
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
        current_user.public = form.public.data     
        if form.image.data:
            current_user.avatar = image_db.data(form.image.data)        
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
        form.public.data = current_user.public
    return render_template('edit.html', title = 'Edit Profile', form = form)    


def parsa(data):
    if data == 'Да, постоянно':
        return 2
    if data == "Иногда":
        return 1
    if data == "Нет":
        return 0
    if data == 'до 50%':
        return 2
    if data == "50%":
        return 1
    if data == "от 50% до 100%":
        return 0


@app.route('/ecoquiz', methods=['GET', 'POST'])
@login_required
def quiz():
    form = ResponsibilityWaste()
    if form.validate_on_submit():
        form.first.data 
        current_user.answers_work =            
        return redirect(url_for('quiz'))
    return render_template('quiz.html', form = form, text='test', title = 'Ecoquiz')


@app.route('/ecoquizalt', methods=['GET', 'POST'])
@login_required
def quiz_alt():
    userTest = test1()
    userLog = current_user.answers
    userTest.start()
    forForm = "Данные передаваемые в форму"
    if userLog == None:
        pass
    else:
        for ans in userLog:
            forForm = userTest.next(ans) 
    if 0:
        "Переход на страницу с результатом"
    else: #подать в формму нужный вопрос
        form = ResponsibilityWaste_alt(forForm)
        if form.validate_on_submit():
            #сохранить ответ пользователя 
            flash(form.first.data)     
            return redirect(url_for('quiz'))
        return render_template('quiz.html', form = form, text='test', title = 'Ecoquiz')
# возможность узнать свою экооценку


userTest = test1()
userLog = None
forForm = userTest.start()
if userLog == None:
    pass
else:
    for ans in userLog:
        forForm = userTest.next(ans)