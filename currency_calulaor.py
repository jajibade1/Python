import requests

def get_exchange_rates(base_currency):
    api_url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()["rates"]
    else:
        raise Exception("Failed to fetch exchange rates.")

def convert_currency(amount, from_currency, to_currency):
    rates = get_exchange_rates(from_currency)
    if to_currency not in rates:
        raise Exception(f"Currency '{to_currency}' not found in the exchange rates.")
    
    exchange_rate = rates[to_currency]
    converted_amount = amount * exchange_rate
    return converted_amount

def main():
    print("Currency Converter")
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency code you want to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency code you want to convert to (e.g., EUR): ").upper()

    try:
        converted_amount = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
