import issue_and_serve_ticket as qm
import logger as lg
import menu
import reports
from tabulate import tabulate
from colorama import init, Fore, Style

"""
Submitted by: Group 5
Members (Surnames): Cacanindin, Chiu, and Turla
Subject: APPDAET
"""

# Initialize colorama
init(autoreset=True)

SEPARATOR = "=" * 60
SubSeparator = "=" * 60


def main():
    print(
        f"{Fore.BLUE}{Style.BRIGHT}\n{SEPARATOR}")
    print(
        f"\t\t     Welcome to the Queuing App (FIFO)")
    print(
        f"{Fore.BLUE}{Style.BRIGHT}{SEPARATOR}{Style.RESET_ALL}\n")
    while True:
        choice = menu.show_menu()

        if choice == "1":
            name = input(f"{Fore.CYAN}Enter name: {Style.RESET_ALL}").strip()
            if not name:
                print(f"{Fore.RED}Name is required.{Style.RESET_ALL}\n")
                continue

            if any(char.isdigit() for char in name):
                print(f"{Fore.RED}Name must not contain a number.{Style.RESET_ALL}\n")
                continue

            tid = qm.issue_ticket(name)
            lg.write_log("ISSUE", {"id": tid, "name": name})
            print(f"{Fore.GREEN}Issued ticket #{tid} for {name}{Style.RESET_ALL}\n")

        elif choice == "2":
            served = qm.serve_ticket()
            if served:
                lg.write_log("SERVE", served)
                print(f"{Fore.GREEN}Served ticket #{served['id']} ({served['name']}){Style.RESET_ALL}\n")
            else:
                print(f"{Fore.YELLOW}No tickets to serve.{Style.RESET_ALL}\n")

        elif choice == "3":
            q = qm.get_queue()
            if q:
                table = [[t['id'], t['name']] for t in q]
                print(
                    f"{Fore.BLUE}{Style.BRIGHT}\n{SubSeparator}{Style.RESET_ALL}\nCurrent Queue:\n{Fore.BLUE}{Style.BRIGHT}{SubSeparator}{Style.RESET_ALL}")
                print(tabulate(table, headers=[Fore.CYAN + "Ticket ID" + Style.RESET_ALL,
                                               Fore.CYAN + "Name" + Style.RESET_ALL], tablefmt="fancy_grid"))

            else:
                print(f"{Fore.YELLOW}Queue is empty.{Style.RESET_ALL}\n")

        elif choice == "4":
            logs = lg.read_logs()
            if logs:
                table = [line.strip().split("|") for line in logs]
                print(
                    f"{Fore.BLUE}{Style.BRIGHT}\n{SubSeparator}{Style.RESET_ALL}\nTransaction Logs:{Fore.BLUE}{Style.BRIGHT}\n{SubSeparator}{Style.RESET_ALL}")
                print(tabulate(table, headers=[Fore.CYAN + "Action" + Style.RESET_ALL,
                                               Fore.CYAN + "Details" + Style.RESET_ALL], tablefmt="fancy_grid"))

            else:
                print(f"{Fore.YELLOW}No logs yet.{Style.RESET_ALL}\n")

        elif choice == "5":
            summary = reports.generate_summary()
            table = [
                ["Total Issued", summary['issued']],
                ["Total Served", summary['served']],
                ["Currently in Queue", summary['in_queue']]
            ]
            print(f"{Fore.CYAN}{Style.BRIGHT}\n{SEPARATOR}\nReport Summary:{Style.RESET_ALL}\n{SEPARATOR}")
            print(tabulate(table, tablefmt="fancy_grid"))


        elif choice == "0":
            print(f"{Style.BRIGHT}{SEPARATOR}\nGoodbye!\n{SEPARATOR}{Style.RESET_ALL}")
            break

        else:
            print(f"{Fore.RED}Invalid choice. Please select 0-5.{Style.RESET_ALL}\n")

    print(f"{Style.BRIGHT}Exiting...{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
