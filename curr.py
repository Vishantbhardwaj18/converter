# Define exchange rates
exchange_rates = {
    'USD': 1.0,        # Base currency
    'EUR': 0.85,      # Euro
    'JPY': 110.0,     # Japanese Yen
    'GBP': 0.75,      # British Pound
    'AUD': 1.35,      # Australian Dollar
    'INR': 84.0       # Indian Rupee
}

def convert_currency(amount, from_currency, to_currency):
    # Convert the amount from the base currency (USD) to the target currency
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Invalid currency!"
    
    # Convert amount to USD first
    amount_in_usd = amount / exchange_rates[from_currency]
    
    # Convert from USD to the target currency
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    
    return converted_amount

def main():
    print("Welcome to the Currency Converter!")
    
    # Get user input
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the currency to convert from (USD, EUR, JPY, GBP, AUD, INR): ").upper()
    to_currency = input("Enter the currency to convert to (USD, EUR, JPY, GBP, AUD, INR): ").upper()
    
    # Perform conversion
    converted_amount = convert_currency(amount, from_currency, to_currency)
    
    if isinstance(converted_amount, str):
        print(converted_amount)  # Print error message
    else:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
