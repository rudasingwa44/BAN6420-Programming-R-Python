class Payment:
    """A bill for one product, owed by one policyholder."""

    def __init__(self, policyholder, product):
        self.policyholder = policyholder
        self.product = product
        self.amount_due = product.price
        self.is_paid = False

    def process_payment(self, amount_paid):
        """Pay the bill. Fails if the account is suspended or the amount is too low."""
        if not self.policyholder.is_active:
            raise ValueError(f"{self.policyholder.name}'s account is suspended.")
        if amount_paid < self.amount_due:
            raise ValueError(f"${amount_paid} is less than the ${self.amount_due} due.")
        self.is_paid = True
        self.policyholder.payments.append(self)

    def send_reminder(self):
        if not self.is_paid:
            return f"Reminder to {self.policyholder.name}: ${self.amount_due} is due for {self.product.name}."
        return f"{self.policyholder.name} has paid in full."

    def apply_penalty(self, penalty_fee):
        """Add a late fee to an unpaid bill."""
        if penalty_fee <= 0:
            raise ValueError("Penalty must be greater than 0.")
        if not self.is_paid:
            self.amount_due += penalty_fee