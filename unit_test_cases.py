import unittest

from shopping import Product, Customer, ShoppingCart, create_customer, find_customer_by_email

class TestProduct(unittest.TestCase):
    def test_display_info(self):
        product = Product(1, "Laptop", 999.99, 10)
        expected_output = "Product ID: 1\nName: Laptop\nPrice: $999.99\nStock Quantity: 10\n"
        self.assertEqual(product.display_info(), expected_output)

class TestCustomer(unittest.TestCase):
    def test_display_info(self):
        customer = Customer(1, "John Doe", "john@example.com", "123 Main St")
        expected_output = "Customer ID: 1\nName: John Doe\nEmail: john@example.com\nAddress: 123 Main St\n"
        self.assertEqual(customer.display_info(), expected_output)

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.product1 = Product(1, "Laptop", 999.99, 10)
        self.product2 = Product(2, "Smartphone", 499.99, 15)
        self.cart = ShoppingCart()

    def test_add_item_valid_quantity(self):
        self.assertEqual(self.cart.add_item(self.product1, 5), "Added 5 Laptop(s) to the cart.")

    def test_add_item_invalid_quantity(self):
        self.assertEqual(self.cart.add_item(self.product1, 15), "Invalid quantity or product out of stock.")

    def test_remove_item_valid_quantity(self):
        self.cart.add_item(self.product1, 5)
        self.assertEqual(self.cart.remove_item(self.product1, 3), "Removed 3 Laptop(s) from the cart.")

    def test_remove_item_invalid_quantity(self):
        self.cart.add_item(self.product1, 5)
        self.assertEqual(self.cart.remove_item(self.product1, 8), "Invalid quantity to remove.")

    def test_remove_item_product_not_found(self):
        self.assertEqual(self.cart.remove_item(self.product2, 3), "Product not found in the cart.")

    def test_view_cart(self):
        self.cart.add_item(self.product1, 3)
        self.cart.add_item(self.product2, 2)
        expected_output = "Shopping Cart:\nLaptop x3: $2999.97\nSmartphone x2: $999.98\nTotal Price: $3999.95"
        self.assertEqual(self.cart.view_cart(), expected_output)

    def test_checkout(self):
        self.cart.add_item(self.product1, 3)
        self.cart.add_item(self.product2, 2)
        self.assertAlmostEqual(self.cart.checkout(), 3999.95, places=2)

class TestCreateCustomer(unittest.TestCase):
    def test_create_customer(self):
        customers = []
        result = create_customer(customers, 1, "John Doe", "john@example.com", "123 Main St")
        self.assertEqual(result, "Customer created: John Doe")
        self.assertEqual(len(customers), 1)

    def test_create_customer_duplicate_id(self):
        customers = [Customer(1, "John Doe", "john@example.com", "123 Main St")]
        result = create_customer(customers, 1, "Jane Smith", "jane@example.com", "456 Elm St")
        self.assertEqual(result, "Customer created: Jane Smith")
        self.assertEqual(len(customers), 2)

    def test_find_customer_by_email(self):
        customers = [Customer(1, "John Doe", "john@example.com", "123 Main St")]
        customer = find_customer_by_email(customers, "john@example.com")
        self.assertIsNotNone(customer)
        self.assertEqual(customer.name, "John Doe")

    def test_find_customer_by_email_not_found(self):
        customers = [Customer(1, "John Doe", "john@example.com", "123 Main St")]
        customer = find_customer_by_email(customers, "jane@example.com")
        self.assertIsNone(customer)

if __name__ == "__main__":
    unittest.main()
