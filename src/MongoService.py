'''
Created on Feb 25, 2013

@author: vaibhavsaini
'''
from LoadTagsPost import DataLoad
from pymongo import Connection
import sys
class MongoService():
    '''
    classdocs
    '''


    def __init__(self, config):
        '''
        Constructor
        '''
        self.config = config
        self.connection = Connection(self.config['host'], self.config['port'])
        self.db = self.connection[self.config['db']]
        self.sqlservice = DataLoad(self.config['sql_config'])

    def loadData(self,start,end,window):
        i = start
        j = i+window
        while j<=end: 
            rows = self.sqlservice.readData(i, j)
            rows = self.getVars(rows)
            print "********", i, j
            i = j
            j += window
            tag_post_answer = self.db.tag_post_map_answer
            tag_post_answer.insert(rows)
        print "returning from loadData"
    
    def getAnswers(self,start,end,window):
        i = start
        j = i+window
        while j<=end: 
            rows = self.sqlservice.loadAnswers(start, end)
            for row in rows:
                print row.acceptedAnswerId
            print "********", i, j
            i = j
            j += window
            #tag_post_map = self.db.tag_post_map
            #tag_post_map.insert(rows)
        print "returning from loadData"

    def getVars(self, rows):
        ret = []
        for row in rows:
            obj = row.__dict__
            obj['_sa_instance_state'] = None
            ret.append(obj)
        return ret

#print "here"
#if __name__ == 'main':
#    print "hi"
dbConfig = { 'host': 'karnali.ics.uci.edu',
                     'user': 'sourcerer',
                     'pass': 'tyl0n4pi',
                     'db': 'stackoverflow'}
config = {'sql_config': dbConfig,
          'host' : 'localhost',
          'port' : 27017,
          'db' : 'stackoverflow'
          }
mservice = MongoService(config)
args = sys.argv
st = sys.argv[1]
en = sys.argv[2]
win = sys.argv[3]
print "loading..."
mservice.getAnswers(int(st),int(en),int(win))
print "loading done.."
