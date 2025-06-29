import json
import os

fruit_store = {}

def load_fruit_data():
    if os.path.exists("fruit_store.txt"):
        with open("fruit_store.txt", "r") as file:
            data = json.load(file)
            return data
    return {}

def save_fruit_data():
    with open("fruit_store.txt", "w") as file:
        json.dump(fruit_store, file)

def add_fruit():
    name = input("Enter the fruit name: ").capitalize()
    price = int(input("Please enter the price per Kg: "))
    quantity = int(input("Enter the quantity: "))

    if name in fruit_store:
        fruit_store[name]['quantity'] += quantity
        fruit_store[name]['price'] = price
        print(f"\nUpdated {name} with new stock and price.")
    else:
        fruit_store[name] = {'price': price, 'quantity': quantity}
        print(f"Added new fruit {name} to stock.")

    save_fruit_data()

def view_stock():
    if not fruit_store:
        print("Fruits are not available in stock.")
        return

    print("\nFruits available in stock:")
    print(f"{'Fruit':<12}{'Price':<10}{'Quantity':<10}")
    for fruit, details in fruit_store.items():
        print(f"{fruit:<12}{details['price']:<10}{details['quantity']:<10}")

def update_fruit():
    name = input("Enter fruit name to update: ").capitalize()

    if name not in fruit_store:
        print(f"\nFruit {name} not found in stock.")
        return

    price_input = input("Enter new price (leave blank to keep same price): ")
    quantity_input = input("Enter new quantity (leave blank to keep same): ")

    if price_input:
        fruit_store[name]['price'] = int(price_input)

    if quantity_input:
        fruit_store[name]['quantity'] = int(quantity_input)

    print(f"\nFruit {name} updated successfully.")
    save_fruit_data()

def manager():
    while True:
        print("\n--- Manager Menu ---")
        print("1. Add Fruit to Stock")
        print("2. View All Fruits")
        print("3. Update Fruit")
        print("4. Back to Main Menu")

        choice = int(input("Enter choice: "))

        if choice == 1:
            add_fruit()
        elif choice == 2:
            view_stock()
        elif choice == 3:
            update_fruit()
        elif choice == 4:
            break
        else:
            print("Invalid option.")

def customer_menu():
    while True:
        print("\n--- Customer Menu ---")
        print("1. View Fruits")
        print("2. Back to Main Menu")

        choice = int(input("Enter choice (1-2): "))
        if choice == 1:
            view_stock()
        elif choice == 2:
            break
        else:
            print("Invalid input.")

def main():
    global fruit_store
    fruit_store = load_fruit_data()

    while True:
        print("\nWelcome to Fruit Store ")
        print("1. Manager")
        print("2. Customer")
        print("3. Exit")

        choice = int(input("Enter choice (1-3): "))

        if choice == 1:
            manager()
        elif choice == 2:
            customer_menu()
        elif choice == 3:
            print("\nThank you! Visit again.")
            break
        else:
            print("Invalid choice.")

main()
