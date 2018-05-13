import requests
import json
import time
from urllib import urlencode
import hmac
import hashlib
import pprint
import config # create a file called 'config.py' and put your api key and secret key in here. Create another file called '.gitignore' and type 'config.py' to keep your private info from being shared

# TODO: Put the following three functions into a private class
def generateQueryString(endpoint, inputParams):
    # Used to produce a string used to sign the query
    sorted_params = sorted(inputParams.items(), key=lambda val: val[0]) # ensures input params will be alphabetical
    stringifiedQueryParams = urlencode(sorted_params) # converts dictionary to query string: &param=PARAM
    stringToSign = endpoint + '?' + stringifiedQueryParams
    stringToSign.replace(' ','+')
    return stringToSign

def generateAPISignature(stringToSign):
    # Creates signature that authenticates a request
    apiSecret = config.apiSecret
    hm = hmac.new(apiSecret,'',hashlib.sha256)
    hm.update(stringToSign)
    return hm.hexdigest()

def initateRequest(requestType, endpoint, requestParams):
    # formats request based on type and initiates request
    queryString = generateQueryString(endpoint,requestParams)
    signature = generateAPISignature(queryString)
    requestParams['signature']=signature
    if requestType=='POST':
        r = requests.post('https://playgroundapi.ost.com'+ endpoint, data=requestParams)
    if requestType=='GET':
        endpointQuery = queryString + '&signature='+signature
        r = requests.get('https://playgroundapi.ost.com' + endpointQuery)
    return r

def createUser(name, log = True):
    # Creates a new user entry - interact with LOGIN UI
    # INPUT PARAMETER OPTIONS
    # name: NAME OF NEW USER
    endpoint = '/users/create'
    requestParams = {'api_key':config.apiKey,
                     'name':name,
                     'request_timestamp': int(time.time()),
                     }
    requestType = 'POST'
    r = initateRequest(requestType, endpoint, requestParams)
    if log:
        print(r.text)
    return r

def editUser(uuid, newName, log = False):
    # Edit existing user account
    # INPUT PARAMETER OPTIONS
    # uuid: Unique identifier of user to editUser
    # name: new name to assign to user profile
    endpoint = '/users/edit'
    requestParams = {'api_key':config.apiKey,
                     'name':newName,
                     'request_timestamp': int(time.time()),
                     'uuid':uuid
                     }
    queryString = generateQueryString(endpoint,requestParams)
    signature = generateAPISignature(queryString)
    requestType = 'POST'
    r = initateRequest(requestType, endpoint, requestParams)
    if log:
        print(r.text)
    return r

def listUsers(page_no = 1, order='desc', listFilter = 'all', order_by='creation_time', log=False):
    # Requests list of all users
    # INPUT PARAMETER OPTIONS
    # order: 'desc'/'asc'
    # filter: 'all'/'never_airdropped'
    # order_by: 'creation_time'/'name'
    # page_no : NUMBER
    endpoint = '/users/list'
    requestParams = {'request_timestamp': int(time.time()),
                     'api_key':config.apiKey,
                     'page_no':page_no,
                     'order':order,
                     'filter':listFilter,
                     'order_by':order_by
                     }
    r = initateRequest('GET', endpoint, requestParams)
    if log:
        pprint.pprint(r.json())
    return r

def executeAirdrop(amount = 2, list_type = 'all', log = True): #post
    # Airdrops tokens to users
    # INPUT PARAMETER OPTIONS
    # amount: Float
    # list_type: 'all'/ ??? maybe same as filter parameter for listUsers
    endpoint = '/users/airdrop/drop'
    requestParams = {'api_key':config.apiKey,
                     'amount':amount,
                     'list_type':list_type,
                     'request_timestamp': int(time.time()),
                     }
    requestType = 'POST'
    r = initateRequest(requestType, endpoint, requestParams)
    if log:
        print(r.text)
    return r



def checkAirdropStatus(airdrop_uuid, log = False): #get
    # Requests list of all users
    # INPUT PARAMETER OPTIONS
    # airdrop_uuid: ID of airdrop initiation request
    endpoint = '/users/airdrop/status'
    requestParams = {'request_timestamp': int(time.time()),
                     'api_key':config.apiKey,
                     'airdrop_uuid':airdrop_uuid
                     }
    r = initateRequest('GET', endpoint, requestParams)
    if log:
        pprint.pprint(r.json())
    return r

