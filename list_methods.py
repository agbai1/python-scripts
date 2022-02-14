#!/usr/bin/env python3

VINIX = ['C', 'MA', 'BA', 'PG', 'CSCO', 'VZ', 'PFE', 'HD', 'INTC', 'T', 'V', 'UNH', 'WFC', 'CVX', 'BAC', 'JNJ', 'GOOGL', 'GOOG', 'BRK.B', 'XOM', 'JPM', 'FB', 'AMZN', 'MSFT', 'AAPL']

STOCK_NAMES = VINIX

print("VINIX stocks: " + str(VINIX))
print('\n')
print("STOCK_NAMES stocks: " + str(STOCK_NAMES))
print('\n')

STOCK_NAMES[1] = 'NETLX'

print("VINIX stocks: " + str(VINIX))
print('\n')
print("STOCK_NAMES stocks: " + str(STOCK_NAMES))
print('\n')
print('\n')

#testing ist methods

# Use this playground to experiment with list methods, using Test Run

home_items = sorted(["Lamp","shleves","table","sofa"])
print("\n".join(home_items))

home_items.append("vase")
print(home_items)

home_items.append("mugs")

print(home_items)

print(home_items[-3:])

