from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateSignature, getTimestamp, generateBniDirectKey
from bnipython.lib.util.response import responseBniDirect

def bulkPaymentMixed(params):
        httpClient = HttpClient();
        timeStamp = getTimestamp()
        payload = {
                'corporateId': params['body']['corporateId'],
                'userId': params['body']['userId'],
                'apiRefNo': params['body']['apiRefNo'],
                'instructionDate': params['body']['instructionDate'],
                'session': params['body']['session'],
                'serviceType': params['body']['serviceType'],
                'debitAcctNo': params['body']['debitAcctNo'],
                'amount': params['body']['amount'],
                'currency': params['body']['currency'],
                'chargeTo': params['body']['chargeTo'],
                'residenceCode': params['body']['residenceCode'],
                'citizenCode': params['body']['citizenCode'],
                'category': params['body']['category'],
                'transactionType': params['body']['transactionType'],
                'accountNmValidation': params['body']['accountNmValidation'],
                'remark': params['body']['remark'],
                'childContent': params['body']['childContent']
        }
        payloadSignature = {**payload, **{ 'timestamp': timeStamp }}
        signature = generateSignature(
            {'body': payloadSignature, 'apiSecret': params['config']['client']['apiSecret']})
        bniDirectKey = generateBniDirectKey({
                'corporateId': params['body']['corporateId'], 
                'userId': params['body']['userId'], 
                'bniDirectKey': params['config']['client']['bniDirectKey']
                })
        res = httpClient.requestV2BniDirect({
            'method': 'POST',
            'apiKey': params['config']['client']['apiKey'],
            'accessToken': params['config']['token'],
            'url': f'{params['config']['baseUrl']}',
            'path': '/bnidirect/api/MassPayment/BulkPaymentMixed',
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload,
            'bniDirectKey': bniDirectKey
        })
        return responseBniDirect(params={'res': res})