from flask import render_template, abort
from flask_flatpages import pygments_style_defs
from app import app, pages, freezer, db
from models import Post, Tag
from settings import POSTS_PER_PAGE

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
    posts_total = len(sorted_posts)
    return render_template('index.html', pages=sorted_posts[:POSTS_PER_PAGE])

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/archive/')
def archive():
    posts = Post.query.all()
    years = list(set([post.date.year for post in posts]))

    return render_template('archive.html', years=years)

@app.route('/archive/<year>')
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

@app.route('/tags/<name>')
def tag_name(name):
    tag = Tag.query.filter_by(name=name).first()

    if tag:
        return render_template('tag_list.html', tag=tag)
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
@app.route('/posts/<page>')
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

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404
