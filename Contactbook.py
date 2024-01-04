class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email, address):
        contact = {
            'name': name,
            'phone_number': phone_number,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)
        print(f"Contact {name} added successfully.")

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts in the list.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone_number']}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact['name'].lower() or query in contact['phone_number']]
        if not results:
            print("No matching contacts found.")
        else:
            print("Search Results:")
            for contact in results:
                print(f"Name: {contact['name']}, Phone: {contact['phone_number']}")

    def update_contact(self, name, new_phone_number, new_email, new_address):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                contact['phone_number'] = new_phone_number
                contact['email'] = new_email
                contact['address'] = new_address
                print(f"Contact {name} updated successfully.")
                return
        print(f"Contact {name} not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully.")
                return
        print(f"Contact {name} not found.")

# Example usage:
contact_book = ContactBook()
contact_book.add_contact("John Doe", "123-456-7890", "john.doe@email.com", "123 Main St")
contact_book.add_contact("Jane Smith", "987-654-3210", "jane.smith@email.com", "456 Oak St")
contact_book.view_contact_list()
contact_book.search_contact("John")
contact_book.update_contact("John Doe", "111-222-3333", "john.updated@email.com", "456 New St")
contact_book.view_contact_list()
contact_book.delete_contact("Jane Smith")
contact_book.view_contact_list()
