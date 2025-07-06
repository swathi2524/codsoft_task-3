import pickle

# Class to represent a Contact
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

# Function to load contacts from a file
def load_contacts():
    try:
        with open("contacts.dat", "rb") as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return []

# Function to save contacts to a file def save_contacts(contacts):
    with open("contacts.dat", "wb") as file:
        pickle.dump(contacts, file)

# Add a new contact
def add_contact(contacts):
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    address = input("Enter the contact's address: ")

    new_contact = Contact(name, phone, email, address)
    contacts.append(new_contact)
    save_contacts(contacts)
    print("Contact added successfully.")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts saved.")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact}")

# Search contacts by name or phone number
def search_contact(contacts):
    search_term = input("Enter the name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
    
    if found_contacts:
        for contact in found_contacts:
            print(contact)
    else:
        print("No matching contacts found.")

# Update a contact's details
def update_contact(contacts):
    search_term = input("Enter the name or phone number of the contact you want to update: ")
    for contact in contacts:
        if search_term.lower() in contact.name.lower() or search_term in contact.phone:
            print(f"Found contact: {contact}")
            contact.name = input("Enter the new name: ") or contact.name
            contact.phone = input("Enter the new phone number: ") or contact.phone
            contact.email = input("Enter the new email address: ") or contact.email
            contact.address = input("Enter the new address: ") or contact.address
            save_contacts(contacts)
            print("Contact updated successfully.")
            return
    print("Contact not found.")

# Delete a contact
def delete_contact(contacts):
    search_term = input("Enter the name or phone number of the contact to delete: ")
    for contact in contacts:
        if search_term.lower() in contact.name.lower() or search_term in contact.phone:
            print(f"Found contact: {contact}")
            confirm = input("Are you sure you want to delete this contact? (y/n): ").lower()
            if confirm == 'y':
                contacts.remove(contact)
                save_contacts(contacts)
                print("Contact deleted successfully.")
            return
    print("Contact not found.")

# User Interface
def show_menu():
    print("\n--- Contact Management System ---")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Exit")
    return input("Choose an option (1-6): ")

# Main function to run the program
def run_program():
    contacts = load_contacts()

    while True:
        choice = show_menu()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    run_program()
