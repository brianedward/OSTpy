import authenticate as auth


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
