from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateSignature, getTimestamp, generateBniDirectKey
from bnipython.lib.util.response import responseBniDirect

def transferRTGS(params):
        httpClient = HttpClient();
        timeStamp = getTimestamp()
        payload = {
                'corporateId': params['body']['corporateId'],
                'userId': params['body']['userId'],
                'debitedAccountNo': params['body']['debitedAccountNo'],
                'amountCurrency': params['body']['amountCurrency'],
                'amount': params['body']['amount'],
                'treasuryReferenceNo': params['body']['treasuryReferenceNo'],
                'chargeTo': params['body']['chargeTo'],
                'remark1': params['body']['remark1'],
                'remark2': params['body']['remark2'],
                'remark3': params['body']['remark3'],
                'remitterReferenceNo': params['body']['remitterReferenceNo'],
                'finalizePaymentFlag': params['body']['finalizePaymentFlag'],
                'beneficiaryReferenceNo': params['body']['beneficiaryReferenceNo'],
                'beneficiaryAccountNo': params['body']['beneficiaryAccountNo'],
                'beneficiaryAccountName': params['body']['beneficiaryAccountName'],
                'beneficiaryAddress1': params['body']['beneficiaryAddress1'],
                'beneficiaryAddress2': params['body']['beneficiaryAddress2'],
                'beneficiaryAddress3': params['body']['beneficiaryAddress3'],
                'beneficiaryResidentshipCountryCode': params['body']['beneficiaryResidentshipCountryCode'],
                'beneficiaryCitizenshipCountryCode': params['body']['beneficiaryCitizenshipCountryCode'],
                'beneficiaryBankCode': params['body']['beneficiaryBankCode'],
                'beneficiaryBankName': params['body']['beneficiaryBankName'],
                'beneficiaryBankBranchCode': params['body']['beneficiaryBankBranchCode'],
                'beneficiaryBankBranchName': params['body']['beneficiaryBankBranchName'],
                'beneficiaryBankCityName': params['body']['beneficiaryBankCityName'],
                'notificationFlag': params['body']['notificationFlag'],
                'beneficiaryEmail': params['body']['beneficiaryEmail'],
                'transactionInstructionDate': params['body']['transactionInstructionDate'],
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
            'path': '/bnidirect/api/RTGS/Transfer',
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload,
            'bniDirectKey': 'dc8f7943e027345677c7dade0441936c3bb3f8d697ef8f7b28ae5dfdeea78dd1',
            # 'bniDirectKey': bniDirectApiKey
        })
        return responseBniDirect(params={'res': res})