from flask import Blueprint, request, Response, session
import requests
import json
import logging
from app.helpers import mcollective_helper
from app.lib import auth_helper
from app.models.config import Configuration

api_logger = logging.getLogger('verbose')
riak_config = Configuration.configfile('riak.json')

api = Blueprint('api',__name__)

# replace this with configfile defaults
server=riak_config.get('hosts') or 'localhost'
mcollective = riak_config.get('mcollective') or 'enabled'

@api.route("/hosts")
@auth_helper.ldap_protected
def hosts():

  reply = {}
  
  # get request arguments
  hosts=request.args.get('host') or None
  sources=request.args.get('mcollective') or mcollective
  servers=request.args.get('server') or server
  
  if hosts:
    hosts=hosts.split(',')
  servers = servers.split(',')
  
  api_logger.debug("%s calling %s" % (session['username'],request.url_rule.rule))
  
  # get results from sources
  if mcollective=='enabled':
    reply['mcollective'] = mcollective_helper.get_hosts(hosts,servers) or None
    api_logger.debug("mcollective host list retrieved for %s" %session['username'])
    
  return Response(json.dumps(reply), mimetype="application/json")

@api.route("/logout")
def logout():
  session.pop('username', None)
  return Response(json.dumps('logged out'), mimetype="application/json")
