# Ask the user for a score (0–100) and print a grade:
user_score = int(input("Enter score: "))
 
if user_score >= 70 and user_score <= 100:
    print("A")
elif user_score >= 60 and user_score <= 69:
    print("B")
elif user_score >= 50 and user_score <= 59:
    print("C")
elif user_score >= 40 and user_score <= 49:
    print("D")
elif user_score >= 0 and user_score <= 39:
    print("F")