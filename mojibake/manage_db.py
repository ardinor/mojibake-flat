from flask.ext.script import Command
#from models import Post
#from mojibake.models import Post
#from app import manager

class ManageMetaDB(Command):

    def __init__(self, db, pages, Post, Category):
        self.db = db
        self.pages = pages
        self.Post = Post
        self.Category = Category

    def run(self):
        posts = [page for page in self.pages if 'date' in page.meta]
        for page in posts:
            print page.path
            db_page = self.Post.query.filter_by(path=page.path).first()
            if db_page is None:
                print page.meta['title']
                print page.meta['date']
                print page.meta['category']
                categories = []
                if isinstance(page.meta['category'], list):
                    for i in page.meta['category']:
                        db_cat = self.Category.query.filter_by(name=i).first()
                        if db_cat is None:
                            db_cat = self.Category(i)
                            self.db.session.add(db_cat)
                            self.db.session.commit()
                            categories.append(db_cat)
                        else:
                            categories.append(db_cat)
                else:
                    db_cat = self.Category.query.filter_by(name=page.meta['category']).first()
                    if db_cat is None:
                        db_cat=self.Category(page.meta['category'])
                        self.db.session.add(db_cat)
                        self.db.session.commit()
                        categories.append(db_cat)
                    else:
                        categories.append(db_cat)
                db_page = self.Post(title=page.meta['title'], path=page.path,
                               date=page.meta['date'],
                               categories=categories)
                self.db.session.add(db_page)
                self.db.session.commit()
            else:
                changed = False
                if db_page.title != page.meta['title']:
                    db_page.title = page.meta['title']
                    changed = True
                if db_page.date != page.meta['date']:
                    db_page.date = page.meta['date']
                    changed = True
                if db_page.categories !=  page.meta['category']:
                    db_page.categories = page.meta['category']
                    changed = True
                if changed:
                    self.db.session.commit()



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


