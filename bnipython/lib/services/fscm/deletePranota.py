from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateSignature, getTimestamp
from bnipython.lib.util.response import responseFSCM

def deletePranota(params):
        httpClient = HttpClient();
        timeStamp = getTimestamp()
        payload = {
                'rq_uuid': params['body']['rq_uuid'],
                'rq_datetime': params['body']['rq_datetime'],
                'password': params['body']['password'],
                'member_code': params['body']['member_code'],
                'comm_code': params['body']['comm_code'],
                'doc_no': params['body']['doc_no'],
                'issue_date': params['body']['issue_date'],
        }
        payloadSignature = {**payload, **{ 'timestamp': timeStamp }}
        signature = generateSignature(
            {'body': payloadSignature, 'apiSecret': params['config']['client']['apiSecret']})
        res = httpClient.requestV2({
            'method': 'POST',
            'apiKey': params['config']['client']['apiKey'],
            'accessToken': params['config']['token'],
            'url': f'{params['config']['baseUrl']}',
            'path': '/FSCM/delete_pranota',
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload,
        })
        return responseFSCM(params={'res': res})