
from flask import Flask
from os import getenv
from config import URI, SECRET_KEY

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["TEMPLATES_AUTO_RELOAD"] = True
#app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
#app.secret_key = getenv("SECRET_KEY")
app.secret_key = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = URI

import routes