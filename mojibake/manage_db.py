import os
import itertools

from flask.ext.script import Command
#from app import manager

class ManageMetaDB(Command):

    def __init__(self, db, pages):
        self.db = db
        self.pages = pages

    def run(self):
        posts = [page for page in self.pages if 'date' in page.meta]
        print posts
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

