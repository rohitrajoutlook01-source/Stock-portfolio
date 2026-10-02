
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("=" * 45)
print("       📈 STOCK PORTFOLIO TRACKER")
print("=" * 45)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

print("\nEnter 'done' when you have finished adding stocks.\n")

while True:
    stock = input("Enter stock symbol: ").upper().strip()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not found. Please choose from the available stocks.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.\n")
            continue

        price = stock_prices[stock]
        investment = price * quantity

        portfolio[stock] = portfolio.get(stock, 0) + quantity
        total_investment += investment

        print(f"✅ {stock} added successfully.")
        print(f"Investment: ${investment}\n")

    except ValueError:
        print("❌ Please enter a valid number for quantity.\n")


# Display portfolio
print("\n" + "=" * 55)
print("              YOUR PORTFOLIO")
print("=" * 55)

print(f"{'Stock':<10}{'Quantity':<12}{'Price':<12}{'Investment'}")
print("-" * 55)

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity

    print(f"{stock:<10}{quantity:<12}${price:<11}${investment}")

print("-" * 55)
print(f"Total Investment: ${total_investment}")
print("=" * 55)


# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("=" * 40 + "\n\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity

        file.write(
            f"{stock} | Quantity: {quantity} | "
            f"Price: ${price} | Investment: ${investment}\n"
        )

    file.write("\n" + "=" * 40 + "\n")
    file.write(f"Total Investment: ${total_investment}\n")

print("\n✅ Portfolio report saved as 'portfolio.txt'")
print("Thank you for using Stock Portfolio Tracker!")