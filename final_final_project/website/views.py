from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():

    return render_template("home.html")

@views.route('/help')
def help():
    return render_template("help.html")

@views.route('/flights', methods=['GET', 'POST'])
# @login_required
def reservation():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         surname = request.form.get('surname')
#         flight = request.form.get('flight')
#         seat = request.form.get('seat')
#
#         if len(name) < 2:
#             flash('Name must be greater than 1 character.', category='error')
#         else:
#             # Insert new Reservation into the database
#             flash('Reservation completed!', category='success')

    return render_template("flights.html")