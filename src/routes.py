from flask import render_template, redirect, flash, request, session
from app import app
from db import db
from entities.user import User
from entities.book import Book
from entities.podcast import Podcast
from entities.blog import Blog
from entities.video import Video
from services.user_service import UserService
from services.book_service import BookService
from services.podcast_service import PodcastService
from services.blog_service import BlogService
from services.video_service import VideoService
from repositories.user_repository import UserRepository
from repositories.book_repository import BookRepository
from repositories.podcast_repository import PodcastRepository
from repositories.blog_repository import BlogRepository
from repositories.video_repository import VideoRepository
from forms import BlogForm, BookForm, LoginForm, PodcastForm, RegisterForm, VideoForm

user_repository = UserRepository(db)
user_service = UserService(user_repository, session)
book_repository = BookRepository(db)
book_service = BookService(book_repository)
podcast_repository = PodcastRepository(db)
podcast_service = PodcastService(podcast_repository)
blog_repository = BlogRepository(db)
blog_service = BlogService(blog_repository)
video_repository = VideoRepository(db)
video_service = VideoService(video_repository)



@app.route("/")
def render_home():
    form = LoginForm()
    books = None
    podcasts = None
    blogs = None
    videos = None
    if "user_id" in session.keys():
        books = book_service.get_my_books(session["user_id"])
        podcasts = podcast_service.get_my_podcasts(session["user_id"])
        blogs = blog_service.get_my_blogs(session["user_id"])
        videos = video_service.get_my_videos(session["user_id"])
    return render_template("index.html", form=form, books=books, podcasts=podcasts, blogs=blogs, videos=videos)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if user_service.login(User(username, password)):
            flash("login succesful")
            return redirect("/")
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
        flash("Something went wrong...")
    return render_template("new_book.html", form=form)


@app.route("/books/<int:book_id>", methods=["GET", "POST"])
def book(book_id):
    # Tässä pitäis olla joku user_service.check_user()
    # joka tarkistaa, että user_id on sama kuin kyseisen kirjan tekijän user_id
    # jos ei, niin abort(403)
    # ^ Toteutin tän tarkastuksen book_servicen ja book_repositoryn kautta, kuten alla näkyy T: Jirko
    book_info = [book_id]
    if book_service.is_book_mine(session["user_id"], book_id):
        if request.method == "POST":
            if "mark_as_read" in request.form:
            # WIP
                book_service.mark_book_finished(book_id)
                return redirect("/")
    else:
        # Tähän "pääsy kielletty"-herja tms ja redirect indexiin.
        pass
    return render_template("book.html", book_info=book_info)


@app.route("/new_blog", methods=["GET", "POST"])
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        author = form.author.data
        title = form.title.data
        url = form.url.data
        description = form.description.data
        user_id = session["user_id"]
        if blog_service.new_blog(Blog(author, title, url, description), user_id):
            return redirect("/")
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
        title = form.title.data
        episode = form.episode.data
        description = form.description.data
        user_id = session["user_id"]
        if podcast_service.new_podcast(Podcast(title, episode, description), user_id):
            return redirect("/")
    return render_template("new_podcast.html", form=form)


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
