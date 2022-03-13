from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField,SelectField
from wtforms.validators import InputRequired

class CommentForm(FlaskForm):

    comment = TextAreaField('Comment')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):

    title = StringField('Title', validators=[InputRequired()])
    text = TextAreaField('Add pitch', validators=[InputRequired()])
    submit = SubmitField('Submit')

class SubscriptionForm(FlaskForm):

    submit = SubmitField('Subscribe')