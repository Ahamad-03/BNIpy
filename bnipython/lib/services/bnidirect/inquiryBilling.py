from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateSignature, getTimestamp, generateBniDirectKey
from bnipython.lib.util.response import responseBniDirect

def inquiryBilling(params):
        httpClient = HttpClient();
        timeStamp = getTimestamp()
        payload = {
                'corporateId': params['body']['corporateId'],
                'userId': params['body']['userId'],
                'debitedAccountNo': params['body']['debitedAccountNo'],
                'institution': params['body']['institution'],
                'customerInformation1': params['body']['customerInformation1'],
                'customerInformation2': params['body']['customerInformation2'],
                'customerInformation3': params['body']['customerInformation3'],
                'customerInformation4': params['body']['customerInformation4'],
                'customerInformation5': params['body']['customerInformation5'],
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
            'path': '/bnidirect/api/Billing/Inquiry',
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload,
            'bniDirectKey': bniDirectApiKey
        })
        return responseBniDirect(params={'res': res})