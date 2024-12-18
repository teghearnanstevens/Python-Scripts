with open('life-expectancy.csv', 'r') as file:
    lines = file.readlines()

lowest_life_expectancy = float('inf')
highest_life_expectancy = float('-inf')

header_skipped = False

for line in lines:
    if not header_skipped:
        header_skipped = True
        continue
    
    parts = line.strip().split(',')
   
    life_expectancy_str = parts[3]
    
    try:
        life_expectancy = float(life_expectancy_str)
    except ValueError:
        continue
    
    lowest_life_expectancy = min(lowest_life_expectancy, life_expectancy)
    highest_life_expectancy = max(highest_life_expectancy, life_expectancy)

print("Lowest Life Expectancy:", lowest_life_expectancy)
print("Highest Life Expectancy:", highest_life_expectancy)