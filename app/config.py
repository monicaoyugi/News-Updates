import os


class Config:
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_KEY = os.environ.get= '2de33a139ddd40a08578b60427d6a839'
    SECRET_KEY = os.environ.get('monica')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
