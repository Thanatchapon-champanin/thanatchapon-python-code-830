"""
Personal Finance Calculator
Student: Thanatchapon champanin
Date: 26/07/2025
Purpose: Calculate monthly budget and savings
"""
import os
monthly_income = float(input("Enter your monthly income (in THB): "))
if monthly_income <= 0:
    print("monthly income cannot be less than 0")
    exit()
rent_cost = float(input("Enter your rent cost(rent/housing cost): "))
if rent_cost > monthly_income:
    print("Not enough money")
    exit()
food_budget = float(input("Enter your food budget(in THB): "))
transportation_cost = float(input("Enter your transportation cost: "))
entertainment_budget = float(input("Enter your entertainment beudget: "))
emergency_fund_percent = float(input("Enter your emergency fund percent: "))
if emergency_fund_percent < 0 or emergency_fund_percent > 100:
    print("Must be between 0 and 100")
    exit()
investment_percent = float(input("Enter your investment percent: "))
if investment_percent < 0 or investment_percent > 100:
    print("Must be between 0 and 100")
    exit()

Total_Fixed_Expenses = rent_cost + transportation_cost
Total_Variable_Expenses = food_budget + entertainment_budget
Total_Expenses = Total_Fixed_Expenses + Total_Variable_Expenses
Remaining_Income = monthly_income - Total_Expenses
Emergency_Fund_Amount = monthly_income * (emergency_fund_percent /100)
Investment_Amount = monthly_income * (investment_percent /100)
Available_for_Savings = Remaining_Income - (Emergency_Fund_Amount + Investment_Amount)
Expenses_Ratio = (Total_Expenses / monthly_income) * 100
os.system('cls')

print("\t=== MONTHLY BUDGET REPORT ===")
print(f"Income: {monthly_income:.2f} THB")
print(f"Fixed Expenses: {Total_Fixed_Expenses:.2f} THB")
print(f"Variable Expenses: {Total_Variable_Expenses:.2f} THB")
print(f"Total Expenses: {Total_Expenses:.2f} THB")
print(f"Remaining: {Remaining_Income:.2f} THB")

print("\n\t=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({emergency_fund_percent}%): {Emergency_Fund_Amount:.2f} THB")
print(f"Investment ({investment_percent}%): {Investment_Amount:.2f} THB")
print(f"Available for Savings: {Available_for_Savings:.2f} THB")

print("\n\t=== ANALYSIS ===")
print(f"Expense Ratio: {Expenses_Ratio:.2f} %")
