from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateSignature, getTimestamp, generateBniDirectKey
from bnipython.lib.util.response import responseBniDirect

def inquiryAccountStatement(params):
        httpClient = HttpClient();
        timeStamp = getTimestamp()
        payload = {
                'corporateId': params['body']['corporateId'],
                'userId': params['body']['userId'],
                'fromDate': params['body']['fromDate'],
                'toDate': params['body']['toDate'],
                'transactionType': params['body']['transactionType'],
                'accountList': params['body']['accountList'],
        }
        payloadSignature = {**payload, **{ 'timestamp': timeStamp }}
        signature = generateSignature(
            {'body': payloadSignature, 'apiSecret': params['config']['client']['apiSecret']})
        bniDirectApiKey = generateBniDirectKey({
            'corporateId': params['body']['corporateId'],
            'userId': params['body']['userId'],
            'bniDirectKey': params['config']['client']['bniDirectKey']
        })
        res = httpClient.requestV2BniDirect({
            'method': 'POST',
            'apiKey': params['config']['client']['apiKey'],
            'accessToken': params['config']['token'],
            'url': f'{params['config']['baseUrl']}',
            'path': '/bnidirect/api/Account/InquiryAccountStatement',
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload,
            'bniDirectKey': bniDirectApiKey
        })
        return responseBniDirect(params={'res': res})