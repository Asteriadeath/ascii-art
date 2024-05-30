import time
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

with open("ascii_art.txt", "r") as f:
    ascii_art = f.read()
    for line in ascii_art.splitlines():
        for i, char in enumerate(line):
            color = Fore.RED if i % 7 == 0 else Fore.GREEN if i % 7 == 1 else Fore.YELLOW if i % 7 == 2 else Fore.BLUE if i % 7 == 3 else Fore.MAGENTA if i % 7 == 4 else Fore.CYAN if i % 7 == 5 else Fore.WHITE
            print(color + char, end='')
        print()
        time.sleep(0.1)