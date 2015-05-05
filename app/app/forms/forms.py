from flask_wtf import Form
from wtforms import StringField, SubmitField, validators

class FuzzyForm(Form):
	search_terms = StringField('Please enter your search terms', validators=[validators.InputRequired()])
	submit = SubmitField('Submit')
