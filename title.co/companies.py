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

# Function to scrape agent names and their realty groups
def scrape_agents_and_groups(url, group_attributes):
    print("Scraping agent names and their realty groups...")
    try:
        driver.get(url)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "rover-tab-654022-1")))
        print("Page loaded successfully.")
        
        # Wait for the tab to be clickable and click it
        tab_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "rover-tab-654022-1"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", tab_element)  # Scroll into view
        tab_element.click()
        
        # Wait for the correct content to load
        WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "office-summary-content")))
        print("Correct tab content loaded.")
        
    except TimeoutException:
        print("Error: Page or tab content load timed out!")
        return []

    # Extract agent names and group names
    scraped_data = []

    for attribute in group_attributes:
        try:
            elements = driver.find_elements(By.XPATH, f"//*[@class='{attribute}' or @id='{attribute}']")
            for el in elements:
                group_name = el.find_element(By.CSS_SELECTOR, ".office-name").text.strip()
                agent_elements = el.find_elements(By.CSS_SELECTOR, ".agent-name-class")
                for agent_el in agent_elements:
                    agent_name = agent_el.text.strip()
                    if agent_name and group_name:
                        scraped_data.append({"Agent Name": agent_name, "Realty Group": group_name})
        except NoSuchElementException:
            print(f"Warning: No elements found for group attribute '{attribute}'.")

    return scraped_data

# Function to save scraped data to a new CSV file
def save_scraped_data_to_csv(data, filename):
    if data:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"Scraped data saved to {filename}.")
    else:
        print("No data scraped. CSV file was not created.")

# Main workflow
def main():
    url = "https://snakerivermls.com/agents/"
    group_attributes = ["office-summary-content"]  # Updated container class

    # Scrape agent names and their realty groups
    scraped_data = scrape_agents_and_groups(url, group_attributes)

    # Save the scraped data to a new CSV file
    save_scraped_data_to_csv(scraped_data, "scraped_agents_and_groups.csv")

if __name__ == "__main__":
    try:
        main()
    finally:
        driver.quit()
