import os

data_file = "database.txt"


def add_status():
    name = input("Write the name of employee: ")
    work = input("Write what do you do today: ")
    daily_blocker = input("Write the daily blocker: ")

    with open(data_file, "a") as data:
        data.write(f"{name}: {work}: {daily_blocker}\n")
    print("\n Status saved successfully!")


def fetch_status():
    if os.path.exists(data_file):
        print("-----Daily status-----")
        try:
            with open(data_file, "r") as data:
                for line in data:
                    print(line.strip())
        except FileNotFoundError:
            print("The database.txt file does not exist yet. Add a status first.")
    else:
        print(f"Error: the file {data_file} was not found.")


def update_status():
    if not os.path.exists(data_file):
        print("Error: database file not found.")
        return

    confirm = input("WARNING: You are about to modify a record. Continue? (yes/no): ")
    if confirm.lower() != "yes":
        print("Action cancelled.")
        return

    with open(data_file, "r") as data:
        lineas = data.readlines()

    if not lineas:
        print("The file is empty. Nothing to update.")
        return

    for i, linea in enumerate(lineas):
        print(f"{i}: {linea.strip()}")

    try:
        indice = int(input("Enter record number: "))
        if indice < 0 or indice >= len(lineas):
            print("Invalid record number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    name = input("Name: ")
    work = input("Work: ")
    daily_blocker = input("Blocker: ")

    lineas[indice] = f"{name}: {work}: {daily_blocker}\n"

    with open(data_file, "w") as data:
        data.writelines(lineas)

    print("Record updated!")


def delete_status():
    if not os.path.exists(data_file):
        print("Error: database file not found.")
        return

    with open(data_file, "r") as data:
        lineas = data.readlines()

    if not lineas:
        print("The file is empty. Nothing to delete.")
        return

    for i, linea in enumerate(lineas):
        print(f"{i}: {linea.strip()}")

    try:
        indice = int(input("Enter record number to delete: "))
        if indice < 0 or indice >= len(lineas):
            print("Invalid record number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    confirm = input(f"WARNING: You are about to delete record {indice}. This will overwrite the file. Continue? (yes/no): ")
    if confirm.lower() != "yes":
        print("Action cancelled.")
        return

    lineas.pop(indice)

    with open(data_file, "w") as data:
        data.writelines(lineas)

    print("Record deleted!")


def main():
    while True:
        print("\n===== Team Daily Status System =====")
        print("1. Add status")
        print("2. Fetch all statuses")
        print("3. Update a status")
        print("4. Delete a status")
        print("5. Exit")

        option = input("\nSelect an option (1-5): ")

        if option == "1":
            add_status()
        elif option == "2":
            fetch_status()
        elif option == "3":
            update_status()
        elif option == "4":
            delete_status()
        elif option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select a number between 1 and 5.")


main()


# =============================================================================
# STEP 5 - ENGLISH PRACTICE
# =============================================================================

# --- Protocol Selection (3-C Rule: Clear, Concise, Courteous) ---
#
# 1. I will reach out to the team via Slack because it allows immediate
#    communication when a daily blocker is urgent and needs fast resolution.
#
# 2. I will use Email to report a file error when the issue requires
#    formal documentation and the team is working in different time zones.
#
# 3. I will create a Jira ticket to log a blocker that persists over
#    multiple days, so the team can track and prioritize it properly.

# --- Vocabulary Integration ---
#
# This script uses Persistence to ensure that all team status records
# are saved to a text file and remain available even after the program closes.
# The Fetch feature allows users to retrieve and display every stored entry
# directly in the Terminal. Before any modification, the system warns the user
# to prevent an accidental Overwrite of existing data, keeping the records safe.
# Whenever a critical blocker is detected, the team should Reach out immediately
# through the appropriate communication channel to resolve the issue efficiently.
