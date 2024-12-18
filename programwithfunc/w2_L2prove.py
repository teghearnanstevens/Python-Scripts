import math

width = float(input("Enter the width of the tire in mm (e.g., 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (e.g., 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (e.g., 15): "))

volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

from datetime import datetime 
current_date_and_time = datetime.now()

print(f"The volume of the tire is approximately {volume:.2f} liters.")

with open("volumes.txt", "at") as tire_file:
    print(f"{current_date_and_time}, {width}, {aspect_ratio}, {diameter}, {volume:.2f},", file = tire_file)

print("Volume.txt should be updated with the new information!")

buy_tires = input("Would you like to buy tires with the dimensions entered? (yes/no): ").strip().lower()

if buy_tires == "yes":
   
    phone_num = input("What is your phone number?: ")
    
    with open("volumes.txt", "at") as tire_file:
        tire_file.write(f"Phone number: {phone_num}\n")
    
    print("Thank you! Your phone number has been recorded.")
else:
    print("Have a nice day!")

width = 205  
aspect_ratio = 60  
diameter = 15 

volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

volume

