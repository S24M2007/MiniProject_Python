import datetime

def add_log(category, description):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {category}: {description}\n"

    with open("maintenance_logs.txt", "a") as log_file:
        log_file.write(log_entry)

def view_logs():
    try:
        with open("maintenance_logs.txt", "r") as log_file:
            logs = log_file.read()
            print(logs)
    except FileNotFoundError:
        print("No logs found.")

def main():
    while True:
        print("\nMaintenance Log System")
        print("1. Add Log")
        print("2. View Logs")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            category = input("Enter category (PC/Printer/IT Equipment): ")
            description = input("Enter maintenance description: ")
            add_log(category, description)
            print("Log added successfully!")

        elif choice == "2":
            print("\nMaintenance Logs:")
            view_logs()

        elif choice == "3":
            print("Exiting Maintenance Log System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()