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

    def testBulkGetStatus(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.bulkGetStatus({
            "corporateId":"BNI_SIT",
            "userId":"WTI_MAKER1",
            "fileRefNo":"",
            "apiRefNo":"34ab87f29e88c23a"
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testBniPopsCashAndCarry(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.bniPopsCashAndCarry({
            "corporateId":"BNI_SIT",
            "userId":"WTI_MAKER1",
            "debitAccountNo": "108098391",
            "salesOrganizationCode": "1001",
            "distributionChannelCode": "10",
            "productCode": "04",
            "shipTo": "700258",
            "debitOrCreditNoteNo": "def",
            "productInformationDetail": [
                {
                    "materialCode": "A040900002",
                    "trip": "1",
                    "quantity": "2",
                    "deliveryDate": "20231228",
                    "transportir": "abcd"
                }
            ]
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testBniPopsProductAllocation(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.bniPopsProductAllocation({
            "corporateId":"BNI_SIT",
            "userId":"WTI_MAKER1",
            "debitAccountNo": "115208364",
            "salesOrganizationCode": "1002",
            "distributionChannelCode": "10",
            "productCode": "04",
            "shipTo": "1123123",
            "scheduleAggreementNo": "118282812",
            "debitOrCreditNoteNo": "123231",
            "productInformationDetail": [
                {
                    "materialCode": "A040900001",
                    "trip": "1123123",
                    "quantity": "100",
                    "deliveryDate": "20231119",
                    "transportir": ""
                }
            ]
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testBniPopsResubmitCashAndCarry(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.bniPopsResubmitCashAndCarry({
            "corporateId":"BNI_SIT",
            "userId":"WTI_MAKER1",
            "transactionReferenceNo":"201809181708919534",
            "SONumber":""
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testBniPopsResubmitProductAllocation(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.bniPopsResubmitProductAllocation({
            "corporateId":"BNI_SIT",
            "userId":"WTI_MAKER1",
            "transactionReferenceNo":"201809181708919534",
            "SONumber":""
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testInquiryVirtualAccountTransaction(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.inquiryVirtualAccountTransaction({
            "corporateId":"BNI_SIT",
            "userId":"WTI_MAKER1",
            "virtualAccountNo":"8310000011112323",
            "fromDate":"20161015",
            "toDate":"20201015"
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testUpdateVirtualAccount(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.updateVirtualAccount({
            "corporateId":"BNI_SIT",
            "userId":"WTI_MAKER1",
            "companyCode":"8310",
            "virtualAccountNo":"8310888800009999",
            "virtualAccountName":"SHORT NAME",
            "virtualAccountTypeCode":"7",
            "billingAmount":"100000",
            "varAmount1":"",
            "varAmount2":"",
            "expiryDate":"20201120",
            "expiryTime":"10:10:10",
            "mobilePhoneNo":"08712717272",
            "statusCode":"1"
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testCreateVirtualAccount(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.createVirtualAccount({
            "corporateId":"BNI_SIT",
            "userId":"WTI_MAKER1",
            "companyCode":"98800011",
            "virtualAccountNo":"16623254",
            "virtualAccountName":"Agus KEREN1",
            "virtualAccountTypeCode":"7",
            "billingAmount":"800000",
            "varAmount1":"200000",
            "varAmount2":"120000",
            "expiryDate":"20201021",
            "expiryTime":"11:09:08",
            "mobilePhoneNo":"08432432432",
            "statusCode":"1"
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testBillingPayment(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.billingPayment({
            "corporateId":"BNI_SIT",
            "userId":"WTI_MAKER1",
            "debitedAccountNo":"115208364",
            "institution":"MPN",
            "payeeName":"asdfasdf",
            "customerInformation1":"111222122212333",
            "customerInformation2":"",
            "customerInformation3":"",
            "customerInformation4":"",
            "customerInformation5":"",
            "billPresentmentFlag":"N",
            "remitterRefNo":"1123123213",
            "finalizePaymentFlag":"Y",
            "beneficiaryRefNo":"",
            "notificationFlag":"N",
            "beneficiaryEmail":"",
            "transactionInstructionDate":"20231102",
            "amountCurrency":"IDR",
            "amount":"2000000"
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testGetPaymentStatus(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.getPaymentStatus({
            "corporateId":"BNI_SIT",
            "userId":"WTI_MAKER1",
            "transactionReferenceNo":"20230704114212237477",
            "remitterReferenceNo":""
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testInhouseTransfer(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.inhouseTransfer({
            "corporateId":"companymb",
            "userId":"jenomaker",
            "debitedAccountNo":"115208364",
            "amountCurrency":"IDR",
            "amount":"200000",
            "treasuryReferenceNo":"",
            "transactionPurposeCode":"2012",
            "remark1":"transfer inhouse",
            "remark2":"api",
            "remark3":"",
            "remitterReferenceNo":"",
            "finalizePaymentFlag":"N",
            "beneficiaryReferenceNo":"",
            "toAccountNo":"113183203",
            "notificationFlag":"N",
            "beneficiaryEmail":"",
            "transactionInstructionDate":"20190905",
            "docUniqueId":""
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testInquiryBNIPOPSProductAllocation(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.inquiryBNIPOPSProductAllocation({
            "corporateId": "BNI_SIT",
            "userId": "WTI_MAKER1",
            "debitAccountNo": "115208364",
            "salesOrganizationCode": "1002",
            "distributionChannelCode": "10",
            "productCode": "04",
            "shipTo": "1123123",
            "scheduleAggreementNo": "118282812",
            "debitOrCreditNoteNo": "123231",
            "productInformationDetail": [
                {
                    "materialCode": "A040900001",
                    "trip": "1123123",
                    "quantity": "100",
                    "deliveryDate": "20231109",
                    "transportir": ""
                }
            ]
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testOnlineTransfer(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.onlineTransfer({
            "corporateId": "BNI_SIT",
            "userId": "WTI_MAKER1",
            "debitedAccountNo": "1000599764",
            "amountCurrency": "IDR",
            "amount": "86000",
            "treasuryReferenceNo": "",
            "chargeTo": "OUR",
            "remark1": "OT-RMK1",
            "remark2": "OT-RMK2",
            "remark3": "OT-RMK3",
            "remitterReferenceNo": "UYOT26092316",
            "finalizePaymentFlag": "Y",
            "beneficiaryReferenceNo": "BEN2022090OT253",
            "beneficiaryAccountNo": "123456789",
            "beneficiaryBankCode": "014",
            "beneficiaryBankName": "BANK BCA",
            "notificationFlag": "Y",
            "beneficiaryEmail": "wide.uatbeneficiary@gmail.com",
            "transactionInstructionDate": "20231102"
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testTransferInternational(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.transferInternational({
            "corporateId": "BNI_SIT",
            "userId": "WTI_MAKER1",
            "debitedAccountNo": "1000599764",
            "amountCurrency": "USD",
            "amount": "10.55",
            "treasuryReferenceNo": "",
            "chargeTo": "OUR",
            "remark1": "INT TRF RMK1",
            "remark2": "INT TRF RMK2",
            "remark3": "INT TRF RMK3",
            "remitterReferenceNo": "UYY26092023009",
            "finalizePaymentFlag": "Y",
            "beneficiaryReferenceNo": "BENHYUDTVGAVD",
            "beneficiaryAccountNo": "11123123",
            "beneficiaryAccountName": "Janifree",
            "beneficiaryAddress1": "MUNICH",
            "beneficiaryAddress2": "GERMANY",
            "beneficiaryAddress3": "",
            "organizationDirectoryCode": "BIC",
            "beneficiaryBankCode": "SOGEDEFFXXX",
            "beneficiaryBankName": "SOCIETE GENERALE - FRANKFURT",
            "beneficiaryBankBranchName": "",
            "beneficiaryBankAddress1": "",
            "beneficiaryBankAddress2": "",
            "beneficiaryBankAddress3": "",
            "beneficiaryBankCountryName": "GERMANY",
            "correspondentBankName": "",
            "identicalStatusFlag": "N",
            "beneficiaryResidentshipCode": "ID",
            "beneficiaryCitizenshipCode": "ID",
            "beneficiaryCategoryCode": "C9",
            "transactorRelationship": "Y",
            "transactionPurposeCode": "2012",
            "transactionDescription": "TRX DESC",
            "notificationFlag": "N",
            "beneficiaryEmail": "",
            "transactionInstructionDate": "20231102",
            "docUniqueId": ""
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testTransferLLG(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.transferLLG({
           "corporateId": "BNI_SIT",
            "userId": "WTI_MAKER1",
            "debitedAccountNo": "1000599764",
            "amountCurrency": "IDR",
            "amount": "960000",
            "treasuryReferenceNo": "",
            "chargeTo": "OUR",
            "remark1": "LLG-RMK1",
            "remark2": "LLG-RMK2",
            "remark3": "LLG-RMK3",
            "remitterReferenceNo": "UYY26092023005",
            "finalizePaymentFlag": "Y",
            "beneficiaryReferenceNo": "BEN202210LLG141",
            "beneficiaryAccountNo": "111282623",
            "beneficiaryAccountName": "PAK BUDI",
            "beneficiaryAddress1": "BENE ADDRESS1",
            "beneficiaryAddress2": "BENE ADDRESS2",
            "beneficiaryAddress3": "BENE ADDRESS3",
            "beneficiaryResidentshipCountryCode": "ID",
            "beneficiaryCitizenshipCountryCode": "ID",
            "beneficiaryType": "1",
            "beneficiaryBankCode": "CENAIDJA",
            "beneficiaryBankName": "BANK CENTRAL ASIA",
            "beneficiaryBankBranchCode": "0391",
            "beneficiaryBankBranchName": "",
            "beneficiaryBankCityName": "WIL. KOTA JAKARTA PUSAT",
            "notificationFlag": "Y",
            "beneficiaryEmail": "wide.uatbeneficiary@gmail.com",
            "transactionInstructionDate": "20231102"
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testTransferRTGS(self):
        print('\n============================================')
        bni_direct = BNIDIRECT(self.client)
        res = bni_direct.transferRTGS({
            "corporateId": "companymb",
            "userId": "jenomaker",
            "debitedAccountNo": "115208364",
            "amountCurrency": "IDR",
            "amount": "100000001",
            "treasuryReferenceNo": "",
            "chargeTo": "BEN",
            "remark1": "coba",
            "remark2": "rtgs",
            "remark3": "1",
            "remitterReferenceNo": "",
            "finalizePaymentFlag": "Y",
            "beneficiaryReferenceNo": "",
            "beneficiaryAccountNo": "11128281223",
            "beneficiaryAccountName": "TEST rtgs TRF",
            "beneficiaryAddress1": "asdfadsf",
            "beneficiaryAddress2": "afefef",
            "beneficiaryAddress3": "ddfdf",
            "beneficiaryResidentshipCountryCode": "ID",
            "beneficiaryCitizenshipCountryCode": "ID",
            "beneficiaryBankCode": "BMRIIDJA",
            "beneficiaryBankName": "BANK MANDIRI",
            "beneficiaryBankBranchCode": "0391",
            "beneficiaryBankBranchName": "adsfadf",
            "beneficiaryBankCityName": "jakarta pusat",
            "notificationFlag": "N",
            "beneficiaryEmail": "",
            "transactionInstructionDate": "20230505"
        })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')