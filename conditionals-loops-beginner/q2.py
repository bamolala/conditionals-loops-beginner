# Set a secret number (e.g., 7). Ask the user to guess the number until they get it right.
number = 7

user_guess = int(input("Guess the number: "))
while user_guess != number:
    print("Wrong, try again.")
    user_guess = int(input("Guess the number: "))

print("Correct!")