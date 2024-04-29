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

    # def testGetBankAndCurrencyLimitation(self):
    #     print('\n============================================')
    #     otr_remittance = OTRRemittance(self.client, {'channelId': 'CORPORATE'})
    #     res = otr_remittance.getBankAndCurrencyLimitation()
    #     # print(json.dumps(res, indent=2))
    #     data = res['statusCode']
    #     self.assertEqual(data, 0)
    #     print('\033[92m should return statusCode 0 \033[0m')

    # def testChargesAndRateInquiry(self):
    #     print('\n============================================')
    #     otr_remittance = OTRRemittance(self.client, {'channelId': 'CORPORATE'})
    #     res = otr_remittance.chargesAndRateInquiry(payload={
    #         'orderingId': 'RESTTEST04',
    #         'bic': 'INITU123456',
    #         'serviceType': 'SWIFT',
    #         'sourceCcy': 'SGD',
    #         'orderingCcy': 'USD',
    #         'detailCharges': 'SHA',
    #         'orderingAmount': 5000
    #     })
    #     # print(json.dumps(res, indent=2))
    #     data = res['statusCode']
    #     self.assertEqual(data, 0)
    #     print('\033[92m should return statusCode 0 \033[0m')

    # def testTrackingTransaction(self):
    #     print('\n============================================')
    #     otr_remittance = OTRRemittance(self.client, {'channelId': 'CORPORATE'})
    #     res = otr_remittance.trackingTransaction(payload={
    #         'referenceNumber': 'RESTTEST04',
    #     })
    #     # print(json.dumps(res, indent=2))
    #     data = res['statusCode']
    #     self.assertEqual(data, 0)
    #     print('\033[92m should return statusCode 0 \033[0m')

    # def testTransactionOverbooking(self):
    #     print('\n============================================')
    #     otr_remittance = OTRRemittance(self.client, {'channelId': 'CORPORATE'})
    #     res = otr_remittance.transactionOverbooking(payload={
    #         "referenceNumber": 'string',
    #         "orderingId": 'string',
    #         "orderingBic": 'string',
    #         "orderingName": 'string',
    #         "orderingAddress": 'string',
    #         "orderingEmail": 'string',
    #         "orderingPhoneNumber": 'string',
    #         "beneficiaryAccount": 'string',
    #         "beneficiaryName": 'string',
    #         "beneficiaryAddress": 'string',
    #         "beneficiaryPhoneNumber": 'string',
    #         "accountWithInstCode": 'string',
    #         "accountWithInstBic": 'string',
    #         "accountWithInstName": 'string',
    #         "remittanceInfo": 'string',
    #         "invoiceNumber": 'string',
    #         "invoiceAmount": 1234
    #     })
    #     # print(json.dumps(res, indent=2))
    #     data = res['statusCode']
    #     self.assertEqual(data, 0)
    #     print('\033[92m should return statusCode 0 \033[0m')
