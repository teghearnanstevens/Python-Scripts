import math

def trapezoid_area(h, B, b):
    # Formula to calculate the area of the trapezoid
    A = 0.5 * h * (B + b)
    # Round the result to the nearest whole number
    return round(A, 1)

height = float(input("What is the height?: "))
base1 = float(input("What is the first base?: "))
base2 = float(input("What is the second base?: "))

area = trapezoid_area(height, base1, base2)
print(f"The area of the trapezoid is: {area} square inches")