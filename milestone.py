def calculate_subtotal(child_price, adult_price, num_children, num_adults):
   
    subtotal = (child_price * num_children) + (adult_price * num_adults)
    print("Subtotal: $", subtotal)

child_price = float(input("Enter the price of a child's meal: $"))
adult_price = float(input("Enter the price of an adult's meal: $"))

num_children = int(input("Enter the number of children: "))
num_adults = int(input("Enter the number of adults: "))

calculate_subtotal(child_price, adult_price, num_children, num_adults)