from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField
from wtforms.fields.core import BooleanField
from wtforms.validators import DataRequired

class TheForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    is_home = BooleanField('is it home?', false_values=(False, 'false', 0, '0'))