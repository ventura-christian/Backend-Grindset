# def exchange_money(budget, exchange_rate):
#     result = float(budget / exchange_rate)
#     return result


# def get_change(budget, exchanging_value):
#     result = float(budget - exchanging_value)
#     return result


# def get_value_of_bills(denomination, number_of_bills):
#     result = int(denomination * number_of_bills)
#     return result


# def get_number_of_bills(amount, denomination):
#     result = int(amount // denomination)
#     return result


# def get_leftover_of_bills(amount, denomination):
#     result = float(amount % denomination)
#     return result

# LEFT OFF HERE. Function not completed. 
def exchangeable_value(budget, exchange_rate, spread, denomination):
    result = int(budget * exchange_rate) + spread / denomination
    spread = spread / 100
    return int(result)
    

    """
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

print(exchangeable_value(127.25, 1.20, 10, 20))