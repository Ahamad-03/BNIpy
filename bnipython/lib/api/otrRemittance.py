from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateSignature, getTimestampOTR, generateGUID
from bnipython.lib.util.response import responseOTR

class OTRRemittance():
    def __init__(self, client, options={'channelId'}):
        self.client = client.config
        self.baseUrl = client.getBaseUrl()
        self.config = client.getConfig()
        self.token = client.getToken()
        self.httpClient = HttpClient()
        self.configOtr = options
        self.configOtr['channelId'] = options.get('channelId', '')

    def _make_request(self, path, method, timeStamp, payload=None):
        signaturePayload = {**payload, **{ 'timestamp': timeStamp}}
        signature = generateSignature(
            {'body': signaturePayload, 'apiSecret': self.client['apiSecret']}
        )
        res = self.httpClient.requestOtr({
            'method': method,
            'url': f'{self.baseUrl}',
            'path': path,
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload,
            'RequestId': generateGUID(),
            'ChannelId': self.configOtr['channelId'],
            'apiKey': self.client['apiKey'],
            'accessToken': self.token,
        })
        return responseOTR(params={'res': res})
            #     - 'serviceType' (str): Service Type.
            # - 'country' (str): country.

    def getBankAndCurrencyLimitation(self, payload=None):
        """
        Conducts a getBankAndCurrencyLimitation.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - serviceType (str): Service Type.
                - country (str): country.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestampOTR()
        method='POST'
        path='/otr/globs/getBankAndCurrencyLimitation'
        return self._make_request(path, method, timeStamp, payload)
    
    def chargesAndRateInquiry(self,  payload=None):
        """
        Conducts a charges and rate inquiry.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - orderingId (str): ID for the order (receiver).
                - bic (str): BID Channel.
                - orderingAmount (float): Transaction amount.
                - orderingCcy (str): Receiver currency.
                - sourceCcy (str): Sender currency.
                - detailCharges (str): Charge type.
                - serviceType (str): Service type.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestampOTR()
        method='POST'
        path='/otr/globs/chargesAndRateInquiry'
        return self._make_request(path, method, timeStamp, payload)
    
    def trackingTransaction(self,  payload=None):
        """
        Conducts a trackingTransaction.

        :param payload: A dictionary containing the following keys:
            - 'referenceNumber' (str): Unique reference from request.
        :return: A response object from the prescreening process.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestampOTR()
        method='POST'
        path='/otr/globs/transaction/tracking/' + payload.get('referenceNumber', '')
        return self._make_request(path, method, timeStamp, payload)
    
    def transactionOverbooking(self,  payload=None):
        """
        Conducts a trackingTransaction.

        :param payload: A dictionary containing the following keys:
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
            - 'invoiceAmount' (int): Invoice amount.
        :return: A response object from the prescreening process.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestampOTR()
        method='POST'
        path='/otr/globs/transaction/overbooking'
        return self._make_request(path, method, timeStamp, payload)