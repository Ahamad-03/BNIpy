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

    def testBniPopsResubmitCashAndCarry(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.bniPopsResubmitCashAndCarry({
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "transactionReferenceNo": "20240226143153233651", 
            "SONumber": ""
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testBniPopsResubmitProductAllocation(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.bniPopsResubmitProductAllocation({
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "transactionReferenceNo": "202402261600016789", 
            "SONumber": "" 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testCreateVirtualAccount(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.createVirtualAccount({
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "companyCode": "7775", 
            "virtualAccountNo": "819283746658", 
            "virtualAccountName": "VA Test 1", 
            "virtualAccountTypeCode": "2", 
            "billingAmount": "800000", 
            "varAmount1": "200000", 
            "varAmount2": "120000", 
            "expiryDate": "20240228", 
            "expiryTime": "11:09:07", 
            "mobilePhoneNo": "08432432432", 
            "statusCode": "1" 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testUpdateVirtualAccount(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.updateVirtualAccount({
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "companyCode": "7775", 
            "virtualAccountNo": "7775129284933441", 
            "virtualAccountName": "VA Test WTI", 
            "virtualAccountTypeCode": "2", 
            "billingAmount": "800000", 
            "varAmount1": "200000", 
            "varAmount2": "120000", 
            "expiryDate": "20240228", 
            "expiryTime": "10:10:10", 
            "mobilePhoneNo": "08432432432", 
            "statusCode": "2" 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testInquiryVirtualAccountTransaction(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.inquiryVirtualAccountTransaction({
            "corporateId":"BNI_UAT", 
            "userId":"BNI_MAKER4", 
            "virtualAccountNo":"7775129284933441", 
            "fromDate":"20230101", 
            "toDate":"20240226" 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testBulkGetStatus(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.bulkGetStatus({
            "corporateId":"BNI_UAT", 
            "userId":"BNI_MAKER4", 
            "fileRefNo":"20230616103436758", 
            "apiRefNo":"ALL_MIXAG" 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testInquiryAccountBalance(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.balanceInquiry({
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "accountList": [ 
                "1000507841", 
                "108101611" 
            ] 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testInquiryForexRate(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.inquiryForexRate({
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "currencyList": [ 
                "USD", 
                "EUR" 
            ]  
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testBulkPaymentMixed(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.bulkPaymentMixed({
            "corporateId": "BNI_UAT",
            "userId": "BNI_MAKER4",
            "apiRefNo": "BLKTRX027FEB2024000003",
            "instructionDate": "20240227",
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
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testPayrollMixed(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.payrollMixed({
            "corporateId": "companymb",
            "userId": "jenomaker",
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
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testDomestivSingleBIFastTransfer(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.domestivSingleBIFastTransfer({
            "corporateId": "BNI_UAT",
            "userId": "BNI_MAKER4", 
            "debitedAccountNo": "108098391", 
            "amountCurrency": "IDR", 
            "amount": "500000", 
            "exchangeRateCode": "Cr", 
            "treasuryReferenceNo": "", 
            "chargeTo": "OUR", 
            "remark1": "BIFast-RMK1", 
            "remark2": "BIFast-RMK1", 
            "remark3": "BIFast-RMK1", 
            "remitterReferenceNo": "REM11OPTYERT0", 
            "finalizePaymentFlag": "Y", 
            "beneficiaryReferenceNo": "BEN11OPDTAS9", 
            "usedProxy": "N", 
            "beneficiaryAccountNo": "9832132281", 
            "proxyId": "", 
            "beneficiaryBankCode": "CENAIDJA", 
            "beneficiaryBankName": "Bank BCA", 
            "notificationFlag": "N", 
            "beneficiaryEmail": "", 
            "transactionInstructionDate": "20240226", 
            "transactionPurposeCode": "00"
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testInquiryBIFastBeneficiaryName(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.inquiryBIFastBeneficiaryName({
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "usedProxy": "N", 
            "beneficiaryAccountNo": "9832132281", 
            "proxyId": "", 
            "beneficiaryBankCode": "CENAIDJA"
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testSingleBulkPayment(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.singleBulkPayment({
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "apiRefNo": "API-REF-BLK-X9", 
            "instructionDate": "20240229", 
            "session": "1", 
            "serviceType": "SBMXD", 
            "isSTP": "N", 
            "transactionType": "D", 
            "remark": "Single To Bulk Payment Mixed From API", 
            "accountNmValidation": "N", 
            "transactionDetail": [ 
                                    { 
                                        "creditAcctNo": "114479721", 
                                        "creditAcctNm": "BULOG4", 
                                        "amount": "100", 
                                        "treasury": "", 
                                        "remark1": "RMK1", 
                                        "remark2": "RMK2", 
                                        "remark3": "RMK3", 
                                        "benAddr1": "BENADDR1", 
                                        "benAddr2": "BENADDR2", 
                                        "benAddr3": "BENADDR3", 
                                        "benBankCode": "BIC|ABBYGB2LXXX", 
                                        "benBankNm": "Abbey National", 
                                        "benBranchNm": "Abbey National Branch 2 Triton Square", 
                                        "benBankAddr1": "BENBANKADDR1", 
                                        "benBankAddr2": "BENBANKADDR2", 
                                        "benBankAddr3": "BENBANKADDR3", 
                                        "benBankCityNm": "BENBANKCITY", 
                                        "benBankCountryNm": "United Kingdom", 
                                        "benResidenceCd": "GB", 
                                        "benCountryCd": "GB", 
                                        "benEmail": "wide.uatbeneficiary@gmail.com", 
                                        "benPhone": "085232323", 
                                        "benFax": "", 
                                        "correspondentBank": "", 
                                        "purposeCode": "2012", 
                                        "affiliate": "N", 
                                        "identical": "N", 
                                        "benCategory": "C9", 
                                        "lldDescription": "LLDDESC", 
                                        "orderPartyRefNo": "REM77812HYFRK", 
                                        "finalizePayment": "N", 
                                        "counterPartyRefNo": "BEN77812HYFRK", 
                                        "extraDetail1": "EXTDET1", 
                                        "extraDetail2": "EXTDET2", 
                                        "extraDetail3": "EXTDET3", 
                                        "extraDetail4": "EXTDET4", 
                                        "extraDetail5": "EXTDET5", 
                                        "typeCode": "", 
                                        "mixedServiceCode": "IFT", 
                                        "mixedCurrency": "USD", 
                                        "mixedDebitAcctNo": "315592342", 
                                        "mixedChargeTo": "OUR", 
                                        "mixedRemCountryCode": "ID", 
                                        "mixedRemCitizenCode": "ID", 
                                        "mixedRemCategory": "C9", 
                                        "proxyId": "", 
                                        "proxyFlag": "" 
                                    } 
                                ] 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testSinglePayroll(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.singlePayroll({
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "apiRefNo": "API-REF-PROLL-X9", 
            "instructionDate": "20240229", 
            "session": "1", 
            "serviceType": "SPMXD", 
            "isSTP": "N", 
            "transactionType": "D", 
            "remark": "Single To Payroll Mixed From API", 
            "accountNmValidation": "N", 
            "transactionDetail": [ 
                { 
                    "creditAcctNo": "114479721", 
                    "creditAcctNm": "BULOG4", 
                    "amount": "100", 
                    "treasury": "", 
                    "remark1": "RMK1", 
                    "remark2": "RMK2", 
                    "remark3": "RMK3", 
                    "benAddr1": "BENADDR1", 
                    "benAddr2": "BENADDR2", 
                    "benAddr3": "BENADDR3", 
                    "benBankCode": "BIC|ABBYGB2LXXX", 
                    "benBankNm": "Abbey National", 
                    "benBranchNm": "Abbey National Branch 2 Triton Square", 
                    "benBankAddr1": "BENBANKADDR1", 
                    "benBankAddr2": "BENBANKADDR2", 
                    "benBankAddr3": "BENBANKADDR3", 
                    "benBankCityNm": "BENBANKCITY", 
                    "benBankCountryNm": "United Kingdom", 
                    "benResidenceCd": "GB", 
                    "benCountryCd": "GB", 
                    "benEmail": "wide.uatbeneficiary@gmail.com", 
                    "benPhone": "085232323", 
                    "benFax": "", 
                    "correspondentBank": "", 
                    "purposeCode": "2012", 
                    "affiliate": "N", 
                    "identical": "N", 
                    "benCategory": "C9", 
                    "lldDescription": "LLDDESC", 
                    "orderPartyRefNo": "REM77812HYFRK", 
                    "finalizePayment": "N", 
                    "counterPartyRefNo": "BEN77812HYFRK", 
                    "extraDetail1": "EXTDET1", 
                    "extraDetail2": "EXTDET2", 
                    "extraDetail3": "EXTDET3", 
                    "extraDetail4": "EXTDET4", 
                    "extraDetail5": "EXTDET5", 
                    "typeCode": "", 
                    "mixedServiceCode": "IFT", 
                    "mixedCurrency": "USD", 
                    "mixedDebitAcctNo": "315592342", 
                    "mixedChargeTo": "OUR", 
                    "mixedRemCountryCode": "ID", 
                    "mixedRemCitizenCode": "ID", 
                    "mixedRemCategory": "C9", 
                    "proxyId": "", 
                    "proxyFlag": "" 
                } 
            ] 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testSingleBulkPaymentSubmit(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.singleBulkPaymentSubmit({
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "apiRefNo": "API-REF-BLK-Y0" 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testSinglePayrollSubmit(self):
        print('\n============================================')
        bni_direct = BNIDirect(self.client)
        res = bni_direct.singlePayrollSubmit({
            "corporateId": "BNI_UAT", 
            "userId": "BNI_MAKER4", 
            "apiRefNo": "API-REF-PROLL-Y0" 
        })
        data = res['requestStatus']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')