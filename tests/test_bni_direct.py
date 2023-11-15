from bnipython.lib.api.bniDirect import BNIDIRECT
from bnipython.lib.util import constants
import unittest
from bnipython.lib.bniClient import BNIClient
import json

class TestBNIDIRECT(unittest.TestCase):
    client = BNIClient({
        'env': 'sandbox-2',
        'appName': constants.APP_NAME,
        'clientId': constants.CLIENT_ID_ENCRYPT,
        'clientSecret': constants.CLIENT_SECRET_ENCRYPT,
        'apiKey': constants.API_KEY_ENCRYPT,
        'apiSecret': constants.API_SECRET_ENCRYPT,
        'bniDirectApiKey': constants.BNI_DIRECT_KEY_ENCRYPT
    })

    # def testBulkGetStatus(self):
    #     print('\n============================================')
    #     bni_direct = BNIDIRECT(self.client)
    #     res = bni_direct.bulkGetStatus({
    #         "corporateId":"BNI_SIT",
    #         "userId":"WTI_MAKER1",
    #         "fileRefNo":"",
    #         "apiRefNo":"34ab87f29e88c23a"
    #     })
    #     data = res['requestStatus']
    #     self.assertEqual(data, '0')
    #     print('\033[92m should return requestStatus 0 \033[0m')

    # def testBniPopsCashAndCarry(self):
    #     print('\n============================================')
    #     bni_direct = BNIDIRECT(self.client)
    #     res = bni_direct.bniPopsCashAndCarry({
    #         "corporateId":"BNI_SIT",
    #         "userId":"WTI_MAKER1",
    #         "debitAccountNo": "108098391",
    #         "salesOrganizationCode": "1001",
    #         "distributionChannelCode": "10",
    #         "productCode": "04",
    #         "shipTo": "700258",
    #         "debitOrCreditNoteNo": "def",
    #         "productInformationDetail": [
    #             {
    #                 "materialCode": "A040900002",
    #                 "trip": "1",
    #                 "quantity": "2",
    #                 "deliveryDate": "20231228",
    #                 "transportir": "abcd"
    #             }
    #         ]
    #     })
    #     data = res['requestStatus']
    #     self.assertEqual(data, '0')
    #     print('\033[92m should return requestStatus 0 \033[0m')

    # def testBniPopsProductAllocation(self):
    #     print('\n============================================')
    #     bni_direct = BNIDIRECT(self.client)
    #     res = bni_direct.bniPopsProductAllocation({
    #         "corporateId":"BNI_SIT",
    #         "userId":"WTI_MAKER1",
    #         "debitAccountNo": "115208364",
    #         "salesOrganizationCode": "1002",
    #         "distributionChannelCode": "10",
    #         "productCode": "04",
    #         "shipTo": "1123123",
    #         "scheduleAggreementNo": "118282812",
    #         "debitOrCreditNoteNo": "123231",
    #         "productInformationDetail": [
    #             {
    #                 "materialCode": "A040900001",
    #                 "trip": "1123123",
    #                 "quantity": "100",
    #                 "deliveryDate": "20231119",
    #                 "transportir": ""
    #             }
    #         ]
    #     })
    #     data = res['requestStatus']
    #     self.assertEqual(data, '0')
    #     print('\033[92m should return requestStatus 0 \033[0m')

    # def testBniPopsResubmitCashAndCarry(self):
    #     print('\n============================================')
    #     bni_direct = BNIDIRECT(self.client)
    #     res = bni_direct.bniPopsResubmitCashAndCarry({
    #         "corporateId":"BNI_SIT",
    #         "userId":"WTI_MAKER1",
    #         "transactionReferenceNo":"201809181708919534",
    #         "SONumber":""
    #     })
    #     data = res['requestStatus']
    #     self.assertEqual(data, '0')
    #     print('\033[92m should return requestStatus 0 \033[0m')

    # def testBniPopsResubmitProductAllocation(self):
    #     print('\n============================================')
    #     bni_direct = BNIDIRECT(self.client)
    #     res = bni_direct.bniPopsResubmitProductAllocation({
    #         "corporateId":"BNI_SIT",
    #         "userId":"WTI_MAKER1",
    #         "transactionReferenceNo":"201809181708919534",
    #         "SONumber":""
    #     })
    #     data = res['requestStatus']
    #     self.assertEqual(data, '0')
    #     print('\033[92m should return requestStatus 0 \033[0m')

    # def testInquiryVirtualAccountTransaction(self):
    #     print('\n============================================')
    #     bni_direct = BNIDIRECT(self.client)
    #     res = bni_direct.inquiryVirtualAccountTransaction({
    #         "corporateId":"BNI_SIT",
    #         "userId":"WTI_MAKER1",
    #         "virtualAccountNo":"8310000011112323",
    #         "fromDate":"20161015",
    #         "toDate":"20201015"
    #     })
    #     data = res['requestStatus']
    #     self.assertEqual(data, '0')
    #     print('\033[92m should return requestStatus 0 \033[0m')

    # def testUpdateVirtualAccount(self):
    #     print('\n============================================')
    #     bni_direct = BNIDIRECT(self.client)
    #     res = bni_direct.updateVirtualAccount({
    #         "corporateId":"BNI_SIT",
    #         "userId":"WTI_MAKER1",
    #         "companyCode":"8310",
    #         "virtualAccountNo":"8310888800009999",
    #         "virtualAccountName":"SHORT NAME",
    #         "virtualAccountTypeCode":"7",
    #         "billingAmount":"100000",
    #         "varAmount1":"",
    #         "varAmount2":"",
    #         "expiryDate":"20201120",
    #         "expiryTime":"10:10:10",
    #         "mobilePhoneNo":"08712717272",
    #         "statusCode":"1"
    #     })
    #     data = res['requestStatus']
    #     self.assertEqual(data, '0')
    #     print('\033[92m should return requestStatus 0 \033[0m')

    # def testUpdateVirtualAccount(self):
    #     print('\n============================================')
    #     bni_direct = BNIDIRECT(self.client)
    #     res = bni_direct.updateVirtualAccount({
    #         "corporateId":"BNI_SIT",
    #         "userId":"WTI_MAKER1",
    #         "companyCode":"8310",
    #         "virtualAccountNo":"8310888800009999",
    #         "virtualAccountName":"SHORT NAME",
    #         "virtualAccountTypeCode":"7",
    #         "billingAmount":"100000",
    #         "varAmount1":"",
    #         "varAmount2":"",
    #         "expiryDate":"20201120",
    #         "expiryTime":"10:10:10",
    #         "mobilePhoneNo":"08712717272",
    #         "statusCode":"1"
    #     })
    #     data = res['requestStatus']
    #     self.assertEqual(data, '0')
    #     print('\033[92m should return requestStatus 0 \033[0m')

    # def testCreateVirtualAccount(self):
    #     print('\n============================================')
    #     bni_direct = BNIDIRECT(self.client)
    #     res = bni_direct.createVirtualAccount({
    #         "corporateId":"BNI_SIT",
    #         "userId":"WTI_MAKER1",
    #         "companyCode":"98800011",
    #         "virtualAccountNo":"16623254",
    #         "virtualAccountName":"Agus KEREN1",
    #         "virtualAccountTypeCode":"7",
    #         "billingAmount":"800000",
    #         "varAmount1":"200000",
    #         "varAmount2":"120000",
    #         "expiryDate":"20201021",
    #         "expiryTime":"11:09:08",
    #         "mobilePhoneNo":"08432432432",
    #         "statusCode":"1"
    #     })
    #     data = res['requestStatus']
    #     self.assertEqual(data, '0')
    #     print('\033[92m should return requestStatus 0 \033[0m')
    
    def testBalanceInquiry(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.balanceInquiry({
            "corporateId":"BNI_SIT",
            "userId":"WTI_MAKER1",
            "accountList": ["116952891", "4447"]
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')
        
    def testDomesticSingleBIFastTransfer(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.domesticSingleBIFastTransfer({
            "corporateId": "BNI_SIT",
            "userId": "WTI_MAKER1",
            "debitedAccountNo": "1000599764",
            "amountCurrency": "IDR",
            "amount": "500000",
            "exchangeRateCode": "Cr",
            "treasuryReferenceNo": "",
            "chargeTo": "OUR",
            "remark1": "BIFast-RMK1",
            "remark2": "BIFast-RMK1",
            "remark3": "BIFast-RMK1",
            "remitterReferenceNo": "UYYBI2103202314",
            "finalizePaymentFlag": "Y",
            "beneficiaryReferenceNo": "BENGTYRSD110",
            "usedProxy": "N",
            "beneficiaryAccountNo": "9832132281",
            "proxyId": "",
            "beneficiaryBankCode": "BBBAIDJA",
            "beneficiaryBankName": "Bank Permata",
            "notificationFlag": "N",
            "beneficiaryEmail": "",
            "transactionInstructionDate": "20231107",
            "transactionPurposeCode": "01"
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testInquiryForexRate(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.inquiryForexRate({
            "corporateId":"BNI_SIT",
            "userId":"WTI_MAKER1",
            "currencyList": ["IDR", "USD"]
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')