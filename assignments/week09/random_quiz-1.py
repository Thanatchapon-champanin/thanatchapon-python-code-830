"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""
import random

def test_random():
    random_number = random.randint(1, 10)
    print(random_number)
    print("You have 6 round")
    for i in range(6):
        print(f"Round {i+1}")
        i += 1  
        number = int(input(f"Guess the number(1-10): "))
    
        if random_number > number:
            print("Too low!")
        elif random_number < number:
            print("Too hight!")
        else:
            print("Congratulations! You won in ",{i} ,"attempts!")
            break
        
    print("Answer :",random_number)
test_random()