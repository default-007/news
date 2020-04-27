from app import app
import urllib.request,json
#getting api_key
Sources = sources.Sources
articles = articles.Articles

api_key = app.config['NEWS_API_KEY']

#getting the sources and the articles base api url

source_base_url = ["NEWS_SOURCES_BASE_URL"]
articles_base_url =["ARTICLES_BASE_URL"]

def get_sources(category):
    
    '''
    Function that gets the json response to our url request
    
    '''
    get_sources_url = source_base_url.format(category,api_key)
    
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        
        source_results = None
        
        if get_sources_response['results']:
            source_results_list = get_sources_response['results']
            
            source_results = process_results(source_results_list)
            
    return source_results