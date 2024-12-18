number_list = []

while True:
    number = input("Enter a number, type '0' when finished: ")

    if number == "0":
        break

    number_list.append(int(number))

print("\nThe numbers you entered are:")
for num in number_list:
    print(num)

print("\nThe sum is:", sum(number_list))

total_sum = sum(number_list)
count = len(number_list)
mean = total_sum / count
print(f"The average is {mean}")

biggest_num = max(number_list)
print(f"The biggest number in the list is: {biggest_num}")

smallest_positive_num = min(num for num in number_list if num > 0)

if smallest_positive_num != float('inf'):
    print(f"The smallest positive number is: {smallest_positive_num}")
else:
    print("There are no positive numbers in the list.") 


