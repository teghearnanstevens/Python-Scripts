from unittest.mock import MagicMock
import pytest
import os
import pandas as pd
from Restate_agents2 import save_agents_csv, clean_agents_csv
import tempfile
import csv

def test_save_agents_csv():
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [30, 25, 35],
        "Role": ["Agent", "Supervisor", "Manager"]
    }
    attributes = ["Name", "Age", "Role"]

    save_agents_csv(data, attributes)

    with open("agents.csv", "r", newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    assert rows[0] == attributes, f"Header row does not match: {rows[0]} != {attributes}"
    
    expected_rows = [
        ["Alice", "30", "Agent"],
        ["Bob", "25", "Supervisor"],
        ["Charlie", "35", "Manager"]
    ]
    assert rows[1:] == expected_rows, f"Data rows do not match: {rows[1:]} != {expected_rows}"


def clean_agents_csv():
    print("Cleaning agent data...")
    if not os.path.exists("agents.csv"):
        print("Error: agents.csv does not exist!")
        return

    
    try:
        df = pd.read_csv("agents.csv")
    except pd.errors.EmptyDataError:
        print("Error: agents.csv is empty!")
        return

    
    df = df.fillna("N/A").replace("", "N/A")

    
    print("Before dropping duplicates:", len(df))
    if "phone" in df.columns:
        df = df.drop_duplicates(subset="phone", keep="first")
    print("After dropping duplicates by phone:", len(df))

    df.drop_duplicates(inplace=True)
    print("After dropping all duplicates:", len(df))
    
    df.to_csv("cleaned_agents.csv", index=False)
    print("Cleaned data saved to cleaned_agents.csv.")


def test_clean_agents_csv():
 
    data = {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "phone": ["123-456", "789-012", "", "123-456", ""],
        "Email": ["alice@example.com", "bob@example.com", "", "david@example.com", ""]
    }
    df = pd.DataFrame(data)
    df.to_csv("agents.csv", index=False)

    clean_agents_csv()

    assert os.path.exists("cleaned_agents.csv"), "cleaned_agents.csv should be created"
    
    cleaned_df = pd.read_csv("cleaned_agents.csv")
    assert len(cleaned_df) == 3, "The cleaned DataFrame should have 4 rows"

    clean_agents_csv()

    assert os.path.exists("cleaned_agents.csv"), "cleaned_agents.csv should still exist after second call"
    
    cleaned_df = pd.read_csv("cleaned_agents.csv")
    assert len(cleaned_df) == 3, "The cleaned DataFrame should still have 4 rows after second call"

    os.remove("agents.csv")
    os.remove("cleaned_agents.csv")

test_clean_agents_csv()









    

pytest.main(["-v", "--tb=line", "-rN", __file__])