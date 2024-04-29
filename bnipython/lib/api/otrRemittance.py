from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateSignature, getTimestampBNIMove, generateGUID
from bnipython.lib.util.response import responseBNIMove

class OTRRemittance():
    def __init__(self, client, options={'channelId'}):
        self.client = client.config
        self.baseUrl = client.getBaseUrl()
        self.config = client.getConfig()
        self.token = client.getToken()
        self.httpClient = HttpClient()
        self.configOtr = options
        self.configOtr['channelId'] = options.get('channelId', '')

    def _create_payload(self, payload=None):
        timeStamp = getTimestampBNIMove()
        payload = payload
        return payload, timeStamp

    def _make_request(self, path, method, timeStamp, query_params=None, payload=None):
        path = f'{path}'
        if query_params:
            query_string = '&'.join([f"{key}={value}" for key, value in query_params.items()])
            path += f'?{query_string}'
        res = self.httpClient.requestOtr({
            'method': method,
            'url': f'{self.baseUrl}',
            'path': path,
            'timestamp': timeStamp,
            'data': payload,
            'RequestId': generateGUID(),
            'ChannelId': self.configOtr['channelId'],
        })
        print('res', res)
        return responseBNIMove(params={'res': res})

    def getBankAndCurrencyLimitation(self, payload=None, query_params=None):
        if payload is None:
            payload = {}
        _ , timeStamp = self._create_payload(payload)
        method='GET'
        path='/IBOCNGWebClient/globsapi/corporate/getBankAndCurrencyLimitation'
        return self._make_request(path, method, timeStamp, query_params, payload)
    
    def chargesAndRateInquiry(self,  payload=None, query_params=None):
        """
        Conducts a chargesAndRateInquiry.

        :param params: A dictionary containing the following keys:
            - 'orderingId' (str): Id for order (receiver).
            - 'bic' (str): BID Channel.
            - 'orderingAmount' (float): Transaction Amount.
            - 'orderingCcy' (str): Receiver currency.
            - 'sourceCcy' (str): Sender currency.
            - 'detailCharges' (str): Charge Type .
            - 'serviceType' (str): Service Type.
        :return: A response object from the prescreening process.
        """
        if payload is None:
            payload = {}
        payload , timeStamp = self._create_payload(payload)
        method='POST'
        path='/IBOCNGWebClient/globsapi/corporate/getBankAndCurrencyLimitation'
        return self._make_request(path, method, timeStamp, query_params, payload)
    
    def trackingTransaction(self,  payload=None, query_params=None):
        """
        Conducts a trackingTransaction.

        :param params: A dictionary containing the following keys:
            - 'referenceNumber' (str): Unique reference from request.
        :return: A response object from the prescreening process.
        """
        if payload is None:
            payload = {}
        _ , timeStamp = self._create_payload()
        method='GET'
        path='/IBOCNGWebClient/globsapi/corporate/transaction/tracking/' + payload.get('referenceNumber', '')
        return self._make_request(path, method, timeStamp, query_params)
    
    def transactionOverbooking(self,  payload=None, query_params=None):
        """
        Conducts a trackingTransaction.

        :param params: A dictionary containing the following keys:
            - 'referenceNumber' (str): Unique reference from request.
            - 'orderingId' (str): Id for order (receiver).
            - 'orderingBic' (str): BID Channel.
            - 'orderingName' (str): Receiver name.
            - 'orderingAddress' (str): Receiver address.
            - 'orderingEmail' (str): Receiver email.
            - 'orderingPhoneNumber' (str): Receiver phone number.
            - 'beneficiaryAccount' (str): Beneficiary account.
            - 'beneficiaryName' (str): Beneficiary name.
            - 'beneficiaryAddress' (str): Beneficiary address.
            - 'beneficiaryPhoneNumber' (str): Beneficiary phone number.
            - 'accountWithInstCode' (str): Account with institution code.
            - 'accountWithInstBic' (str): Account with institution BIC.
            - 'accountWithInstName' (str): Account with institution name.
            - 'remittanceInfo' (str): Remittance info.
            - 'invoiceNumber' (str): Invoice number.
            - 'invoiceAmount' (float): Invoice amount.
        :return: A response object from the prescreening process.
        """
        if payload is None:
            payload = {}
        payload , timeStamp = self._create_payload(payload)
        method='POST'
        path='/IBOCNGWebClient/globsapi/corporate/transaction/overbooking'
        return self._make_request(path, method, timeStamp, query_params, payload)