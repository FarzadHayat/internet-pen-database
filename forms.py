from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired

class Select_Pen(FlaskForm):
    pens = SelectField('pens', validators = [DataRequired()], coerce = int)