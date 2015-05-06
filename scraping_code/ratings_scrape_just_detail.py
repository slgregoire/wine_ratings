#scraping data from wine enthusiast's site
#Note that as of now this works on a single page of wines. Need to incorporate flipping through pages

import requests
import pyquery as pq
import pandas as pd 
import json

#read in csv with links
links = pd.read_csv('wine_enthusiast_links.csv')

#hostname that needs to be prepended to the href links to create full url to product detail page
url_begin = r'http://buyingguide.winemag.com/'

#list to populate with scraped data
wine_list = []
count = 0
#cycle through wine product pages and extract name, rating, and expert description
for url_end_item in links.links:

	url_item = url_begin + url_end_item
	r_item = requests.get(url_item)
	parsed_item = pq.PyQuery(r_item.text)

	box = parsed_item('.catalog-header')
	name = box.find('h1').text()
	rating = box.find('.expert-rating').find('.rating').text()
	expert_review = parsed_item('.review.expert-review').find('p').text()

	item = {
		'name': name,
		'expert_review': expert_review,
		'rating': rating
	}
	wine_list.append(item)
	count += 1
	print(count)

#saving scraped data in structured format. what shoudl this be pandas, json, csv? maybe try nosql db?
with open('wine_ratings.json','w') as file:
    json.dump(wine_list, file)

    
