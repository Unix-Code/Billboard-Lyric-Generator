from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, URL

class Params(FlaskForm):
    prime = StringField('Prime')
    submit = SubmitField('Generate')
