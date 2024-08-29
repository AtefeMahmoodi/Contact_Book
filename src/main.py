from prettytable import PrettyTable

class ContactBook():
    def __init__(self):
        """Class for creating a contact list with CRUD features
        """
        self.contacts: dict = {}

    def add_contact(self, name: str, phone: str, email: str) -> None:
        """Method to add new contacts

        :param name: Name of the contact. This parameter is unique.
        :param phone: Phone number
        :param email: Email address
        """
        if name not in self.contacts:
            self.contacts[name] = {'phone': phone, 'email': email}
            print("Contact created successfully!")
            return
        print("Contact already exists!")

    def view_contacts(self):
        """Method for viewing all contacts
        """
        table = PrettyTable()
        table.field_names = ["Name", "Phone", "Email"]
        for name, info in self.contacts.items():
            table.add_row([name, info['phone'], info['email']])
        print(table)

    def update_contact(self,name : str, phone: str = None, email: str = None):
        """Method for editting contacts

        :param name: Name of the contact you want to edit
        :param phone: New phone number you want to replace, defaults to None
        :param email: New email address you ant to replace, defaults to None
        """
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            print("Contact updated successfully!")
            return
        print("Contact doesn't exist!")

    def delete_contact(self,name: str):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
            return
        print("Contact doesn't exist!")


if __name__ == "__main__":
    book = ContactBook()

    while True:
        print("\n\n*** Contact Book Application ***")
        print("1. Add Contact.")
        print("2. view Contacts.")
        print("3. Edit Contact.")
        print("4. Delete Contact.")
        print("5. Quit.")
        user_input = input("Please choose an option: ")

        if user_input == "5":
            break

        elif user_input == "1":
            name = input("\n\nPlease enter name: ")
            phone = input("Please enter phone: ")
            email = input("Please enter email: ")
            book.add_contact(name, phone, email)

        elif user_input == "2":
            print("\n\n")
            book.view_contacts()

        elif user_input == "3":
            name = input("\n\nPlease enter the contact name you want to edit: ")
            phone = input("Please enter new phone number: ")
            email = input("Please enter new email address: ")
            book.update_contact(name, phone, email)

        elif user_input == "4":
            name = input("\n\nPlease enter the contact name you want to delete: ")
            book.delete_contact(name)

        else:
            print("\n\nPlease choose from valid options!")

