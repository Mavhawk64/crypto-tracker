import discord
import random

def get_bad_message_lol():
	li = ['much noob', 'very silly', 'silly boi', 'foolish mortal', 'try again']
	return '```' + li[random.randint(0, len(li)-1)] + '```'

with open('api-key.txt') as f:
	token = f.readlines()[1].strip()

with open('api-key.txt') as f:
	coinmarketcap_key = f.readlines()[0].strip() # something like 'a123b45c-6de7-8fg9-01h2-3ij4kl56m789'
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' # testing
# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' # prod
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': coinmarketcap_key,
}

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$help'):
    	msg = '**HELP:**\n\n'
    	msg += '**Specific Crypto:** Type **$** followed by any cryptocurrency\'s symbol/ticker. (i.e. $BTC)\n'
    	msg += '**Random Crypto:** Type **$random**\n'
    	msg += '**Help Menu:** Type **$help**\n'
    	await message.reply(msg)
    	return
    if message.content.startswith('$'):
    	session = Session()
    	session.headers.update(headers)
    	# print(session.headers)
    	try:
    		response = session.get(url, params=parameters)
    		data = json.loads(response.text)
    		idNum = -1
    		#Obtain the idNum value with lookup.
    		d = data['data']
    		if message.content.upper() == '$RANDOM' or message.content.upper() == '$RAND':
    			idNum = random.randint(0,len(d)-1)
    		else:
	    		for i in range(0,len(d)):
	    			if message.content.upper() == '$' + d[i]['symbol']:
	    				idNum = i
	    				break

    		if idNum == -1:
    			await message.channel.send(get_bad_message_lol())
    			return
    		ticker = d[idNum]['symbol']
    		name = d[idNum]['name']
    		# print(name + ' ' + ticker)
    		retmes = '```The Price of ' + name + ' (' + ticker + ') is $' + str(data['data'][idNum]['quote']['USD']['price'])
    	except (ConnectionError, Timeout, TooManyRedirects) as e:
    		retmes = '```I had an error!\nContact Crypto Bot Developers with Error.\n' + e

    	if len(retmes) > 2000:
    		retmes = retmes[:1980] + '\nToo long...'
    	retmes += '```'
    	await message.channel.send(retmes)



client.run(token)