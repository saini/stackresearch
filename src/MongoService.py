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
            tag_post_answer_new = self.db.tag_post_map_answer_new
            tag_post_answer_new.insert(rows)
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

    def removeRows(self,start, end,window):
        i=start
        j=i+window
        while j <=end:
            print i,j
            rows = self.sqlservice.getDamagedPosts(i,j)
            for row in rows:
                post_id = row.id
                print post_id, row.tags
                self.db.tag_post_map.remove({'post_id':post_id})
            i=j
            j=j+window
    
    def getVars(self, rows):
        ret = []
        for row in rows:
            obj = row.__dict__
            obj['_sa_instance_state'] = None
            ret.append(obj)
        return ret

#print "here"
if __name__ == '__main__':
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
    mservice.removeRows(int(st),int(en),int(win))
    print "loading done.."
