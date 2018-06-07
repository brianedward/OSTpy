import authenticate as auth
<<<<<<< HEAD

class Users:
    def create(self, params):
        # Initiates a new user
        # https://dev.ost.com/docs/api_users_create.html
        endpoint = '/users'
        requestType = 'POST'
        return auth.initiateRequest(requestType, endpoint, params)

    def update(self, params, uuid):
        # Edit existing user account
        # https://dev.ost.com/docs/api_users_edit.html
        endpoint = '/users/'+uuid
        requestType = 'POST'
        return auth.initiateRequest(requestType, endpoint, params)

    def list(self, params):
        # Requests list of all users
        # https://dev.ost.com/docs/api_users_list.html
        endpoint = '/users'
        requestType = 'GET'
        return auth.initiateRequest(requestType, endpoint, params)

    def retrieve(self, uuid):
        # Retrieves specific user
        # https://dev.ost.com/docs/api_users_retrieve.html
        endpoint = '/users/'+uuid
        params = {}
        requestType = 'GET'
        return auth.initiateRequest(requestType, endpoint, params)

class Airdrops:

    def execute(self, params):
        # Airdrops tokens to users
        #https://dev.ost.com/docs/api_airdrop_execute.html
        endpoint = '/airdrops'
        requestType = 'POST'
        return auth.initiateRequest(requestType, endpoint, params)

    def retrieve(self, airdrop_uuid):
        # Requests list of all users
        # https://dev.ost.com/docs/api_airdrop_retrieve.html
        endpoint = '/airdrops/'+airdrop_uuid
        params = {}
        requestType='GET'
        return auth.initiateRequest(requestType, endpoint, params)

    def list(self, params):
        # Requests list of all users
        # https://dev.ost.com/docs/api_airdrop_list.html
        endpoint = '/airdrops'
        requestType = 'GET'
        return auth.initiateRequest(requestType, endpoint, params)

class Actions:
    def create(self, params):
        # Create New Action
        # https://dev.ost.com/docs/api_actions_create.html

        endpoint = '/actions'
        if params['kind'] != 'user_to_user':
            forbidden = ['arbitrary_commission','commission_percent']
            if params['arbitrary_amount'] == 'true':
                forbidden.append('amount')
        else:
            forbidden=[]
            if params['arbitrary_amount'] == 'true':
                forbidden.append('amount')
            if params['arbitrary_commission'] == 'true':
                forbidden.append('commission_percent')
        for ps in forbidden:
            if ps in params:
                del params[ps]

        requestType = 'POST'
        return auth.initiateRequest(requestType, endpoint, params)

    def update(self, params, action_id):
        # Edit existing transaction
        # https://dev.ost.com/docs/api_actions_update.html
        endpoint = '/actions/'+str(action_id)

        if params['kind'] != 'user_to_user':
            forbidden = ['arbitrary_commission','commission_percent']
            if params['arbitrary_amount'] == 'true':
                forbidden.append('amount')
        else:
            forbidden=[]
            if params['arbitrary_amount'] == 'true':
                forbidden.append('amount')
            if params['arbitrary_commission'] == 'true':
                forbidden.append('commission_percent')
        for ps in forbidden:
            if ps in params:
                del params[ps]

        requestType = 'POST'
        return auth.initiateRequest(requestType, endpoint, params)

    def list(self, params):
        # Generates list of all transaction types
        endpoint = '/actions'
        requestType = 'GET'
        return auth.initiateRequest(requestType, endpoint, params)

    def retrieve(self, action_uuid):
        endpoint = '/actions/'+str(action_uuid)
        params={
        }
        requestType = 'GET'
        return auth.initiateRequest(requestType, endpoint, params)

class Transactions:

    def execute(self, params): #post
        # Executes a transaction
        # https://dev.ost.com/docs/api_action_execute.html
        endpoint = '/transactions'
        requestType = 'POST'
        return auth.initiateRequest(requestType, endpoint, params)

    def retrieve(self, transaction_uuid):
        # Outputs status of transaction
        # # https://dev.ost.com/docs/api_transaction_retrieve.html
        endpoint = '/transactions/' + str(transaction_uuid)
        params = {}
        requestType = 'GET'
        return auth.initiateRequest(requestType, endpoint, params)

    def list(self, params):
        # Generates list of all transaction types
        # https://dev.ost.com/docs/api_transaction_list.html
        endpoint = '/transactions'
        return auth.initiateRequest('GET', endpoint, params)

class Transfer:
    def create(self, params): #post
        # Create New Transfer
        # https://dev.ost.com/docs/api_transfers_create.html
        endpoint = '/transfers'
        requestType = 'POST'
        return auth.initiateRequest(requestType, endpoint, params)


    def list(self, params): #get
        # Generates list of all transfers
        # https://dev.ost.com/docs/api_transfers_list.html
        endpoint = '/transfers'
        return auth.initiateRequest('GET', endpoint, params)

    def retrieve(self, transfer_id):
        # Generates list of all transfers
        # https://dev.ost.com/docs/api_transfers_retrieve.html
        endpoint = '/transfers/'+str(transfer_id)
        params={}
        requestType = 'GET'
        return auth.initiateRequest(requestType, endpoint, params)

class Token:
    def getInfo(self):
        endpoint = '/token'
        params = {}
        requestType = 'GET'
        return auth.initiateRequest(requestType, endpoint, params)
=======
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
>>>>>>> a40cdbd3c00960fcbf314cc94667569dbfcd0ef8
