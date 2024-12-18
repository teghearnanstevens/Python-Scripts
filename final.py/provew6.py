def calculate_average(data):
    if not data:
        return None
    return sum(data) / len(data)

with open('life-expectancy.csv', 'r') as file:
    lines = file.readlines()

lowest_life_expectancy = float('inf')
lowest_life_expectancy_year = None
lowest_life_expectancy_country = None

highest_life_expectancy = float('-inf')
highest_life_expectancy_year = None
highest_life_expectancy_country = None

life_expectancy_data = {}

header_skipped = False

for line in lines:
    if not header_skipped:
        header_skipped = True
        continue
    
    parts = line.strip().split(',')
   
    if len(parts) < 4:  # Check if there are enough elements
        continue

    try:
        year = int(parts[0])
        country = parts[1]
        life_expectancy = float(parts[3])
    except ValueError:
        continue
    
    # Update lowest life expectancy
    if life_expectancy < lowest_life_expectancy:
        lowest_life_expectancy = life_expectancy
        lowest_life_expectancy_year = year
        lowest_life_expectancy_country = country
    
    # Update highest life expectancy
    if life_expectancy > highest_life_expectancy:
        highest_life_expectancy = life_expectancy
        highest_life_expectancy_year = year
        highest_life_expectancy_country = country
    
    # Store life expectancy data by year
    if year not in life_expectancy_data:
        life_expectancy_data[year] = {'countries': [country], 'life_expectancies': [life_expectancy]}
    else:
        life_expectancy_data[year]['countries'].append(country)
        life_expectancy_data[year]['life_expectancies'].append(life_expectancy)

print("Year and Country with the Lowest Life Expectancy:")
print("Year:", lowest_life_expectancy_year)
print("Country:", lowest_life_expectancy_country)
print("Lowest Life Expectancy:", lowest_life_expectancy)

print("\nYear and Country with the Highest Life Expectancy:")
print("Year:", highest_life_expectancy_year)
print("Country:", highest_life_expectancy_country)
print("Highest Life Expectancy:", highest_life_expectancy)

user_input_year = input("\nEnter a year to find the average life expectancy for that year: ")
if user_input_year.isdigit():  # Check if input is a valid integer
    user_input_year = int(user_input_year)
    if user_input_year in life_expectancy_data:
        average_life_expectancy = calculate_average(life_expectancy_data[user_input_year]['life_expectancies'])
        min_life_expectancy_country = life_expectancy_data[user_input_year]['countries'][life_expectancy_data[user_input_year]['life_expectancies'].index(min(life_expectancy_data[user_input_year]['life_expectancies']))]
        max_life_expectancy_country = life_expectancy_data[user_input_year]['countries'][life_expectancy_data[user_input_year]['life_expectancies'].index(max(life_expectancy_data[user_input_year]['life_expectancies']))]
        print(f"\nAverage Life Expectancy for {user_input_year}: {average_life_expectancy:.2f}")
        print(f"Country with Minimum Life Expectancy: {min_life_expectancy_country}")
        print(f"Country with Maximum Life Expectancy: {max_life_expectancy_country}")
    else:
        print("Year not found in the dataset.")
else:
    print("Invalid input. Please enter a valid year.")