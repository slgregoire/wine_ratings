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
		return render_template('search.html', form=fuzzy_form, results=results)
	elif request.method == 'POST':
		flash('Actually enter searchable terms, please')

	return	render_template('search.html', form=fuzzy_form, results=None)

@search_bp.route('/detail', methods=['GET'])
def detail():
	name = request.args.get('name')
	rating = request.args.get('rating')
	review = request.args.get('review')
	return	render_template('detail.html', name=name, rating=rating, review=review)