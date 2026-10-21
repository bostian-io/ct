inventory = {
    "laptop": {"price": 999.99, "quantity": 15},
    "mouse": {"price": 29.99, "quantity": 50},
    "mouse_pad": {"price": 12.99, "quantity": 15},
    "ps5": {"price": 299.99, "quantity": 8} 
}
low_stock = set()

for item_name, info in inventory.items():
    if info["quantity"] < 10:
        low_stock.add(item_name)

def display_inventory():
    """Display entire inventory in a formatted table, including inventory totals."""
    print("=" * 30)
    print("===== Item Inventory =====")
    print("=" * 30)

    print(f"\n{'Item Name':<10}{'Price':<10}{'Quantity':<10}{'Total Inventory':<10}")
    for item_name, info in inventory.items():
        total_item_inventory = info["price"] * info["quantity"]
        print(f"{item_name:<10}{info['price']:<10}{info['quantity']:<10}{total_item_inventory:<10}")
        if item_name in low_stock:
            print(f"\n{item_name} low stock!") # adding this to alert users of low stock from the low_stock set

display_inventory()

search = input("\nEnter the name of the product you're looking for. ").lower()

current_inventory = inventory.get(search)

if current_inventory:
    print(f"\nFound: {search}")
    print(f"Currently we have {current_inventory['quantity']} in stock, priced at ${current_inventory['price']}.")
    quantity_update = input(f"\nWould you like to update the quantity of {search}? ").lower() # added this nested here because anyone that would want to update quantity on something would have to first look up the item
    if quantity_update == "yes":
        try:
            new_quantity = int(input("Enter a whole number for the new quantity: "))
            inventory[search]["quantity"] = new_quantity
            print(f"Updated to {new_quantity}.")
        except ValueError:
            print("That's not a whole number, so quantity was not changed.")
    elif quantity_update == "no":
        print("No changes made.")
    else:
        print("Please answer yes or no.")
else:
    print(f"Sorry. Seems we don't have {search} in our inventory.")

