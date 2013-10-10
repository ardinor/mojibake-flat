from flask.ext.script import Command
#from models import Post
#from mojibake.models import Post
#from app import manager

class ManageMetaDB(Command):

    def __init__(self, db, pages, Post):
        self.db = db
        self.pages = pages
        self.Post = Post

    def run(self):
        posts = [page for page in self.pages if 'date' in page.meta]
        for page in posts:
            db_page = self.Post.query.filter_by(title=page.meta['title']).first()
            if db_page is None:
                db_page = self.Post(title=page.meta['title'], path=page.path,
                               date=page.meta['date'],
                               categories=page.meta['category'])
                self.db.session.add(db_page)
                self.db.session.commit()
            else:
                pass
                #check and update if necessary here
        # posts = os.path.join(FLATPAGES_ROOT, 'posts')
        # categories = {}
        # dates = {}
        # for i in os.listdir(posts):
        #     if os.path.splitext(i)[1].lower() == '.md':
        #         #https://github.com/SimonSapin/Flask-FlatPages/blob/master/flask_flatpages/__init__.py
        #         with open(os.path.join(posts, i), 'r') as j:
        #             content = j.read().decode('utf-8')
        #         lines = iter(content.split(u'\n'))
        #         meta = u'\n'.join(itertools.takewhile(unicode.strip, lines))


