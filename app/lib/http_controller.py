# import api version 1
from app.controllers.v1.api import api as api_v1
from app.lib import logging_helper
import logging
from app.lib import random_helper as random
from app.models.config import Configuration
from flask import Flask, session

app_logger = logging.getLogger("verbose")

app = Flask(__name__)
# use api_v1 if the url prefix is /api/v1
app.register_blueprint(api_v1, url_prefix='/api/v1')
   
def run():
  app.config.from_object(Configuration())
  app.secret_key = random.get_secret_key()  
  app_logger.debug("application started through commandline")
  app.run()

if __name__=="__main__":
  app.config.from_object(Configuration())
  app.secret_key = random.get_secret_key()
  app_logger.debug("application started")
  app.run()