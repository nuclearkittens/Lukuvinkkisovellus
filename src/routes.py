from app import app
from db import db
from flask import render_template, redirect, flash, request, session
from services.user_service import UserService
from entities.user import User
from repositories.user_repository import UserRepository
from forms import BookForm, LoginForm, RegisterForm

user_repository = UserRepository(db)
user_service = UserService(user_repository, session)

@app.route("/")
def render_home():
    form = LoginForm()
    return render_template("index.html", form = form)
    #kun book_service on olemassa lisää render_template argumentteihin
    #books = book_service.get_my_books(user_id) yms, joka antaa index.html:lle
    #tiedot omista kirjoista, jotta voi rendaa ne


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if user_service.login(User(username,password)):
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
        user = User(username, password)
        if user_service.register(user):
            if user_service.login(user):
                return redirect("/")
        else:
            flash("Username taken")
    return render_template("register.html", form=form)

@app.route("/new_book", methods=["GET", "POST"])
def new_book():
    form = BookForm()
    if form.validate_on_submit():
        author = form.author.data
        title = form.title.data
        isbn = form.isbn.data
        if book_service.new_book(author, title, isbn):
            return redirect("/")
        else:
            flash("Something went wrong...")
    return render_template("new_book.html", form=form)

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
