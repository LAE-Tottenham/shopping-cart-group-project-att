import math # you'll probably need this

exchange_rates = {
    'USD': 1.13, #I.E. 1 Pound is 1.13 Dollars
    'EUR': 1.15,
    "ALL": 118.39,
    "VND": 32617.15,
    
}

def check_currency_exists():
    currency = input("Choose a desired currency(USD,EUR,CAD,ALL,VND): ")
    if not currency.isalpha():
        print(" Invalid format ")
    if currency.upper() in exchange_rates:
        return (f"{currency.upper()}")
    else:
        print ("Currency unavailable")
    
check_currency_exists()    
def currency_convert(original_c, new_c, amount):
    # your code here
    return
