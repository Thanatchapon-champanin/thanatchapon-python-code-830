import random

def test_random():
    random_number = random.randint(1, 10)
    print(random_number)

    number = int(input("Guess the number(1-10): "))
    
    if random_number > number:
        print("Too low!")
    elif random_number < number:
        print("Too high!")
    else:
        print("Congratulations!")

    print(random_number)

test_random()