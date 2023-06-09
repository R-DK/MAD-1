import os
from re import template
from flask import Flask
from flask_restful import Resource, Api
from application import config
from application.config import LocalDevelopmentConfig
from application.database import db

app = None
api = None 
def create_app():
    app = Flask(__name__, template_folder='templates')
    if os.getenv('ENV', 'development') == 'production':
        raise Exception("No production development is setup")
    else:
        print('Starting local development')
        app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    app.app_context().push()
    api = Api(app)
    return app, api 

app, api = create_app()

#Import all controllers so they are loaded
from application.controller import *

if __name__=='__main__':
    #Run the flask app
	app.run(host='0.0.0.0', port=8080)