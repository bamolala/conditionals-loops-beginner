# Ask the user for a number n and print numbers from n down to 1.

user_input = int(input("Enter a number: "))
while user_input >= 1:
    print(user_input)
    user_input = user_input - 1