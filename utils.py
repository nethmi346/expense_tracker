from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_month(month_str):
    try:
        datetime.strptime(month_str, "%Y-%m")
        return True
    except ValueError:
        return False
