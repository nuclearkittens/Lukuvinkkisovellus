from app import app
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