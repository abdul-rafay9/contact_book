#  Add a new contact.
# - Display all contacts.
# - Search for a contact by name.
# - Delete a contact by name.
#

import json
import os

file_path = "contacts List.json"


def add_contact():
    contacts = {}
    while True:
        print("\nAap kn see country ka contact add karna chatea hai:"
              "\n1.Pakistan"
              "\n2.India"
              "\n3.Dubai"
              "\n4.Sudia"
              "\n5.Back to main 'Menu' ")

        choice = input("Enter your choice: ")

        if choice == "1":
            key = input("Enter contact owner name: ")
            value = input(f"Enter {key} contact number :+92 ")
            contacts[key] = "+92"  + value  # Prefix the country code
            print("Your Contact Added Successfully!")

        elif choice == "2":
            key = input("Enter contact owner name: ")
            value = input(f"Enter {key} contact number :+91 ")
            contacts[key] = "+91"  + value
            print("Your Contact Added Successfully!")

        elif choice == "3":
            key = input("Enter contact owner name: ")
            value = input(f"Enter {key} contact number :+971 ")
            contacts[key] = "+971"  + value
            print("Your Contact Added Successfully!")

        elif choice == "4":
            key = input("Enter contact owner name: ")
            value = input(f"Enter {key} contact number :+966 ")
            contacts[key] = "+966"  + value
            print("Your Contact Added Successfully!")

        elif choice == "5":
            print("Back to main Menu")
            break

        else:
            print("Please Select Correct Choice!")

    if contacts:  # O1nly append if contacts are not empty
        if os.path.exists(file_path):
            # Load JSON data from file
            with open(file_path, 'r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []  # Initialize as empty list if JSON is invalid
        else:
            data = []

        data.append(contacts)

        # Write updated data back to the file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

        print("Entry added successfully!")


def show_contact():
    if not os.path.exists(file_path):
        print("File Not Found! Please enter contact first.")
        return
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            print("Contacts Detail:")
            print(json.dumps(data, indent=4))
        except json.JSONDecodeError:
            print("Error reading contacts. File may be corrupt or empty.")


def find_contacts():
    if not os.path.exists(file_path):
        print("File Not Found! Please enter contact first.")
        return

    key = input("Enter owner name to search: ")

    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            print("Error reading contacts. File may be corrupt or empty.")
            return

    found = False

    for contact in data:
        if key in contact:
            print("Contact is found")
            print(f"Owner: {key}, Contact Number: {contact[key]}")
            found = True
            break

    if not found:
        print(f"Wrong name {key}! Enter correct owner name.")


def delete_contact():
    if not os.path.exists(file_path):
        print("File Not Found! Please enter contact first.")
        return

    key = input("Enter owner name to delete: ")

    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            print("Error reading contacts. File may be corrupt or empty.")
            return

    initial_length = len(data)
    data = [contact for contact in data if key not in contact]

    if len(data) < initial_length:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Contact {key} deleted successfully!")
    else:
        print(f"Contact with name {key} not found.")


while True:
    print("\nMenu")
    print("1.Add a new contact.")
    print("2.Display all contacts.")
    print("3.Search for a contact by name.")
    print("4.Delete a contact by name.")
    print("5.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        show_contact()

    elif choice == "3":
        find_contacts()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        print("\n\t\tHave a nice day!")
        break

    else:
        print("Invalid Action!\nPlease select correct choice.")
