"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""
direction = input("What's your conversion direction (THB to USD(1),USD to THB(2)) : ")
amount = float(input("Enter the amount: "))
if direction == 1:
    result == amount/ 35.5
    print("Result = ",result,"USD")
else :
    result == amount* 35.5
    print("Result = ",result,"THB")