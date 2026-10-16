# Made by Eleanor Pendrey
# This is a currency conversion program.


conversion_history = []

exchange_rates = {
    "GBP" : 1,
    "AUD" : 1.92,
    "EUR" : 1.19,
    "JPY" : 210.73
}


def currency_aud():
    original_rate = exchange_rates[current_currency]
    new_amount = (current_amount / original_rate)  * exchange_rates["AUD"]
    new_amount = round(new_amount, 2)
    print("Your new amount is", new_amount, "AUD")
    conversion_history.append(f"{current_amount} {current_currency} to {new_amount} AUD")

def currency_eur():
    original_rate = exchange_rates[current_currency]
    new_amount = (current_amount / original_rate) * exchange_rates["EUR"]
    new_amount = round(new_amount, 2)
    print("Your new amount is", new_amount, "EUR")
    conversion_history.append(f"{current_amount} {current_currency} to {new_amount} EUR")

def currency_jpy():
    original_rate = exchange_rates[current_currency]
    new_amount = (current_amount / original_rate) * exchange_rates["JPY"]
    new_amount = round(new_amount, 2)
    print("Your new amount is", new_amount, "JPY")
    conversion_history.append(f"{current_amount} {current_currency} to {new_amount} JPY")

def currency_gbp():
    original_rate = exchange_rates[current_currency]
    new_amount = (current_amount / original_rate) * exchange_rates["GBP"]
    new_amount = round(new_amount, 2)
    print("Your new amount is", new_amount, "GBP")
    conversion_history.append(f"{current_amount} {current_currency} to {new_amount} GBP")


continue_loop = True

while continue_loop == True:

    current_amount = float(input("Input the amount of money you'd like to convert: "))
    current_currency = input("What currency is the money currently in? AUD, EUR, JPY or GBP?").upper()
    wanted_currency = input("What currency would you like to convert to? Choose from AUD, EUR, JPY, or GBP: ").upper()

    if wanted_currency == 'AUD':
        currency_aud()

    elif wanted_currency == 'EUR':
        currency_eur()

    elif wanted_currency == 'JPY':
        currency_jpy()

    elif wanted_currency == 'GBP':
        currency_gbp()

    choice = input("Would you like to convert more money? y or n").lower()

    if choice == 'y':
        continue_loop = True

    elif choice == 'n':
        break

    else:
        print("That isn't a valid answer.")


print(f"Your conversion history is {conversion_history}")

