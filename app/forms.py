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
    first = RadioField('Выберите тип организации общественного питания', choices = ('Ресторан', 'Бар', 'Кафе', 'Столовая', 'Закусочная', 'Кафетерий', 'Магазин-кулинариная', 'Другое'))
    second = StringField('Наименование организации (включая форму собственности)', validators = [Length(min = 1, max = 25)])
    third = StringField('ФИО руководителя', validators = [Length(min = 1, max = 40)])
    fourth = StringField('Электронный адрес руководителя', validators = [Length(min = 1, max = 32)])
    fifth = StringField('ФИО куратора проекта с вашей стороны', validators = [Length(min = 1, max = 40)])
    sixth = StringField('Электронный адрес куратора проекта', validators = [Length(min = 1, max = 32)])
    seventh = StringField('Ваше местоположение (фактическое)', validators = [Length(min = 1, max = 50)])
    eighth = RadioField('Есть ли в компании менеджер по корпоративной социальной ответственности?', choices = ('Да', 'Нет'))
    ninth = RadioField('Был ли у вас опыт внедрения мер по снижению экологического следа в организации?', choices = ('Да', 'Нет'))
    tenth = StringField('Опишите кратко ваш опыт работы по снижению экологического следа', validators = [Length(min = 1, max = 50)])
    eleventh = StringField('С какими компаниями работали ранее?', validators = [Length(min = 1, max = 50)])
    twelfth = RadioField('Какие направления снижения экологического следа вам интересны?', choices = ('Ответственное обращение с отходами', 'Водоочистка', 'Энергосбережение', 'Экопросвещение', 'Ответственные закупки', 'Материалы для ремонта и строительства', 'Углеродный след'))
    thirteenth = RadioField('Ваша компания', choices = ('Арендует помещение', 'Находится в собственном помещении'))
    fourteenth = StringField('Общая площадь помещения (м2)', validators = [Length(min = 1, max = 8)])
    fifteenth = StringField('Количество посадочных мест', validators = [Length(min = 1, max = 8)])
    sixteenth = StringField('Количество сотрудников', validators = [Length(min = 1, max = 8)])
    seventeenth = StringField('Перечислите отходы, которые вы хотели бы переработать с указанием количества и промежутка времени (если известны)', validators = [Length(min = 1, max = 40)])
    eighteenth = RadioField('Сдаете в переработку макулатуру?', choices = ('Да, постоянно', 'Иногда', 'Нет', 'Нет таких отходов'))

    twentyth = RadioField(' Какой объем макулатуры в процентах вы сдаете в переработку? ', choices = ('до 50%', '50%', 'от 50% до 100%', 'Нет таких отходов'))
    twentyfirst = RadioField(' Сдаете в переработку металл (алюминий, фольгу, металлические предметы и упаковку)? ', choices = ('Да, постоянно', 'Иногда', 'Нет', 'Нет таких отходов'))
    twentysecond = RadioField(' Какой объем металла в процентах вы сдаете в переработку? ', choices = ('до 50%', '50%', 'от 50% до 100%', 'Нет таких отходов'))
    twentythird = RadioField(' Сдаете в переработку пластиковую тару? ', choices = ('Да, постоянно', 'Иногда', 'Нет', 'Нет таких отходов'))
    twentyfourth = RadioField(' Какой объем пластика в процентах вы сдаете в переработку? ', choices = ('до 50%', '50%', 'от 50% до 100%', 'Нет таких отходов'))
    twentyfifth = RadioField(' Сдаете в переработку стекло? ', choices = ('Да, постоянно', 'Иногда', 'Нет', 'Нет таких отходов'))
    twentysixth = RadioField(' Какой объем стекла в процентах вы сдаете в переработку? ', choices = ('до 50%', '50%', 'от 50% до 100%', 'Нет таких отходов'))
    twentyseventh = RadioField(' Сдаете ли в переработку тетрапак и их аналоги? ', choices = ('Да, постоянно', 'Иногда', 'Нет', 'Нет таких отходов'))
    twentyeighth = RadioField(' Сколько процентов тетрапака и аналогов сдаете в переработку? ', choices = ('до 50%', '50%', 'от 50% до 100%', 'Нет таких отходов'))
    twentyninth = RadioField(' Сдаете в переработку ртутные лампы? ', choices = ('Да, постоянно', 'Иногда', 'Нет', 'Нет таких отходов'))
    thirtieth = RadioField(' Сдаете в переработку батарейки? ', choices = ('Да', 'Нет'))
    thirtyfirst = RadioField(' Сдаете в переработку аккумуляторы? ', choices = ('Да, постоянно', 'Иногда', 'Нет', 'Нет таких отходов'))
    thirtysecond = RadioField(' Участвуете в акции "Добрые крышечки" или в других подобных акциях? ', choices = ('Да', 'Нет'))
    thirtythird = RadioField(' Сдаете в переработку электротехнику и электронику? ', choices = ('Да, постоянно', 'Иногда', 'Нет', 'Нет таких отходов'))
    thirtyfourth = RadioField(' Сдаете в переработку отслуживший текстиль? ', choices = ('Да, постоянно', 'Иногда', 'Нет', 'Нет таких отходов'))
    thirtyfifth = RadioField(' Ремонтируете ли вещи, чтобы дать им "вторую жизнь"? ', choices = ('Да, постоянно', 'Иногда', 'Нет', 'Нет таких отходов'))
    thirtysixth = RadioField(' Пользуетесь ли шеринговыми платформами для сдачи отслуживших вещей и предметов еще пригодных для использования? ', choices = ('Да, постоянно', 'Иногда', 'Нет', 'Нет таких отходов'))
    thirtyseventh = RadioField(' Перерабатываете ли пищевые отходы? ', choices = ('Да, постоянно', 'Иногда', 'Нет', 'Нет таких отходов'))
    thirtyeughth = RadioField(' Используете ли компостирование (холодное или горячее) для переработки пищевых отходов?  ', choices = ('Да', 'Нет'))
    thirtyninth = RadioField(' Используете ли вермитехнологии для переработки пищевых отходов? ', choices = ('Да', 'Нет'))
    fortieth = RadioField(' Используете ли другие способы переработки пищевых отходов? ', choices = ('Да', 'Нет'))
    fourtyfirst = RadioField(' Сотрудничаете ли с проектами фудшеринга? ', choices = ('Да', 'Нет'))
    fourtysecond = RadioField(' Сколько пищевых отходов в процентах, по вашему мнению, перерабатывают в вашей организации? ', choices = ('до 50%', '50%', 'от 50% до 100%', 'Нет таких отходов'))
    fourtythird = RadioField(' Есть ли возможность для накопления чистого (без запаха) вторсырья в помещениях или на улице? ', choices = ('Да', 'Нет'))
    fourtyfourth = RadioField(' Есть ли возможность для накопления органики (возможно с запахом) в помещениях или на улице? ', choices = ('Да', 'Нет'))
    fourtyfifteenth = RadioField(' Есть ли возможность самостоятельного круглосуточного вывоза отходов? ', choices = ('Да', 'Нет'))
    fourtysixteenth = RadioField(' Есть ли услуга доставки продуктов питания? ', choices = ('Да', 'Нет'))
    fourtyeighteenth = RadioField(' Можно ли у вас при заказе на дом отказаться от одноразовой посуды, салфеток и соусов при доставке на дом? * ', choices = ('Да', 'Нет'))
    submit = SubmitField('Confirm')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    about_me = TextAreaField('About me', validators = [Length(min = 0, max = 140)])
    public = BooleanField('Make your results public')
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

class ResponsibilityWaste_alt(FlaskForm):
    first =  RadioField(' Можно ли у вас при заказе на дом отказаться от одноразовой посуды, салфеток и соусов при доставке на дом? * ', choices = ('Да', 'Нет'))
    submit = SubmitField('Confirm')
    def fff(self, keys):
        ResponsibilityWaste_alt.first = RadioField(keys[0],  choices = tuple(keys[1]))

class TestForm(FlaskForm):
    eighteenth = RadioField('Сдаете в переработку макулатуру?', choices = ('Да, постоянно', 'Иногда', 'Нет', 'Нет таких отходов'))
    twentyth = RadioField(' Какой объем макулатуры в процентах вы сдаете в переработку? ', choices = ('до 50%', '50%', 'от 50% до 100%', 'Нет таких отходов'))
    twentyfirst = RadioField(' Сдаете в переработку металл (алюминий, фольгу, металлические предметы и упаковку)? ', choices = ('Да, постоянно', 'Иногда', 'Нет', 'Нет таких отходов'))
    submit = SubmitField('Confirm')