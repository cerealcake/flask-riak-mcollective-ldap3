import click
import json
import logging
from app.helpers import mcollective_helper
from app.lib import logging_helper

cli_log = logging.getLogger('main')

@click.command()
@click.option('--hosts', is_flag=True, default=False, help="")
@click.option('--host', default=None, help="hostname to query")
@click.option('--server', default='riaknode-1.example.net,riaknode-2.example.net', help="riak kv server")
@click.option('--mcollective_disable', is_flag=True, default=True, help="toggle to not include mcollective data in searches")
def cli(hosts,host,server,mcollective_disable):
  reply={}
  if hosts or (host is not None):
    try:
      reply['hosts']=get_hosts(host,server,source)
    except:
      cli_log.debug("unable to get hosts from %s" % server)
  click.echo(json.dumps(reply))

def get_hosts(hosts,servers,mcollective_disable):

  if hosts:
    hosts=hosts.split(',')
  servers = servers.split(',')
  
  reply = {}
  if not mcollective_disable:
    reply['mcollective']=mcollective_helper.get_hosts(hosts,servers) or None
  reply['hosts']=hosts
  return reply
    
if __name__=="__main__":
  cli()
        
    
