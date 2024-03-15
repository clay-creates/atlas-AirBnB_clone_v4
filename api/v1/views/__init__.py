#!/usr/bin/python3
""" Set up Flask blueprint """
from flask import Blueprint


# Create blueprint instance and set url prefix
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


# Wildcard import to prevent circular import
from api.v1.views.index import *