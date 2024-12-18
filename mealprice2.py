def calculate_meal_price(child_price, adult_price, num_children, num_adults, store_name, promo_code=None):
    
    subtotal = (child_price * num_children) + (adult_price * num_adults)
    print("Subtotal: $", subtotal)

    sales_tax_rate = float(input("Enter the sales tax rate (as a percentage): "))
    
    sales_tax = subtotal * (sales_tax_rate / 100)
    print("Sales Tax: $", sales_tax)

    #I added this to calculate coupons that many times people have. So I thought it would be a good idea to include it!
    if promo_code:
        promo_discount = 0
        if "10%" in promo_code:
            promo_discount = 0.10 * subtotal
        elif "20%" in promo_code:
            promo_discount = 0.20 * subtotal
        subtotal -= promo_discount
        print("Promo Discount: $", promo_discount)

    total_price = subtotal + sales_tax
    print("Total Price: $", total_price)

    payment_amount = float(input("Enter the payment amount: $"))

    change = payment_amount - total_price
    print("Change: $", change)

child_price = float(input("Enter the price of a child's meal: $"))
adult_price = float(input("Enter the price of an adult's meal: $"))
num_children = int(input("Enter the number of children: "))
num_adults = int(input("Enter the number of adults: "))
store_name = input("Enter the name of the store: ")
promo_code = input("Enter discount if any (an example 10% off or 20% off): ")

calculate_meal_price(child_price, adult_price, num_children, num_adults, promo_code)