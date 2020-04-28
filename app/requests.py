from app import app
import urllib.request,json
from .models import sources, articles
#getting api_key
Sources = sources.Sources
articles = articles.Articles

api_key = app.config['NEWS_API_KEY']

#getting the sources and the articles base api url

base_url = ["NEWS_SOURCES_BASE_URL"]
articles_base_url =["ARTICLES_BASE_URL"]

def get_sources(category):
	'''
	Function that gets the json response to our url request
	'''
	get_sources_url = base_url.format(category,api_key)

	with urllib.request.urlopen(get_sources_url) as url:
		get_sources_data = url.read()
		get_sources_response = json.loads(get_sources_data)

		sources_results = None

		if get_sources_response['sources']:
			sources_results = process_results(get_sources_response['sources'])

	return sources_results

def process_results(sources_list):
    
    '''
    Function  that processes the source result and transform them to a list of Objects
    Args:
        source_list: A list of dictionaries that contain news source details
    Returns :
        source_results: A list of source objects
        
    '''
    
    source_results = []
    for source_item in sources_list:
        
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')
        language = source_item.get('language')
        
        if url:
            source_object = Sources(id,name.description,url,category,country,language)
            source_results.append(source_object)
            
        
    return source_results