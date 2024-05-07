# Define a class representing a product
class Product:
    # Constructor to initialize product attributes
    def __init__(self, product_id, name, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    # Method to display product information
    def display_info(self):
        return f"Product ID: {self.product_id}\nName: {self.name}\nPrice: ${self.price:.2f}\nStock Quantity: {self.stock_quantity}\n"


# Define a class representing a customer
class Customer:
    # Constructor to initialize customer attributes
    def __init__(self, customer_id, name, email, address):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.address = address

    # Method to display customer information
    def display_info(self):
        return f"Customer ID: {self.customer_id}\nName: {self.name}\nEmail: {self.email}\nAddress: {self.address}\n"


# Define a class representing a shopping cart
class ShoppingCart:
    # Constructor to initialize shopping cart
    def __init__(self):
        self.items = []

    # Method to add a product to the shopping cart
    def add_item(self, product, quantity):
        if quantity > 0 and product.stock_quantity >= quantity:
            self.items.append({"product": product, "quantity": quantity})
            product.stock_quantity -= quantity
            return f"Added {quantity} {product.name}(s) to the cart."
        else:
            return "Invalid quantity or product out of stock."

    # Method to remove a product from the shopping cart
    def remove_item(self, product, quantity):
        for item in self.items:
            if item["product"] == product:
                if quantity <= item["quantity"]:
                    item["quantity"] -= quantity
                    product.stock_quantity += quantity
                    if item["quantity"] == 0:
                        self.items.remove(item)
                    return f"Removed {quantity} {product.name}(s) from the cart."
                else:
                    return "Invalid quantity to remove."
        return "Product not found in the cart."

    # Method to view the contents of the shopping cart
    def view_cart(self):
        cart_info = "Shopping Cart:\n"
        total_price = 0
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            cart_info += f"{product.name} x{quantity}: ${product.price * quantity:.2f}\n"
            total_price += product.price * quantity
        cart_info += f"Total Price: ${total_price:.2f}"
        return cart_info

    # Method to checkout and calculate total price
    def checkout(self):
        total_price = sum(item["product"].price * item["quantity"] for item in self.items)
        return total_price


# Function to create a new customer and add to the list of customers
def create_customer(customers, customer_id, name, email, address):
    new_customer = Customer(customer_id, name, email, address)
    customers.append(new_customer)
    return f"Customer created: {new_customer.name}"


# Function to find a customer by email
def find_customer_by_email(customers, email):
    return next((customer for customer in customers if customer.email == email), None)


# Main function to run the e-commerce system
def main():
    # List of available products
    products = [
        Product(1, "Laptop", 999.99, 10),
        Product(2, "Smartphone", 499.99, 15),
        Product(3, "Headphones", 49.99, 20),
    ]

    # List of customers
    customers = []

    # Main loop for the e-commerce system
    while True:
        # Display menu options
        print("\nE-commerce System")
        print("1. View Products")
        print("2. Create Customer")
        print("3. Find Customer by Email")
        print("4. Add to Cart")
        print("5. Remove from Cart")
        print("6. View Cart")
        print("7. Checkout")
        print("8. Quit")

        # Get user input for choice
        choice = input("Enter your choice (1-8): ")

        # Execute corresponding action based on user choice
        if choice == "1":
            print("\nAvailable Products:")
            for product in products:
                print(product.display_info())
        elif choice == "2":
            customer_id = input("Enter customer ID: ")
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            address = input("Enter customer address: ")
            print(create_customer(customers, customer_id, name, email, address))
        elif choice == "3":
            email = input("Enter customer email to find: ")
            customer = find_customer_by_email(customers, email)
            if customer:
                print(customer.display_info())
            else:
                print("Customer not found.")
        elif choice == "4":
            product_id = int(input("Enter the product ID to add to the cart: "))
            quantity = int(input("Enter the quantity to add: "))
            product = next((p for p in products if p.product_id == product_id), None)
            if product:
                print(cart.add_item(product, quantity))
            else:
                print("Product not found.")
        elif choice == "5":
            product_id = int(input("Enter the product ID to remove from the cart: "))
            quantity = int(input("Enter the quantity to remove: "))
            product = next((p for p in products if p.product_id == product_id), None)
            if product:
                print(cart.remove_item(product, quantity))
            else:
                print("Product not found.")
        elif choice == "6":
            print(cart.view_cart())
        elif choice == "7":
            total_price = cart.checkout()
            print(f"Checkout successful. Total amount: ${total_price:.2f}")
            cart.items = []
        elif choice == "8":
            print("Thank you for using our e-commerce system!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


# Entry point of the program
if __name__ == "__main__":
    cart = ShoppingCart()
    main()
