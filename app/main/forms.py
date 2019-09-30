from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
	title = StringField('Title', validators=[Required()])
	description = TextAreaField("What would you like to post ?",validators=[Required()])
	category = RadioField('Label', choices=[ ('music','music'), ('lifestyle','lifestyle'),('sports','sports'),('fashion','fashion')],validators=[Required()])
	submit = SubmitField('Submit')

class CommentForm(FlaskForm):
	description = TextAreaField('Add comment',validators=[Required()])
	submit = SubmitField()

class UpdateForm(FlaskForm):
	title = StringField('Title', validators=[Required()])
	description = TextAreaField("What would you like to post ?",validators=[Required()])
	category = RadioField('Label', choices=[ ('music','music'), ('lifestyle','lifestyle'),('sports','sports'),('fashion','fashion')],validators=[Required()])
	submit = SubmitField('Submit')

