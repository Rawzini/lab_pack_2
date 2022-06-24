from flask import render_template, request, flash, redirect, url_for
from models.user import get_user_by_email, get_user_by_username, create_new_user
from flask_login import logout_user, current_user, login_user, login_required

def get_login_form():
    return render_template('login.html')

def login():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = get_user_by_email(email)

    if not user or not user.check_password(password):
        flash('Неверное имя пользователя, либо пароль')
        return redirect(url_for('routes.login'))

    login_user(user, remember=remember)
    return redirect(url_for('routes.get_profile_page'))

def get_signup_form():
    return render_template('signup.html')

def signup():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    user = get_user_by_email(email)
    if user:  # если пользователь есть, то отправим заново на форму регистрации
        flash('Пользователь с данным email уже существует')
        return redirect(url_for('routes.signup'))

    user = get_user_by_username(username)
    if user:  # если пользователь есть, то отправим заново на форму регистрации
        flash('Пользователь с данным юзернеймом уже существует')
        return redirect(url_for('routes.signup'))

    create_new_user(username, password, email)

    return redirect(url_for('routes.login'))

@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.index'))

@login_required
def get_profile_page():
    name = current_user.name
    return render_template('profile.html', name=name)
