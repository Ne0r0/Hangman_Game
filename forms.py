from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from models import User


class RegistracionForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    email = StringField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Repeat password', [EqualTo('password', message='Password must mach!')])
    submit = SubmitField('Registration')
   
    def check_user_name(self, vardas):
        user = User.query.filter_by(vardas=vardas.data).first()
        if user:
            raise ValidationError("Šis vardas panaudotas. Pasirinkite kitą")
        
    def check_user_email(self, el_pastas):
        user = User.query.filter_by(el_pastas=el_pastas.data).first()
        if user:
            raise ValidationError("This email address is already in use, choose other email!")
        
class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField('Login')