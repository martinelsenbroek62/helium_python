from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class LoginForm(FlaskForm):
    email = StringField()
    password = PasswordField()

class ProfileForm(FlaskForm):
    email = StringField()
    name = StringField()
    password = PasswordField()

class ForgotPasswordForm(FlaskForm):
    email = StringField()

class ResetPasswordForm(FlaskForm):
    password = PasswordField()
    password1 = PasswordField(label="Confirm password")

class UserSignupForm(FlaskForm):
    email = StringField()
    password = PasswordField()
    password2 = PasswordField()