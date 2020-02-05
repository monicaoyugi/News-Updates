import urllib.request, json
from .models import Sources

from config import Config

api_key = None
base_url = None


# NEWS_API_BASE_URL = app.config['NEWS_API_BASE_URL']

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_sources():
    sources_url = base_url.format(api_key)
    print('*************sources url******')
    print(sources_url)
    with urllib.request.urlopen(sources_url) as url:
        get_source = url.read()
        response = json.loads(get_source)
        if response['sources']:
            rep = response['sources']
            result = process_result(rep)
    # response = requests.get(sources_url)
    # if response.status_code == 200:
    #     for data in response.json()['sources']:
    #         sources.append(data)
    #     print(sources)

    return result


#

def process_result(sources):
    result = []

    for news in sources:
        id = news['id']
        name = news['name']
        description = news['description']
        url = news['url']
        category = news['category']
        language = news['language']
        country = news['country']

        object_news = Sources(id, name, description, url, category, language, country)

        if id:
            result.append(object_news)

    return result

# class NewsRequest:
#     # API_KEY = Config.NEWS_API_KEY
# class NewsRequest:
# API_KEY = Config.NEWS_API_KEY

# def get_articles(self, article):
#     articles = []
#     articles_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(article, self.API_KEY)
#     response = request.urlopen(articles_url)
#     if response.status_code == 200:
#         for data in response.json()['articles']:
#             articles.append(data)
#         print(articles)
#         return articles
#
# def get_article_by_source(self, id):
#     source_article = []
#     source_articles_url = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'.format(id, self.API_KEY)
#     response = request.urlopen(source_articles_url)
#     if response.status_code == 200:
#         for data in response.json()['articles']:
#             source_article.append(data)
#         print('This is a test string...')
#         print(source_article)
#         return source_article
