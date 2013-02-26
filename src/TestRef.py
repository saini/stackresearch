'''
Created on Feb 24, 2013

@author: vaibhavsaini
'''

class TestRef():
    '''
    classdocs
    '''
    var1 = "hi"
    var2 = "hey"

    def __init__(self, params):
        '''
        Constructor
        '''
        self.name = "hello"
        self.purpose = "world"


x = "TestRef.var1"
print eval(x)