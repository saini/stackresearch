'''
Created on Feb 18, 2013

@author: vaibhavsaini
'''

from MySQLdb import cursors
import MySQLdb as mdb
import sys

class DataLoad():
    
    def __init__(self , config):
        self.dbConfig = config
        self.con = self.openConnection()
        self.writeCon = self.openConnection()
        self.cursor = self.con.cursor(cursors.SSCursor)
    def loadData(self, fromTable, toTable):
        #rowNum =  self.getTotalRowsInTable(fromTable)
        query = "SELECT id, tags, acceptedanswerid from {0} where posttypeid = 1".format(fromTable)
        num=1000
        print "firing query"
        self.fireQuery(query, self.cursor)
        print "query fired"
        while True:
            rows = self.cursor.fetchmany(num)
            if rows is None:
                break
            else:
                self.insertRows(rows, toTable)
                self.writeCon.commit()

    def getTotalRowsInTable(self, tableName):
        query = "SELECT count(*) from {0}".format(tableName)
        self.fireQuery(query)
        row = self.cursor.fetchone()
        return row
    
    def fireQuery(self, query, cursor):
        try:
            cursor.execute(query)
        except Exception, e:
            self.writeToFile("FAILED:" + query)
            print "Error: " , sys.exc_info()
                
    def openConnection(self):
        try:
            con = mdb.connect(self.dbConfig['host'], 
                                  self.dbConfig['user'], 
                                  self.dbConfig['pass'], 
                                  self.dbConfig['db']);
            return con
        except Exception, e:
            print "Error :", sys.exc_info()
            sys.exit(1)
    def writeToFile(self, text):
        try:
            file = open("errorlog.txt",'a')
            file.write(text+'\n')
        finally:
            file.close()
        
    def closeConnection(self):
        try:
            if self.con:
                self.con.close()
            if self.writeCon:
                self.writeCon.close()
        except Exception, e:
            print "Error ", sys.exc_info()

    def insertRows(self, rows, toTable):
        for row in rows:
            tags = self.process(row)
            try:
                self.insert(tags,toTable)
            except Exception , e:
                print "ERROR: ", sys.exc_info()

    def process(self, row):
        id = row[0]
        tags = row[1]
        answer_id = row[2]
        tags = tags.strip() #=strip(tags)
        tags = tags[1:-1]
        tags = tags.split("><")
        rows = []
        for tag in tags:
            tag_sql = ("%s" % (tag),"%s" % (id))
            rows.append(tag_sql)
        return rows
        
    
    def insert(self,tags,toTable):
        
        cur = self.writeCon.cursor(cursors.SSCursor)
        for tag in tags:
            query= "insert into " + toTable + "(tags, postid) values('%s','%s')"%(tag[0],tag[1])
            
            self.fireQuery(query, cur)
            

dbConfig = { 'host': 'karnali.ics.uci.edu',
                         'user': 'sourcerer',
                         'pass': 'tyl0n4pi',
                         'db': 'stackoverflow'}
dataLoad =  DataLoad(dbConfig) # gets the dataLoadObject and opens the connection
print "starting load"
dataLoad.loadData("posts", 'tags_post_id')
dataLoad.closeConnection()
print "done"
