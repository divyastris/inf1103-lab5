import json
import os

FILENAME = "inventory.json"


# ---------- Phase 1: display ----------
def display_all(inventory):
    print("Current Inventory")
    print("------------------------------------------------")
    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | "
              f"Price: ${product['price']:.2f} | Stock: {product['stock']}")
    print("------------------------------------------------")


# ---------- Phase 2: load and save ----------
def load_inventory():
    if os.path.exists(FILENAME):
        print("inventory.json found.")
        with open(FILENAME, "r") as file:
            inventory = json.load(file)
        print("Inventory loaded successfully.")
        return inventory
    print("No inventory.json found. Starting with empty inventory.")
    return []


def save_inventory(inventory):
    with open(FILENAME, "w") as file:
        json.dump(inventory, file, indent=4)
    print("Inventory saved successfully to inventory.json.")


# ---------- Phase 3: add, update, search ----------
def add_product(inventory):
    print("Add New Product")
    new_id = input("Product ID: ")
    new_name = input("Product Name: ")
    new_price = float(input("Price: "))
    new_stock = int(input("Stock Quantity: "))
    inventory.append({"id": new_id, "name": new_name,
                      "price": new_price, "stock": new_stock})
    print("\nProduct added successfully!")


def update_stock(inventory):
    print("Update Stock")
    search_id = input("Enter Product ID: ")
    for product in inventory:
        if product["id"] == search_id:
            print("\nProduct Found:")
            print("Name:", product["name"])
            print("Current Stock:", product["stock"])
            product["stock"] = int(input("\nNew Stock Quantity: "))
            print("\nStock updated successfully!")
            return
    print("\nProduct not found.")


def search_product(inventory):
    print("Search Product")
    search_id = input("Enter Product ID: ")
    for product in inventory:
        if product["id"] == search_id:
            print("\nProduct Found")
            print("------------------------------------------------")
            print("ID:", product["id"])
            print("Name:", product["name"])
            print(f"Price: ${product['price']:.2f}")
            print("Stock:", product["stock"])
            print("------------------------------------------------")
            return
    print("\nProduct not found.")


# ---------- Phase 4: menu ----------
def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)
    print()
    inventory = load_inventory()

    while True:
        print()
        print("----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")
        choice = input("\nEnter option: ")
        print()

        if choice == "1":
            display_all(inventory)
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            print("Saving inventory...")
            save_inventory(inventory)
        elif choice == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please try again.")


main()