age = input("How old are you? ")

if age:
    age = int(age)
    if age >= 21:
        print("You are good to go")
    elif age >= 18:
        print("You can enter but you need a writband")
    else:
        print("Sorry, too young")
else:
    print("Please enter an age")