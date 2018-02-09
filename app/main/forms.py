from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title= StringField('Enter the pitch category ',validators = [Required()])
    description= StringField('Enter the pitch description' ,validators = [Required()])

    submit = SubmitField('create')

class CommentForm(FlaskForm):

    name= StringField('Enter your comment here' ,validators = [Required()])

    submit = SubmitField('create')
