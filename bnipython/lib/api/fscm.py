from bnipython.lib.services.fscm import sendInvoice
from bnipython.lib.services.fscm import inquiry
from bnipython.lib.services.fscm import checkTransactionPlafond
from bnipython.lib.services.fscm import checkLimit
from bnipython.lib.services.fscm import checkStopSupply
from bnipython.lib.services.fscm import deleteInvoice
from bnipython.lib.services.fscm import praNota
from bnipython.lib.services.fscm import deletePranota

class FSCM():
     def __init__(self, client):
        self.client = client.config
        self.baseUrl = client.getBaseUrl()
        self.config = client.getConfig()
        self.token = client.getToken()

     def sendInvoice(self, params):
         res = sendInvoice.sendInvoice({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def inquiry(self, params):
         res = inquiry.inquiry({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def checkTransactionPlafond(self, params):
         res = checkTransactionPlafond.checkTransactionPlafond({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def checkLimit(self, params):
         res = checkLimit.checkLimit({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def checkStopSupply(self, params):
         res = checkStopSupply.checkStopSupply({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def deleteInvoice(self, params):
         res = deleteInvoice.deleteInvoice({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def praNota(self, params):
         res = praNota.praNota({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def deletePranota(self, params):
         res = deletePranota.deletePranota({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     