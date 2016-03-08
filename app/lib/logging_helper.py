import logging
import logging.config

logger = logging.getLogger(__name__)

# load config from file 

# logging.config.fileConfig('logging.ini', disable_existing_loggers=False)

# or, for dictConfig

global_logger = logging.getLogger("global_logger")

logging.config.dictConfig({
  'version': 1,              
  'disable_existing_loggers': False,  # this fixes the problem

  'formatters': {
    'standard': {
      'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
      },
    'my_verbose_formatter': {
      'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
      },
    },
  'handlers': {
    'default': {
      'level':'DEBUG',    
      'class':'logging.StreamHandler',
      'formatter': 'standard'
      },  
    'my_verbose_handler': {
      'level':'DEBUG',    
      'class':'logging.StreamHandler',
      'formatter': 'my_verbose_formatter'
      },  

    },
  'loggers': {
    'mylogger': {                  
      'handlers': ['default'],        
      'level': 'DEBUG',  
      'propagate': True  
      },
    'main': {                  
      'handlers': ['default'],        
      'level': 'DEBUG',  
      'propagate': True  
      },
    'verbose': {                  
      'handlers': ['my_verbose_handler'],        
      'level': 'DEBUG',  
      'propagate': True  
    }        
  }
})