from flask import Flask
from views.search import search_bp

def create_app():

	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'supersecretkey'
	app.register_blueprint(search_bp, url_prefix='')
	
	return app