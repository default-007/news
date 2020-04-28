class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL=('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=29cf65da063444ed9aa21d63d634447b')



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True