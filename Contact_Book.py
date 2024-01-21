contacts = {}

def add_contact(name, phone_number, email):
    contacts[name] = {'phone_number': phone_number, 'email': email}
    print(f"Contact {name} added successfully.")

def display_contact(name):
    if name in contacts:
        contact_details = contacts[name]
        print(f"Name: {name}")
        print(f"Phone Number: {contact_details['phone_number']}")
        print(f"Email: {contact_details['email']}")
    else:
        print(f"Contact {name} not found.")

def list_contacts():
    print("Contacts in the Contact Book:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone Number: {details['phone_number']}, Email: {details['email']}")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully****.")
    else:
        print(f"Contact {name} not found.")

# Example usage:
add_contact("Arin Mulla", "123-456-7890", "Arin@example.com \n")
add_contact("Jishan", "987-654-3210 " , "Jishan@example.com \n")

list_contacts()

display_contact("Arin Mulla")
display_contact("Jishan")

delete_contact("Jishan")

list_contacts()



