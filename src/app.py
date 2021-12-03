
from flask import Flask
from config import URI, SECRET_KEY

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = URI

import routes # pylint: disable=wrong-import-position, unused-import
