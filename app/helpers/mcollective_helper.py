from riak import RiakClient

def get_hosts(hosts,servers):
  
  results=list()
  riak_reply={}
    
  for server in servers:
    mcodata=RiakClient(host=server).bucket_type('puppet').bucket('nodes')
    
    if hosts is not None: 
        
      for host in hosts:
      #then get specific host
        riak_reply[server] = mcodata.search("facts.fqdn:%s" % host,index='mco_nodes') 
        if riak_reply[server]['docs']:
          results.extend(riak_reply[server]['docs'])
    else: 
      #then get all hosts
      riak_reply[server] = mcodata.get_keys()
      if riak_reply[server]:
        results.extend(riak_reply[server])
        results.sort()
  reply = {'servers':'%s'%servers,'results':results} or None
  return reply

  
