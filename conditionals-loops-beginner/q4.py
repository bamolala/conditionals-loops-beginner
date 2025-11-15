# Ask the user to input a password. Keep asking until they enter the correct password.
user_password = "python123"

user_input = str(input("Enter password: "))
while user_input != user_password:
    print("Wrong password, try again.")
    user_input = str(input("Enter password: "))

print("Password accepted!")