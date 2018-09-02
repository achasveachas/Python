from random import randint
TOKENS = ['rock', 'paper', 'scissors']

p1 = input("Player one input: ").lower()
p2 = TOKENS[randint(0,2)]
print(f"Computer chose {p2}")

if p1 == p2:
    print("Draw")
elif p1 == "rock" and p2 == "scissors":
    print("p1 wins")
elif p1 == "paper" and p2 == "rock":
    print("p1 wins")
elif p1 == "scissors" and p2 == "paper":
    print("p1 wins")
else:
    print("Computer wins")