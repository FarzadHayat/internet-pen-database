from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import IntegerField, StringField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired, Optional, ValidationError

class Search(FlaskForm):
    brand = SelectField('brand', validators = [DataRequired()])
    tag = SelectField('tag', validators = [DataRequired()])


class Add_Brand(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    desc = TextAreaField('desc', validators=[Optional()])
    photo = FileField('photo', validators=[FileAllowed(['jpg', 'png']), Optional()])