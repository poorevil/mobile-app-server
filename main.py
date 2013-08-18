#-*- coding:UTF-8 -*-

import webapp2

from GetLastSsqData import GetLastSsqData
from interface import ClientInterface

import ServerInit


app = webapp2.WSGIApplication([('/ssqlastdata', ClientInterface.SSQLastData)
                              ,('/ssqhistory', ClientInterface.SSQHistory)
                              ,('/getdata', GetLastSsqData)
                              ,('/ssqtotalamount', ServerInit.SSQGetTotalAmountInDB)
                              ,('/empty', ServerInit.SSQRemoveAllData)
                              ,('/init4', ServerInit.Init4)],
                              debug=True)
