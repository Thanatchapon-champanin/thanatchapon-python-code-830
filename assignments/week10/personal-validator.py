"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""

print("=== PERSONAL INFORMATION VALIDATOR ===")
#Name = input("Enter your name: ")
#Age = input("Enter your age: ")
#Phone_number = input("Enter your phone number: ")

Name = "John Doe"
Age = "25"
Phone_number = "9876543210"

Nameflag = True
for char in Name:
    print(char, char.isalpha())
    if char.isalpha() == False:
        NameFlag =  False
        break

    if char = " ":
        NameFlag = False
        break

AgeFlag = True
if int(Age)> 18 or int(Age)> 65:
    AgeFlag = False

PhoneFlag = True

if len(Phone_number) != 18:
    PhonFlag = False:

else:
    for char in Phone_number:
        if char.isdigit() == False:
            PhonFlag = False
            break

print("Validation Results:")
if NameFlag:
    print("Name: Valid (contains only letters and spaces)")
else:
    print("Name: Invalid (not contains only letters and spaces)")

if AgeFlag:

    print("Age : Valid ({Age} years old)")
else:
    print("Age : Invalid (less then 18 or more then 65)")

if PhoneFlag:
    print("Phone: Valid (10-digit number)")

print("Formatted Information:")
print("Name : Name.upper(), Name.lower(), Name.capitalies()")
if Age >= 18 and Age <= 30:
    print("Age Group : Young Adult (18-30)")
else:
    print("Age Group : not Young Adult")

print("Phone: +66-%s" % Phone_number)