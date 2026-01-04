"""
TEC102 Fundamentals of Programming - Assessment 1
Program: Shopping Cart Total Calculator

Specifications:
- Prompt user to enter price and quantity for up to 10 items.
- Apply 10% discount if subtotal > $100.
- Add $5 delivery fee if total after discount < $50.
- Display subtotal, discount, delivery fee, and final total.
- Input validation included.
- Uses only Lessons 1–4 concepts.
"""

def get_positive_float(prompt):
    """Prompt for a positive floating-point number."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Price must be greater than 0.")
            else:
                return value
        except ValueError:
            print("Error: Please enter a valid number.")

def get_positive_int(prompt):
    """Prompt for a positive integer."""
    while True:
        value = input(prompt)
        if value.isdigit():
            value = int(value)
            if value > 0:
                return value
            else:
                print("Error: Quantity must be greater than 0.")
        else:
            print("Error: Please enter a whole number.")

def ask_yes_no(prompt):
    """Ask user a yes/no question."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in ("y", "yes"):
            return True
        elif choice in ("n", "no"):
            return False
        else:
            print("Please enter 'y' or 'n'.")

def main():
    print("=== Shopping Cart Total Calculator ===")
    print("You can enter up to 10 items.\n")

    subtotal = 0.0
    item_count = 0

    while item_count < 10:
        price = get_positive_float(f"Enter price for item {item_count + 1}: $")
        quantity = get_positive_int(f"Enter quantity for item {item_count + 1}: ")

        line_total = price * quantity
        subtotal += line_total
        item_count += 1

        print(f"Item total: ${line_total:.2f}")
        print(f"Current subtotal: ${subtotal:.2f}\n")

        if item_count < 10:
            if not ask_yes_no("Do you want to add another item? (y/n): "):
                break
        else:
            print("Maximum item limit reached.")

    # Discount calculation
    discount = 0.0
    if subtotal > 100:
        discount = subtotal * 0.10

    total_after_discount = subtotal - discount

    # Delivery fee calculation
    delivery_fee = 0.0
    if total_after_discount < 50 and subtotal > 0:
        delivery_fee = 5.0

    final_total = total_after_discount + delivery_fee

    # Output summary
    print("\n=== Checkout Summary ===")
    print(f"Items entered: {item_count}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Delivery fee: +${delivery_fee:.2f}")
    print(f"Final total: ${final_total:.2f}")
    print("\nThank you for shopping!")

if __name__ == "__main__":
    main()
