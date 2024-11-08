# finance/analytics/reports.py


from . import budget  # noqa: F401
from ..expenses import summarize_expenses


def generate_financial_report(incomes, expenses):
    income_summary = sum(income["amount"] for income in incomes)
    expense_summary = summarize_expenses(expenses)
    return {"total_income": income_summary, "expenses_by_category": expense_summary}
