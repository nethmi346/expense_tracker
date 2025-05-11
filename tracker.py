from storage import load_expenses, save_expenses
from utils import validate_date, validate_month
from collections import defaultdict
from tabulate import tabulate

def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ").strip()
        date_str = input("Enter date (YYYY-MM-DD): ").strip()
        if not validate_date(date_str):
            raise ValueError
    except ValueError:
        print("Invalid input. Please try again.")
        return

    expense = {"amount": amount, "category": category, "date": date_str}
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully.")

def view_expenses(filter_type=None, filter_value=None):
    expenses = load_expenses()
    if filter_type == "category":
        expenses = [e for e in expenses if e['category'].lower() == filter_value.lower()]
    elif filter_type == "date":
        expenses = [e for e in expenses if e['date'] == filter_value]

    if not expenses:
        print("No expenses found.")
        return

    table = [[e['date'], e['category'], f"${e['amount']:.2f}"] for e in expenses]
    print(tabulate(table, headers=["Date", "Category", "Amount"], tablefmt="grid"))

def monthly_summary(month_str):
    if not validate_month(month_str):
        print("Invalid month format. Use YYYY-MM.")
        return

    expenses = load_expenses()
    summary = defaultdict(float)
    for e in expenses:
        if e["date"].startswith(month_str):
            summary[e["category"]] += e["amount"]

    if not summary:
        print("No expenses found for that month.")
        return

    table = [[category, f"${total:.2f}"] for category, total in summary.items()]
    print(f"\nSummary for {month_str}")
    print(tabulate(table, headers=["Category", "Total"], tablefmt="grid"))
