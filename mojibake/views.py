from urlparse import urljoin
from flask import render_template, abort, request
from flask_flatpages import pygments_style_defs
from werkzeug.contrib.atom import AtomFeed

#
import datetime

from app import app, pages, freezer, db
from models import Post, Tag, Category
from settings import POSTS_PER_PAGE

def make_external(url):
    return urljoin(request.url_root, url)

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
    return render_template('index.html', pages=sorted_posts[:POSTS_PER_PAGE])

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/archive/')
def archive():
    posts = Post.query.all()
    years = list(set([post.date.year for post in posts]))

    return render_template('archive.html', years=years)

@app.route('/archive/<year>/')
def archive_year(year):
    year_posts = Post.query.filter("strftime('%Y', date) = :year"). \
            params(year=year).order_by('-date').all()

    if year_posts:
        return render_template('archive_year.html', year=year,
            posts=year_posts)
    else:
        abort(404)

@app.route('/tags/')
def tags():
    tags = Tag.query.order_by('name').all()

    return render_template('tags.html', tags=tags)

@app.route('/bans/')
def bans():

    #just fill it with filler information, this template is made elsewhere

    breakin_attempts = {datetime.datetime(2013, 12, 2, 20, 31, 46): ('95.183.198.46', 'nagios'),
                        datetime.datetime(2013, 12, 2, 20, 56, 46): ('95.183.198.46', 'postgres'),
                        datetime.datetime(2013, 12, 2, 21, 04, 46): ('95.183.198.46', 'igor'),
                        datetime.datetime(2013, 12, 2, 22, 31, 46): ('211.141.113.237', 'ftpuser'),
                        datetime.datetime(2013, 12, 2, 22, 48, 46): ('195.60.215.30', 'oracle')
                        }

    bans = {datetime.datetime(2013, 12, 2, 21, 05, 46): '95.183.198.46',
            datetime.datetime(2013, 12, 2, 21, 10, 46): '211.141.113.237',
            datetime.datetime(2013, 12, 2, 22, 50, 46): '195.60.215.30'}

    ips = {'95.183.198.46': {'country':'Test', 'region': 'Test Region'},
           '211.141.113.237': {'country':'Test', 'region': 'Test Region'},
           '195.60.215.30': {'country':'Test', 'region': 'Test Region'}}

    displayed_time = 'CET'
    time_offset = '+1'

    last_month = datetime.datetime.now().replace(day=1) - datetime.timedelta(days=1)

    return render_template('bans.html', displayed_time=displayed_time,
        time_offset=time_offset, last_month=last_month,
        breakin_attempts=breakin_attempts,
        bans=bans, ips=ips)

@app.route('/tags/<name>/')
def tag_name(name):
    tag = Tag.query.filter_by(name=name).first()

    if tag:
        return render_template('tag_list.html', tag=tag)
    else:
        abort(404)

@app.route('/categories/')
def categories():
    categories = Category.query.order_by('name').all()

    return render_template('categories.html', categories=categories)

@app.route('/categories/<name>/')
def category(name):
    category = Category.query.filter_by(name=name).first()

    if category:
        return render_template('category.html', category=category)
    else:
        abort(404)

#@app.route('/posts/')
#def posts():
    #posts = [page for page in pages if 'date' in page.meta]
    # Sort pages by date
    #sorted_posts = sorted(posts, reverse=True,
    #    key=lambda page: page.meta['date'])
    #return render_template('posts.html', pages=sorted_posts[:POSTS_PER_PAGE])

@app.route('/posts/')
@app.route('/posts/p/<page>/')
def posts(page=1):
    #maybe we should parse the body into the DB too....
    #this is kind of messy
    posts = Post.query.order_by(Post.date.desc()).paginate(int(page), POSTS_PER_PAGE, False)
    found_pages = []
    for i in posts.items:
        found_pages.append(pages.get(i.path))
    return render_template('posts.html', pages=found_pages,
        pagination_item=posts)


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

@app.route('/recent.atom')
def recent_feed():
    feed = AtomFeed('Recent Articles',
                    feed_url=request.url, url=request.url_root)
    posts = [page for page in pages if 'date' in page.meta]
    sorted_posts = sorted(posts, reverse=True,
        key=lambda page: page.meta['date'])[:10]
    for post in sorted_posts:
        feed.add(post.meta['title'], unicode(post.body[:500] + '\n\n....'),
                 content_type='html',
                 author='Jordan Moeser',
                 url=make_external(post.path),
                 updated=page.meta['date'])
    return feed.get_response(), 200, {'Content-Type': 'application/atom+xml; charset=utf-8'}


@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404
