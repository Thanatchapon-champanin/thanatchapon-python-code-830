"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""
# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("Thanatchapon", 19, "src", "Thailand")  # name, age, city, country
    hobbies = []
    # Your code here

    while True:
        print("===Menu===")
        print("1. Display")
        print("2. Add new hobbies")
        print("3. Remove hobbies")
        print("4. Update age")
        choice = input("Your choice: ")

        if choice == "1":
            print("Name: ",{person.index[0]})
            print("Age: {person.index[1]}")
            print("City: ",+ {person.index[2]})
            print("Country: ",{person.index[3]})
            print("Hobbise: ",hobbies)
        
        elif choice == "2":
            hobby = input("Your hobby: ")
            hobbies.append[hobby]
            print(hobby)

        elif choice == "3":
            hobby.pop()

        elif choice == "4":
            person_list = list(person)
            age = input("How old are you: ")
            person_list[1] = age
            person = tuple(person_list)

        else:
            break
    