def createTransactionType(name = 'good looks', kind = 'user_to_user', currency_type='BT', currency_value='1', commission_percent=0.02, log = True): #post
    # Create New Transaction Type
    # INPUT PARAMETER OPTIONS
    # name: name
    # kind: 'user_to_user', 'user_to_company', 'company_to_user'
    # currency_type: 'USD', 'BT'
    # currency_value: #
    # commission_percent: only for user_to_user transactions float {0:1}
    endpoint = '/transaction-types/create'
    requestParams = {'api_key':config.apiKey,
                     'request_timestamp': int(time.time()),
                     'name':name,
                     'kind':kind,
                     'currency_type':currency_type,
                     'currency_value':currency_value,
                     'commission_percent':commission_percent
                     }
    requestType = 'POST'
    r = initateRequest(requestType, endpoint, requestParams)
    if log:
        print(r.text)
    return r

def editTransaction(client_transaction_id, name, kind, currency_type, currency_value, commission_percent, log = True):#post
    # Edit existing transaction
    # INPUT PARAMETER OPTIONS
    # client_transaction_id: ID of transaction to edit
    # name: name
    # kind: 'user_to_user', 'user_to_company', 'company_to_user'
    # currency_type: 'USD', 'BT'
    # currency_value: #
    # commission_percent: only for user_to_user transactions float {0:1}
    endpoint = '/transaction-types/edit'
    requestParams = {'api_key':config.apiKey,
                     'request_timestamp': int(time.time()),
                     'client_transaction_id':client_transaction_id,
                     'name':name,
                     'kind':kind,
                     'currency_type':currency_type,
                     'currency_value':currency_value,
                     'commission_percent':commission_percent
                     }
    requestType = 'POST'
    r = initateRequest(requestType, endpoint, requestParams)
    if log:
        print(r.text)
    return r

def listTransactions(log = True): #get
    # Generates list of all transaction types
    # INPUT PARAMETER OPTIONS
    # airdrop_uuid: ID of airdrop initiation request
    endpoint = '/transaction-types/list'
    requestParams = {'request_timestamp': int(time.time()),
                     'api_key':config.apiKey
                     }
    r = initateRequest('GET', endpoint, requestParams)
    if log:
        pprint.pprint(r.json())
    return r

def executeTransaction(from_uuid, to_uuid, transaction_kind, log = True): #post
    # Executes a transaction
    # INPUT PARAMETER OPTIONS
    # from_uuid  >> to_uuid
    # transaction_kind: name of the transaction to execute

    endpoint = '/transaction-types/execute'
    requestParams = {'api_key':config.apiKey,
                     'request_timestamp': int(time.time()),
                     'from_uuid':from_uuid,
                     'to_uuid':to_uuid,
                     'transaction_kind':transaction_kind
                     }
    requestType = 'POST'
    r = initateRequest(requestType, endpoint, requestParams)
    if log:
        print(r.text)
    return r

def checkTransactionStatus(transaction_uuids, log = True): 
    # Currently does not work. investigating
    # Outputs status of transaction
    # INPUT PARAMETER OPTIONS
    # airdrop_uuid: ID of airdrop initiation request
    endpoint = '/transaction-types/status'
    requestParams = {'request_timestamp': int(time.time()),
                     'api_key':config.apiKey,
                     'transaction_uuids[]':transaction_uuids
                     }
    requestType = 'POST'
    r = initateRequest(requestType, endpoint, requestParams)
    if log:
        print(r.text)
    return r


# Test function calls with inputs from command line.

#newUserName = raw_input("Enter new user name: ")
#createUser(name = raw_input("Enter new user name: "))
#editUser(raw_input('Enter UUID to edit: '), raw_input('Enter new name: '))
#executeAirdrop(log = True)
#listUsers(log=True)
#checkAirdropStatus(airdrop_uuid=raw_input('Airdrop UUID: '), log = True)
#createTransactionType()
#listTransactions(log=True)
#editTransaction(client_transaction_id = raw_input('ID of transaction to edit: '), name= raw_input('New transaction name: '), kind= raw_input('New transaction kind: '), currency_type= raw_input('New currency type [USD or BT]: '), currency_value= raw_input('New transaction value: '), commission_percent=raw_input('New commission percent: '))
#executeTransaction(from_uuid = raw_input('ID From: '), to_uuid=raw_input('ID To: '), transaction_kind = raw_input('Transaction type: '))
#checkTransactionStatus(transaction_uuids = raw_input('Transaction ID: ')) # only one that doesn't work
