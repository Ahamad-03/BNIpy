from bnipython.lib.services.bnidirect import bulkGetStatus
from bnipython.lib.services.bnidirect import bniPopsCashAndCarry
from bnipython.lib.services.bnidirect import bniPopsProductAllocation
from bnipython.lib.services.bnidirect import bniPopsResubmitCashAndCarry
from bnipython.lib.services.bnidirect import bniPopsResubmitProductAllocation
from bnipython.lib.services.bnidirect import inquiryVirtualAccountTransaction
from bnipython.lib.services.bnidirect import updateVirtualAccount
from bnipython.lib.services.bnidirect import createVirtualAccount
from bnipython.lib.services.bnidirect import billingPayment
from bnipython.lib.services.bnidirect import getPaymentStatus
from bnipython.lib.services.bnidirect import inhouseTransfer
from bnipython.lib.services.bnidirect import inquiryBNIPOPSProductAllocation
from bnipython.lib.services.bnidirect import onlineTransfer
from bnipython.lib.services.bnidirect import transferInternational
from bnipython.lib.services.bnidirect import transferLLG
from bnipython.lib.services.bnidirect import transferRTGS

class BNIDIRECT():
     def __init__(self, client):
        self.client = client.config
        self.baseUrl = client.getBaseUrl()
        self.config = client.getConfig()
        self.token = client.getToken()

     def bulkGetStatus(self, params):
         res = bulkGetStatus.bulkGetStatus({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def bniPopsCashAndCarry(self, params):
         res = bniPopsCashAndCarry.bniPopsCashAndCarry({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def bniPopsProductAllocation(self, params):
         res = bniPopsProductAllocation.bniPopsProductAllocation({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def bniPopsResubmitCashAndCarry(self, params):
         res = bniPopsResubmitCashAndCarry.bniPopsResubmitCashAndCarry({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def bniPopsResubmitProductAllocation(self, params):
         res = bniPopsResubmitProductAllocation.bniPopsResubmitProductAllocation({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def inquiryVirtualAccountTransaction(self, params):
         res = inquiryVirtualAccountTransaction.inquiryVirtualAccountTransaction({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def updateVirtualAccount(self, params):
         res = updateVirtualAccount.updateVirtualAccount({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def createVirtualAccount(self, params):
         res = createVirtualAccount.createVirtualAccount({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def billingPayment(self, params):
         res = billingPayment.billingPayment({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def getPaymentStatus(self, params):
         res = getPaymentStatus.getPaymentStatus({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def inhouseTransfer(self, params):
         res = inhouseTransfer.inhouseTransfer({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def inquiryBNIPOPSProductAllocation(self, params):
         res = inquiryBNIPOPSProductAllocation.inquiryBNIPOPSProductAllocation({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def onlineTransfer(self, params):
         res = onlineTransfer.onlineTransfer({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def transferInternational(self, params):
         res = transferInternational.transferInternational({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def transferLLG(self, params):
         res = transferLLG.transferLLG({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def transferRTGS(self, params):
         res = transferRTGS.transferRTGS({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res