from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateSignature, getTimestamp
from bnipython.lib.util.response import responseFSCM

def sendInvoice(params):
        httpClient = HttpClient();
        timeStamp = getTimestamp()
        payload = {
                'rq_uuid': params['body']['rq_uuid'],
                'password': params['body']['password'],
                'doc_no': params['body']['doc_no'],
                'member_code': params['body']['member_code'],
                'due_date': params['body']['due_date'],
                'amount': params['body']['amount'],
                'currency': params['body']['currency'],
                'issue_date': params['body']['issue_date'],
                'rq_datetime': params['body']['rq_datetime'],
                'term_of_payment': params['body']['term_of_payment'],
                'comm_code': params['body']['comm_code'],
        }
        payloadSignature = {**payload, **{ 'timestamp': timeStamp }}
        signature = generateSignature(
            {'body': payloadSignature, 'apiSecret': params['config']['client']['apiSecret']})
        res = httpClient.requestV2({
            'method': 'POST',
            'apiKey': params['config']['client']['apiKey'],
            'accessToken': params['config']['token'],
            'url': f'{params['config']['baseUrl']}',
            'path': '/FSCM/send_invoice',
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload,
        })
        return responseFSCM(params={'res': res})