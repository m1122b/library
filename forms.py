
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms import validators
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    author = StringField('Autor')
    description = TextAreaField('Opis')
    done = BooleanField('Czy przeczytana?')





