import os

class Config:

    NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?apiKey={}&language=en'
    # https://newsapi.org/v2/top-headlines/sources?apiKey={}
    # https://newsapi.org/v2/sources?apiKey={}&language=en
    ARTICLES_BASE_URL =  'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = '8120360ba9e342dbaccb75e01109ca34'
    # SECRET_KEY = os.environ.get('SECRET_KEY')

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}