import os
from re import template
from flask import Flask
from application import config
from application.config import LocalDevelopmentConfig
from application.database import db

# current_dir = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(current_dir, "testdb.sqlite3")

# db = SQLAlchemy()
# db.init_app(app)
# app.app_context().push()

app = None 

def create_app():
    app = Flask(__name__, template_folder=templates)
    


if __name__=='__main__':
	app.run()