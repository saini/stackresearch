'''
Created on Feb 19, 2013

@author: vaibhavsaini
'''

try:
    import MySQLdb as mdb
except ImportError:
    print "Just because you're using this wrapper, doesn't mean you can escape"
    print "from installing MySQLdb. This module depends on it."

class mysql:
    def __init__(self, host, username, password, database):
        self.host = host
        self.db = mdb.connect(host=host, user=username, passwd=password, db=database)
        self.cursor = self.db.cursor()
    
    def get_array(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        results = []
        for record in result:
            results.append(record)
        return results
    
    def query(self, sql):
        return self.cursor.execute(sql)
    
    def execute(self, sql):
        self.query(sql)
        return self
    
    def insert_id(self):
        return self.db.insert_id()

    def get_row(self, sql):
        query = self.query(sql)
        result = self.cursor.fetchall()
        
        try:
            return result[0]
        except:
            return False
    
    def get_one(self, sql, offset=0):
        row = self.get_row(sql)
        
        try:
            return row[offset]
        except:
            return False
    
#    def clean(self, string):
#        string = str(string)
#        return mdb.