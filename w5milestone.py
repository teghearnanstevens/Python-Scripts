shopping_cart = []

def add_item():
    item_name = input("What item would you like to add? ")
    shopping_cart.append(item_name)
    print(f"'{item_name}' has been added to the cart.\n")

def display_cart():
    if not shopping_cart:
        print("Your shopping cart is empty.\n")
    else:
        print("Contents of your shopping cart:")
        for index, item in enumerate(shopping_cart, start=1):
            print(f"{index}. {item}")
        print()

def main():
    print("Welcome to the Shopping Cart Program!\n")
    while True:
        print("Please select one of the following options:")
        print("1. Add item to cart")
        print("2. View shopping cart")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")
        print()

        if choice == '1':
            add_item()
        elif choice == '2':
            display_cart()
        elif choice == '3':
            print("Thank you for using the Shopping Cart Program. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()