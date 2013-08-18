'''
Created on 2011-11-13

@author: evil
'''
from google.appengine.ext import db

class Message(db.Model):
    '''
    classdocs
    '''
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

#    def __init__(selfparams):
#        '''
#        Constructor
#        '''
    
    


        