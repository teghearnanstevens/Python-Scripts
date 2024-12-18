import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import csv

# Initialize the driver
driver = webdriver.Chrome()

# Function to scrape data and save to agents.csv
def scrape_agents(url, attributes):
    print("Scraping agent data...")
    try:
        driver.get(url)
        WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//*")))
        print("Page loaded successfully.")
    except TimeoutException:
        print("Error: Page load timed out!")
        return

    # Extract data
    data = {attribute: [] for attribute in attributes}
    for attribute in attributes:
        try:
            elements = driver.find_elements(By.XPATH, f"//*[@class='{attribute}' or @id='{attribute}']")
            # Replace empty or missing values with "N/A"
            data[attribute] = [el.text.strip() if el.text.strip() else "N/A" for el in elements]
        except NoSuchElementException:
            print(f"Warning: No elements found for attribute '{attribute}'.")
            data[attribute] = ["N/A"]

    # Ensure all lists in data are the same length
    max_length = max(len(values) for values in data.values())
    for key in data:
        while len(data[key]) < max_length:
            data[key].append("N/A")

    save_agents_csv(data, attributes)

def save_agents_csv(data, attributes):
    with open("agents.csv", "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(attributes)
        for row in zip(*[data[attr] for attr in attributes]):
            writer.writerow(row)
    print("Data saved to agents.csv.")

# Function to check if the CSV file is empty or full
def is_csv_empty(file_path):
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
        return True  # File does not exist or is empty
    else:
        # Check if the file contains only the header row
        with open(file_path, "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            return len(rows) <= 1  # True if only header row or completely empty

# Function to clean data and save to cleaned_agents.csv
def clean_agents_csv():
    print("Cleaning agent data...")
    if not os.path.exists("agents.csv"):
        print("Error: agents.csv does not exist!")
        return

    # Load the CSV file
    try:
        df = pd.read_csv("agents.csv")
    except pd.errors.EmptyDataError:
        print("Error: agents.csv is empty!")
        return

    # Replace missing or empty values with "N/A"
    df = df.fillna("N/A").replace("", "N/A")

    # Drop duplicates based on the "phone" column if it exists
    print("Before dropping duplicates:", len(df))
    if "phone" in df.columns:
        df = df.drop_duplicates(subset="phone", keep="first")
    df.drop_duplicates(inplace=True)

    print("After dropping duplicates:", len(df))
    df.to_csv("cleaned_agents.csv", index=False)
    print("Cleaned data saved to cleaned_agents.csv.")

# Main workflow
def main():
    url = "https://snakerivermls.com/agents"
    attributes = ["rover-img-lazy", "phone", "email"]

    # Check if agents.csv exists and whether it is empty
    if is_csv_empty("agents.csv"):
        print("agents.csv is missing or empty. Scraping data...")
        scrape_agents(url, attributes)
    else:
        print("agents.csv is full. Skipping scraping.")

    # Always clean the data after scraping or skipping
    clean_agents_csv()

if __name__ == "__main__":
    try:
        main()
    finally:
        driver.quit()
