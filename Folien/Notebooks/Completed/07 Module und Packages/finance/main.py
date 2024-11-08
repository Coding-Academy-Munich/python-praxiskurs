from .analytics.budget import compare_budget_to_actual, create_budget
from .analytics.reports import generate_financial_report
from .expenses import add_expense
from .income import record_income


def record_income_and_expenses():
    incomes = [
        record_income(5000, "Salary"),
        record_income(200, "Interest"),
    ]
    expenses = [
        add_expense(100, "Groceries"),
        add_expense(150, "Utilities"),
        add_expense(200, "Rent"),
    ]
    return incomes, expenses


def print_report(incomes, expenses):
    report = generate_financial_report(incomes, expenses)
    print("Financial Report:", report)


def analyze_budget(expenses):
    budget = create_budget(500)
    is_within_budget = compare_budget_to_actual(budget, expenses)
    print("Is within budget:", is_within_budget)


def main():
    incomes, expenses = record_income_and_expenses()
    print_report(incomes, expenses)
    analyze_budget(expenses)


if __name__ == "__main__":
    main()
