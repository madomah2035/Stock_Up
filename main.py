from prettytable import PrettyTable
import json


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        return (f"Product: {self.name}, Price: {self.price:.2f}, Quantity: {self.quantity}, "
                f"Total: {self.price * self.quantity:.2f}")


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def modify_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                try:
                    new_price = float(input(f"Enter the new price for {product_name}: "))
                    new_quantity = int(input(f"Enter the new quantity for {product_name}: "))
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    return

                if new_price <= 0 or new_quantity <= 0:
                    print("Price and quantity must be positive values.")
                    return

                product.price = new_price
                product.quantity = new_quantity
                print(f"{product_name} modified successfully!")
                return

        print(f"Product with name {product_name} not found.")

    def display_inventory(self):
        print("\nInventory:")

        stock = PrettyTable()
        stock.field_names = ["Product/Item", "Price(GHS)", "Quantity", "Total(GHS)"]

        for product in self.products:
            stock.add_row(product.display_info())

        if self.products:
            print(stock)
        else:
            print("No products in the inventory.")

    def save_inventory(self, filename="Material_Stock.json"):
        data = [product.display_info() for product in self.products]
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_inventory(self, filename="Material_Stock.json"):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.products = [Product(item["Product"], item["Price"], item["Quantity"]) for item in data]
        except FileNotFoundError:
            print(f"No existing inventory file found. Starting with an empty inventory.")


def main():
    inventory = Inventory()
    inventory.load_inventory()

    while True:
        print("\nOptions:")
        print("1. Add Product")
        print("2. Display Inventory")
        print("3. Modify Product")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            try:
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if price <= 0 or quantity <= 0:
                print("Price and quantity must be positive values.")
                continue

            new_product = Product(name, price, quantity)
            inventory.add_product(new_product)
            print("Product added successfully!")

        elif choice == '2':
            inventory.display_inventory()

        elif choice == '3':
            product_name = input("Enter the name of the product to modify: ")
            inventory.modify_product(product_name)

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
