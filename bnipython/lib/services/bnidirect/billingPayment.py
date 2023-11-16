from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateSignature, getTimestamp, generateBniDirectKey
from bnipython.lib.util.response import responseBniDirect

def billingPayment(params):
        httpClient = HttpClient();
        timeStamp = getTimestamp()
        payload = {
                'corporateId': params['body']['corporateId'],
                'userId': params['body']['userId'],
                'debitedAccountNo': params['body']['debitedAccountNo'],
                'institution': params['body']['institution'],
                'payeeName': params['body']['payeeName'],
                'customerInformation1': params['body']['customerInformation1'],
                'customerInformation2': params['body']['customerInformation2'],
                'customerInformation3': params['body']['customerInformation3'],
                'customerInformation4': params['body']['customerInformation4'],
                'customerInformation5': params['body']['customerInformation5'],
                'billPresentmentFlag': params['body']['billPresentmentFlag'],
                'remitterRefNo': params['body']['remitterRefNo'],
                'finalizePaymentFlag': params['body']['finalizePaymentFlag'],
                'beneficiaryRefNo': params['body']['beneficiaryRefNo'],
                'notificationFlag': params['body']['notificationFlag'],
                'beneficiaryEmail': params['body']['beneficiaryEmail'],
                'transactionInstructionDate': params['body']['transactionInstructionDate'],
                'amountCurrency': params['body']['amountCurrency'],
                'amount': params['body']['amount'],
        }
        payloadSignature = {**payload, **{ 'timestamp': timeStamp }}
        signature = generateSignature(
            {'body': payloadSignature, 'apiSecret': params['config']['client']['apiSecret']})
        bniDirectApiKey = generateBniDirectKey({
            'corporateId': payload['corporateId'],
            'userId': payload['userId'],
            'bniDirectKey': params['config']['client']
        })
        res = httpClient.requestV2BniDirect({
            'method': 'POST',
            'apiKey': params['config']['client']['apiKey'],
            'accessToken': params['config']['token'],
            'url': f'{params['config']['baseUrl']}',
            'path': '/bnidirect/api/Billing/Payment',
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload,
            'bniDirectKey': 'dc8f7943e027345677c7dade0441936c3bb3f8d697ef8f7b28ae5dfdeea78dd1',
            # 'bniDirectKey': bniDirectApiKey
        })
        return responseBniDirect(params={'res': res})