def main():
    print(calculate(10, 5, 'add'))
    print(calculate_2(10, 5, 'divide'))

def calculate(num1, num2, add_operator):
    add_operator = num1 + num2
    return add_operator

def calculate_2(num3, num4, div_operator):
    div_operator = num3 / num4
    return div_operator

main()