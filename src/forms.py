from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, InputRequired

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=36)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=36)])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign up")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=36)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
