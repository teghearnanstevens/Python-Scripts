employee_file = open("hr_system.txt")

with open("hr_system.txt") as employee_file:
    for line in employee_file:
        print(line)

employee_only = employee_file.split()

print(employee_file)
print(employee_only)

second = employee_only[1]

print(second)

#with open("hr_system.txt") as f:
#for line in f:
#parts = line.split(" ")
#name = parts[0] title = parts[2]
#print(f"Name: {name}, Title: {title}")