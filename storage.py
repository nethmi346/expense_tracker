import json
import os

FILE_PATH = 'expenses.json'

def load_expenses():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r') as file:
        return json.load(file)

def save_expenses(expenses):
    with open(FILE_PATH, 'w') as file:
        json.dump(expenses, file, indent=4)
