#-*- coding:UTF-8 -*-
'''
Created on 2011-11-13

@author: evil

双色球值对象
'''
from google.appengine.ext import db

class SsqInfo(db.Model):
    kjDate = db.StringProperty()        #开奖时间
    issue = db.StringProperty()         #期号
    red = db.StringProperty()           #红球
    blue = db.StringProperty()          #篮球
    ballNum = db.StringProperty()       #本期开奖采用 : 第X套球
    poolMoneyAmount = db.FloatProperty()   #奖池累计金额
    soldMoneyAmount = db.FloatProperty()   #本期销售额
    
    oneMoneyAmount = db.FloatProperty()   #一等奖 单注中奖金额（元） :     5719094
    oneBetAmount = db.IntegerProperty()   #一等奖 中奖注数（注） :     17
    twoMoneyAmount = db.FloatProperty()
    twoBetAmount = db.IntegerProperty()
    threeMoneyAmount = db.FloatProperty()
    threeBetAmount = db.IntegerProperty()
    fourMoneyAmount = db.FloatProperty()
    fourBetAmount = db.IntegerProperty()
    fiveMoneyAmount = db.FloatProperty()
    fiveBetAmount = db.IntegerProperty()
    sixMoneyAmount = db.FloatProperty()
    sixBetAmount = db.IntegerProperty()
    
    createDate = db.DateTimeProperty(auto_now_add=True)   #create Date
    
    


        