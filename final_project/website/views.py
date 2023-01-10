from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Reservation
import json
# from . import db


views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user = current_user)


@views.route('/make-reservation', methods=['GET', 'POST'])
@login_required
def make_reservation():
    if request.method == 'POST':
        reservation = request.form.get('reservation')
        new_reservation = Reservation(data=reservation, user_id=current_user.id)
        # db.addReservation(new_reservation)                                        # new method to store res in db
        flash('Reservation completed', category = 'success')
    return render_template("reservation.html", user = current_user)


@views.route('/delete-reservation', methods = ['POST'])
# sth like @admin_required
def delete_reservation():
    reservation = json-loads(request.data)
    reservationId = reservation['reservationID']
    reservation = Reservation.query.get(reservationId)
    if reservation:
        # db.session.delete(reservation)                  # other database query
    return jsonify({})