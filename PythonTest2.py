def calculate_average(data):
    if not data:
        return None
    return sum(data) / len(data)

# Function to filter and sort data based on user-defined criteria
def filter_and_sort_data(data, min_life_expectancy=None, country=None, start_year=None, end_year=None):
    filtered_data = []
    for year, year_data in data.items():
        if start_year and year < start_year:
            continue
        if end_year and year > end_year:
            continue
        for i, life_expectancy in enumerate(year_data['life_expectancies']):
            if (not min_life_expectancy or life_expectancy >= min_life_expectancy) and \
               (not country or year_data['countries'][i] == country):
                filtered_data.append((year, year_data['countries'][i], life_expectancy))
    filtered_data.sort(key=lambda x: x[2])  # Sort by life expectancy
    return filtered_data

filename = 'life-expectancy.csv'
with open(filename, 'r') as file:
    lines = file.readlines()

life_expectancy_data = {}  
header_skipped = False

for line in lines:
    if not header_skipped:
        header_skipped = True
        continue

    parts = line.strip().split(',')
    
    if len(parts) < 4:  # Check if there are enough elements
        continue
    
    # Validate year
    year_str = parts[0]
    try:
        year = int(year_str)
    except ValueError:
        continue
    
    country = parts[1]
    life_expectancy_str = parts[3]
    
    try:
        life_expectancy = float(life_expectancy_str)
    except ValueError:
        continue
    
    if year not in life_expectancy_data:
        life_expectancy_data[year] = {'countries': [country], 'life_expectancies': [life_expectancy]}
    else:
        life_expectancy_data[year]['countries'].append(country)
        life_expectancy_data[year]['life_expectancies'].append(life_expectancy)

# Allow user to filter and sort the data based on criteria
min_life_expectancy = input("\nEnter minimum life expectancy (leave blank for no filter): ")
country = input("Enter country name (leave blank for no filter): ").strip()
start_year = input("Enter start year (leave blank for no filter): ")
end_year = input("Enter end year (leave blank for no filter): ")

# Convert user inputs to float or int if they are not empty strings
if min_life_expectancy:
    min_life_expectancy = float(min_life_expectancy)
if start_year:
    start_year = int(start_year)
if end_year:
    end_year = int(end_year)

filtered_data = filter_and_sort_data(life_expectancy_data, min_life_expectancy, country, start_year, end_year)

# Display filtered and sorted data
print("\nFiltered and Sorted Data:")
print("Year\tCountry\t\tLife Expectancy")
print("------------------------------------")
for entry in filtered_data:
    print(f"{entry[0]}\t{entry[1]}\t\t{entry[2]}")

# Remaining code for finding lowest and highest life expectancy, calculating average, and prompting user for year input remains unchanged