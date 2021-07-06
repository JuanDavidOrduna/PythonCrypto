from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from datetime import datetime
import json
import os

currency = 'USD'
key=os.environ.get('COINMARKETCAP_API_KEY')

url = 'https://sandbox-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'a7a49c82-2785-49d0-8307-9a684db13161',
}
parameters = {
  #'start':'1',
  #'limit':'5',
  'convert':currency,
  #'symbol':'BTC,ETH',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url,params=parameters)
  #data = json.loads(response.text)
  results = response.json()
  print(json.dumps(results,sort_keys=True,indent=4))
  
  
  active_currencies = results['data']['active_cryptocurrencies']
  active_markets = results['data']['active_market_pairs']
  bitcoin_percentage = results['data']['btc_dominance']
  last_updated = results['data']['last_updated']
  global_cap = int(results['data']['quote'][currency]['total_market_cap'])
  global_volume = int(results['data']['quote'][currency]['total_volume_24h'])

  active_currencies_string = '{:,}'.format(active_currencies)
  active_markets_string = '{:,}'.format(active_markets)
  global_cap_string = '{:,}'.format(global_cap)
  global_volume_string = '{:,}'.format(global_volume)

  #last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')
  

  print()
  print('There are currently ' + active_currencies_string + ' active cryptocurrecies and ' + active_markets_string + ' active markets.')
  print('The global cap of all cryptos is ' + global_cap_string + ' and the 24h global volume is ' + global_volume_string + '.')
  print('Bitcoin\'s total percentage of the global cap is ' + str(bitcoin_percentage) + '%.')
  print()
  print('This information was last updated on ' + last_updated + '.')
  

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)