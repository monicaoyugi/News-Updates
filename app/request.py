import urllib.request, json
from .models import Sources, News

from config import Config

api_key = None
base_url = None
article_url = None


def configure_request(app):
    global api_key, base_url, article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['ARTICLE_API_BASE_URL']


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

    return result


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


def get_articles(id):
    get_articles_url = article_url.format(id, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_source = url.read()
        response = json.loads(get_source)
        if response['articles']:
            rep = response['articles']
            result = process_articles(rep)

    return result


def process_articles(articles):
    result = []

    for news in articles:
        description = news['description']
        urlToImage = news['urlToImage']
        publishedAt = news['publishedAt']

        object_news = News(description, urlToImage, publishedAt)

        if description:
            result.append(object_news)

    return result
