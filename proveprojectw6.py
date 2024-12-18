with open("life-expectancy.csv") as file: 
    year_desired = input("Enter a desired year: ")
    all_years = []
    single_year = []
    country = []
    all_entities = []
    all_expectancies = []
    # Clean format
    for line in file: 
        fix_line = line.strip()
        fixtwo_line = fix_line.split(",")
        entity = fixtwo_line[0]
        code = fixtwo_line[1]
        year = fixtwo_line[2]
        try:
            expectancy = float(fixtwo_line[3])
        except ValueError:
            print("Error: Invalid data format for life expectancy.")
            continue  # Skip this line and continue with the next one

        # Adds values to separate lists to be referenced in the near future
        all_entities.append(entity)
        all_years.append(year)
        all_expectancies.append(expectancy)
        if year == year_desired:
            single_year.append(expectancy)
            country.append(entity)

# Maxs and Mins for expectancies
max_expectancies = max(all_expectancies)
min_expectancies = min(all_expectancies)
entity_max = all_expectancies.index(max_expectancies)
entity_min = all_expectancies.index(min_expectancies)
relevant_max_year = all_expectancies.index(max_expectancies)
relevant_min_year = all_expectancies.index(min_expectancies)

# Prints
print("\nGeneral Maximums and Minimums: ")
print(f"The entity {all_entities[entity_max]} had an expectancy value of {max_expectancies} in {all_years[relevant_max_year]}")
print(f"The entity {all_entities[entity_min]} had an expectancy value of {min_expectancies} in {all_years[relevant_min_year]}")

# Finds and lists max, min, and average values for the given year
max_year = max(single_year)
min_year = min(single_year)
location_a = single_year.index(max_year)
location_b = single_year.index(min_year)
year_sum = sum(single_year)
single_year_length = len(single_year)
avg = year_sum / single_year_length

# Prints values of specific year of user
print(f"The data for year {year_desired}:")
print(f"The maximum life expectancy was {max_year} in {country[location_a]}")
print(f"The maximum life expectancy was {min_year} in {country[location_b]}")