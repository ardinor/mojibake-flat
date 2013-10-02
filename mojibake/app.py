# -*- coding: utf-8 -*-

from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flask.ext.assets import Environment, Bundle

from moment_js import moment_js

app = Flask(__name__)
app.config.from_pyfile('settings.py')
pages = FlatPages(app)
freezer = Freezer(app)

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
