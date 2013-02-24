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
        i=0;
        window = 1000
        j=i+window
        count = 0
        keepLoading = True
        while keepLoading:
            #print "INDEXS ARE ",i, j
            keepLoading=False
            for row in self.session.query(Post).filter(Post.postTypeId==1)[i:j]:
                keepLoading=True
                self.insertRow(row)
                count +=1
            i=j
            j=j+window
        print "done", count

    def insertRow(self, row):
        tags = self.processRow(row) # clean tags.
        lang = ''
        for tag in tags:
            if tag in self.languages:
                lang = tag
                if lang.lower()== 'c#':
                    lang = 'cSharp'
                elif lang.lower()=='c++':
                    lang = 'cPP'
                elif lang.lower() == 'ruby-on-rails':
                    lang = 'ruby_on_rails'
                elif lang.lower() == 'asp.net':
                    lang = 'asp_dot_net'
                elif lang.lower() == 'objective-c':
                    lang = 'objective_c'
                elif lang.lower() == 'node.js':
                    lang = 'node_dot_js'
                elif lang.lower() == 'visual-c++':
                    lang = 'visual_cPP'
                break;
        try:
            for tag in tags:
                self.addTagPost(row, lang=lang, tag=tag)
            self.session.commit()
        except Exception , e:
            print "ERROR: ", sys.exc_info()
            self.writeToFile(sys.exc_info())


    def addTagPost(self,row,lang=None,tag=None):
        vars = row.getVars()
        tpm = Tag_Post_Map()
        print type(tpm), tpm
        for field in vars:
            if field=='_sa_instance_state':
                pass
            elif field == 'id':
                setattr(tpm,'post_id', vars[field])
            else:
                setattr(tpm, field, vars[field])
        tpm.tag = tag
        if lang is not None:
            setattr(tpm, lang, True)
        self.session.add(tpm)

    def processRow(self, row):
        tags = row.tags
        print tags
        tags = tags.strip() #=strip(tags)
        tags = tags[1:-1]
        tags = tags.split("><")
        return tags
    
    def addData(self):
        dummy = Dummy(name="ba", score=12)
        self.session.add(dummy)
        dummy.score=14
        dummy.name='vv'
        self.session.add(dummy)
        self.session.commit()

    def writeToFile(self, text):
        try:
            file = open("errorlog.txt",'a')
            file.write(text+'\n')
        finally:
            file.close()
dbConfig = { 'host': 'karnali.ics.uci.edu',
                         'user': 'sourcerer',
                         'pass': 'tyl0n4pi',
                         'db': 'stackoverflow'}
dataLoad =  DataLoad(dbConfig) # gets the dataLoadObject and opens the connection
dataLoad.loadData2()
