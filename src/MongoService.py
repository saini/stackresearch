'''
Created on Feb 25, 2013

@author: vaibhavsaini
'''
from LoadTagsPost import DataLoad
from pymongo import Connection
import sys
from bson.code import Code 
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
        self.langMap = {1:'java',
                        2:'pyhton',
                        3:'c#',
                        4:'c++',
                        5:'php',
                        6:'c',
                        7:'ruby',
                        8:'ruby-on-rails',
                        9:'javascript',
                        10:'jquery',
                        11:'asp.net',
                        12:'objective-c',
                        13:'sql',
                        14:'xml',
                        15:'perl',
                        16:'cocoa',
                        17:'delphi',
                        18:'scala',
                        19:'node.js',
                        20:'visual-c++'}
        #self.sqlservice = DataLoad(self.config['sql_config'])

    def loadData(self,start,end,window):
        i = start
        j = i+window
        while j<=end: 
            rows = self.sqlservice.readData(i, j)
            rows = self.getVars(rows)
            print "********", i, j
            i = j
            j += window
            question_answer_map = self.db.qa
            question_answer_map.insert(rows)
        print "returning from loadData"

    def loadData2(self,start,end,window):
        i = start
        j = i+window
        while j<=end: 
            rows = self.sqlservice.readData2(i, j)
            rows = self.getVars(rows)
            print "********", i, j
            i = j
            j += window
            question_answer_map = self.db.qa
            question_answer_map.insert(rows)
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
    
    def tag_toLang_Html(self):
        tag_aac_qc_ratio =  self.db.tag_aac_qc_ratio
        tag = 'list'
        entry = tag_aac_qc_ratio.find_one({"_id":tag})
        langsArray = entry['value']['langs']
#        langArray = ['Germany', 'USA', 'Brazil', 'Canada', 'France', 'RU']
#        acc_qc_count_array = [700, 300, 400, 500, 600, 800]
        lang = "["
        acc_qc_count = "["
#        for langObj in langArray:
#            print langObj
#            lang += "'"+langObj+"', "
#        lang = lang[:-2]+"]"
#
#        for a in acc_qc_count_array:
#            print a
#            acc_qc_count += str(a)+", "
#        acc_qc_count = acc_qc_count[:-2]+"]"

        for langObj in langsArray:
            print langObj['lang']
            lang += "'"+self.langMap[langObj['lang']]+"', "
            acc_qc_count += str(langObj['ratio'])+", "
        lang = lang[:-2]+"]"
        acc_qc_count = acc_qc_count[:-2]+"]"

        #lang = """['Germany', 'USA', 'Brazil', 'Canada', 'France', 'RU']"""
        #acc_qc_count = """[700, 300, 400, 500, 600, 800]"""
        html = """<!--
You are free to copy and use this sample in accordance with the terms of the
Apache license (http://www.apache.org/licenses/LICENSE-2.0.html)
-->

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
    <title>
      Google Visualization API Sample
    </title>
    <script type="text/javascript" src="http://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load('visualization', '1');
    </script>
    <script type="text/javascript">
      function drawVisualization() {
          var data = new google.visualization.DataTable();
          data.addColumn('string','lang');
          data.addColumn('number','aac');
          langs = """ + lang +""" ;
          aac = """ + acc_qc_count + """ ;
          for (var i = 0; i < aac.length; ++i) {
              data.addRow([ langs[i],aac[i]])
            }
          
          var wrapper = new google.visualization.ChartWrapper({
            chartType: 'ColumnChart',
            dataTable: data,
            options: {'title': 'AAC To Language for Tag: """+tag+""" '},
            containerId: 'visualization'
          });
          wrapper.draw();
        }
      
      

      google.setOnLoadCallback(drawVisualization);
    </script>
  </head>
  <body style="font-family: Arial;border: 0 none;">
    <div id="visualization" style="width: 600px; height: 400px;"></div>
  </body>
</html>
"""
        return html
    
    def scattared_tags_Html(self, limit):
        lang_aac_qc_ratio =  self.db.lang_aac_qc_ratio
        language_id = 1
        entry = lang_aac_qc_ratio.find_one({"_id":language_id})
        tagsArray = entry['value']['tags']
        qc = "["
        aac = "["
        for tagObj in tagsArray:
            print tagObj['AcceptedAnswerCount']
            if tagObj['QuestionCount']<limit:
                aac += str(tagObj['AcceptedAnswerCount'])+", "
                qc += str(tagObj['QuestionCount'])+", "
        aac = aac[:-2]+"]"
        qc = qc[:-2]+"]"
        html = """<!--
You are free to copy and use this sample in accordance with the terms of the
Apache license (http://www.apache.org/licenses/LICENSE-2.0.html)
-->

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
    <title>
      Google Visualization API Sample
    </title>
    <script type="text/javascript" src="http://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load('visualization', '1', {packages: ['corechart']});
    </script>
    <script type="text/javascript">
      function drawVisualization() {
    // Create and populate the data table.
    var data = new google.visualization.DataTable();
    data.addColumn('number');
    data.addColumn('number');
    data.addColumn('number');
  data.addColumn('number');
var aac= """+aac + """ 
var qc= """ + qc + """ 
    for (var i = 0; i < aac.length; ++i) {
      data.addRow([ qc[i],aac[i], null,null])
    }
    for (var i = 0; i < """+ str(limit)+ """ ; ++i) {
      data.addRow([ i,null, i,null])
    }



    // Create and draw the visualization.
    var chart = new google.visualization.ScatterChart(
        document.getElementById('visualization'));
    chart.draw(data, {title: 'Stackoverflow Language community support for : """+self.langMap[language_id]+""" accross all tags',
                      width: 600, height: 400,
                      vAxis: {title: "Accepted Answer Count", titleTextStyle: {color: "green"},minValue: 0, maxValue: 1400},
                      hAxis: {title: "Question Count", titleTextStyle: {color: "green"},minValue: 0, maxValue: 1000},
                      pointSize:1,
                     }
              );
}
      google.setOnLoadCallback(drawVisualization);
    </script>
  </head>
  <body style="font-family: Arial;border: 0 none;">
    <div id="visualization" style="width: 600px; height: 400px;"></div>
  </body>
</html>
"""
        return html

    def writeToFile(self, text):
        file = open("dummy2.html",'a')
        try:
            file.write(text)
        finally:
            file.close()

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
    print "creating html"
    #mservice.dummyHtml()
    #mservice.writeToFile(mservice.tag_toLang_Html())
    args = sys.argv
    mservice.writeToFile(mservice.scattared_tags_Html(int(args[1])))
    print "done"
#    args = sys.argv
#    st = sys.argv[1]
#    en = sys.argv[2]
#    win = sys.argv[3]
#    sel = sys.argv[4]
#    print "loading..."
#    if int(sel)==1:
#        mservice.loadData(int(st),int(en),int(win))
#    elif int(sel)==2:
#        mservice.loadData2(int(st),int(en),int(win))
#    print "loading done.."
