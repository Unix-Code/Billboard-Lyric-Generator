from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class Params(FlaskForm):
    prime = StringField('Prime')
    submit = SubmitField('Generate')
