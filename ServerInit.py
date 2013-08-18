#-*- coding:UTF-8 -*-

import webapp2 , time
from vo.SsqInfo import SsqInfo

from google.appengine.ext import db

'''
数据初始化
'''
class SSQGetTotalAmountInDB(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('there are %d records in DB!!<br/>' % SsqInfo.all(keys_only=True).count(999999))
        
class SSQRemoveAllData(webapp2.RequestHandler):
    def get(self):
        try:
            while True:
                q = db.GqlQuery("SELECT __key__ FROM SsqInfo")
                assert q.count()
                db.delete(q.fetch(200))
                time.sleep(0.5)
        except Exception, e:
            self.response.out.write(repr(e)+'\n')
            pass

        self.response.out.write('empty DB is Done!!<br/>')

class Init1(webapp2.RequestHandler):
    def get(self):
        f = open('num1.csv', 'r')
        
        for idx,l in enumerate(f):
            l = l.replace('\n','')
            colArray = l.split(',')
            if len(colArray) == 8 :
                ssqInfo = SsqInfo()
                #2003-1,10,11,12,13,26,28,11 
                issueStr = colArray[0];
                
                replaceWord = ''
                if len(issueStr) == 6 :
                    replaceWord = '00'
                elif len(issueStr) == 7 :
                    replaceWord = '0'
                elif len(issueStr) == 8 :
                    replaceWord = ''
                
                ssqInfo.issue = issueStr.replace('-',replaceWord)
                ssqInfo.red = '%s %s %s %s %s %s' % (colArray[1],colArray[2],colArray[3],colArray[4],colArray[5],colArray[6])
                ssqInfo.blue = '%s' % colArray[7]
                
                ssqInfo.save()
                self.response.out.write('%d is Done<br/>' % idx)

class Init2(webapp2.RequestHandler):
    def get(self):
        f = open('num2.csv', 'r')
        
        for idx,l in enumerate(f):
            l = l.replace('\n','')
            colArray = l.split(',')
            if len(colArray) == 8 :
                ssqInfo = SsqInfo()
                #2003-1,10,11,12,13,26,28,11 
                issueStr = colArray[0];
                
                replaceWord = ''
                if len(issueStr) == 6 :
                    replaceWord = '00'
                elif len(issueStr) == 7 :
                    replaceWord = '0'
                elif len(issueStr) == 8 :
                    replaceWord = ''
                
                ssqInfo.issue = issueStr.replace('-',replaceWord)
                ssqInfo.red = '%s %s %s %s %s %s' % (colArray[1],colArray[2],colArray[3],colArray[4],colArray[5],colArray[6])
                ssqInfo.blue = '%s' % colArray[7]
                
                ssqInfo.save()
                self.response.out.write('%d is Done<br/>' % idx)
                
class Init3(webapp2.RequestHandler):
    def get(self):
        f = open('num3.csv', 'r')
        
        for idx,l in enumerate(f):
            l = l.replace('\n','')
            colArray = l.split(',')
            if len(colArray) == 8 :
                ssqInfo = SsqInfo()
                #2003-1,10,11,12,13,26,28,11 
                issueStr = colArray[0];
                
                replaceWord = ''
                if len(issueStr) == 6 :
                    replaceWord = '00'
                elif len(issueStr) == 7 :
                    replaceWord = '0'
                elif len(issueStr) == 8 :
                    replaceWord = ''
                
                ssqInfo.issue = issueStr.replace('-',replaceWord)
                ssqInfo.red = '%s %s %s %s %s %s' % (colArray[1],colArray[2],colArray[3],colArray[4],colArray[5],colArray[6])
                ssqInfo.blue = '%s' % colArray[7]
                
                ssqInfo.save()
                self.response.out.write('%d is Done<br/>' % idx)
                
class Init4(webapp2.RequestHandler):
    def get(self):
        f = open('num4.csv', 'r')
        
        for idx,l in enumerate(f):
            l = l.replace('\n','')
            colArray = l.split(',')
            if len(colArray) == 8 :
                ssqInfo = SsqInfo()
                #2003-1,10,11,12,13,26,28,11 
                issueStr = colArray[0];
                
                replaceWord = ''
                if len(issueStr) == 6 :
                    replaceWord = '00'
                elif len(issueStr) == 7 :
                    replaceWord = '0'
                elif len(issueStr) == 8 :
                    replaceWord = ''
                
                ssqInfo.issue = issueStr.replace('-',replaceWord)
                ssqInfo.red = '%s %s %s %s %s %s' % (colArray[1],colArray[2],colArray[3],colArray[4],colArray[5],colArray[6])
                ssqInfo.blue = '%s' % colArray[7]
                
                ssqInfo.save()
                self.response.out.write('%d is Done<br/>' % idx)