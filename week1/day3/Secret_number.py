import random

random_number = random.randint(1, 100)
attempts = 0

while attempts <= 8:
    attempts += 1
    if attempts == 9:
        print("You lost!")
        break
    guess = int(input("Guess the number: "))
    if guess == random_number:
        print("You won!!!")
        break
    elif guess < random_number:
        print("Secret number is higher.")
    else:
        print("Secret number is lower.")
