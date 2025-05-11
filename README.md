# Expense Tracker CLI

A simple command-line application to manage your personal expenses.

## 🚀 Features

- Add expenses with amount, category, and date
- View expenses filtered by category or date
- View a monthly summary (total per category)
- Save all data to a file (`expenses.json`)
- Visual summaries and table formatting using `tabulate`

---

## 🛠️ Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/expense-tracker-cli.git
   cd expense-tracker-cli
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   python main.py
   ```

---

## 📦 Requirements

Dependencies are listed in `requirements.txt`. Example:
```
tabulate
```

---

## 📂 File Structure

```
expense_tracker/
├── main.py
├── tracker.py
├── storage.py
├── utils.py
├── expenses.json
├── requirements.txt
└── README.md
```

---

## 🔧 Development

To modify or extend the app:

1. **Add new features** in `tracker.py`, such as budgets or graphs.
2. Use `utils.py` for shared helper functions.
3. Always keep `expenses.json` in a consistent format.
4. After installing any new package, update dependencies with:

```bash
pip freeze > requirements.txt
```

Use good commit messages and test your changes by running:

```bash
python main.py
```

Happy coding!