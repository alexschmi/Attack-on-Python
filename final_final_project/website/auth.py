from flask import Blueprint, render_template, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from . import db

auth = Blueprint('auth', __name__)

class User:
    def __init__(self, firstName, surName, email, password):
        self.name = firstName
        self.surname = surName
        self.email = email
        db.insert_user(name=firstName, surname=surName, username=email[0:-4], email=email,
                       password=generate_password_hash(password, method='sha256'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # TO DO: check whether email exists in user db

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category = 'success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user = current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        surName = request.form.get('surName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(password1) < 7:
            flash('Your password must be at least 7 characters.', category='error')
        elif password1 != password2:
            flash('Passwords do not match!', category='error')
        else:
            # Insert new User into the database
            if not user_exists(email):
                new_user = User(firstName, surName, email, password1)
            else:
                print("User already exists.")
            login_user(new_user, remember = True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user = current_user)