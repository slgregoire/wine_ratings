#an alternative method of implementing fuzzy search using a pandas in memory dataframe, instead of iterating through documents in a mongodb database. 

from fuzzywuzzy import fuzz
import pandas as pd 
import time

start = time.time()

df_all = pd.read_json('wine_ratings.json')

search = 'Chateau La Tonnelle Haut Medoc, 2011'

df_all['score'] = df_all['name'].map(lambda x: fuzz.token_set_ratio(search, x))

df_sorted = df_all.sort(columns='score', ascending=False)

total_time = time.time() - start