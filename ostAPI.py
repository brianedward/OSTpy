import authenticate as auth
import time
import pprint

class User:
    def create(self, name, log = True):
        # Creates a new user entry - interact with LOGIN UI
        # INPUT PARAMETER OPTIONS
        # name: NAME OF NEW USER
        endpoint = '/users/create'
        requestParams = {
                         'name':name,
                         }
        requestType = 'POST'
        r = auth.initiateRequest(requestType, endpoint, requestParams)
        if log:
            print(r.text)
        return r

    def edit(self, uuid, newName, log = False):
        # Edit existing user account
        # INPUT PARAMETER OPTIONS
        # uuid: Unique identifier of user to editUser
        # name: new name to assign to user profile
        endpoint = '/users/edit'
        requestParams = {
                         'name':newName,
                         'uuid':uuid
                         }
        requestType = 'POST'
        r = auth.initiateRequest(requestType, endpoint, requestParams)
        if log:
            print(r.text)
        return r

    def list(self, page_no = 1, order = 'desc', listFilter = 'all', order_by = 'creation_time', log=False):
        # Requests list of all users
        # INPUT PARAMETER OPTIONS
        # order: 'desc'/'asc'
        # filter: 'all'/'never_airdropped'
        # order_by: 'creation_time'/'name'
        # page_no : NUMBER
        endpoint = '/users/list'
        requestParams = {
                         'page_no':page_no,
                         'order':order,
                         'filter':listFilter,
                         'order_by':order_by
                         }
        requestType = 'GET'
        pprint.pprint(requestParams)
        r = auth.initiateRequest(requestType, endpoint, requestParams)
        if log:
            pprint.pprint(r.json())
        return r

class Airdrop:

    def execute(self, amount, list_type = 'all', log = False): #post
        # Airdrops tokens to users
        # INPUT PARAMETER OPTIONS
        # amount: Float
        # list_type: 'all'/ ??? maybe same as filter parameter for listUsers
        endpoint = '/users/airdrop/drop'
        requestParams = {
                         'amount':amount,
                         'list_type':list_type,
                         }
        requestType = 'POST'
        r = auth.initiateRequest(requestType, endpoint, requestParams)
        if log:
            print(r.text)
        return r

    def checkStatus(self, airdrop_uuid, log = False): #get
        # Requests list of all users
        # INPUT PARAMETER OPTIONS
        # airdrop_uuid: ID of airdrop initiation request
        endpoint = '/users/airdrop/status'
        requestParams = {
                         'airdrop_uuid':airdrop_uuid
                         }
        requestType='GET'
        r = auth.initiateRequest(requestType, endpoint, requestParams)
        if log:
            pprint.pprint(r.json())
        return r
class Transactions:
    def create(self, name, kind, currency_type, currency_value, commission_percent, log = True): #post
        # Create New Transaction Type
        # INPUT PARAMETER OPTIONS
        # name: name
        # kind: 'user_to_user', 'user_to_company', 'company_to_user'
        # currency_type: 'USD', 'BT'
        # currency_value: #
        # commission_percent: only for user_to_user transactions float {0:1}
        endpoint = '/transaction-types/create'
        requestParams = {
                         'name':name,
                         'kind':kind,
                         'currency_type':currency_type,
                         'currency_value':currency_value,
                         'commission_percent':commission_percent
                         }
        requestType = 'POST'
        r = auth.initiateRequest(requestType, endpoint, requestParams)
        if log:
            print(r.text)
        return r

    def edit(self, client_transaction_id, name, kind, currency_type, currency_value, commission_percent, log = True):#post
        # Edit existing transaction
        # INPUT PARAMETER OPTIONS
        # client_transaction_id: ID of transaction to edit
        # name: name
        # kind: 'user_to_user', 'user_to_company', 'company_to_user'
        # currency_type: 'USD', 'BT'
        # currency_value: #
        # commission_percent: only for user_to_user transactions float {0:1}
        endpoint = '/transaction-types/edit'
        requestParams = {
                         'client_transaction_id':client_transaction_id,
                         'name':name,
                         'kind':kind,
                         'currency_type':currency_type,
                         'currency_value':currency_value,
                         'commission_percent':commission_percent
                         }
        requestType = 'POST'
        r = auth.initiateRequest(requestType, endpoint, requestParams)
        if log:
            print(r.text)
        return r

    def list(self, log = True): #get
        # Generates list of all transaction types
        # INPUT PARAMETER OPTIONS
        # airdrop_uuid: ID of airdrop initiation request
        endpoint = '/transaction-types/list'
        requestParams = {
                         }
        r = auth.initiateRequest('GET', endpoint, requestParams)
        if log:
            pprint.pprint(r.json())
        return r

    def execute(self, from_uuid, to_uuid, transaction_kind, log = True): #post
        # Executes a transaction
        # INPUT PARAMETER OPTIONS
        # from_uuid  >> to_uuid
        # transaction_kind: name of the transaction to execute

        endpoint = '/transaction-types/execute'
        requestParams = {
                         'from_uuid':from_uuid,
                         'to_uuid':to_uuid,
                         'transaction_kind':transaction_kind
                         }
        requestType = 'POST'
        r = auth.initiateRequest(requestType, endpoint, requestParams)
        if log:
            print(r.text)
        return r

    def checkStatus(self, transaction_uuids, log = True):
        # Outputs status of transaction
        # INPUT PARAMETER OPTIONS
        # airdrop_uuid: ID of airdrop initiation request
        endpoint = '/transaction-types/status'
        requestParams = {
                         'transaction_uuids':transaction_uuids
                         }
        requestType = 'POST'
        r = auth.initiateRequest(requestType, endpoint, requestParams)
        if log:
            pprint.pprint(r.text)
        return r
