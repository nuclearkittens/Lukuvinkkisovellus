from app import app
from db import db
from flask import render_template
from services.user_service import user_service
from repositories.user_repository import user_repository


@app.route("/")
def render_home():
    return render_template("index.html")

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
    