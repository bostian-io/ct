import csv

sales_data = []

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["quantity"] = int(row["quantity"])
        row["price"] = float(row["price"])
        row["revenue"] = row["quantity"] * row["price"]
        sales_data.append(row)

# We want to calculate these totals in one pass. Start with zero values and empty dictionaries and loop through the sales data to update them as we go. This approach makes more sense to me than doing multiple passes through for different dictionaries.
total_revenue = 0
product_revenue = {}
product_quantity = {}
day_revenue = {}

print("\n=== Sales Info ===")
print(f"{'Date':<12}{'Product':<10}{'Qty':>5}{'Price':>10}{'Revenue':>11}")

for i in sales_data:
    print(f"{i['date']:<12}{i['product']:<10}{i['quantity']:>5}{i['price']:>10.2f}{i['revenue']:>11.2f}")

    total_revenue += i["revenue"]

    product = i["product"]
    if product not in product_revenue:
        product_revenue[product] = 0
        product_quantity[product] = 0
    product_revenue[product] += i["revenue"]
    product_quantity[product] += i["quantity"]

    day = i["date"]
    if day not in day_revenue:
        day_revenue[day] = 0
    day_revenue[day] += i["revenue"]

best_day = None
best_day_revenue = 0
for day, revenue in day_revenue.items():
    if revenue > best_day_revenue:
        best_day_revenue = revenue
        best_day = day

print("\n=== Product Totals ===")
for product in product_revenue:
    print(f"{product}: {product_quantity[product]} sold, ${product_revenue[product]:.2f}")

print(f"\nTotal revenue: ${total_revenue:.2f}")
print(f"Best day: {best_day} with ${best_day_revenue:.2f}")

# write formatted summary to a new text file
with open("sales_report.txt", "w") as file:
    file.write("=== Sales Info ===\n")
    file.write(f"{'Date':<12}{'Product':<10}{'Qty':>5}{'Price':>10}{'Revenue':>11}\n")
    for i in sales_data:
        file.write(f"{i['date']:<12}{i['product']:<10}{i['quantity']:>5}{i['price']:>10.2f}{i['revenue']:>11.2f}\n")

    file.write("\n=== Product Totals ===\n")
    for product in product_revenue:
        file.write(f"{product}: {product_quantity[product]} sold, ${product_revenue[product]:.2f}\n")

    file.write(f"\nTotal revenue: ${total_revenue:.2f}\n")
    file.write(f"Best day: {best_day} with ${best_day_revenue:.2f}\n")

# write formatted summary to a new CSV file
with open("product_summary.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["product", "total_quantity", "total_revenue"])
    writer.writeheader()
    for product in product_revenue:
        writer.writerow({
            "product": product,
            "total_quantity": product_quantity[product],
            "total_revenue": round(product_revenue[product], 2), # added rounding to 2 decimal places for better formatting
        })