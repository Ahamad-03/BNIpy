from bnipython.lib.api.rdn import RDN
from bnipython.lib.util import constants
import unittest
from bnipython.lib.bniClient import BNIClient

class TestRDN(unittest.TestCase):
    client = BNIClient({
        'env': 'sandbox-dev',
        # 'appName': constants.APP_NAME,
        'clientId': constants.CLIENT_ID_ENCRYPT,
        'clientSecret': constants.CLIENT_SECRET_ENCRYPT,
        'apiKey': constants.API_KEY_ENCRYPT,
        'apiSecret': constants.API_SECRET_ENCRYPT
    })

    def testFaceRecog(self):
        print('\n==============================================')
        rekening_dana_nasabah = RDN(self.client)
        res = rekening_dana_nasabah.faceRecognition({
            'companyId': 'SANDBOX',
            'parentCompanyId': 'STI_CHS',
            'firstName': 'MOHAMMAD',  
            'middleName': 'BAQER',  
            'lastName': 'ZALQAD', 
            'idNumber': '0141111121260118', 
            'birthDate': '29-09-2021', 
            'birthPlace': 'BANDUNG', 
            'gender': 'M', 
            'cityAddress': 'Bandung', 
            'stateProvAddress': 'Jawa Barat', 
            'addressCountry': 'ID', 
            'streetAddress1': 'bandung', 
            'streetAddress2': 'bandung', 
            'postCodeAddress': '40914', 
            'country': 'ID',
            'selfiePhoto': '29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuP'
        })
        data = res['response']['responseCode']
        self.assertEqual(data, '0001')
        print('\033[92m should return responseCode 0001 \033[0m')
        
    def testRegisterInvestor(self):
        print('\n==============================================')
        rekening_dana_nasabah = RDN(self.client)
        res = rekening_dana_nasabah.registerInvestor({
            'companyId': 'SANDBOX',
            'parentCompanyId': 'STI_CHS',
            'uuidFaceRecog': '40FCB72E71D35C81',
            'title': '01',
            'firstName': 'Agus',
            'middleName': '',
            'lastName': 'Saputra',
            'optNPWP': '1',
            'npwpNum': '001058893408123',
            'nationality': 'ID',
            'domicileCountry': 'ID',
            'religion': '2',
            'birthPlace': 'Semarang',
            'birthDate': '14081982',
            'gender': 'M',
            'isMarried': 'S',
            'motherMaidenName': 'Dina Maryati',
            'jobCode': '01',
            'education': '07',
            'idType': '01',
            'idNumber': '4147016201959998',
            'idIssuingCity': 'Jakarta Barat',
            'idExpiryDate': '26102099',
            'addressStreet': 'Jalan Mawar Melati',
            'addressRtRwPerum': '003009Sentosa',
            'addressKel': 'Cengkareng Barat',
            'addressKec': 'Cengkareng/Jakarta Barat',
            'zipCode': '11730',
            'homePhone1': '0214',
            'homePhone2': '7459',
            'officePhone1': '',
            'officePhone2': '',
            'mobilePhone1': '0812',
            'mobilePhone2': '12348331',
            'faxNum1': '',
            'faxNum2': '',
            'email': 'agus.saputra@gmail.com',
            'monthlyIncome': '8000000',
            'branchOpening': '0259',
            'institutionName': 'PT. BNI SECURITIES',
            'sid': 'IDD280436215354',
            'employerName': 'Salman',
            'employerAddDet': 'St Baker',
            'employerAddCity': 'Arrandelle',
            'jobDesc': '13',
            'ownedBankAccNo': '0337109074',
            'idIssuingDate': '10122008'
        })
        data = res['response']['responseCode']
        self.assertEqual(data, '0001')
        print('\033[92m should return responseCode 0001 \033[0m')