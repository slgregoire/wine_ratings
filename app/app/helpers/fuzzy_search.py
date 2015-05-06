#fuzzy search functionality

from fuzzywuzzy import fuzz
import pandas as pd 
import os

def fuzzy_search(search):
	#import json file with wine ratings/reviews into pandas dataframe
	df_ratings = pd.read_json('../data/wine_ratings.json')
	#execute fuzzy search and save results
	df_ratings = df_ratings[:100]
	df_ratings['score'] = df_ratings['name'].map(lambda x: fuzz.token_set_ratio(search, x))
	df_sorted = df_ratings.sort(columns='score', ascending=False)

	return df_sorted
	


