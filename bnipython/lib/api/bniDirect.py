from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateBniDirectKey, generateSignature, getTimestamp
from bnipython.lib.util.response import responseBniDirect

class BNIDirect():
    def __init__(self, client):
        self.client = client.config
        self.baseUrl = client.getBaseUrl()
        self.config = client.getConfig()
        self.token = client.getToken()
        self.httpClient = HttpClient()

    def _make_request(self, path, method, timeStamp, payload=None):
        signaturePayload = {**payload, **{ 'timestamp': timeStamp}}
        signature = generateSignature(
            {'body': signaturePayload, 'apiSecret': self.client['apiSecret']}
        )
        bniDirectKey = generateBniDirectKey({
            'corporateId': payload['corporateId'], 
            'userId': payload['userId'], 
            'bniDirectApiKey': self.client['bniDirectApiKey'],
            })
        res = self.httpClient.requestV2BniDirect({
            'method': method,
            'apiKey': self.client['apiKey'],
            'accessToken': self.token,
            'url': f'{self.baseUrl}',
            'path': path,
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload,
            'bniDirectKey': bniDirectKey
        })
        return responseBniDirect(params={'res': res})

    def createMPNG2BillingID(self, payload=None):
        """
        Create MPN G2 billing ID

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID - Required.
                - userId (str): User ID - Required.
                - npwp (str): NPWP - Required.
                - taxPayerName (str): taxPayerName - Required.
                - taxPayerAddress1 (str): taxPayerAddress(1) - Required.
                - taxPayerAddress2 (str): taxPayerAddress(2) - Optional.
                - taxPayerAddress3 (str): taxPayerAddress(3) - Optional.
                - taxPayerCity (str): taxPayerCity - Required.
                - NOP (str): Tax Object Number(NOP) - Optional.
                - MAPCode (str): MAP/Akun Code - Required.
                - depositTypeCode (str): Deposit Type Code - Required.
                - wajibPungutNPWP (str): Wajib Pungut NPWP - Optional.
                - wajibPungutName (str): Wajib Pungut Name - Optional.
                - wajibPungutAddress1 (str): Wajib Pungut Address (1) - Optional.
                - wajibPungutAddress2 (str): Wajib Pungut Address (2) - Optional.
                - wajibPungutAddress3 (str): Wajib Pungut Address (3) - Optional.
                - participantId (str): Participant ID - Optional.
                - assessmentTaxNumber (str): Assessment Tax Number - Optional.
                - amountCurrency (str): Amount Currency - Required.
                - amount (str): Amount - Required.
                - monthFrom (str): Month (From), e.g. 1-12 - Required.
                - monthTo (str): Month (To), e.g. 1-12 - Required.
                - year (str): year - Required.
                - confirmNumber (str): Confirm Number - Required.
                - traceId (str): Trace ID - Optional.
                - kelurahan (str): kelurahan - Optional.
                - kecamatan (str): kecamatan - Optional.
                - provinsi (str): provinsi - Optional.
                - kota (str): kota - Optional.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/MPNG2/CreateBilling'
        return self._make_request(path, method, timeStamp, payload)

    def inquiryNPWP(self, payload=None):
        """
        inquiry NPWP MPN G2.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (40 characters) - Required.
                - userId (str): User ID (40 characters) - Required.
                - npwp (str): NPWP (15 characters) - Required.
                - NOP (str): Tax Object Number (NOP) (18 characters) - Optional.
                - MAPCode (str): MAP/Account Code (6 characters) - Required.
                - depositTypeCode (str): Deposit Type Code (40 characters) - Required.
                - currency (str): Currency Code (3 characters) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/MPNG2/InquiryNPWP'
        return self._make_request(path, method, timeStamp, payload)
    
    def inquiryInHouseAndVABeneficiaryName(self, payload=None):
        """
        Inquiry InHouse and VA Beneficiary Name.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (40 characters) - Required.
                - userId (str): User ID (40 characters) - Required.
                - accountNo (str): Account No. (16 characters) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/InHouse/InquiryBeneficiaryName'
        return self._make_request(path, method, timeStamp, payload)
    
    def inquiryLLGRTGSOnlineBenefiacyName(self, payload=None):
        """
        Service untuk melakukan inquiry nama rekening Bank lain (LLG/ RTGS/ Online).

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (40 characters) - Required.
                - userId (str): User ID (40 characters) - Required.
                - beneficiaryAccountNo (str): Beneficiary Account No. (16 characters) - Required.
                - beneficiaryBankCode (str): Beneficiary Bank Code (40 characters) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/Online/InquiryBeneficiaryName'
        return self._make_request(path, method, timeStamp, payload)
    
    def inquiryAccountStatement(self, payload=None):
        """
        Service untuk melakukan inquiry transaksi dari account.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (40 characters) - Required.
                - userId (str): User ID (40 characters) - Required.
                - fromDate (str): From Posting Date (yyyyMMdd format, 8 characters) - Required.
                - toDate (str): To Posting Date (yyyyMMdd format, 8 characters) - Required.
                - transactionType (str): Transaction Type (All, Db (debit), Cr (credit)) - Required.
                - accountList (array): Account List 
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/Account/InquiryAccountStatement'
        return self._make_request(path, method, timeStamp, payload)
    
    def inquiryBilling(self, payload=None):
        """
        Service untuk melakukan inquiry tagihan (billing) dari institusi yang ada di BNI Direct

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (40 characters) - Required.
                - userId (str): User ID (40 characters) - Required.
                - debitedAccountNo (str): Debited Account (16 characters) - Required.
                - institution (str): Institution (40 characters) - Required.
                - customerInformation1 (str): Customer Information (1) - Required.
                - customerInformation2 (str): Customer Information (2) - Optional.
                - customerInformation3 (str): Customer Information (3) - Optional.
                - customerInformation4 (str): Customer Information (4) - Optional.
                - customerInformation5 (str): Customer Information (5) - Optional.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/Billing/Inquiry'
        return self._make_request(path, method, timeStamp, payload)
    
    def inquiryBNIPopsCashAndCarry(self, payload=None):
        """
        Service untuk melakukan inquiry detail Cash and Carry.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (40 characters) - Required.
                - userId (str): User ID (40 characters) - Required.
                - debitAccountNo (str): Debited Account (16 characters) - Required.
                - salesOrganizationCode (str): Sales Organization Code (40 characters) - Required.
                - distributionChannelCode (str): Distribution Channel Code (40 characters) - Required.
                - productCode (str): Product Code (40 characters) - Required.
                - shipTo (str): Ship To (100 characters) - Required.
                - debitOrCreditNoteNo (numeric): Debit / Credit Note Number (up to 18 digits) - Optional.
                - productInformationDetail (list of dict): Product Information Detail - Optional. Each object in the array should have its own structure defined.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/BNIPOPS/CashandCarry/Inquiry'
        return self._make_request(path, method, timeStamp, payload)
    
    def inquiryBNIPopsProductAllocation(self, payload=None):
        """
        Service untuk melakukan transaksi Product Allocation.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (40 characters) - Required.
                - userId (str): User ID (40 characters) - Required.
                - debitAccountNo (str): Debited Account (16 characters) - Required.
                - salesOrganizationCode (str): Sales Organization Code (40 characters) - Required.
                - distributionChannelCode (str): Distribution Channel Code (40 characters) - Required.
                - productCode (str): Product Code (40 characters) - Required.
                - shipTo (str): Ship To (100 characters) - Required.
                - scheduleAgreementNo (str): Schedule Agreement Number (100 characters) - Required.
                - debitOrCreditNoteNo (str): Debit / Credit Note Number (up to 18 characters) - Optional.
                - productInformationDetail (list of dict): Product Information Detail - Optional. Each object in the array should have its own structure defined.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/BNIPOPS/ProductAllocation/Inquiry'
        return self._make_request(path, method, timeStamp, payload)
    
    def getPaymentStatus(self, payload=None):
        """
        Service untuk melakukan inquiry Transaction Status dari transaksi yang sudah dilakukan.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (40 characters) - Required.
                - userId (str): User ID (40 characters) - Required.
                - transactionReferenceNo (str): Transaction Reference No. (40 characters) - Required.
                - remitterReferenceNo (str): Remitter Reference No. (16 characters) - Optional.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/InquiryTransactionStatus'
        return self._make_request(path, method, timeStamp, payload)
    
    def inhouseTransfer(self, payload=None):
        """
        Service untuk melakukan transaksi InHouse Transfer.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (40 characters) - Required.
                - userId (str): User ID (40 characters) - Required.
                - debitedAccountNo (str): Debited Account No. (16 characters) - Optional.
                - amountCurrency (str): Amount Currency (3 characters) - Required.
                - amount (str): Amount (up to 15 characters) - Required.
                - treasuryReferenceNo (str): Treasury Reference No. (40 characters) - Optional.
                - transactionPurposeCode (str): Transaction Purpose Code (40 characters) - Required.
                - remark1 (str): Remark 1 (up to 40 characters) - Optional.
                - remark2 (str): Remark 2 (up to 40 characters) - Optional.
                - remark3 (str): Remark 3 (up to 40 characters) - Optional.
                - remitterReferenceNo (str): Remitter Reference No. (16 characters) - Required.
                - finalizePaymentFlag (str): Finalize Payment Flag (1 character) - Required.
                - beneficiaryReferenceNo (str): Beneficiary Reference No. (16 characters) - Optional.
                - toAccountNo (str): To Account No. (16 characters) - Required.
                - notificationFlag (str): Notification Flag (1 character) - Required.
                - beneficiaryEmail (str): Beneficiary Email (100 characters) - Optional.
                - transactionInstructionDate (str): Transaction Instruction Date (yyyyMMdd format, 8 characters) - Required.
                - docUniqueId (str): Unique ID (40 characters) - Optional.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/InHouse/Transfer'
        return self._make_request(path, method, timeStamp, payload)
    
    def LLGTransfer(self, payload=None):
        """
        Service untuk melakukan transaksi LLG Transfer. 

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (40 characters) - Required.
                - userId (str): User ID (40 characters) - Required.
                - debitedAccountNo (str): Debited Account No. (16 characters) - Required.
                - amountCurrency (str): Amount Currency (3 characters) - Required.
                - amount (str): Amount (up to 15 characters) - Required.
                - treasuryReferenceNo (str): Treasury Reference No. (40 characters) - Optional.
                - chargeTo (str): Charge To (3 characters) - Required.
                - remark1 (str): Remark 1 (up to 40 characters) - Optional.
                - remark2 (str): Remark 2 (up to 40 characters) - Optional.
                - remark3 (str): Remark 3 (up to 40 characters) - Optional.
                - remitterReferenceNo (str): Remitter Reference No. (16 characters) - Required.
                - finalizePaymentFlag (str): Finalize Payment Flag (1 character) - Required.
                - beneficiaryReferenceNo (str): Beneficiary Reference No. (16 characters) - Optional.
                - beneficiaryAccountNo (str): Beneficiary Account No. (34 characters) - Required.
                - beneficiaryAccountName (str): Beneficiary Account Name (70 characters) - Required.
                - beneficiaryAddress1 (str): Beneficiary Address (1) (50 characters) - Optional.
                - beneficiaryAddress2 (str): Beneficiary Address (2) (50 characters) - Optional.
                - beneficiaryAddress3 (str): Beneficiary Address (3) (50 characters) - Optional.
                - beneficiaryResidentshipCountryCode (str): Beneficiary Residentship Country Code (40 characters) - Required.
                - beneficiaryCitizenshipCountryCode (str): Beneficiary Citizenship Country Code (40 characters) - Required.
                - beneficiaryType (str): Beneficiary Type (2 characters) - Required.
                - beneficiaryBankCode (str): Beneficiary Bank Code (40 characters) - Required.
                - beneficiaryBankName (str): Beneficiary Bank Name (100 characters) - Required.
                - beneficiaryBankBranchCode (str): Beneficiary Bank Branch Code (40 characters) - Optional.
                - beneficiaryBankBranchName (str): Beneficiary Bank Branch Name (100 characters) - Optional.
                - beneficiaryBankCityName (str): Beneficiary Bank City Name (100 characters) - Required.
                - notificationFlag (str): Notification Flag (1 character) - Required.
                - beneficiaryEmail (str): Beneficiary Email (100 characters) - Optional.
                - transactionInstructionDate (str): Transaction Instruction Date (yyyyMMdd format, 8-18 characters) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/LLG/Transfer'
        return self._make_request(path, method, timeStamp, payload)
    
    def RTGSTransfer(self, payload=None):
        """
        Service untuk melakukan transaksi RTGS Transfer. 

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (40 characters) - Required.
                - userId (str): User ID (40 characters) - Required.
                - debitedAccountNo (str): Debited Account No. (3 characters) - Required.
                - amountCurrency (str): Amount Currency (16 characters) - Required.
                - amount (str): Amount (15 characters) - Required.
                - treasuryReferenceNo (str): Treasury Reference No. (40 characters) - Optional.
                - chargeTo (str): Charge To (3 characters) - Required.
                - remark1 (str): Remark 1 (up to 40 characters) - Optional.
                - remark2 (str): Remark 2 (up to 40 characters) - Optional.
                - remark3 (str): Remark 3 (up to 40 characters) - Optional.
                - remitterReferenceNo (str): Remitter Reference No. (16 characters) - Required.
                - finalizePaymentFlag (str): Finalize Payment Flag (1 character) - Required.
                - beneficiaryReferenceNo (str): Beneficiary Reference No. (16 characters) - Optional.
                - beneficiaryAccountNo (str): Beneficiary Account No. (17 characters) - Required.
                - beneficiaryAccountName (str): Beneficiary Account Name (80 characters) - Required.
                - beneficiaryAddress1 (str): Beneficiary Address (1) (50 characters) - Optional.
                - beneficiaryAddress2 (str): Beneficiary Address (2) (50 characters) - Optional.
                - beneficiaryAddress3 (str): Beneficiary Address (3) (50 characters) - Optional.
                - beneficiaryResidentshipCountryCode (str): Beneficiary Residentship Country Code (40 characters) - Required.
                - beneficiaryCitizenshipCountryCode (str): Beneficiary Citizenship Country Code (40 characters) - Required.
                - beneficiaryBankCode (str): Beneficiary Bank Code (40 characters) - Required.
                - beneficiaryBankName (str): Beneficiary Bank Name (100 characters) - Required.
                - beneficiaryBankBranchCode (str): Beneficiary Bank Branch Code (40 characters) - Optional.
                - beneficiaryBankBranchName (str): Beneficiary Bank Branch Name (100 characters) - Optional.
                - beneficiaryBankCityName (str): Beneficiary Bank City Name (100 characters) - Required.
                - notificationFlag (str): Notification Flag (1 character) - Required.
                - beneficiaryEmail (str): Beneficiary Email (100 characters) - Optional.
                - transactionInstructionDate (str): Transaction Instruction Date (yyyyMMdd format, 8 characters) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/RTGS/Transfer'
        return self._make_request(path, method, timeStamp, payload)
    
    def onlineTransfer(self, payload=None):
        """
        Service untuk melakukan transaksi Domestic Online Transfer. 

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (40 characters) - Required.
                - userId (str): User ID (40 characters) - Required.
                - debitedAccountNo (str): Debited Account No. (16 characters) - Required.
                - amountCurrency (str): Amount Currency (3 characters) - Required.
                - amount (str): Amount (15 characters) - Required.
                - treasuryReferenceNo (str): Treasury Reference No. (40 characters) - Optional.
                - chargeTo (str): Charge To (3 characters) - Required.
                - remark1 (str): Remark 1 (up to 40 characters) - Optional.
                - remark2 (str): Remark 2 (up to 40 characters) - Optional.
                - remark3 (str): Remark 3 (up to 40 characters) - Optional.
                - remitterReferenceNo (str): Remitter Reference No. (16 characters) - Required.
                - finalizePaymentFlag (str): Finalize Payment Flag (1 character) - Required.
                - beneficiaryReferenceNo (str): Beneficiary Reference No. (16 characters) - Optional.
                - beneficiaryAccountNo (str): Beneficiary Account No. (17 characters) - Required.
                - beneficiaryBankCode (str): Beneficiary Bank Code (40 characters) - Required.
                - beneficiaryBankName (str): Beneficiary Bank Name (100 characters) - Required.
                - notificationFlag (str): Notification Flag (1 character) - Required.
                - beneficiaryEmail (str): Beneficiary Email (100 characters) - Optional.
                - transactionInstructionDate (str): Transaction Instruction Date (yyyyMMdd format, 8 characters) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/Online/Transfer'
        return self._make_request(path, method, timeStamp, payload)
    
    def internationalTransfer(self, payload=None):
        """
        Service untuk melakukan transaksi International Transfer. 

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (40 characters) - Required.
                - userId (str): User ID (40 characters) - Required.
                - debitedAccountNo (str): Debited Account No. (16 characters) - Required.
                - amountCurrency (str): Amount Currency (3 characters) - Required.
                - amount (str): Amount (15 characters) - Required.
                - treasuryReferenceNo (str): Treasury Reference No. (40 characters) - Optional.
                - chargeTo (str): Charge To (3 characters) - Required.
                - remark1 (str): Remark 1 (up to 40 characters) - Optional.
                - remark2 (str): Remark 2 (up to 40 characters) - Optional.
                - remark3 (str): Remark 3 (up to 40 characters) - Optional.
                - remitterReferenceNo (str): Remitter Reference No. (16 characters) - Required.
                - finalizePaymentFlag (str): Finalize Payment Flag (1 character) - Required.
                - beneficiaryReferenceNo (str): Beneficiary Reference No. (16 characters) - Optional.
                - beneficiaryAccountNo (str): Beneficiary Account No. (17 characters) - Required.
                - beneficiaryAccountName (str): Beneficiary Account Name (80 characters) - Required.
                - beneficiaryAddress1 (str): Beneficiary Address (1) (50 characters) - Optional.
                - beneficiaryAddress2 (str): Beneficiary Address (2) (50 characters) - Optional.
                - beneficiaryAddress3 (str): Beneficiary Address (3) (50 characters) - Optional.
                - organizationDirectoryCode (str): Organization Directory Code (40 characters) - Required.
                - beneficiaryBankCode (str): Beneficiary Bank Code (40 characters) - Required.
                - beneficiaryBankName (str): Beneficiary Bank Name (100 characters) - Required.
                - beneficiaryBankBranchName (str): Beneficiary Bank Branch Name (100 characters) - Optional.
                - beneficiaryBankAddress1 (str): Beneficiary Bank Address (1) (35 characters) - Optional.
                - beneficiaryBankAddress2 (str): Beneficiary Bank Address (2) (35 characters) - Optional.
                - beneficiaryBankAddress3 (str): Beneficiary Bank Address (3) (35 characters) - Optional.
                - beneficiaryBankCountryName (str): Beneficiary Bank Country Name (100 characters) - Optional.
                - correspondentBankName (str): Correspondent Bank Name (100 characters) - Optional.
                - identicalStatusFlag (str): Identical Status Flag (1 character) - Required.
                - beneficiaryResidentshipCode (str): Beneficiary Residentship Code (40 characters) - Required.
                - beneficiaryCitizenshipCode (str): Beneficiary Citizenship Code (40 characters) - Required.
                - beneficiaryCategoryCode (str): Beneficiary Category Code (40 characters) - Optional.
                - transactorRelationship (str): Transactor Relationship (Affiliated) Flag (1 character) - Required.
                - transactionPurposeCode (str): Transaction Purpose Code (40 characters) - Required.
                - transactionDescription (str): Transaction Description (100 characters) - Optional.
                - notificationFlag (str): Notification Flag (1 character) - Required.
                - beneficiaryEmail (str): Beneficiary Email (100 characters) - Optional.
                - transactionInstructionDate (str): Transaction Instruction Date (yyyyMMdd format, 8 characters) - Required.
                - docUniqueId (str): Unique underlying ID (40 characters) - Required if transaction exceeds PIB 18 or WIC limits.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/International/Transfer'
        return self._make_request(path, method, timeStamp, payload)
    
    def billPayment(self, payload=None):
        """
        Service untuk melakukan transaksi Bill Payment dari institusi yang ada di BNI Direct. 

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (40 characters) - Required.
                - userId (str): User ID (40 characters) - Required.
                - debitedAccountNo (str): Debited Account No. (16 characters) - Required.
                - institution (str): Institution (40 characters) - Required.
                - payeeName (str): Payee Name (40 characters) - Required.
                - customerInformation1 (str): Customer Information (1) (40 characters) - Optional.
                - customerInformation2 (str): Customer Information (2) (40 characters) - Optional.
                - customerInformation3 (str): Customer Information (3) (40 characters) - Optional.
                - customerInformation4 (str): Customer Information (4) (40 characters) - Optional.
                - customerInformation5 (str): Customer Information (5) (40 characters) - Optional.
                - billPresentmentFlag (str): Bill Presentment Flag (1 character) - Required.
                - remitterRefNo (str): Remitter Reference No. (16 characters) - Required.
                - finalizePaymentFlag (str): Finalize Payment Flag (1 character) - Required.
                - beneficiaryRefNo (str): Beneficiary Reference No. (16 characters) - Optional.
                - notificationFlag (str): Notification Flag (1 character) - Required.
                - beneficiaryEmail (str): Beneficiary Email (100 characters) - Optional.
                - transactionInstructionDate (str): Transaction Instruction Date (yyyyMMdd format, 8 characters) - Required.
                - amountCurrency (str): Amount Currency (3 characters) - Required.
                - amount (str): Amount (18 characters) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/Billing/Payment'
        return self._make_request(path, method, timeStamp, payload)
    
    def bniPopsCashAndCarry(self, payload=None):
        """
       Service untuk melakukan transaksi Cash and Carry. 

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (40 characters) - Required.
                - userId (str): User ID (40 characters) - Required.
                - debitedAccountNo (str): Debited Account No. (16 characters) - Required.
                - salesOrganizationCode (str): Sales Organization Code (40 characters) - Required.
                - distributionChannelCode (str): Distribution Channel Code (40 characters) - Required.
                - productCode (str): Product Code (40 characters) - Required.
                - shipTo (str): Ship To (100 characters) - Required.
                - debitOrCreditNoteNo (str): Debit / Credit Note Number (18 characters) - Optional.
                - productInformationDetail (list of dict): Product Information Detail - Optional.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/BNIPOPS/CashandCarry/Payment'
        return self._make_request(path, method, timeStamp, payload)
    
    def bniPopsProductAllocation(self, payload=None):
        """
        Service untuk melakukan transaksi Product Allocation.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (40 characters) - Required.
                - userId (str): User ID (40 characters) - Required.
                - debitedAccountNo (str): Debited Account No. (16 characters) - Required.
                - salesOrganizationCode (str): Sales Organization Code (40 characters) - Required.
                - distributionChannelCode (str): Distribution Channel Code (40 characters) - Required.
                - productCode (str): Product Code (40 characters) - Required.
                - shipTo (str): Ship To (100 characters) - Required.
                - scheduleAggreementNo (str): Schedule Agreement Number (100 characters) - Required.
                - debitOrCreditNoteNo (str): Debit / Credit Note Number (18 characters) - Optional.
                - productInformationDetail (list of dict): Product Information Detail - Optional.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/BNIPOPS/ProductAllocation/Payment'
        return self._make_request(path, method, timeStamp, payload)
    

# BNI POPS – Resubmit Cash and Carry page 87
    def balanceInquiry(self, payload=None):
        """
        Conducts a charges and rate inquiry.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID - Required.
                - userId (str): User ID - Required.
                - accountList (float): List of Account (1 … n) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/Account/InquiryBalance'
        return self._make_request(path, method, timeStamp, payload)
