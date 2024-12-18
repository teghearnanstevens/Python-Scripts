def check_distributive_property():
    
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))

    left_side = a * (b + c)
    right_side = a * b + a * c

    print(f"Original form: {a} * ({b} + {c}) = {a} * {b} + {a} * {c}")
    print(f"Expanded form: {left_side} = {right_side}")

    if left_side == right_side:
        print("This equation follows the distributive property.")
    else:
        print("This equation does not follow the distributive property.")

check_distributive_property()