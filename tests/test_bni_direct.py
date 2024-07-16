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