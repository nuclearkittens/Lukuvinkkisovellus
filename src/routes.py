from app import app
from db import db
from flask import render_template, redirect, flash, request, session
from services.user_service import user_service
from repositories.user_repository import user_repository
from forms import LoginForm, RegisterForm


@app.route("/")
def render_home():
    form = LoginForm()
    return render_template("index.html", form = form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if user_service.login(username,password):
            flash("login succesful")
            return redirect("/")
        else:
            return render_template("index.html", form = form, error="Invalid username of password")
    return render_template("index.html", form = form)


@app.route("/logout")
def logout():
    user_service.logout()
    flash("logged out")
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if user_service.register(username, password):
            if user_service.login(username, password):
                return redirect("/")
        else:
            flash("Username taken")
    return render_template("register.html", form=form)

# For run robot bash script

@app.route("/ping")
def ping():
    return "Pong"


@app.route("/try_db")
def try_db():
    sql = "INSERT INTO users (username, password) VALUES ('Paavo', 'Pesusieni22')"
    db.session.execute(sql)
    sql = "SELECT username FROM users"
    result = db.session.execute(sql)
    sql = "DELETE FROM users WHERE username='Paavo'"
    db.session.commit()
    row = result.fetchone()
    name = row[0]

    return f"heippa {name}"
