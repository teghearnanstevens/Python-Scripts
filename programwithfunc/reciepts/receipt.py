import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Reads a CSV file into a dictionary."""
    products_dict = {}
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                key = row[key_column_index]
                value = [row[0], row[1], float(row[2])]
                products_dict[key] = value
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        raise 
    except IndexError:
        print("Error: The file has an incorrect format.")
        raise
    return products_dict

def main():
    """Generates a receipt based on product and request CSV files."""
    TAX_RATE = 0.06  

    try:
       
        products_dict = read_dictionary("products.csv", 0)

        print("Inkom Emporium\n")
        total_items = 0
        subtotal = 0

        
        try:
            with open("request.csv", "r") as file:
                reader = csv.reader(file)
                next(reader)  

                for row in reader:
                    product_number = row[0]
                    quantity = int(row[1])

                    try:
                      
                        product = products_dict[product_number]
                        product_name = product[1]
                        product_price = product[2]

                        
                        total_items += quantity
                        subtotal += quantity * product_price

                        
                        print(f"{product_name}: {quantity} @ {product_price:.2f}")
                    except KeyError:
                        print(f"Error: Product number '{product_number}' not found in products_dict.")

        except FileNotFoundError:
            print("Error: The file 'request.csv' was not found.")
            return

       
        sales_tax = subtotal * TAX_RATE
        total = subtotal + sales_tax

        print(f"\nNumber of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}\n")

       
        print("Thank you for shopping at the Inkom Emporium.")
        print(datetime.now().strftime("%a %b %d %H:%M:%S %Y"))

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
