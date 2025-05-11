from tracker import add_expense, view_expenses, monthly_summary

def main():
    print("Welcome to Expense Tracker CLI")

    while True:
        command = input("\nEnter command (add/view/summary/exit): ").strip().lower()

        if command == "add":
            add_expense()
        elif command.startswith("view"):
            parts = command.split()
            if len(parts) == 3 and parts[1] == "--category":
                view_expenses("category", parts[2])
            elif len(parts) == 3 and parts[1] == "--date":
                view_expenses("date", parts[2])
            else:
                view_expenses()
        elif command.startswith("summary"):
            parts = command.split()
            if len(parts) == 3 and parts[1] == "--month":
                monthly_summary(parts[2])
            else:
                print("Usage: summary --month YYYY-MM")
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
