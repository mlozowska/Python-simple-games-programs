
print("Hi, welcome to the quiz about Python!\n")
ans = input("Are you ready to play? (yes/no)\n").strip().lower()
score = 0
total_q = 7

if ans.lower() == 'yes':
    ans = input("1. Who designed Python?").strip()
    if ans == "Guido van Rossum":
        score += 1
        print("Correct\n")
    else:
        print("Incorrect\n")

    ans = input("2. Is Integer a whole number?").strip().lower()
    if ans.lower() == "yes":
        score += 1
        print("Correct\n")
    else:
        print("Incorrect\n")


    ans = input("3. 2.5 is an example of an integer or a float?").strip().lower()
    if ans.lower() == "a float" or "float":
        score += 1
        print("Correct\n")
    else:
        print("Incorrect\n")

    ans = input("4.String is an iterable data type. (true/false)").strip().lower()
    if ans == "true":
        score += 1
        print("Correct\n")
    else:
        print("Incorrect\n")

    ans = input("5. The basic slice format is: variable[end:step:start] (true/false)").strip().lower()
    if ans == "false":
        score += 1
        print("Correct\n")
    else:
        print("Incorrect\n")

    ans = input("6. In logical operators - True and False is... (True/False)").strip().upper()
    if ans.upper() == "False":
        score += 1
        print("Correct\n")
    else:
        print("Incorrect\n")

    ans = input("7. In logical operators - True or False is... (True/False)").strip().upper()
    if ans.upper() == "True":
        score += 1
        print("Correct\n")
    else:
        print("Incorrect\n") \

print(f"Thank you for playing, you got {score} questions correct out of 7")
mark = round((score/total_q) * 100)


print("Mark:", str(mark) + "%\n")
print("Goodbye!")
