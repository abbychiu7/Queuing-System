from tabulate import tabulate
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


def show_menu():
    menu_items = [
        ["[1]", "Issue ticket"],
        ["[2]", "Serve ticket"],
        ["[3]", "View queue"],
        ["[4]", "View logs"],
        ["[5]", "Generate report summary"],
        ["[0]", "Exit"]
    ]

    # Minimalist display without heavy borders

    print(f"\t\nTicketing System")
    print(tabulate(menu_items, tablefmt="simple", colalign=("center", "left")))

    choice = input(f"Choose a number: ").strip()
    return choice
