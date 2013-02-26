'''
Created on Feb 24, 2013

@author: vaibhavsaini
'''
from DbConnect import *
from Models import *
from sets import Set

class StackService():
    '''
    classdocs
    '''


    def __init__(self,config):
        '''
        Constructor
        '''
        self.dbConfig = config
        self.langs = ['java', 'python', 'cSharp', 'cPP', 'php', 'c',
                           'ruby', 'ruby_on_rails', 'javascript', 'jquery',
                            'asp_dot_net', 'objective_c','sql', 'xml', 'perl',
                             'cocoa', 'delphi', 'node_dot_js', 
                             'scala', 'visual_cPP']
        self.languages = ['java', 'python']
        self.dbConnect =DbConnect(self.dbConfig)
        Session, self.engine  = self.dbConnect.openConnection()
        self.session = Session()
    
    def getCommonTagsAccrossLangs(self):
        commonTags = Set()
        for lang in self.languages:
            tags = self.getTagsOfLanguage(lang)
            print len(tags)
            commonTags = commonTags.intersection(tags)
        return commonTags

    def getTagsOfLanguage(self, lang):
        filterString = "Tag_Post_Map."+ lang
        returnSet = Set()
        i=0;
        window = 20000
        j=i+window
        count = i
        keepLoading = True
        while keepLoading:
            keepLoading=False
            for row in self.session.query(Tag_Post_Map).filter(eval(filterString)==True)[i:j]:
                keepLoading=True
                returnSet.add(row)
                count +=1
            i=j
            j=j+window
        print "done", count
        return returnSet
if __name__ == 'main':
    dbConfig = { 'host': 'karnali.ics.uci.edu',
                             'user': 'sourcerer',
                             'pass': 'tyl0n4pi',
                             'db': 'stackoverflow'}
    print 'starting..'
    stackService = StackService(dbConfig)
    s = stackService.getCommonTagsAccrossLangs()
    print '*'*20
    tags = ''
    for row in s:
        tags += row.tag + ', '
    print tags
    print 'done'