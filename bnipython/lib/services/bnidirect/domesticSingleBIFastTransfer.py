from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateSignature, getTimestamp, generateBniDirectKey
from bnipython.lib.util.response import responseBniDirect

def domesticSingleBIFastTransfer(params):
        httpClient = HttpClient();
        timeStamp = getTimestamp()
        payload = {
                'corporateId': params['body']['corporateId'],
                'userId': params['body']['userId'],
                'debitedAccountNo': params['body']['debitedAccountNo'],
                'amountCurrency': params['body']['amountCurrency'],
                'amount': params['body']['amount'],
                'exchangeRateCode': params['body']['exchangeRateCode'],
                'treasuryReferenceNo': params['body']['treasuryReferenceNo'],
                'chargeTo': params['body']['chargeTo'],
                'remark1': params['body']['remark1'],
                'remark2': params['body']['remark2'],
                'remark3': params['body']['remark3'],
                'remitterReferenceNo': params['body']['remitterReferenceNo'],
                'finalizePaymentFlag': params['body']['finalizePaymentFlag'],
                'beneficiaryReferenceNo': params['body']['beneficiaryReferenceNo'],
                'usedProxy': params['body']['usedProxy'],
                'beneficiaryAccountNo': params['body']['beneficiaryAccountNo'],
                'proxyId': params['body']['proxyId'],
                'beneficiaryBankCode': params['body']['beneficiaryBankCode'],
                'beneficiaryBankName': params['body']['beneficiaryBankName'],
                'notificationFlag': params['body']['notificationFlag'],
                'beneficiaryEmail': params['body']['beneficiaryEmail'],
                'transactionInstructionDate': params['body']['transactionInstructionDate'],
                'transactionPurposeCode': params['body']['transactionPurposeCode']
        }
        payloadSignature = {**payload, **{ 'timestamp': timeStamp }}
        signature = generateSignature(
            {'body': payloadSignature, 'apiSecret': params['config']['client']['apiSecret']})
        bniDirectKey = generateBniDirectKey({
                'corporateId': params['body']['corporateId'], 
                'userId': params['body']['userId'], 
                'bniDirectKey': params['config']['client']['bniDirectApiKey']
                })
        res = httpClient.requestV2BniDirect({
            'method': 'POST',
            'apiKey': params['config']['client']['apiKey'],
            'accessToken': params['config']['token'],
            'url': f'{params['config']['baseUrl']}',
            'path': '/bnidirect/api/BIFAST/Transfer',
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload,
            'bniDirectKey': bniDirectKey
        })
        return responseBniDirect(params={'res': res})