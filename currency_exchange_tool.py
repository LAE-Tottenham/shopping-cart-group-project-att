import math # you'll probably need this

exchange_rates = {
    'USD': 1.13, #I.E. 1 Pound is 1.13 Dollars
    'EUR': 1.15,
    'CAD': 1.80,
    'LEK': 118.00,
    'VND': 324220.09,
}

def check_currency_exists(currency):
    return

def currency_convert(new_c, amount):
    conversion_rate=exchange_rates.get(new_c)
    total=amount*conversion_rate
    total=round(total,2)
    print(total)
    return total

