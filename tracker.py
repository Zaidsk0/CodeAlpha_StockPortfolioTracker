# CodeAlpha Task 2: Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 330
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available stocks and prices ($):")
for stock, price in stock_prices.items():
    print(f"- {stock}: ${price}")
print("===================================\n")

while True:
    stock_name = input("Enter stock symbol (or type 'done' to finish): ").upper().strip()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Invalid stock! Please select from the list above.\n")
        continue

    try:
        shares = int(input(f"Enter number of shares for {stock_name}: "))
        if shares <= 0:
            print("Quantity must be greater than zero.\n")
            continue
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    # Update shares in portfolio
    portfolio[stock_name] = portfolio.get(stock_name, 0) + shares
    print(f"Added {shares} shares of {stock_name}.\n")

# Display results
print("\n===== Portfolio Summary =====")
if not portfolio:
    print("No stocks in portfolio.")
else:
    for stock, shares in portfolio.items():
        price = stock_prices[stock]
        stock_total = price * shares
        total_investment += stock_total
        print(f"{stock}: {shares} shares @ ${price} = ${stock_total}")

    print("-----------------------------")
    print(f"Total Investment Value: ${total_investment}")
    print("=============================")

    # Optional file export
    save_option = input("\nDo you want to save the summary to a text file? (y/n): ").lower().strip()
    if save_option == "y":
        with open("portfolio_summary.txt", "w") as file:
            file.write("===== Portfolio Summary =====\n")
            for stock, shares in portfolio.items():
                price = stock_prices[stock]
                file.write(f"{stock}: {shares} shares @ ${price} = ${price * shares}\n")
            file.write("-----------------------------\n")
            file.write(f"Total Investment Value: ${total_investment}\n")
        print("Summary saved to portfolio_summary.txt successfully!")