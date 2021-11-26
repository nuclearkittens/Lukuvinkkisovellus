from flask_sqlalchemy import SQLAlchemy
from app import app
from config import URI

app.config['SQLALCHEMY_DATABASE_URI'] = URI
db = SQLAlchemy(app)

# get rid of error message when starting server
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
