from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, GameStatistic
from datetime import datetime
from app import bcrypt, mail
from flask_mail import Message
from forms import RegistracionForm
routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')


@routes.route('/registration', methods=["GET", "POST"])
def registration():
    form = RegistracionForm()
    if request.method == "POST":
        username = form.username.data
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("This user already exist. Try different name.")
        else:
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash("Registration complete")
            return redirect(url_for("routes.login"))
    return render_template("registration.html", form=form, now=datetime.now())


@routes.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash("Prisijungimas sėkmingas!")
            return redirect(url_for("hangman_game"))
        flash("Klaidingi prisijungimo duomenys.")
    return render_template("login.html", now=datetime.now())


@routes.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Sėkmingai atsijungta.")
    return redirect(url_for("login"))


@routes.route('/reset-password')
def reset_password():
    return render_template('reset_password.html')


@routes.route('/statistics')
def statistics():
    stats = GameStatistic.query.order_by(GameStatistic.played_at.desc()).all()
    return render_template('statistics.html', stats=stats)


@routes.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form["email"]
        user = User.query.filter_by(email=email).first()
        if user:
            msg = Message("Slaptažodžio priminimas", recipients=[email])
            msg.body = f"Jūsų slaptažodį reikia nustatyti iš naujo. Apsilankykite: http://localhost:8000/reset"
            mail.send(msg)
            flash("El. laiškas išsiųstas.")
        else:
            flash("Vartotojas nerastas.")
    return render_template("forgot_password.html")


@routes.route('/hangman-game')
@login_required
def hangman_game():
    return render_template('hangman_game.html', user=current_user)
