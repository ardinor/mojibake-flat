# -*- coding: utf-8 -*-

'''Entry point to all things to avoid circular imports.'''
from app import app, db, freezer, pages, manager, models
from views import *
