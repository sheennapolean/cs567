import unittest

# Importing the classes and functions to be tested from the shopping module
from shopping import Product, Customer, ShoppingCart, create_customer, find_customer_by_email

# Test case for the Product class
class TestProduct(unittest.TestCase):
    # Test case for the display_info method of the Product class
    def test_display_info(self):
        # Creating a Product object with test data
        product = Product(1, "Laptop", 999.99, 10)
        # Expected output string for the display_info method
        expected_output = "Product ID: 1\nName: Laptop\nPrice: $999.99\nStock Quantity: 10\n"
        # Asserting that the actual output matches the expected output
        self.assertEqual(product.display_info(), expected_output)

# Test case for the Customer class
class TestCustomer(unittest.TestCase):
    # Test case for the display_info method of the Customer class
    def test_display_info(self):
        # Creating a Customer object with test data
        customer = Customer(1, "John Doe", "john@example.com", "123 Main St")
        # Expected output string for the display_info method
        expected_output = "Customer ID: 1\nName: John Doe\nEmail: john@example.com\nAddress: 123 Main St\n"
        # Asserting that the actual output matches the expected output
        self.assertEqual(customer.display_info(), expected_output)

# Test case for the ShoppingCart class
class TestShoppingCart(unittest.TestCase):
    # Method to set up the test environment before each test case
    def setUp(self):
        # Creating Product objects for testing
        self.product1 = Product(1, "Laptop", 999.99, 10)
        self.product2 = Product(2, "Smartphone", 499.99, 15)
        # Creating a ShoppingCart object for testing
        self.cart = ShoppingCart()

    # Test case for adding items to the shopping cart with a valid quantity
    def test_add_item_valid_quantity(self):
        self.assertEqual(self.cart.add_item(self.product1, 5), "Added 5 Laptop(s) to the cart.")

    # Test case for adding items to the shopping cart with an invalid quantity
    def test_add_item_invalid_quantity(self):
        self.assertEqual(self.cart.add_item(self.product1, 15), "Invalid quantity or product out of stock.")

    # Test case for removing items from the shopping cart with a valid quantity
    def test_remove_item_valid_quantity(self):
        self.cart.add_item(self.product1, 5)
        self.assertEqual(self.cart.remove_item(self.product1, 3), "Removed 3 Laptop(s) from the cart.")

    # Test case for removing items from the shopping cart with an invalid quantity
    def test_remove_item_invalid_quantity(self):
        self.cart.add_item(self.product1, 5)
        self.assertEqual(self.cart.remove_item(self.product1, 8), "Invalid quantity to remove.")

    # Test case for removing items from the shopping cart when the product is not found
    def test_remove_item_product_not_found(self):
        self.assertEqual(self.cart.remove_item(self.product2, 3), "Product not found in the cart.")

    # Test case for viewing the contents of the shopping cart
    def test_view_cart(self):
        self.cart.add_item(self.product1, 3)
        self.cart.add_item(self.product2, 2)
        expected_output = "Shopping Cart:\nLaptop x3: $2999.97\nSmartphone x2: $999.98\nTotal Price: $3999.95"
        self.assertEqual(self.cart.view_cart(), expected_output)

    # Test case for checking out the shopping cart and calculating the total price
    def test_checkout(self):
        self.cart.add_item(self.product1, 3)
        self.cart.add_item(self.product2, 2)
        self.assertAlmostEqual(self.cart.checkout(), 3999.95, places=2)

# Test case for the create_customer function
class TestCreateCustomer(unittest.TestCase):
    # Test case for creating a new customer
    def test_create_customer(self):
        customers = []
        result = create_customer(customers, 1, "John Doe", "john@example.com", "123 Main St")
        self.assertEqual(result, "Customer created: John Doe")
        self.assertEqual(len(customers), 1)

    # Test case for creating a new customer with a duplicate ID
    def test_create_customer_duplicate_id(self):
        customers = [Customer(1, "John Doe", "john@example.com", "123 Main St")]
        result = create_customer(customers, 1, "Jane Smith", "jane@example.com", "456 Elm St")
        self.assertEqual(result, "Customer created: Jane Smith")
        self.assertEqual(len(customers), 2)

    # Test case for finding a customer by email
    def test_find_customer_by_email(self):
        customers = [Customer(1, "John Doe", "john@example.com", "123 Main St")]
        customer = find_customer_by_email(customers, "john@example.com")
        self.assertIsNotNone(customer)
        self.assertEqual(customer.name, "John Doe")

    # Test case for finding a customer by email when not found
    def test_find_customer_by_email_not_found(self):
        customers = [Customer(1, "John Doe", "john@example.com", "123 Main St")]
        customer = find_customer_by_email(customers, "jane@example.com")
        self.assertIsNone(customer)

# Entry point to run the tests
if __name__ == "__main__":
    unittest.main()
