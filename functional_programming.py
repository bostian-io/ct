products = [
    {"name": "Laptop", "price": 999.99, "category": "electronics", "in_stock": True},
    {"name": "Python Book", "price": 39.99, "category": "books", "in_stock": True},
    {"name": "Headphones", "price": 149.99, "category": "electronics", "in_stock": False},
    {"name": "Desk Lamp", "price": 29.99, "category": "home", "in_stock": True},
    {"name": "AI Textbook", "price": 89.99, "category": "books", "in_stock": True},
    {"name": "Monitor", "price": 349.99, "category": "electronics", "in_stock": True},
    {"name": "Notebook", "price": 4.99, "category": "office", "in_stock": True},
    {"name": "Keyboard", "price": 79.99, "category": "electronics", "in_stock": False},
]

in_stock = [product for product in products if product["in_stock"]]

discounted_10_percent = [{**p, "price": round(p["price"]*0.9, 2)} for p in products]

under_200_electronics = [product for product in products if product["price"] < 200 and product["category"] == "electronics"]

sorted_by_price = sorted(products, key=lambda p: p["price"])

total = round(sum(product["price"] for product in in_stock), 2)

products_by_category = {
    category: [product for product in products if product["category"] == category] for category in sorted({p["category"] for p in products})
}

summary = (
    f"Total products: {len(products)}\n"
    f"In-stock products: {len(in_stock)}\n"
    f"Total price of in-stock products: ${total}\n"
    f"Products by category:\n" +
    "\n".join(f"{category}: {len(products_by_category[category])} products" for category in products_by_category)
)

print(summary)

# printed results
"""
Total products: 8
In-stock products: 6
Total price of in-stock products: $1514.94
Products by category:
books: 2 products
electronics: 4 products
home: 1 products
office: 1 products
"""