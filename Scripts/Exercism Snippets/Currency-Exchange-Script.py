"""
Currency Exchange Utility Functions

This script provides functions to:
- Calculate exchanged currency based on a budget and exchange rate (with optional spread/fee).
- Determine change after exchanging money.
- Compute the value and number of bills received for a given denomination.
- Find leftover currency after exchanging into bills.
- Calculate the maximum exchangeable value in whole bills, considering the spread and denomination.

Useful for simulating or automating currency exchange scenarios.
"""

def exchange_money(budget, exchange_rate):
    result = float(budget / exchange_rate)
    return result


def get_change(budget, exchanging_value):
    result = float(budget - exchanging_value)
    return result


def get_value_of_bills(denomination, number_of_bills):
    result = int(denomination * number_of_bills)
    return result


def get_number_of_bills(amount, denomination):
    result = int(amount // denomination)
    return result


def get_leftover_of_bills(amount, denomination):
    result = float(amount % denomination)
    return result

def exchangeable_value(budget, exchange_rate, spread, denomination):
    actual_rate = exchange_rate + (exchange_rate * spread / 100)
    exchanged = budget / actual_rate
    number_of_bills = int(exchanged // denomination)
    return number_of_bills * denomination
    

