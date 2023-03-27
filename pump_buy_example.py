#This is an example of how to use pybit_functions and IS NOT A TRADING BOT so use at your own risk
#It gets all USDT base tickers from Bybit API and if the price of a ticker is greater than 1.03 times the average of the last 9 prices, then buy (PUMP Detected)

#Must run pip install requests and pip install numpy
import requests
import numpy as np
import json
import datetime
import time
import decimal
import pybit_functions as mypybit

# set the quantity in USD to invest in each trade
qtyinusdt = 10
# set the minimum price change to consider a pump valid (grater the value, less pumps will be detected)
pumprate = 1.03

# create a dictionary with the symbols info as keys and empty lists as values
jsoninfo = {}
# This is the URL of the Bybit API symbols info endpoint
urlinfo = "https://api.bybit.com/spot/v3/public/symbols"
# get the result from the API endpoint
resultinfo = requests.get(urlinfo)
# convert the result to a JSON object
jsonresultinfo = resultinfo.json()
# get the list of tickers info
lastInfo = jsonresultinfo['result']['list']
# create a dictionary with the symbols info as keys and empty lists as values
for info in lastInfo:
    # get the number of decimals to round the quantity to buy
    d = decimal.Decimal(info['basePrecision'])
    dround = abs(d.as_tuple().exponent)
    jsoninfo[info['name']] = dround

# create a dictionary with the symbols as keys and empty lists as values
jsonsymb = {}
# This is the URL of the Bybit API
url = "https://api.bybit.com/spot/v3/public/quote/ticker/price"
# get the result from the API endpoint
result = requests.get(url)
# convert the result to a JSON object
jsonresult = result.json()
# get the list of tickers
lastTickers = jsonresult['result']['list']
# create a dictionary with the symbols as keys and empty lists as values
for symbol in lastTickers:
    jsonsymb[symbol['symbol']] = []

# loop forever
while True:
    try:
        # get the result from the API endpoint
        result = requests.get(url)
        # convert the result to a JSON object
        jsonresult = result.json()
        # get the list of tickers
        lastTickers = jsonresult['result']['list']
        # loop through the list of tickers
        for symbol in lastTickers:
            # if the symbol is in the dictionary, append the price to the list
            if (symbol['symbol'] in jsonsymb) and ('USDT' in symbol['symbol']):
                # if the list has less than 10 elements, append the price
                if len(jsonsymb[symbol['symbol']])<10:
                    jsonsymb[symbol['symbol']].append(float(symbol['price']))
                # if the list has 10 elements, append the price and remove the first element (FIFO)
                else:
                    jsonsymb[symbol['symbol']].append(float(symbol['price']))
                    jsonsymb[symbol['symbol']].pop(0)
                    values = ",".join(map(str, jsonsymb[symbol['symbol']]))
                    
                    # if the price is greater than 1.03 times the average of the last 9 prices, then buy (PUMP Detected)
                    if float(symbol['price']) > 1.03*(np.max(jsonsymb[symbol['symbol']][:-1])):
                        mypybit.buyMarketPybit(symbol['symbol'], round(jsoninfo[symbol['symbol']],qtyinusdt/float(symbol['price'])))
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f") +  " - "+ symbol['symbol'] +" - buy at: " + str(symbol['price']))
                    else:
                        pass        
            # if the symbol is not in the dictionary, do nothing     
            else:
                pass
                
    # if there is an error, print the error     
    except Exception as e:
        print(e)

    # wait 1 second before the next loop
    time.sleep(1)