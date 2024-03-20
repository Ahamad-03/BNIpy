from bnipython.lib.api.fscm import FSCM
from bnipython.lib.util import constants
import unittest
from bnipython.lib.bniClient import BNIClient
import json

class TestFSCM(unittest.TestCase):
    client = BNIClient({
        'env': 'sandbox-2',
        'appName': constants.APP_NAME,
        'clientId': constants.CLIENT_ID_ENCRYPT,
        'clientSecret': constants.CLIENT_SECRET_ENCRYPT,
        'apiKey': constants.API_KEY_ENCRYPT,
        'apiSecret': constants.API_SECRET_ENCRYPT,
        'bniDirectKey': constants.BNI_DIRECT_KEY_ENCRYPT
    })


    def testSendInvoice(self):
        print('\n============================================')
        fscm = FSCM(self.client)
        res = fscm.sendInvoice({
            "rq_uuid" : "test-uuid-send-invoice",
            "password": "sigbni",
            "doc_no": "INV_TEST111",
            "member_code": "142",
            "due_date": "23/10/2023",
            "amount": "1000",
            "currency" : "IDR",
            "issue_date": "22/10/2023",
            "rq_datetime": "2023-10-23 09:34:00",
            "term_of_payment" : "",
            "comm_code": "7900"
            })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testInquiry(self):
        print('\n============================================')
        fscm = FSCM(self.client)
        res = fscm.inquiry({
            "rq_uuid": "test-uuid-inquiry",
            "comm_code" : "7900",
            "password" : "sigbni",
            "doc_no" : "INV20231023JKL5",
            "rq_datetime" : "2023-01-04 16:50:00",
            "member_code" : "142"
            })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testCheckTransactionPlafond(self):
        print('\n============================================')
        fscm = FSCM(self.client)
        res = fscm.checkTransactionPlafond({
            "rq_uuid":"test-uuid-check",
            "comm_code":"7900",
            "credit_type":"CREDIT",
            "currency":"IDR",
            "rq_datetime":"2023-01-04 13:47:00",
            "member_code":"142",
            "amount":"30000000000"
            })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testCheckLimit(self):
        print('\n============================================')
        fscm = FSCM(self.client)
        res = fscm.checkLimit({
            "rq_uuid" : "test-uuid-check-limit",
            "rq_datetime" : "2021-11-18 10:18:00",
            "password" : "sigbni",
            "member_code" : "142",
            "comm_code" : "7900",
            "currency" : "IDR"
            })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testCheckStopSupply(self):
        print('\n============================================')
        fscm = FSCM(self.client)
        res = fscm.checkStopSupply({
            "rq_uuid":"test-uuid-check-stop-supply",
            "password":"sigbni",
            "member_code":"142",
            "rq_datetime":"2022-11-18 16:50:00",
            "comm_code":"7900",
            "currency" : "IDR",
            "ccy":"",
            "status_member":"1"
            })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testDeleteInvoice(self):
        print('\n============================================')
        fscm = FSCM(self.client)
        res = fscm.deleteInvoice({
            "rq_uuid" : "test-uuid-delete-invoice",
            "password" : "sigbni",
            "doc_no" : "INV_TEST111",
            "member_code" : "142",
            "rq_datetime" : "2023-10-24 08:22:00",
            "comm_code" : "7900"
            })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testPranota(self):
        print('\n============================================')
        fscm = FSCM(self.client)
        res = fscm.praNota({
            "rq_uuid": "rq-test-pranota",
            "password": "sigbni",
            "doc_no": "INVtest-201",
            "member_code": "142",
            "amount": "1000000",
            "currency": "IDR",
            "issue_date": "17/10/2023",
            "rq_datetime": "2023-01-05 09:34:00",
            "term_of_payment" : "2",
            "comm_code": "7900"
            })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')

    def testDeletePranota(self):
        print('\n============================================')
        fscm = FSCM(self.client)
        res = fscm.deletePranota({
            "rq_uuid" : "rq-test-pranota",
            "rq_datetime" : "2023-01-05-09:34:00",
            "password" : "sigbni",
            "member_code" : "142",
            "comm_code" : "7900",
            "doc_no": "INVtest-201",
            "issue_date" :"16/10/2023"
            })
        data = res['requestStatus']
        self.assertEqual(data, '0')
        print('\033[92m should return requestStatus 0 \033[0m')