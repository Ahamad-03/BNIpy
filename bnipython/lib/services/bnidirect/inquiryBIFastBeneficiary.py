from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateSignature, getTimestamp, generateBniDirectKey
from bnipython.lib.util.response import responseBniDirect

def inquiryBIFastBeneficiary(params):
        httpClient = HttpClient();
        timeStamp = getTimestamp()
        payload = {
                'corporateId': params['body']['corporateId'],
                'userId': params['body']['userId'],
                'usedProxy': params['body']['usedProxy'],
                'beneficiaryAccountNo': params['body']['beneficiaryAccountNo'],
                'proxyId': params['body']['proxyId'],
                'beneficiaryBankCode': params['body']['beneficiaryBankCode']
        }
        payloadSignature = {**payload, **{ 'timestamp': timeStamp }}
        signature = generateSignature(
            {'body': payloadSignature, 'apiSecret': params['config']['client']['apiSecret']})
        bniDirectKey = generateBniDirectKey({
                'corpId': params['body']['corporateId'], 
                'userId': params['body']['userId'], 
                'bniDirectKey': params['config']['client']['bniDirectApiKey']
                })
        res = httpClient.requestV2BniDirect({
            'method': 'POST',
            'apiKey': params['config']['client']['apiKey'],
            'accessToken': params['config']['token'],
            'url': f'{params['config']['baseUrl']}',
            'path': '/bnidirect/api/BIFAST/InquiryBeneficiaryName',
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload,
            'bniDirectKey': 'dc8f7943e027345677c7dade0441936c3bb3f8d697ef8f7b28ae5dfdeea78dd1'
        })
        return responseBniDirect(params={'res': res})