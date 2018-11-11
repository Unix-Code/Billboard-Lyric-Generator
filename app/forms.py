from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField

class Params(FlaskForm):
    #prime = StringField('Prime')
    song = TextAreaField('Song', default="")
    submit = SubmitField('Generate Your Hit!')
