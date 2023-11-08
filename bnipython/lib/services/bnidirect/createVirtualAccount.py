from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateSignature, getTimestamp, generateBniDirectKey
from bnipython.lib.util.response import responseBniDirect

def createVirtualAccount(params):
        httpClient = HttpClient();
        timeStamp = getTimestamp()
        payload = {
                'corporateId': params['body']['corporateId'],
                'userId': params['body']['userId'],
                'companyCode': params['body']['companyCode'],
                'virtualAccountNo': params['body']['virtualAccountNo'],
                'virtualAccountName': params['body']['virtualAccountName'],
                'virtualAccountTypeCode': params['body']['virtualAccountTypeCode'],
                'billingAmount': params['body']['billingAmount'],
                'varAmount1': params['body']['varAmount1'],
                'varAmount2': params['body']['varAmount2'],
                'expiryDate': params['body']['expiryDate'],
                'expiryTime': params['body']['expiryTime'],
                'mobilePhoneNo': params['body']['mobilePhoneNo'],
                'statusCode': params['body']['statusCode'],
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
            'path': '/bnidirect/api/VirtualAccount/Create',
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload,
            'bniDirectKey': bniDirectApiKey
        })
        return responseBniDirect(params={'res': res})