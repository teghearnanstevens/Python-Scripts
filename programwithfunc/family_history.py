name_index = 0
gender_index = 1
birth_year_index = 2
death_year_index = 3

husband_key_index = 0
wife_key_index = 1
wedding_year_index = 2

def main():
    people_dictionary = {
        "P143": ["Lola Park", "F", 1663, 1706],
        "P338": ["Savanna Foster", "F", 1674, 1723],
        "P201": ["Tiffany Hughes", "F", 1689, 1747],
        "P203": ["Ignacio Torres", "M", 1693, 1758],
        "P128": ["Yasmin Li", "F", 1701, 1716],
        "P342": ["Trent Ross", "M", 1705, 1757],
        "P202": ["Samyukta Nguyen", "M", 1717, 1774],
        "P132": ["Joel Johnson", "M", 1724, 1800],
        "P445": ["Whitney Nelson", "F", 1757, 1823],
        "P318": ["Khalid Ali", "M", 1759, 1814],
        "P317": ["Davina Patel", "F", 1775, 1860],
        "P313": ["Enzo Ruiz", "M", 1782, 1782],
        "P475": ["Lauren Smith", "F", 1800, 1802],
        "P455": ["Lucas Ross", "M", 1800, 1853],
        "P435": ["Jamal Gray", "M", 1810, 1831],
        "P204": ["Fatima Soares", "F", 1812, 1898],
        "P206": ["Ephraim Foster", "M", 1831, 1885],
        "P500": ["Peter Price", "M", 1832, 1878],
        "P207": ["Rosalina Jimenez", "F", 1875, 1956],
        "P425": ["Rachel Johnson", "F", 1876, 1940],
        "P121": ["Vanessa Bennet", "F", 1880, 1960],
        "P152": ["Jose Castillo", "M", 1884, 1931],
        "P205": ["Liam Myers", "M", 1902, 1950],
        "P465": ["Isabella Lopez", "F", 1907, 1959],
        "P168": ["Megan Anderson", "F", 1909, 1945]
    }

    marriage_dictionary = {
        "M48": ["P203", "P201", 1711],
        "M45": ["P342", "P338", 1722],
        "M36": ["P203", "P201", 1724],
        "M47": ["P202", "P445", 1774],
        "M21": ["P132", "P445", 1775],
        "M59": ["P132", "P317", 1792],
        "M63": ["P318", "P445", 1804],
        "M12": ["P318", "P317", 1808],
        "M54": ["P435", "P204", 1830],
        "M34": ["P455", "P204", 1853],
        "M55": ["P500", "P317", 1859],
        "M52": ["P206", "P204", 1875],
        "M78": ["P152", "P121", 1905],
        "M50": ["P152", "P425", 1917],
        "M64": ["P205", "P465", 1925],
        "M62": ["P152", "P207", 1925],
        "M70": ["P152", "P168", 1928]
    }

    print_death_age(people_dictionary)
    print()
    count_genders(people_dictionary)
    print()
    print_marriages(marriage_dictionary, people_dictionary)
    print()

def print_death_age(people_dictionary):
    print("Ages at Death")
    for person_key, person_list in people_dictionary.items():
        name = person_list[0]
        birth_year = person_list[2]
        death_year = person_list[3]
        age_at_death = death_year - birth_year
        print(f"{name} was {age_at_death} years old at death.")

def count_genders(people_dictionary):
    male_count = 0
    female_count = 0
    for person_key, person_list in people_dictionary.items():
        gender = person_list[1]
        if gender == "M":
            male_count += 1
        elif gender == "F":
            female_count += 1
    print(f"There are {male_count} males in the people dictionary.")
    print(f"There are {female_count} females in the people dictionary.")

def print_marriages(marriages_dictionary, people_dictionary):
    for marriage_key, marriage_list in marriages_dictionary.items():
        husband_key = marriage_list[0]
        wife_key = marriage_list[1]
        wedding_year = marriage_list[2]
        husband_name = people_dictionary[husband_key][0]
        husband_age = wedding_year - people_dictionary[husband_key][2]
        wife_name = people_dictionary[wife_key][0]
        wife_age = wedding_year - people_dictionary[wife_key][2]
        print(f"{husband_name} married {wife_name} in {wedding_year}.")
        print(f"{husband_name} was {husband_age} years old when married.")
        print(f"{wife_name} was {wife_age} years old when married.")

if __name__ == "__main__":
    main()