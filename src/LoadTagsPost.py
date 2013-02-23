'''
Created on Feb 18, 2013

@author: vaibhavsaini
'''

from Base import *
from DbConnect import DbConnect
from Models import *
from MySQLdb import cursors
import MySQLdb as mdb
import datetime
import sys
class DataLoad():
    
    def __init__(self , config):
        self.dbConfig = config
        #self.con = self.openConnection()
        #self.writeCon = self.openConnection()
        #self.cursor = self.con.cursor(cursors.SSCursor)
        self.languages = ['java', 'python', 'c#', 'c++', 'php', 'c',
                           'ruby', 'ruby-on-rails', 'javascript', 'jquery',
                            'asp.net', 'objective-c','sql', 'xml', 'perl',
                             'cocoa', 'delphi', 'node.js', 
                             'scala', 'visual-c++']
        self.langString = ''
        for language in self.languages:
            self.langString += "1 as "+ language+", "
        self.langString =self.langString[0:len(self.langString)-2]
        self.postsFields = "id, AcceptedAnswerId, ParentId, CreationDate, Score, ViewCount, Body, OwnerUserId, OwnerDisplayName, LastEditorUserId, LastEditorDisplayName, LastEditDate, LastActivityDate, Title, Tags, AnswerCount, CommentCount, FavouriteCount, ClosedDate, CommunityOwnedDate"
        self.fields = "Tag, PostId, AcceptedAnswerId, ParentId, CreationDate, Score, ViewCount, Body, OwnerUserId, OwnerDisplayName, LastEditorUserId, LastEditorDisplayName, LastEditDate, LastActivityDate, Title, Tags, AnswerCount, CommentCount, FavouriteCount, ClosedDate, CommunityOwnedDate"
        self.valStr=""
        for field in self.fields.split(","):
            self.valStr += "'%s',"
        self.valStr = self.valStr[0:len(self.valStr)-2]
        self.dbConnect =DbConnect(self.dbConfig)
        Session, self.engine  = self.dbConnect.openConnection()
        self.session = Session()
        
            
    def loadData(self, fromTable, toTable):
        #rowNum =  self.getTotalRowsInTable(fromTable)
        query = "SELECT "+self.postsFields+" from {0} where posttypeid = 1".format(fromTable)
        num=10
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
    
    def loadData2(self):
        for row in self.session.query(Post).filter(Post.postTypeId==1)[0:10]:
            print row
        print "done"

    def addData(self):
        dummy = Dummy(name="ba", score=12)
        self.session.add(dummy)
        dummy.score=14
        dummy.name='vv'
        self.session.add(dummy)
        self.session.commit()


    def getTotalRowsInTable(self, tableName):
        query = "SELECT count(*) from {0}".format(tableName)
        self.fireQuery(query)
        row = self.cursor.fetchone()
        return row
    
    def fireQuery(self, query, cursor):
        try:
            print "query: ", query
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
            lang = ''
            for tag in tags:
                if tag in self.languages:
                    lang = tag
                    break;
            try:
                if len(lang)>0:
                    self.insert(tags,toTable,lang)
                else:
                    self.insert(tags,toTable)
            except Exception , e:
                print "ERROR: ", sys.exc_info()

    def process(self, row):
        id = row[0]
        tags = row[14]
        print tags
        answer_id = row[2]
        tags = tags.strip() #=strip(tags)
        tags = tags[1:-1]
        tags = tags.split("><")
        rows = []
        for tag in tags:
            tup= (tag,)
            tag_sql = tup+ row
            rows.append(tag_sql)
        return rows

    def insert(self,tags,toTable,lang=None):
        cur = self.writeCon.cursor(cursors.SSCursor)
        if lang is None:
            for tag in tags:
                print 'tag', tag
                pf = "insert into " + toTable + "("+self.fields+") values("+self.valStr +")"
                print 'query prefix', pf
                query= "insert into " + toTable + "("+self.fields+") values("+self.valStr +")"%tag
                self.fireQuery(query, cur)
        else:
            for tag in tags:
                query = "insert into "+ toTable+"("+self.fields+", "  +lang+") values("+self.valStr +",1)"%tag
                self.fireQuery(query, cur)

dbConfig = { 'host': 'karnali.ics.uci.edu',
                         'user': 'sourcerer',
                         'pass': 'tyl0n4pi',
                         'db': 'stackoverflow'}
dataLoad =  DataLoad(dbConfig) # gets the dataLoadObject and opens the connection
#print dataLoad.langString
#print "starting load"
#print len(dataLoad.fields.split(',')), len(dataLoad.valStr.split(',')) 
#Base.metadata.create_all(dataLoad.engine)
dataLoad.loadData2()
#tag = ('java', 7779L, 28154L, None, datetime.datetime(2008, 8, 11, 13, 30, 21), 4L, 894L, "<p>I have read through several reviews on Amazon and some books seem outdated.  I am currently using MyEclipse 6.5 which is using Eclipse 3.3.  I'm interested in hearing from people that have experience learning RCP and what reference material they used to get started.  Thanks in advance. Bruce</p>&#xA;", 791L, None, None, None, None, datetime.datetime(2012, 4, 18, 15, 19, 12), 'I would like a recommendation for a book on E', '<java><eclipse><rcp><myeclipse>', 6L, None, None, None, None)
#query_prefix= "insert into tags_post_flat(Tag, PostId, AcceptedAnswerId, ParentId, CreationDate, Score, ViewCount, Body, OwnerUserId, OwnerDisplayName, LastEditorUserId, LastEditorDisplayName, LastEditDate, LastActivityDate, Title, Tags, AnswerCount, CommentCount, FavouriteCount, ClosedDate, CommunityOwnedDate) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s)"
#query = query_prefix%tag
#print query
##dataLoad.loadData("posts", 'tags_post_flat')
##dataLoad.closeConnection()
#print "done"
