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

    def testBulkPaymentMixed(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.bulkPaymentMixed({
            "corporateId": "BNI_SIT",
            "userId": "WTI_MAKER1",
            "apiRefNo": "TRX029SEPT23009971301",
            "instructionDate": "20230929",
            "session": "",
            "serviceType": "MXD",
            "debitAcctNo": "",
            "amount": "",
            "currency": "",
            "chargeTo": "",
            "residenceCode": "",
            "citizenCode": "",
            "category": "",
            "transactionType": "D",
            "accountNmValidation": "Y",
            "remark": "BULK PAYMENT MXD",
            "childContent": "9832132281,NAMA ILMPPJTNU,100001,,REMARK1-HWBM,REMARK2-YFFW,REMARK3-UNBJ,Bene Address 1,Bene Address 2,Bene Address 3,BBBAIDJA,Bank Permata,Bank Permata|Branch Jl. Kapten Tendean 12-14A,Jl. Kapten Tendean 12-14A,Jakarta 12790,Jakarta Selatan,Jakarta,Indonesia,ID,ID,wide.beneficiary@gmail.com,,,,,,,,,REM70587148UDMW,Y,BEN70587148UDMW,EXDET1,EXDET2,EXDET3,EXDET4,EXDET5,,BF,IDR,108098391,OUR,ID,ID,C9,N,N,085317773020,01"
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testPayrollMixed(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.payrollMixed({
            "corporateId": "BNI_SIT",
            "userId": "WTI_MAKER1",
            "apiRefNo": "YXX029SEPT2300997131",
            "instructionDate": "20230929",
            "session": "",
            "serviceType": "MXD",
            "debitAcctNo": "",
            "amount": "",
            "currency": "",
            "chargeTo": "",
            "residenceCode": "",
            "citizenCode": "",
            "category": "",
            "transactionType": "D",
            "accountNmValidation": "Y",
            "remark": "BULK PAYMENT MXD",
            "childContent": "889213621,NAMA SWQUTGLHR,101,,REMARK1-IGTE,REMARK2-QEZQ,REMARK3-TYXH,Bene Address 1,Bene Address 2,Bene Address 3,,,,,,,,,,,wide.beneficiary@gmail.com,,,,2012,,,,,REM38060584AHIQ,Y,BEN38060584AHIQ,EXDET1,EXDET2,EXDET3,EXDET4,EXDET5,,IHT,IDR,108098391,OUR,ID,ID,C9,N,,,|@|889213622,NAMA VONGVHDPW,100002,,REMARK1-TLHU,REMARK2-RNWB,REMARK3-BOYN,Bene Address 1,Bene Address 2,Bene Address 3,BRINIDJA,Bank Raykat Indonesia,Bank Raykat Indonesia|Branch Jl. M.H Thamrin No. 1,Jl. M.H Thamrin No. 1,Jakarta 10310,Jakarta Pusat,Jakarta,Indonesia,ID,ID,wide.beneficiary@gmail.com,,,,,,,,,REM67021138WHQM,Y,BEN67021138WHQM,EXDET1,EXDET2,EXDET3,EXDET4,EXDET5,2,LLG,IDR,108098391,OUR,ID,ID,C9,N,,,|@|889213623,NAMA CFOJGYSCN,100000002,,REMARK1-JIEV,REMARK2-EPMP,REMARK3-ZXFR,Bene Address 1,Bene Address 2,Bene Address 3,BRINIDJA,Bank Raykat Indonesia,Bank Raykat Indonesia|Branch Jl. M.H Thamrin No. 1,Jl. M.H Thamrin No. 1,Jakarta 10310,Jakarta Pusat,Jakarta,Indonesia,ID,ID,wide.beneficiary@gmail.com,,,,,,,,,REM53427300BHQC,Y,BEN53427300BHQC,EXDET1,EXDET2,EXDET3,EXDET4,EXDET5,,RTGS,IDR,108098391,OUR,ID,ID,C9,N,,,|@|889213624,NAMA YPEGAUEUJ,100003,,REMARK1-NXHV,REMARK2-DMNV,REMARK3-RNMI,Bene Address 1,Bene Address 2,Bene Address 3,002,Bank Raykat Indonesia,Bank Raykat Indonesia|Branch Jl. M.H Thamrin No. 1,Jl. M.H Thamrin No. 1,Jakarta 10310,Jakarta Pusat,Jakarta,Indonesia,ID,ID,wide.beneficiary@gmail.com,,,,,,,,,REM87661139PXGR,Y,BEN87661139PXGR,EXDET1,EXDET2,EXDET3,EXDET4,EXDET5,,OT,IDR,108098391,OUR,ID,ID,C9,N,,,|@|1150007270863,NAMA TAQMEAMLE,100001,,REMARK1-UZAB,REMARK2-RXWS,REMARK3-UWPS,Bene Address 1,Bene Address 2,Bene Address 3,BMRIIDJA,BANK MANDIRI,BANK MANDIRI BRANCH,Jl. Kapten Tendean 12-14A,Jakarta 12790,Jakarta Selatan,Jakarta,Indonesia,ID,ID,wide.beneficiary@gmail.com,,,,,,,,,REM96734911GLBT,Y,BEN96734911GLBT,EXDET1,EXDET2,EXDET3,EXDET4,EXDET5,,BF,IDR,108098391,OUR,ID,ID,C9,N,N,6281280533832,03|@|889213626,NAMA QVBCZETAV,102,,REMARK1-SBUR,REMARK2-URWV,REMARK3-HBSC,Bene Address 1,Bene Address 2,Bene Address 3,BIC|ABBYGB2LXXX,Abbey National,Abbey National|Branch 2 Triton Square,2 Triton Square,Regent's Place NW1 3AN,London,London,United Kingdom,ID,ID,wide.beneficiary@gmail.com,085317773020,021991826,Bank BNI,2012,N,N,C9,LLD Desc,REM61083690MDPP,Y,BEN61083690MDPP,EXDET1,EXDET2,EXDET3,EXDET4,EXDET5,,IFT,USD,108098391,OUR,ID,ID,C9,N,,,"
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testInquiryChildAccount(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.inquiryChildAccount({
            "corporateId": "BNI_SIT",
            "userId": "WTI_MAKER1",
            "accountNo": "1000599684"
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testCallbackApi(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.callbackApi({
            "corporateId": "COMPANYMB",
            "userId": "SWAMAKER",
            "apiRefNo": "2324dab653f",
            "status": "Executed Successfully"
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testInquiryBIFastBeneficiary(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.inquiryBIFastBeneficiary({
            "corporateId": "BNI_SIT",
            "userId": "WTI_MAKER1",
            "usedProxy": "N",
            "beneficiaryAccountNo": "9832132281",
            "proxyId": "",
            "beneficiaryBankCode": "BBBAIDJA"
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')