import issue_and_serve_ticket as qm
import logger as lg
import menu
import reports

def main():
    print("Welcome to the Ticketing System (FIFO)")
    while True:
        choice = menu.show_menu()
        if choice == "1":
            name = input("Enter name: ").strip()
            if not name:
                print("Name is required.")
                continue

            if any(char.isdigit() for char in name):
                print("Name must not contain a number.")
                continue
            tid = qm.issue_ticket(name)
            lg.write_log("ISSUE", {"id": tid, "name": name})
            print(f"Issued ticket #{tid} for {name}")
        elif choice == "2":
            served = qm.serve_ticket()
            if served:
                lg.write_log("SERVE", served)
                print(f"Served ticket #{served['id']} ({served['name']})")
            else:
                print("No tickets to serve.")
        elif choice == "3":
            q = qm.get_queue()
            if q:
                print("Current queue:")
                for t in q:
                    print(f" - #{t['id']} ({t['name']})")
            else:
                print("Queue is empty.")
        elif choice == "4":
            logs = lg.read_logs()
            if logs:
                print("Transaction logs:")
                for line in logs:
                    print(line.strip())
            else:
                print("No logs yet.")
        elif choice == "5":
            summary = reports.generate_summary()
            print("\nReport Summary")
            print(f"Total issued: {summary['issued']}")
            print(f"Total served: {summary['served']}")
            print(f"Currently in queue: {summary['in_queue']}")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 0-5.")
    print("Exiting...")

if __name__ == "__main__":
    main()
