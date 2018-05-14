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
    inputParams['api_key']=config.apiKey
    inputParams['request_timestamp'] = int(time.time())
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

def initiateRequest(requestType, endpoint, requestParams):
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
