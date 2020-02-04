from flask import render_template, request
from . import main


@main.route('/')
def index():
    sources = request.get_sources()
    if sources:
        return render_template('index.html', sources=sources)


@main.route('/articles', methods=["POST", "GET"])
def articles_page():
    if request.method == 'POST':
        search = request.form.get("search")
        articles = request.get_articles(search)
    else:
        articles = request.get_articles("tech")
    return render_template('articles.html', articles=articles)


@main.route('/article/<id>')
def source_article(id):
    source_articles = request.get_article_by_source(id)
    source = id
    return render_template('articles_display.html', source_articles=source_articles, )
