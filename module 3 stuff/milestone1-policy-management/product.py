class Product:
    """An insurance product (e.g. a health plan) that policyholders can buy."""

    def __init__(self, product_id, name, price):
        if price <= 0:
            raise ValueError("Price must be greater than 0.")
        self.product_id = product_id
        self.name = name
        self.price = price
        self.is_suspended = False

    def update_price(self, new_price):
        """Change the product price (must be positive)."""
        if new_price <= 0:
            raise ValueError("Price must be greater than 0.")
        self.price = new_price

    def suspend(self):
        """Stop the product from being sold."""
        self.is_suspended = True

    def reactivate(self):
        """Make a suspended product available again."""
        self.is_suspended = False