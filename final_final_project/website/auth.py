from flask import Blueprint, render_template, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from __main__ import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if db.read_login(email) != -1:
            if check_password_hash(db.read_login(email), password):
                flash('Logged in successfully!', category = 'success')
                # return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user = current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    # return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('first_name')
        surname = request.form.get('surname')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('First Name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        elif db.insert_user(name, surname, username, email, password=generate_password_hash(password1, method='sha256')) == False:
            flash('This user already exists!', category='error')
        else:
            db.insert_user(name, surname, username, email, password=generate_password_hash(password1, method='sha256'))
            flash('Account created!', category='success')

            # login_user(new_user, remember = True)
            # return redirect(url_for('views.home'))

    return render_template("sign_up.html")
