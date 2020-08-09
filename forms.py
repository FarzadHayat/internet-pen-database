from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import IntegerField, TextField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired, Optional, ValidationError
import models

class Select_Pen(FlaskForm):
    pens = SelectField('pens', validators = [DataRequired()], coerce = int)

class Add_Brand(FlaskForm):
    name = TextField('name', validators=[DataRequired()])
    desc = TextAreaField('desc', validators=[Optional()])
    photo = FileField('photo', validators=[FileAllowed(['jpg', 'png']), Optional()])