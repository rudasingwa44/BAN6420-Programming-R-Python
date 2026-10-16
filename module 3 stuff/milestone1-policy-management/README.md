# Milestone 1 – Policy Management System for an Insurance Company

A Python object-oriented system that manages **policyholders**, **insurance
products** and **payments**. Policy managers can register, suspend and reactivate
policyholders; create, update and suspend products; and process payments with
reminders and late penalties.

## Files
| File | Contents |
|---|---|
| `product.py` | `Product` class – create, update price, suspend, reactivate |
| `policyholder.py` | `Policyholder` class – register, suspend, reactivate, buy products, display account |
| `payment.py` | `Payment` class – process payment, send reminder, apply penalty |
| `main.py` | Demonstration that uses all three classes |

Each class is in its own file, and `main.py` imports them.

## Requirements
- Python 3 (no extra packages needed)

## How to run
1. Keep all four `.py` files in the same folder.
2. Open a terminal in that folder and run:

python main.py

   Or open `main.py` in VS Code and click **Run** (▷).

## How it works
- **Product:** created with an ID, name and price. The price must be greater
  than 0. Products can have their price updated, and can be suspended (no
  longer sold) or reactivated.
- **Policyholder:** starts inactive and becomes active with `register()`.
  Accounts can be suspended and reactivated. Only an active policyholder can
  buy a product, and only if the product is not suspended.
- **Payment:** a bill for one product, owed by one policyholder. The amount due
  is taken from the product price. Payment is accepted only if the account is
  active and the amount paid covers the amount due. Successful payments are
  saved to the policyholder's account.
- **Reminders:** `send_reminder()` tells the policyholder the amount due if the
  bill is unpaid.
- **Penalties:** `apply_penalty(fee)` adds a late fee to an unpaid bill.

## Demonstration (`main.py`)
1. Creates the product **Premium Health** ($500).
2. Registers **Alice Smith** and **Bob Jones**, who both buy and pay for the product.
3. Displays both account details.
4. Shows the other features with a third customer, **Carol White**, who has not
   paid: a reminder, a $50 late penalty, and an updated reminder.
5. Shows the error handling:
   - paying less than the amount due is rejected
   - a suspended policyholder cannot pay (Bob is suspended, then reactivated)
   - a suspended product cannot be bought (after a price update to $550)

## Expected output

Member ID: 1 | Name: Alice Smith | Status: Active
Product: Premium Health ($500)
Payment: $500 for Premium Health - Paid: True
Member ID: 2 | Name: Bob Jones | Status: Active
Product: Premium Health ($500)
Payment: $500 for Premium Health - Paid: True

--- Other features ---
Reminder to Carol White: $500 is due for Premium Health.
After late penalty: Reminder to Carol White: $550 is due for Premium Health.
Error: $100 is less than the $550 due.
Error: Bob Jones’s account is suspended.
Bob reactivated: True
New price: 550
Error: Premium Health is currently suspended.


**Author:** Ivan