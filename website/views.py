from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, UserInfo
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint("views", __name__)


@views.route("/")
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    if request.method == "POST":
        surname = request.form.get("surname")
        if len(surname) < 2:
            flash("Surname too short!", category="error")
        else:
            new_surname = UserInfo(surname=surname, user_id=current_user.id)
            db.session.add(new_surname)
            db.session.commit()
            flash("Profile Updated", category="success")

        return render_template("profile.html", user=current_user)
