from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateSignature, getTimestamp
from bnipython.lib.util.response import responseFSCM

def checkStopSupply(params):
        httpClient = HttpClient();
        timeStamp = getTimestamp()
        payload = {
                'rq_uuid': params['body']['rq_uuid'],
                'comm_code': params['body']['comm_code'],
                'currency': params['body']['currency'],
                'rq_datetime': params['body']['rq_datetime'],
                'member_code': params['body']['member_code'],
                'password': params['body']['password'],
                'ccy': params['body']['ccy'],
                'status_member': params['body']['status_member'],
        }
        payloadSignature = {**payload, **{ 'timestamp': timeStamp }}
        signature = generateSignature(
            {'body': payloadSignature, 'apiSecret': params['config']['client']['apiSecret']})
        res = httpClient.requestV2({
            'method': 'POST',
            'apiKey': params['config']['client']['apiKey'],
            'accessToken': params['config']['token'],
            'url': f'{params['config']['baseUrl']}',
            'path': '/FSCM/check-stop-supply',
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload,
        })
        return responseFSCM(params={'res': res})