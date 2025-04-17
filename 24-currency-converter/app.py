import requests
def main():
    print("\n Simple Currency Converter")
    print(" Getting exchange rates ")

    try:
        response = requests.get("https://open.er-api.com/v6/latest/USD")
        rates = response.json()["rates"]
        print(" Exchange rates fetched successfully.")
    except:
        print("Error: Unable to fetch exchange rates.")
        return
    
    print("\n Popular: USD EUR GBP JPY")

    while True:
        print("\n Enter details:")
        from_currency = input(" From currency (USD): ").upper()
        if from_currency not in rates:
            print("Error: Invalid {from_currency} currency.")
            continue

        to_currency = input(" To currency (EUR): ").upper()
        if to_currency not in rates:
            print("Error: Invalid {to_currency} currency.")
            continue
        try:
            amount = float(input(f" Amount in {from_currency}: "))
        except:
            print("Error: Invalid amount.")
            continue

        amount_in_usd = amount / rates[from_currency]
        converted_amount = amount_in_usd * rates[to_currency]

        print(f"Rate: {amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        print(f"Rate: {rates[to_currency] / rates[from_currency]:.4f} {to_currency} per {from_currency}")

        if input(" Convert again? (y/n): ").lower().startswith("y"):
            print(" Thanks for using the currency converter!")
            break


main()