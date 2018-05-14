# Test function calls with inputs from command line.
# Uncomment the controls to

import ostAPI

user = ostAPI.User()
airdrop = ostAPI.Airdrop()
t = ostAPI.Transactions()



#user.create(name = raw_input("Enter new user name: "))
#user.edit(raw_input('Enter UUID to edit: '), raw_input('Enter new name: '))
user.list(log=True)


#airdrop.execute(amount = raw_input('Enter airdrop amount'), log = True)
#airdrop.checkStatus(airdrop_uuid=raw_input('Airdrop UUID: '), log = True)


#t.create(name = raw_input('New transaction type name: '), kind= raw_input('New transaction kind (user_to_user, user_to_company, company_to_user): '), currency_type= raw_input('Currency type (USD, BT): '), currency_value= raw_input('Value of transaction: '), commission_percent= raw_input('Commission percent only if user-to-user: '), log = True)
t.list(log=True)
#t.edit(client_transaction_id = raw_input('ID of transaction to edit: '), name= raw_input('New transaction name: '), kind= raw_input('New transaction kind: '), currency_type= raw_input('New currency type [USD or BT]: '), currency_value= raw_input('New transaction value: '), commission_percent=raw_input('New commission percent: '))
#t.execute(from_uuid = raw_input('ID From: '), to_uuid=raw_input('ID To: '), transaction_kind = raw_input('Transaction type: '))
#t.checkStatus(transaction_uuids = raw_input('Transaction ID: ')) # only one that doesn't work
