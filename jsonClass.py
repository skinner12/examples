import json
import os
import warnings
from urllib.request import urlopen


class jSon:
    """ Test Class
        Read jSon File
    """
    def __init__(self):
        print("===========Welcome to jSon Reader===============")
        print("=======Extract Info From jSon Example===========")

    def load1(url, jsonFile):
        if not os.path.exists(jsonFile):
            msg = 'downloading {} to {}'.format(url, jsonFile)
            warnings.warn(msg)
            with urlopen(url) as remote, open(jsonFile, 'wb') as local:
                local.write(remote.read())

        with open(jsonFile) as fp:
            return json.load(fp)

    """feed = load()
    print(sorted(feed['Schedule'].keys()))

    for key, value in sorted(feed['Schedule'].items()):
        print('{:3} {}'.format(len(value), key))

    ''' Legge JSON nella posizione specificata '''
    print('Ultimo NAME: ', feed['Schedule']['speakers'][-1]['name'])"""

