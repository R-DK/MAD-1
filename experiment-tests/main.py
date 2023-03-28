import os
from flask import Flask
from application import config
from application.config import LocalDevelopmentConfig, TestingConfig
from application.database import db
from flask_security import Security, SQLAlchemySessionUserDatastore,  SQLAlchemyUserDatastore
from application.models import User, Role 
import logging
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = None

def create_app():
    app = Flask(__name__, template_folder="templates")
    if os.getenv('ENV', "development") == "production":
      app.logger.info("Currently no production config is setup.")
      raise Exception("Currently no production config is setup.")
    elif os.getenv('ENV', "development") == "testing":
      app.logger.info("Start testing")
      print('Start testing')
      app.config.from_object(TestingConfig)
    else:
      app.logger.info("Staring Local Development.")
      print("Staring Local Development")
      app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    app.app_context().push()
    user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
    security = Security(app, user_datastore)
    app.logger.info("App setup complete")
    return app

app = create_app()

# Import all the controllers so they are loaded
from application.controllers import *

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

if __name__ == '__main__':
  # Run the Flask app
  app.run(host='0.0.0.0',port=8080)