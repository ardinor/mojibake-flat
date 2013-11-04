from flask import render_template, abort
from flask_flatpages import pygments_style_defs
from app import app, pages, freezer, db
from models import Post, Category
from settings import APP_DIR

import os
import ast

# From https://github.com/killtheyak/killtheyak.github.com/blob/master/killtheyak/views.py
@freezer.register_generator
def pages_url_generator():
    all_pages = [p for p in pages]
    for page in all_pages:
        yield 'page', {'path': page.path}


@app.route('/')
def home():
    posts = [page for page in pages if 'date' in page.meta]
    # Sort pages by date
    sorted_posts = sorted(posts, reverse=True,
        key=lambda page: page.meta['date'])
    return render_template('index.html', pages=sorted_posts[:10])

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/archive/')
def archive():
    return render_template('archive.html')

@app.route('/categories/')
def categories():
    categories = Category.query.all()

    return render_template('categories.html', categories=categories)

@app.route('/categories/<name>')
def category_name(name):
    category = Category.query.filter_by(name=name).first()

    if category:
        return render_template('category_list.html', category=category)
    else:
        abort(404)

@app.route('/posts/')
def posts():
    posts = [page for page in pages if 'date' in page.meta]
    # Sort pages by date
    sorted_posts = sorted(posts, reverse=True,
        key=lambda page: page.meta['date'])
    return render_template('posts.html', pages=sorted_posts[:10])

@app.route('/<path:path>/')
def page(path):
    # `path` is the filename of a page, without the file extension
    # e.g. "first-post"
    page = pages.get_or_404(path)
    template = page.meta.get('template', 'post.html')
    return render_template(template, page=page)

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('autumn'), 200, {'Content-Type': 'text/css'}

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404
