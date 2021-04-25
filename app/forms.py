from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FileField, RadioField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class ResponsibilityWaste(FlaskForm):
    #username = StringField('Username', validators=[DataRequired()])
    #email = StringField('Email', validators=[DataRequired(), Email()])
    #example = RadioField('Label', choices=[('sec','description'),('sec1','whatever')])
    first = RadioField('Выберите тип организации общественного питания', choices = ('Ресторан', 'Бар', 'Кафе', 'Столовая', 'Закусочная', 'Кафетерий', 'Магазин-кулинариная', 'Другое'))
    #second = StringField('Наименование организации (включая форму собственности)', validators = [Length(min = 1, max = 25)])
    submit = SubmitField('Confirm')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    about_me = TextAreaField('About me', validators = [Length(min = 0, max = 140)])
    image = FileField('Avatar')
    submit = SubmitField('Submit')

    def __init__(self, original_name, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_name = original_name

    def validate_username(self, username):
        if username.data != self.original_name:
            user = User.query.filter_by(username = username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')