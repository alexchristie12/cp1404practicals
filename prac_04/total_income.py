"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""
import math


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    total_earnings = calculate_cumulative_earnings(incomes)
    print_report(incomes, total_earnings, number_of_months)


def print_report(incomes: list, total_earnings: list, number_of_months: int) -> None:
    """Prints income report"""
    print("\nIncome Report\n-------------")
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total_earning = total_earnings[month - 1]
        print(f"Month {month:2} - Income: #{income:10.2f} Total: ${total_earning:10.2f}")


def calculate_cumulative_earnings(incomes: list) -> list:
    """Calculates the Cumulative Total Earnings from monthly incomes."""
    totals = []
    for i in range(1, len(incomes) + 1):
        totals.append(sum(incomes[:i]))
    return totals


main()
