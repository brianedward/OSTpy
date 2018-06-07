# Test function calls with inputs from command line.
# Uncomment the controls to

import ostAPI
import config
import random
import pprint
import json

users = ostAPI.Users()
airdrops = ostAPI.Airdrops()
actions = ostAPI.Actions()
transactions = ostAPI.Transactions()
goodlooks = ostAPI.Token()
transfers = ostAPI.Transfer()


### EXAMPLES ###
# set to True or False to toggle on/off examples


### USERS ###
# Create a user
if False:
    create_user_params = {
        'name':'whatschill'
    }
    new_user = users.create(create_user_params)
    pprint.pprint(new_user.json())
# Update a user
if False:
    update_user_params = {
        'name':'NEWER NAME'
    }
    updated_user = user.update(update_user_params, uuid=raw_input('Enter UUID to edit: '), log = True)
    pprint.pprint(updated_user.json())
# List users
if False:
    list_user_params = {
        'airdropped':'false',
        'page_no':1,
        'order_by':'created',
        'order':'desc',
        'limit':'10',
        #'id':raw_input('Enter UUID: ')
        #'id':'OPTIONAL COMMA SEPERATED LIST OF UUIDS'
    }
    user_list = user.list(list_user_params, log=True)
    pprint.pprint(user_list.json())
# Retrieves information about specific user
if False:
    uuid_to_retrieve=raw_input('Enter UUID to retrieve: ')
    retrieved_user = user.retrieve(uuid_to_retrieve)
    pprint.pprint(retrieved_user.json())

### AIRDROP ###
#Execute airdrop
#https://dev.ost.com/docs/api_airdrop_execute.html
if False:
    execute_airdrop_params = {
                 'amount':'1',
                 #***OPTIONAL***
                 #'user_ids':'',
                 #'airdropped':'true'
                 }
    execute_airdop = airdrop.execute(execute_airdrop_params)
    pprint.pprint(execute_airdop.json())
# Retrieve information about an airdrop
# https://dev.ost.com/docs/api_airdrop_retrieve.html
if False:
    airdrop_uuid=raw_input('Airdrop UUID: ')
    retrieved_airdrop = airdrop.retrieve(airdrop_uuid)
    pprint.pprint(retrieved_airdrop.json())
# List airdrops
# https://dev.ost.com/docs/api_airdrop_list.html
if False:
    list_airdrop_params = {
                     'page_no':1,
                     'order_by':'created',
                     'order':'desc',
                     'limit':'10',
                     # OPTIONAL FILTERS#
                     #'id':'', Comma-seperated list of airdrop uuids to read,
                     #'current_status': '' complete or pending
                     }
    airdrop_list = airdrop.list(list_airdrop_params)
    pprint.pprint(airdrop_list.json())

### ACTIONS ###
# Create new action
# https://dev.ost.com/docs/api_actions_create.html
if False:
    create_action_params = {
        'name':'good mothafuckin looks',
        'kind':'user_to_company',
        'currency':'BT',
        'arbitrary_amount':'true',
        'amount':'10',
        'arbitrary_commission':'true',
        'commission_percent':'0.01'
    }
    create_action = actions.create(create_action_params)
    pprint.pprint(create_action.json())

# Update existing action
# https://dev.ost.com/docs/api_actions_update.html
if False:
    update_action_params = {
        'name':'newnametransaction',
        'kind':'user_to_company',
        'currency':'BT',
        'arbitrary_amount':'true',
        'amount':'10',
        'arbitrary_commission':'true',
        'commission_percent':'0.01'
    }
    action_id = raw_input('Enter action ID to update: ')
    update_action = actions.update(update_action_params, action_id)
    pprint.pprint(update_action.json())

# List actions
# https://dev.ost.com/docs/api_actions_list.html
if False:
    list_action_params = {
        'page_no':1,
        'order_by':'created',
        'order':'desc',
        'limit':'10',
        # OPTIONAL:
        #'id':'12345,67890',
        #'name': 'Like, Upvote',
        #'kind':'company_to_user',
        #'arbitrary_amount':'false'
    }
    action_list = actions.list(list_action_params)
    pprint.pprint(action_list.json())

# Retrieve an action
# https://dev.ost.com/docs/api_actions_retrieve.html
if False:
    action_uuid = 'action UUID'
    retrieve_action = actions.retrieve(action_uuid)
    pprint.pprint(retrieve_action.json())

# Executes a transactions
# https://dev.ost.com/docs/api_action_execute.html
if False:
    execute_transaction_params = {
        'from_user_id':'enter from UUID',
        'to_user_id': 'enter to UUID,
        'action_id': 37005,
        # OPTIONAL - depending on action definition
        'amount':1,
        #'commission_percent':''
    }
    execute_transaction = transactions.execute(execute_transaction_params)
    pprint.pprint(execute_transaction.json())

# Retrieve a Transaction
# https://dev.ost.com/docs/api_transaction_retrieve.html
if False:
    transaction_id = 'transaction UUID'
    retrieve_transaction = transactions.retrieve(transaction_id)
    pprint.pprint(retrieve_transaction.json())

# List transactions
# https://dev.ost.com/docs/api_transaction_list.html
if False:
    list_transaction_params = {
        'page_no':1,
        'order_by':'created',
        'order':'desc',
        'limit':'10',
        # OPTIONAL
        #'id':''
    }
    list_transaction = transactions.list(list_transaction_params)
    pprint.pprint(list_transaction.json())

# Create Transfer - OST Prime
# https://dev.ost.com/docs/api_transfers_create.html
if False:
    create_transfer_params = {
        'to_address':'',
        'amount':''
    }
    new_transfer = transfers.create(create_transfer_params)
    pprint.pprint(new_transfer.json())

# List transfers
# https://dev.ost.com/docs/api_transfers_list.html
if False:
    list_transfer_params = {
            'page_no':1,
            'order_by':'created',
            'order':'desc',
            'limit':'10',
        }
    transfer_list = transfers.list(list_transfer_params)
    pprint.pprint(transfer_list.json())
# Retrieve Transfer
# https://dev.ost.com/docs/api_transfers_retrieve.html
if False:
    retrieve_transfer = transfers.retrieve(transfer_id = 'ENTER ID HERE')

### TOKEN INFO ###
if True:
    token_info = goodlooks.getInfo()
    pprint.pprint(token_info.json())
