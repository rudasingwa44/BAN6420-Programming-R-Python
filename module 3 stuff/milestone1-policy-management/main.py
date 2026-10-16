from product import Product
from policyholder import Policyholder
from payment import Payment

# 1. Create a product
health_plan = Product(product_id=101, name="Premium Health", price=500)

# 2. Register two policyholders and sell them the product
alice = Policyholder(member_id=1, name="Alice Smith")
bob = Policyholder(member_id=2, name="Bob Jones")
for person in [alice, bob]:
    person.register()
    person.buy_product(health_plan)

# 3. Both pay for the product
Payment(alice, health_plan).process_payment(500)
Payment(bob, health_plan).process_payment(500)

# 4. Display account details
alice.display_account()
bob.display_account()

# 5. Demonstrate the other methods and error handling
print("--- Other features ---")
carol = Policyholder(member_id=3, name="Carol White")
carol.register()
carol.buy_product(health_plan)
carol_bill = Payment(carol, health_plan)
print(carol_bill.send_reminder())
carol_bill.apply_penalty(50)
print("After late penalty:", carol_bill.send_reminder())

# Error handling: each of these should be blocked
try:
    carol_bill.process_payment(100)            # too little
except ValueError as error:
    print("Error:", error)

bob.suspend()
try:
    Payment(bob, health_plan).process_payment(500)   # suspended account
except ValueError as error:
    print("Error:", error)
bob.reactivate()
print("Bob reactivated:", bob.is_active)

health_plan.update_price(550)
print("New price:", health_plan.price)
health_plan.suspend()
try:
    alice.buy_product(health_plan)             # suspended product
except ValueError as error:
    print("Error:", error)