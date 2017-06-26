from debug import *
from zoodb import *
import rpclib

sockname = "/banksvc/sock"
c = rpclib.client_connect(sockname)

def transfer(sender, recipient, zoobars, tokens):
    if not is_valid_user(sender, tokens):
        return
    kwargs = {}
    kwargs['sender'] = sender
    kwargs['recipient'] = recipient
    kwargs['zoobars'] = zoobars
    return c.call('transfer', **kwargs)
    
def balance(username):
    kwargs = {}
    kwargs['username'] = username
    return c.call('balance', **kwargs)
            
def get_log(username):
    kwargs = {}
    kwargs['username'] = username
    return c.call('get_log', **kwargs)

def setup(username):
    kwargs = {}
    kwargs['username'] = username
    return c.call('setup', **kwargs)

def is_valid_user(username, token):
    kwargs = {}
    kwargs['username'] = username
    kwargs['token'] = token
    c2 = rpclib.client_connect("/authsvc/sock")
    return c2.call('check_token', **kwargs)

