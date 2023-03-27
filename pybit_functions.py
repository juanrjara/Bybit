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

#setStopLoss(symbol, price, order_id) is a function to set the Stop Loss value of an order in bybit using pybit library
#by: @juanrjaram
# @param symbol: symbol to set Stop Loss
# @param price: price to set Stop Loss
# @param order_id: order id to set Stop Loss
# @return: none
# @example: setStopLoss("BTCUSD", 10000, 123456789)
def setStopLoss(symbol, price, order_id):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    bybit.stop_loss(symbol=symbol, stop_px=price, order_link_id=order_id)
    print("Stop Loss set to " + str(price) + " for " + symbol + " order " + str(order_id))

#setTakeProfit(symbol, price, order_id) is a function to set the Take Profit value of an order in bybit using pybit library
#by: @juanrjaram
# @param symbol: symbol to set Take Profit
# @param price: price to set Take Profit
# @param order_id: order id to set Take Profit
# @return: none
# @example: setTakeProfit("BTCUSD", 10000, 123456789)
def setTakeProfit(symbol, price, order_id):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    bybit.take_profit(symbol=symbol, take_profit=price, order_link_id=order_id)
    print("Take Profit set to " + str(price) + " for " + symbol + " order " + str(order_id))

#cancelOrder(order_id) is a function to cancel an order in bybit using pybit library
#by: @juanrjara
# @param order_id: order id to cancel
# @return: none
# @example: cancelOrder(123456789)
def cancelOrder(order_id):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    bybit.cancel_order(order_id=order_id)
    print("Order " + str(order_id) + " cancelled")

#cancelAllOrders() is a function to cancel all orders in bybit using pybit library
#by: @juanrjaram
# @return: none
# @example: cancelAllOrders()
def cancelAllOrders():
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    bybit.cancel_all_orders()
    print("All orders cancelled")

#cancelAllOrdersBySymbol(symbol) is a function to cancel all orders of a symbol in bybit using pybit library
#by: @juanrjaram
# @param symbol: symbol to cancel all orders
# @return: none
# @example: cancelAllOrdersBySymbol("BTCUSD")
def cancelAllOrdersBySymbol(symbol):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    bybit.cancel_all_orders(symbol=symbol)
    print("All orders of " + symbol + " cancelled")

#cancelAllOrdersBySymbolAndSide(symbol, side) is a function to cancel all orders of a symbol and side in bybit using pybit library
#by: @juanrjaram
# @param symbol: symbol to cancel all orders
# @param side: side to cancel all orders
# @return: none
# @example: cancelAllOrdersBySymbolAndSide("BTCUSD", "Buy")
def cancelAllOrdersBySymbolAndSide(symbol, side):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    bybit.cancel_all_orders(symbol=symbol, side=side)
    print("All " + side + " orders of " + symbol + " cancelled")

#cancelAllOrdersBySymbolAndSideAndOrderType(symbol, side, order_type) is a function to cancel all orders of a symbol, side and order type in bybit using pybit library
#by: @juanrjaram
# @param symbol: symbol to cancel all orders
# @param side: side to cancel all orders
# @param order_type: order type to cancel all orders
# @return: none
# @example: cancelAllOrdersBySymbolAndSideAndOrderType("BTCUSD", "Buy", "Limit")
def cancelAllOrdersBySymbolAndSideAndOrderType(symbol, side, order_type):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    bybit.cancel_all_orders(symbol=symbol, side=side, order_type=order_type)
    print("All " + side + " " + order_type + " orders of " + symbol + " cancelled")

#cancelAllOrdersBySymbolAndSideAndOrderTypeAndTimeInForce(symbol, side, order_type, time_in_force) is a function to cancel all orders of a symbol, side, order type and time in force in bybit using pybit library
#by: @juanrjaram
# @param symbol: symbol to cancel all orders
# @param side: side to cancel all orders
# @param order_type: order type to cancel all orders
# @param time_in_force: time in force to cancel all orders
# @return: none
# @example: cancelAllOrdersBySymbolAndSideAndOrderTypeAndTimeInForce("BTCUSD", "Buy", "Limit", "GoodTillCancel")
def cancelAllOrdersBySymbolAndSideAndOrderTypeAndTimeInForce(symbol, side, order_type, time_in_force):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    bybit.cancel_all_orders(symbol=symbol, side=side, order_type=order_type, time_in_force=time_in_force)
    print("All " + side + " " + order_type + " " + time_in_force + " orders of " + symbol + " cancelled")

#cancelAllOrdersBySymbolAndSideAndOrderTypeAndTimeInForceAndOrderStatus(symbol, side, order_type, time_in_force, order_status) is a function to cancel all orders of a symbol, side, order type, time in force and order status in bybit using pybit library
#by: @juanrjaram
# @param symbol: symbol to cancel all orders
# @param side: side to cancel all orders
# @param order_type: order type to cancel all orders
# @param time_in_force: time in force to cancel all orders
# @param order_status: order status to cancel all orders
# @return: none
# @example: cancelAllOrdersBySymbolAndSideAndOrderTypeAndTimeInForceAndOrderStatus("BTCUSD", "Buy", "Limit", "GoodTillCancel", "New")
def cancelAllOrdersBySymbolAndSideAndOrderTypeAndTimeInForceAndOrderStatus(symbol, side, order_type, time_in_force, order_status):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    bybit.cancel_all_orders(symbol=symbol, side=side, order_type=order_type, time_in_force=time_in_force, order_status=order_status)
    print("All " + side + " " + order_type + " " + time_in_force + " " + order_status + " orders of " + symbol + " cancelled")
    
