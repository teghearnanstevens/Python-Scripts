import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Initialize the driver
driver = webdriver.Chrome()

# Function to scrape agent names and their companies
def scrape_agents_and_companies(url):
    print("Scraping agent names and companies...")
    try:
        # Open the URL and wait for the page to load
        driver.get(url)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "rover-tab-654022-1")))
        print("Page loaded successfully.")

        # Switch to the 'Offices' tab
        offices_tab = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-tab_id='#rover-tab-654022-1']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", offices_tab)
        offices_tab.click()
        print("Navigated to Offices tab successfully.")

        # Wait for the content to load
        WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "office-name")))
        print("Content loaded successfully.")
    except TimeoutException:
        print("Error: Page or tab content load timed out!")
        return []

    # Extract agent names and company names
    scraped_data = []
    try:
        # Find all companies
        company_elements = driver.find_elements(By.CLASS_NAME, "office-name")
        for company in company_elements:
            # Scrape the company name
            company_name = company.text.strip()
            print(f"Company Found: {company_name}")  # Print company names

            # Locate agents under each company
            agent_elements = company.find_elements(By.XPATH, ".//following-sibling::div[@class='rover-one-agent-desc']")
            agents_list = []
            for agent in agent_elements:
                try:
                    # Scrape the agent name
                    agent_name = agent.find_element(By.TAG_NAME, "a").text.strip()
                    agents_list.append(agent_name)
                    print(f"Agent: {agent_name} - Company: {company_name}")  # Debug output
                    # Append to data
                    scraped_data.append({"Agent Name": agent_name, "Company": company_name})
                except NoSuchElementException:
                    continue
            print(f"Agents under {company_name}: {agents_list}")  # Debugging
    except NoSuchElementException:
        print("Warning: Could not find agents or companies.")

    return scraped_data

# Function to update 'agents.csv' with company names
def update_agents_csv(filename, scraped_data):
    # Load existing agents.csv
    if os.path.exists(filename) and os.stat(filename).st_size > 0:
        agents_df = pd.read_csv(filename)
    else:
        print("Error: agents.csv not found or is empty!")
        return

    # Ensure 'Company' column exists
    if "Company" not in agents_df.columns:
        agents_df["Company"] = "N/A"

    # Update 'Company' column based on scraped data
    for row in scraped_data:
        match = agents_df['rover-img-lazy'].str.contains(row['Agent Name'], case=False, na=False)
        print(f"Matching agent: {row['Agent Name']} - Found Matches: {match.sum()}")  # Debugging output
        agents_df.loc[match, 'Company'] = row['Company']

    # Save the updated CSV
    agents_df.to_csv(filename, index=False)
    print("Updated agents.csv saved with company names.")

# Main workflow
def main():
    url = "https://snakerivermls.com/agents/#rover-tab-654022-1"  # Correct URL for 'Offices' tab

    # Scrape agents and companies
    scraped_data = scrape_agents_and_companies(url)

    # Update agents.csv with the scraped data
    update_agents_csv("agents.csv", scraped_data)

if __name__ == "__main__":
    try:
        main()
    finally:
        driver.quit()
