from termcolor import colored
from colorama import init
init()

print(colored("Hello", color="yellow", on_color="on_cyan", attrs=["blink"]))