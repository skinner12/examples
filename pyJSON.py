import json
import os
import warnings
from urllib.request import urlopen


class osconFeed:
    """ Test Class
    """

    URL = 'http://www.oreilly.com/pub/sc/osconfeed'
    JSON = 'data/osconfeed.json'


    def __init__(self):
        print('Inizio CLASSE')


    def load(self):
        if not os.path.exists(self.JSON):
            msg = 'downloading {} to {}'.format(self.URL, self.JSON)
            warnings.warn(msg)
            with urlopen(self.URL) as remote, open(self.JSON, 'wb') as local:
                local.write(remote.read())

        with open(self.JSON) as fp:
            return json.load(fp)

    """feed = load()
    print(sorted(feed['Schedule'].keys()))

    for key, value in sorted(feed['Schedule'].items()):
        print('{:3} {}'.format(len(value), key))

    ''' Legge JSON nella posizione specificata '''
    print('Ultimo NAME: ', feed['Schedule']['speakers'][-1]['name'])"""


    def ultimeName(self):
        print('Ultimo NAME: ', self.load()['Schedule']['speakers'][-1]['name'])
        return self.load()['Schedule']['speakers'][-1]['name']


a = osconFeed()
feed = osconFeed.ultimeName(a)


