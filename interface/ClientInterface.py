#-*- coding:UTF-8 -*-

import json

import webapp2
#from google.appengine.ext import webapp

from vo.SsqInfo import SsqInfo

'''
客户端接口

'''

'''获取最新开奖信息'''
class SSQLastData(webapp2.RequestHandler):
    
    def get(self):
        ssqInfo = None
        q = SsqInfo.all()
        q.order('-issue')
        results = q.fetch(limit=1)
        if len(results) > 0:
            ssqInfo = results[0]
        
        dict = {}
        if ssqInfo is not None:
            if ssqInfo.kjDate is not None :
                dict["kjDate"] = ssqInfo.kjDate
            if ssqInfo.issue is not None :
                dict["issue"] = ssqInfo.issue
            if ssqInfo.red is not None :
                dict["red"] = ssqInfo.red
            if ssqInfo.blue is not None :
                dict["blue"] = ssqInfo.blue
            if ssqInfo.ballNum is not None :
                dict["ballNum"] = ssqInfo.ballNum
            if ssqInfo.poolMoneyAmount is not None :
                dict["poolMoneyAmount"] = ssqInfo.poolMoneyAmount
            if ssqInfo.soldMoneyAmount is not None :
                dict["soldMoneyAmount"] = ssqInfo.soldMoneyAmount
                
            if ssqInfo.oneMoneyAmount is not None :
                dict["oneMoneyAmount"] = ssqInfo.oneMoneyAmount
            if ssqInfo.oneBetAmount is not None :
                dict["oneBetAmount"] = ssqInfo.oneBetAmount
            if ssqInfo.twoMoneyAmount is not None :
                dict["twoMoneyAmount"] = ssqInfo.twoMoneyAmount
            if ssqInfo.twoBetAmount is not None :
                dict["twoBetAmount"] = ssqInfo.twoBetAmount
            if ssqInfo.threeMoneyAmount is not None :
                dict["threeMoneyAmount"] = ssqInfo.threeMoneyAmount
            if ssqInfo.threeBetAmount is not None :
                dict["threeBetAmount"] = ssqInfo.threeBetAmount
            if ssqInfo.fourMoneyAmount is not None :
                dict["fourMoneyAmount"] = ssqInfo.fourMoneyAmount
            if ssqInfo.fourBetAmount is not None :
                dict["fourBetAmount"] = ssqInfo.fourBetAmount
            if ssqInfo.fiveMoneyAmount is not None :
                dict["fiveMoneyAmount"] = ssqInfo.fiveMoneyAmount
            if ssqInfo.fiveBetAmount is not None :
                dict["fiveBetAmount"] = ssqInfo.fiveBetAmount
            if ssqInfo.sixMoneyAmount is not None :
                dict["sixMoneyAmount"] = ssqInfo.sixMoneyAmount
            if ssqInfo.sixBetAmount is not None :
                dict["sixBetAmount"] = ssqInfo.sixBetAmount
            
        self.response.out.write(json.dumps(dict))

''' 获取历史开奖数据 '''
class SSQHistory(webapp2.RequestHandler):
    def get(self):
        beginIssue = None   #起始期号
        pageCount = 15      #分页数量
        
        try:
            beginIssue = self.request.headers['beginIssue']
        except:
            pass
        
        q = SsqInfo.all()
        if beginIssue is not None :
            q.filter('issue <', beginIssue)
        q.order('-issue')
        results = q.fetch(limit=pageCount)
        
        resultArray = []
        if len(results) > 0 :
            for ssqInfo in results :
                dict = {}
                if ssqInfo.kjDate is not None :
                    dict["kjDate"] = ssqInfo.kjDate
                if ssqInfo.issue is not None :
                    dict["issue"] = ssqInfo.issue
                if ssqInfo.red is not None :
                    dict["red"] = ssqInfo.red
                if ssqInfo.blue is not None :
                    dict["blue"] = ssqInfo.blue
                if ssqInfo.ballNum is not None :
                    dict["ballNum"] = ssqInfo.ballNum
                if ssqInfo.poolMoneyAmount is not None :
                    dict["poolMoneyAmount"] = ssqInfo.poolMoneyAmount
                if ssqInfo.soldMoneyAmount is not None :
                    dict["soldMoneyAmount"] = ssqInfo.soldMoneyAmount
                    
                if ssqInfo.oneMoneyAmount is not None :
                    dict["oneMoneyAmount"] = ssqInfo.oneMoneyAmount
                if ssqInfo.oneBetAmount is not None :
                    dict["oneBetAmount"] = ssqInfo.oneBetAmount
                if ssqInfo.twoMoneyAmount is not None :
                    dict["twoMoneyAmount"] = ssqInfo.twoMoneyAmount
                if ssqInfo.twoBetAmount is not None :
                    dict["twoBetAmount"] = ssqInfo.twoBetAmount
                if ssqInfo.threeMoneyAmount is not None :
                    dict["threeMoneyAmount"] = ssqInfo.threeMoneyAmount
                if ssqInfo.threeBetAmount is not None :
                    dict["threeBetAmount"] = ssqInfo.threeBetAmount
                if ssqInfo.fourMoneyAmount is not None :
                    dict["fourMoneyAmount"] = ssqInfo.fourMoneyAmount
                if ssqInfo.fourBetAmount is not None :
                    dict["fourBetAmount"] = ssqInfo.fourBetAmount
                if ssqInfo.fiveMoneyAmount is not None :
                    dict["fiveMoneyAmount"] = ssqInfo.fiveMoneyAmount
                if ssqInfo.fiveBetAmount is not None :
                    dict["fiveBetAmount"] = ssqInfo.fiveBetAmount
                if ssqInfo.sixMoneyAmount is not None :
                    dict["sixMoneyAmount"] = ssqInfo.sixMoneyAmount
                if ssqInfo.sixBetAmount is not None :
                    dict["sixBetAmount"] = ssqInfo.sixBetAmount
        
                resultArray.append(dict)
                
        self.response.out.write(json.dumps(resultArray))
        
        