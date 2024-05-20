from bnipython.lib.api.otrRemittance import OTRRemittance
from bnipython.lib.util import constants
import unittest
from bnipython.lib.bniClient import BNIClient
import json


class TestBNIMove(unittest.TestCase):
    client = BNIClient({
        'env': 'dev',
        'appName': constants.APP_NAME,
        'clientId': constants.CLIENT_ID_ENCRYPT,
        'clientSecret': constants.CLIENT_SECRET_ENCRYPT,
        'apiKey': constants.API_KEY_ENCRYPT,
        'apiSecret': constants.API_SECRET_ENCRYPT
    })

    def testGetBankAndCurrencyLimitation(self):
        print('\n============================================')
        otr_remittance = OTRRemittance(self.client, {'channelId': 'CORPORATE'})
        res = otr_remittance.getBankAndCurrencyLimitation(payload={
            "serviceType": "SWIFT",
            "country": "SG"
        })
        # print(json.dumps(res, indent=2))
        data = res['code']
        self.assertEqual(data, "200")
        print('\033[92m should return code 200 \033[0m')

    def testChargesAndRateInquiry(self):
        print('\n============================================')
        otr_remittance = OTRRemittance(self.client, {'channelId': 'CORPORATE'})
        res = otr_remittance.chargesAndRateInquiry(payload={
            'orderingId': 'RESTTEST04',
            'bic': 'INITU123456',
            'serviceType': 'SWIFT',
            'sourceCcy': 'SGD',
            'orderingCcy': 'USD',
            'detailCharges': 'SHA',
            'orderingAmount': 5000
        })
        # print(json.dumps(res, indent=2))
        data = res['code']
        self.assertEqual(data, "200")
        print('\033[92m should return statusCode 200 \033[0m')

    def testTrackingTransaction(self):
        print('\n============================================')
        otr_remittance = OTRRemittance(self.client, {'channelId': 'CORPORATE'})
        res = otr_remittance.trackingTransaction(payload={
            'referenceNumber': 'S10JPUC000008224',
        })
        # print(json.dumps(res, indent=2))
        data = res['code']
        self.assertEqual(data, "200")
        print('\033[92m should return statusCode 200 \033[0m')

    def testTransactionOverbooking(self):
        print('\n============================================')
        otr_remittance = OTRRemittance(self.client, {'channelId': 'CORPORATE'})
        res = otr_remittance.transactionOverbooking(payload={
            "referenceNumber": "GLBS10032959",
            "orderingId": "RESTTEST26",
            "orderingBic": "CITIUS30XXX",
            "orderingName": "Nama",
            "orderingAddress": "Alamatnya",
            "orderingEmail": "nama@initu.com",
            "orderingPhoneNumber": "08091000100",
            "beneficiaryAccount": "72183810",
            "beneficiaryName": "SIAPA YA",
            "beneficiaryAddress": "Alamatmu",
            "beneficiaryPhoneNumber": "08091000101",
            "accountWithInstCode": "A",
            "accountWithInstBic": "CHASUS30XXX",
            "accountWithInstName": "JPMORGAN",
            "remittanceInfo": "PERSONAL",
            "invoiceNumber": "INVOICE001",
            "invoiceAmount": 9000
        }
        )
        # print(json.dumps(res, indent=2))
        data = res['code']
        self.assertEqual(data, "200")
        print('\033[92m should return statusCode 200 \033[0m')
