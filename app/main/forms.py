from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField,SelectField,ValidationError
from wtforms.validators import InputRequired,Email
from ..models import Subscribe

class CommentForm(FlaskForm):

    comment = TextAreaField('Comment')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):

    title = StringField('Title')
    text = TextAreaField('Blog')
    submit = SubmitField('Submit')

class UpdateBlog(FlaskForm):
    text = TextAreaField('Edit blog ')
    submit = SubmitField('Update')

class SubscriptionForm(FlaskForm):

    email = StringField('Your Email Address',validators=[InputRequired(),Email()])
    submit = SubmitField('Subscribe')

    def validate_email(self,data_field):
        if Subscribe.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is a subscriber with that email')