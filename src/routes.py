from flask import render_template, redirect, flash, request, session, abort
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
from services.tag_service import TagService
from repositories.user_repository import UserRepository
from repositories.book_repository import BookRepository
from repositories.podcast_repository import PodcastRepository
from repositories.blog_repository import BlogRepository
from repositories.video_repository import VideoRepository
from repositories.tag_repository import TagRepository
from forms import BlogForm, BookForm, IsbnForm, LoginForm, PodcastForm, RegisterForm, SearchForm, VideoForm, TagForm

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
tag_repository = TagRepository(db)
tag_service = TagService(tag_repository)



@app.route("/", methods=["GET", "POST"])
def render_home():
    form = LoginForm()
    books = None
    podcasts = None
    blogs = None
    videos = None
    keyword = ""
    checked_types = ["books", "podcasts", "blogs", "videos"]

    search_form = SearchForm()
    if search_form.validate_on_submit():
        keyword = search_form.keyword.data
        checked_types = request.form.getlist("type_check")

    if "user_id" in session.keys():
        if "books" in checked_types:
            books = book_service.get_my_books(session["user_id"])
        if "podcasts" in checked_types:
            podcasts = podcast_service.get_my_podcasts(session["user_id"])
        if "blogs" in checked_types:
            blogs = blog_service.get_my_blogs(session["user_id"])
        if "videos" in checked_types:
            videos = video_service.get_my_videos(session["user_id"])

    return render_template(
        "index.html",
        form=form,
        search_form=search_form,
        books=books,
        podcasts=podcasts,
        blogs=blogs,
        videos=videos,
        keyword=keyword,
        checked_types=checked_types
        )


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

        if book_service.new_book(Book(author=author, title=title, isbn=isbn, description=description), user_id):
            return redirect("/")
        flash("Something went wrong...")
    return render_template("new_book.html", form=form)

@app.route("/search_isbn", methods=["GET", "POST"])
def search_isbn():
    form = IsbnForm()

    if form.validate_on_submit():
        isbn = form.isbn.data
        description = form.description.data
        book_info = book_service.get_book_info_from_isbn(isbn)

        if book_info is None:
            flash("No info found with this ISBN")
            return redirect("/search_isbn")

        author = book_info["author"]
        title = book_info["title"]
        user_id = session["user_id"]

        if book_service.new_book(Book(author=author, description=description, title=title, isbn=isbn), user_id):
            return redirect("/")

    return render_template("search_isbn.html", form=form)

@app.route("/books/<int:book_id>", methods=["GET", "POST"])
def book(book_id):
    book = book_service.get_book(book_id)
    user_tags = tag_service.get_tags(session["user_id"])
    form = BookForm()
    if book_service.is_book_mine(session["user_id"], book_id):
        if form.validate_on_submit():
            author = form.author.data
            title = form.title.data
            isbn = form.isbn.data
            description = form.description.data
            read_check = request.form.get("read_check")
            tag_check = request.form.getlist("tag_check")
            book_service.remove_all_tags_by_book(book_id)
            for tag_id in tag_check:
                book_service.attach_tag(int(tag_id), book_id)
            if read_check == "readed":
                book_service.mark_book_finished(book_id)
            else:
                # To be implemented...
                # book_service.mark_book_unfinished(book_id)
                pass
            if book_service.update_book(author, title, description, isbn, book_id):
                return redirect("/")
            flash("Something went wrong...")
    else:
        abort(403)
    return render_template("book.html", book=book, form=form, user_tags=user_tags)


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

@app.route("/blogs/<int:blog_id>", methods=["GET", "POST"])
def blog(blog_id):
    blog = blog_service.get_blog(blog_id)
    if blog_service.is_blog_mine(session["user_id"], blog_id):
        if request.method == "POST":
            if "mark_as_read" in request.form:
                blog_service.mark_blog_finished(blog_id)
                return redirect("/")
    else:
        abort(403)
    return render_template("blog.html", blog=blog)

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

@app.route("/videos/<int:video_id>", methods=["GET", "POST"])
def video(video_id):
    video = video_service.get_video(video_id)
    if video_service.is_video_mine(session["user_id"], video_id):
        if request.method == "POST":
            if "mark_as_read" in request.form:
                video_service.mark_video_finished(video_id)
                return redirect("/")
    else:
        abort(403)
    return render_template("video.html", video=video)

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

@app.route("/podcasts/<int:podcast_id>", methods=["GET", "POST"])
def podcast(podcast_id):
    podcast = podcast_service.get_podcast(podcast_id)
    if podcast_service.is_podcast_mine(session["user_id"], podcast_id):
        if request.method == "POST":
            if "mark_as_read" in request.form:
                podcast_service.mark_podcast_finished(podcast_id)
                return redirect("/")
    else:
        abort(403)
    return render_template("podcast.html", podcast=podcast)

@app.route("/tags/<int:user_id>", methods=["GET", "POST"])
def tags(user_id):
    form = TagForm()
    user_tags = tag_service.get_tags(user_id)
    
    if form.validate_on_submit():
        name = form.name.data
        tag_service.add_tag(name, user_id)
        return redirect(f"/tags/{user_id}")

    return render_template("tag.html", form=form, user_tags=user_tags)

@app.route("/tags/<int:user_id>/<int:tag_id>", methods=["POST"])
def delete_tag(user_id, tag_id):
    tag_service.delete_tag(tag_id)
    return redirect(f"/tags/{user_id}")

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


