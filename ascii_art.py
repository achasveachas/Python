from termcolor import colored
from pyfiglet import figlet_format
from random import choice
from colorama import init
init()

msg = input("Hello, what would you like to display? ")
color = input("Which color would you like it in? ")

available_colors = ("red", "yellow", "green", "blue", "magenta", "cyan", "white")
if color not in available_colors:
    color = choice(available_colors)
    

print(colored(figlet_format(msg), color=color))
