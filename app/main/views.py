from flask import render_template, request
from . import main
from app.request import get_sources


@main.route('/')
def index():
    sources = get_sources()

    return render_template('index.html', sources=sources)




# @main.route('/articles', methods=["POST", "GET"])
# def articles_page():
#     if request.method == 'POST':
#         search = request.form.get("search")
#         articles = NewsRequest.get_articles(search)
#     else:
#         articles = NewsRequest.get_articles("tech")
#     return render_template('articles.html', articles=articles)
#
#
# @main.route('/article/<id>')
# def source_article(id):
#     source_articles = NewsRequest.get_article_by_source(id)
#     source = id
#     return render_template('articles_display.html', source_articles=source_articles, )
