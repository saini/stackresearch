'''
Created on Mar 2, 2013

@author: vaibhavsaini
'''
import os

class FilePart():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.rows = 10338371
        self.outFileName = "posts_part_"
        self.xmlHeader = """<?xml version="1.0" encoding="utf-8"?>"""
        self.posts_begin = "<posts>"
        self.posts_end = "</posts>"
        #self.initializeFiles()
        
    def cleanFiles(self):
        print 'removing files'
        filelist= [f for f in os.listdir(".") if f.endswith(".xml")]
        for f in filelist:
            print 'removing file', f
            os.remove(f)
        
    def initializeFiles(self):
        print 'initialising files'
        for i in range(2,12):
            self.writeToFile(self.outFileName+str(i)+".xml", self.xmlHeader)
            self.writeToFile(self.outFileName+str(i)+".xml", self.posts_begin)
        print 'initialising done'

    def addClosures(self):
        for i in range(1,11):
            self.writeToFile(self.outFileName+str(i)+".xml", self.posts_end)

    def partFile(self, filename):
        f = open(filename)
        count=0
        for line in f:
            if count < 100000:
                self.writeToFile(self.outFileName+'1.xml',line)
            elif count <200000:
                self.writeToFile(self.outFileName+'2.xml',line)
            elif count < 3000000:
                self.writeToFile(self.outFileName+'3.xml',line)
            elif count < 4000000:
                self.writeToFile(self.outFileName+'4.xml',line)
            elif count < 5000000:
                self.writeToFile(self.outFileName+'5.xml',line)
            elif count < 6000000:
                self.writeToFile(self.outFileName+'6.xml',line)
            elif count < 7000000:
                self.writeToFile(self.outFileName+'7.xml',line)
            elif count < 8000000:
                self.writeToFile(self.outFileName+'8.xml',line)
            elif count < 9000000:
                self.writeToFile(self.outFileName+'9.xml',line)
            elif count < 10000000:
                self.writeToFile(self.outFileName+'10.xml',line)
            else:
                self.writeToFile(self.outFileName+'11.xml',line)
            
            count +=1
    
    def writeToFile(self, filename,text):
        try:
            file = open(filename,'a')
            file.write(text)
            file.write('\n')
        finally:
            file.close()

if __name__=="__main__":
    print ("starting..")
    fp = FilePart()
    fp.cleanFiles()
    fp.initializeFiles()
    filename = "/Users/vaibhavsaini/Documents/stackoverflow research/unzip-001/stackoverflow.com.7z/posts.xml"
    print "parting files.."
    fp.partFile(filename)
    print "parting files done, adding end tags"
    fp.addClosures()
    print "end tags added"
    print ("done")