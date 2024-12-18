import datetime
import json
import os

class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, category):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be a positive number.")
        except ValueError as e:
            print("Error:", e)
            return

        transaction = {
            "date": str(datetime.datetime.now()),
            "amount": round(amount, 2),
            "category": category
        }
        self.transactions.append(transaction)
        print("Transaction added successfully.")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions found.")
            return
        for idx, transaction in enumerate(self.transactions, start=1):
            print(f"{idx}. Date: {transaction['date']}, Amount: ${transaction['amount']}, Category: {transaction['category']}")

    def save_transactions(self, filename):
        try:
            with open(filename, 'w') as f:
                json.dump(self.transactions, f, indent=4)
            print(f"Transactions saved to {filename}.")
        except Exception as e:
            print("Error occurred while saving transactions:", e)

    def load_transactions(self, filename):
        if not os.path.exists(filename):
            print(f"File '{filename}' not found.")
            return
        try:
            with open(filename, 'r') as f:
                self.transactions = json.load(f)
            print(f"Transactions loaded from {filename}.")
        except Exception as e:
            print("Error occurred while loading transactions:", e)

# Example usage
def main():
    tracker = FinanceTracker()
    tracker.add_transaction(50, "Groceries")
    tracker.add_transaction(20, "Transportation")
    tracker.view_transactions()
    tracker.save_transactions("transactions.json")
    tracker.load_transactions("transactions.json")

if __name__ == "__main__":
    main()
