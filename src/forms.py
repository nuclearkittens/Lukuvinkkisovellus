from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[
                           DataRequired(), Length(min=3, max=36)])
    password = PasswordField("Password", validators=[
                             DataRequired(), Length(min=6, max=36)])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(),
                                                                     EqualTo("password")])
    submit = SubmitField("Sign up")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[
                           DataRequired(), Length(min=3, max=36)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


# Myöhemmin kun isbn-haku on toteutettu, niin pitäisi varmaan toteuttaa jonkinlainen systeemi,
# joka tarkistaa onko isbn annettu, jos on niin authoria tai titleä ei tarvitse syöttää..
# Mennään ainakin aluksi tällä


class BookForm(FlaskForm):
    author = StringField(
        "Kirjoittaja (*)", validators=[DataRequired(), Length(min=3, max=50)])
    title = StringField(
        "Otsikko (*)", validators=[DataRequired(), Length(min=2, max=200)])
    isbn = StringField("ISBN")
    description = StringField("Kuvaus")
    submit = SubmitField("Submit")

class BlogForm(FlaskForm):
    title = StringField("Otsikko (*)", validators=[DataRequired()])
    author = StringField("Kirjoittaja (*)", validators=[DataRequired()])
    url = StringField("URL (*)", validators=[DataRequired()])
    description = StringField("Kuvaus")
    submit = SubmitField("Submit")
