#view file for wine ratings database search page

from flask import Blueprint, render_template, request, flash
from app.helpers.fuzzy_search import fuzzy_search
from app.forms.forms import FuzzyForm

search_bp = Blueprint('search_bp', __name__)

@search_bp.route('/', methods=['GET','POST'])
def search():
	fuzzy_form = FuzzyForm()

	if fuzzy_form.validate_on_submit():
		search_terms = fuzzy_form.search_terms.data 
		results = fuzzy_search(search_terms)
		results_exist = 'results' in locals()
		
		return render_template('search.html', form=fuzzy_form, results=results, results_exist=results_exist)
	elif request.method == 'POST':
		flash('No wine name was entered.')

	return	render_template('search.html', form=fuzzy_form, results=None, results_exist=False)
