# finance/income.py


def record_income(amount, source):
    return {"amount": amount, "source": source}


def categorize_income(income):
    return income["source"]
