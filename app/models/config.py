import os
import sys
import logging
import json

config_logger = logging.getLogger("main")

class Configuration():

  @property
  def DEBUG(self):
    if "WINGDB_ACTIVE" in os.environ:
      return False
    else:
      return True

  @property    
  def TESTING(self):
    return False

  @property
  def DATABASE_URI(self):
    if "WINGDB_ACTIVE" in os.environ:
      return False
    else:
      return True

  @classmethod
  def configfile(self,config_filename="ldap.json"):
    try:
      config_logger.debug("retrieving %s configuration"% config_filename)
      with open(self.config_path('%s'%config_filename), "r") as f:
        x = f.read()
      if config_filename.endswith("json"):
        config=json.loads(x)
      else:
        auth_logger.error("extension unknown")
      return config
    except:
      config_logger.error("failed to retrieve %s configuration"%config_filename)

  @staticmethod
  def config_path(config_name):
    try:
      if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
      elif __file__:
        application_path = os.path.dirname(__file__)

      confpath = application_path + '/..' +'/config/' + config_name
      return confpath
    except:
      config_logger.error("failed to get config path")
