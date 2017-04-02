import ConfigParser
import os


def read_config():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    config = ConfigParser.ConfigParser()
    configfile = os.path.join(ROOT_DIR, '..', 'app.ini')
    config.read(configfile)

    return config
