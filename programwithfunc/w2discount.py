def calculate_tax():
    
    sub_total = float(input("Please enter the subtotal: $"))

    tax_rate = 0.06

    from datetime import datetime
    current_date_and_time = datetime.now()

    day_of_week = current_date_and_time.weekday()

    if day_of_week == 1 or day_of_week == 2:
        discount_rate = 0.10
        discount = sub_total * discount_rate
        sub_total -= discount
        print(f"A 10% discount of {discount:.2f} $ has been applied.")
    else:
        discount = 0
        print("No discount available today.")

    tax_amount = sub_total * tax_rate

    taxed_total = sub_total + tax_amount

    print(f"Sales tax amount: {tax_amount:.2f} $")
    print(f"Total: {taxed_total:.2f} $")

calculate_tax()

