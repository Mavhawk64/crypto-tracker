with open('api-key.txt') as f:
	coinmarketcap_key = f.readlines()[0].strip() # something like 'a123b45c-6de7-8fg9-01h2-3ij4kl56m789'
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

# url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' # testing
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' # prod
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': coinmarketcap_key,
}

session = Session()
session.headers.update(headers)
f2 = open("sample_output.json", "w")
try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(json.dumps(data['data'][0],indent=2))
  f2.write(json.dumps(data, indent=2))
except (ConnectionError, Timeout, TooManyRedirects) as e:
  f2.write(e)
