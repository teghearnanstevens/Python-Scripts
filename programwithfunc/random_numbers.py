import random

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        random_num = round(random.uniform(0, 100), 1)  # Generate and round random number
        numbers_list.append(random_num)

def main():
    numbers = [16.2, 75.1, 52.3]
    print("Initial numbers list:", numbers)
    
    # Add one random number
    append_random_numbers(numbers)
    print("After adding one random number:", numbers)
    
    # Add three random numbers
    append_random_numbers(numbers, 3)
    print("After adding three random numbers:", numbers)

if __name__ == "__main__":
    main()