class Policyholder:
    """A customer who owns insurance products and makes payments."""

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.is_active = False
        self.products = []
        self.payments = []

    def register(self):
        """Activate a new policyholder's account."""
        self.is_active = True

    def suspend(self):
        self.is_active = False

    def reactivate(self):
        self.is_active = True

    def buy_product(self, product):
        """Add a product, but only if the account and product are both active."""
        if not self.is_active:
            raise ValueError(f"{self.name}'s account is not active.")
        if product.is_suspended:
            raise ValueError(f"{product.name} is currently suspended.")
        self.products.append(product)

    def display_account(self):
        """Print the policyholder's account details."""
        status = "Active" if self.is_active else "Suspended"
        print(f"Member ID: {self.member_id} | Name: {self.name} | Status: {status}")
        for product in self.products:
            print(f"  Product: {product.name} (${product.price})")
        for payment in self.payments:
            print(f"  Payment: ${payment.amount_due} for {payment.product.name} - Paid: {payment.is_paid}")
        print("-" * 40)