#cancelAllOrdersBySymbolAndSideAndOrderTypeAndTimeInForceAndOrderStatusAndOrderLinkID(symbol, side, order_type, time_in_force, order_status, order_link_id) is a function to cancel all orders of a symbol, side, order type, time in force, order status and order link id in bybit using pybit library
#by: @juanrjaram
# @param symbol: symbol to cancel all orders
# @param side: side to cancel all orders
# @param order_type: order type to cancel all orders
# @param time_in_force: time in force to cancel all orders
# @param order_status: order status to cancel all orders
# @param order_link_id: order link id to cancel all orders
# @return: none
# @example: cancelAllOrdersBySymbolAndSideAndOrderTypeAndTimeInForceAndOrderStatusAndOrderLinkID("BTCUSD", "Buy", "Limit", "GoodTillCancel", "New", "123456789")
def cancelAllOrdersBySymbolAndSideAndOrderTypeAndTimeInForceAndOrderStatusAndOrderLinkID(symbol, side, order_type, time_in_force, order_status, order_link_id):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    bybit.cancel_all_orders(symbol=symbol, side=side, order_type=order_type, time_in_force=time_in_force, order_status=order_status, order_link_id=order_link_id)
    print("All " + side + " " + order_type + " " + time_in_force + " " + order_status + " " + order_link_id + " orders of " + symbol + " cancelled")

#cancelAllOrdersBySymbolAndSideAndOrderTypeAndTimeInForceAndOrderStatusAndOrderLinkIDAndOrderID(symbol, side, order_type, time_in_force, order_status, order_link_id, order_id) is a function to cancel all orders of a symbol, side, order type, time in force, order status, order link id and order id in bybit using pybit library
#by: @juanrjaram
# @param symbol: symbol to cancel all orders
# @param side: side to cancel all orders
# @param order_type: order type to cancel all orders
# @param time_in_force: time in force to cancel all orders
# @param order_status: order status to cancel all orders
# @param order_link_id: order link id to cancel all orders
# @param order_id: order id to cancel all orders
# @return: none
# @example: cancelAllOrdersBySymbolAndSideAndOrderTypeAndTimeInForceAndOrderStatusAndOrderLinkIDAndOrderID("BTCUSD", "Buy", "Limit", "GoodTillCancel", "New", "123456789", "123456789")
def cancelAllOrdersBySymbolAndSideAndOrderTypeAndTimeInForceAndOrderStatusAndOrderLinkIDAndOrderID(symbol, side, order_type, time_in_force, order_status, order_link_id, order_id):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    bybit.cancel_all_orders(symbol=symbol, side=side, order_type=order_type, time_in_force=time_in_force, order_status=order_status, order_link_id=order_link_id, order_id=order_id)
    print("All " + side + " " + order_type + " " + time_in_force + " " + order_status + " " + order_link_id + " " + order_id + " orders of " + symbol + " cancelled")

#getAllOrdersBySymbol(symbol) is a function to get all orders of a symbol in bybit using pybit library
#by: @juanrjaram
# @param symbol: symbol to get all orders
# @return: all orders of a symbol
# @example: getAllOrdersBySymbol("BTCUSD")
def getAllOrdersBySymbol(symbol):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    orders = bybit.get_all_orders(symbol=symbol)
    print(orders)

#getAllOrdersBySymbolAndSide(symbol, side) is a function to get all orders of a symbol and side in bybit using pybit library
#by: @juanrjaram
# @param symbol: symbol to get all orders
# @param side: side to get all orders
# @return: all orders of a symbol and side
# @example: getAllOrdersBySymbolAndSide("BTCUSD", "Buy")
def getAllOrdersBySymbolAndSide(symbol, side):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    orders = bybit.get_all_orders(symbol=symbol, side=side)
    print(orders)

#getOpenOrdersBySymbol(symbol) is a function to get open orders of a symbol in bybit using pybit library
#by: @juanrjaram
# @param symbol: symbol to get open orders
# @return: open orders of a symbol
# @example: getOpenOrdersBySymbol("BTCUSD")
def getOpenOrdersBySymbol(symbol):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    orders = bybit.get_open_orders(symbol=symbol)
    print(orders)

#getOpenOrdersBySymbolAndSide(symbol, side) is a function to get open orders of a symbol and side in bybit using pybit library
#by: @juanrjaram
# @param symbol: symbol to get open orders
# @param side: side to get open orders
# @return: open orders of a symbol and side
# @example: getOpenOrdersBySymbolAndSide("BTCUSD", "Buy")
def getOpenOrdersBySymbolAndSide(symbol, side):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    orders = bybit.get_open_orders(symbol=symbol, side=side)
    print(orders)

#getOrderBookBySymbol(symbol) is a function to get order book of a symbol in bybit using pybit library
#by: @juanrjaram
# @param symbol: symbol to get order book
# @return: order book of a symbol
# @example: getOrderBookBySymbol("BTCUSD")
def getOrderBookBySymbol(symbol):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    order_book = bybit.get_order_book(symbol=symbol)
    print(order_book)

#getOpenPositions() is a function to get open positions in bybit using pybit library
#by: @juanrjaram
# @return: open positions
# @example: getOpenPositions()
def getOpenPositions():
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    open_positions = bybit.get_open_positions()
    print(open_positions)

#getOpenPositionsBySymbol(symbol) is a function to get open positions of a symbol in bybit using pybit library
#by: @juanrjaram
# @param symbol: symbol to get open positions
# @return: open positions of a symbol
# @example: getOpenPositionsBySymbol("BTCUSD")
def getOpenPositionsBySymbol(symbol):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    bybit = pybit.Bybit(api_key=api_key, api_secret=api_secret)
    open_positions = bybit.get_open_positions(symbol=symbol)
    print(open_positions)
    