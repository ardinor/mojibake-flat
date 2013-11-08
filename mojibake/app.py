# -*- coding: utf-8 -*-

from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flask.ext.assets import Environment, Bundle
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from moment_js import moment_js
from manage_db import ManageMetaDB

app = Flask(__name__)
app.config.from_pyfile('settings.py')
pages = FlatPages(app)
freezer = Freezer(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from mojibake import models

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('manage_db', ManageMetaDB(db, pages, models.Post, models.Tag))

app.jinja_env.globals['moment_js'] = moment_js

assets = Environment(app)
app.config['ASSETS_DEBUG'] = True

css = Bundle('css/bootstrap.min.css',
             'css/mojibake.css')
assets.register('css_all', css)

js = Bundle('js/jquery-2.0.3.min.js',
            'js/bootstrap.min.js',
            'js/mojibake.js',
            filters='rjsmin', output='gen/packed.js')
assets.register('js_all', js)

#Moment needs to be in the document head apparently
moment = Bundle('js/moment.min.js')
assets.register('js_moment', moment)
