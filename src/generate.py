import pymongo
from pymongo import MongoClient
import glob,os
class result: 
	tag = ""
	AcceptedAnswerCount = 0
	QuestionCount = 0

class tag_aac_qc_ratio: 
	tagfile = "tag_aac_qc_ratio.csv"
	def process(self, post):
		langs = [result() for i in range(21)]
		tag = post["_id"]
		for  lang in langs:
			lang.tag = tag
		
		langlist = post["value"]["langs"]
		for arr in langlist:
			lang = arr["lang"]
			lang = int(lang)
			langs[lang].AcceptedAnswerCount = arr["AcceptedAnswerCount"]
			langs[lang].QuestionCount = arr["QuestionCount"]
		return langs

	def printtofile(self, post):
		result = self.process(post)
		string = ""
		fh = open(self.tagfile,"a+")
		for i in range(1,len(result)):
			string += "%d,%d,"%(result[i].QuestionCount,result[i].AcceptedAnswerCount)
		fh.write(string+"\n")
		fh.close()
	
	def clear(self):
		os.remove(self.tagfile)

	def __init__(self):
		self.clear()
		connection = MongoClient()
		db = connection.stackoverflow
		table = db.tag_aac_qc_ratio.find()
		for post in table:
			self.printtofile(post)		

obj = tag_aac_qc_ratio()
