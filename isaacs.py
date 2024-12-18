# Python 

# Life expectancy data organizer, by Isaac Hammes
# Created 11/23/22

with open("life-expectancy (2).csv") as expct_data:
# Asks the user for a year to search for data in.
    desired_year = (input("Enter a year of interest: "))
    year_list = []
    location_list = []
    all_entities = []
    all_years = []
    all_expectancies = []
# Cleans up the fromatting of and organizes data from each line for use
    for line in expct_data:
        fix_line = line.strip()
        fixtwo_line = fix_line.split(",")
        entity = fixtwo_line[0]
        code = fixtwo_line[1]
        year = fixtwo_line[2]
        expectancy = float(fixtwo_line[3])
# Appends values to seperate lists to be referneced in the future
        all_entities.append(entity)
        all_years.append(year)
        all_expectancies.append(expectancy)
        if year == desired_year:
            year_list.append(expectancy)
            location_list.append(entity)

# Finds the maximum and minimum for expectancies and the correlating years and locations for the whole dataset.
max_expectancies = max(all_expectancies)
min_expectancies = min(all_expectancies)
entity_max = all_expectancies.index(max_expectancies)
relevent_max_year = all_expectancies.index(max_expectancies)
entity_min = all_expectancies.index(min_expectancies)
relevent_min_year = all_expectancies.index(min_expectancies)

# Prints the found data values out  
print("\nGeneral maximums and minimums: ")
print(f"The entity {all_entities[entity_max]} had an expectancy value of {max_expectancies} in {all_years[relevent_max_year]}.")
print(f"The entity {all_entities[entity_min]} had an expectancy value of {min_expectancies} in {all_years[relevent_min_year]}.")

# Finds and lists max, min, and average values for the given year
max_year = max(year_list)
min_year = min(year_list)
location_a = year_list.index(max_year)
location_b = year_list.index(min_year)
year_sum = sum(year_list)
year_list_length = len(year_list)
avg = year_sum / year_list_length

# Prints values of specified year out for user 
print(f"\nThe data for year {desired_year}:")
print(f"The average for all countries was {avg:.2f}.")
print(f"The maximum life expectancy was {max_year} in {location_list[location_a]}.")
print(f"The minimum life expectancy was {min_year} in {location_list[location_b]}.")