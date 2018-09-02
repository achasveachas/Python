for num in range(1, 21):
    if num == 4 or num == 13:
        print(f"{num} in unlucky")
    else:
        oddness = "even" if num % 2 == 0 else "odd"
        print (f"{num} is {oddness}")