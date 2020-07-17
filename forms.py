from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired,ValidationError
from .models import UserInfo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])

    def validate_username(self,username):
        user = UserInfo.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('pls someone has taken this username,try another one')


    def validate_email(self,email):
        user = UserInfo.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('pls someone has login with this email,check it very well')