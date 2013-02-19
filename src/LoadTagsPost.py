'''
Created on Feb 18, 2013

@author: vaibhavsaini
'''

import MySQLdb as mdb
import sys

class DataLoad():
    
    def __init__(self , config):
        self.dbConfig = config
        self.con = self.openConnection()
        self.cursor = self.con.cursor()
##db = _mysql.connect('karnali.ics.uci.edu', 'sourcerer', 'tyl0n4pi', 'stackoverflow')
#db.query("""SELECT id, tags, acceptedanswersid from posts where posttypeid = 1""")
#r = db.use_result() 
#rows = r.fetchall()
#query = """SELECT id, tags, acceptedanswersid from posts where posttypeid = 1"""
    def loadData(self, fromTable, toTable):
        #rowNum =  self.getTotalRowsInTable(fromTable)
        query = "SELECT * from {0}".format(fromTable)
        num=1000
        self.fireQuery(query)
        while True:
            rows = self.cursor.fetchmany(num)
            if len(rows)==0:
                break
            else:
                self.inserRows(rows, toTable)

    def getTotalRowsInTable(self, tableName):
        query = "SELECT count(*) from {0}".format(tableName)
        self.fireQuery(query)
        row = self.cursor.fetchone()
        return row
    
    def fireQuery(self, query):
        try:
            self.cursor.execute(query)
        except Exception, e:
            print "Error: "+ e.message()
                
    def openConnection(self):
        print "inside openConnection"
        try:
            con = mdb.connect(self.dbConfig['host'], 
                                  self.dbConfig['user'], 
                                  self.dbConfig['pass'], 
                                  self.dbConfig['db']);
            return con
        except Exception, e:
            print "Error :"+ e.message()
            sys.exit(1)
    
    def closeConnection(self):
        try:
            if self.con:
                self.con.close()
        except Exception, e:
            print "Error %d: %s" % (e.args[0], e.args[1])

    def insertRows(self, rows, toTable):
        for row in rows:
            tags = self.process(row)
            self.insert(tags)

    def process(self, row):
        id = row[0]
        tags = row[1]
        answer_id = row[3]
        tags = tags.strip() #strip(tags)
        tags = tags[1:-1]
        tags = tags.split("><")
        rows = []
        for tag in tags:
            tag_sql = ("'%s'" % (id), "'%s'" % (tag))
            rows.append(tag_sql)
        return rows
        
    
    def insert(self,tags):
        sql = """ insert into tags_post_id values(NULL,%s,%s,%) """
        self.cursor.execute(sql, tags)
    
    #for row in rows:
    #    try:
    #        tags = process(row)
    #        insert(tags)
    #    except Exception:
    #        print ("some error in %s", row)


rows = None
dbConfig = { 'host': 'karnali.ics.uci.edu',
                         'user': 'sourcerer',
                         'pass': 'tyl0n4pi',
                         'db': 'stackoverflow'}
dataLoad =  DataLoad(dbConfig) # gets the dataLoadObject and opens the connection
dataLoad.loadData("posts", 'toTable')
#

#dbConfig = { 'host': 'karnali.ics.uci.edu',
#            'user': 'sourcerer',
#            'pass': 'tyl0n4pi',
#            'db': 'stackoverflow'}
#
#try:
#    con = mdb.connect(dbConfig['host'], 
#                      dbConfig['user'], 
#                      dbConfig['pass'], 
#                      dbConfig['db']);
#    cur = con.cursor()
#    print type(cur)
#    query = """SELECT id, tags, AcceptedAnswerId from posts where id > 1 and id <100 """
#    cur.execute(query)
#    data = cur.fetchone()
#    print(data)
#except Exception, e:
#    print "Error %d: %s" % (e.args[0], e.args[1])
#    sys.exit(1)
#finally:    
#    if con:    
#        con.close()