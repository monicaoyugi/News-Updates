from flask import render_template, request
from . import main
from app.request import get_sources, get_articles


@main.route('/')
def index():
    sources = get_sources()
    print(sources)
    return render_template('index.html', sources=sources)


# @main.route('/articles', methods=["POST", "GET"])
# def articles_page():
#     if request.method == 'POST':
#         search = request.form.get("search")
#         articles = NewsRequest.get_articles(search)
#     else:
#         articles = New  sRequest.get_articles("tech")
#     return render_template('articles.html', articles=articles)
#
#
@main.route('/article/<id>')
def source_article(id):
    source_articles = get_articles(id)
    return render_template('articles_display.html', source_articles=source_articles)
