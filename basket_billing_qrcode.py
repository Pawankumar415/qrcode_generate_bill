
import qrcode

data = {
    'apple': 35,
    'mango': 50,
    'pineapple': 20,
    'banana': 5,
    'cherry': 15,
    'strawberry': 25
}

basket = {}  # Stores {fruit_name: {'quantity': qty, 'total_price': price}}



# Function to add items to basket
def add_to_basket():
    while True:
        print("\n Current Basket:", basket if basket else "Empty")
        action = input("\nDo you want to 'add', 'remove' an item or 'exit' to finalize purchase? ").strip().lower()

        if action == 'exit':
            print("Thank you for shopping with us! ")
            break

        elif action == 'add':
            name = input("Enter fruit name: ").strip().lower()
            if name not in data:
                print("Fruit not found! Please enter a valid fruit name.")
                continue

            quantity = input(f"Enter quantity of {name.capitalize()}: ").strip()
            if not quantity.isdigit() or int(quantity) <= 0:
                print("Invalid quantity. Please enter a positive number.")
                continue

            quantity = int(quantity)
            if name in basket:
                basket[name]['quantity'] += quantity
            else:
                basket[name] = {'quantity': quantity}

            basket[name]['total_price'] = basket[name]['quantity'] * data[name]
            print(f"{quantity} {name}(s) added.")

        elif action == 'remove':
            remove_from_basket()

        else:
            print("Invalid option! Please enter 'add', 'remove', or 'exit'.")

    return basket


# Function to remove items from the basket
def remove_from_basket():
    if not basket:
        print("Your basket is already empty!")
        return

    name = input("Enter the fruit name to remove: ").strip().lower()
    if name not in basket:
        print("Fruit not found in your basket!")
        return

    quantity = input(
        f"Enter quantity to remove from {name.capitalize()} (or type 'all' to remove completely): ").strip()

    if quantity.lower() == 'all':
        del basket[name]
        print(f"Removed all {name}s from your basket.")
    elif quantity.isdigit() and int(quantity) > 0:
        quantity = int(quantity)
        if quantity >= basket[name]['quantity']:
            del basket[name]
            print(f"Removed all {name}s from your basket.")
        else:
            basket[name]['quantity'] -= quantity
            basket[name]['total_price'] = basket[name]['quantity'] * data[name]
            print(f"Removed {quantity} {name}(s).")
    else:
        print("Invalid quantity! Please enter a positive number or 'all'.")


# Function to generate bill
def generate_bill():
    if not basket:
        print("Your basket is empty. No bill generated!")
        return None

    print("\n**Final Bill** ")
    total_amount = 0
    bill_text = "Final Bill \n\n"

    for fruit, details in basket.items():
        qty = details['quantity']
        price = details['total_price']
        total_amount += price
        bill_text += f"{fruit.capitalize()} - {qty} x {data[fruit]} = ₹{price}\n"

    bill_text += f"\n**Total Amount: ₹{total_amount}** "
    print(bill_text)

    return bill_text


# Function to generate QR Code
def generate_qr_code(bill_text):
    if not bill_text:
        return

    qr = qrcode.make(bill_text)
    qr.save("final_bill.png")
    print("QR Code Generated! Scan 'final_bill.png' to view your bill.")


# Run the functions
add_to_basket()
bill_text = generate_bill()
generate_qr_code(bill_text)