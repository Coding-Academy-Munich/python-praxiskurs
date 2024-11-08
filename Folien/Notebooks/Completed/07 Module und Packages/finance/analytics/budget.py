# finance/analytics/budget.py

from .. import expenses, income  # noqa: F401


def create_budget(limit):
    return {"limit": limit}


def compare_budget_to_actual(budget, actual):
    total_expenses = sum(expense["amount"] for expense in actual)
    return total_expenses <= budget["limit"]
