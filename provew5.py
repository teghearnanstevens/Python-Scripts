
shopping_cart = []
budget = None

def add_item():
    global budget  
    item_name = input("What item would you like to add? ")
    item_price = float(input(f"What is the price of {item_name}? $"))
    shopping_cart.append((item_name, item_price))
    print(f"'{item_name}' (${item_price:.2f}) has been added to the cart.\n")
    if budget is not None:
        print(f"Budget: ${budget:.2f}\n")  
    return sum(item[1] for item in shopping_cart)

def display_cart():
    global budget
    if not shopping_cart:
        print("Your shopping cart is empty.\n")
        return 0
    else:
        print("Contents of your shopping cart:")
        total = 0
        for index, (item, price) in enumerate(shopping_cart, start=1):
            print(f"{index}. {item} (${price:.2f})")
            total += price
        print(f"\nTotal: ${total:.2f}")
        if budget is not None:
            print(f"Budget: ${budget:.2f}\n")
        else:
            print("\n")
        return total

def remove_item():
    if display_cart():
        while True:
            try:
                index_to_remove = int(input("Enter the index of the item you want to remove: "))
                if 1 <= index_to_remove <= len(shopping_cart):
                    removed_item = shopping_cart.pop(index_to_remove - 1)
                    print(f"'{removed_item[0]}' has been removed from the cart.\n")
                    break
                else:
                    print("Invalid index. Please enter a valid index.\n")
            except ValueError:
                print("Invalid input. Please enter a valid integer index.\n")

#I added this budget to help people like me stay within their means. If you type in your budget it will remember and display it when adding an item and when reviewing the cart.
def budget_main():
    global budget
    while True:
        try:
            if budget is None:
                budget = float(input("What is your budget today? $"))
                if budget < 0:
                    print("Invalid input. Please enter a non-negative number.")
                else:
                    break
            else:
                print(f"Your budget for today is: ${budget:.2f}")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to the Shopping Cart Program!\n")
    total_spent = 0  
    while True:
        print("Please select one of the following options:")
        print("1. Add item to cart")
        print("2. View shopping cart")
        print("3. Remove item from cart")
        print("4. Sum total")
        print("5. Budget tracker")
        print("6. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")
        print()

        if choice == '1':
            total_spent = add_item()
        elif choice == '2':
            display_cart()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            total_spent = display_cart()  
        elif choice == '5':
            budget_main() 
        elif choice == '6':
            print("Thank you for using the Shopping Cart Program. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a valid option.\n")

if __name__ == "__main__":
    main()