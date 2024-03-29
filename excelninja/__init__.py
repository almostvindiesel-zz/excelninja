#!/usr/bin/env python
# -*- coding: utf-8 -*-
print "Loading " + __file__

import os
from flask import Flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)

# ------------------------------------------------------------------------------------------ Configuration 
if('EXCELNINJA_ENVIRONMENT' in os.environ):
    if os.environ['EXCELNINJA_ENVIRONMENT'] == 'heroku':
        print "-" * 50
        print "set os.environ from Heroku to app.config vars:"
        for key, value in os.environ.iteritems() :
            app.config[key] = value
            print key, value
    elif os.environ['EXCELNINJA_ENVIRONMENT'] == 'local':
        from excelninja import settingslocal
    elif os.environ['EXCELNINJA_ENVIRONMENT'] == 'pythonanywhere':
        from excelninja import settingspa
# ------------------------------------------------------------------------------------------

import excelninja.views