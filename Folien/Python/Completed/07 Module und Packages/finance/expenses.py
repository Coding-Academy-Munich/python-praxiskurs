# finance/expenses.py


def add_expense(amount, category):
    return {"amount": amount, "category": category}


def categorize_expense(expense):
    return expense["category"]


def summarize_expenses(expenses):
    summary = {}
    for expense in expenses:
        category = categorize_expense(expense)
        summary[category] = summary.get(category, 0) + expense["amount"]
    return summary
