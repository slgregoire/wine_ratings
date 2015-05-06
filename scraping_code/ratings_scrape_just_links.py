#NOTE: this code just collects links to detailed product pages

import requests
import pyquery as pq
import pandas as pd 


#hostname that needs to be prepended to the href links to create full url to product detail page
url_begin = r'http://buyingguide.winemag.com/'
url_end_list = r'search/types/wines'

#list to populate with scraped data
all_links = []
while url_end_list:

	#pull html document
	url_list = url_begin + url_end_list
	r_list = requests.get(url_list)

	##parse html and grab links, and add to list
	parsed_list = pq.PyQuery(r_list.text)
	a_tags = parsed_list('div.wines').find('.expert-rating').parent()
	links = [tag.attrib['href'] for tag in a_tags]
	all_links.extend(links)
	
	#update url to call next page in wine list
	url_end_list = parsed_list('.command.next-page').attr['href']
	print('link list size: ', len(all_links))

#writing links to csv
link_series = pd.Series(all_links, name='links')
link_series.to_csv('wine_enthusiast_links.csv', header=True)

    
