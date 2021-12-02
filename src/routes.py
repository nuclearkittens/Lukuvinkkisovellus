from app import app
from db import db
from flask import render_template, redirect, flash, request, session
from services.user_service import UserService
from entities.user import User
from repositories.user_repository import UserRepository
from services.book_service import BookService
from entities.book import Book
from repositories.book_repository import BookRepository
from forms import BlogForm, BookForm, LoginForm, PodcastForm, RegisterForm, VideoForm

user_repository = UserRepository(db)
user_service = UserService(user_repository, session)
book_repository = BookRepository(db)
book_service = BookService(book_repository)

@app.route("/")
def render_home():
    form = LoginForm()
    books = None
    if "user_id" in session.keys():
        books = book_service.get_my_books(session["user_id"])
    return render_template("index.html", form=form, books=books)



@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if user_service.login(User(username, password)):
            flash("login succesful")
            return redirect("/")
        else:
            return render_template("index.html", form=form, error="Invalid username of password")
    return render_template("index.html", form=form)


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
        if user_service.register(User(username, password)):
            flash("Registration succesful")
            if user_service.login(User(username, password)):
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
        description = form.description.data
        user_id = session["user_id"]

        if book_service.new_book(Book(author, title, isbn, description), user_id):
            return redirect("/")
        else:
            flash("Something went wrong...")
    return render_template("new_book.html", form=form)

@app.route("/books/<int:id>", methods=["GET", "POST"])
def book(id):
    book_info = [id]
    if request.method == "GET":
        return render_template("book.html", book_info=book_info)
    
    if request.method == "POST":
        if "mark_as_read" in request.form:
            #TODO
            #book_service.mark_as_read()...
            return redirect("/")
        

@app.route("/new_blog", methods=["GET", "POST"])
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        url = form.url.data
        description = form.description.data
        user_id = session["user_id"]
        if blog_service.new_blog(Blog(title, author, url, description), user_id):
            return redirect("/")
        else:
            flash("Something went wrong...")
    return render_template("new_blog.html", form=form)

@app.route("/new_video", methods=["GET", "POST"])
def new_video():
    form = VideoForm()
    if form.validate_on_submit():
        title = form.title.data
        url = form.url.data
        description = form.description.data
        user_id = session["user_id"]
        if video_service.new_video(Video(title, url, description), user_id):
            return redirect("/")
    return render_template("new_video.html", form=form)

@app.route("/new_podcast", methods=["GET", "POST"])
def new_podcast():
    form = PodcastForm()
    if form.validate_on_submit():
        podcast_name = form.podcast_name.data
        title = form.title.data
        description = form.description.data
        user_id = session["user_id"]
        if podcast_service.new_podcast(Podcast(podcast_name, title, description), user_id):
            return redirect("/")
    return render_template("new_podcast.html", form=form)



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
