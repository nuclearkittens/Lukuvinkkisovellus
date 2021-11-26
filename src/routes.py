from app import app
from db import db
from flask import render_template, redirect, flash, request, session
from services.user_service import user_service
from repositories.user_repository import user_repository
from forms import LoginForm, RegisterForm


@app.route("/")
def render_home():
    login_form = LoginForm()
    return render_template("index.html", login_form = login_form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        _username = request.form["username"]
        _password = request.form["password"]
        if user_service.login(_username, _password):
            flash("login succesful!")
            return redirect("/")
        else:
            flash("wrong username or password")
            return redirect("/login")


@app.route("/logout")
def logout():
    user_service.logout()
    flash("logged out")
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        if (request.form["a_password"] != request.form["b_password"]):
            flash("passwords do not match")
            return redirect("/register")
        _username = request.form["username"]
        _password = request.form["a_password"]
        if (not user_service.check_username(_username)):
            flash("invalid username")
            return redirect("/register")
        if (not user_service.check_password(_password)):
            flash("invalid password")
            return redirect("/register")
        if user_service.register(_username, _password):
            flash("new user created")
            return redirect("/")
        else:
            flash("username taken")
            return redirect("/register")


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
