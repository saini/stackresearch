'''
Created on Feb 20, 2013

@author: vaibhavsaini
'''
from sqlalchemy.engine import *
import sqlalchemy
from sqlalchemy.orm.session import sessionmaker
class DbConnect(object):
    '''
    classdocs
    '''


    def __init__(self, config):
        '''
        Constructor
        '''
        self.config = config
    
    def openConnection(self):
        connectionString = 'mysql+mysqldb://{0}:{1}@{2}/{3}?charset=utf8'.format(self.config['user'],
                                                                    self.config['pass'],
                                                                    self.config['host'],
                                                                    self.config['db'])
        engine = create_engine(connectionString,echo=True)
        Session = sessionmaker(engine)
        return Session,engine
    
        #print engine.execute('select 1').scalar()

dbConfig = { 'host': 'karnali.ics.uci.edu',
                         'user': 'sourcerer',
                         'pass': 'tyl0n4pi',
                         'db': 'stackoverflow'}
dbcon = DbConnect(dbConfig)
dbcon.openConnection()