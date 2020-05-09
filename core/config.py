from configparser import ConfigParser
from getpass import getpass
from os.path import exists

# Configuration file
def init_config():
    config = ConfigParser()
    config.add_section('connection')
    fields = ['host', 'port', 'sid', 'user', 'password']
    for field in fields:
        config['connection'][field] = ''
    with open('config.ini', 'w+') as configfile:
        config.write(configfile)

    

def get_config():
    config = ConfigParser()
    config.read('config.ini')

    return config._sections

def set_config(section, param, value):
    config = ConfigParser()
    config.read("config.ini")
    config.set(section, param, value)
    with open('config.ini', 'w+') as configfile:
        config.write(configfile)

def modify_config(index):
    config = get_config()['connection']
    values = {i: k for i, k in zip(range(1, len(config) + 1), config.keys())}

    if values[index] == 'password':
        value = getpass('\nInput new password > ')
    else:
        value = input(f'\nInput new value for {values[index]} > ')
    set_config('connection', values[index], value)

if not exists('config.ini'):
    init_config()