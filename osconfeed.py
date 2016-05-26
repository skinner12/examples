from jsonClass import jSon

class osconfeed(jSon):

    def __init__(self):
        print("=======Extract Info From jSon OsconFeed===========")

    def ultimeName(self, url, json):
        #print('Last NAME: ', jSon.load(url, json)['Schedule']['speakers'][-1]['name'])
        return jSon.load1(url, json)['Schedule']['speakers'][-1]['name']

    def getCount(self, url, json):
        for key, value in sorted(jSon.load1(url, json)['Schedule'].items()):
            print('{:3} {}'.format(len(value), key))
