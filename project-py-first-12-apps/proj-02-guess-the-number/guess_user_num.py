import random


# user's guess
def guess(x):
    random_num = random.randint(1, x)
    guess = 0

    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))

        if guess < random_num:
            print("Too low!")
        elif guess > random_num:
            print("Too high!")

    print(f"You guessed it, the number is {random_num} !!  Alright...")


# user's guess
def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c" and low != high:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(
            f"Is {guess} too high (H), too low (L), or correct (C)? "
        ).lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Wow! The computer guessed your number, {guess}, correctly!")


computer_guess(100)
