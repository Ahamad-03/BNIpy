from bnipython.lib.api.bniDirect import BNIDirect
from bnipython.lib.util import constants
import unittest
from bnipython.lib.bniClient import BNIClient
import json


class TestBNIDirect(unittest.TestCase):
    client = BNIClient({
        'env': 'sandbox',
        'appName': constants.APP_NAME,
        'clientId': constants.CLIENT_ID_ENCRYPT,
        'clientSecret': constants.CLIENT_SECRET_ENCRYPT,
        'apiKey': constants.API_KEY_ENCRYPT,
        'apiSecret': constants.API_SECRET_ENCRYPT,
        'bniDirectApiKey': constants.BNI_DIRECT_KEY_ENCRYPT
    })

    def testCreateBillingMPNG2(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.createMPNG2BillingID({ 
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "npwp": "312312309013000", 
            "taxPayerName": "NAMA NPWP", 
            "taxPayerAddress1": "ALAMAT 1", 
            "taxPayerAddress2": "", 
            "taxPayerAddress3": "", 
            "taxPayerCity": "JAKARTA", 
            "NOP": "", 
            "MAPCode": "411211", 
            "depositTypeCode": "100", 
            "wajibPungutNPWP": "", 
            "wajibPungutName": "", 
            "wajibPungutAddress1": "", 
            "wajibPungutAddress2": "", 
            "wajibPungutAddress3": "", 
            "participantId": "", 
            "assessmentTaxNumber": "", 
            "amountCurrency": "IDR", 
            "amount": "2000000", 
            "monthFrom": "12", 
            "monthTo": "12", 
            "year": "2020", 
            "confirmNumber": "0", 
            "traceId": "", 
            "kelurahan": "", 
            "kecamatan": "", 
            "provinsi": "", 
            "kota": "" 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testInquiryNPWP(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.inquiryNPWP({ 
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "npwp": "312312309013000", 
            "NOP": "", 
            "MAPCode": "411211", 
            "depositTypeCode": "100", 
            "currency": "IDR" 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testInquiryInHouseAndVABeneficiaryName(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.inquiryInHouseAndVABeneficiaryName({ 
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "accountNo":"113183203" 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testInquiryLLGRTGSOnlineBenefiacyName(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.inquiryLLGRTGSOnlineBenefiacyName({ 
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "beneficiaryAccountNo": "10541448", 
            "beneficiaryBankCode": "014" 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testInquiryAccountStatement(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.inquiryAccountStatement({ 
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "fromDate": "20240227", 
            "toDate": "20240227", 
            "transactionType": "All", 
            "accountList": [ 
                "164117161" 
            ] 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testInquiryBilling(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.inquiryBilling({ 
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "debitedAccountNo": "108098391", 
            "institution": "MPN", 
            "customerInformation1": "172837627222376", 
            "customerInformation2": "", 
            "customerInformation3": "", 
            "customerInformation4": "", 
            "customerInformation5": "" 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testInquiryBNIPopsCashAndCarry(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.inquiryBNIPopsCashAndCarry({ 
            "corporateId":"BNI_UAT", 
            "userId":"BNI_MAKER4", 
            "debitAccountNo":"108098391", 
            "salesOrganizationCode":"2201", 
            "distributionChannelCode":"10", 
            "productCode":"04", 
            "shipTo":"700258", 
            "debitOrCreditNoteNo":"", 
            "productInformationDetail": 
                [
                    { 
                    "materialCode":"A040900001", 
                    "trip":"1", 
                    "quantity":"8", 
                    "deliveryDate":"20240228", 
                    "transportir":"" 
                    }
                ] 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testInquiryBNIPopsProductAllocation(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.inquiryBNIPopsProductAllocation({ 
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "debitAccountNo": "108098391", 
            "salesOrganizationCode": "2201", 
            "distributionChannelCode": "10", 
            "productCode": "04", 
            "shipTo": "112312", 
            "scheduleAggreementNo": "124379", 
            "debitOrCreditNoteNo": "123456789012346789", 
            "productInformationDetail": [ 
                    { 
                        "materialCode": "A040900001", 
                        "trip": "1", 
                        "quantity": "1", 
                        "deliveryDate": "20240228", 
                        "transportir": "AAA" 
                    } 
                ] 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testGetPaymentStatus(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.getPaymentStatus({ 
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "transactionReferenceNo": "20240227083050233689", 
            "remitterReferenceNo": "" 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testInhouseTransfer(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.inhouseTransfer({
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "debitedAccountNo": "108098391", 
            "amountCurrency": "IDR", 
            "amount": "100", 
            "treasuryReferenceNo": "", 
            "transactionPurposeCode": "", 
            "remark1": "IH-TRF-RMK1", 
            "remark2": "IH-TRF-RMK2", 
            "remark3": "IH-TRF-RMK3", 
            "remitterReferenceNo": "REM20230704IHKG", 
            "finalizePaymentFlag": "Y", 
            "beneficiaryReferenceNo": "BEN20230704IHKG", 
            "toAccountNo": "115208364", 
            "notificationFlag": "Y", 
            "beneficiaryEmail": "wide.uatbeneficiary@gmail.com", 
            "transactionInstructionDate": "20240227", 
            "docUniqueId": ""
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testLLGTransfer(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.LLGTransfer({
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "debitedAccountNo": "108098391", 
            "amountCurrency": "IDR", 
            "amount": "960000", 
            "treasuryReferenceNo": "", 
            "chargeTo": "OUR", 
            "remark1": "LLG-RMK1", 
            "remark2": "LLG-RMK2", 
            "remark3": "LLG-RMK3", 
            "remitterReferenceNo": "REM20226RLLG5O8", 
            "finalizePaymentFlag": "Y", 
            "beneficiaryReferenceNo": "BEN20226RLLG18", 
            "beneficiaryAccountNo": "111282623", 
            "beneficiaryAccountName": "PAK BUDI", 
            "beneficiaryAddress1": "BENE ADDRESS1", 
            "beneficiaryAddress2": "BENE ADDRESS2", 
            "beneficiaryAddress3": "BENE ADDRESS3", 
            "beneficiaryResidentshipCountryCode": "AT", 
            "beneficiaryCitizenshipCountryCode": "AT",
            "beneficiaryType": "1", 
            "beneficiaryBankCode": "CENAIDJA", 
            "beneficiaryBankName": "BANK CENTRAL ASIA", 
            "beneficiaryBankBranchCode": "0391", 
            "beneficiaryBankBranchName": "", 
            "beneficiaryBankCityName": "WIL. KOTA JAKARTA PUSAT", 
            "notificationFlag": "Y", 
            "beneficiaryEmail": "wide.uatbeneficiary@gmail.com", 
            "transactionInstructionDate": "20240227" 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testRTGSTransfer(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.RTGSTransfer({
            "corporateId":"BNI_UAT", 
            "userId":"BNI_MAKER4", 
            "debitedAccountNo":"108098391", 
            "amountCurrency":"IDR", 
            "amount":"100050000", 
            "treasuryReferenceNo":"", 
            "chargeTo":"OUR", 
            "remark1":"RTGS-RMK1", 
            "remark2":"RTGS-RMK2", 
            "remark3":"RTGS-RMK3", 
            "remitterReferenceNo":"REM20221RTGS07E5", 
            "finalizePaymentFlag":"Y", 
            "beneficiaryReferenceNo":"BEN20221RTGS07E4", 
            "beneficiaryAccountNo":"10529373", 
            "beneficiaryAccountName":"PAK CHANDRA", 
            "beneficiaryAddress1":"BENE ADD 1", 
            "beneficiaryAddress2":"BENE ADD 2", 
            "beneficiaryAddress3":"BENE ADD 3",
            "beneficiaryResidentshipCountryCode":"ID", 
            "beneficiaryCitizenshipCountryCode":"ID", 
            "beneficiaryBankCode":"CENAIDJA", 
            "beneficiaryBankName":"BANK CENTRAL ASIA", 
            "beneficiaryBankBranchCode":"0391", 
            "beneficiaryBankBranchName":"", 
            "beneficiaryBankCityName":"WIL. KOTA JAKARTA PUSAT", 
            "notificationFlag":"Y", 
            "beneficiaryEmail":"wide.uatbeneficiary@gmail.com", 
            "transactionInstructionDate":"20240227"
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testOnlineTransfer(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.onlineTransfer({
            "corporateId":"BNI_UAT", 
            "userId":"BNI_MAKER4", 
            "debitedAccountNo":"108098391", 
            "amountCurrency":"IDR", 
            "amount":"860000", 
            "treasuryReferenceNo":"", 
            "chargeTo":"OUR", 
            "remark1":"OT-RMK1", 
            "remark2":"OT-RMK2", 
            "remark3":"OT-RMK3", 
            "remitterReferenceNo":"REM2022090OT54", 
            "finalizePaymentFlag":"Y", 
            "beneficiaryReferenceNo":"BEN2022090OT54", 
            "beneficiaryAccountNo":"773723561", 
            "beneficiaryBankCode":"014", 
            "beneficiaryBankName":"BANK SULUTGO", 
            "notificationFlag":"Y", 
            "beneficiaryEmail":"wide.uatbeneficiary@gmail.com", 
            "transactionInstructionDate":"20240227" 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testInternationalTransfer(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.internationalTransfer({
           "corporateId":"BNI_UAT", 
            "userId":"BNI_MAKER4", 
            "debitedAccountNo":"315592342", 
            "amountCurrency":"USD", 
            "amount":"100.55", 
            "treasuryReferenceNo":"", 
            "chargeTo":"OUR", 
            "remark1":"INT TRF RMK1", 
            "remark2":"INT TRF RMK2", 
            "remark3":"INT TRF RMK3", 
            "remitterReferenceNo":"REMHYUD200T456", 
            "finalizePaymentFlag":"Y", 
            "beneficiaryReferenceNo":"REMHYUD00F456", 
            "beneficiaryAccountNo":"1000551267", 
            "beneficiaryAccountName":"Janifree", 
            "beneficiaryAddress1":"MUNICH", 
            "beneficiaryAddress2":"GERMANY", 
            "beneficiaryAddress3":"", 
            "organizationDirectoryCode":"BIC", 
            "beneficiaryBankCode":"ABBYGB2LXXX", 
            "beneficiaryBankName":"ABBEY NATIONALE PLC. - LONDON", 
            "beneficiaryBankBranchName":"", 
            "beneficiaryBankAddress1":"", 
            "beneficiaryBankAddress2":"", 
            "beneficiaryBankAddress3":"", 
            "beneficiaryBankCountryName":"GERMANY", 
            "correspondentBankName":"", 
            "identicalStatusFlag":"N", 
            "beneficiaryResidentshipCode":"ID", 
            "beneficiaryCitizenshipCode":"ID", 
            "beneficiaryCategoryCode":"C9", 
            "transactorRelationship":"Y", 
            "transactionPurposeCode":"2012", 
            "transactionDescription":"TRX DESC", 
            "notificationFlag":"Y", 
            "beneficiaryEmail":"janifree.aprisma@gmail.com", 
            "transactionInstructionDate":"20240227", 
            "docUniqueId":"" 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')


    def testBillPayment(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.billPayment({
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "debitedAccountNo": "108098391", 
            "institution": "MPN", 
            "payeeName": "MPN", 
            "customerInformation1": "172837627222376", 
            "customerInformation2": "", 
            "customerInformation3": "", 
            "customerInformation4": "", 
            "customerInformation5": "", 
            "billPresentmentFlag": "N", 
            "remitterRefNo": "REMYUBGEYVFT", 
            "finalizePaymentFlag": "Y", 
            "beneficiaryRefNo": "BENYUBGEYVFEE", 
            "notificationFlag": "Y", 
            "beneficiaryEmail": "janifree.aprisma@gmail.com", 
            "transactionInstructionDate": "20240227", 
            "amountCurrency": "IDR", 
            "amount": "100000" 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testBniPopsCashAndCarry(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.bniPopsCashAndCarry({
            "corporateId":"BNI_UAT", 
            "userId":"BNI_MAKER4", 
            "debitAccountNo":"108098391", 
            "salesOrganizationCode":"2201", 
            "distributionChannelCode":"10", 
            "productCode":"04", 
            "shipTo":"700075", 
            "debitOrCreditNoteNo":"", 
            "productInformationDetail": 
                [
                    { 
                        "materialCode":"A040900001", 
                        "trip":"10", 
                        "quantity":"2", 
                        "deliveryDate":"20240228", 
                        "transportir":"" 
                    }
                ]
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testBniPopsProductAllocation(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.bniPopsProductAllocation({
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "debitAccountNo": "108098391", 
            "salesOrganizationCode": "2201", 
            "distributionChannelCode": "10", 
            "productCode": "04", 
            "shipTo": "701759", 
            "scheduleAggreementNo": "124365", 
            "debitOrCreditNoteNo": "", 
            "productInformationDetail": [ 
                    { 
                        "materialCode": "A040900001", 
                        "trip": "10", 
                        "quantity": "2", 
                        "deliveryDate": "20240228", 
                        "transportir": "AAA" 
                    }, 
                    { 
                        "materialCode": "A040900001", 
                        "trip": "15", 
                        "quantity": "2", 
                        "deliveryDate": "20240228", 
                        "transportir": "AAA"
                    }
                ]
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testInquiryAccountBalance(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.balanceInquiry({
            "corporateId":"companymb",
            "userId":"jenomaker",
            "accountList": ["116952891", "4447"]
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')