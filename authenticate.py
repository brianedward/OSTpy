import requests
import json
import time
from urllib import urlencode
import hmac
import hashlib
import pprint
import config # create a file called 'config.py' and put your api key and secret key in here. Create another file called '.gitignore' and type 'config.py' to keep your private info from being shared


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




#newUserName = raw_input("Enter new user name: ")
createUser()
#editUser(raw_input('Enter UUID to edit: '), raw_input('Enter new name: '))
#listUsers()
