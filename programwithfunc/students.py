def read_students_file(filename):
    """Read the contents of a CSV file into a dictionary."""
    students = {}
    with open(filename) as file:
        next(file)  # Skip the first line (header)
        for line in file:
            parts = line.strip().split(',')
            i_number = parts[0]
            name = parts[1]
            students[i_number] = name
    return students

def main():
    
    filename = 'students.csv'
    students_dict = read_students_file(filename)
    
    # Get an I-Number from the user
    i_number = input("Enter an I-Number: ").strip()

    # Check if the I-Number exists in the dictionary
    if i_number in students_dict:
        print(f"Student Name: {students_dict[i_number]}")
    else:
        print("No such student")

# Run the program
main()