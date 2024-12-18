from datetime import datetime

def main():
    
    gender = input("Enter your gender (f for female, m for male): ").lower()
    birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
    weight_lbs = float(input("Enter your weight in lbs: "))
    height_in = float(input("Enter your height in inches: "))

    if gender != "m" and gender != "f":
        print("Invalid input. Please enter 'f' for female or 'm' for male.")
        return
    if birth_str > datetime.now().strftime("%Y-%m-%d"):
        print("Invalid input. Birthdate cannot be in the future.")
        return
    if weight_lbs <= 0:
        print("Invalid input. Weight must be greater than 0.")
        return
    if height_in <= 0:
        print("Invalid input. Height must be greater than 0.")
        return

    age = compute_age(birth_str)
    weight_kg = kg_from_lb(weight_lbs)
    height_cm = cm_from_in(height_in)
    bmi = body_mass_index(weight_kg, height_cm / 100)  
    bmr = basal_metabolic_rate(gender, weight_kg, height_cm, age)

    
    print(f"Age: {age} years")
    print(f"Weight: {weight_kg:.2f} kg")
    print(f"Height: {height_cm:.2f} cm")
    print(f"Body Mass Index (BMI): {bmi:.2f}")
    print(f"Basal Metabolic Rate (BMR): {bmr:.2f} kcal/day")

def compute_age(birth_str):
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()  
    years = today.year - birthdate.year
    if birthdate.month > today.month or (birthdate.month == today.month and birthdate.day > today.day):
        years -= 1
    return years

def kg_from_lb(pounds):
    return pounds * 0.45359237

def cm_from_in(inches):
    return inches * 2.54

def body_mass_index(weight, height):
    return weight / (height * height)

def basal_metabolic_rate(gender, weight, height, age):
    if gender == "m":
        return 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
    elif gender == "f":
        return 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)


main()