from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateSignature, getTimestamp, generateBniDirectKey
from bnipython.lib.util.response import responseBniDirect

def createMpnG2Billing(params):
        httpClient = HttpClient();
        timeStamp = getTimestamp()
        payload = {
                'corporateId': params['body']['corporateId'],
                'userId': params['body']['userId'],
                'npwp': params['body']['npwp'],
                'taxPayerName': params['body']['taxPayerName'],
                'taxPayerAddress1': params['body']['taxPayerAddress1'],
                'taxPayerAddress2': params['body']['taxPayerAddress2'],
                'taxPayerAddress3': params['body']['taxPayerAddress3'],
                'taxPayerCity': params['body']['taxPayerCity'],
                'NOP': params['body']['NOP'],
                'mapCode': params['body']['mapCode'],
                'depositTypeCode': params['body']['depositTypeCode'],
                'wajibPungutNPWP': params['body']['wajibPungutNPWP'],
                'wajibPungutName': params['body']['wajibPungutName'],
                'wajibPungutAddress1': params['body']['wajibPungutAddress1'],
                'wajibPungutAddress2': params['body']['wajibPungutAddress2'],
                'wajibPungutAddress3': params['body']['wajibPungutAddress3'],
                'participantId': params['body']['participantId'],
                'assesmentTaxNumber': params['body']['assesmentTaxNumber'],
                'amountCurrency': params['body']['amountCurrency'],
                'amount': params['body']['amount'],
                'monthFrom': params['body']['monthFrom'],
                'monthTo': params['body']['monthTo'],
                'year': params['body']['year'],
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
            'path': '/bnidirect/api/MPNG2/CreateBilling',
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload,
            'bniDirectKey': bniDirectApiKey
        })
        return responseBniDirect(params={'res': res})