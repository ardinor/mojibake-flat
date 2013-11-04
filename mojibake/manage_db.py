import collections
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
            db_page = self.Post.query.filter_by(path=page.path).first()
            if db_page is None:
                categories = []
                split_cat = page.meta['category'].split(', ')
                if isinstance(split_cat, list):
                    for i in split_cat:
                        db_cat = self.Category.query.filter_by(name=i).first()
                        if db_cat is None:
                            db_cat = self.Category(name=i)
                            self.db.session.add(db_cat)
                            self.db.session.commit()
                            categories.append(db_cat)
                        else:
                            categories.append(db_cat)
                # else:
                #     db_cat = self.Category.query.filter_by(name=page.meta['category']).first()
                #     if db_cat is None:
                #         db_cat = self.Category(name=page.meta['category'])
                #         self.db.session.add(db_cat)
                #         self.db.session.commit()
                #         categories.append(db_cat)
                #     else:
                #         categories.append(db_cat)
                db_page = self.Post(title=page.meta['title'], path=page.path,
                               date=page.meta['date'],
                               categories=categories)
                self.db.session.add(db_page)
                self.db.session.commit()
            else:
                changed = False
                split_cat = page.meta['category'].split(', ')
                if db_page.title != page.meta['title']:
                    db_page.title = page.meta['title']
                    changed = True
                if db_page.date != page.meta['date']:
                    db_page.date = page.meta['date']
                    changed = True
                db_categories = []
                for i in db_page.categories:
                    db_categories.append(i.name)
                counter = collections.Counter(split_cat)
                counter.subtract(db_categories)
                if list(counter.elements()):
                    categories = []
                    for i in list(counter.elements()):
                        db_cat = self.Category.query.filter_by(name=i).first()
                        if db_cat is None:
                            db_cat = self.Category(name=i)
                            self.db.session.add(db_cat)
                            self.db.session.commit()
                        categories.append(db_cat)
                    if categories:
                        changed = True
                        db_page.categories = categories

                if changed:
                    self.db.session.commit()

        categories = self.Category.query.all()
        for i in categories:
            if i.posts.count() == 0:
                self.db.session.delete(i)
                self.db.session.commit()

