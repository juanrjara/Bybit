#Most common functions in bybit using pybit library
#by: @juanrjaram
import pybit

#setLeverage(symbol, leverage) is a function to set the leverage of a symbol in bybit using pybit library
#by: @juanrjaram
# @param symbol: symbol to set leverage
# @param leverage: leverage to set
# @return: none
# @example: setLeverage("BTCUSD", 5)
def setLeverage(symbol, leverage):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    bybit.set_leverage(symbol=symbol, leverage=leverage)
    print("Leverage set to " + str(leverage) + " for " + symbol)

#buyMarketPybit(symbol, qty) is a function to put a buy order of Market type in bybit using pybit library
#by: @juanrjaram
# @param symbol: symbol to buy
# @param qty: quantity to buy
# @return: order id
# @example: buyMarketPybit("BTCUSD", 0.001)
def buyMarketPybit(symbol, qty):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    order = bybit.buy(symbol=symbol, qty=qty, order_type="Market")
    print(order)
    return order['result']['order_id']    

#sellMarketPybit(symbol, qty) is a function to put a sell order of Market type in bybit using pybit library
#by: @juanrjaram
# @param symbol: symbol to sell
# @param qty: quantity to sell
# @return: order id
# @example: sellMarketPybit("BTCUSD", 0.001)
def sellMarketPybit(symbol, qty):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    order = bybit.sell(symbol=symbol, qty=qty, order_type="Market")
    print(order)
    return order['result']['order_id']

#buyLimitPybit(symbol, qty, price) is a function to put a buy order of Limit type in bybit using pybit library
#by: @juanrjaram
# @param symbol: symbol to buy
# @param qty: quantity to buy
# @param price: price to buy
# @return: order id
# @example: buyLimitPybit("BTCUSD", 0.001, 10000)
def buyLimitPybit(symbol, qty, price):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    order = bybit.buy(symbol=symbol, qty=qty, price=price, order_type="Limit")
    print(order)
    return order['result']['order_id']

#sellLimitPybit(symbol, qty, price) is a function to put a sell order of Limit type in bybit using pybit library
#by: @juanrjaram
# @param symbol: symbol to sell
# @param qty: quantity to sell
# @param price: price to sell
# @return: order id
# @example: sellLimitPybit("BTCUSD", 0.001, 10000)
def sellLimitPybit(symbol, qty, price):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    order = bybit.sell(symbol=symbol, qty=qty, price=price, order_type="Limit")
    print(order)
    return order['result']['order_id']
