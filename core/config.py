from configparser import ConfigParser

# Configuration file
def get_config():
    config = ConfigParser()
    config.read('config.ini')

    return config._sections