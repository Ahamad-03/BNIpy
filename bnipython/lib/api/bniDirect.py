from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateBniDirectKey, generateSignature, getTimestamp
from bnipython.lib.util.response import responseBniDirect

class BNIDirect():
    def __init__(self, client):
        self.client = client.config
        self.baseUrl = client.getBaseUrl()
        self.config = client.getConfig()
        self.token = client.getToken()
        self.httpClient = HttpClient()

    def _make_request(self, path, method, timeStamp, payload=None):
        signaturePayload = {**payload, **{ 'timestamp': timeStamp}}
        signature = generateSignature(
            {'body': signaturePayload, 'apiSecret': self.client['apiSecret']}
        )
        bniDirectKey = generateBniDirectKey({
            'corporateId': payload['corporateId'], 
            'userId': payload['userId'], 
            'bniDirectApiKey': self.client['bniDirectApiKey'],
            })
        res = self.httpClient.requestV2BniDirect({
            'method': method,
            'apiKey': self.client['apiKey'],
            'accessToken': self.token,
            'url': f'{self.baseUrl}',
            'path': path,
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload,
            'bniDirectKey': bniDirectKey
        })
        return responseBniDirect(params={'res': res})

    def balanceInquiry(self, payload=None):
        """
        Conducts a charges and rate inquiry.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID #Mandatory.
                - userId (str): User ID #Mandatory.
                - accountList (float): List of Account (1 … n) #Mandatory.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/Account/InquiryBalance'
        return self._make_request(path, method, timeStamp, payload)
