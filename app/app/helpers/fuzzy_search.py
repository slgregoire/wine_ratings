#fuzzy search functionality

from fuzzywuzzy import fuzz
import pymongo 

def fuzzy_search(search):
	#connect to db and collection
	client = pymongo.MongoClient()
	db = client.wine_ratings
	collection = db.wine_enthusiast

	#query db for all documents
	docs = collection.find()

	#execute fuzzy search
	results = []
	scores = []
	for doc in docs:
		score = fuzz.token_set_ratio(search, doc['name'])
		results_item = {
			'score': score,
			'doc': doc
		}
		results.append(results_item)

	sorted_results = sorted(results, key=lambda k: k['score'], reverse=True)

	return sorted_results
	


