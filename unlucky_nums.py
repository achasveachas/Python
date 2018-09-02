for num in range(1, 21):
    state = "even" if num % 2 == 0 else "odd"
    state = "unlucky" if num == 4 or num == 13 else state
    print(f"{num} is {state}")