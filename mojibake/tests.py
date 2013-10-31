import unittest

from app import app, db
from app.models import Post, Category

class Tests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['']


if __name__ == '__main__':
