import issue_and_serve_ticket as qm
import logger as lg
import menu
import reports
from tabulate import tabulate
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def main():
    print(f"{Fore.MAGENTA}{Style.BRIGHT}Welcome to the Queuing App (FIFO){Style.RESET_ALL}\n")

    while True:
        choice = menu.show_menu()
        print()  # spacing

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
                print(f"{Fore.BLUE}{Style.BRIGHT}Current Queue:{Style.RESET_ALL}")
                print(tabulate(table, headers=[Fore.CYAN + "Ticket ID" + Style.RESET_ALL,
                                               Fore.CYAN + "Name" + Style.RESET_ALL], tablefmt="fancy_grid"))
                print()
            else:
                print(f"{Fore.YELLOW}Queue is empty.{Style.RESET_ALL}\n")

        elif choice == "4":
            logs = lg.read_logs()
            if logs:
                table = [line.strip().split("|") for line in logs]
                print(f"{Fore.BLUE}{Style.BRIGHT}Transaction Logs:{Style.RESET_ALL}")
                print(tabulate(table, headers=[Fore.CYAN + "Action" + Style.RESET_ALL,
                                               Fore.CYAN + "Details" + Style.RESET_ALL], tablefmt="fancy_grid"))
                print()
            else:
                print(f"{Fore.YELLOW}No logs yet.{Style.RESET_ALL}\n")

        elif choice == "5":
            summary = reports.generate_summary()
            table = [
                ["Total Issued", summary['issued']],
                ["Total Served", summary['served']],
                ["Currently in Queue", summary['in_queue']]
            ]
            print(f"{Fore.CYAN}{Style.BRIGHT}Report Summary:{Style.RESET_ALL}")
            print(tabulate(table, tablefmt="fancy_grid"))
            print()

        elif choice == "0":
            print(f"{Style.BRIGHT}Goodbye!{Style.RESET_ALL}")
            break

        else:
            print(f"{Fore.RED}Invalid choice. Please select 0-5.{Style.RESET_ALL}\n")

    print("Exiting...")

if __name__ == "__main__":
    main()
