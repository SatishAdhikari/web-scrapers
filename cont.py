import contextio as c 
import contextio1
from contextio1 import *
from prettytable import PrettyTable

CONSUMER_KEY = '1gxbnjou'										# context.io API key
CONSUMER_SECRET = 'pU5pszGSWPa2nGWv'							# context.io API secret

        ####################################################
        ## OAuth Requests to Context.IO's version 2.0 API ##
        ####################################################

conn = contextio1.ContextIO(CONSUMER_KEY, CONSUMER_SECRET)

result, data = conn.request('POST', 'connect_tokens', {'callback_url':'https://api.context.io/connect/oauth2callback'})

#print result
#print "="*50
print data['browser_redirect_url']

#print data['uuid']

contextio_token = raw_input('contextio_token : ')

result, user = conn.request('GET', 'connect_tokens/'+contextio_token)
#print data['account']['email']
#print result
#print "="*50

print user['first_name'] + ' ' + user['last_name']
print user['email']

#print data

result, data = conn.request('GET', 'https://api.context.io/connect/oauth2callback', {'file_name':'test.pdf'})

# If the result from the API is not content-type: application/json, the raw body is returned instead of a
# the parsed json object
result, link = conn.request('GET', 'https://api.context.io/connect/oauth2callback', {'as_link':1})

#print link

        ###################################
        ## Querying the API for accounts ##
        ###################################

context_io = c.ContextIO(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)

accounts = context_io.get_accounts(email=user['email'])

if accounts:
	account = accounts[0]

id = account.id 																				               
params = {'id': id}

account = c.Account(context_io, params)
contacts = account.get_contacts(limit=300)

pt = PrettyTable(field_names=['Name', 'E-mail ID'])
pt.align='l'

[pt.add_row((contacts[i].name, contacts[i].email))
for i in range(len(contacts))]

print pt




















