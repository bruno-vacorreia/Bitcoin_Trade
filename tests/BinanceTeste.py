#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 19:55:35 2020
Tutorial Binance
@author: ravi
"""
from binance.client import Client



api_key = 'NzVenBqk2rXFvpaUaHqf89jW5ySUK3GOPIjS2i4ov7IdAwuriumNUjrQnh45SZcq'

api_secret = 'yq5f4Px8eMiH9QdlOmmNVKlvUq2ysRDuaVEYmBHDMQVTlTN1tkr24iJDqMcDDSlX'


client = Client(api_key, api_secret)

# get market depth
depth = client.get_order_book(symbol='GRTUSDT')


"""
To test the connection we will make a request to get the last price for each trading pair. 
To do this we will use the get_all_tickers() function. Don’t forget to call the client first. 
The following code should return all ticker prices.
"""
# tickers = client.get_all_tickers()
# print(tickers)

# place a test market buy order, to place an actual order use the create_order

# order = client.create_test_order(
#     symbol='BNBBTC',
#     side=Client.SIDE_BUY,
#     type=Client.ORDER_TYPE_MARKET,
#     quantity=100)

# # get all symbol prices
# prices = client.get_all_tickers()

## Get system status
# status = client.get_system_status()
# print(status)

##Get Recent Trades
trades = client.get_recent_trades(symbol='GRTUSDT')
print(trades)